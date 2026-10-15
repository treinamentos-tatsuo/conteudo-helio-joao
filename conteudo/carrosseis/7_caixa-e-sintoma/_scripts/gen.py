#!/usr/bin/env python3
"""Gera as imagens do carrossel 7 via gpt-image2 (proxy openai-oauth). Uma por vez.

Uso:  python3 gen.py            -> gera as que faltam
      python3 gen.py 3 7 12     -> regera so essas (sobrescreve)
"""
import base64, json, pathlib, subprocess, sys, time

SCR = pathlib.Path(__file__).parent
IMG = SCR.parent / "imagens"
IMG.mkdir(exist_ok=True)
CFG = json.loads((SCR / "prompts.json").read_text())
PORT = 10531
URL = f"http://127.0.0.1:{PORT}/v1/responses"

only = [int(a) for a in sys.argv[1:]]


def gen(n, kind, scene):
    base = CFG["cutout"] if kind == "cutout" else CFG["base"]
    prompt = f"{base} SCENE: {scene}"
    payload = {
        "model": "gpt-5.4-mini",
        "input": [
            {"role": "developer", "content": "You are an image generation assistant. Your sole function is to invoke the image_generation tool. Never respond with plain text."},
            {"role": "user", "content": f"Generate an image: {prompt}"},
        ],
        "tools": [{"type": "image_generation", "quality": "high", "size": "1024x1024", "moderation": "low"}],
        "tool_choice": "auto",
        "stream": True,
    }
    p = SCR / "_payload.json"
    p.write_text(json.dumps(payload))
    r = subprocess.run(
        ["curl", "-sS", "-N", "-X", "POST", URL, "-H", "Content-Type: application/json",
         "-H", "Accept: text/event-stream", "-d", f"@{p}"],
        capture_output=True, text=True, timeout=600,
    )
    b64 = None
    for block in r.stdout.split("\n\n"):
        data = "".join(l[6:] for l in block.split("\n") if l.startswith("data: "))
        if not data or data == "[DONE]":
            continue
        try:
            e = json.loads(data)
        except json.JSONDecodeError:
            continue
        if e.get("type") == "response.output_item.done":
            item = e.get("item", {})
            if item.get("type") == "image_generation_call" and item.get("result"):
                b64 = item["result"]
    if not b64:
        return None
    out = IMG / f"img-{n:02d}.png"
    out.write_bytes(base64.b64decode(b64))
    return out


for item in CFG["images"]:
    n, kind = item["n"], item["kind"]
    if only and n not in only:
        continue
    dest = IMG / f"img-{n:02d}.png"
    if not only and dest.exists():
        print(f"[{n:02d}] ja existe, pulando", flush=True)
        continue
    for attempt in (1, 2):
        t0 = time.time()
        try:
            r = gen(n, kind, item["scene"])
        except Exception as exc:
            r = None
            print(f"[{n:02d}] excecao: {exc}", flush=True)
        if r:
            from PIL import Image
            print(f"[{n:02d}] OK {Image.open(r).size} em {time.time()-t0:.0f}s", flush=True)
            break
        print(f"[{n:02d}] FALHOU (tentativa {attempt})", flush=True)
        time.sleep(5)
print("FIM", flush=True)
