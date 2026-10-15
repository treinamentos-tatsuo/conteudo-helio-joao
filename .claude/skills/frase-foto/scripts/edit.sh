#!/bin/bash
# Escreve a frase à mão sobre a base (papel ou vidro) com o gpt-image-2 (image-edit).
# Copiado de conteudo/carrosseis/210_quebra-por-trabalhar-errado/_scripts/edit.sh (o mesmo usado do 210 ao 228).
#
# uso (da raiz do projeto):
#   .claude/skills/frase-foto/scripts/edit.sh conteudo/carrosseis/N_slug/imagens/base-vidro.png conteudo/carrosseis/N_slug/imagens/vidro-v1.png "PROMPT"
# Prompts-modelo: .claude/skills/frase-foto/templates/b-prompt-vidro.txt e b-prompt-papel.txt
#
# Precisa do proxy openai-oauth na porta 10531 (ver .claude/skills/gpt-image2-ratos/SKILL.md).
# O prompt vai com --form-string: com -F o motor ignora o texto e inventa outra frase (07/10).
# Tenta 3 vezes. Cada geração leva de 1 a 3 minutos.
for i in 1 2 3; do
  curl -sS -m 500 -X POST http://127.0.0.1:10531/v1/images/edits -F model=gpt-image-2 -F "image=@$1" -F size=1024x1536 -F quality=high --form-string "prompt=$3" > "$2.json"
  python3 -c "import json,base64,sys;d=json.load(open('$2.json'));open('$2','wb').write(base64.b64decode(d['data'][0]['b64_json']))" 2>/dev/null && { rm "$2.json"; echo "OK $2"; exit 0; }
  sleep 5
done
echo "FALHOU $2 (ver $2.json)"
exit 1
