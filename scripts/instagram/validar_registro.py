#!/usr/bin/env python3
"""
Valida o registro-posts.csv. ZERO API — lê só o disco.

    python3 scripts/instagram/validar_registro.py

POR QUE ISSO EXISTE
-------------------
Mais de uma sessão do Claude escreve neste CSV ao mesmo tempo, e cada uma carrega o
contexto do momento em que começou. Em 27/08/2026 isso produziu dois estragos silenciosos
no mesmo dia:

  1. Uma sessão acrescentou a coluna `data_publicacao`; outra, que já estava rodando,
     gravou uma ficha no layout antigo. A linha ficou deslocada em um campo — `pasta`
     lia "frase" e `formato` lia "banco-16". Quem lesse por nome de coluna leria errado
     e não perceberia.
  2. A previsão mudou de número absoluto para TAXA. Uma sessão que não sabia disso
     regravou uma ficha com faixa em absoluto, sem marcação. A faixa "20-90" atravessa
     as três bandas de taxa de uma vez — não é previsão de nada, mas parece uma.

Nenhum dos dois quebra nada na hora. Os dois envenenam o placar semanas depois, quando
já ninguém lembra. Este script existe pra que o estrago apareça no dia em que acontece.

Rodar: no fim de toda /etiqueta, no início de todo /ritual, e sempre que duas sessões
tiverem trabalhado no mesmo dia. Sai com código 1 se achar erro — dá pra usar em hook.
"""
import csv
import datetime
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
CSV = os.path.join(REPO_ROOT, "conteudo", "analise", "registro-posts.csv")

COLUNAS = ["data", "data_publicacao", "post_id", "pasta", "formato", "semente", "pilar", "nervo",
           "consciencia_dor", "mecanismo", "roupa", "palavra_chave", "funil", "objetivo",
           "previsao", "previsao_faixa", "justificativa", "resultado_com",
           "resultado_taxa", "resultado_alcance", "resultado_vs_previsao"]

# `objetivo` (31/08): pra que a peça existe. É CONSTANTE do formato em carrossel (lead)
# e frase (alcance) — por isso preenchido automaticamente, sem decisão do operador — e
# DECLARADO só no reel, o único formato em que varia de peça pra peça (decisão do user:
# "sobre o reel é mais amplo, depende da construção dele em si"). O que ele governa é
# qual métrica lidera a leitura daquele post, não o alvo que pontua no placar.
OBJETIVOS = {"lead", "seguidor", "alcance", ""}

# `funil` foi APOSENTADO em 31/08. A coluna fica pelos 14 valores históricos, mas saiu do
# fluxo: a /etiqueta não pergunta mais e o validador não exige. Ela pedia leitura DEPOIS do
# fato ("puxou alcance = topo"), o ritual parou de preencher nas últimas 18 fichas, e nenhum
# script jamais consumiu. `objetivo` responde melhor a mesma pergunta, declarado ANTES.
FUNIL_APOSENTADO = True

# Três regimes de previsão, e cada um se conta separado no placar:
#   1) até 26/08: número absoluto contra régua FIXA (36 comentários) — apodreceu;
#   2) 27/08 a 13/09: TAXA por mil contra terços vivos;
#   3) desde 14/09: ABSOLUTO EM D+7 (comentários no carrossel/reel, compartilhamentos na
#      frase) contra terços vivos de posts maturados. A taxa virou ESTIMATIVA: guia a
#      escolha da banda antes de publicar e a leitura de D+1 a D+4, mas não fecha nada.
#      Decisão do user, 14/09: "as primeiras taxas dos posts são mais para dar um norte
#      do que para atestar a eficiência dele".
# Ficha de regime 1 precisa dizer isso na própria faixa, senão se mistura com as outras.
VIRADA_TAXA = "2026-08-27"
VIRADA_FINAL = "2026-09-14"
MARCA_ANTIGA = "regime antigo"

# Faixas plausíveis por formato (ordem de grandeza, não banda de previsão).
# Servem só pra flagrar número que claramente não é daquela unidade.
PLAUSIVEL = {"carrossel": (5.0, 400.0), "frase": (0.5, 40.0)}            # taxa (regime 2)
PLAUSIVEL_FINAL = {"carrossel": (0, 20000), "reel": (0, 20000), "frase": (0, 200000)}  # absoluto (regime 3)

PREVISOES = {"abaixo", "mediana", "acima", ""}
# "nao-pontua" (01/09): ficha retroativa, escrita DEPOIS do resultado estar na tela.
# Fecha a leitura mas fica fora do placar — sem isso ela ficava marcada "fecha hoje" pra
# sempre, poluindo a tabela e sugerindo trabalho pendente que nao existe.
VEREDITOS = {"acertou", "errou-pra-cima", "errou-pra-baixo", "nao-pontua", ""}


_BANDAS = {}


def _carregar_bandas():
    if not _BANDAS:
        try:
            sys.path.insert(0, _HERE)
            import reguas
            r = reguas.calcular()
            for nome, f in r["formatos"].items():
                if "taxa_p33" in f:
                    _BANDAS[nome] = (f["taxa_p33"], f["taxa_p67"])
                if "final_p33" in f:
                    _BANDAS[nome + "/final"] = (f["final_p33"], f["final_p67"])
        except Exception as e:  # sem desempenho.json, a checagem de banda é pulada
            _BANDAS["_erro"] = str(e)


def bandas(formato):
    """Bandas vigentes de TAXA (regime 2), da régua viva. Sem número fixo aqui: se a
    régua muda, a validação muda junto."""
    _carregar_bandas()
    return _BANDAS.get(formato)


def bandas_final(formato):
    """Bandas vigentes do DADO FINAL (regime 3): comentários em D+7 no carrossel e no
    reel, compartilhamentos na frase."""
    _carregar_bandas()
    return _BANDAS.get(formato + "/final")


def _data_ok(s):
    try:
        datetime.date.fromisoformat(s)
        return True
    except ValueError:
        return False


def validar(caminho=CSV):
    erros, avisos = [], []
    with open(caminho, newline="") as f:
        linhas = list(csv.reader(f))
    if not linhas:
        return ["CSV vazio"], []

    hdr = linhas[0]
    if hdr != COLUNAS:
        faltam = [c for c in COLUNAS if c not in hdr]
        sobram = [c for c in hdr if c not in COLUNAS]
        erros.append(f"cabeçalho fora do esperado — faltam {faltam or 'nada'}, sobram {sobram or 'nada'}")
        return erros, avisos

    # 1) desalinhamento: o erro que passou despercebido em 27/08
    for i, r in enumerate(linhas[1:], start=2):
        if len(r) != len(hdr):
            erros.append(f"linha {i}: {len(r)} campos, esperado {len(hdr)} "
                         f"(desalinhada — provável escrita com layout antigo). Começa em: {r[:3]}")
    if erros:
        return erros, avisos

    rows = [dict(zip(hdr, r)) for r in linhas[1:]]
    vistos = {}

    for i, r in enumerate(rows, start=2):
        pasta = r["pasta"] or f"<linha {i}>"

        if not _data_ok(r["data"]):
            erros.append(f"{pasta}: campo 'data' inválido ({r['data']!r})")
        if r["data_publicacao"] and not _data_ok(r["data_publicacao"]):
            erros.append(f"{pasta}: 'data_publicacao' inválida ({r['data_publicacao']!r})")
        if not r["data_publicacao"]:
            avisos.append(f"{pasta}: sem data_publicacao — o ritual não sabe quando fecha em D+7")

        if r["pasta"] in vistos:
            avisos.append(f"{pasta}: aparece 2x (linhas {vistos[r['pasta']]} e {i})")
        vistos[r["pasta"]] = i

        if r["previsao"] not in PREVISOES:
            erros.append(f"{pasta}: previsao {r['previsao']!r} não é abaixo/mediana/acima")
        if r["resultado_vs_previsao"] not in VEREDITOS:
            erros.append(f"{pasta}: resultado_vs_previsao {r['resultado_vs_previsao']!r} inválido")

        obj = r.get("objetivo", "")
        if obj not in OBJETIVOS:
            erros.append(f"{pasta}: objetivo {obj!r} não é lead/seguidor/alcance")
        # Em carrossel e frase o objetivo é constante do formato — divergir dele é sinal de
        # ficha preenchida à mão contra a régua, não de peça excepcional. No reel não se
        # checa valor (é lá que ele varia), só que exista.
        esperado = {"carrossel": "lead", "frase": "alcance"}.get(r["formato"])
        if esperado and obj and obj != esperado:
            erros.append(f"{pasta}: objetivo {obj!r} contraria a constante de {r['formato']} "
                         f"({esperado!r}). Objetivo só se declara em reel.")
        if r["formato"] == "reel" and not obj:
            avisos.append(f"{pasta}: reel sem objetivo declarado — a leitura do post fica sem "
                          f"métrica líder (lead ou alcance?)")

        # 2) mistura de regimes: o erro que a outra sessão cometeu sem ter como saber
        faixa = r["previsao_faixa"]
        # Ficha já FECHADA (resultado_vs_previsao preenchido) não passa pela checagem de
        # encaixe na banda: as bandas são terços vivos de 90 dias e se movem todo dia, e a
        # faixa foi escrita contra a régua da data da ficha. Reconferir depois do fechamento
        # acusa erro falso (81_tempo-de-resposta, 14/09: "52.0-85.0" cabia na mediana de
        # 02/09 e não cabe na de 14/09) — e mexer numa previsão já pontuada é o que o placar
        # existe pra impedir. Formato e ordem de grandeza continuam sendo checados.
        fechada = bool(r["resultado_vs_previsao"])
        if faixa:
            antiga = MARCA_ANTIGA in faixa
            m = re.match(r"^\s*([\d.]+)\s*-\s*([\d.]+)", faixa)
            if not m:
                erros.append(f"{pasta}: faixa {faixa!r} não está no formato min-max")
            elif not antiga and r["data"] >= VIRADA_FINAL:
                # REGIME 3: faixa em ABSOLUTO (comentários; shares na frase), tem que caber na
                # banda prevista do dado final. Faixa de taxa gravada aqui por sessão velha
                # (ex.: "48-80" com previsão mediana) cai fora da banda e é acusada.
                lo, hi = float(m.group(1)), float(m.group(2))
                if lo >= hi:
                    erros.append(f"{pasta}: faixa invertida ({lo} >= {hi})")
                pl = PLAUSIVEL_FINAL.get(r["formato"])
                if pl and not (pl[0] <= lo and hi <= pl[1]):
                    erros.append(f"{pasta}: faixa {faixa!r} fora da ordem de grandeza do dado final "
                                 f"de {r['formato']} ({pl[0]}-{pl[1]} em absoluto). Desde {VIRADA_FINAL} a "
                                 f"faixa é de COMENTÁRIOS em D+7 (shares na frase), não de taxa.")
                elif r["previsao"] and not fechada:
                    b = bandas_final(r["formato"])
                    if b:
                        p33, p67 = b
                        limite = {"abaixo": (0.0, p33), "mediana": (p33, p67),
                                  "acima": (p67, float("inf"))}[r["previsao"]]
                        if lo < limite[0] * 0.9 or hi > limite[1] * 1.1:
                            erros.append(
                                f"{pasta}: previsão {r['previsao']!r} mas faixa {faixa!r} não cabe na banda "
                                f"do dado final ({limite[0]:.0f}–{limite[1]:.0f} {r['formato']}, absoluto em D+7). "
                                f"Ou a faixa ainda está em taxa (regime 2, encerrado em 13/09), ou previsão "
                                f"e faixa se contradizem.")
            elif not antiga:
                lo, hi = float(m.group(1)), float(m.group(2))
                if lo >= hi:
                    erros.append(f"{pasta}: faixa invertida ({lo} >= {hi})")
                pl = PLAUSIVEL.get(r["formato"])
                nova = r["data"] >= VIRADA_TAXA
                if pl and not (pl[0] <= lo and hi <= pl[1]):
                    (erros if nova else avisos).append(
                        f"{pasta}: faixa {faixa!r} está fora da ordem de grandeza de taxa "
                        f"de {r['formato']} ({pl[0]}-{pl[1]}). Se for número absoluto do regime "
                        f"antigo, marcar com '({MARCA_ANTIGA})'; se for taxa, corrigir.")
                elif nova and r["previsao"] and not fechada:
                    # A checagem que pega o erro sutil: a faixa tem que CABER na banda
                    # prevista. Faixa que atravessa as três bandas não prevê nada —
                    # parece previsão, mas não pode errar, então nunca ensina nada.
                    b = bandas(r["formato"])
                    if b:
                        p33, p67 = b
                        limite = {"abaixo": (0.0, p33), "mediana": (p33, p67),
                                  "acima": (p67, float("inf"))}[r["previsao"]]
                        if lo < limite[0] * 0.9 or hi > limite[1] * 1.1:
                            erros.append(
                                f"{pasta}: previsão {r['previsao']!r} mas faixa {faixa!r} não cabe "
                                f"na banda ({limite[0]:.1f}–{limite[1]:.1f} {r['formato']}). "
                                f"Ou a faixa é de outro regime (marcar '({MARCA_ANTIGA})'), "
                                f"ou previsão e faixa se contradizem.")
                elif not nova:
                    avisos.append(f"{pasta}: ficha anterior a {VIRADA_TAXA} sem marca de regime — "
                                  f"confirmar se a faixa é taxa ou absoluto")

    return erros, avisos


if __name__ == "__main__":
    caminho = sys.argv[1] if len(sys.argv) > 1 else CSV
    erros, avisos = validar(caminho)
    for a in avisos:
        print(f"  aviso: {a}")
    for e in erros:
        print(f"  ERRO : {e}")
    if erros:
        print(f"\n{len(erros)} erro(s) — corrigir antes do próximo ritual, "
              f"senão entram no placar como se fossem dado bom.")
        sys.exit(1)
    print(f"\nregistro OK ({len(avisos)} aviso(s)).")
