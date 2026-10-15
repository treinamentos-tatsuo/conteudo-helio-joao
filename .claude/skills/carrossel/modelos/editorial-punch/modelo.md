# Modelo: Editorial-punch

**Em uma linha:** carrossel editorial P&B, frases-punch (setup preto + remate vermelho) costuradas num storytelling encadeado, foto editorial vintage na faixa inferior. O modelo "carro-chefe" da Tatsuo no feed.

> Voz: sempre `referencias/voz-tatsuo.md`. Operação de imagem: `referencias/motor-imagem.md`. Este arquivo define o QUE é o modelo. Não sobrescrever.

---

## 1. Quando usar (propósito / canal)

- **Canal:** feed do Instagram (e versão TikTok opcional). Carrossel educacional/provocativo.
- **Objetivo:** pegar uma dor do empresário, desenvolver com tensão e fechar amarrando a metodologia (MBV: Lucratividade, Crescimento, Cultura) à dor + CTA "Comenta [número]".
- **Quando NÃO usar:** post de uma imagem só, conteúdo de dado/lista pura, ou formato tweet — esses pedem outro modelo.

---

## 2. Arco de texto (a espinha)

Storytelling **encadeado**, não frases soltas. A última linha de cada slide puxa o próximo, e o slide seguinte **responde ou retoma** (ex: termina "...de que fez algo errado." → abre "Não fez."). A virada de página tem que ser inevitável pela tensão, sem "swipe pra ver mais".

Arco típico (adaptar ao tema):

1. **Capa** — promessa/tensão. Setup curto + grito vermelho. O dedo na ferida pode vir já aqui: aperta a dor que o dono sente, não condena o caráter dele (ver `referencias/voz-tatsuo.md` → "Dedo na ferida é condenar a DOR"). A acusação pode ser a entrada ou o destino do arco, conforme o conteúdo.
2. **Hook** — a cena/realidade que todo dono reconhece. Cria a tensão.
3. **Aprofundamento** — por que isso acontece / o tamanho real do problema.
4. **Mecanismo** — o motor por trás. Dado concreto (número + fonte + ano) ou exemplo real e específico.
5. **A armadilha / dúvida** — a leitura errada que a maioria faz (prepara a virada).
6. **Virada** — responde a dúvida e reposiciona (o peso é cargo, não castigo; o topo é trabalho, não prêmio).
7. **Ponte com a metodologia** — o que muda é o método (entra o MBV/comando/clareza).
8. **Fechamento + CTA** — sintetiza o método e chama pra ação.

Não é fixo: alguns temas pedem 2 aprofundamentos, outros 2 provas. Mas **mínimo ~8 slides** — abaixo disso não dá pra construir impacto sólido nem amarrar a metodologia.

**Cada slide adiciona uma camada nova**, nunca repete o anterior com outras palavras. Teste do "e daí?": cada slide responde o "e daí?" do anterior; se não avança a narrativa, cortar.

---

## 3. Nº e formato de slides

- **Mínimo ~8 slides** (varia por tema; 8-10 é a faixa boa).
- **Instagram:** 1080 × 1350px (4:5). **TikTok:** 1080 × 1920px (deixar 230px livres embaixo).

---

## 4. Estrutura por slide + estrofes

Padrão de cada slide: **setup em preto** + **punch em vermelho** (`#A91C20`). Texto curto, no máx ~6 linhas curtas, que respira.

- **2 linhas** (1 setup + 1 punch) = estrofe única, não quebra.
- **4 linhas → 2 estrofes de 2 (2+2)**, com respiro entre elas. NUNCA 3+1.
- **CTA:** estrofe de 2 + a linha de chamada com respiro, número/ação em vermelho.

```html
<div class="stanza">
  <div class="line">linha 1 (setup)</div>
  <div class="line">linha 2</div>
</div>
<div class="stanza">
  <div class="line">linha 3</div>
  <div class="line red">linha 4 (punch)</div>
</div>
```
```css
.line{ font-size:41px; line-height:1.32; font-weight:600; color:#1A1A1A; }
.line.red{ font-weight:700; color:#A91C20; }   /* sem margin próprio */
.stanza + .stanza{ margin-top:34px; }          /* o respiro é da estrofe */
```
Slides de 2 linhas podem usar `font-size:42-44px`. **Capa = 2 linhas, sempre** (setup + grito), em corpo maior (`~50-52px`). Sem subtítulo, sem linha de sussurro, sem terceira linha — regra dura do user (28/08/2026), ver `referencias/erros-frequentes.md`. **Capa toda em Anton reprova** (user, 11/09/2026, carrossel 111: "muito ruim de ler"): o setup vai em Source Serif preto (~48px) e só o grito vai em Anton vermelho. **Grito em Anton numa linha só quando couber, mesmo abaixo de 80px** (user, 13/10/2026; o 201 foi ao ar com 76px numa linha); só quebra quando não couber nem assim. **Exceção do repost (135, 231):** repost com arte nova mantém a capa do original como ela era, com subtítulo e diagramação, mesmo que fuja das 2 linhas.

---

## 5. Regras visuais

- **Fonte:** Source Serif Pro (serif), via Google Fonts. (Montserrat é dos documentos, não do carrossel.)
- **Cores:** preto `#1A1A1A` (corpo), vermelho carmim `#A91C20` (punch/título), fundo linho off-white. **Nunca** branco puro `#FFFFFF` no fundo, nunca o vermelho como bloco de cor.
- **Fundo:** arquivo único e canônico `conteudo/carrosseis/_banco-referencias/background para carrosséis.png` (textura linho) em TODOS os slides — garante cor idêntica no carrossel inteiro. Fallback de cor: `#F5F0EB`.
- **Layout:** texto centralizado no topo (a partir de ~160px; zona reservada = primeiros ~150px, texto nunca entra nela), **foto P&B sangrando na faixa inferior** ocupando a largura toda.
- **Sem:** bordas/frames na foto, gradientes, sombras no texto, emojis, sans-serif, ornamentos, cores fora da paleta.

Esqueleto do slide:
```html
<div class="slide">
  <img class="slide-photo" src="../imagens/img-0X.png" alt="">
  <div class="text"> ... estrofes ... </div>
</div>
```
```css
.slide{ width:1080px; height:1350px; position:relative; overflow:hidden;
  background:#F5F0EB url("../../_banco-referencias/background para carrosséis.png") center/cover no-repeat;
  font-family:'Source Serif Pro',serif; }
.slide-photo{ position:absolute; bottom:0; left:0; width:100%; display:block; mix-blend-mode:multiply;
  /* fade no topo: funde a foto no linho sem emenda quando o fundo dela não é branco puro */
  -webkit-mask-image:linear-gradient(to bottom,transparent 0%,#000 20%);
  mask-image:linear-gradient(to bottom,transparent 0%,#000 20%); }
.text{ position:absolute; top:240px; left:0; right:0; padding:0 90px; text-align:center; z-index:2; }
/* calibragem do user: corpo 240, capa 280 (11/09/2026, carrossel 111: "descer levemente" a partir de 200/240 de 04/09) */
```

---

## 6. Estilo de imagem

- **Look:** fotografia **editorial P&B vintage**, desaturada, granulada, dramática. As imagens não precisam ser do mesmo universo: podem ser coisas diferentes, desde que cada uma faça sentido com o punch do seu slide (user em 13, 14 e 15/09 e 05/10: "não precisa... pode ser coisas aleatórias, mas que fazem sentido").
- **Formato:** **landscape 1536×1024**, entra no rodapé com `width:100%` (vira ~720px de altura). Sujeito na metade inferior, metade de cima clara pro texto. (Ver gotcha de orientação retrato em `referencias/motor-imagem.md`.)
- **Fade no topo** (CSS acima) é acabamento, nunca remendo. **A foto nasce pro slide (regra do user, 11/09/2026, carrossel 111):** o sujeito ocupa só os ~55% de baixo e os ~45% de cima são uma parede lisa, plana e iluminada **no tom do fundo padrão** (`_banco-referencias/background para carrosséis.png`, medido em 11/09: #F3F3F3, textura leve), que faz parte da própria foto. Foto de slide inteiro (fachada, rua, depósito com textura até o topo) que depende do degradê pra combinar com o linho reprova: "a proposta é o fundo da imagem fazer parte de verdade da imagem gerada, e não algo que tem que ser feito um degradê para combinar". Descrever a parede pelo padrão (off-white como papel de linho, textura fina), **nunca como "branca"**; e medir o padrão no arquivo antes de escrever, não citar de cabeça. Fato técnico: a foto entra em `multiply`, então essa parede tem que continuar muito clara (`topo.py` ≥ ~245) pra se fundir com o linho em vez de escurecê-lo. Com a parede na foto, o `check.py` acusa vão morto falso (parede não conta como assunto): julgar no olho.
- **Variedade:** curto (5-6) pode repetir o motivo. **Longo (8+): variar o motivo/sujeito** dentro do universo (motivos adjacentes — esporte, objeto/still-life, instrumento, paisagem), não só o ângulo do mesmo objeto. Ex (tema "permanecer no topo"): cume + corredor cruzando a linha + troféu empoeirado + corda bamba — todos dizem "topo/queda" sem ser todos montanha.
- **Composição no prompt:** cena única e coerente; sujeito baixo no quadro; nunca "close-up/cinematic/realistic" (joga pro fotorrealismo e quebra o look). Pra variar, pedir sujeito "on the LEFT/RIGHT side" mantendo o topo limpo.
- **Cláusula de composição pro slide (EN, obrigatória depois do estilo-base):**
  > `COMPOSITION FOR THE SLIDE (HARD REQUIREMENT): the subject occupies ONLY the LOWER 55 percent of the frame; the ENTIRE UPPER 45 percent of the frame is a plain, flat, evenly lit wall in a very pale OFF-WHITE tone (like unbleached linen paper, hex F3F3F3), with a faint fine plaster texture and absolutely nothing on it: no shelves, no appliances, no boxes, no doorway, no window, no sign, no ceiling line, no heads. The wall is part of the photograph and simply continues upward, staying very pale and uniform to the top edge.`
- **Estilo-base do prompt (EN):**
  > `black-and-white editorial vintage documentary photograph, desaturated, high contrast, grainy. WIDE HORIZONTAL LANDSCAPE orientation, 3:2 aspect ratio, much wider than tall. The subject sits low in the frame with a large pale/empty upper half for clean compositing. No text, no words, no logos, no emojis, no gradients, no added color, no stock photo look.`
- **Gerar OU banco, nunca misturar** (ver motor-imagem). O banco (`_banco-referencias/`) é referência de ESTILO descrita em texto, nunca `input_image`.
- **Pós-aprovação:** copiar as imagens aprovadas pro banco (`_banco-referencias/`, próximos números `N.png`) e atualizar o catálogo `README.md`.

---

## 7. Fechamento

O último slide não é só CTA. Primeiro **amarra a metodologia (MBV) à dor** do carrossel — uma frase de síntese que entrega o "como" (ex: "Permanecer é sempre método" · "carregar com clareza, método e comando") — e SÓ ENTÃO chama pra ação: **"Comenta [número]"** (o número da oferta/lead, em vermelho), com frase-ponte ligada ao conteúdo. A legenda pode fechar com a frase institucional "Seja Bem-Vindo ao Fim do Analfabetismo Empresarial."

> **Dois caminhos de CTA (regra do user, 14/09/2026; substitui os três caminhos de 09/09):** o fechamento serve a um dos dois destinos de conversão, escolhido pela narrativa (ver `SKILL.md` passo 2c). O que muda em cada um:
> - **Imersão MBV** (treinamento): slide de oferta ("Eu tenho um treinamento pra donos de PME, onde ensino: ...") ou fechamento sutil casado com o tema ("e rotina, eu ensino a montar", como no 122) + CTA com palavra única de estado desejado. Link: `https://rtc.tatsuoacademy.com/v2-maio-org`, UTM `AAAA-MM-DD-PALAVRA`. Era o destino único até 08/09.
> - **RAIO-X da empresa** (módulo de aula do Hélio + documento): slide de ponte que amarra o raio-x à DOR da peça, na linguagem da própria peça (no 127: "ninguém assume um volante sem conhecer o carro; antes de dirigir, você precisa de um raio-x da sua empresa") + CTA "Comenta RAIO-X" ou palavra única da peça (o 135 usou PATO). Link: `https://tatsuoacademy.com/raio-x-empresa-lucrativa/` com `utm_source=manychat&utm_medium=dm&utm_campaign=AAAA-MM-DD-PALAVRA&utm_content=<link limpo do post>` (o `utm_content` entra na hora de amarrar ao post; ver `manychat-baseline.md`). Palavra RAIO-X nas 7 grafias da global do user: `RAIO-X, raio-x, Raio-X, Raio-x, raio-X, RAIOX, raiox`. Botão `>> Quero a aula <<`. A global `RAIO - X` (qualquer publicação, mesma página, utm `raio-x-feed`) fica no ar; a específica tem prioridade. Primeiras específicas: 127 (18/09) e 135 (21/09).
> - **Diagnóstico gratuito: PAUSADO desde 14/09.** Não propor e não montar Manychat DIAGNÓSTICO até o user religar. O histórico (100, 103, 106, 111, 114 com UTM numérico 1..5 e link `rtc.tatsuoacademy.com/diagnostico`) fica só como referência. Raio-x nunca é diagnóstico: um é aula, o outro é call.
>
**Palavra-chave única por post (aprovado pelo user em 19/08/2026; vale pro caminho da imersão):** no lugar do número padrão (ex: 307), usar a **palavra-chave ÚNICA deste post** — derivada do batismo/termo central do tema (ex: BABA, DELARGAR), em CAIXA ALTA e sem acento, inédita no perfil (conferir `conteudo/analise/registro-posts.csv`). Propor a palavra junto com o texto e submeter à aprovação do user. O formato do CTA continua idêntico: "Comenta [PALAVRA]".

---

## 8. Exemplos prontos (referência)

Em `conteudo/carrosseis/`:
- `1_lider-que-mata-talento`
- `2_clareza-de-numero` — estrofes 2+2
- `3_peso-do-leme` — storytelling encadeado, 8 slides, metáfora náutica com variedade (âncora, píer, bússola, navio)
- `4_permanecer-no-topo` — 8 slides, variedade (cume, corredor, troféu, corda bamba)

Abrir os `carousel-text.md` e os `instagram/*.png` desses pra calibrar tom, ritmo e visual antes de escrever um novo.
