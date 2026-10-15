#!/usr/bin/env python3
"""Image-edit cirurgico de uma imagem existente (adiciona elemento, congela o resto)."""
import base64, json, pathlib, subprocess, sys, time

SCR = pathlib.Path(__file__).parent
IMG = SCR.parent / "imagens"
PORT = 10531
URL = f"http://127.0.0.1:{PORT}/v1/responses"

DEV = "You are an image generation assistant. Your sole function is to invoke the image_generation tool. Never respond with plain text."

EDITS = {
    7: (
        "Edit this photograph. Remove the walking man entirely, leaving the corridor completely empty. "
        "Fill the space where he was with the continuation of the corridor: the polished reflective floor, "
        "the thin grey smoke drifting low, the far end lost in haze. Change absolutely nothing else: same "
        "corridor, same identical scorched doors, same walls, same smoke, same lighting, same film grain, "
        "same framing, black and white."
    ),
    10: (
        "Edit this photograph. Add ONE subtly demonic elegant hand gripping the top edge of the empty "
        "chair's backrest at the head of the table, as if someone is hiding crouched behind the chair. "
        "The hand emerges from a dark tailored suit sleeve with a white shirt cuff, fingers slightly "
        "elongated with short dark pointed claws, pale taut skin, refined and sinister, no gore, no "
        "flames, no face visible, nothing else of the hidden figure visible. Change absolutely nothing "
        "else: same room, same table, same chairs, same papers, same window, same lighting, same film "
        "grain, same framing, black and white."
    ),
}


def edit(n, prompt):
    src = IMG / f"img-{n:02d}.png"
    b64in = base64.b64encode(src.read_bytes()).decode()
    payload = {
        "model": "gpt-5.4-mini",
        "input": [
            {"role": "developer", "content": DEV},
            {"role": "user", "content": [
                {"type": "input_text", "text": prompt},
                {"type": "input_image", "image_url": f"data:image/png;base64,{b64in}"},
            ]},
        ],
        "tools": [{"type": "image_generation", "quality": "medium", "size": "1024x1024", "moderation": "low"}],
        "tool_choice": "required",
        "stream": True,
    }
    pf = SCR / f"_payload-edit-{n:02d}.json"
    pf.write_text(json.dumps(payload))
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
        return None
    src.write_bytes(base64.b64decode(b64))
    return src


for n in [int(a) for a in sys.argv[1:]] or list(EDITS):
    t0 = time.time()
    res = edit(n, EDITS[n])
    print(f"[{n:02d}] {'OK' if res else 'FALHOU'} em {time.time()-t0:.0f}s", flush=True)
