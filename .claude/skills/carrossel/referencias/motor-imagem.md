# Motor de imagem — como operar (compartilhado entre modelos)

> Este arquivo é sobre COMO dirigir o gerador. O QUE gerar (estilo, orientação, composição, layout no slide) é definido na seção **Estilo de imagem** do modelo escolhido.

## Engine: gpt-image2-ratos

Usar a skill `.claude/skills/gpt-image2-ratos/` (fica no projeto). Roda pelo plano ChatGPT do usuário via OAuth — sem API key, sem custo direto. É encanamento puro de geração; serve qualquer projeto. Esta skill só a chama.

- Latência de **20-110 s por imagem** → gerar **uma por vez**, nunca todas de uma vez.
- Modo **text-to-image** (`/v1/images/generations`, sem imagem de referência).
- Mostrar cada imagem e **esperar aprovação** antes de gerar a próxima. Ajuste → regerar só aquela.
- Alternativa rápida/grátis: `nanobanana-ratos` (Gemini) se a latência incomodar.

## Chamada: endpoint direto `/v1/images/generations` com `gpt-image-2` (desde 2026-09-09)

O `gen.py` faz um POST no proxy, direto no endpoint de imagem:

```
POST http://127.0.0.1:10531/v1/images/generations
{"model": "gpt-image-2", "prompt": "...", "size": "1536x1024", "n": 1, "quality": "high"}
```

A imagem volta em `data[0].b64_json`. O `size` sai do modelo escolhido (`1536x1024` no carrossel landscape, `1024x1024` na frase quadrada). No carrossel 107 foram 19 imagens sem falha, de 20 a 110 s cada, com o landscape respeitado. **`gen.py` de referência: `conteudo/carrosseis/107_outro-bicho/_scripts/gen.py`** (os dos posts recentes, como o 231, são o mesmo script).

Com imagem de referência (image-edit, usado nas frases de papel e vidro): `POST /v1/images/edits` em multipart, com o prompt em `--form-string` (com `-F` o texto é ignorado e o motor inventa a frase). Exemplo pronto: `conteudo/carrosseis/210_quebra-por-trabalhar-errado/_scripts/edit.sh`.

**O caminho antigo morreu.** Até 09/09 o `gen.py` chamava `/v1/responses` com um modelo de texto (`gpt-5.4-mini` até 07/09, `gpt-5.5` em 08/09) que invocava a tool `image_generation`. Em 09/09 o `gpt-5.5` passou a devolver `model_not_found`, e os outros modelos de texto do proxy respondem vazio sem chamar a tool. **Todo `gen.py` de carrossel anterior ao 107 está no caminho morto:** ao copiar um deles, trocar pelo do 107. Falha em 0-1 s com `model_not_found` é isso, não é token nem proxy. Em qualquer falha, ler `_scripts/_err-NN.txt` ANTES de reiniciar proxy ou pedir login (a ordem de investigação abaixo vale só quando o erro é 401).

## Gotchas (verdades técnicas do gpt-image-2)

1. **Devolve retrato por padrão.** Mesmo passando `size` landscape, o modelo tende a entregar retrato. Por isso, quando o modelo quer landscape, travar a orientação NO PROMPT (`WIDE HORIZONTAL LANDSCAPE orientation, 3:2 aspect ratio, much wider than tall`) e **validar a dimensão gerada** (conferir largura vs. altura). Se vier errado, regerar reforçando. Não confiar só no parâmetro `size`.
2. **Image-edit copia as figuras da referência.** Se passar uma foto como `input_image`, o modelo cola pedaços reconhecíveis dela no resultado (vira colagem). Por isso: **gerar autêntico (text-to-image) OU usar um recorte pronto direto — nunca misturar.** Banco de referências serve como referência de ESTILO descrita em texto no prompt, nunca como `input_image`.

## Validar a FAIXA DO TOPO — obrigatório (02/09/2026)

É o que decide se a foto funde no linho ou parece recorte colado. Rodar depois de gerar, antes de renderizar:

```bash
python3 .claude/skills/carrossel/referencias/topo.py       # todas
python3 .claude/skills/carrossel/referencias/topo.py 5 14  # só essas
```
Reprova por **média < 170** (topo escuro demais: no `multiply` vira mancha) ou **desvio > 28** (tem
objeto atravessando a faixa — telhado, viga, prateleira, cabeça — e aí a emenda aparece). Calibrado
com o veredito do user no carrossel 81. Imagem reprovada se regera com a cláusula de topo reforçada;
ver `erros-frequentes.md` 2026-09-02.

## Validar dimensão (snippet)

```bash
python3 -c "from PIL import Image; im=Image.open('img-03.png'); print(im.size, 'OK' if im.size[0]>im.size[1] else 'REGERAR')"
```

## Fluxo

1. Montar prompt = **estilo-base do modelo** + a cena daquele slide (guiada pelo contexto do slide no `carousel-text.md`).
2. Gerar 1 imagem (text-to-image, size do modelo). Salvar em `conteudo/carrosseis/[N]_[nome]/imagens/img-0X.png`.
3. Validar dimensão/orientação. Mostrar. Aprovou → próxima. Não → regerar só aquela.

## Render dos slides (Playwright)

```bash
npx playwright screenshot --viewport-size=1080,1350 --wait-for-timeout=1100 "slide-01.html" "slide-01.png"
```
O `--wait-for-timeout` dá tempo da fonte do Google Fonts carregar antes do print. TikTok: `--viewport-size=1080,1920`.

## Gotcha de proxy: `401 token_revoked` quase nunca é o login (2026-08-27, carrossel 62)

**Sintoma:** as primeiras imagens geram normalmente e de repente todas falham em 0s com
`{"code": "token_revoked", "status": 401}`.

**Diagnóstico errado (e caro):** pedir pro user rodar `npx @openai/codex login`. No carrossel 62 isso
foi feito, o login funcionou, geraram mais 3 imagens e o erro voltou — porque a causa era outra.

**Causa real:** o proxy `openai-oauth` fica de pé entre sessões (a skill manda não matar). Depois de
muitas horas no ar (no caso, ~9h) ele segura em memória um token já rotacionado e continua mandando
esse, mesmo com o `~/.codex/auth.json` fresco no disco.

**Ordem de investigação (fazer nesta ordem):**
1. `ps -o etime= -p $(lsof -t -nP -iTCP:10531 -sTCP:LISTEN)` — proxy de pé há horas é o suspeito nº 1.
2. **Reiniciar o proxy** e testar uma imagem:
   ```bash
   lsof -ti:10531 | xargs kill; sleep 2
   (npx -y openai-oauth --port 10531 > /tmp/proxy.log 2>&1 &)
   ```
3. **Só se ainda falhar**, aí sim pedir o re-login pro user (`npx @openai/codex login`) — é fluxo de
   navegador com a senha dele, então nunca é o Claude que roda.

**Segunda causa, confirmada em 2026-09-04 (carrossel 90): o token no disco já nasce revogado.** Sintoma
que separa das duas: o proxy **recém-subido morre no boot** com `Encountered invalidated oauth token for
user, failing request` no log e a porta 10531 nem abre (`curl` dá "Failed to connect"), mesmo com
`~/.codex/auth.json` recém-gravado (`last_refresh` de minutos atrás). Reiniciar não resolve, porque o
proxy novo lê do disco um refresh token que a OpenAI já invalidou. Causa provável: **renovação concorrente
do mesmo token por mais de um proxy** (sessões paralelas do Claude na mesma máquina, cada uma com o seu
`openai-oauth`, e as duas gerando ao mesmo tempo); o refresh token rotaciona e o segundo a renovar perde.
No 90 o 401 começou no exato momento em que dois `gen.py` rodavam em paralelo. **Aqui o re-login é o
conserto certo e o único**, e resolveu de primeira. Regra prática que sai daí: o passo 1 vira *"o proxy
está de pé?"* — se `lsof` não mostra a porta e o log tem a linha acima, pular o reinício e pedir o login.

**Correção (user, 09/09/2026, carrossel 105):** a coincidência com dois `gen.py` em paralelo era n=1 e
NÃO virou regra. Gerar em paralelo entre sessões (e dentro da mesma sessão, ex. regen de uma imagem
enquanto a fila principal roda) é prática normal e funciona: *"da pra gerar ao mesmo tempo, ja fizemos isso
varias vezes"*. Ver outro `gen.py` ativo não é motivo pra parar nem enfileirar. Se aparecer `401
token_revoked`, investigar proxy (idade, reinício) e login, nunca a concorrência.

A troubleshooting da skill global `gpt-image2-ratos` manda relogar direto no 401. Está incompleta:
reiniciar o proxy vem antes, é local, e resolve o caso comum sem custar nada pro user.
