#!/usr/bin/env python3
"""Gera as imagens do carrossel 146 via gpt-image-2 (proxy openai-oauth local), endpoint DIRETO
/v1/images/generations. Uma por vez. (09/09: o caminho /v1/responses + modelo de texto parou de
invocar a tool image_generation: gpt-5.5 'model_not_found', 5.6-sol/terra e 6-astra devolvem
mensagem vazia. O endpoint direto responde em ~20 s e entrega landscape.)"""
import base64, json, os, pathlib, subprocess, sys, time

SCR = pathlib.Path(__file__).parent
IMG = SCR.parent / "imagens"
IMG.mkdir(parents=True, exist_ok=True)
CFG = json.loads((SCR / "prompts.json").read_text())
PORT = 10531
URL = f"http://127.0.0.1:{PORT}/v1/images/generations"

only = [int(a) for a in sys.argv[1:]] or None


def gen(n, prompt):
    payload = {"model": "gpt-image-2", "prompt": prompt, "size": "1536x1024", "n": 1, "quality": "high"}
    pf = SCR / f"_payload-{n:02d}.json"
    pf.write_text(json.dumps(payload))
    r = subprocess.run(
        ["curl", "-sS", "-X", "POST", URL, "-H", "Content-Type: application/json", "-d", f"@{pf}"],
        capture_output=True, text=True, timeout=600,
    )
    pf.unlink(missing_ok=True)
    try:
        d = json.loads(r.stdout)
        b64 = d["data"][0]["b64_json"]
    except Exception:
        (SCR / f"_err-{n:02d}.txt").write_text(r.stdout[-4000:] + "\n---STDERR---\n" + r.stderr[-2000:])
        return None
    out = IMG / f"img-{n:02d}.png"
    out.write_bytes(base64.b64decode(b64))
    return out


for item in CFG["images"]:
    n = item["n"]
    if only and n not in only:
        continue
    dest = IMG / f"img-{n:02d}.png"
    if dest.exists() and not only:
        print(f"[{n:02d}] ja existe, pulando", flush=True)
        continue
    prompt = item["prompt"] if "prompt" in item else (CFG[item.get("base","base")] + (CFG["cinema"] if item.get("cinema") else "") + (CFG["fit"] if item.get("fit") else "") + " SCENE: " + CFG[item.get("setting","setting")] + item["scene"])

    for attempt in (1, 2, 3):
        t0 = time.time()
        res = gen(n, prompt)
        if res:
            print(f"[{n:02d}] OK em {time.time()-t0:.0f}s -> {res.name}", flush=True)
            break
        print(f"[{n:02d}] FALHOU tentativa {attempt} ({time.time()-t0:.0f}s)", flush=True)
        time.sleep(5)
print("FIM", flush=True)
