#!/usr/bin/env python3
"""
Régua viva da máquina de análise — calcula as medianas e as faixas de previsão
a partir do desempenho.json, na hora. ZERO chamada de API.

    python3 scripts/instagram/reguas.py            # janela padrão (90 dias)
    python3 scripts/instagram/reguas.py 180        # outra janela

POR QUE ISSO EXISTE
-------------------
Até 27/08/2026 as réguas viviam escritas à mão dentro das skills: a /etiqueta mandava
calibrar carrossel por "36 comentários" e frase por "67 compartilhamentos". Os dois
números tinham envelhecido em direções opostas (o real era 17,5 e 147), e isso
contaminava toda previsão: o placar acumulado ficou em 33% de acerto, contra 33,3%
de puro acaso, com 18 previsões "acima" e ZERO "abaixo" em 24 fichas.

Número fixo em arquivo de texto apodrece em silêncio. Régua calculada na hora, não.

O QUE MUDOU JUNTO (decisão do user, 27/08)
------------------------------------------
A previsão passou a ser sobre TAXA (engajamento por mil alcançados), não sobre número
absoluto. Motivo: o absoluto é o produto de duas coisas muito diferentes —

    absoluto  =  taxa  ×  alcance
                 ^^^^     ^^^^^^^
                 o que    o que ninguém
                 se       controla
                 controla

A dispersão do alcance (p90/p25) é de 14x no carrossel e 16x na frase; a da taxa é de
6x e 2,3x. Prever o absoluto é, em boa parte, apostar na loteria da distribuição e
depois creditar (ou culpar) o texto. A taxa isola o que a edição de fato decide.

AS FAIXAS SÃO TERCIS, DE PROPÓSITO
----------------------------------
abaixo / mediana / acima são os terços da distribuição real: cada banda contém 1/3 dos
posts por construção. Assim o acaso vale exatamente 33,3% e o placar fica lido de
imediato — acertar mais que isso é competência, e não artefato de banda larga.

O QUE MUDOU EM 14/09 (decisão do user): TAXA ESTIMA, ABSOLUTO EM D+7 FECHA
---------------------------------------------------------------------------
Nas palavras dele: "as primeiras taxas dos posts são mais para dar um norte do que para
atestar a eficiência dele; todas as análises devem ser feitas usando o D7 com base no
total de comentários e não a taxa". Fica assim, e os dois papéis são declarados na saída:

  DADO FINAL  = o ABSOLUTO em D+7 da métrica que o formato produz: COMENTÁRIOS no carrossel
                e no reel (é o degrau que vira lead: rho +0,94 com disparo do Manychat),
                COMPARTILHAMENTOS na frase (ela não gera comentário por desenho). É contra
                as bandas do absoluto que o placar fecha e que se compara post com post.
  ESTIMATIVA  = a TAXA por mil. Serve pra três coisas e nenhuma delas é atestar eficiência:
                (1) antes de publicar, ler os comparáveis descontando o alcance e escolher a
                banda prevista; (2) entre D+1 e D+4, ler se a peça está pegando em quem viu,
                antes de o alcance se decidir (o "norte"); (3) no fechamento, explicar o erro:
                taxa alta com absoluto baixo = pegou em quem viu e viu pouca gente; taxa
                baixa = o conteúdo não pegou.

Por que o absoluto voltou: a taxa não neutraliza o tamanho (hipótese fechada 🟢 em 02/09:
rho +0,70 entre alcance e interações/1k; o post grande é premiado duas vezes), e o que vira
negócio é o comentário contado, não o comentário por mil. As bandas do absoluto são
calculadas SÓ sobre posts com 7 dias ou mais na janela (maturados) — post de dois dias
puxaria o terço de baixo pra baixo sem ter terminado de crescer. Regime 3 do placar
(1 = absoluto contra régua fixa, até 26/08; 2 = taxa, 27/08 a 13/09; 3 = absoluto em D+7
contra terços vivos, desde 14/09). Cada regime se conta separado.
"""
import datetime
import csv
import json
import os
import statistics as st
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
OUT_JSON = os.path.join(REPO_ROOT, "conteudo", "analise", "desempenho.json")

JANELA_PADRAO = 90

# Cada formato é medido pela métrica que ele de fato produz. Frase quase não gera
# comentário (mediana 3) e viaja por compartilhamento; carrossel conversa e é de onde
# sai o lead. Julgar frase por comentário — ou carrossel por alcance — é erro de régua.
#
# `final` (14/09) é a métrica que FECHA o placar, em absoluto, lida em D+7. `alvo`/`rotulo`
# seguem sendo a taxa: agora ESTIMATIVA (previsão antes de publicar e norte de D+1 a D+4).
FORMATOS = {
    "frase":     {"media_type": "IMAGE",          "alvo": "shares",             "rotulo": "shares/1k",
                  "final": "shares",   "final_rotulo": "compartilhamentos"},
    "carrossel": {"media_type": "CAROUSEL_ALBUM", "alvo": "total_interactions", "rotulo": "interações/1k",
                  "final": "comments", "final_rotulo": "comentários"},
    # REEL entrou em 31/08. Até aqui os ~330 vídeos de cada janela de 90d não tinham régua
    # nenhuma — a máquina simplesmente não olhava o formato mais publicado da casa.
    # O alvo nasce em interações/1k, igual ao carrossel, por dois motivos: é TAXA (comparável
    # entre peças de alcance muito diferente, e é taxa que se prevê) e permite comparar reel
    # com carrossel na mesma escala. Isto NÃO fere a regra de congelamento abaixo: congelar
    # proíbe TROCAR um alvo, e o reel nunca teve um.
    "reel":      {"media_type": "VIDEO",          "alvo": "total_interactions", "rotulo": "interações/1k",
                  "final": "comments", "final_rotulo": "comentários"},
}

MATURACAO_DIAS = 7  # o dado final só existe em D+7; banda do absoluto sai só de post maturado

# POR QUE CARROSSEL NÃO É MEDIDO EM COMENTÁRIO (medido em 27/08, 353 carrosséis de 12 meses)
# Comentário parecia o alvo óbvio: é o proxy de lead. Mas como medida de QUALIDADE do conteúdo
# ele é ruim, e por um motivo técnico específico — comentário aqui é EXÓGENO, dirigido pelo CTA
# de palavra-chave e pela automação, não pela qualidade que o algoritmo lê:
#   - a correlação de comentário com alcance EVAPORA ao destendenciar (+0,316 bruto -> +0,017, p=0,73),
#     enquanto interações e shares seguram (+0,70 e +0,69);
#   - a mediana mensal de com/1k andou de 0,28 a 3,36 em 12 meses (57x de deriva) — a régua não para de pé;
#   - 15 dos 147 carrosséis dos últimos 90d têm ZERO comentário, contra 0 zeros em interações;
#   - dispersão p90/p25: interações 3,2x contra 6,8x de comentário. Alvo mais apertado = previsão que informa.
# Comentário CONTINUA sendo lido — só que como proxy de LEAD (ordena posts por lead com rho=0,92),
# não como nota do conteúdo. São dois trabalhos diferentes e o arquivo reporta os dois.
#
# RE-EXAMINADO EM 28/08 (o user mandou decidir, não sugerir) — A ESCOLHA SE MANTÉM.
# Eu tinha proposto trocar o alvo pra com/1k, apoiado em rho +0,85 com disparo real do Manychat
# (contra +0,54 da taxa composta). A proposta CAI por dois testes:
#   1. deriva da régua: a mediana mensal de com/1k andou de 0,28 a 15,85 em 20 meses (57x);
#      a de interações/1k andou 44,5 a 75,4 (1,7x). Banda montada sobre com/1k mede a nossa
#      própria mudança de prática de CTA, não a qualidade da peça. Placar assim se autoengana.
#   2. o rho alto de com/1k era resposta a OUTRA pergunta. Ordenar por lead e dar nota ao conteúdo
#      são trabalhos distintos — exatamente o que este bloco já dizia. Meu dado não contradisse
#      o raciocínio original; respondeu coisa diferente e eu quase troquei a régua por isso.
# Achado que sobra e vale: a taxa composta é MAIS presa ao alcance que com/1k
# (rho com alcance: +0,711 contra +0,436). Não muda o alvo, mas é limite conhecido — a taxa
# carrega distribuição junto com qualidade, e por isso alcance vai SEMPRE na tabela do lado dela.
#
# REGRA DE CONGELAMENTO (28/08): o alvo do placar não muda de novo antes de 20 fichas fechadas
# em D+7 no regime vigente. Trocar a régua a cada achado zera o placar toda semana e a máquina
# nunca chega a saber se acerta. Achado novo entra como COLUNA na tabela, não como troca de alvo.

# PRIORIDADE DE MÉTRICAS POR FORMATO (decisão do user, 31/08)
#
# O problema que isto resolve, nas palavras dele: "não criar uma expectativa errada de um post
# que vai ser postado". Cada formato existe pra uma coisa — o carrossel pede ação e vira lead,
# a frase fura a bolha, o reel depende de como foi construído — e medir os três pela mesma
# métrica cobra da peça um resultado que não é o dela. Frase não gera comentário por desenho;
# cobrar comentário dela é erro de régua, não desempenho ruim.
#
# Cada formato passa a ter uma LISTA ORDENADA: a 1ª é a métrica que lidera a leitura daquele
# formato e ordena a tabela do relatório; as outras entram ao lado, na ordem.
#
# ISTO NÃO É TROCA DE ALVO. O que pontua no placar continua sendo `alvo`, congelado até 20
# fichas fechadas (ver regra acima). A prioridade governa LEITURA e ORDENAÇÃO, que é
# exatamente o "achado novo entra como COLUNA" que o congelamento manda fazer.
#
# COMENTÁRIO VOLTA COMO 1ª DO CARROSSEL — e isso não contradiz o bloco acima, que o rebaixou.
# São duas perguntas diferentes, e o próprio bloco já dizia isso ("são dois trabalhos distintos
# e o arquivo reporta os dois"). Como nota de QUALIDADE do conteúdo, comentário continua ruim:
# é exógeno, dirigido pelo CTA, e a régua deriva 57x em 20 meses. Como medida de LEAD, é o
# melhor que existe — medido em 31/08 sobre os 19 posts com automação: rho +0,94 com disparo
# real do Manychat, contra +0,70 da taxa composta e +0,51 do alcance. Por isso ele lidera a
# leitura do carrossel (cujo objetivo é lead) e NÃO pontua no placar (que mede qualidade).
#
# "por1k" divide pelo alcance e multiplica por mil; "absoluto" entra cru. Dividir alcance por
# alcance não significa nada, e views idem — por isso o tipo é declarado, não inferido.
PRIORIDADES = {
    # objetivo: LEAD. Comentário é o degrau que vira disparo de automação.
    "carrossel": [("comments", "por1k"), ("views", "absoluto"), ("shares", "por1k")],
    # objetivo: ALCANCE (furar a bolha). Medido em 31/08: a frase alcança 8x mais que as
    # outras na veia de pressão, com taxa de share IDÊNTICA — ela compra distribuição, não
    # intensidade. Então o tamanho vem primeiro, e o seguidor ganho é o ativo que fica.
    "frase":     [("reach", "absoluto"), ("shares", "por1k"), ("follows", "absoluto")],
    # objetivo: VARIÁVEL, declarado na ficha. Esta é a ordem de quando o reel é de alcance;
    # quando a ficha declara `lead`, a leitura usa a ordem do carrossel (ver PRIORIDADES_POR_OBJETIVO).
    "reel":      [("views", "absoluto"), ("reach", "absoluto"), ("shares", "por1k")],
}

# O reel é o único formato cujo objetivo varia por peça, então é o único que precisa disto.
PRIORIDADES_POR_OBJETIVO = {
    "lead":    [("comments", "por1k"), ("views", "absoluto"), ("shares", "por1k")],
    "alcance": [("views", "absoluto"), ("reach", "absoluto"), ("shares", "por1k")],
    "seguidor": [("follows", "absoluto"), ("profile_visits", "absoluto"), ("reach", "absoluto")],
}


# Pra que cada formato existe. Constante em carrossel e frase; no reel é declarado na ficha.
OBJETIVO_DO_FORMATO = {"carrossel": "objetivo: lead", "frase": "objetivo: alcance",
                       "reel": "objetivo: varia — declarado na ficha"}


def prioridades(formato, objetivo=None):
    """Lista ordenada de (métrica, tipo) que lidera a leitura. O objetivo só manda no reel —
    em carrossel e frase ele é constante do formato e a lista já reflete isso."""
    if formato == "reel" and objetivo in PRIORIDADES_POR_OBJETIVO:
        return PRIORIDADES_POR_OBJETIVO[objetivo]
    return PRIORIDADES.get(formato, [])


def _pct(valores, f):
    """Percentil com interpolação linear (sem numpy)."""
    v = sorted(valores)
    if not v:
        return 0.0
    i = f * (len(v) - 1)
    lo = int(i)
    if lo + 1 >= len(v):
        return float(v[-1])
    return v[lo] + (i - lo) * (v[lo + 1] - v[lo])


def descartados():
    """IDs de posts que NAO entram em nenhuma regua nem mediana.
    Casos tipicos: post republicado (a versao morta fica na API e puxa a mediana pra baixo).
    Fonte: conteudo/analise/_descartados.csv — uma linha por post, com motivo e data."""
    caminho = os.path.join(os.path.dirname(OUT_JSON), "_descartados.csv")
    if not os.path.exists(caminho):
        return set()
    with open(caminho, encoding="utf-8") as f:
        return {linha["post_id"].strip() for linha in csv.DictReader(f) if linha.get("post_id", "").strip()}


def calcular(janela_dias=JANELA_PADRAO):
    with open(OUT_JSON) as f:
        data = json.load(f)
    corte = (datetime.date.today() - datetime.timedelta(days=janela_dias)).isoformat()
    fora = descartados()

    out = {"pulled_at": data.get("pulled_at"), "janela_dias": janela_dias,
           "desde": corte, "formatos": {}}

    for nome, cfg in FORMATOS.items():
        grupo = [p for p in data["posts"]
                 if p["media_type"] == cfg["media_type"]
                 and p["timestamp"][:10] >= corte
                 and str(p.get("id")) not in fora
                 and (p.get("metrics") or {}).get("reach")]
        if len(grupo) < 12:
            out["formatos"][nome] = {"n": len(grupo), "aviso": "amostra pequena demais"}
            continue

        def mt(p, k):
            return (p.get("metrics") or {}).get(k) or 0

        taxa = [1000 * mt(p, cfg["alvo"]) / mt(p, "reach") for p in grupo]
        reach = [mt(p, "reach") for p in grupo]
        absoluto = [mt(p, cfg["alvo"]) for p in grupo]

        # DADO FINAL (14/09): absoluto da métrica do formato, só em post maturado (>= D+7).
        # A lista "grupo" inclui post de ontem; ele entra na taxa (estimativa) e fica fora daqui.
        corte_mat = (datetime.date.today() - datetime.timedelta(days=MATURACAO_DIAS)).isoformat()
        maturados = [p for p in grupo if p["timestamp"][:10] <= corte_mat]
        final = [mt(p, cfg["final"]) for p in maturados]

        out["formatos"][nome] = {
            "n": len(grupo),
            "metrica_alvo": cfg["alvo"],
            "rotulo_taxa": cfg["rotulo"],
            "final_metrica": cfg["final"],
            "final_rotulo": cfg["final_rotulo"],
            "final_n": len(final),
            "final_p33": round(_pct(final, 1 / 3), 1),
            "final_mediana": round(st.median(final), 1) if final else 0.0,
            "final_p67": round(_pct(final, 2 / 3), 1),
            "final_p90": round(_pct(final, 0.90), 1),
            # terços: cada banda com 1/3 dos posts -> acaso = 33,3%
            "taxa_p33": round(_pct(taxa, 1 / 3), 2),
            "taxa_mediana": round(st.median(taxa), 2),
            "taxa_p67": round(_pct(taxa, 2 / 3), 2),
            "taxa_p90": round(_pct(taxa, 0.90), 2),
            "alcance_p33": int(_pct(reach, 1 / 3)),
            "alcance_mediana": int(st.median(reach)),
            "alcance_p67": int(_pct(reach, 2 / 3)),
            "absoluto_mediana": round(st.median(absoluto), 1),
        }
        # Prioridades: medianas na ORDEM declarada. Não pontuam — lideram a leitura.
        pri = []
        for metrica, tipo in prioridades(nome):
            if tipo == "por1k":
                vals = [1000 * mt(p, metrica) / mt(p, "reach") for p in grupo]
                rotulo = f"{metrica}/1k"
            else:
                vals = [mt(p, metrica) for p in grupo]
                rotulo = metrica
            # métrica que a API não devolve pra este tipo de mídia (ex.: follows em VIDEO)
            # sai da lista em vez de virar uma coluna de zeros que parece resultado ruim.
            if not any(vals):
                pri.append({"metrica": metrica, "rotulo": rotulo, "tipo": tipo,
                            "indisponivel": True})
                continue
            pri.append({"metrica": metrica, "rotulo": rotulo, "tipo": tipo,
                        "mediana": round(st.median(vals), 2),
                        "p33": round(_pct(vals, 1 / 3), 2), "p67": round(_pct(vals, 2 / 3), 2)})
        out["formatos"][nome]["prioridades"] = pri
    return out


def imprimir(r):
    print(f"RÉGUA VIVA — dado de {r['pulled_at']} · janela {r['janela_dias']}d (desde {r['desde']})\n")
    for nome, f in r["formatos"].items():
        if "aviso" in f:
            print(f"  {nome.upper()}: {f['aviso']} (n={f['n']})\n")
            continue
        print(f"  {nome.upper()} (n={f['n']}) — dado final: {f['final_metrica']} em D+7 · estimativa: {f['metrica_alvo']}/1k")
        print(f"    DADO FINAL ({f['final_rotulo'].upper()}, absoluto em D+7; n={f['final_n']} maturados) — é ISTO que fecha o placar")
        print(f"      abaixo  : < {f['final_p33']:.0f}")
        print(f"      mediana : {f['final_p33']:.0f} a {f['final_p67']:.0f}   (mediana {f['final_mediana']:.0f})")
        print(f"      acima   : > {f['final_p67']:.0f}                   (top 10% acima de {f['final_p90']:.0f})")
        print(f"    ESTIMATIVA ({f['rotulo_taxa']}) — norte antes de publicar e de D+1 a D+4; NÃO atesta eficiência")
        print(f"      abaixo  : < {f['taxa_p33']}")
        print(f"      mediana : {f['taxa_p33']} a {f['taxa_p67']}   (mediana {f['taxa_mediana']})")
        print(f"      acima   : > {f['taxa_p67']}                   (top 10% acima de {f['taxa_p90']})")
        print(f"    ALCANCE — NÃO se prevê e NÃO pontua. Só se registra o realizado.")
        print(f"      mediana de referência {f['alcance_mediana']} (bandas: baixo < {f['alcance_p33']} · alto > {f['alcance_p67']})")
        print(f"    PRIORIDADE DE LEITURA ({OBJETIVO_DO_FORMATO.get(nome, '?')}) — ordena a tabela, NÃO pontua")
        for i, pr in enumerate(f.get("prioridades", []), 1):
            if pr.get("indisponivel"):
                print(f"      {i}ª {pr['rotulo']:<22} — a API não devolve esta métrica neste formato")
            else:
                print(f"      {i}ª {pr['rotulo']:<22} mediana {pr['mediana']}"
                      f"   (terços: {pr['p33']} · {pr['p67']})")
        print(f"    contexto (não pontua): absoluto mediano {f['absoluto_mediana']}\n")
    print("  Cada banda tem 1/3 dos posts. Acaso = 33,3%. Acertar menos que isso não é azar,")
    print("  é régua ou critério errado.")
    print("  DESDE 14/09: a previsão se ESCREVE olhando a taxa dos comparáveis (estimativa) e se")
    print("  FECHA contra o dado final absoluto em D+7 (comentários; na frase, compartilhamentos).")
    print("  Leitura de D+1 a D+4 é norte, nunca atestado. Taxa alta com absoluto baixo = pegou em")
    print("  quem viu e viu pouca gente; taxa baixa = o conteúdo não pegou.")
    print("  ALCANCE NÃO SE PREVÊ: medido em 27/08, nenhuma variável conhecida antes de publicar")
    print("  passa de ~7% da variância, e o formato é a única que sobrevive à validação cruzada.")


if __name__ == "__main__":
    janela = int(sys.argv[1]) if len(sys.argv) > 1 else JANELA_PADRAO
    r = calcular(janela)
    if os.environ.get("REGUAS_JSON"):
        print(json.dumps(r, ensure_ascii=False, indent=2))
    else:
        imprimir(r)
