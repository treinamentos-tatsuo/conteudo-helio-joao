#!/usr/bin/env python3
"""Image-edit do gpt-image-2: usa a imagem JA PROCESSADA como referencia e altera so o que o prompt nomeia."""
import base64, json, pathlib, subprocess, sys

SCR = pathlib.Path(__file__).parent
IMG = SCR.parent / "imagens"
URL = "http://127.0.0.1:10531/v1/responses"
DEV = "You are an image editing assistant. Your sole function is to invoke the image_generation tool. Never respond with plain text."

EDITS = {
 11: ("Keep this photograph EXACTLY as it is: same man, same pose, same face, same shirt, same wooden bench, "
      "same cracked wall, same framed picture of the empty shed on the wall, same crate, same scale, same lighting, "
      "same film grain, same framing, same black-and-white look. Add ONLY two things. FIRST: the man's closed right "
      "hand resting on the bench is now gripping a single detached worn wooden stool leg, held upright in his fist. "
      "SECOND: lying on its side on the bench top next to him is a worn three-legged wooden stool with ONE LEG "
      "MISSING, its empty socket clearly visible, the same weathered wood as the leg in his hand. "
      "Change absolutely nothing else in the image."),
 13: ("Keep this photograph EXACTLY as it is: same man, same pose, same face, same shirt, same workbench, same "
      "three-legged wooden stool on the left, same tools hanging on the wall, same shelves, same vice, same lighting, "
      "same film grain, same framing, same black-and-white look. Change ONLY the metal toolbox sitting on the stool: "
      "it is now OPEN with its lid raised, and it is crammed full of banknotes, thick stacks of bills spilling over "
      "the edges and almost overflowing out of it. Change absolutely nothing else in the image."),
}

def edit(n, prompt):
    src = IMG / f"img-{n:02d}.png"
    b64in = base64.b64encode(src.read_bytes()).decode()
    payload = {
        "model": "gpt-5.4-mini",
        "input": [
            {"role": "developer", "content": DEV},
            {"role": "user", "content": [
                {"type": "input_image", "image_url": f"data:image/png;base64,{b64in}"},
                {"type": "input_text", "text": f"Edit this image: {prompt}"},
            ]},
        ],
        "tools": [{"type": "image_generation", "quality": "medium", "size": "1024x1024", "moderation": "low"}],
        "tool_choice": "required",
        "stream": True,
    }
    pf = SCR / f"_edit-{n:02d}.json"
    pf.write_text(json.dumps(payload))
    r = subprocess.run(["curl", "-sS", "-N", "-X", "POST", URL, "-H", "Content-Type: application/json",
                        "-H", "Accept: text/event-stream", "-d", f"@{pf}"],
                       capture_output=True, text=True, timeout=900)
    pf.unlink(missing_ok=True)
    out = None
    for block in r.stdout.split("\n\n"):
        data = "".join(l[6:] for l in block.split("\n") if l.startswith("data: "))
        if not data or data == "[DONE]":
            continue
        try:
            e = json.loads(data)
        except json.JSONDecodeError:
            continue
        if e.get("type") == "response.output_item.done":
            it = e.get("item", {})
            if it.get("type") == "image_generation_call" and it.get("result"):
                out = it["result"]
    if not out:
        (SCR / f"_err-edit-{n:02d}.txt").write_text(r.stdout[-3000:])
        return False
    # versiona o raw antigo (nunca rm) pra dar pra voltar
    raw = IMG / "_raw" / f"img-{n:02d}.png"
    if raw.exists():
        raw.rename(IMG / "_raw" / f"img-{n:02d}-v1.png")
    src.write_bytes(base64.b64decode(out))
    return True

for n in [int(a) for a in sys.argv[1:]] or sorted(EDITS):
    print(f"[{n:02d}] {'OK' if edit(n, EDITS[n]) else 'FALHOU'}", flush=True)
