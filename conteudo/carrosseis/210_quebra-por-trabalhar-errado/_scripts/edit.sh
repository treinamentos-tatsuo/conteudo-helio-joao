#!/bin/bash
# uso: edit.sh REF OUT "PROMPT"
for i in 1 2 3; do
  curl -sS -m 500 -X POST http://127.0.0.1:10531/v1/images/edits -F model=gpt-image-2 -F "image=@$1" -F size=1024x1536 -F quality=high --form-string "prompt=$3" > "$2.json"
  python3 -c "import json,base64,sys;d=json.load(open('$2.json'));open('$2','wb').write(base64.b64decode(d['data'][0]['b64_json']))" 2>/dev/null && { rm "$2.json"; echo "OK $2"; exit 0; }
  sleep 5
done
echo "FALHOU $2"
