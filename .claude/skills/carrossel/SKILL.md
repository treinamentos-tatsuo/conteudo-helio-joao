---
name: carrossel
description: >
  Cria carrosséis para Instagram e TikTok da Tatsuo Academy. Funciona por MODELOS:
  cada tipo de carrossel é uma receita própria em modelos/. O fluxo é o mesmo
  (briefing → escolher modelo → texto → HTML → PNG via Playwright → imagens),
  o modelo define visual, arco de texto, nº de slides, estilo de imagem.
  Use quando o usuário mencionar "carrossel", "carousel", "slides instagram",
  "slides tiktok", "faz um carrossel", ou pedir pra transformar um tema em carrossel.
---

# /carrossel — Criação de Carrossel (Tatsuo Academy)

## Como esta skill é organizada

Duas camadas:

- **Fluxo (este arquivo)** — o passo a passo de produção, igual pra todo carrossel.
- **Modelo (`modelos/<nome>/modelo.md`)** — a receita de cada tipo de carrossel: propósito, arco de texto, nº de slides, regras visuais, estilo de imagem. Cada modelo é diferente; o fluxo lê o modelo escolhido e segue a receita dele. **Nunca sobrescrever um modelo** — eles são permanentes.

Compartilhado entre modelos, em `referencias/`:
- `voz-tatsuo.md` — voz do Hélio (tom constante em todos os modelos)
- `voz-helio-gabarito.md` — pares de texto reprovado → aprovado, conferidos contra o que foi ao ar (ler antes de escrever)
- `doutrina.md` — o que o Hélio ensina, o ICP, a oferta, os fatos do Hélio e o que nunca vai ao ar
- `motor-imagem.md` — como operar o gerador de imagem (gpt-image2-ratos) + gotchas
- `erros-frequentes.md` — log de correções (ler antes de gerar)

Motor de imagem: skill `gpt-image2-ratos` do projeto (`.claude/skills/gpt-image2-ratos/`), encanamento de OAuth/geração. Esta skill só o chama.

---

## Setup (checar rápido, não travar)

Este workspace já está configurado. Só conferir o que a tarefa exigir:
- **Playwright** (pra renderizar PNG): `npx playwright screenshot --help 2>/dev/null && echo OK || echo INSTALAR`. Se faltar: `npx playwright install chromium` (avisar que demora ~30s na 1ª vez).
- **Voz/contexto:** `_contexto/preferencias.md` (guia original de voz) e as transcrições do MBV em `_contexto/transcricoes-mbv/` — ler pra calibrar. A voz base está em `referencias/voz-tatsuo.md`; a doutrina em `referencias/doutrina.md`.
- **Marca:** `marca/design-guide.md` (cores/logo). Cada modelo pode ter identidade visual própria (o editorial, por ex., tem fonte e paleta próprias).

---

## Workflow

### Passo 1 — Briefing + escolher o modelo

1. Entender o input: tema, ângulo, link ou arquivo de referência, imagens (se houver). Se existir `conteudo/carrosseis/[tema]/briefing.md`, ler e usar de ponto de partida.
   - **A dor primeiro.** Se o pedido não diz qual dor do dono a peça aperta, perguntar isso antes de escrever (uma linha). Os carrosséis que passaram de primeira (183, 184) chegaram com a dor definida.
   - **Semente do banco MBV:** "abrir as seeds" = abrir os .md de `_contexto/banco-scouting-mbv/` e mostrar o cardápio; quem escolhe é o user. Ranking só se ele pedir. Topo ou meio de funil se decide aqui, pelo tema (ver `doutrina.md`).
   - **Repost:** só post com mais de 90 dias corridos de publicação (conferir a data e se já foi repostado). Texto, subtítulo e capa do original ficam literais; só entram oferta e CTA. O post antigo está em `conteudo/carrosseis/` ou em `~/Desktop/carrosseis claude/POSTADOS/`.
   - **Roteamento:** post da apostila → modelo infográfico (perfil da Tatsuo Academy, sem /etiqueta, sem Manychat). Fotos reais do Hélio → modelo fotos-reais. Frase única → `/frase` ou `/frase-foto`, não esta skill.
2. **Escolher o modelo.** Listar os modelos disponíveis (varrer `modelos/*/modelo.md` e mostrar nome + uma linha de cada). Perguntar qual usar:
   > "Qual modelo? 1. **Editorial-punch** — P&B editorial, storytelling encadeado, 8+ slides. [outros conforme existirem]"
   Se o usuário já disse o modelo no pedido, não perguntar.
3. **Ler o `modelo.md` escolhido** — ele governa texto, visual, nº de slides e imagem daqui pra frente.
4. Confirmar parâmetros que faltam (nº de slides dentro do que o modelo recomenda, se vai ter imagem, capa). Se o usuário já mandou tudo, não ficar perguntando.

### Passo 2 — Texto (Fase 1)

1. Ler `referencias/voz-tatsuo.md` (voz), `referencias/voz-helio-gabarito.md` (gabarito), `referencias/doutrina.md` + a seção **Arco de texto** do modelo escolhido.
2. Se o input for link: WebFetch direto; fallback Jina (`https://r.jina.ai/<url>`); X/Twitter → `api.fxtwitter.com`; Instagram → pedir o texto colado; YouTube → skill de transcrição se houver.

**2b. REGIME DE LEITURA — obrigatório quando o input é material pronto de outra pessoa** (transcrição de reel de terceiro, roteiro alheio, post de outro perfil). Duas leituras opostas e nenhum desempate automático — ver `erros-frequentes.md` (2026-07-30 × 2026-08-05 e 2026-08-27):

- **`tema`** → a fonte é insumo de conteúdo. Arco, voz e pedrada nascem do zero no arco do modelo.
- **`espinha`** → seguir os beats da fonte na mesma ordem, trabalhando só linguagem e diagramação.

Se o user não disse qual, **perguntar em uma linha antes de escrever** — é a única pergunta desta fase. Não herdar o default de "referência estruturada" (`espinha`): transcrição de reel *parece* estruturada e o modo `espinha` já foi reprovado nesse caso. Se a fonte for uma lista de N itens, confirmar junto: 1 peça ou N peças.

**2c. Duas declarações de saída (decidir sozinho, sem perguntar) — escrever no topo do `carousel-text.md` ANTES do CHECKPOINT 1:**

- **Interlocutor:** confirmar que nenhum slide fala com quem EXECUTA (prospectar, ligar, atender, produzir) em vez de com quem MANDA A EMPRESA EXECUTAR (cobrar, acompanhar número, puxar resultado através do time). O interlocutor é sempre o **dono de PME** — não é escolha, é checagem de contaminação da fonte. Ver `erros-frequentes.md` 2026-07-28 (carrossel 13).
- **Causa técnica:** qual é o número/mecanismo de gestão que o CTA e o treinamento vendem. Material de terceiro traz sintoma e postura, quase nunca traz a causa. Sem isso a peça fecha sem gancho de venda.
- **Caminho do CTA (regra do user, 14/09/2026; substitui os três caminhos de 09/09):** toda peça casa com UM de DOIS caminhos de conversão, escolhido pela NARRATIVA (o que a peça deixa o dono querendo no último slide), nunca fixo: (1) **imersão MBV** — inscrição no treinamento; peça que ensina o método e o dono sai querendo o "como"; (2) **RAIO-X da empresa** — módulo de aula do Hélio em que o dono faz o raio-x da própria empresa (com documento pra levar); peça que abre uma pergunta sobre a própria empresa dele ("você sabe quanto entra, quanto sai, onde vaza?"). **O diagnóstico gratuito está PAUSADO** (não propor, não montar Manychat DIAGNÓSTICO) e o raio-x nunca se confunde com ele: raio-x é aula, diagnóstico é call com especialista. Declarar o caminho e o porquê no `carousel-text.md` junto com a palavra-chave e mostrar no CHECKPOINT 1. O slide de fechamento, a legenda, a DM do Manychat e o link/UTM seguem o caminho (detalhes operacionais no modelo → "Fechamento").
3. Se citar algo que você não conhece (produto, evento, termo): **pesquisar antes**, nunca chutar nem "corrigir" o usuário.
4. Escrever os slides seguindo o **arco do modelo** + a voz. Gerar também a **legenda** (na voz do Hélio, amplia a reflexão, não resume os slides).
5. **Antes de mostrar, autorrevisão:** cada slide contra o gabarito (parece a coluna "reprovado"? reescreve); a dor é a do ICP e é uma só; frase falada inteira (artigo, sujeito, conectivo; corpo até ~180 caracteres); revisão de português (concordância, sentido, pronome sem ambiguidade, nada de "te" com "você" na mesma frase); a oferta promete gestão.
6. Mostrar no chat, nesta ordem: (1) contexto de cada slide (guia a imagem), (2) legenda, (3) texto que renderiza em cada slide. Salvar em `conteudo/carrosseis/[N]_[nome]/carousel-text.md`.

**CHECKPOINT 1 (obrigatório, nunca pular):** mostrar texto + legenda e esperar aprovação. Se pedir mudança num slide, mexer só naquele (pedido de redação muda a redação, não a abordagem) e **mostrar de novo a peça inteira**, todos os slides na ordem + a legenda, com uma linha dizendo o que mudou. Nunca descartar a versão anterior: salvar numerada (`_rodadas/v1.md`, `v2.md`...) e, quando o user voltar atrás, ela está lá. Texto que o user mandou entra literal; ajuste vai como sugestão ao lado.

### Passo 3 — Visual (Fase 2)

1. Montar os HTMLs seguindo a seção **Regras visuais** do modelo (1 HTML por slide) em `conteudo/carrosseis/[N]_[nome]/instagram/`.
2. Renderizar via Playwright (viewport do formato do modelo, padrão Instagram 1080×1350):
   ```bash
   npx playwright screenshot --viewport-size=1080,1350 --wait-for-timeout=1100 "slide-01.html" "slide-01.png"
   ```
   Renderizar o **slide 1 primeiro** e mostrar.

**CHECKPOINT 2:** slide 1 aprovado → renderizar os demais. Ajuste pontual → editar o HTML e re-renderizar só aquele slide.

### Passo 4 — Imagens (se o modelo usa)

Seguir `referencias/motor-imagem.md` + a seção **Estilo de imagem** do modelo. A imagem de cada slide diz o punch daquele slide, não o cenário (teste: "a foto sozinha diz o punch?"); imagem reaproveitada de outro post passa pelo mesmo teste. **O Hélio nunca é gerado por IA.**

Ordem: a capa e a primeira cena primeiro, pra aprovar o padrão. Com o padrão aprovado (ou o sinal do user, "capa aprovada", "me entregue pronto"), gerar o resto **em lote**, com autorrevisão slide a slide, e regerar sozinho o que falhar. Aprovação imagem a imagem só se o user pedir. Layout e alturas saem do modelo da skill, nunca do build.py do carrossel anterior.

### Passo 5 — TikTok (opcional)

Perguntar se quer a versão TikTok (1080×1920). Se sim: adaptar HTMLs (height 1920, mais padding, **deixar 230px livres embaixo** — UI do TikTok), renderizar com `--viewport-size=1080,1920`, salvar em `tiktok/`.

### Passo 6 — Entrega no Desktop (sempre, ao finalizar)

Quando os slides do carrossel estiverem **finalizados** (aprovados / prontos), copiar automaticamente pra área de trabalho do usuário:

1. Criar a subpasta `~/Desktop/carrosseis claude/<palavra>/` — `<palavra>` = **uma palavra** que representa o carrossel (o tema, ex: `equidade`, `barcos`, `beija-flor`). Criar a pasta-mãe `carrosseis claude` se não existir.
2. Copiar pra lá **todos os PNGs finais** dos slides (`instagram/slide-*.png`) e a **legenda** em `legenda.txt` (só o texto do post — extrair a seção `## Legenda (post)` do `carousel-text.md`).
3. Não precisa perguntar; faz parte do fechamento. Se o disco estiver cheio (ENOSPC), avisar o usuário pra liberar espaço e limpar os `imagens/_raw/` temporários.
4. Entregar só os PNGs individuais: nunca montar mosaico ou folha de contato com todos os slides juntos.
5. Abrir os PNGs no Preview e a pasta no Finder, sem perguntar.
6. Rodar `/etiqueta`. Se o post tem "Comenta PALAVRA", a automação se monta com `/manychat` na hora da publicação.
7. Commit conforme a regra de commit da máquina (CLAUDE.md).

---

## Pasta e nomenclatura

Cada carrossel vive em `conteudo/carrosseis/[N]_[nome-do-post]/`, **N = ordem de publicação** (olhar as pastas existentes e usar o próximo número). `[nome]` = slug kebab-case.

```
conteudo/carrosseis/[N]_[nome]/
  briefing.md            (opcional — ideia bruta de entrada)
  carousel-text.md       (texto aprovado + legenda)
  imagens/               (img-01.png ...)
  instagram/             (slide-01.html → slide-01.png ...)
  tiktok/                (se solicitado)
```

---

## Regras gerais

- Texto aprovado na Fase 1 não muda na Fase 2 (visual fiel ao texto).
- Sempre mostrar slide 1 antes de renderizar os demais. Ajuste no visual → editar HTML e re-renderizar só o slide alterado.
- Sem travessões/emojis no texto por padrão (a menos que `preferencias.md` diga o contrário).
- Ler `referencias/erros-frequentes.md` antes de gerar. Quando o usuário corrigir algo que é regra (mexe em leitura, impacto ou doutrina, e se repetiu ou ele disse "sempre/nunca/registra"), propor o registro e registrar com o sim dele. Correção de uma peça só e escolha artística não viram regra: "a gente enche de regra o negócio e começa a se perder".
- **Não inventar modelo.** Se o pedido não encaixa em nenhum modelo existente, dizer isso e oferecer criar um modelo novo (copiar `modelos/_GABARITO.md`).
- Adicionar modelo novo = criar `modelos/<nome>/modelo.md` a partir do gabarito. Nunca editar/sobrescrever um modelo pra "virar" outro.
