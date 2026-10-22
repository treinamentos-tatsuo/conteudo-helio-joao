import base64, json, subprocess, pathlib
SCR=pathlib.Path(__file__).parent; out=SCR.parent/"imagens/_src"
p=("black-and-white editorial documentary photograph, Brazil, desaturated, high contrast, deep blacks, fine film grain, professional cinematic grade. "
"VERTICAL PORTRAIT orientation, 2:3. COMPOSITION: the subject sits in the LOWER-MIDDLE of the frame; the UPPER 45 percent falls into deep dark shadow, almost black and empty, so white text can sit over it. "
"Low-key warm light from a single pendant lamp. Everything in sharp focus, one single real photographic exposure. No text, no readable words, no numbers, no logos, no added color. NO PEOPLE, no hands, no faces. "
"SCENE: a family dinner table at night in a comfortable Brazilian home, seen from the foot of the table. Three plates already used, napkins crumpled, children's cups. "
"At the head of the table, the father's place is still set and untouched: clean plate, folded napkin, full glass, the chair pushed in and empty. A smartphone face-down next to that plate.")
for k in (1,2):
    pl={"model":"gpt-image-2","prompt":p,"size":"1024x1536","n":1,"quality":"high"}
    (SCR/"_p5.json").write_text(json.dumps(pl))
    r=subprocess.run(["curl","-sS","-X","POST","http://127.0.0.1:10531/v1/images/generations","-H","Content-Type: application/json","-d",f"@{SCR/'_p5.json'}"],capture_output=True,text=True,timeout=600)
    try:
        (out/f"gen-05-v{k}.png").write_bytes(base64.b64decode(json.loads(r.stdout)["data"][0]["b64_json"])); print("ok",k)
    except Exception: print("falhou",k,r.stdout[-300:])
