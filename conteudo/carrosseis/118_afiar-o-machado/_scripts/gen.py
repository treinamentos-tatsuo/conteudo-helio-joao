#!/usr/bin/env python3
"""Gera as imagens do carrossel 118 via gpt-image-2 (proxy openai-oauth local), endpoint DIRETO
/v1/images/generations (referência: gen.py do 107). Uma por vez. Uso: gen.py [n ...]  (n = 1, 2, 3a, 3b ...)."""
import base64, json, pathlib, subprocess, sys, time

SCR = pathlib.Path(__file__).parent
IMG = SCR.parent / "imagens"
IMG.mkdir(parents=True, exist_ok=True)
CFG = json.loads((SCR / "prompts.json").read_text())
URL = "http://127.0.0.1:10531/v1/images/generations"
SIZE = {"base": "1536x1024", "base_portrait": "1024x1536", "base_square": "1024x1024", "base_nowheel": "1536x1024", "base_square_nowheel": "1024x1024"}
only = [a for a in sys.argv[1:]] or None


def gen(tag, prompt, size):
    payload = {"model": "gpt-image-2", "prompt": prompt, "size": size, "n": 1, "quality": "high"}
    pf = SCR / f"_payload-{tag}.json"
    pf.write_text(json.dumps(payload))
    r = subprocess.run(["curl", "-sS", "-X", "POST", URL, "-H", "Content-Type: application/json", "-d", f"@{pf}"],
                       capture_output=True, text=True, timeout=600)
    pf.unlink(missing_ok=True)
    try:
        b64 = json.loads(r.stdout)["data"][0]["b64_json"]
    except Exception:
        (SCR / f"_err-{tag}.txt").write_text(r.stdout[-4000:] + "\n---STDERR---\n" + r.stderr[-2000:])
        return None
    out = IMG / f"img-{tag}.png"
    out.write_bytes(base64.b64decode(b64))
    return out


for item in CFG["images"]:
    n = item["n"]
    tag = f"{n:02d}" if isinstance(n, int) else n
    if only and tag not in only and str(n) not in only:
        continue
    dest = IMG / f"img-{tag}.png"
    if dest.exists() and not only:
        print(f"[{tag}] ja existe, pulando", flush=True); continue
    base = item.get("base", "base")
    prompt = CFG[base] + " " + item["scene"]
    for attempt in (1, 2, 3):
        t0 = time.time()
        res = gen(tag, prompt, SIZE[base])
        if res:
            from PIL import Image
            w, h = Image.open(res).size
            print(f"[{tag}] OK em {time.time()-t0:.0f}s -> {res.name} {w}x{h}", flush=True); break
        print(f"[{tag}] FALHOU tentativa {attempt} ({time.time()-t0:.0f}s)", flush=True); time.sleep(5)
print("FIM", flush=True)
