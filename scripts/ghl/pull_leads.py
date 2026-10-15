#!/usr/bin/env python3
import sys as _sys_trava
_sys_trava.exit("TRAVADO: esta máquina NÃO acessa a API (a Meta bloqueia quando roda em duas máquinas). Os dados chegam pelo pacote diário: python3 scripts/pacote/importar_pacote.py <zip>. Ver CLAUDE.md -> Analytics.")

"""
pull_leads.py — extrai contatos + oportunidades do GoHighLevel (conta Tatsuo Academy)
e salva conteudo/analise/leads.json com atribuição UTM por contato.

Uso:
  python3 scripts/ghl/pull_leads.py update [DIAS]   # janela rolante (padrão 35 dias)

Baseado no "Manual de Extração de Dados do CRM — API GoHighLevel v2" (14/08/2026):
- POST /contacts/search com filtro dateAdded (UTC; Brasília = UTC-3, somar 3h no filtro)
  + segunda varredura por dateUpdated: pega leads REIMPACTADOS (GHL deduplica por e-mail;
  contato antigo que volta por post novo só atualiza — o rastro fica em lastAttributionSource)
- paginação por searchAfter (marcador do último contato da página)
- GET /opportunities/search com parâmetros em underline e datas mm-dd-yyyy
- GET /opportunities/pipelines pra traduzir IDs (parâmetro locationId, sem underline)
- Tatsuo: contabilizar SÓ os 5 "Funil de Vendas" (funis de teste são descartados, mas ficam
  no JSON marcados com funil_valido=false pra auditoria)
- rate limit 100 req/10s — pausa de 0.15s entre requisições

Credenciais em ~/.config/tatsuo/ghl.env (NUNCA no repositório).
"""
import json, os, sys, time, urllib.request, urllib.parse
from datetime import datetime, timedelta, timezone

BASE = "https://services.leadconnectorhq.com"
ENV_PATH = os.path.expanduser("~/.config/tatsuo/ghl.env")
OUT = os.path.join(os.path.dirname(__file__), "..", "..", "conteudo", "analise", "leads.json")
BRT = timezone(timedelta(hours=-3))
FUNIS_VALIDOS = [
    "Funil de Vendas - Arthur Negrelli",
    "Funil de Vendas - Victor Carvalho",
    "Funil de Vendas - Lucas Castro",
    "Funil de Vendas - Cauê de Souza",
    "Funil de Vendas - Líderes do Amanhã",
]

def env():
    cfg = {}
    with open(ENV_PATH) as f:
        for ln in f:
            ln = ln.strip()
            if ln and not ln.startswith("#") and "=" in ln:
                k, v = ln.split("=", 1)
                cfg[k] = v.strip()
    return cfg["GHL_TOKEN"], cfg["GHL_LOCATION_ID"]

def req(method, url, token, body=None):
    headers = {"Authorization": f"Bearer {token}", "Version": "2021-07-28", "Accept": "application/json",
               "User-Agent": "tatsuo-analytics/1.0 (script interno de marketing)"}
    data = None
    if body is not None:
        headers["Content-Type"] = "application/json"
        data = json.dumps(body).encode()
    r = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(r, timeout=60) as resp:
        out = json.loads(resp.read().decode())
    time.sleep(0.15)
    return out

def norm_funil(nome):
    # tolera hífen/travessão e acentos diferentes entre painel e API
    return (nome or "").replace("—", "-").replace("–", "-").lower().replace("  ", " ").strip()

def attribution(obj):
    if not obj:
        return None
    out = {k: obj.get(k) for k in ("url", "utmSource", "campaign", "campaignId", "utmMedium",
                                   "utmContent", "medium", "mediumId", "sessionSource", "referrer")}
    return out if any(out.values()) else None

def main():
    if len(sys.argv) < 2 or sys.argv[1] != "update":
        print(__doc__); sys.exit(1)
    dias = int(sys.argv[2]) if len(sys.argv) > 2 else 35
    token, loc = env()

    agora_brt = datetime.now(BRT)
    ini_brt = (agora_brt - timedelta(days=dias)).replace(hour=0, minute=0, second=0, microsecond=0)
    # filtro em UTC (Brasília + 3h)
    gte = ini_brt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.000Z")
    lte = agora_brt.astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.999Z")

    # ---- 1. pipelines (tradução de IDs) ----
    pipes = req("GET", f"{BASE}/opportunities/pipelines?locationId={loc}", token)
    pipe_nome, stage_nome = {}, {}
    validos = {norm_funil(n) for n in FUNIS_VALIDOS}
    for p in pipes.get("pipelines", []):
        pipe_nome[p["id"]] = p["name"]
        for s in p.get("stages", []):
            stage_nome[s["id"]] = s["name"]

    # ---- 2. contatos por período (paginação por searchAfter) ----
    # Duas varreduras: dateAdded (criados na janela) + dateUpdated (reimpactados —
    # o GHL deduplica por e-mail, então lead antigo que volta por post novo NÃO cria
    # contato; o rastro cai em lastAttributionSource e só aparece via dateUpdated).
    def fetch(campo):
        out, search_after, total = [], None, None
        while True:
            body = {
                "locationId": loc, "pageLimit": 100,
                "filters": [{"field": campo, "operator": "range", "value": {"gte": gte, "lte": lte}}],
                "sort": [{"field": campo, "direction": "asc"}],
            }
            if search_after:
                body["searchAfter"] = search_after
            r = req("POST", f"{BASE}/contacts/search", token, body)
            page = r.get("contacts", [])
            total = r.get("total", r.get("count", total))
            if not page:
                break
            out.extend(page)
            search_after = page[-1].get("searchAfter")
            print(f"  contatos ({campo}): {len(out)}/{total}")
            if not search_after or (total and len(out) >= total):
                break
        return out

    def dt_para_brt(dt_utc):
        if not dt_utc:
            return ""
        try:
            return datetime.fromisoformat(dt_utc.replace("Z", "+00:00")).astimezone(BRT).strftime("%Y-%m-%d %H:%M")
        except ValueError:
            return dt_utc

    criados = fetch("dateAdded")
    atualizados = fetch("dateUpdated")
    ids_criados = {c.get("id") for c in criados}
    reimpactados = [c for c in atualizados if c.get("id") not in ids_criados]

    contatos = []
    for c, reimp in [(c, False) for c in criados] + [(c, True) for c in reimpactados]:
        contatos.append({
            "id": c.get("id"),
            "nome": f'{c.get("firstName") or ""} {c.get("lastName") or ""}'.strip(),
            "email": c.get("email"), "phone": c.get("phone"),
            "dt_criacao_brt": dt_para_brt(c.get("dateAdded", "")),
            "dt_atualizacao_brt": dt_para_brt(c.get("dateUpdated", "")),
            "reimpactado": reimp,
            "source": c.get("source"), "tags": c.get("tags") or [],
            "customFields": c.get("customFields") or [],
            "primeira_atribuicao": attribution(c.get("attributionSource")),
            "ultima_atribuicao": attribution(c.get("lastAttributionSource")),
            "oportunidades": [],
        })

    # ---- 3. oportunidades do período (datas mm-dd-yyyy, params em underline) ----
    por_contato = {c["id"]: c for c in contatos}
    pg, ops_total = 1, 0
    d_ini = ini_brt.strftime("%m-%d-%Y"); d_fim = agora_brt.strftime("%m-%d-%Y")
    while True:
        q = urllib.parse.urlencode({"location_id": loc, "limit": 100, "page": pg, "status": "all",
                                    "order": "added_asc", "date": d_ini, "endDate": d_fim})
        r = req("GET", f"{BASE}/opportunities/search?{q}", token)
        ops = r.get("opportunities", [])
        if not ops:
            break
        for o in ops:
            ops_total += 1
            funil = pipe_nome.get(o.get("pipelineId"), o.get("pipelineId"))
            item = {
                "id": o.get("id"), "nome": o.get("name"), "status": o.get("status"),
                "fonte": o.get("source"), "funil": funil,
                "funil_valido": norm_funil(funil) in validos,
                "estagio": stage_nome.get(o.get("pipelineStageId"), o.get("pipelineStageId")),
                "valor": o.get("monetaryValue"),
            }
            c = por_contato.get(o.get("contactId"))
            if c:
                c["oportunidades"].append(item)
        print(f"  oportunidades: {ops_total} (página {pg})")
        if len(ops) < 100:
            break
        pg += 1

    # ---- 4. salvar + resumo ----
    out = {
        "pulled_at": agora_brt.strftime("%Y-%m-%d %H:%M"),
        "janela_dias": dias, "total_contatos": len(contatos),
        "total_reimpactados": sum(1 for c in contatos if c["reimpactado"]),
        "total_oportunidades": ops_total,
        "contatos": contatos,
    }
    with open(os.path.abspath(OUT), "w") as f:
        json.dump(out, f, ensure_ascii=False)

    from collections import Counter
    def campanha(c):
        # reimpactado: o rastro do post que trouxe o lead de volta vive na ÚLTIMA atribuição
        at = (c["ultima_atribuicao"] if c["reimpactado"] else c["primeira_atribuicao"]) or {}
        return at.get("campaign") or at.get("utmContent") or "SEM-RASTRO"
    camp = Counter(campanha(c) for c in contatos)
    rastreado = sum(1 for c in contatos if (c["primeira_atribuicao"] or {}).get("utmSource")
                    or (c["ultima_atribuicao"] or {}).get("utmSource"))
    print(f"\nSalvo em {os.path.abspath(OUT)}")
    print(f"Contatos: {len(contatos)} (novos: {len(contatos) - out['total_reimpactados']} | "
          f"reimpactados: {out['total_reimpactados']}) | origem rastreada (utmSource): "
          f"{rastreado} ({100*rastreado/max(1,len(contatos)):.0f}%)")
    print("Top campanhas (novos pela primeira atribuição; reimpactados pela última):")
    for k, v in camp.most_common(12):
        print(f"  {k}: {v}")

    # qualificação do comercial: tags mql / q-mql / n-mql (regra da operação Tatsuo)
    def classe(tags):
        t = [x.strip().lower() for x in tags]
        if "mql" in t: return "MQL"
        if "q-mql" in t: return "Q-MQL"
        if "n-mql" in t: return "N-MQL"
        return "sem classificação"
    qual = Counter(classe(c["tags"]) for c in contatos)
    print("Qualificação (tags do CRM):")
    for k in ("MQL", "Q-MQL", "N-MQL", "sem classificação"):
        if qual.get(k): print(f"  {k}: {qual[k]}")

if __name__ == "__main__":
    main()
