#!/usr/bin/env python3
"""
importar_pacote.py — importa o pacote diário de dados brutos que vem da máquina principal.

Roda na máquina do João. NÃO chama API nenhuma: só lê o zip e copia arquivos.

Uso:
  python3 scripts/pacote/importar_pacote.py ~/Downloads/pacote-2026-10-13.zip
  python3 scripts/pacote/importar_pacote.py ZIP --destino /caminho/do/projeto   # outro projeto (teste)
  python3 scripts/pacote/importar_pacote.py ZIP --forcar                       # aceita pacote mais velho que o último importado

O que faz, nesta ordem:
  1. Abre o zip e confere o sha256 de cada arquivo contra o checksums.txt. Qualquer
     divergência, arquivo faltando ou arquivo a mais = nada é copiado.
  2. Copia analise/* para conteudo/analise/ (substitui os arquivos de mesmo nome), com
     duas exceções de nome:
       registro-posts-factual.csv -> conteudo/analise/_registro-maquina-user.csv
       MANIFESTO.md               -> conteudo/analise/_pacote-MANIFESTO.md
     O registro-posts.csv daqui NUNCA é tocado.
  3. Copia posts/<pasta>/ para conteudo/carrosseis/_da-maquina-do-user/<pasta>/.
  4. Anota a importação (ou a recusa) em conteudo/analise/_pacotes-importados.log.

Só entram os nomes de arquivo da lista abaixo; qualquer outro arquivo do zip é ignorado
e anotado no log. Nada é apagado.
"""

import argparse
import datetime as dt
import hashlib
import json
import os
import re
import socket
import sys
import tempfile
import zipfile

try:
    from zoneinfo import ZoneInfo
    BRT = ZoneInfo("America/Sao_Paulo")
except Exception:
    BRT = dt.timezone(dt.timedelta(hours=-3))

AQUI = os.path.dirname(os.path.abspath(__file__))
REPO_PADRAO = os.path.abspath(os.path.join(AQUI, "..", ".."))

# nome no pacote (analise/...) -> caminho no projeto
ANALISE = {
    "desempenho.json": "conteudo/analise/desempenho.json",
    "desempenho.csv": "conteudo/analise/desempenho.csv",
    "_snapshots.csv": "conteudo/analise/_snapshots.csv",
    "leads.json": "conteudo/analise/leads.json",
    "_disparos.json": "conteudo/analise/_disparos.json",
    "_painel-instagram.csv": "conteudo/analise/_painel-instagram.csv",
    "_update.log": "conteudo/analise/_update.log",
    "_pull.log": "conteudo/analise/_pull.log",
    "registro-posts-factual.csv": "conteudo/analise/_registro-maquina-user.csv",
}
RAIZ_ARQUIVOS = {
    "MANIFESTO.md": "conteudo/analise/_pacote-MANIFESTO.md",
}
TEXTOS_POST = {"carousel-text.md", "legenda.txt"}
PASTA_POSTS = "conteudo/carrosseis/_da-maquina-do-user"
PROTEGIDO = "conteudo/analise/registro-posts.csv"
LOG = "conteudo/analise/_pacotes-importados.log"
PASTA_OK = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


def agora():
    return dt.datetime.now(BRT).strftime("%Y-%m-%d %H:%M")


def h_maquina():
    return hashlib.sha256(("tatsuo-pacote|" + socket.gethostname()).encode()).hexdigest()[:16]


def h_repo(path):
    return hashlib.sha256(("tatsuo-pacote|" + os.path.realpath(path)).encode()).hexdigest()[:16]


def anotar(destino, linha):
    p = os.path.join(destino, LOG)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "a", encoding="utf-8") as f:
        f.write(linha + "\n")


def recusar(destino, zip_nome, motivo, gravar_log=True):
    if gravar_log:
        anotar(destino, f"{agora()} | recusado | {zip_nome} | {motivo}")
    sys.exit(f"RECUSADO: {motivo}\nNada foi copiado.")


def ultimo_importado(destino):
    """gerado_em do pacote mais recente já importado (lido do log)."""
    p = os.path.join(destino, LOG)
    if not os.path.exists(p):
        return None
    ult = None
    for ln in open(p, encoding="utf-8"):
        partes = [x.strip() for x in ln.split("|")]
        if len(partes) >= 4 and partes[1] == "importado" and partes[3].startswith("gerado_em "):
            g = partes[3][len("gerado_em "):]
            if ult is None or g > ult:
                ult = g
    return ult


def ler_zip(caminho):
    """Lê o zip inteiro para a memória, validando nomes. Devolve (raiz, {rel: bytes})."""
    try:
        z = zipfile.ZipFile(caminho)
    except (zipfile.BadZipFile, OSError) as e:
        return None, None, f"zip ilegível ({e})"
    conteudo, raizes = {}, set()
    with z:
        for info in z.infolist():
            nome = info.filename
            if nome.endswith("/"):
                continue
            if nome.startswith("/") or "\\" in nome or ".." in nome.split("/"):
                return None, None, f"caminho perigoso dentro do zip: {nome}"
            if (info.external_attr >> 16) & 0o170000 == 0o120000:
                return None, None, f"link simbólico dentro do zip: {nome}"
            partes = nome.split("/", 1)
            if len(partes) != 2 or not partes[1]:
                return None, None, f"arquivo fora da pasta do pacote: {nome}"
            raizes.add(partes[0])
            conteudo[partes[1]] = z.read(info)
    if len(raizes) != 1:
        return None, None, f"o zip devia ter uma pasta só na raiz, tem {sorted(raizes)}"
    return raizes.pop(), conteudo, None


def conferir(conteudo):
    if "checksums.txt" not in conteudo:
        return "sem checksums.txt"
    esperado = {}
    for ln in conteudo["checksums.txt"].decode("utf-8").splitlines():
        if not ln.strip():
            continue
        m = re.match(r"^([0-9a-f]{64})  (.+)$", ln)
        if not m:
            return f"linha inválida no checksums.txt: {ln[:80]}"
        esperado[m.group(2)] = m.group(1)
    presentes = set(conteudo) - {"checksums.txt"}
    faltando = sorted(set(esperado) - presentes)
    sobrando = sorted(presentes - set(esperado))
    if faltando:
        return f"listados no checksums.txt e ausentes no zip: {faltando[:5]}"
    if sobrando:
        return f"no zip e fora do checksums.txt: {sobrando[:5]}"
    ruins = [rel for rel, h in esperado.items() if hashlib.sha256(conteudo[rel]).hexdigest() != h]
    if ruins:
        return f"sha256 não confere em {len(ruins)} arquivo(s): {sorted(ruins)[:5]}"
    return None


def plano(conteudo):
    """Decide destino de cada arquivo pelas regras daqui (nunca pelo que o pacote diz)."""
    copiar, ignorados = [], []
    for rel in sorted(conteudo):
        if rel in ("checksums.txt", "pacote.json"):
            continue
        if rel in RAIZ_ARQUIVOS:
            copiar.append((rel, RAIZ_ARQUIVOS[rel]))
            continue
        partes = rel.split("/")
        if len(partes) == 2 and partes[0] == "analise" and partes[1] in ANALISE:
            copiar.append((rel, ANALISE[partes[1]]))
        elif (len(partes) == 3 and partes[0] == "posts" and PASTA_OK.match(partes[1])
              and partes[2] in TEXTOS_POST):
            copiar.append((rel, f"{PASTA_POSTS}/{partes[1]}/{partes[2]}"))
        else:
            ignorados.append(rel)
    for _, dst in copiar:
        if dst == PROTEGIDO:  # cinto e suspensório: o registro daqui não se toca
            raise SystemExit("erro interno: plano tentou escrever no registro-posts.csv")
    return copiar, ignorados


def gravar(destino, dst_rel, dados):
    final = os.path.join(destino, dst_rel)
    os.makedirs(os.path.dirname(final), exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=os.path.dirname(final), prefix=".importando-")
    with os.fdopen(fd, "wb") as f:
        f.write(dados)
    os.chmod(tmp, 0o644)  # mkstemp nasce 600; os arquivos do projeto são 644
    os.replace(tmp, final)


def main():
    ap = argparse.ArgumentParser(description="Importa o pacote diário de dados brutos (zero API).")
    ap.add_argument("zip", help="caminho do pacote-AAAA-MM-DD.zip")
    ap.add_argument("--destino", help="raiz do projeto que recebe (padrão: o projeto onde este script está)")
    ap.add_argument("--forcar", action="store_true",
                    help="aceita pacote gerado antes do último já importado")
    args = ap.parse_args()

    destino = os.path.abspath(os.path.expanduser(args.destino or REPO_PADRAO))
    zip_path = os.path.abspath(os.path.expanduser(args.zip))
    zip_nome = os.path.basename(zip_path)
    if not os.path.isdir(os.path.join(destino, "conteudo")):
        sys.exit(f"{destino} não parece o projeto (não tem a pasta conteudo/). Nada foi copiado.")
    if not os.path.isfile(zip_path):
        sys.exit(f"Não achei o zip: {zip_path}")

    # Até saber que o destino não é o projeto que gerou o pacote, nada é escrito nele (nem o log).
    raiz, conteudo, erro = ler_zip(zip_path)
    if erro:
        recusar(destino, zip_nome, erro, gravar_log=False)
    try:
        meta = json.loads(conteudo["pacote.json"].decode("utf-8"))
    except Exception as e:
        recusar(destino, zip_nome, f"pacote.json ausente ou ilegível ({e})", gravar_log=False)
    gerado = meta.get("gerado_em", "?")

    # A máquina principal é a fonte da verdade: nada de fora entra nela, nem o próprio pacote.
    if meta.get("origem_repo") == h_repo(destino) and meta.get("origem_maquina") == h_maquina():
        recusar(destino, zip_nome, "este é o projeto que GEROU o pacote (máquina principal); importar aqui é proibido",
                gravar_log=False)

    erro = conferir(conteudo)
    if erro:
        recusar(destino, zip_nome, f"checksums: {erro}")

    ult = ultimo_importado(destino)
    if ult and gerado < ult and not args.forcar:
        recusar(destino, zip_nome, f"pacote gerado em {gerado}, mais velho que o último importado ({ult}); "
                                   "use --forcar se for de propósito")

    copiar, ignorados = plano(conteudo)
    for rel, dst in copiar:
        gravar(destino, dst, conteudo[rel])

    n_analise = sum(1 for rel, _ in copiar if rel.startswith("analise/"))
    pastas = sorted({rel.split("/")[1] for rel, _ in copiar if rel.startswith("posts/")})
    n_textos = sum(1 for rel, _ in copiar if rel.startswith("posts/"))
    linha = (f"{agora()} | importado | {zip_nome} | gerado_em {gerado} | "
             f"{n_analise} arquivos de analise, {n_textos} textos de {len(pastas)} posts | checksums ok")
    if ignorados:
        linha += f" | ignorados: {', '.join(ignorados)}"
    anotar(destino, linha)

    print(f"Importado: {zip_nome} (gerado em {gerado}) -> {destino}")
    for rel, dst in copiar:
        if not rel.startswith("posts/"):
            info = (meta.get("arquivos") or {}).get(rel, {})
            extra = f"  [coleta {info.get('coleta')}; {info.get('registros')}]" if info else ""
            print(f"  {rel:40} -> {dst}{extra}")
    print(f"  posts: {n_textos} textos de {len(pastas)} pastas -> {PASTA_POSTS}/")
    if ignorados:
        print(f"  ignorados (fora da lista): {', '.join(ignorados)}")
    print(f"  {PROTEGIDO}: não tocado")
    print(f"  log: {LOG}")

    # A API da Meta não pode rodar em duas máquinas: avisa se esta tiver o que precisa pra isso.
    sinais = [p for p in ("~/.tatsuo/ig-token.json", "~/Library/LaunchAgents/com.tatsuo.ig-update.plist")
              if os.path.exists(os.path.expanduser(p))]
    if sinais and meta.get("origem_maquina") != h_maquina():
        print("\nATENÇÃO: esta máquina tem " + " e ".join(sinais) + ". A API do Instagram só roda na máquina "
              "principal; aqui o dado chega pelo pacote. Desligar isso com o user antes de seguir.")


if __name__ == "__main__":
    main()
