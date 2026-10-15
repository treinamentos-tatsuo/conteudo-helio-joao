---
name: gpt-image2-ratos
description: Gera imagens via gpt-image-2 (OpenAI) usando OAuth do plano ChatGPT do user — sem API key, sem custo direto. Lê ~/.codex/auth.json (login feito uma vez via Codex CLI) e dispara um proxy local openai-oauth que roteia pelo backend Codex. Suporta text-to-image e image-edit (referência por upload, endpoint /v1/images/edits). Setup conversacional do estilo a cada uso. Latência de 20-110 s por imagem. Use quando o user paga ChatGPT Plus/Pro e não quer cobrar API. Pra iteração rápida ou usuários sem plano pago, usar image-gen-ratos (FAL) ou nanobanana-ratos (Gemini).
---

# gpt-image2-ratos

Skill de geração de imagens via **gpt-image-2** usando **OAuth do plano ChatGPT do user**. Sem API key, sem custo direto — queima limite do plano.

Pra usuários que pagam ChatGPT Plus/Pro/Business/Enterprise. Pra usuários sem plano, redirecionar pra [`/image-gen-ratos`](https://github.com/duduesh/image-gen-ratos) (FAL) ou [`/nanobanana-ratos`](https://github.com/duduesh/nanobanana-ratos) (Gemini).

## Aviso de latência (importante)

Antes de gerar, deixar claro pro user que cada imagem leva de **20 a 110 segundos** (medido no carrossel 107, 19 imagens). Isso é o overhead do proxy OAuth + geração do gpt-image-2.

Se o user quer 5+ variações pra escolher, sugerir usar `image-gen-ratos` (FAL) em vez disso. Aqui a skill brilha quando é "1 imagem boa final".

## Setup (primeira vez)

A skill **não tem .env**. Toda a auth vem do `~/.codex/auth.json` que o Codex CLI cria. O fluxo de setup é:

### 1. Verificar pré-requisitos

```bash
test -f ~/.codex/auth.json && echo "OK_AUTH" || echo "NO_AUTH"
which node npx && node --version
which python3
```

### 2. Se `~/.codex/auth.json` NÃO existe

Mostrar ao user:

> Pra usar essa skill tu precisa logar no Codex CLI uma vez (vai abrir o browser). Roda isso no terminal e me avisa quando terminar:
>
> ```bash
> npx @openai/codex login
> ```
>
> Depois disso o token fica salvo em `~/.codex/auth.json` e dura meses. Tu não precisa logar de novo.
>
> Se tu não tem plano ChatGPT pago, essa skill não funciona. Usa `/image-gen-ratos` (FAL, $0.06/imagem) ou `/nanobanana-ratos` (Gemini, grátis) em vez disso.

### 3. Se `~/.codex/auth.json` JÁ existe

Seguir direto pro fluxo de geração. Não precisa de setup adicional.

## Estilo visual (conversacional, NÃO hardcoded)

Igual a `image-gen-ratos`. A skill **não força** nenhum estilo. Cada projeto/marca/canal tem o seu.

No início de cada sessão (a primeira vez que o user pedir imagem na conversa atual), perguntar:

> Como tu quer o estilo? 4 caminhos:
>
> 1. **Livre** — descreve em palavras
> 2. **Brand guide** — cola aqui o teu DNA visual ou aponta pra um arquivo
> 3. **Usar exemplo** — tem exemplos em `~/.claude/skills/gpt-image2-ratos/examples/`
> 4. **Sem estilo** — gera puro, sem calibração

Aplicar o estilo escolhido como contexto/prefixo no prompt em inglês. Não perguntar isso a cada imagem da mesma sessão — só na primeira.

## Modos de operação

### Modo direto

User cola um prompt pronto em inglês. Claude só roda.

### Modo assistido (default quando user só passa tema)

User dá um tema curto. Claude:

1. Se ainda não definiu estilo nesta sessão, pergunta
2. Sugere **3 conceitos distintos** em 2-3 linhas cada
3. Pergunta qual vai
4. Quando user escolher: escreve o prompt em **inglês** com detalhes (lighting, câmera, composição, etc)
5. Roda
6. Mostra

## Endpoint (desde 09/09/2026)

A chamada vai **direto no endpoint de imagem do proxy**: `POST /v1/images/generations` com `"model": "gpt-image-2"`. A imagem volta em `data[0].b64_json`.

O caminho antigo morreu: `/v1/responses` com um modelo de texto (`gpt-5.4-mini`, depois `gpt-5.5`) invocando a tool `image_generation`. Em 09/09 o `gpt-5.5` passou a devolver `model_not_found` e os outros modelos de texto do proxy respondem vazio sem chamar a tool. Script que ainda manda `/v1/responses` ou `"model": "gpt-5.5"` não gera nada: trocar pelo de referência, `conteudo/carrosseis/107_outro-bicho/_scripts/gen.py`.

## Tamanho e quality

| Size | Pra quê |
|---|---|
| `1024x1024` | Quadrado (frase) |
| `1536x1024` | Landscape (slides do carrossel) |
| `1024x1536` | Retrato (image-edit do papel e do vidro) |

São os tamanhos que os scripts da casa usam. A casa gera em `"quality": "high"`.

## Comando base (text-to-image)

```bash
PORT=10531
OUT_DIR="${OUT_DIR:-/tmp/gpt-image2-out}"
mkdir -p "$OUT_DIR"

# 1. Verificar se proxy ja esta rodando
if curl -s -o /dev/null -w "%{http_code}" "http://127.0.0.1:$PORT/v1/models" 2>/dev/null | grep -qE "^(2|4)"; then
  echo "[skill] proxy ja UP"
else
  echo "[skill] subindo proxy openai-oauth na porta $PORT..."
  npx -y openai-oauth --port "$PORT" > "$OUT_DIR/proxy.log" 2>&1 &
  # Esperar proxy ficar disponivel (max 30s)
  for i in $(seq 1 30); do
    if curl -s -o /dev/null -w "%{http_code}" "http://127.0.0.1:$PORT/v1/models" 2>/dev/null | grep -qE "^(2|4)"; then
      echo "[skill] proxy UP (tentativa $i)"
      break
    fi
    sleep 1
  done
fi

# 2. Montar payload e disparar no endpoint direto de imagem
python3 - "$OUT_DIR" <<'PY'
import json, pathlib, sys
out = pathlib.Path(sys.argv[1])
payload = {"model": "gpt-image-2", "prompt": "PROMPT_AQUI", "size": "1024x1024", "n": 1, "quality": "high"}
(out / "payload.json").write_text(json.dumps(payload))
PY
curl -sS -X POST "http://127.0.0.1:$PORT/v1/images/generations" \
  -H "Content-Type: application/json" \
  -d "@$OUT_DIR/payload.json" > "$OUT_DIR/resposta.json"

# 3. Salvar o PNG
python3 - "$OUT_DIR/resposta.json" "OUTPUT_PATH_PLACEHOLDER" <<'PY'
import json, base64, pathlib, sys
d = json.loads(pathlib.Path(sys.argv[1]).read_text())
try:
    b64 = d["data"][0]["b64_json"]
except (KeyError, IndexError, TypeError):
    print("ERRO: sem data[0].b64_json. Resposta:", json.dumps(d)[:2000], file=sys.stderr)
    sys.exit(1)
out = pathlib.Path(sys.argv[2])
out.write_bytes(base64.b64decode(b64))
print(f"Salvo: {out} ({out.stat().st_size} bytes)")
PY
```

Substituir `PROMPT_AQUI` e `OUTPUT_PATH_PLACEHOLDER` antes de rodar. Pra uma fila de imagens, usar o `gen.py` de referência (`conteudo/carrosseis/107_outro-bicho/_scripts/gen.py`: lê `prompts.json`, gera uma por vez, tenta 3 vezes e grava o erro em `_scripts/_err-NN.txt`).

**Não matar o proxy** ao final do request. Deixa rodando pra reusar nas próximas imagens da sessão. Pra parar manualmente: `lsof -ti:10531 | xargs kill`.

## Comando com imagem de referência (image edit)

Endpoint próprio, em multipart: `POST /v1/images/edits`. O prompt vai em `--form-string` (com `-F` o texto é ignorado e o motor inventa o conteúdo):

```bash
curl -sS -m 500 -X POST http://127.0.0.1:10531/v1/images/edits \
  -F model=gpt-image-2 -F "image=@referencia.png" -F size=1024x1536 -F quality=high \
  --form-string "prompt=PROMPT_AQUI" > resposta.json
```

A imagem volta igual, em `data[0].b64_json`. Script pronto com 3 tentativas: `conteudo/carrosseis/210_quebra-por-trabalhar-errado/_scripts/edit.sh`.

## Princípios pra escrever o prompt

1. **Em inglês.** O modelo entende PT mas responde melhor a direção técnica em EN. Texto literal na imagem pode ser em PT.
2. **Texto em quotes.** Pra renderizar verbatim: `reads "[texto em português]"`. ~99% accuracy.
3. **Composição, não intenção.** "Medium shot, subject centered, banker lamp backlighting" > "dramatic portrait".
4. **Listar negativos.** "No emojis, no gradients, no stock photo aesthetic".
5. **Specificity vence.** "Space-black MacBook Pro 16-inch M3" > "a laptop".
6. **Referências cinematográficas (se o estilo pedir).** "In the visual style of Severance office scenes".

## Pós-geração

Mostrar a imagem ao user. Por causa da latência, perguntar **antes** de fazer outra:
- Aprovou? → pergunta onde salvar/publicar
- Quer variação? → ajusta 1 detalhe e roda de novo (avisa que vai levar mais 1-3 min)
- Quer mesma ideia em outro aspect/quality? → rerodar

Não gerar 3 variações em paralelo sem perguntar — cada uma queima quota Codex do plano dele.

## Troubleshooting

**`~/.codex/auth.json` não existe**
User não logou no Codex CLI. Mostrar: `npx @openai/codex login`.

**Proxy não sobe (timeout em 30s)**
Ver `$OUT_DIR/proxy.log`. Causas comuns:
- Porta 10531 ocupada por outro processo: `lsof -i :10531` e matar
- Rede lenta no primeiro download do `openai-oauth` (npx baixa antes de rodar)
- Token expirado e refresh falhou: rodar `npx @openai/codex login` de novo

**`401` ou `403` do proxy**
Token OAuth expirou ou foi revogado. User precisa relogar: `npx @openai/codex login`.

**`429` do proxy**
Limite Codex do plano ChatGPT esgotado. Esperar reset (geralmente a cada 5h).

**Imagem não veio (resposta sem `data[0].b64_json`)**
Ler a resposta salva (no `gen.py`, `_scripts/_err-NN.txt`). `model_not_found` em 0-1 s = script no caminho antigo (`/v1/responses` ou modelo de texto): trocar pelo de referência. Recusa de moderação ou prompt ambíguo: reescrever o prompt.

**Latência muito maior que 110s**
Status do plano ChatGPT pode estar com fila. Verificar [status.openai.com](https://status.openai.com).

**Imagem em PT com acentos quebrados**
Encurtar a string. Confirmar que tá em quotes: `reads "texto"`.

## Custos reais (atenção)

A skill é "free" no sentido de não cobrar API extra, mas **queima limite do plano ChatGPT**. Por doc oficial da OpenAI, image generation consome limite Codex **3-5x mais rápido** que turn de texto.

Avisar o user no setup:

> Heads up: cada imagem aqui usa parte da tua quota Codex do plano ChatGPT. Se tu também usa Codex CLI pra coding, isso compete pelo mesmo limite. No Plus ($20/mês), tu provavelmente consegue gerar ~6-30 imagens medium em cada janela de 5h, mas isso vai depender do uso normal do Codex.

## Referências

- Exemplos de estilo: `~/.claude/skills/gpt-image2-ratos/examples/`
- [Pacote openai-oauth (proxy local)](https://github.com/EvanZhouDev/openai-oauth)
- [Codex CLI Authentication (OpenAI)](https://developers.openai.com/codex/auth)
- [Codex CLI Features (image generation)](https://developers.openai.com/codex/cli/features)
- Skill complementar (FAL, paga): `/image-gen-ratos`
- Skill complementar (Gemini, grátis): `/nanobanana-ratos`
