#!/usr/bin/env python3
"""Gera as imagens de um post de frase via gpt-image-2, pelo proxy openai-oauth local (porta 10531),
endpoint direto /v1/images/generations (o caminho que funciona desde 09/09/2026). Base: o gen.py do
post 230_varal, com a pasta do post passada como argumento.

Uso, sempre da raiz do projeto:
  python3 .claude/skills/frase/scripts/gen.py conteudo/carrosseis/<N>_<nome>          # todas que faltam
  python3 .claude/skills/frase/scripts/gen.py conteudo/carrosseis/<N>_<nome> 4 5      # só a 4 e a 5
Pra várias em paralelo, um processo por imagem, cada um com seu log:
  python3 .claude/skills/frase/scripts/gen.py <pasta> 1 > <pasta>/_scripts/gen-01.log 2>&1 &

Lê <pasta>/_scripts/prompts.json (modelo: .claude/skills/frase/template/prompts.json) e grava
<pasta>/imagens/img-NN.png. NUNCA sobrescreve: se img-NN já existe, pula e avisa. Imagem nova =
número novo no prompts.json (a versão anterior fica guardada; o user volta a ela com frequência).

Prompt de cada imagem: o texto da base escolhida ("base" por padrão, ou a chave indicada em "base",
ex. "base_alto") + " SCENE: " + "scene". Se o item tiver "prompt", ele vai inteiro, sem base.
1024x1024, quality high, 3 tentativas. Falha: <pasta>/_scripts/_err-NN.txt com a resposta do proxy.
"""
import base64, json, pathlib, subprocess, sys, time

PORT = 10531
URL = f"http://127.0.0.1:{PORT}/v1/images/generations"

if len(sys.argv) < 2:
    sys.exit(__doc__)
POST = pathlib.Path(sys.argv[1]).resolve()
SCR = POST / "_scripts"
IMG = POST / "imagens"
CFG_FILE = SCR / "prompts.json"
if not CFG_FILE.exists():
    sys.exit(f"Não achei {CFG_FILE}. Copie .claude/skills/frase/template/prompts.json pra lá e escreva as cenas.")
IMG.mkdir(parents=True, exist_ok=True)
CFG = json.loads(CFG_FILE.read_text(encoding="utf-8"))
only = [int(a) for a in sys.argv[2:]] or None


def proxy_ok():
    r = subprocess.run(["curl", "-s", "-o", "/dev/null", "-w", "%{http_code}", f"http://127.0.0.1:{PORT}/v1/models"],
                       capture_output=True, text=True)
    return r.stdout.strip()[:1] in ("2", "4")


def gen(n, prompt):
    payload = {"model": "gpt-image-2", "prompt": prompt, "size": "1024x1024", "n": 1, "quality": "high"}
    pf = SCR / f"_payload-{n:02d}.json"
    pf.write_text(json.dumps(payload))
    r = subprocess.run(
        ["curl", "-sS", "-X", "POST", URL, "-H", "Content-Type: application/json", "-d", f"@{pf}"],
        capture_output=True, text=True, timeout=600,
    )
    pf.unlink(missing_ok=True)
    try:
        b64 = json.loads(r.stdout)["data"][0]["b64_json"]
    except Exception:
        (SCR / f"_err-{n:02d}.txt").write_text(r.stdout[-4000:] + "\n---STDERR---\n" + r.stderr[-2000:])
        return None
    out = IMG / f"img-{n:02d}.png"
    if out.exists():  # outra sessão/processo gravou no meio do caminho: não pisar
        out = IMG / f"img-{n:02d}-{int(time.time())}.png"
    out.write_bytes(base64.b64decode(b64))
    return out


if not proxy_ok():
    sys.exit(f"Proxy fora do ar na porta {PORT}. Subir da raiz do projeto: "
             f"npx -y openai-oauth --port {PORT} > proxy.log 2>&1 &  (esperar ~10 s e rodar de novo)")

for item in CFG["images"]:
    n = item["n"]
    if only and n not in only:
        continue
    dest = IMG / f"img-{n:02d}.png"
    if dest.exists():
        print(f"[{n:02d}] img-{n:02d}.png já existe, pulando (imagem nova = número novo no prompts.json)", flush=True)
        continue
    prompt = item.get("prompt") or (CFG[item.get("base", "base")] + " SCENE: " + item["scene"])
    for attempt in (1, 2, 3):
        t0 = time.time()
        res = gen(n, prompt)
        if res:
            print(f"[{n:02d}] OK em {time.time()-t0:.0f}s -> {res.name}", flush=True)
            break
        print(f"[{n:02d}] FALHOU tentativa {attempt} ({time.time()-t0:.0f}s); ver _scripts/_err-{n:02d}.txt", flush=True)
        time.sleep(5)
print("FIM", flush=True)
