#!/usr/bin/env python3
"""Image-edit da capa: estende a cena pra baixo (sangria) preservando tudo."""
import base64, json, pathlib, subprocess, time

SCR = pathlib.Path(__file__).parent
IMG = SCR.parent / "imagens"
PORT = 10531
URL = f"http://127.0.0.1:{PORT}/v1/responses"
DEV = "You are an image generation assistant. Your sole function is to invoke the image_generation tool. Never respond with plain text."

src = IMG / "img-01.png"
b64in = base64.b64encode(src.read_bytes()).decode()

prompt = (
    "Extend this exact black-and-white photograph to the LEFT. Everything currently visible must stay "
    "absolutely identical: same four saluting workers, same benches, same lighting, same film grain. "
    "The pointing boss on the left is currently cropped by the left edge: reveal the REST of his body so he "
    "stands FULLY inside the frame, with a clear margin of dark wooden floorboards and hazy factory background "
    "behind him on the left. Same man, same dark three-piece suit, same pose pointing forward. Keep the bottom "
    "floorboards continuous. No new people, no new objects, no text, no words, no letters, no numbers, "
    "no logos, no added color."
)

payload = {
    "model": "gpt-5.4-mini",
    "input": [
        {"role": "developer", "content": DEV},
        {"role": "user", "content": [
            {"type": "input_text", "text": f"Generate an image: {prompt}"},
            {"type": "input_image", "image_url": f"data:image/png;base64,{b64in}"},
        ]},
    ],
    "tools": [{"type": "image_generation", "quality": "medium", "size": "1024x1536", "moderation": "low"}],
    "tool_choice": "required",
    "stream": True,
}
pf = SCR / "_payload-edit02.json"
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
    (SCR / "_err-edit02.txt").write_text(r.stdout[-4000:] + "\n---STDERR---\n" + r.stderr[-2000:])
    raise SystemExit("FALHOU")
out = IMG / "img-01-ext2.png"
out.write_bytes(base64.b64decode(b64))
print(f"OK em {time.time()-t0:.0f}s -> {out.name}")
