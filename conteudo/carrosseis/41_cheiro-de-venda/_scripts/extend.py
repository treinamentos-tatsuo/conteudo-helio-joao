#!/usr/bin/env python3
"""Estende a parte de baixo das imagens 7 e 8 via image-edit (preserva a cena aprovada)."""
import base64, json, pathlib, subprocess, sys, time

SCR = pathlib.Path(__file__).parent
IMG = SCR.parent / "imagens"
RAW = IMG / "_raw"
PORT = 10531
URL = f"http://127.0.0.1:{PORT}/v1/responses"

PROMPTS = {
    7: ("Recreate this exact black-and-white photograph on a slightly taller canvas, EXTENDED DOWNWARD. "
        "Everything currently visible stays identical and occupies the upper four fifths of the new image: "
        "same coffee lady pouring from the thermos, same visitor at the counter, same smiling doorman at the door, "
        "same walls, light and film grain. Below the current bottom edge, continue the scene naturally downward, "
        "adding about one fifth more: the dark wooden reception counter front continuing down and the floor of the lobby. "
        "Black and white, desaturated, heavy film grain, vintage documentary look. "
        "No text, no words, no letters, no logos, no added color."),
    8: ("Recreate this exact black-and-white photograph on a slightly taller canvas, EXTENDED DOWNWARD. "
        "Everything currently visible stays identical and occupies the upper five sixths of the new image: "
        "same vigorous shop owner in apron leaning forward behind his counter, same customers, same goods, "
        "same light and film grain. Below the current bottom edge, continue the scene naturally downward, "
        "adding about one sixth more: the wooden counter front with crates and produce continuing down toward the viewer. "
        "Black and white, desaturated, heavy film grain, vintage documentary look. "
        "No text, no words, no letters, no logos, no added color."),
}

DEV = "You are an image generation assistant. Your sole function is to invoke the image_generation tool. Never respond with plain text."


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
        "tools": [{"type": "image_generation", "quality": "medium", "size": "1024x1536", "moderation": "low"}],
        "tool_choice": "required",
        "stream": True,
    }
    pf = SCR / f"_payload-ext-{n:02d}.json"
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
        (SCR / f"_err-ext-{n:02d}.txt").write_text(r.stdout[-4000:] + "\n---STDERR---\n" + r.stderr[-2000:])
        return None
    return base64.b64decode(b64)


only = [int(a) for a in sys.argv[1:]] or [7, 8]
for n in only:
    # versionar (nunca rm): guarda raw e processada atuais como -v1
    raw_old = RAW / f"img-{n:02d}.png"
    if raw_old.exists():
        raw_old.rename(RAW / f"img-{n:02d}-v1.png")
    proc_v1 = RAW / f"img-{n:02d}-v1-proc.png"
    if not proc_v1.exists():
        proc_v1.write_bytes((IMG / f"img-{n:02d}.png").read_bytes())
    for attempt in (1, 2, 3):
        t0 = time.time()
        data = edit(n, PROMPTS[n])
        if data:
            (IMG / f"img-{n:02d}.png").write_bytes(data)
            print(f"[{n:02d}] EXT OK em {time.time()-t0:.0f}s", flush=True)
            break
        print(f"[{n:02d}] EXT FALHOU tentativa {attempt} ({time.time()-t0:.0f}s)", flush=True)
        time.sleep(5)
print("FIM", flush=True)
