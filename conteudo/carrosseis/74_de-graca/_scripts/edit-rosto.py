#!/usr/bin/env python3
"""Image-edit: troca o rosto do homem mais velho da cena pelo rosto real do Helio.
Duas input_images: [1] a cena aprovada, [2] o rosto do Helio."""
import base64, json, pathlib, subprocess, sys, time

SCR = pathlib.Path(__file__).parent
IMG = SCR.parent / "imagens"
PORT = 10531
URL = f"http://127.0.0.1:{PORT}/v1/responses"
DEV = "You are an image generation assistant. Your sole function is to invoke the image_generation tool. Never respond with plain text."

cena = base64.b64encode((IMG / "img-02.png").read_bytes()).decode()
rosto = base64.b64encode((SCR / "_helio-rosto.png").read_bytes()).decode()

prompt = (
    "The FIRST image is a black-and-white photograph of two men at a wooden desk. "
    "The SECOND image is a colour photograph of a specific real man. "
    "Reproduce the FIRST image EXACTLY: same square composition, same two men, same poses and gestures, "
    "same desk with scattered papers, same pointing hand, same window light from the left, same pale hazy "
    "background, same black-and-white desaturated film grain, same framing. "
    "The ONE change: the face and head of the OLDER man on the right must become the face and head of the man "
    "in the SECOND image. Match his facial features faithfully — the shape of his eyes, his nose, his mouth, "
    "his cheekbones, his short dark side-parted hair and his hairline. He keeps the same light buttoned dress "
    "shirt with rolled sleeves, the same seated pose on the corner of the desk, the same downward gaze at the "
    "papers. Render him in the same black-and-white grainy documentary style as the rest of the photograph, "
    "not as a colour portrait. Change absolutely nothing else in the image. "
    "No text, no words, no letters, no numbers, no logos, no added color."
)

payload = {
    "model": "gpt-5.4-mini",
    "input": [
        {"role": "developer", "content": DEV},
        {"role": "user", "content": [
            {"type": "input_text", "text": f"Generate an image: {prompt}"},
            {"type": "input_image", "image_url": f"data:image/png;base64,{cena}"},
            {"type": "input_image", "image_url": f"data:image/png;base64,{rosto}"},
        ]},
    ],
    "tools": [{"type": "image_generation", "quality": "high", "size": "1024x1024", "moderation": "low"}],
    "tool_choice": "required",
    "stream": True,
}
pf = SCR / "_payload-rosto.json"
pf.write_text(json.dumps(payload))
t0 = time.time()
r = subprocess.run(["curl", "-sS", "-N", "-X", "POST", URL, "-H", "Content-Type: application/json",
                    "-H", "Accept: text/event-stream", "-d", f"@{pf}"], capture_output=True, text=True, timeout=900)
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
    (SCR / "_err-rosto.txt").write_text(r.stdout[-4000:] + "\n---\n" + r.stderr[-2000:])
    print(f"FALHOU em {time.time()-t0:.0f}s — ver _err-rosto.txt")
    sys.exit(1)
out = IMG / "img-04.png"
out.write_bytes(base64.b64decode(b64))
print(f"OK em {time.time()-t0:.0f}s -> {out.name}")
