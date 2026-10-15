#!/usr/bin/env python3
"""2o passe: corrige a IDADE do rosto na cena, com as duas fotos reais como referencia."""
import base64, json, pathlib, subprocess, sys, time

SCR = pathlib.Path(__file__).parent
IMG = SCR.parent / "imagens"
URL = "http://127.0.0.1:10531/v1/responses"
DEV = "You are an image generation assistant. Your sole function is to invoke the image_generation tool. Never respond with plain text."

cena  = base64.b64encode((IMG / "img-04.png").read_bytes()).decode()
rosto_a = base64.b64encode((SCR / "_rosto-a.png").read_bytes()).decode()
rosto_b = base64.b64encode((SCR / "_rosto-b.png").read_bytes()).decode()

prompt = (
    "The FIRST image is a black-and-white photograph of two men at a wooden desk. "
    "The SECOND and THIRD images are photographs of the same specific real man, from two angles. "
    "Reproduce the FIRST image EXACTLY: same square composition, same two men, same poses, same desk and "
    "scattered papers, same pointing hand, same window light from the left, same pale hazy background, same "
    "black-and-white desaturated film grain, same framing. "
    "The ONE change: make the face of the man on the right match the real man in the SECOND and THIRD images "
    "much more closely, and above all make him look his real age, around sixty years old. He currently looks "
    "far too young and too smooth. Give him the heavier, fuller face of the reference: broader jaw and fuller "
    "cheeks, a soft double chin under the jawline, visible creases running from the nose to the corners of the "
    "mouth, crow\'s feet and clear lines around the eyes, a lined forehead, heavier upper eyelids, and mature "
    "skin texture rather than smooth young skin. Keep his thick dark side-parted hair with grey only at the "
    "temples. Keep the same light buttoned dress shirt with rolled sleeves, the same seated pose on the corner "
    "of the desk, the same downward gaze at the papers, the same faint smile. "
    "Render him in the same black-and-white grainy documentary style as the rest of the photograph. "
    "Change absolutely nothing else in the image. No text, no words, no letters, no numbers, no logos, no added color."
)

payload = {
    "model": "gpt-5.4-mini",
    "input": [
        {"role": "developer", "content": DEV},
        {"role": "user", "content": [
            {"type": "input_text", "text": f"Generate an image: {prompt}"},
            {"type": "input_image", "image_url": f"data:image/png;base64,{cena}"},
            {"type": "input_image", "image_url": f"data:image/png;base64,{rosto_a}"},
            {"type": "input_image", "image_url": f"data:image/png;base64,{rosto_b}"},
        ]},
    ],
    "tools": [{"type": "image_generation", "quality": "high", "size": "1024x1024", "moderation": "low"}],
    "tool_choice": "required",
    "stream": True,
}
pf = SCR / "_payload-idade.json"
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
    (SCR / "_err-idade.txt").write_text(r.stdout[-4000:] + "\n---\n" + r.stderr[-2000:])
    print(f"FALHOU em {time.time()-t0:.0f}s"); sys.exit(1)
out = IMG / "img-06.png"
out.write_bytes(base64.b64decode(b64))
print(f"OK em {time.time()-t0:.0f}s -> {out.name}")
