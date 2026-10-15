#!/usr/bin/env python3
"""
validar_fontes.py — o guarda-corpo de PROCEDÊNCIA do dado.

Por que existe (02/09/2026). Num único ritual eu cometi três erros, e os três
eram o mesmo erro: comparar números sem auditar se eram comparáveis.
  1. chamei um post de "o maior evento de lead da história" sem olhar o histórico;
  2. reportei "zero lead" de um post de 31/08 lendo um CRM puxado ANTES dele existir;
  3. gravei um link como "sem UTM" sem ter aberto o link.

Nenhum é erro de estatística — os testes estavam certos. É erro de não perguntar
"de quando é esse número e o que ele cobre". O `validar_registro.py` já provou que
essa classe de falha se resolve com script, não com boa intenção: depois que ele
passou a barrar ficha desalinhada, nunca mais passou uma.

O que este script faz, e que nenhum outro fazia:
  A. carimba TODA fonte com a data dela e diz há quanto tempo foi lida;
  B. BLOQUEIA a leitura de um post contra uma fonte anterior à publicação dele
     — o buraco não é resultado, é ausência de medição;
  C. avisa quando uma fonte está velha demais pro que ela mede;
  D. imprime a BASE DE ORDENAÇÃO (n e janela) que qualquer superlativo precisa citar.

Zero chamada de API: lê só o disco.

Saída: exit 0 se tudo limpo, 1 se há BLOQUEIO. Avisos não travam.
"""

import csv
import json
import os
import sys
from datetime import datetime, timedelta

RAIZ = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
AN = os.path.join(RAIZ, "conteudo", "analise")

# Idade máxima aceitável por fonte, em horas, e o porquê de cada teto.
TETOS = {
    "instagram": (24, "o launchd roda 9h/14h/20h + boot; >24h significa Mac desligado o dia todo"),
    "crm": (24, "lead entra a qualquer hora; CRM velho faz post novo parecer que não converteu"),
    "manychat": (48, "leitura é manual, não há API; 48h é o intervalo tolerável entre rituais"),
    "snapshots": (36, "a foto do dia é insubstituível — valores são acumulados de vida"),
}


def _agora():
    return datetime.now()


def _parse(s, fmts=("%Y-%m-%d %H:%M", "%Y-%m-%d %H:%M:%S", "%Y-%m-%d")):
    s = (s or "").strip()
    for f in fmts:
        try:
            return datetime.strptime(s, f)
        except ValueError:
            continue
    return None


def _idade_h(dt):
    return (_agora() - dt).total_seconds() / 3600


def _fmt_idade(h):
    if h < 1:
        return f"{int(h*60)} min"
    if h < 48:
        return f"{h:.1f}h"
    return f"{h/24:.1f} dias"


def carregar_fontes():
    """Cada fonte vira {nome, carimbo (datetime), cobre_ate (date), detalhe}."""
    fontes = {}

    p = os.path.join(AN, "desempenho.json")
    if os.path.exists(p):
        d = json.load(open(p))
        ts = _parse(d.get("pulled_at"))
        fontes["instagram"] = {
            "arquivo": "desempenho.json",
            "carimbo": ts,
            # métrica de post é acumulada de vida: o pull cobre tudo até o instante do pull
            "cobre_ate": ts,
            "detalhe": f"{d.get('count', '?')} posts",
        }

    p = os.path.join(AN, "leads.json")
    if os.path.exists(p):
        d = json.load(open(p))
        ts = _parse(d.get("pulled_at"))
        fontes["crm"] = {
            "arquivo": "leads.json",
            "carimbo": ts,
            "cobre_ate": ts,
            "detalhe": (f"{d.get('total_contatos', '?')} contatos · janela "
                        f"{d.get('janela_dias', '?')}d"),
        }

    p = os.path.join(AN, "_disparos.json")
    if os.path.exists(p):
        d = json.load(open(p))
        ts = _parse(d.get("_lido_em"))
        palavras = [k for k in d if not k.startswith("_")]
        fontes["manychat"] = {
            "arquivo": "_disparos.json",
            "carimbo": ts,
            "cobre_ate": ts,
            "detalhe": f"{len(palavras)} palavras lidas no painel",
            "palavras": set(palavras),
        }

    p = os.path.join(AN, "_snapshots.csv")
    if os.path.exists(p):
        datas = sorted({r["data_snapshot"] for r in csv.DictReader(open(p))})
        ts = _parse(datas[-1]) if datas else None
        # a foto é tirada de manhã; para efeito de cobertura vale o dia inteiro
        fontes["snapshots"] = {
            "arquivo": "_snapshots.csv",
            "carimbo": ts,
            "cobre_ate": ts,
            "detalhe": f"{len(datas)} dias de foto · da {datas[0]} à {datas[-1]}" if datas else "vazio",
            "dias": set(datas),
        }

    return fontes


def checar_frescor(fontes):
    linhas, avisos = [], []
    for nome, f in fontes.items():
        if not f["carimbo"]:
            avisos.append(f"{nome} ({f['arquivo']}): sem carimbo de data legível — "
                          f"não dá pra saber se está fresco")
            linhas.append((nome, f["arquivo"], "SEM CARIMBO", "?", f["detalhe"]))
            continue
        h = _idade_h(f["carimbo"])
        teto, motivo = TETOS.get(nome, (72, ""))
        status = "ok" if h <= teto else "VELHO"
        if status == "VELHO":
            avisos.append(f"{nome} ({f['arquivo']}) tem {_fmt_idade(h)} — teto é {teto}h. {motivo}")
        linhas.append((nome, f["arquivo"],
                       f["carimbo"].strftime("%d/%m %H:%M"), _fmt_idade(h) + f" [{status}]",
                       f["detalhe"]))
    return linhas, avisos


def _hora_real_publicacao():
    """
    O registro guarda só a DATA de publicação; a API guarda a hora. A diferença
    importa: o post da lealdade saiu 31/08 às 21:42 e o CRM foi puxado 31/08 às
    09:09 — comparando só a data, a fonte parece cobrir o post, e não cobre.
    Foi exatamente esse buraco que produziu o falso "zero lead" de 02/09.
    """
    p = os.path.join(AN, "desempenho.json")
    if not os.path.exists(p):
        return {}
    d = json.load(open(p))
    fora = {}
    for x in d.get("posts", []):
        ts = (x.get("timestamp") or "").replace("T", " ")[:16]
        dt = _parse(ts)
        if dt and x.get("id"):
            # timestamp da API vem em UTC (+0000); Brasil é UTC-3
            fora[str(x["id"])] = dt - timedelta(hours=3)
    return fora


def checar_cobertura(fontes):
    """O bloqueio que teria matado o erro nº 2: post publicado DEPOIS da fonte ser lida."""
    reg = os.path.join(AN, "registro-posts.csv")
    if not os.path.exists(reg):
        return [], []

    posts = [r for r in csv.DictReader(open(reg)) if r.get("data_publicacao")]
    horas = _hora_real_publicacao()
    bloqueios, ok = [], []

    # de que fonte cada tipo de afirmação depende
    DEPENDE = {
        "métrica / taxa / alcance": "instagram",
        "disparo / CTR do Manychat": "manychat",
        "lead / MQL no CRM": "crm",
    }

    for r in posts:
        dp = _parse(r["data_publicacao"])
        if not dp:
            continue
        # hora exata da API quando existe; senão fica a meia-noite (e vira 'indeterminado')
        exata = horas.get((r.get("post_id") or "").strip())
        quando = exata or dp
        rotulo = quando.strftime("%d/%m %H:%M") if exata else r["data_publicacao"] + " (hora ?)"

        # só interessa o que ainda está vivo na janela de leitura do ritual
        if (_agora() - dp).days > 35:
            continue
        for assunto, chave in DEPENDE.items():
            f = fontes.get(chave)
            if not f or not f["cobre_ate"]:
                continue
            cobre = f["cobre_ate"]
            if quando > cobre:
                # publicado depois da fonte ter sido lida -> a fonte não sabe nada dele
                bloqueios.append((r["pasta"], rotulo, assunto, f["arquivo"],
                                  cobre.strftime("%d/%m %H:%M"), "publicado depois da leitura"))
            elif not exata and quando.date() == cobre.date():
                # mesmo dia e hora desconhecida: não dá pra afirmar que a fonte cobre
                bloqueios.append((r["pasta"], rotulo, assunto, f["arquivo"],
                                  cobre.strftime("%d/%m %H:%M"),
                                  "mesmo dia da leitura e hora do post desconhecida"))
            else:
                ok.append((r["pasta"], chave))

    # o caso específico do Manychat: palavra que nunca foi lida no painel
    mc = fontes.get("manychat")
    sem_leitura = []
    if mc and mc.get("palavras") is not None:
        for r in posts:
            pal = (r.get("palavra_chave") or "").strip()
            dp = _parse(r["data_publicacao"])
            if not pal or not dp or (_agora() - dp).days > 35:
                continue
            if pal not in mc["palavras"]:
                sem_leitura.append((r["pasta"], r["data_publicacao"], pal))

    return bloqueios, sem_leitura


def base_de_ordenacao():
    """
    O antídoto do erro nº 1. Todo superlativo ("o maior", "recorde", "nunca")
    precisa dizer contra QUE base foi ordenado — e a base tem buracos nomeados.
    """
    out = []
    p = os.path.join(AN, "desempenho.json")
    if os.path.exists(p):
        d = json.load(open(p))
        posts = d.get("posts", [])
        datas = sorted(x["timestamp"][:10] for x in posts if x.get("timestamp"))
        por_tipo = {}
        for x in posts:
            por_tipo[x.get("media_type", "?")] = por_tipo.get(x.get("media_type", "?"), 0) + 1
        if datas:
            out.append(f"métricas do Instagram: {len(posts)} posts, de {datas[0]} a {datas[-1]}")
            out.append("   " + " · ".join(f"{k}={v}" for k, v in sorted(por_tipo.items())))

    reg = os.path.join(AN, "registro-posts.csv")
    if os.path.exists(reg):
        rows = [r for r in csv.DictReader(open(reg)) if r.get("data_publicacao")]
        d0 = min(r["data_publicacao"] for r in rows)
        fechados = [r for r in rows if (r.get("resultado_vs_previsao") or "").strip()]
        out.append(f"fichas com previsão: {len(rows)}, a partir de {d0} "
                   f"({len(fechados)} já fechadas)")
        out.append(f"   ATENÇÃO: post anterior a {d0} NÃO tem ficha. "
                   f"Superlativo sobre nervo/roupa/previsão só vale daí pra frente.")

    # o buraco da atribuição, que é o que derrubou o superlativo de 02/09
    disp = os.path.join(AN, "_disparos.json")
    if os.path.exists(disp):
        d = json.load(open(disp))
        globais = [k for k, v in d.items()
                   if not k.startswith("_") and isinstance(v, dict)
                   and "INATRIBUIVEL" in str(v.get("post", ""))]
        if globais:
            out.append(f"atribuição de lead por post: NÃO vale antes de 23/08 "
                       f"(palavra genérica {', '.join(globais)} com gatilho global)")
            for k in globais:
                out.append(f"   {k}: {d[k].get('disparos')} disparos que NÃO se dividem por post")

    snap = os.path.join(AN, "_snapshots.csv")
    if os.path.exists(snap):
        datas = sorted({r["data_snapshot"] for r in csv.DictReader(open(snap))})
        if datas:
            d0 = datetime.strptime(datas[0], "%Y-%m-%d")
            d1 = datetime.strptime(datas[-1], "%Y-%m-%d")
            esperados = {(d0 + timedelta(days=i)).strftime("%Y-%m-%d")
                         for i in range((d1 - d0).days + 1)}
            buracos = sorted(esperados - set(datas))
            if buracos:
                out.append(f"curva de decaimento: {len(buracos)} dia(s) sem foto "
                           f"({', '.join(buracos)}) — irrecuperáveis")
    return out


def main():
    fontes = carregar_fontes()
    if not fontes:
        print("nenhuma fonte encontrada em conteudo/analise/ — nada a validar")
        return 0

    print("=" * 78)
    print("PROCEDÊNCIA DAS FONTES — de quando é cada número que o ritual vai usar")
    print("=" * 78)
    linhas, avisos = checar_frescor(fontes)
    print(f"{'fonte':<11} {'arquivo':<22} {'lida em':<14} {'idade':<18} detalhe")
    for nome, arq, carimbo, idade, det in linhas:
        print(f"{nome:<11} {arq:<22} {carimbo:<14} {idade:<18} {det}")

    if avisos:
        print("\nAVISOS DE FRESCOR:")
        for a in avisos:
            print(f"  ! {a}")

    bloqueios, sem_leitura = checar_cobertura(fontes)

    print("\n" + "=" * 78)
    print("COBERTURA — post que a fonte NÃO alcança (o buraco não é resultado)")
    print("=" * 78)
    if bloqueios:
        print("BLOQUEIO: não afirme nada sobre estes pares post × assunto.")
        print("Um zero aqui significa 'não medido', nunca 'não converteu'.\n")
        for pasta, dp, assunto, arq, cobre, motivo in bloqueios:
            print(f"  X {pasta:<32} publicado {dp}")
            print(f"    {assunto:<26} → {arq} só cobre até {cobre} ({motivo})")
    else:
        print("  ok — toda fonte cobre todos os posts da janela.")

    if sem_leitura:
        print("\n  Palavras sem leitura no painel do Manychat (disparo desconhecido,")
        print("  o que NÃO é o mesmo que disparo zero):")
        for pasta, dp, pal in sem_leitura:
            print(f"    ? {pal:<14} {pasta} ({dp})")

    print("\n" + "=" * 78)
    print("BASE DE ORDENAÇÃO — todo superlativo tem que citar uma destas linhas")
    print("=" * 78)
    for l in base_de_ordenacao():
        print(f"  {l}")
    print("\n  Antes de escrever 'o maior', 'recorde' ou 'nunca aconteceu': diga contra")
    print("  qual destas bases, e confira se a base cobre a era que você está comparando.")

    if bloqueios:
        print(f"\n>>> {len(bloqueios)} BLOQUEIO(S). Atualize a fonte ou declare o post como não medido.")
        return 1
    print("\n>>> fontes limpas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
