#!/bin/bash
# uso: gen.sh <numero> "<cena em ingles>"
set -e
N=$(printf "%02d" "$1"); CENA="$2"; PORT=10531
BASE="/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/77_dia-da-virada"
TMP="$BASE/_scripts/tmp"; mkdir -p "$TMP" "$BASE/imagens"
OUT="$BASE/imagens/img-$N.png"

ESTILO="black-and-white editorial vintage documentary photograph, desaturated, high contrast, grainy film. WIDE HORIZONTAL LANDSCAPE orientation, 3:2 aspect ratio, much wider than tall. The subject sits LOW in the frame with a large pale and empty upper half for clean compositing. Brazilian small-business setting, humble and real, never corporate. No text, no words, no letters, no numbers, no logos, no emojis, no gradients, no added color, no stock photo look."

PROMPT=$(python3 -c "
import json,sys
print(json.dumps(sys.argv[1]+' '+sys.argv[2])[1:-1])
" "$CENA" "$ESTILO")

cat > "$TMP/payload-$N.json" <<JSON
{
  "model": "gpt-5.4-mini",
  "input": [
    {"role": "developer", "content": "You are an image generation assistant. Your sole function is to invoke the image_generation tool. Never respond with plain text."},
    {"role": "user", "content": "Generate an image: $PROMPT"}
  ],
  "tools": [{"type": "image_generation", "quality": "medium", "size": "1536x1024", "moderation": "low"}],
  "tool_choice": "auto",
  "stream": true
}
JSON

curl -sS -N -X POST "http://127.0.0.1:$PORT/v1/responses" \
  -H "Content-Type: application/json" -H "Accept: text/event-stream" \
  -d "@$TMP/payload-$N.json" > "$TMP/sse-$N.raw"

python3 - "$TMP/sse-$N.raw" "$OUT" <<'PY'
import json, base64, pathlib, sys
raw = pathlib.Path(sys.argv[1]).read_text()
img=None
for block in raw.split("\n\n"):
    data="".join(l[6:] for l in block.split("\n") if l.startswith("data: "))
    if not data or data=="[DONE]": continue
    try: e=json.loads(data)
    except json.JSONDecodeError: continue
    if e.get("type")=="response.output_item.done":
        it=e.get("item",{})
        if it.get("type")=="image_generation_call" and it.get("result"): img=it["result"]
if not img:
    print("ERRO: sem resultado. Trecho:", raw[:400], file=sys.stderr); sys.exit(1)
out=pathlib.Path(sys.argv[2]); out.write_bytes(base64.b64decode(img))
from PIL import Image
im=Image.open(out)
print(f"Salvo: {out.name} {im.size} {'OK landscape' if im.size[0]>im.size[1] else 'REGERAR (veio retrato)'}")
PY
