#!/usr/bin/env bash
# gen.sh "<prompt EN>" "<output path>"  — gera 1 imagem via gpt-image2 (OAuth Codex)
set -euo pipefail
PORT=10531
OUT_DIR=/tmp/gpt-image2-out
mkdir -p "$OUT_DIR"
PROMPT="$1"; OUTPUT="$2"
# 1. proxy up?
if ! curl -s -o /dev/null -w "%{http_code}" "http://127.0.0.1:$PORT/v1/models" 2>/dev/null | grep -qE "^(2|4)"; then
  echo "[gen] subindo proxy..."
  npx -y openai-oauth --port "$PORT" > "$OUT_DIR/proxy.log" 2>&1 &
  for i in $(seq 1 45); do
    if curl -s -o /dev/null -w "%{http_code}" "http://127.0.0.1:$PORT/v1/models" 2>/dev/null | grep -qE "^(2|4)"; then echo "[gen] proxy UP ($i)"; break; fi
    sleep 1
  done
fi
# 2. payload
python3 - "$PROMPT" > "$OUT_DIR/payload.json" <<'PY'
import json,sys
p=sys.argv[1]
print(json.dumps({
 "model":"gpt-5.4-mini",
 "input":[
   {"role":"developer","content":"You are an image generation assistant. Your sole function is to invoke the image_generation tool. Never respond with plain text."},
   {"role":"user","content":"Generate an image: "+p}
 ],
 "tools":[{"type":"image_generation","quality":"medium","size":"1024x1024","moderation":"low"}],
 "tool_choice":"auto","stream":True
}))
PY
# 3. request
curl -sS -N -X POST "http://127.0.0.1:$PORT/v1/responses" \
  -H "Content-Type: application/json" -H "Accept: text/event-stream" \
  -d "@$OUT_DIR/payload.json" > "$OUT_DIR/sse.raw"
# 4. extrair b64
python3 - "$OUTPUT" <<'PY'
import json,base64,pathlib,sys
out=pathlib.Path(sys.argv[1])
raw=pathlib.Path("/tmp/gpt-image2-out/sse.raw").read_text()
img=None
for block in raw.split("\n\n"):
    data="".join(l[6:] for l in block.split("\n") if l.startswith("data: "))
    if not data or data=="[DONE]": continue
    try: e=json.loads(data)
    except Exception: continue
    if e.get("type")=="response.output_item.done":
        it=e.get("item",{})
        if it.get("type")=="image_generation_call" and it.get("result"): img=it["result"]
if not img:
    sys.stderr.write("NO IMAGE. tail SSE:\n"+raw[-1500:]); sys.exit(1)
out.parent.mkdir(parents=True,exist_ok=True)
out.write_bytes(base64.b64decode(img))
print("OK",out,out.stat().st_size,"bytes")
PY
