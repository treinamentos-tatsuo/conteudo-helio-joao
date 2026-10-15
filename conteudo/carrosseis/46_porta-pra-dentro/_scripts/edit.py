#!/usr/bin/env python3
"""Image-edit via gpt-image2 (proxy local): input_image = imagem atual, prompt cirúrgico. Uso: edit.py N "prompt" """
import base64, json, pathlib, subprocess, sys, time

SCR = pathlib.Path(__file__).parent
IMG = SCR.parent / "imagens"
URL = "http://127.0.0.1:10531/v1/responses"
DEV = "You are an image generation assistant. Your sole function is to invoke the image_generation tool. Never respond with plain text."

n = int(sys.argv[1])
prompt = sys.argv[2]
src = IMG / f"img-{n:02d}.png"
b64in = base64.b64encode(src.read_bytes()).decode()

payload = {
    "model": "gpt-5.4-mini",
    "input": [
        {"role": "developer", "content": DEV},
        {"role": "user", "content": [
            {"type": "input_image", "image_url": f"data:image/png;base64,{b64in}"},
            {"type": "input_text", "text": prompt},
        ]},
    ],
    "tools": [{"type": "image_generation", "quality": "medium", "size": "1024x1024", "moderation": "low"}],
    "tool_choice": "required",
    "stream": True,
}
pf = SCR / f"_payload-edit-{n:02d}.json"
pf.write_text(json.dumps(payload))
t0 = time.time()
r = subprocess.run(
    ["curl", "-sS", "-N", "-X", "POST", URL, "-H", "Content-Type: application/json",
     "-H", "Accept: text/event-stream", "-d", f"@{pf}"],
    capture_output=True, text=True, timeout=600,
)
pf.unlink(missing_ok=True)
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
    (SCR / f"_err-edit-{n:02d}.txt").write_text(r.stdout[-4000:] + "\n---STDERR---\n" + r.stderr[-2000:])
    print(f"[{n:02d}] EDIT FALHOU ({time.time()-t0:.0f}s)")
    sys.exit(1)
src.write_bytes(base64.b64decode(b64))
print(f"[{n:02d}] EDIT OK em {time.time()-t0:.0f}s")
