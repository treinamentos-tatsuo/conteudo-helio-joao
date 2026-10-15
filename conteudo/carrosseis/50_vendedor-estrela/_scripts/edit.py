#!/usr/bin/env python3
"""Image-edit (gpt-image-2) da propria imagem processada: estende a cena pra baixo.
Uso: python3 edit.py <n>  — le imagens/img-0N.png, salva o resultado por cima (P&B garantido, sem crop)."""
import base64, json, pathlib, subprocess, sys, time
from PIL import Image
from io import BytesIO

SCR = pathlib.Path(__file__).parent
IMG = SCR.parent / "imagens"
PORT = 10531
URL = f"http://127.0.0.1:{PORT}/v1/responses"

EDITS = {
    1: "Keep this exact photograph: same grinning salesman with his feet up on the desk, same trophy, same rotary phone, same objects on the desktop, same pale hazy background, same carpeted floor visible at the left and right sides of the desk. ONLY change the front panel of the desk: it is too short now, so extend the dark wooden desk front DOWNWARD so it grows toward the camera and bleeds off the bottom edge of the frame, wider at the bottom in natural perspective, while the carpet remains visible in the lower left and lower right corners beside the desk. Same black-and-white grain and lighting. Nothing else changes.",
    2: "Extend this canvas DOWNWARD so the final image is roughly one quarter taller than the current one. Everything currently visible stays absolutely identical and occupies the upper part of the new canvas. Continue the scene naturally downward in the near foreground: the office floorboards and the lower parts of the steel desks and chairs continue toward the camera, same perspective, same light, same heavy film grain, bleeding off the new bottom edge. Change absolutely nothing else: same walking salesman with jacket over his shoulder, same men on phones.",
    5: "Extend this canvas DOWNWARD so the final image is roughly one quarter taller than the current one. Everything currently visible stays absolutely identical and occupies the upper part of the new canvas. Continue the scene naturally downward in the near foreground: the wooden desk surface with its papers and objects continues toward the camera, larger and closer, same lighting, same heavy film grain, bleeding off the new bottom edge. Change absolutely nothing else: same circle of laughing salesmen, same lone young salesman standing apart.",
    7: "Extend this canvas DOWNWARD so the final image is roughly one sixth taller than the current one. Everything currently visible stays absolutely identical and occupies the upper part of the new canvas. Continue the scene naturally downward: the bottom edge of the glowing lightbox and the dark wall below it continue toward the bottom, same glow, same heavy film grain, bleeding off the new bottom edge. Change absolutely nothing else: same X-ray film, same clips, same light.",
}

n = int(sys.argv[1])
prompt = EDITS[n]
src = IMG / f"img-{n:02d}.png"
b64_in = base64.b64encode(src.read_bytes()).decode()

payload = {
    "model": "gpt-5.4-mini",
    "input": [
        {"role": "developer", "content": "You are an image generation assistant. Your sole function is to invoke the image_generation tool. Never respond with plain text."},
        {"role": "user", "content": [
            {"type": "input_text", "text": prompt},
            {"type": "input_image", "image_url": f"data:image/png;base64,{b64_in}"},
        ]},
    ],
    "tools": [{"type": "image_generation", "quality": "medium", "size": "1024x1536", "moderation": "low"}],
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

im = Image.open(BytesIO(base64.b64decode(b64))).convert("L").convert("RGB")  # P&B garantido, SEM crop
im.save(src)
print(f"[{n:02d}] EDIT OK em {time.time()-t0:.0f}s -> {im.size[0]}x{im.size[1]}")
