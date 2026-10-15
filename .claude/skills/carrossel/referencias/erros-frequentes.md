# Erros Frequentes — Carrossel Tatsuo Academy

> Registro de correções e ajustes feitos pelo Rodrigo. Ler antes de gerar qualquer carrossel. As regras citadas vivem no modelo escolhido (`modelos/<nome>/modelo.md`) ou na voz (`referencias/voz-tatsuo.md`).

---

## Erros de design

### 2026-06-17 — Texto alto demais na zona reservada
**O que foi feito:** texto posicionado em `top: 80px`, dentro da zona reservada para logo/marca.
**O que o Rodrigo pediu:** texto começa no mínimo em `top: 200px` — abaixo da zona reservada + margem de respiro.
**Regra:** zona reservada = primeiros ~150px do topo. Texto começa a partir de ~200px. Ver o modelo → "Regras visuais".

### 2026-06-24 — Slides de 4 frases agrupados em 3+1
**O que foi feito:** as 4 frases saíam em bloco corrido com o punch vermelho descolado no fim (3 juntas + 1 separada).
**O que o Rodrigo pediu (via designer):** slides de 4 frases = **2 estrofes 2+2**. Duas frases juntas, respiro, duas frases juntas.
**Regra:** slide de 4 linhas → 2 estrofes de 2 (`.stanza` com margin entre elas), nunca 3+1. Ver o modelo → "Estrutura por slide / estrofes".

### 2026-06-24 — Imagens presas a um único motivo (repetição)
**O que foi feito:** carrossel inteiro com o mesmo motivo literal (carrossel 1 só empresários; outro quase todo montanha).
**O que o Rodrigo pediu (via designer):** curto (5-6) tudo bem; longo (8+) fica repetitivo. Variar os motivos.
**Regra:** manter o MESMO universo metafórico, mas em 8+ slides **variar o motivo/sujeito** (motivos adjacentes — esporte, objeto/still-life, instrumento — que ainda servem o tema), não só o ângulo. Ver o modelo → "Estilo de imagem / variedade".

---

## Erros de design

### 2026-07-02 — Texto concentrado alto demais + espaçamento entre estrofes
**O que foi feito:** bloco de texto dos slides de conteúdo começando em `top:160px` (colado na zona reservada), e estrofes de frases muito próximas.
**O que o Rodrigo pediu:** descer a região de exibição do texto (ficou em `top:240px`) — um degrau pra baixo, **sem ir ao meio da imagem**. E dar um pouco mais de respiro entre estrofes (`.stanza + .stanza` de `34px` → `48px`), sem exagerar (longe demais também fica ruim).
**Regra:** slides de conteúdo do editorial-punch: texto em ~`240px`, respiro entre estrofes ~`48px`. Capa fica mais baixa (~`330px`) e não muda.

### 2026-07-02 — Subtítulo da capa em itálico pequeno (ilegível)
**O que foi feito:** subtítulo da capa em itálico e pequeno (`25px`) — o combo itálico + pequeno dificulta a leitura.
**O que o Rodrigo pediu:** manter pequeno mas **tirar o itálico** (subiu pra `28px`). Mais legível, mantendo a sutileza.
**Regra:** subtítulo da capa: pequeno, **sem itálico**.

### 2026-07-02 — Palavra órfã na 2ª linha / quebras desbalanceadas
**O que foi feito:** frases quebrando e sobrando **uma palavra sozinha** na segunda linha (ex: "...terceiriza as / decisões.", "...enxergar o jogo / é você."), cada frase com margem de início diferente — dá impressão de "texto jogado na imagem".
**O que o Rodrigo pediu:** quando uma frase ocupa duas linhas, deixar **as duas linhas com tamanhos próximos** (balanceadas), nunca uma linha cheia + uma palavra solta. Controlar a quebra manualmente (encurtar a frase pra caber numa linha, ou dividir em duas metades equilibradas).
**Regra:** nada de palavra órfã. Linhas da mesma frase equilibradas. ~46 caracteres cabem numa linha a `41px`/`900px`.

### 2026-07-02 — Agrupamento de frases quebrando a continuidade
**O que foi feito:** frases de ideias diferentes agrupadas na mesma estrofe, cortando o sentido (ex: fim de uma ideia + começo da próxima no mesmo bloco).
**O que o Rodrigo pediu:** agrupar na mesma estrofe as frases que **pertencem à mesma ideia**; separar por respiro as ideias distintas. Uma frase-âncora curta pode ficar sozinha na própria estrofe.
**Regra:** estrofe = unidade de sentido. O respiro marca a troca de ideia, não corta a ideia no meio.

### 2026-07-07 — Capa com foto de topo escuro (divisão suja) + rei pequeno
**O que foi feito:** capa do reino com o rei no salão de paredes escuras — a foto tinha conteúdo escuro subindo alto, criando uma faixa cinza no meio (fade visível), sem divisão limpa entre zona de texto e imagem.
**O que o Rodrigo pediu:** organizar melhor a divisão imagem × texto, como nas capas que funcionaram (#8): a foto tem que ter o **topo naturalmente claro/enevoado** pra dissolver no linho — terço de cima cremoso (texto), sujeito escuro e baixo no rodapé. Depois: "aproxima levemente o sujeito, tá pequeno" → resolver com **crop-zoom da própria imagem** (~1,2x, âncora no rodapé), sem regerar ("mesma imagem, só mais próximo").
**Regra:** toda imagem do editorial-punch precisa de **metade/topo superior claro e vazio** (luz, névoa, céu, pedra clara) que some no fundo; sujeito escuro e baixo. No prompt: "the ENTIRE UPPER HALF is bright/pale/hazy, fading to near-white at the top edge". Ajuste de escala do sujeito = crop-zoom da imagem aprovada, não regerar.

### 2026-07-07 — Figura do sujeito (o rei) repetida demais
**O que foi feito:** carrossel do reino com a figura do rei de frente em ~11 dos 15 slides — virou repetitivo, mesmo variando ângulo/cena.
**O que o Rodrigo pediu:** "tem muito rei, repetido; usar melhor o tema". Explorar a riqueza simbólica do universo (coroa, cetro, selo, decreto, mapa, espada, mãos, o reino sendo construído) e **guardar a figura humana só pros slides-pilar** (capa, o peso da decisão, liderar o povo, CTA).
**Regra:** reforça a regra de variedade — em 8+ slides, o **sujeito humano principal deve aparecer no máximo ~5-6 vezes**; o resto conta a história por **símbolos/objetos/mãos/ambiente** do mesmo universo. Cada símbolo carrega uma ideia (selo=decidir, mapa=direção, espada=coragem, mãos dadas=ouvir a ponta, trono vazio=abrir mão). Menos rosto, mais símbolo.

### 2026-07-08 — Imagem pequena demais (muito fundo branco) + hierarquia da capa
**O que foi feito:** fotos entravam no rodapé com `width:100%` (~45% de altura), e como o topo delas é claro/enevoado (pro fade), sobrava muito linho vazio — "a maior parte do slide é fundo branco". Na capa, o título quebrado em 2 linhas + subtítulo longo tirava o impacto da frase principal.
**O que o Rodrigo pediu:** aumentar as imagens pra ocuparem ~**2/3 do slide** ("expandir a parte de baixo", sem alterar o conteúdo delas). E na capa, a frase de impacto em **linha única e maior** (nunca menor que o subtítulo).
**Regra:** (1) escalar a foto ancorada no rodapé pra ocupar ~2/3 — `.slide-photo{transform-origin:bottom center;transform:scale(1.5);}` (a native 1672px aguenta sem perder nitidez). (2) Capa: título de impacto em uma linha só, fonte maior que o subtítulo; vermelho como `<span class="red">` dentro da linha. (3) Quando juntar frase numa linha que estoura 900px, baixar fonte/padding só naquele slide. Ajuste de escala do sujeito ≠ regerar; é CSS.

### 2026-07-02 — CTA sem hierarquia
**O que foi feito:** CTA numa fonte só ("Comenta 307 que eu te mostro por onde começar." tudo do mesmo tamanho, quebrando com "começar" órfã).
**O que o Rodrigo pediu:** **"Comenta [número]," em fonte MAIOR** que o resto (numa linha própria, com vírgula), e a continuação ("que eu te mostro por onde começar.") em fonte menor embaixo. A fonte maior chama a ação E resolve a disposição das linhas.
**Regra:** CTA do editorial-punch = `Comenta <b>[número]</b>,` grande (`~60px`) em linha própria + frase-ponte menor (`~36px`) embaixo.

### 2026-07-16 — Imagem baixa/estreita (espaço negativo) → disposição de imagem em tela alta
**O que foi feito:** foto landscape 3:2 (1536×1024) entrando no rodapé cobria ~60% do slide; sobrava linho vazio em cima e um vão morto entre o texto e o sujeito da foto.
**O que o user pediu:** imagem ocupando mais o slide (~75-80%), menos espaço negativo — e definiu isso como **padrão de disposição pra todas as imagens daqui pra frente**. A mecânica pedida foi "adicionar mais um terço à imagem" (esticar pra baixo). Outpainting da mesma imagem sai sujo (colagem, gotcha do gpt-image-2), então o equivalente limpo é **regerar em tela mais alta**.
**Regra (disposição-padrão de imagem no editorial-punch):**
1. **Gerar quadrada (1:1) em vez de landscape 3:2** — a tela mais alta já nasce cobrindo mais slide, com o terço extra como **primeiro plano sangrando no rodapé** (borda da mesa, objetos, chão). Prompt mantém "the ENTIRE UPPER HALF is bright, pale, empty and hazy, fading to near-white at the top edge" (topo pálido pro texto e pro fade).
2. **No slide:** `.slide-photo{ position:absolute; bottom:0; width:100%; mix-blend-mode:multiply; mask top ~15% }` — **sem `scale`** (a quadrada já preenche ~80% a `width:100%`).
3. **Descer o texto** pra encostar na imagem e matar o vão (capa foi de `top:200px` → `top:330px`). O texto vive na faixa pálida superior da foto.
Ver o modelo → "Estilo de imagem".

### 2026-07-16 — Sistema de tipografia + elementos à mão (design mais profissional)
**O que foi feito:** slides só com Source Serif Pro (setup preto + punch vermelho), monótono.
**O que o user pediu:** subir o nível do design com duas fontes + elementos gráficos à mão, usados com CRITÉRIO (não empilhar).
**Regras:**
1. **Duas fontes.** Base = **Source Serif Pro** (serif). Destaque = **Anton, sempre CAIXA ALTA** (condensada, pesada). Anton entra na frase que é um **grito**/tapa inesperado. Dimensionar a linha Anton pra **respeitar as margens da linha de referência** (não estourar nem sobrar vão) — medir a largura das duas e ajustar `font-size` (medi via Playwright `Range.getBoundingClientRect`).
2. **Elementos à mão** (carmim `#A91C20`, PNG transparente): grifo/sublinhado, círculo/elipse, seta, bullets, ticks, brilho. Biblioteca oficial em `_banco-referencias/elementos/` (ver `README.md` lá). **Usar os PNGs reais sobrepostos**, nunca redesenhar em SVG (SVG fica liso demais, sem grão de lápis).
3. **Critério de ênfase (regra de ouro):** máx ~2 recursos por composição, cada um com função, **sem repetir o mesmo recurso nem a mesma cor** no slide. Anton = grito; grifo = ênfase calma (usar quando já tem Anton/vermelho); círculo = encapsular; seta = direcionar. Vermelho no texto virou só mais um recurso (parcimônia), não o punch-padrão.
Ex. aplicado (slide 2 do carrossel 1): linha "GESTÃO É CHATA PRA CACETE" em Anton vermelho (grito) + "Abre pra ganhar dinheiro" em serif preto com `sublinhado-rabisco.png` (ênfase calma, sem repetir Anton nem vermelho).

### 2026-07-17 — Layout, tamanho padrão, splits e figura solta (refinamento fino)
**O que o user pediu (batelada de ajustes no carrossel 1):**
1. **Tamanho padrão da Source Serif Pro = 44px** no canvas 1080×1350 (o "tamanho 30" do Canva). Corpo de texto SEMPRE nesse tamanho; só desvia (a) pra combinar/preencher com Anton, ou (b) pra reduzir e respeitar margem. Nada de misturar 58/50/52 à toa — falta de padronização é erro.
2. **Rodapé não cola na borda.** Texto de baixo em `bottom:~200-210px` (não 120). Perto da borda inferior dificulta leitura.
3. **Respeitar margem entre blocos.** O bloco de baixo (secundário) não pode ultrapassar a largura do bloco de cima (referência). Se ultrapassar, reduzir o `font-size` do bloco de baixo (medir com Playwright).
4. **Anton casa a margem da linha de referência** (a linha logo acima). Medir as duas larguras e ajustar `font-size` da Anton até bater (script de autofit). Quando a Anton é bem mais curta que a referência, ela infla (virou 94-107px em alguns) — e isso, casado na margem, funciona como grito, não fica desproporcional.
5. **Três layouts** (escolher por slide): *sanduíche* (texto topo + figura no miolo + texto rodapé); *dois blocos no topo* (as duas estrofes juntas em cima, figura ocupando a metade de baixo — o editorial clássico); *herói* (uma linha só, centrada).
6. **Figura solta / minimalista.** Nem toda imagem sangra no rodapé. Momentos pedem uma **figura isolada recortada** (fundo transparente) flutuando no miolo ou embaixo. O banco (`_banco-referencias/`) tem várias figuras `pessoa`/`objeto-metafora` já recortadas em PNG transparente — usar direto (recorte pronto), centralizar com `mix-blend-mode:multiply`. Recortar na caixa via alfa: `Image.open(x).convert('RGBA').getbbox()`. Quando a figura tem elemento entrando pela borda do canvas (ex. braço), usar o **canvas cheio 1:1** pra preservar a composição do artista, não centralizar.
7. **Split de frase prioriza o começo.** Quebrar uma frase em 2 slides (com "..." e continuação em minúscula) segura o swipe. Se o carrossel estourar o teto de 16, **manter os splits do gancho** (slides iniciais) e cortar beats do miolo/fim — o gancho vale mais.
**Regra:** ver o `carousel-text.md` do carrossel 1 (`1_ninguem-quer-gestao`) como referência viva desse sistema de layout + ênfase.

### 2026-07-28 — Diagramação "perdeu a mão": órfãs, parágrafos irregulares, foto invadindo o texto (carrossel 13)
**O que foi feito:** ao montar 13 slides rápido, a diagramação saiu irregular — parágrafos de 1, 2 e 3 linhas misturados, **palavras órfãs** (linha cheia + 1-2 palavras soltas: "é chato.", "puxar a venda.", "sabe.", "MAIS."), quebras desbalanceadas, e a **foto sangrando subindo até a faixa de texto** (fade curto de 16%), deixando o conteúdo médio/escuro atrás das linhas.
**O que o user pediu:** "perdeu a mão na disposição da parte textual... muitos slides com palavras órfãs, slides com a imagem invadindo o espaço do texto... deixe visualmente confortável para ler. Duas linhas de texto cada parágrafo, se tiver mais de um parágrafo não tem problema, mas dê o espaçamento."
**O que foi corrigido (sistema de diagramação confortável):**
1. **Cada parágrafo = 2 linhas balanceadas.** Nunca 1 linha solta nem 3 linhas com sobra. As duas linhas com larguras próximas (nada de linha cheia + palavra órfã). Pode ter 1, 2 ou 3 parágrafos por slide — cada um em bloco de 2 linhas.
2. **Espaçamento generoso entre parágrafos:** `.stanza + .stanza { margin-top: 52px }` (não 34-46).
3. **Linhas curtas por design:** manter cada linha ≤ ~36 caracteres (a 43px/940px de largura útil) pra a quebra ser controlada, não automática. Reescrever a frase pra fechar em 2 linhas limpas em vez de deixar o navegador quebrar.
4. **Foto não invade o texto:** aumentar o fade do topo pra **24-30%** (era 16%) — a imagem entra só na metade de baixo e o texto vive sobre o linho, com folga antes do sujeito. Slides mais escuros (feixe de luz) pedem 30%.
5. **Slide de CTA:** foto **subida** (`bottom:300px`) com **fade duplo** (topo + rodapé), CTA no rodapé sobre linho limpo — nunca o CTA sobre o corpo escuro do sujeito.
**Regra:** o padrão de bloco de texto do editorial-punch é **parágrafo de 2 linhas balanceadas + respiro de ~52px + foto na metade de baixo (fade 24-30%)**. Antes de renderizar, checar: nenhuma palavra órfã, nenhum parágrafo de 1 ou 3 linhas, e o sujeito da foto começa ABAIXO da última linha de texto. Reescrever a copy pra caber em 2 linhas limpas é preferível a encolher fonte ou deixar quebrar sozinho.

### 2026-07-30 — Quando o user manda uma referência pronta, copiar a IDEIA, não expandir nem traduzir literal (carrossel 17)
**O que foi feito:** com um input de 6 slides do marketing ("ter pena de funcionário"), montei um editorial-punch de 10 slides com beats inventados (empatia x pena / "medo de decidir", "a demissão azeda") e o CTA padrão "Comenta 307".
**O que o user pediu (em 3 rodadas):** (1) "o carrossel de referência já está muito bom, só ajuste de linguagem e estruturação, mas passar exatamente a mesma ideia" — enxugar pros beats da referência (6) + CTA = 7 slides; (2) manter a **capa literal** que ele mandou ("O maior erro de um empresário é ter pena de funcionário"), que era o gancho mais atrativo, em vez do espelho que eu tinha proposto; (3) "copiar a ideia e abordagem, não tudo... use o mesmo sentido com a nossa cara" — reescrever cada beat na voz do Hélio sem calcar a redação (ex: slide 3 abre "E não é só você que paga essa conta"; slide 4 vira "quando você demite, já foi tarde, o time já tirou a conclusão" em vez do beat de gratidão da referência).
**Regra:** quando o user traz uma **referência estruturada** (não um tema solto), o default NÃO é o arco padrão do editorial-punch nem expandir pro mínimo de ~8. É **seguir a espinha da referência** (mesmos beats, mesma ordem, mesmo nº de slides) e trabalhar só a **linguagem** (voz do Hélio) e a **diagramação** (2 linhas balanceadas, Anton nos gritos). Copiar a ideia e a abordagem ≠ copiar a redação ≠ inventar beats novos. Se for melhorar um beat, manter o MESMO sentido com a nossa cara, não trocar o argumento. Confirmar a capa: se o user já mandou uma frase-gancho forte, ela é a capa (não "corrigir" pra um espelho).

### 2026-08-05 — "Roteiro é só o tema": quando o user manda um roteiro pra CONTEXTUALIZAR, não virar versão-carrossel do roteiro (carrossel 22)
**O que foi feito:** o user mandou um roteiro do Hélio sobre a torcida do Japão que limpa o estádio (cultura), dizendo "pega SÓ o direcionamento de conteúdo e o tema, nada mais". Eu montei um editorial-punch seguindo os beats do roteiro na ordem dele (cena → "isso é cultura" → criança limpa a escola → teste → doutrina → caminho → CTA).
**O que o user pediu:** "não ficou ruim, mas perdeu nosso punch. Te mandei o roteiro pra você se contextualizar sobre o tema. O que você entregou foi uma versão carrossel do roteiro." Ou seja: o roteiro era insumo de TEMA, não espinha estrutural. É o **oposto** do caso 2026-07-30 (lá o user trouxe uma referência estruturada pra seguir a espinha; aqui ele avisou explicitamente que é só o tema).
**O que corrigiu:** reescrever no diagnóstico editorial-punch que **acusa o dono**, não que explica cultura. (1) **capa-espelho** que reposiciona a queixa dele ("A sua empresa não está sem cultura, está do jeito que você treinou"), como o tubarão abriu no espelho e não na história; (2) a história do Japão virou **prova comprimida**, não contada slide a slide; (3) entraram as **pedradas** que o roteiro-explicador não tinha (o time copia o que você deixa acontecer; "Você não tolerou. Você ensinou." em tríade); (4) cortadas as muletas de explicador ("de onde vem isso? olha só", "quer saber de verdade?") → declarativas.
**Regra:** ler com atenção o QUE o user diz sobre o material que manda. "Pega só o tema / me contextualiza" = insumo de conteúdo, e o arco/voz/punch são NOSSOS (construir do zero no diagnóstico editorial-punch: capa-espelho → prova → pedrada → teste → doutrina → caminho → CTA). "Passa a mesma ideia / ajuste de linguagem" (2026-07-30) = seguir a espinha da referência. Os dois pedidos são opostos; não confundir. Sinal de que virou "versão-carrossel do roteiro": os slides estão na ordem do roteiro, sem capa-espelho e sem pedrada que responsabiliza o dono.

### 2026-08-05 — Jersey de seleção gera brasão real (logo) na imagem (carrossel 22)
**O que foi feito:** prompt de "torcedores em camisa de seleção" (slide 2, cena da torcida do Japão) devolveu camisas brancas com o **brasão dos três leões da Inglaterra** — brasão real (logo) E errado pra uma história do Japão.
**O que corrigiu:** regerar pedindo "plain blank shirts with absolutely no crest, no emblem, no logo, no badge and no number of any kind" + "East Asian supporters". Voltou limpo.
**Regra:** ao gerar torcida/uniforme/esporte, nunca pedir "camisa de seleção/time" (o gpt-image-2 inventa brasão reconhecível = logo real). Pedir explicitamente camisa **lisa, sem brasão, sem emblema, sem número**. Se a cena é de um país específico, dar a etnia ("East Asian") em vez do brasão pra ancorar sem logo. Vale a regra geral: nada de logo/marca/número identificável na imagem (já está no estilo-base, mas uniforme esportivo fura — reforçar).

### 2026-07-30 — CTA sutil por DM (comenta [palavra] → direct), alternativo ao "Comenta 307" (carrossel 17)
**O que o user pediu:** em vez do "Comenta 307", um CTA sutil descrevendo a oferta: "Eu tenho um treinamento voltado a gestão pra pequena e média empresa, inclusive gestão de pessoas, cultura e liderança. Se quer saber mais, comente CULTURA que eu te chamo no direct." E manter o slide de engajamento da referência ("Você concorda? Comenta sua opinião") ANTES do CTA — dois pedidos separados (opinião no penúltimo, oferta no último).
**Regra:** o "Comenta 307" (2026-07-28) é o default, não a única forma. Quando o user pede, usar o CTA sutil: 1 frase que descreve o treinamento + ação "comenta [PALAVRA-CHAVE] que te chamo no direct" (a palavra em vermelho, ex. CULTURA). A palavra-chave casa com o tema/pilar. Pode conviver com um slide de engajamento (pergunta + "comenta sua opinião") logo antes. Alinhar a legenda: o fecho troca o "Comenta 307..." pelo mesmo convite do treinamento/DM. Vale por carrossel (o user sinaliza qual quer); não apaga o 307 como default global.

### 2026-08-03 — CTA fraco quando não nomeia o treinamento; CTA pode ser 2 slides (carrossel 19)
**O que foi feito:** carrossel 19 (texto campeão "cansar é privilégio de quem está no jogo") fechado com 1 slide de CTA que só vendia o desejo abstrato ("Comenta 307, que eu te mostro como fazer o seu esforço construir uma empresa que cresce").
**O que o user pediu:** "esse CTA ficou fraco e não fala sobre o treinamento. Faça 2 slides se necessário."
**O que foi corrigido:** CTA virou **2 slides** — (9) **pedrada** que justifica a oferta ("cansar não basta, cansaço não é resultado; tem dono que se mata de trabalhar e a empresa não sai do lugar"); (10) **método + treinamento + CTA** que revela o que falta ("O que falta não é esforço. É método."), **nomeia explicitamente o produto** ("é isso que eu ensino no meu treinamento de gestão pra pequena e média empresa") e chama pra ação vendendo o desejo grande ("Comenta 307, que eu te mostro como participar e transformar o seu esforço em lucro, crescimento e um time que joga com você").
**Regra:** vender o desejo (2026-07-27) **não basta** — o CTA também precisa **nomear o treinamento** como coisa concreta a participar ("eu tenho/ensino um treinamento de gestão pra pequena e média empresa"), senão soa a frase de efeito, não a oferta. E o fechamento **pode ocupar 2 slides** quando 1 fica apertado: slide-pedrada (por que o conteúdo prova que ele precisa do método) → slide-oferta (método + treinamento nomeado + Comenta 307 + desejo). Aqui os 3 pilares do MBV (lucro, crescimento, time/cultura) **cabem** porque descrevem a OFERTA, não os slides emocionais — não contradiz 2026-07-23 (que proíbe forçar MBV nos slides de dor pessoal).

---

## Erros de texto

### 2026-08-06 — "Juro" no singular soa estranho (carrossel 25)
**O que foi feito:** slide 5 com "Do governo, do juro, da taxa." (e "o juro do banco" na legenda).
**O que o user pediu:** trocar por "dos juros". O plural "juros" é a forma natural de falar; o singular "juro" é técnico e destoa da voz.
**Regra:** usar sempre **"os juros"** (plural) em slide e legenda, nunca "o juro".

### 2026-06-17 — Concordância, acento e gênero
**O que foi feito:** "você vai se cercar de medíocre" + "vai achar que ele é ótimo".
**O que o Rodrigo pediu:** "pessoas medíocres" + "vai achar que elas são ótimas" (concordância de gênero e número com o referente).
**Regra:** forma completa com concordância de gênero e número. Nunca cortar artigo/substantivo/acento pra economizar espaço. Verificar o referente antes de usar pronomes. Ver `referencias/voz-tatsuo.md`.

### 2026-09-24 — A máquina de aforismo: o slide virou epigrama e o "eu" só aparecia na oferta (carrossel 142)
**O que foi feito:** a v1 do 142 (inspiração de terceiro sobre "tá foda empreender no Brasil") saiu tecnicamente correta e morta. Quatro dos doze slides eram o MESMO molde de oposição: "aguentar não é resultado, é falta de resultado", "sobreviver não é meta, é sintoma", "não é que você seja fraco, é o contrário", "continuar aberto não é resultado, é ponto de partida". O vocabulário era de análise (sintoma, resultado, ponto de partida, placar) e o primeiro "eu" da peça aparecia no slide 11, pra vender a aula.
**O que o user disse:** *"a linguagem que você tem apresentado está se distanciando do que sempre deu certo para nós: o hélio falando, pessoa falando para pessoa... começa com uma característica humana muito forte que é experiência pessoal. Não é só uma afirmação, é uma afirmação com um tom de experiência humana."* E, sobre a fonte de terceiro: *"até o parágrafo 4 ele parece muito mais hélio do que o que você me entregou agora, e olha que ele é de outra pessoa!"*
**Diagnóstico:** o punch curto do editorial-punch degenera em epigrama quando o texto é escrito DE FORA. Simetria perfeita repetida é assinatura de máquina (as `preferencias.md` já banem a simetria e o "não só X, mas Y"); repetida quatro vezes na mesma peça, vira o formato inteiro. E uma peça em que o único "eu" está na oferta é um diagnóstico apontando o dedo, não um empresário falando com outro.
**Regra:**
1. **Punch curto é gente falando curto, não epigrama.** O molde de oposição ("não é X, é Y") entra no máximo UMA vez por peça, e só como remate.
2. **O "eu" vive nos slides, não só na legenda e na oferta.** "Vou dizer o que tá entalado", "eu sei o que é", "eu respeito isso", espalhados pela peça. Quem se expõe primeiro ganha o direito de falar da dor do outro.
3. **Afirmação com lastro de vivência, não axioma.** O que sustenta a frase é ter vivido aquilo, não a construção retórica.
4. **Ganhar o direito de concluir.** A dor se sustenta por vários slides antes de qualquer virada; conclusão no slide 2 é observação de quem está de fora.

### 2026-09-24 — Copiar o que é bom da fonte: lista de COISA, nunca de ação; dor dita, nunca encenada (carrossel 142)
**O que foi feito:** com a fonte de terceiro na mão, eu reescrevi as linhas que o user tinha elogiado ("A folha vence dia 5. O aluguel dia 10." no lugar de "A folha, o aluguel, o imposto: tudo vence") e **importei justamente as duas que ele reprova**: a enumeração de verbos ("fez, divulgou, chamou, treinou") e a cena do dono chorando no banheiro e voltando com um sorriso.
**O que o user disse:** *"Você copiou as únicas coisas ruins da referência"* e, depois, *"caralho claude, COPIA O QUE É BOM, COPIE. VOCÊ TÁ DEIXANDO RUIM TODA HORA."*
**A distinção fina (as duas coisas convivem no mesmo texto-fonte):**
- **Presta:** fato dito seco, sem construção ("tá foda", "tudo vence"); **lista de COISA** que existe na mesa dele (escândalos, crise, bancos, juros, medo / a folha, o aluguel, o imposto); verbo de boca ("não quer saber"); sintaxe falada ("Só que...", "A pior parte?" respondido por ele mesmo).
- **Não presta:** **lista de AÇÃO pra emocionar** ("fez, divulgou, chamou, treinou") — é cadência de copy e não diz nada concreto; e **cena montada pra comover** (chorar no banheiro, lavar o rosto, voltar sorrindo) — é melodrama, e já era proibido pela entrada de 09/09 (descrever a cena em vez de dizer a dor). O fecho de homenagem ("parabéns pra você que cai e volta") também sai: é motivacional e contraria a posição da casa.
**Regra:** quando o user manda material de terceiro e aponta trechos como bons, **copiar esses trechos LITERAIS** — reescrever com outras palavras é piorar. No 142 os slides 1 a 4 são o texto dele palavra por palavra. E a régua que separa o bom do ruim em qualquer peça: **lista de coisa, nunca de ação; dor dita, nunca encenada.**

---

## Erros de estrutura / fluxo

### 2026-06-24 — Slides soltos, sem narrativa entre eles
**O que foi feito:** cada slide parecia um "post de frase" independente — bom punch isolado, mas sem fio condutor; carrossel de 5-6 slides.
**O que o Rodrigo pediu (via designer):** storytelling desenhado, com conexão entre o conteúdo de um slide e o outro; e no **mínimo ~8 slides** pra construir impacto sólido e correlacionar a metodologia (MBV) com a dor, fechando de verdade.
**Regra:** (1) **Handoff encadeado** — a última linha de cada slide puxa o próximo; o seguinte responde/retoma (ex: termina "...fez algo errado." → abre "Não fez."). (2) **Mínimo ~8 slides** (varia por tema). (3) **Fechamento** que amarra a metodologia à dor, não só CTA. Ver o modelo → "Arco de texto".

### 2026-06-24 — Imagem gerada em retrato (gpt-image-2)
**O que foi feito:** prompt sem orientação explícita → o gpt-image-2 devolveu retrato (1024x1536) mesmo com `size` landscape; retrato estoura por cima do texto no layout de rodapé.
**O que foi corrigido:** forçar landscape no PROMPT ("WIDE HORIZONTAL LANDSCAPE, 3:2, much wider than tall") e validar a dimensão depois.
**Regra:** ver `referencias/motor-imagem.md` → "Gotchas". Quando o fundo da imagem não for branco puro (céu, parede), aplicar **fade no topo** (`mask-image:linear-gradient(to bottom,transparent 0%,#000 20%)`) pra fundir sem emenda. Ver o modelo → "Estilo de imagem".

### 2026-07-20 — Capa-título sem gancho (capa e hook tratados como slides separados)
**O que foi feito:** slide 1 virou uma capa-título genérica ("Empresa grande não é ser rico") e o gancho de verdade ("Conheço empresa que fatura milhão e vive apertado") foi jogado pro slide 2 — como se capa e hook fossem beats diferentes.
**O que o user pediu:** "O gancho é no primeiro slide, sempre." O primeiro slide JÁ é o soco. A capa não é um título de abertura — ela é o gancho. Abrir com o beat mais forte (no carrossel 2, o reposicionamento do propósito da empresa virou o slide 1).
**Regra:** slide 1 do editorial-punch = gancho. Formato de capa (impacto grande + punch/subtítulo), mas o conteúdo tem que ser o soco que segura o dono, nunca um rótulo do tema. Se o beat mais forte está no meio do rascunho, ele provavelmente é a capa.

### 2026-07-21 — Vermelho em Source Serif Pro sem negrito
**O que foi feito:** ênfase em vermelho aplicada só com cor (`.red{ color:#A91C20 }`), mantendo o peso do corpo (400).
**O que o user pediu:** "Sempre que for pintar o texto Source Serif Pro em vermelho, coloque essa parte em negrito." O vermelho serif precisa de peso pra bater.
**Regra (permanente):** `.red{ color:#A91C20; font-weight:700 }` — todo texto serif em vermelho vai em negrito. Não vale pra Anton (já é pesado) nem pro grifo (elemento à mão). Ver o modelo → "Estrutura por slide / estrofes".

### 2026-07-20 — Texto óbvio / briefing despejado sem fluidez
**O que foi feito:** o input do user (comparação "1 milhão × 10 milhões, mesmos 30 mil no bolso") saiu como sequência mecânica de slides — "pensa em duas empresas → uma fatura X → a outra Y → qual é melhor? → a de 1 milhão, disparado → porque...". Ficou óbvio, sem virada.
**O que o user pediu:** "muito óbvio e falta fluidez, parece que jogou as informações sem explorar o contexto." Não repetir a informação crua — costurar como raciocínio: entrar com a comparação como PROVA de uma tese, com virada de leitura (ex: "não é dez vezes melhor, é dez vezes mais pesada pelo mesmo dinheiro"; "faturamento passa pela mão, riqueza fica"). O dado é insumo; o slide entrega o insight.
**Regra:** o briefing é matéria-prima, não roteiro. Cada slide precisa de uma camada de leitura que o dado sozinho não dá (reframe, anáfora, claim→prova). Se o slide só reafirma o que o user disse com outras palavras, reescrever. Ver `referencias/voz-tatsuo.md` → teste da substituição.

### 2026-07-23 — Ideia certa com execução fraca ("largar no topo")
**O que foi feito:** a tese "abandonar no topo aquilo que você faz melhor" (que veio da transcrição-fonte) virou slide literal: "Você vai ter que largar no topo / o que você faz melhor que todo mundo."
**O que o user pediu:** "a palavra topo não tem tanto impacto. Eu entendi a ideia, mas achei a execução pouco impactante." Trocou pelo mecanismo concreto: **"você fez resultado sozinho, mas só cresce quem faz resultado através dos outros"** — que ainda amarra em delegar.
**Regra:** aprovar a tese não é aprovar a frase. Quando um conceito é abstrato ou metafórico demais ("no topo", "dar um passo atrás"), procurar o **mecanismo concreto** que o empresário reconhece na rotina. Metáfora explica; mecanismo cutuca.

### 2026-07-23 — Metodologia forçada em tema pessoal
**O que foi feito:** slide de ponte fechava com MBV + os três pilares (Lucratividade, Crescimento, Cultura), por reflexo do arco padrão do editorial-punch.
**O que o user pediu:** "não precisamos falar de lucratividade e crescimento nesse tema... é um tema mais pessoal do empresário, uma dor que ele vive sozinho. Não há necessidade de falar do MBV." O fecho virou método + fundamento + **coragem**.
**Regra:** a "ponte com a metodologia" do arco é opcional, não obrigatória. Em tema de dor pessoal/identidade do dono, citar os pilares esfria. Fechar na virada humana e deixar o CTA carregar a oferta. **Quando o MBV sai dos slides, tirar também da legenda e das hashtags** — senão o texto fica descolado da peça.

### 2026-07-23 — Figura recortada usada sem crop na caixa
**O que foi feito:** as figuras soltas (recorte em fundo branco) entraram no HTML no canvas cheio da geração (1024×1536). Como o sujeito não ocupa o quadro inteiro, sobrava branco em volta: a figura saía pequena e descentralizada mesmo com `left:50%; translateX(-50%)`.
**O que foi corrigido:** passo de crop na caixa real do conteúdo antes de usar. Como o fundo é branco (não transparente), binarizar por limiar (~243) e pegar o `getbbox()` da máscara, com ~12px de folga.
**Regra:** toda figura solta passa por crop na caixa antes de entrar no slide. Só depois definir `top`/`height` — senão o dimensionamento é chute. Vale pro recorte gerado por IA e pro recorte vindo do banco.

### 2026-07-23 — Vão morto entre o texto e o sujeito da capa
**O que foi feito:** capa com o bloco de texto em `top:262px` sobre uma foto de sujeito muito baixo no quadro (trator no rodapé). Ficou um vazio grande de linho entre a última linha e a imagem.
**O que foi corrigido:** descer o bloco pra `top:352px`.
**Regra:** reforça a regra de 16-07 — a posição do texto da capa não é fixa, ela **acompanha a altura do sujeito na foto**. Renderizar, olhar o vão e descer o texto até encostar na imagem. Quanto mais baixo o sujeito, mais baixo o texto.

### 2026-07-23 — Subir imagem por zoom (scale) x regerar a composição
**O que foi feito:** pra tirar o vão morto entre texto e sujeito em 3 slides de foto sangrada, apliquei `transform:scale(1.14)` ancorado no rodapé (sobe o sujeito ampliando).
**O que o user pediu:** "mantenha o tamanho original das que ampliou e gere a parte que falta de baixo, pois vc subiu elas." Ou seja: não gosta do zoom (amplia e corta as laterais, perde qualidade). Prefere **tamanho original (scale 1.0) e o sujeito subindo pela COMPOSIÇÃO** — mais primeiro plano preenchendo o rodapé, sujeito no miolo-baixo, metade de cima vazia.
**O que foi corrigido:** reverter o scale pra 1.0 e **regerar** com o prompt reforçando "the subject sits in the lower-middle of the frame with foreground filling the bottom third and bleeding off the bottom edge, the ENTIRE upper half is bright, pale and empty". **Gotcha confirmado:** pedir size portrait (1024x1536) NÃO funciona — o gpt-image-2 devolveu quadrada (1254×1254) mesmo assim. Quem levanta o sujeito é a instrução de composição no prompt, não o parâmetro de aspect.
**Regra:** pra subir o sujeito, **regerar a composição, nunca dar zoom** por CSS. `scale` no `.slide-photo` só quando o user pedir explicitamente. O sujeito sobe no prompt (mais primeiro plano embaixo), não na escala. Ver `referencias/motor-imagem.md` → gotcha de orientação.

### 2026-07-23 — Recorte do banco com fundo de cena (não é só transparente/branco)
**O que o user disse:** "tem algumas com fundo também, precisa tirar o fundo ou fazer aquele degradê pro nosso fundo padrão sempre que for usar elas. Não consegui remover o fundo por isso mandei assim." (imagens 274-299 que ele enviou pro banco).
**Regra:** ao usar um recorte do banco como figura solta no slide, checar o fundo: **branco ou transparente** → `mix-blend-mode:multiply` resolve, usar direto (crop no alpha via `getbbox()`). **Fundo de cena cinza embutido** (céu, parede, estrada) → o multiply NÃO apaga; recortar o sujeito no alpha OU aplicar o fade pro linho (`mask-image:linear-gradient(to bottom,transparent,#000 X%)`). O catálogo do banco (`_banco-referencias/README.md`) marca quais precisam de tratamento (274-299: são 276, 287, 288, 292). Não pintar fundo branco atrás achando que resolve — branco puro some, cinza não.

### 2026-07-24 — "Sair do operacional" (posição da casa, permanente)
**O que foi feito:** carrossel sobre o dono virar substituível construído sem se posicionar — o texto podia ser lido como "saia do operacional".
**O que o user pediu:** "não podemos passar ideia de 'saia do operacional' pois isso é um argumento muito forte nosso. O dono que quer sair do operacional, é melhor vender a empresa."
**Regra (permanente, vale pra todo conteúdo):** a Tatsuo é **contra** o discurso de sair do operacional. Dono que quer sair do operacional quer sair da empresa, e nesse caso o certo é vender. Quando o tema for delegar / ser substituível / a empresa andar sozinha, **posicionar explicitamente contra** e definir a coisa certa: a empresa para de PRECISAR do dono, e ele continua dentro **por escolha, não por refém**. Nunca prometer distância, ausência ou "liberdade de não trabalhar".

### 2026-07-24 — Repertório de empresa grande em conteúdo pra PME
**O que foi feito:** slide fechando em "por isso existe sucessão, por isso existe conselho".
**O que o user pediu:** "falamos sempre para o pequeno e médio empresário, coisas de empresas grandes como sucessão e conselho não traduzem nossa realidade."
**Regra:** o interlocutor é o dono de pequena e média empresa. Cortar instrumento de empresa grande (conselho de administração, governança formal, sucessão estruturada, board, comitê, valuation). O equivalente que fala com ele é gente formada, regra clara, quem decide no lugar dele. Vale também pra legenda e hashtags.

### 2026-07-24 — Pedrada alongada demais
**O que foi feito:** 16 slides num tema que se resolve em menos, com dois beats de patrimônio ("ninguém compra uma empresa pra virar você", "não pode nem adoecer") atrasando a virada.
**O que o user pediu:** "esse podemos ser mais breve, está alongando demais a pedrada."
**Regra:** o mínimo de ~8 slides do editorial-punch não é uma meta de comprimento. Quando a tese é um **critério** (uma régua), o carrossel é mais curto que quando é um **diagnóstico** (uma dor que precisa ser desenvolvida). Se um slide só acumula prova de algo já aceito pelo leitor, ele atrasa a virada — cortar. Faixa boa pra tema de critério: 12-13.

### 2026-07-24 — Pares A/B (contraste em dois slides) como recurso de ritmo
**O que o user pediu:** "o carrossel fica muito mais dinâmico quando um slide fala um contra e o outro o revés" (ex: slide A = a vantagem do pequeno, slide B = o revés do grande). Também melhora o trabalho de imagem: foto A = pequeno, foto B = grande, e a alternância de escala vira uma segunda camada de leitura. Preocupação dele: o carrossel fica gigantesco.
**Decisão (carrossel 6):** aplicar em **dois pares só**, os de melhor reveal, mantendo os outros contrastes inteiros. Motivos: (1) **teto duro de 20 slides** no carrossel do Instagram — abrir todos os contrastes de um editorial-punch de 16 daria ~26; (2) a partir do 3º-4º par o leitor antecipa o swipe e o A/B deixa de ser virada e vira formato.
**Regra:** o par A/B é **pontuação, não estrutura**. Antes de abrir, checar quantos pares o carrossel já tem embutidos (split com "...", metáfora A → metáfora B, causa → consequência) — normalmente já são 2-3. Abrir no máximo mais 2, escolhendo os de reveal mais forte, e alternar par → slide inteiro → par → slide inteiro. Um A/B integral (todo o carrossel em pares) é outro produto: vira **modelo próprio** (`modelos/duelo/`), não ajuste do editorial-punch.

### 2026-07-24 — Vídeo de terceiro em formato de lista vira SÉRIE de comportamento, não um carrossel-lista
**O que foi feito:** transcrição de vídeo de terceiro com "os 4 tipos de pessoa que você nunca deve contratar" virou um carrossel só, com os quatro tipos como beats internos e o fecho em critério de contratação.
**O que o user pediu:** "eu pensei em escrever 4 carrosséis a partir desse, e não um só. Os 4 sobre os 4 tipos de pessoas, mas não falando de funcionários, mas sobre comportamento. Ex: Gente morna acaba com a cultura aos poucos."
**Por que é melhor:** contratação é decisão pontual (o dono lê pensando no próximo currículo). Comportamento é o que acontece todo dia (ele lê pensando na terça-feira passada, e às vezes se reconhece). E um comportamento por peça deixa espaço pra desenvolver a corrosão lenta, que é o que dá o "aos poucos".
**Regra:** quando a fonte é uma lista de N tipos/erros/sinais, o default é **uma peça por item**, com o item tratado como comportamento, não como categoria de pessoa. Arquitetura de cada peça: comportamento → cena que o dono reconhece → o que corrói ao longo do tempo → **a parte do dono** → virada contra a leitura preguiçosa → régua concreta → CTA. E cultura não morre de evento, morre de repetição: esse é o motor da série.
**Regras de série (várias peças em sequência no feed):** (1) cada peça com **universo de imagem próprio**, senão o feed repete; (2) frase-âncora (ex: "o time copia tudo que você tolera") entra em **uma peça só**, senão vira bordão; (3) cada peça tem a **sua** virada anti-leitura-preguiçosa, nunca a mesma das outras; (4) 10-13 slides cada, porque um comportamento só não sustenta o comprimento do carrossel-diagnóstico; (5) o último slide de uma peça pode entregar o gancho da próxima. Exemplo vivo: `8_deslealdade-educada`, `9_torcida-contra`, `10_intocavel`, `11_copo-cheio` (o insumo da versão umbrella descartada ficou em `8_deslealdade-educada/_insumo-versao-umbrella.md`).

### 2026-07-24 — Nem todo item da lista-fonte sustenta uma peça forte (revisão da série)
**O que foi feito:** na 1ª rodada da série de comportamento, dois dos quatro voltaram fracos. **9 (invejoso/torcida contra)** ficou confuso por empilhar metáfora no TEXTO (moeda da empresa, placar, política interna). **11 (copo cheio)** ficou confuso por trocar de alvo no meio (começa no funcionário e vira pro dono sem avisar).
**O que o user pediu:** "ficou confuso pra caramba... acha que tem outra abordagem ou que não precisamos desse?" (9) e "ficou ruim, confuso, precisamos melhorar ou até não fazer" (11).
**O que corrigiu:**
1. **9** — tirar a metáfora do texto. O universo metafórico vive só na IMAGEM (arquibancada/placar); o texto fala direto (ele disputa razão, precisa do seu erro, você acendeu a torcida com comparação). Regra reforçada: metáfora na imagem, não no texto do slide (senão vira clichê e confunde).
2. **11** — um alvo só. Ficou 100% no dono a partir do slide 3 (o funcionário copo cheio é só gancho de reconhecimento). Regra: **uma peça, um alvo**; se o texto troca de sujeito no meio, o leitor se perde.
**Regra:** quando a fonte é uma lista, tratar cada item como candidato, não como obrigação. (a) Itens que se sobrepõem (invejoso ~ desrespeitoso silencioso: ambos "duas caras") podem virar a peça mais fraca ou cortável. (b) O item mais provocativo da lista costuma ser o melhor **fecho de série** quando vira 100% espelho do leitor (copo cheio → o copo do dono). (c) Se uma peça precisa de metáfora no texto pra se sustentar, provavelmente o beat está fraco: resolver na imagem ou cortar.

### 2026-07-24 — Punch confuso porque o slide ANTERIOR contradiz (checar a cadeia, não a frase)
**O que foi feito:** carrossel 7, slide 4 dizia "o peixe passou a chegar vivo" e o slide 5 emendava "O peixe não estava morrendo da viagem. / ELE ESTAVA MORRENDO DA PARADA."
**O que o user pediu:** "slide 5 não ficou claro porque eles morreram, talvez mudar para 'eles morreram por ficarem parados demais'."
**Diagnóstico:** a frase do 5 era vaga ("da parada" nomeia o estado, não a causa), mas o que realmente travava era a **contradição com o slide 4** — o leitor tinha acabado de ler que o peixe chegava VIVO. Trocar só a frase do 5 resolveria metade.
**O que foi corrigido:** o slide 4 parou de falar de vida/morte e passou a descrever o **conforto** ("Água limpa, espaço, nenhum predador"), e o 5 nomeou a causa com verbo e agente — "O problema nunca foi a viagem. / **ELES MORRIAM DE FICAR PARADOS.**".
**Regra:** quando o user diz que um slide "não ficou claro", conferir os **dois slides anteriores** antes de reescrever o slide apontado — no editorial-punch o handoff é encadeado, então falta de clareza costuma ser contradição ou premissa faltando, não escolha de palavra. E punch de mecanismo pede **verbo + causa explícita** ("morriam DE FICAR parados"), não o nome do estado ("morriam da parada").

### 2026-07-24 — Carrossel-parábola sem slide de PROMESSA (o leitor sai antes do payoff)
**O que foi feito:** carrossel 7 (tubarão no tanque) abriu com o gancho e emendou direto na história japonesa dos pescadores — quatro slides de peixe, tanque e viagem antes de a história virar espelho ("VOCÊ É O PEIXE").
**O que o user pediu:** "o principal ponto forte é o desenvolvimento, mas até chegar lá o cara já saiu da publicação. O início deve gerar mais curiosidade para reter o empresário, talvez uma frase mais impactante, e colocar um link com a história: o que os pescadores do Japão vão te ensinar sobre manter sua empresa viva."
**Por que acontece:** numa parábola, os primeiros slides falam de um universo que NÃO é o do leitor (peixe, barco, tanque). Sem um contrato explícito de payoff, o dono não tem motivo pra investir quatro swipes num assunto que não é o dele.
**O que foi corrigido:** (1) **capa mais visceral** — o paradoxo abstrato ("o problema é não ter nenhum") virou reconhecimento + lacuna: "A sua empresa não está em crise. **Ela está apodrecendo em água limpa.**"; (2) **slide 2 = a ponte**, uma promessa nomeada em uma frase — "O que os pescadores do Japão vão te ensinar sobre manter a sua empresa viva."; (3) **história comprimida** (dois beats viraram um) pra a virada não atrasar mesmo com o slide a mais.
**Regra:** todo carrossel construído sobre **história/parábola/analogia** leva um **slide-ponte logo depois do gancho**, dizendo em uma frase o que a história vai entregar pro negócio dele. O custo é um slide; o retorno é o leitor atravessar o setup. E a ponte NÃO substitui o gancho: slide 1 continua sendo o soco (regra de 2026-07-20). Estrutura de abertura da parábola: **soco → promessa → história → espelho**. Ao inserir a ponte, comprimir um beat do setup pra a virada não escorregar pra frente.

### 2026-07-27 — CTA que vende a tarefa, não o desejo do empresário
**O que foi feito:** carrossel 13 (equidade × igualdade) fechava com "Comenta 307, que eu te mostro como reconhecer quem entrega sem quebrar a justiça do time".
**O que o user pediu:** "esse CTA não vende pro empresário. O empresário quer aprender mais sobre como construir uma cultura forte do que como reconhecer funcionário." Trocou por "construir uma cultura forte que segura os seus melhores".
**Regra:** o CTA vende o que o dono QUER aprender (o resultado grande: cultura forte, empresa que sobra, máquina de vendas), não a mecânica que apareceu no conteúdo (reconhecer funcionário, dar bônus, corrigir). A tarefa é meio; a cultura/lucro/crescimento é o desejo. Alinhar a legenda: a ponte de fecho sobe do gesto isolado (bônus) pra cultura antes do CTA. Vale pra todo editorial-punch.

### 2026-07-28 — Capa que acusa não segura o ICP + reveal antes da dor
**O que foi feito:** carrossel 14 (protagonista x vitimista) abria a capa acusando ("Você culpa o mercado, a crise, a equipe / MENOS A ÚNICA PESSOA QUE RESOLVE") e entregava o reveal ("é você") já no slide 2.
**O que o user pediu:** "slide 1 faz nosso ICP parar pra ler?" (não fazia) e "slide 2 você apresentou a solução cedo demais, nem bateu na dor dele".
**Por que acontece:** ninguém se enxerga como "o cara que culpa os outros" — capa que aponta o dedo vira defesa ("isso não é comigo"), não curiosidade. E reveal/solução antes de a dor doer não tem peso.
**O que foi corrigido:** capa virou reconhecimento da dor sentida na pele ("Todo ano você jura que vai ser diferente / E TODO ANO A CULPA É DE OUTRO") — espelho, não acusação; a culpa entra plantada, o dedo vem depois. O reveal desceu pro slide 6, atrás de 4 slides de dor (cena da culpa → refém → anestesia → rodando).
> **[PARTE SUPERADA em 13/10/2026]** O user retirou o "nunca o dedo na cara no slide 1": às vezes ele vem no slide 1, e a acusação pode ser a entrada ou o destino do arco, conforme o conteúdo. Continua valendo o miolo da lição: o dedo na ferida aperta a DOR que o dono sente, não condena o caráter dele (ver `voz-tatsuo.md` → "Dedo na ferida é condenar a DOR").

**Regra (texto original de 28/07):** capa do editorial-punch = reconhecimento de um estado doloroso + lacuna/paradoxo (como a capa "apodrecendo em água limpa"), nunca o dedo na cara no slide 1. A acusação/responsabilização é o destino do arco, não a entrada. E reveal/virada só depois de a dor estar desenvolvida — solução cedo demais desperdiça o peso. Reforça 2026-07-20 (gancho no slide 1) e o arco soco→dor→virada.

### 2026-07-28 — Pedrada fraca = verdade genérica; ancorar o CTA num terreno concreto
**O que foi feito:** (1) slides de mecanismo/consequência corretos mas mornos ("o mundo mudar no seu lugar", "E NÃO CHEGA A LUGAR NENHUM"). (2) CTA de tema pessoal fechava só na escolha filosófica (solução ou problema).
**O que o user pediu:** "pouco pedrada, pouco verdade na cara do empresário"; "está muito fraco"; e no CTA, virar a chave depois de "você não controla o mundo" pra "você só controla o que você conhece" — quem não conhece a DRE, a margem de contribuição, não controla o resultado.
**O que foi corrigido:** pedrada = verdade específica e desconfortável ("você virou refém de quem nem sabe que você existe"; "Muito suor pra continuar parado"). E o fecho ganhou um degrau concreto: controla o que faz → **controla o que conhece** → o que ele não conhece são os números → CTA oferece exatamente isso ("os números que tiram a sua empresa do achismo e botam no seu controle").
**Regra:** (1) claim correto não basta — a pedrada precisa nomear o custo específico que o dono reconhece, com verbo e agente, não o estado genérico. (2) Mesmo em tema pessoal (sem MBV nos slides), o CTA ancora melhor num terreno acionável e nosso: virar a chave do abstrato ("controla o que faz") pro concreto ("conhece os números") dá ao "Comenta 307" o que entregar. Não contradiz 2026-07-23 — é o gancho de Lucratividade entrando por escolha, no fecho, sem esfriar a dor. (3) CTA padrão do user = **307**.

### 2026-07-28 — Texto do "básico" com cara de vendedor, não de dono (carrossel 13)
**O que foi feito:** carrossel sobre disciplina/cultura (fonte: transcrição do Hélio sobre "só fazer o básico dobra a receita"). O básico saiu literal da fala — "prospectar, ligar, aparecer", "ligar pra cliente", "cadê as ligações" — e o elogio do fracasso era "você é qualificado demais pra ficar ligando".
**O que o user pediu:** "gostei, mas parece mais voltado a funcionário, a vendedor do que dono de empresa."
**O que foi corrigido:** elevar o básico pro **comando do dono** — "acompanhar o número, cobrar a meta, puxar a venda (através do time)", "cansa cobrar, cansa acompanhar, cansa estar em cima", "cadê a rotina que você largou". O elogio do fracasso passou a bater no **ego do dono**: "você é o dono, não é você que tem que estar cobrando isso" (que é a própria isca do "saia do operacional"). Régua = "comandar no dia ruim", não "ligar".
**Regra:** o interlocutor é o DONO. Mesmo quando a transcrição-fonte fala em prospecção/ligação (rotina de vendedor), traduzir o "básico" pra a linguagem de comando do dono — cobrar, acompanhar número, puxar resultado através do time, manter a rotina de gestão. "Ligar pra cliente / prospectar" é tarefa de quem executa; o dono faz a empresa executar. Vale pros slides E pra legenda. Cuidar pra não implicar que o dono faz tudo sozinho (contradiz "faz resultado através dos outros").

### 2026-07-28 — "Carregar nas costas" vira o dono, não o funcionário (PME)
**O que foi feito:** carrossel 13, slide 9 fechava "É reconhecer quem carrega a empresa nas costas" com foto de um homem carregando uma viga nas costas.
**O que o user pediu:** "pode soar ruim pro empresário, porque em pequena e média empresa quem carrega tudo nas costas é o próprio dono. Trocar por 'quem veste a camisa', que faz mais sentido de pertencimento." (E a imagem de peso nas costas reforçava justo a leitura errada.)
**Regra:** no conteúdo pra PME, "carregar a empresa nas costas" é a autoimagem do DONO, não elogio ao funcionário. Pra reconhecer o comprometimento do time, usar linguagem de pertencimento ("vestir a camisa", "joga junto"), não de peso/sacrifício. E a IMAGEM segue o texto: nada de figura carregando carga nas costas quando a ideia é pertencimento; usar o trabalhador vestindo o avental/uniforme, com ar de dono do lugar.

### 2026-07-28 — Margem de contribuição × lucro líquido (não confundir quem cada uma paga)
**O que foi feito:** carrossel 15 (a margem que vale o risco), slide definia "Margem é o que sobra depois que todo mundo recebeu. É o pagamento do dono."
**O que o user pediu:** "margem de contribuição é o salário da empresa, não o do dono. O do dono é o lucro líquido." Corrigido pra "Lucro é o que sobra depois que tudo foi pago. É o pagamento do dono pelo risco que só ele correu."
**Regra:** distinção técnica que a marca (fim do analfabetismo empresarial) tem que acertar. **Margem de contribuição** = o que sobra de cada venda pra sustentar a estrutura = **salário da empresa**. **Lucro líquido** = o que sobra depois que TUDO foi pago = o que remunera o **dono**. O que paga o dono pelo risco é o LUCRO, não a margem. "Margem/margem boa" no sentido coloquial ("a fatia que você fica", "quanto sobra em cada venda") continua válido em capa/tese; mas ao atribuir "o pagamento do dono", usar LUCRO. Vale pros slides e pra legenda.

---

## Erros de motor / imagem

### 2026-07-24 — Cortar o topo da imagem NÃO desce o sujeito (mecânica, permanente)
**O que foi feito:** pra tirar o texto de cima do sujeito (o monitor no slide 15, o frasco de soro no 7), tentei cortar o topo do quadrado (`EXTRA_TOP`), na expectativa de empurrar o sujeito pra baixo.
**Por que não funciona:** a foto entra com `bottom:0; width:100%`, ou seja, ancorada no rodapé e com escala fixa (largura da imagem = 1080). Cortar o topo só encurta a imagem; o sujeito **fica exatamente na mesma altura absoluta** no slide.
**Regra:** `EXTRA_TOP` serve pra **tirar conteúdo médio/escuro da faixa de texto** (o caso da água no carrossel 6) e pra matar emenda de topo, nunca pra reposicionar o sujeito. Quando o texto encosta no sujeito, quem cede é o **bloco de texto** (subir o `top` e/ou reduzir a Anton) — ou se regera a composição. Nunca `scale`.

### 2026-07-24 — Teto de altura do bloco quando o slide tem Anton sobre foto
**O que foi feito:** Anton em 2 linhas preenchendo a coluna (~930px → 144px) caiu em cima do frasco de soro (slide 7) e a serif de remate ficou ilegível em cima do monitor (slide 15).
**O que foi corrigido:** antes de rodar o autofit, medir no render onde começa o sujeito da foto e usar isso como **teto do bloco**: subir o `top` e baixar o alvo de largura da Anton até o bloco inteiro (incluindo o remate serif) terminar acima do sujeito. Ficou 840px/92px no slide 7 e 760px/82px no 15.
**Regra:** o alvo de ~930px da Anton é o padrão, não uma obrigação. Em slide com foto sangrada, o limite real é a **linha do sujeito** — o bloco de texto inteiro tem que caber na faixa pálida acima dela. Anton menor que ~2x o corpo (44px) ainda é grito; Anton sobre o sujeito é erro.

### 2026-07-24 — Figura solta de corpo inteiro fica pequena demais
**O que foi feito:** o recorte do slide de CTA veio de corpo inteiro (601×1473 depois do crop na caixa). Numa altura que não invade o CTA, a figura sai com ~240px de largura: some no slide.
**O que foi corrigido:** cortar o recorte na **fração de cima da caixa** (`KEEP_TOP = {17: 0.60}`, ficou 601×883) — a figura vira meio-corpo, e na mesma altura ela ganha quase o dobro de largura. O `mask` de dissolução no rodapé resolve o corte na cintura.
**Regra:** figura solta de corpo inteiro raramente funciona em slide que já tem texto em cima e CTA embaixo. Cortar na cintura/peito depois do crop na caixa, e deixar a máscara dissolver o corte. Vale pro recorte gerado e pro recorte do banco.

### 2026-07-24 — gpt-image-2 devolve leve desvio de cor no "P&B"
**O que foi feito:** uma das imagens (ala hospitalar) voltou com uma mancha azulada numa parede, mesmo com o prompt pedindo black-and-white e "no added color".
**O que foi corrigido:** desaturar no pós, sempre: `Image.open(x).convert("L").convert("RGB")` antes de qualquer crop.
**Regra:** o P&B do editorial-punch é garantido no **pós-processamento**, não no prompt. Passo obrigatório do `post.py`.

### 2026-07-24 — gpt-image-2 ignora `size` (confirmado de novo) → resolver no pós, não no prompt
**O que foi feito:** 18 imagens pedidas em `1024x1024` com a composição descrita no prompt. **17 voltaram retrato (1024×1536)** e 1 voltou landscape (1536×1024). O parâmetro `size` é praticamente decorativo.
**Por que importa:** retrato a `width:100%` no slide vira 1620px de altura num canvas de 1350 — cobre o slide inteiro e come a faixa de texto.
**O que foi corrigido:** parar de brigar com o modelo. O prompt cuida só da **composição** ("sujeito no terço inferior, metade de cima pálida e vazia") e a proporção é resolvida no **pós-processamento**: crop do **quadrado inferior** (`side = min(w,h)`, ancorado no rodapé, centrado no eixo x). A composição pedida garante que esse crop pega o sujeito e mantém o topo pálido. Guardar o original em `imagens/_raw/` antes de cortar.
**Regra:** nunca confiar no `size` do gpt-image-2. Gerar com a composição certa, cortar pro 1:1 no pós (script), e só regerar se a **composição** vier errada. Ver `referencias/motor-imagem.md` → gotcha de orientação.

### 2026-07-24 — Figura recortada com objeto sangrando nas bordas = caixa cinza visível
**O que foi feito:** recorte do homem na proa (o barco entra pelas duas laterais do quadro). O crop na caixa pegou quase o canvas inteiro, e como o convés é **cinza** (não branco), o `multiply` deixou um **retângulo visível** flutuando no linho.
**O que foi corrigido:** máscara de dissolução nas bordas da própria figura, em vez de regerar:
```css
mask-image:linear-gradient(to bottom,#000 0%,#000 50%,transparent 97%),
           linear-gradient(to right,transparent 0%,#000 15%,#000 85%,transparent 100%);
mask-composite:intersect;   /* + -webkit-mask-composite:source-in */
```
**Regra:** figura solta só entra "crua" quando o fundo é branco puro. Se o sujeito vier apoiado em algo cinza que sangra nas bordas, aplicar a máscara de dissolução (baixo + laterais) — o objeto some no linho e sobra o sujeito. Complementa a regra de 2026-07-23 sobre recortes do banco com fundo de cena.

### 2026-07-24 — Imagem metafórica que não "traduz a mensagem" → preferir o literal
**O que foi feito:** carrossel 9 (ninguém te contraria) montado com universo 100% metafórico de marcenaria — porta fechada = "pararam de te falar", plaina sozinha = "jeito de decidir não mudou", pilha de peças = "os acertos". Várias vieram bonitas mas **abstratas demais**: o dono olha e não liga a foto à frase.
**O que o user pediu (slide a slide):** "imagem deve ser mais literal"; "não transmite a mensagem"; "está muito abstrato, deve ser mais fácil de compreender". Trocou por cenas **literais e humanas**: mesa de reunião vazia com cadeira isolada (isolamento), duas pessoas cochichando no corredor (a fofoca que não chega em você), um chefe de costas com o time calado desviando o olhar (pararam de te falar), um artesão confiante admirando a própria obra sozinho (acertar ensina a parar de perguntar).
**Regra:** a metáfora visual só se sustenta quando a leitura é **imediata** — o dono tem que bater o olho e entender sem decifrar. Objeto/still-life metafórico funciona pra conceitos concretos (prumo=referência externa, esquadro=alinhar, oficina abandonada=abandono); **falha** em conceitos relacionais/humanos (alguém deixou de te falar, o time cochicha, o dono decide sozinho) — esses pedem **gente em cena, ação literal**. Na dúvida entre metáfora elegante e cena literal clara, escolher o literal. Vale mais o dono entender do que o slide ser sofisticado. O "universo coerente" do modelo é um bônus, não uma prisão: clareza da mensagem ganha da coerência estética.

### 2026-07-24 — Herói Anton discrepante quando o setup é curto → casar com a linha de referência
**O que foi feito:** slide-herói com a linha Anton preenchendo a coluna toda (~930px, deu 108px) enquanto o setup serif logo acima era bem mais curto — "está muito discrepante a disposição de espaço das duas frases".
**O que foi corrigido:** trocar o alvo do autofit de `930` (preencher coluna) para `'ref'` (casar com a largura da linha de referência logo acima). Aí as duas linhas ficam com larguras próximas e o bloco respira equilibrado.
**Regra:** herói Anton preenche a coluna (930) só quando a frase é longa (é a linha mais larga do slide). Quando o setup acima é curto, o Anton casa com ele (`'ref'`), senão o grito fica desproporcional ao par. Complementa a regra de "Anton casa a margem da linha de referência".

### 2026-07-24 — Geometria da elipse cortando a linha de cima
**O que foi feito:** `elipse-larga` com `height:2.35em; top:-0.62em` (herdado do carrossel 4) por cima de uma linha de 44px: a borda superior da elipse atravessava a **linha anterior**, parecendo um risco de tachado.
**O que foi corrigido:** `height:1.78em; top:-0.36em` — a elipse abraça só a própria linha.
**Regra:** elipse encapsula **uma linha**. Depois de aplicar, renderizar e conferir se a borda de cima não invade a linha anterior; se invadir, baixar `height`/`top`.

**Correção (2026-07-24, carrossel 7):** `1.78em` / `-0.36em` AINDA invadia a linha de cima quando a estrofe tem duas linhas (a `elipse-larga-2` tem folga de traço no topo). Valor que fecha a 44px com `line-height:1.26`: **`height:1.50em; top:-0.08em`**. Usar esse como referência e conferir no render — a elipse tem que abraçar só a própria linha, sem tocar a de cima.

### 2026-07-24 — Autofit da Anton quando a linha é LONGA
**O que foi feito:** o script de autofit casava a Anton com a largura da linha de referência (a serif logo acima). Como as frases Anton eram longas (28-31 caracteres) e a referência curta, o cálculo devolveu **47-70px** — menor que o corpo de texto. Anton menor que a serif não é grito, é erro.
**O que foi corrigido:** quando a Anton é a linha **mais larga** do slide, ela não casa com a referência: ela **preenche a coluna de texto** (alvo ~930px de 940). E quando nem assim cabe com peso (frase muito longa), quebrar em **duas linhas Anton** e ajustar pela mais longa — foi o que deu o pico do carrossel 6 (122px em 2 linhas).
**Detalhe técnico:** medir com `white-space:nowrap` durante a busca binária. Sem isso a linha quebra, o `Range` mede a largura do contêiner e o autofit sobe até o teto.
**Regra:** "Anton casa a margem da linha de referência" vale quando a Anton é a **mais curta**. Sendo a mais larga, ela define a margem (preenche a coluna). Frase longa demais → duas linhas Anton, nunca encolher abaixo do corpo.

### 2026-07-24 — Elemento à mão que não cumpre função (seta sem alvo)
**O que foi feito:** slide de "a ordem chega torta" com `sublinhado-seta.png` sob a frase — o traço grifa e depois curva pra fora, mas **não aponta pra nada**.
**O que o user pediu:** "tem um risco com uma seta que não aponta pra ligar nenhum... é melhor deixar o segundo parágrafo todo em vermelho negrito."
**Regra:** **seta só entra quando existe um alvo visível** (uma palavra circulada, um número, um ponto da imagem). Seta decorativa polui. Quando não há alvo, a ênfase certa é a mais simples: a estrofe inteira em vermelho negrito. Vale o mesmo pros outros elementos — se você não consegue dizer pra onde o traço aponta ou o que ele encapsula, ele não deve estar ali.

### 2026-07-24 — Ênfase pode ser a ESTROFE inteira, não só uma linha
**O que o user pediu:** a segunda estrofe do slide toda em vermelho negrito (as duas linhas), em vez de recurso na linha de remate.
**Regra:** o vermelho negrito pode pintar a **estrofe inteira** quando ela é um bloco de sentido único (a consequência, o revés). Não vira "2 recursos" — continua sendo um. Útil quando a frase de punch precisa das duas linhas pra fechar.

### 2026-07-24 — Água/conteúdo escuro da foto invadindo a faixa de texto
**O que foi feito:** foto quadrada de mar aberto a `width:100%` (1080px de altura) subindo até a faixa do texto; a água em tom médio comia a legibilidade das linhas de baixo.
**O que o user pediu:** "a água pegou o texto, ficou difícil de ler, talvez cortar a parte superior da imagem é o suficiente."
**O que foi corrigido:** cortar o topo da imagem no pós (244px do quadrado) — a foto fica mais baixa e mais curta, começa abaixo do bloco de texto, e o `fade` do topo subiu de 16% pra 26% pra dissolver a nova borda (que já não é branca).
**Regra:** legibilidade ganha da composição. Se o conteúdo médio/escuro da foto sobe até o texto, **cortar o topo da imagem** (ela desce no slide) e aumentar o fade proporcionalmente. Não é mover o texto pra baixo — o texto tem posição de sistema; quem cede é a foto.

### 2026-07-24 — Figura solta desperdiçando a sangria
**O que foi feito:** slide de gancho montado como sanduíche (texto topo + figura recortada pequena no miolo + texto rodapé).
**O que o user pediu:** "pode ser melhor aproveitado em termos de imagem... figura preenchendo toda sangria e que transmita a mensagem". As três linhas subiram pro topo (2 + 1 estrofes) e a foto passou a ocupar o slide inteiro.
**Regra:** figura solta é pro slide que pede **respiro e isolamento**. Quando o slide carrega uma ideia que quer **peso** (um valor, uma ameaça, uma revelação), a foto sangrada na tela toda entrega muito mais. Antes de escolher o sanduíche, perguntar: essa imagem merece a tela inteira? Se merece, o texto vai todo pro topo.

---

### 2026-08-21 — "Subir a imagem" = subir o sujeito E completar a sangria (nunca deslocar com fade no rodapé) (carrossel 49)
**O que foi feito:** o user pediu pra "subir" as imagens dos slides 10 e 11. Eu desloquei a foto com `bottom:170/90px` + fade duplo (topo e rodapé) — a imagem flutuou e a sangria inferior ficou aberta (faixa de linho esvaziada embaixo).
**O que o user pediu:** "sempre que eu pedir para subir a imagem, é para subir ela E para terminar de gerar a parte de baixo para completar a sangria."
**Regra (permanente, pedida pelo user):** "subir a imagem" NUNCA é `bottom` offset com fade no rodapé. É **regerar a composição** com o sujeito mais alto no quadro e **mais primeiro plano embaixo** (chão, mesa, parede continuando) preenchendo o terço inferior e sangrando na borda — a imagem continua ancorada em `bottom:0` cobrindo até a borda. Outpainting da mesma imagem sai sujo (gotcha 2026-07-16); o caminho limpo é regerar a cena com a instrução "the subject sits in the MIDDLE of the frame, generous foreground filling the entire bottom third, bleeding off the bottom edge". Fade duplo com foto deslocada segue existindo só como exceção do slide de CTA dividido (2026-07-28), não como resposta a "subir a imagem".

### 2026-08-03 — Regen de imagem não pega por causa do `_raw` preservado (post.py)
**O que foi feito:** no carrossel 19, reprovei 2 imagens (luminária invadindo o texto no slide 7; figura de braços cruzados no CTA 13, que contradiz a linguagem do vitimista) e rodei `gen.py 7 13` + `post.py 7 13`. As duas voltaram **idênticas** às reprovadas.
**Por quê:** o `post.py` guarda o raw original em `imagens/_raw/` com `if not keep.exists(): keep.write_bytes(...)`. No regen, o `gen.py` sobrescreve `imagens/img-0X.png` com o raw novo, mas o `post.py` vê que `_raw/img-0X.png` **já existe**, ignora o raw novo e **reprocessa o antigo**, sobrescrevendo a imagem nova com a velha. O regen é perdido.
**O que corrigiu:** antes de regerar, **apagar o `_raw` daquele slide**: `rm ../imagens/_raw/img-0X.png` → `gen.py X` → `post.py X`. Aí o post copia o raw fresco e processa certo.
**Regra:** ao regerar uma imagem já pós-processada, apagar `imagens/_raw/img-0X.png` ANTES do `gen.py`/`post.py`. Senão o `post.py` reprocessa o raw antigo e o regen não aparece. (Vale pro pipeline `_scripts` copiado entre carrosséis.)

### 2026-08-03 — Conceito abstrato positivo (prosperidade) pede CUE explícito, não a cena literal genérica (carrossel 20)
**O que foi feito:** slide de "lugar próspero forma gente próspera" com a foto de uma loja de rua comum (açougue/mercearia com clientes). O user: "não transmite nem um pouco a sensação de lugar próspero."
**Por quê:** "loja com gente" é o literal de *comércio*, não de *prosperidade*. Conceito abstrato positivo (prosperidade, sucesso, crescimento, fartura) não aparece só por mostrar o cenário — precisa dos **sinais** do conceito na cena.
**O que corrigiu:** regerar pedindo os cues explícitos de prosperidade: **prateleiras abundantes lotadas do chão ao teto, dono confiante e sorridente atendendo, dinheiro trocando de mão, movimento de clientes felizes, fartura, luz rica**. Aí o armazém lê como "negócio prosperando".
**Regra:** pra ilustrar um conceito abstrato positivo, listar no prompt os **sinais concretos** dele (prosperidade = abundância + movimento + dinheiro + orgulho + fartura), não só o lugar onde ele aconteceria. Complementa a regra de 2026-07-24 (imagem literal): o literal do *cenário* não é o literal da *mensagem*. Vale o teste: bate o olho e sente o conceito? Se sente só "um comércio", falta cue.

### 2026-08-03 — Cortar o topo não basta quando o conteúdo ruim está no MEIO da imagem (faixa baixa) (carrossel 20)
**O que foi feito:** slides 2 (prateleira) e 11 (toldo) com conteúdo médio/escuro batendo no texto. Tentei cortar 25% do topo do quadrado — o render voltou **idêntico**.
**Por quê:** a imagem entra `bottom:0; width:100%` (ancorada no rodapé). A prateleira/toldo não estava no topo do recorte, estava no MEIO — cortar 25% do topo só removeu céu/vazio e encurtou a imagem; a prateleira ficou na **mesma altura absoluta** (reforça 2026-07-24 "cortar o topo NÃO desce o sujeito").
**O que corrigiu:** recortar uma **faixa mais baixa** da foto (landscape, ~bottom 40-55% do raw) que **exclui** a prateleira/toldo — sobra só o assunto de baixo (mãos+mesa / loja+gente) com linho limpo acima do bloco de texto.
**Regra:** quando o conteúdo que invade o texto está no miolo/topo-do-conteúdo (não no topo-vazio), não adianta "cortar um pouco do topo": recortar uma faixa baixa que exclua de vez o elemento ruim, exibida em landscape ancorada no rodapé. O que define quanto cortar é onde o assunto bom começa, não uma % fixa.

### 2026-08-06 — User define abertura em 2 slides: pergunta-isca + tapa literal (carrossel 23)
**O que foi feito:** capa-espelho padrão ("Você jura que ninguém quer trabalhar. / Gente boa existe. E já está empregada.") e o "roubar dos outros" do MBV suavizado pra "tirar gente boa de outra empresa" no miolo.
**O que o user pediu:** "Slide 1: quer uma dica de como encontrar gente boa? Slide 2: ROUBE DOS OUTROS. e seguir." Ou seja, abertura em DUPLA: slide 1 é a isca (pergunta que oferece uma dica), slide 2 é o tapa em Anton vermelho puro, com a frase crua do Hélio SEM suavizar. O beat da capa antiga desceu pro slide 3 como justificativa.
**Regra:** (1) quando a fonte tem uma frase agressiva marcante do Hélio ("roube dos outros"), ela é candidata a slide-grito literal, não a parafrasear com eufemismo; a suavização mata o punch. (2) Abertura pergunta-isca → resposta-tapa é um padrão de gancho válido: capa promete a dica, slide 2 entrega o choque, e o resto do arco justifica. Anton fills-column no grito puro (sem setup serif no slide).

### 2026-08-06 — Pilares do clima organizacional como "o que se vende" na atração/retenção (carrossel 23)
**O que foi feito:** o beat "o que se vende" ficou genérico ("você vende desafio e crescimento, um futuro maior que o atual") e a abordagem usava "gosta de onde você está hoje?".
**O que o user pediu:** (1) trocar "gosta" pela ideia de **ter orgulho** ("você tem orgulho de onde trabalha?"), que casa com o pilar de Cultura do MBV; (2) adicionar sutilmente os **pilares do clima organizacional**: ganhar bem ele já ganha, o jogo pra trazer E manter esse profissional é outro. É ele saber que ali vai **aprender mais, se divertir mais e ter orgulho de pertencer** àquele lugar; (3) o Hélio é quem ensina a construir o ambiente que retém essas pessoas (CTA).
**O que corrigiu:** slide 8 virou a virada ("Ganhar bem, esse cara já ganha. O que faz ele trocar de lado não está no contracheque"), entrou slide 9 com a tríade do clima (aprender / divertir / orgulho de pertencer, punch no orgulho), e o CTA fechou vendendo o ambiente que atrai e segura ("uma empresa que gente boa escolhe e não quer largar").
**Regra:** em tema de time/contratação/retenção, o que a empresa "vende" pro profissional são os pilares do clima: **aprender mais, se divertir trabalhando e ter orgulho de pertencer** (dinheiro ele já tem; a disputa não se ganha no contracheque). "Orgulho" > "gostar" nesse contexto. E o fecho amarra: esse ambiente se constrói com método, e é o que o Hélio ensina.

### 2026-08-06 — FABULA: espelho que "vive fora do chão" passa ideia de sair do operacional (carrossel 25)
**O que foi feito:** na fábula da visão sistêmica (toupeira), o espelho era uma águia apresentada como "ela quase não punha as garras no chão" — o bicho-modelo vivia FORA da operação.
**O que o user pediu:** "dá a impressão de que a águia saiu do operacional, e não é isso que pregamos". Trocar por um animal que voe mas tenha hábitos de chão, e explorar que estar presente na operação mantém o tato do negócio; o que muda é DE ONDE se decide (pensando no todo). Virou a garça: pés na lama todo dia, igual a todo mundo, e só sobe antes de decidir.
**Regra:** na FABULA, o **espelho encarna a posição da casa** — o leitor entende o bicho-modelo como "o certo a ser". Bicho que vive longe do chão/da operação contradiz a regra de 2026-07-24 ("sair do operacional" é discurso que combatemos), mesmo sem dizer isso no texto. O espelho certo trabalha NA operação como o protagonista e se diferencia só no gesto de decidir (sobe antes de escolher). Checar o espelho contra as posições da casa antes de escrever o arco.

### 2026-08-06 — FABULA: slide com 6+ linhas é inviável de produzir (carrossel 25)
**O que foi feito:** slides 5, 11, 12 e 14 saíram com 5-9 linhas (dois exemplos de erro, moral com 4 estrofes + CTA) — texto demais pra caixa da FABULA (texto no topo + gravura embaixo).
**O que o user pediu:** "tem slides com muito texto, fica inviável produzir um slide assim".
**Regra:** teto prático do slide FABULA = **~3 estrofes / ~5 linhas curtas** (a §4 do modelo diz 2-6 linhas; mirar o meio da faixa, não o teto). Um exemplo basta (não empilhar dois casos do mesmo erro); a moral também é compacta (1 estrofe de espelho + 1 punch + CTA). Se o beat precisa de mais texto, dividir em dois slides ou cortar.

### 2026-08-06 — CTA sobre foto de cena cheia ilegível → figura flutuante recortada (carrossel 24)
**O que foi feito:** slide 12 (fechamento + CTA) com a foto de cena cheia (dono no balcão da loja abastecida) subida com fade duplo. Mesmo com o prompt pedindo "figure low in the frame, upper two thirds pale", a cena veio com prateleiras cheias subindo até o meio e o texto ficou em cima do conteúdo escuro: "a imagem está pegando muita parte do texto e não deixa ler nada".
**O que o user pediu:** trocar por "uma daquelas flutuantes que não ocupa tanto espaço, mas sem perder o sentido da mensagem".
**O que corrigiu:** regerar como **cutout** (sujeito isolado em fundo branco, mesma mensagem: dono confiante de braços cruzados), crop na caixa + corte na cintura (~56% de cima), figura centrada no miolo (~460px de altura entre o texto e o CTA) com máscara dissolvendo o corte embaixo. Texto e CTA 100% sobre linho.
**Regra:** no slide de CTA, se a foto de cena tem conteúdo médio/escuro subindo além do rodapé (loja cheia, prateleira, interior), não insistir em fade — trocar por **figura flutuante recortada** (meio-corpo) no miolo, que preserva o sentido e deixa o CTA sobre linho limpo. A cena cheia funciona no CTA só quando o entorno do sujeito é genuinamente pálido/vazio.

### 2026-08-06 — Ajuste de linguagem pontual: "taria ganhando" → "teria ganho mais" (carrossel 24)
**O que o user pediu:** no slide 2, trocar "se eu vendesse mais, taria ganhando" por "se eu vendesse mais, teria ganho mais". **Correção só daquele carrossel**, não é regra geral de voz (o coloquial continua permitido quando fizer sentido).

### 2026-08-06 — Capa com metáfora + punch juntos → dividir em dupla espelho → tapa (carrossel 26)
**O que foi feito:** capa única com a tese e o punch no mesmo slide ("Ser dono... é dormir de cobertor curto. / Cobre a cabeça, descobre o pé.").
**O que o user pediu:** dividir em 2 slides — slide 1 só a frase-espelho ("Ser dono de empresa no Brasil é dormir de cobertor curto."), slide 2 só o punch em grito ("Cobre a cabeça, descobre o pé.", Anton vermelho fills-column). Motivo: "fica mais impactante a mensagem e melhor de trabalhar as imagens para cada slide isoladas".
**Regra:** quando a capa carrega metáfora + punch, avaliar a dupla: slide 1 = a frase-espelho (a imagem ilustra a metáfora inteira), slide 2 = o punch sozinho em Anton vermelho (a imagem ilustra só o detalhe do punch). Generaliza o padrão isca → tapa do carrossel 23: o tapa ganha slide próprio e cada metade ganha a própria imagem. O user elogiou muito essa estrutura.

### 2026-08-06 — Abertura com 3 imagens do mesmo motivo + Anton de grito puro grande demais + still parado pra conceito de movimento (carrossel 26)
**O que foi feito:** (1) slides 1-3 todos com cama/cobertor/pés (capa, tapa e cena) — "é o terceiro slide e a imagem está muito repetitiva"; (2) grito puro fills-column a 146px — "o tamanho da fonte está enorme"; (3) "acorda na conta dos outros" ilustrado com notas paradas na mesa de cabeceira — "não transmitiu a mensagem"; (4) capa com muito espaço negativo em cima — pediu fonte menor, bloco mais alto e imagem maior.
**O que corrigiu:** (1) o slide 3 saiu do quarto e virou a tradução da frase no mundo do trabalho (feirante puxando lona curta demais sobre as caixas: cobre uma ponta, descobre a outra); (2) Anton do grito puro desceu pra ~100px (alvo 640, não 930); (3) a nota parada virou mão entregando o maço na mão de outro (o movimento carrega o sentido); (4) capa regerada com o sujeito GRANDE no quadro (cama preenchendo a metade inferior) + fonte 48px + bloco em top:400.
**Regra:** (1) a regra de variedade vale JÁ na abertura: no máximo 2 slides seguidos do mesmo motivo, mesmo quando a metáfora é a moldura do carrossel — o 3º beat traduz a metáfora pro mundo do dono. (2) Anton fills-column (930) é pra frase que precisa de peso máximo; em grito puro de frase curta o teto confortável é ~100-110px — acima disso o user acha enorme. (3) Conceito de MOVIMENTO (dinheiro que sai, troca de dono, passa) pede GESTO na imagem (mão entregando, saindo), nunca still-life parado — complementa a regra do cue explícito (2026-08-03). (4) Na capa, sujeito grande no quadro > texto descendo atrás de sujeito pequeno.

### 2026-08-06 — FABULA: protagonista gigante em cena com outros bichos/cutaway (carrossel 25)
**O que foi feito:** na vista em corte (vila em cima, túneis embaixo), o toupeira saiu gigantescamente desproporcional — a câmara dele do tamanho da rua inteira, ele maior que os cidadãos da superfície.
**O que o user pediu:** "o tamanho da toupeira está gigantescamente desproporcional a dos outros animais".
**Regra:** o gpt-image-2 infla o protagonista quando ele é o foco da cena. Em cena com múltiplos personagens, multidão ou **corte/cutaway** (dois mundos no mesmo quadro), travar a escala no prompt: "the [bicho] is SMALL, exactly the same body size as the townsfolk animals; his rooms are modest burrow-sized, much smaller than the houses". Vale deixar uma cláusula de escala no prompt-base do carrossel inteiro (todos os personagens na mesma escala realista relativa). Cena solo não precisa.

### 2026-08-06 — Capa-redefinição não é gancho (tese ≠ gancho) (carrossel 26)
**O que foi feito:** capa do carrossel 26 com a frase-tese do input ("Crescer não é faturar mais. / É aumentar a última linha.") — uma redefinição conceitual como slide 1.
**O que o user pediu:** "o slide gancho não pega a atenção do público... o gancho está fraco. me dê 4 variações." Escolheu o paradoxo-espelho: "A sua empresa cresceu. / E o seu bolso nem ficou sabendo." A tese desceu pro miolo (reveal, slides 6-7).
**Regra:** frase-gancho forte do user é candidata a capa (2026-07-30), MAS só se for gancho de verdade: uma capa que REDEFINE um conceito é aula, explica antes de doer — o ICP não para pra ler definição. Teste: a capa nomeia uma dor/paradoxo que o dono sente na pele, ou ensina algo? Se ensina, é tese: vira o reveal do miolo, e a capa nasce do paradoxo-espelho da mesma ideia (reforça 2026-07-28: reconhecimento + lacuna). No slide 1 da capa nova, subir o bloco de texto pra não encostar na imagem (o texto vive inteiro na faixa clara).

### 2026-08-06 — FABULA: proporção texto×gravura, corte de painéis e padrão de cinema (carrossel 25, batelada)
**O que foi feito:** slides montados com o respiro do gabarito (`gap 1.95em`, texto a partir de 190px) e imagens landscape 1536×1024 em `object-fit:cover`. Resultado: (a) slides de 3 estrofes com texto tomando metade da tela e gravura pequena ("muito texto e pouca imagem, uma fábula deve ser o contrário"); (b) montagem de painéis com as laterais cortadas quase pela metade (o cover corta as bordas da landscape em caixa alta); (c) split de duas metades lido como "imagem cortada no meio sem motivo"; (d) planos repetidos, personagens sempre de frente ("imagens genéricas, eleve o padrão para cinema").
**O que o user pediu:** fábula é imagem dominante. Bons de proporção: slides curtos e a moral (que pode ter mais texto). Cada ângulo deve NARRAR (zenital do poço = afundar; aéreo = revelação); sugeriu até POV do personagem. Painéis não podem ser cortados; split de metades não usar.
**Regras (FABULA v2):**
1. **Texto compacto nos slides de conteúdo:** `margin-top:175px`, `line-height:1.42`, `.stanza + .stanza margin-top:1.15em`. A moral mantém o respiro do gabarito (190px / 1.95em) — mais área textual lá é aceito.
2. **Montagem de painéis = grade 2×2 QUADRADA** (pedir "SQUARE 1:1" com override no fim do prompt + `size 1024x1024`), nunca tira horizontal de 3 painéis — em caixa alta o cover decapita os painéis laterais.
3. **Split de duas metades: não usar.** Contraste A×B vira UMA cena contínua que contém os dois lados (ex: corte transversal no nível do solo — túnel embaixo, pomar morto em cima).
4. **Padrão cinema:** cada plano escolhido pela emoção do beat e VARIADO (macro/close extremo, de costas, zenital, aéreo, contra-plongée, POV é bem-vindo). Personagem de frente em plano médio é o default preguiçoso — usar pouco. Reforça a regra de "VARIAR os enquadramentos" do modelo, com régua mais alta.

### 2026-08-11 — Slide de fechamento+CTA com 3 blocos = muito texto; separar CTA em slide próprio (carrossel 30)
**O que foi feito:** último slide com fechamento (método + treinamento nomeado, 2 estrofes) E o CTA "Comenta 307" no mesmo slide — 3 blocos de texto.
**O que o user pediu:** "slide 13 pode ser dividido em 2, pois tem muito texto, o slide 14 só com a CTA."
**Regra:** evolução da regra 2026-08-03 (CTA pode ser 2 slides): quando o fechamento tem pedrada/método + treinamento nomeado, o "Comenta 307" vai num **slide só dele**. Fechamento = slide de conteúdo normal (2+2 com foto). Não empilhar fechamento e CTA num slide só.

### 2026-08-11 — Slide EXCLUSIVO de CTA usa o layout padrão (texto no topo + foto impactante sangrada), não figura solta + texto no rodapé (carrossel 30)
**O que foi feito:** o slide só-CTA saiu no layout herdado do fechamento+CTA dos carrosséis anteriores: figura flutuante recortada no miolo e o "Comenta 307," + frase-ponte no rodapé.
**O que o user pediu:** "o CTA está saindo sempre embaixo e com uma figura solta no meio... esse slide é exclusivo pro CTA, portanto pode ser como os demais, e com uma imagem muito bem impactante sob o subtexto."
**Regra:** o rodapé + figura flutuante é solução pra CTA que DIVIDE o slide com texto de fechamento em cima. Slide exclusivo de CTA = layout padrão do carrossel: "Comenta 307," (cta-big) + frase-ponte (3 linhas balanceadas) no topo (~236px) e **foto de cena impactante sangrando na metade de baixo** (no 30: retrato do dono com o time na porta da oficina). A imagem do CTA é um beat visual forte, não um recorte decorativo.

### 2026-08-11 — Doutrina: não é o lugar que "segura" gente — é a pessoa que ESCOLHE estar (carrossel 30)
**O que foi feito:** slide da régua com "constrói um lugar que segura gente".
**O que o user pediu:** "não é o lugar que segura, é a pessoa quem escolhe estar. E quando essa chave vira na cabeça do funcionário tudo muda: ele entende que ele faz porque ele quer, ele faz pelo futuro dele, e não pelo dono." Virou dois beats: "um lugar que gente boa escolhe" + slide novo ("Porque ninguém fica pelo dono. / Ele fica pelo futuro dele. / E o dia que essa chave vira, / ele entrega porque quer.").
**Regra (posição da casa, tema retenção/cultura):** evitar linguagem de **prender/segurar** gente como mérito do lugar — a agência é do funcionário: ele **escolhe** ficar, pelo futuro DELE (ecoa a doutrina "empresa é ponte do sonho dele", D3-S30). O ambiente é o que torna a escolha óbvia. E os pilares do clima são **4** (aprender, ganhar, se divertir, ter orgulho) — ao citar a tríade, incluir o "se diverte" (o user sente falta quando falta). Conecta com 2026-08-06 (pilares do clima) sem contradizer "segura gente boa" como verbo de RESULTADO no CTA (lá é aceito).

### 2026-08-11 — Beat "empresa para sem você" está batido nessa forma (carrossel 31)
**O que foi feito:** carrossel 31 (empresa não é família) com um slide-teste "Faz o teste: sai uma semana e observa o que acontece. Se tudo para, você não tem time. Tem uma folha de pagamento."
**O que o user pediu:** cortar o slide. "A ideia é boa, mas a dor de a empresa ser dependente da pessoa é muito batida dessa forma que foi apresentada." Sem substituição — o arco fechou em 11 slides.
**Regra:** a dor da dependência do dono ("sai X dias e a empresa para") já foi usada demais nesse formato de teste. Evitar o beat "se afaste e veja se para" como slide; se o tema pedir essa dor, achar um ângulo novo (mecanismo/consequência específica), não o teste da ausência. Cortar um beat batido > substituir por outro genérico.

### 2026-08-11 — Fechamento pulando direto pro treinamento sem desenvolver a SOLUÇÃO (carrossel 33)
**O que foi feito:** depois da régua ("ela escolheria a sua empresa?"), o fechamento resolvia a dor em uma estrofe ("Construir esse lugar não é sorte. É método.") e já emendava o treinamento nomeado.
**O que o user pediu:** "o desenvolvimento da solução nossa merece mais espaço do que 2 frases de uma estrofe... como vamos fazer isso? como vamos resolver a dor do cara? falta aprofundar nesse ponto."
**O que corrigiu:** entrou um slide próprio de CAMINHO antes do fechamento — o "como" concreto (não se constrói com frase na parede; se constrói com gestão: treinamento que vira rotina, meta clara, reconhecimento, caminho pra crescer). O fechamento seguinte só amarra (é método, método se aprende, treinamento nomeado).
**Regra:** o arco de fechamento tem 3 papéis em 3 slides: **caminho** (o como concreto, os componentes da solução) → **fechamento** (método + treinamento nomeado) → **CTA** (slide exclusivo). Nomear o treinamento sem antes mostrar O QUE se faz deixa a solução rasa — o leitor precisa visualizar o mecanismo antes da oferta. Complementa 2026-08-03 (CTA nomeia o treinamento) e 2026-08-11 (CTA em slide próprio).

### 2026-08-11 — Fechamento que só NOMEIA a solução é entrega rasa; desenvolver o método (carrossel 34)
**O que foi feito:** o fechamento resumia a solução em "Enxergar a empresa inteira não é dom. É método." e emendava direto no treinamento.
**O que o user pediu:** "é muita pouca entrega... desenvolva melhor a solução nossa, não precisa ser algo prático, mas para mostrar de fato que temos uma metodologia que funciona."
**O que corrigiu:** o fechamento virou 2 slides de conteúdo antes do CTA: (13) a PROMESSA do método, com contraste de consequência ("Com método, o erro aparece cedo. Sem método, aparece no prejuízo."); (14) o treinamento nomeado + a substância do que ensina ("o que olhar, onde cobrar e como fazer o time entregar").
**Regra:** complementa 2026-08-03 (nomear o treinamento) e 2026-08-11 (CTA em slide próprio): entre a virada e o CTA, a solução precisa de DESENVOLVIMENTO que prove que existe metodologia — uma promessa com contraste de consequência (com × sem método) e/ou a substância do que o treinamento ensina. Só declarar "é método" + nomear o treinamento soa vazio. Não precisa ser tático; precisa mostrar que o método existe e funciona.

### 2026-08-11 — Anomalia de anatomia (mão fantasma): corrigir com IMAGE-EDIT da própria imagem, não regerar (carrossel 33)
**O que foi feito:** o slide 6 (funcionário olhando o celular) veio com uma terceira mão fantasma. O user pediu: "não mude a imagem, só corrija esse erro".
**O que corrigiu:** image-edit do gpt-image-2 (input_image = a própria img processada, `tool_choice: required`) com prompt cirúrgico: nomear o artefato a remover ("remove the anomalous extra third ghost hand, the man must have exactly two arms and two hands") + travar todo o resto ("change absolutely nothing else: same man, same pose, same background, same lighting, same grain, same framing"). Voltou a mesma cena, sem a mão. Depois: `rm imagens/_raw/img-0X.png` → salvar o edit em `imagens/img-0X.png` → `post.py X` (re-desatura e re-cropa).
**Regra:** anomalia pontual (membro extra, objeto deformado) em imagem que o user gostou = **image-edit da própria imagem**, nunca regerar do zero (regerar perde a cena aprovada). O gotcha "image-edit copia a referência" vira vantagem aqui: é exatamente o que se quer. Prompt = nomear o defeito + cláusula de congelamento do resto. Lembrar do fluxo `_raw` (2026-08-03): apagar o raw antigo antes do post.py.

### 2026-08-11 — Capa: leitura rápida + linha-sussurro; imagem de capa pode ENCENAR a tese (carrossel 33)
**O que foi feito:** capa com 3 linhas de leitura "argumentada" (setup em 2 linhas + punch: "O sonho mais vendido do mercado / fica esquisito dito com clareza: / fugir da própria empresa.") e imagem de reconhecimento (dono exausto no balcão).
**O que o user pediu:** "o slide 1, gancho, deve ser leitura rápida e impactante" — cortou a linha explicadora ("fica esquisito dito com clareza:") e definiu a estrutura: impacto negrito (48px) + punch vermelho negrito (58px) + **linha-sussurro** ("e você caiu nisso como um pato.", 30px, sem negrito, "como se fosse um sussurro, algo discreto"). Na imagem: "ângulo aberto plongée com a empresa em primeiro plano e o empresário correndo em segundo plano" — a imagem ENCENA a tese em vez de só ambientar a dor.
**Regra:** (1) capa = leitura de 2 segundos: nada de linha "explicadora"/argumentativa; se uma linha só prepara a outra, cortar. (2) Novo recurso tipográfico da capa: o **sussurro** — a 3ª linha menor (≈30px), sem negrito, tom de deboche íntimo, abaixo do punch. Hierarquia: impacto > punch vermelho > sussurro. (3) A imagem da capa pode ser NARRATIVA (encenar a tese), não só ambientação da dor. **CORREÇÃO (mesmo dia, fim da saga):** depois de 10+ variações da cena narrativa (plongée, nível de rua, perfil chapado, diorama, proporções travadas), o user reprovou todas e mandou VOLTAR à primeira imagem entregue (o dono exausto no balcão, dor/reconhecimento). Lição: cena narrativa de tese com múltiplos elementos (prédio + figura em escala) é frágil no gpt-image-2 — cada correção quebra outra coisa (corte, escala, ângulo) e o resultado nunca fecha. Pra capa, a imagem de DOR/reconhecimento com um sujeito só é mais robusta e segura o gancho. Tentar a cena-tese no máximo 2-3 gerações; se não fechar, voltar pra dor com 1 sujeito. Guardar sempre o raw da 1ª versão aprovada antes de iterar (aqui o original foi sobrescrito e precisou regerar parecido).

### 2026-08-11 — Cue de imagem: "apodrecer" pede o podre literal; "grande demais" pede escala exagerada (carrossel 33)
**O que foi feito:** slide "ela apodrece em silêncio" ilustrado com loja abandonada (lona, poeira, teia) e slide "a conta já é grande demais" com uma pilha normal de envelopes.
**O que o user pediu:** "a imagem não transmite a ideia de apodrecer em silêncio"; "a imagem pode demonstrar de modo mais exacerbado a ideia de conta grande demais".
**Regra:** reforça o cue explícito (2026-08-03) com dois casos: (1) verbo forte no texto pede o cue LITERAL do verbo na cena — "apodrecer" = coisa podre visível (fruta estragada no caixote do balcão), não "abandono" (lona/poeira dizem abandono, não apodrecimento); (2) adjetivo de escala ("grande demais", "gigante") pede EXAGERO deliberado na cena (montanha absurda de contas soterrando a mesa, quase cômica), não a versão realista. A imagem traduz a palavra-chave do punch, não o cenário do beat.

### 2026-08-11 — Regen sobrescreveu uma versão que o user queria de volta (carrossel 33)
**O que foi feito:** na capa, iterei imagem v1 → v2 → v3 (monstro) apagando `_raw/img-0X.png` + `imagens/img-0X.png` a cada regen (procedimento de 2026-08-03). O user reprovou a v3 ("o monstro ficou muito visível") e pediu a v2 de volta — que já não existia. Sem snapshot/lixeira, tive que regerar com o mesmo prompt (saiu parecida, não idêntica) e avisar.
**Regra:** ao regerar uma imagem que é ITERAÇÃO de conceito (não correção de defeito), **versionar em vez de apagar**: `mv imagens/_raw/img-0X.png imagens/_raw/img-0X-v1.png` (e o processado também, se quiser) antes do `gen.py`. O "apagar o _raw antes do regen" (2026-08-03) continua valendo pro pipeline não reprocessar o antigo — mas apagar = renomear, nunca `rm`. Assim "volta a versão anterior" é sempre possível. E quando o user pede um elemento novo na imagem (ex: monstro), tratar como VARIAÇÃO da imagem atual, não como licença pra recompor a cena inteira.

### 2026-08-11 — Punch de consequência com palavra genérica ("problema") ou difícil ("vício"): buscar o coloquial com peso (carrossel 33)
**O que foi feito:** beat de cultura fechava "Na sua ausência, não nasce nada" — o user pediu pra elaborar a ideia "cultura da PME é a cultura do dono / empresa tem a cara do dono" e propôs o paralelismo "Dono ausente, X presente", vetando "problema" (genérico demais pra um problema de CULTURA).
**O que o user escolheu:** entre vício (preciso mas menos imediato), moleza (fácil mas raso), mau costume, relaxo, bagunça e desmando, ele escolheu **"jeitinho"** — "Dono ausente, jeitinho presente." Fácil de entender no primeiro olhar E específico de cultura (o atalho que vira regra).
**Regra:** (1) punch de consequência não usa palavra-balde ("problema", "coisa errada") nem palavra que exige elaboração ("vício"): procurar o termo coloquial que o dono entende de bate-pronto e que nomeia o mecanismo específico ("jeitinho", "mau costume", "relaxo"). (2) Paralelismo espelhado ("Dono ausente, X presente") é padrão de punch aprovado. (3) Ao pedirem uma ideia que é âncora de outro carrossel (aqui "cultura não se delega", grito do 32), sintetizar a ideia com redação própria — frase-âncora entra numa peça só; avisar o user do conflito.

### 2026-08-11 — Cena aberta sem nada cortado: o base "bleeding off" sabota; usar base próprio + diorama (carrossel 33)
**O que foi feito:** capa com cena ampla (loja + empresário correndo) iterada 5x com o prompt-base padrão do editorial-punch — o gpt-image-2 SEMPRE sangrava o sujeito na borda inferior (pés/pernas cortados) e/ou cortava a loja na lateral, mesmo com "nothing cropped", "strip of pavement below" e override no fim do prompt.
**Por quê:** o prompt-base do modelo manda "subject... bleeding off the bottom edge" — pra cena que precisa aparecer INTEIRA, essa cláusula vence qualquer pedido pontual de "não cortar".
**O que corrigiu (combinação que funcionou de primeira):** (1) **base próprio pro slide** (campo "base" no prompts.json + gen.py usando item.get("base")) — mesmo estilo P&B, SEM a cláusula de composição/sangria; (2) descrever a cena como **"small diorama floating in the center-bottom of the frame, with generous empty margins on ALL FOUR sides"**, nomeando o vazio de cada lado (rua à esquerda, calçada embaixo, rua à direita); (3) exibir a imagem em formato nativo, **sem o crop quadrado** do post.py (lista NO_SQUARE).
**Regra:** quando o slide pede a cena COMPLETA dentro do quadro (nada tocando borda), não adianta remendar o prompt-base: trocar por um base sem "bleeding off" e pedir o diorama com margens nomeadas nos 4 lados. O crop quadrado do pós também sai (NO_SQUARE) — quem garante o respiro é a geração, não o corte.

### 2026-08-14 — Repetir universo/tema entre posts próximos não veta metáfora (volume de 8-9 posts/dia) (carrossel 41)
**O que foi feito:** descartei a metáfora da pesca na escolha do gancho por "repetição de universo" com os posts 37-39 (no raso, água parada, maré), aplicando a regra de série.
**O que o user pediu:** a pesca era a melhor das opções; com 8 a 9 posts por dia o feed dilui e não fica repetitivo.
**Regra:** a regra de "universo próprio por peça" vale pra SÉRIE deliberada publicada em sequência, não pro feed geral — no volume atual, universo parecido entre posts vizinhos não descarta uma metáfora. O critério de escolha do gancho é a força da assimilação (o dono bate o olho e entende), não a distância temática dos posts ao lado. Ainda vale sinalizar a coincidência pro user decidir.

### 2026-08-14 — Subir imagem em slide de conteúdo = ESTENDER a parte de baixo (sangria completa), nunca offset + fade (carrossel 41)
**O que foi feito:** slides 7 e 8 com a cena começando só na metade de baixo (topo de névoa alto), miolo de linho vazio entre texto e sujeito. O user pediu "suba a imagem". Primeira tentativa: subir com `bottom:170px/80px` + fade duplo dissolvendo o corte de baixo no linho. O user corrigiu: "faltou gerar o restante da imagem, da parte debaixo, para completar a sangria toda como sempre fazemos."
**O que corrigiu:** **image-edit da própria imagem aprovada** (input_image = a processada, `tool_choice: required`) pedindo o canvas estendido PRA BAIXO: "everything currently visible stays identical and occupies the upper four fifths; continue the scene naturally downward" + o conteúdo concreto do primeiro plano novo (balcão descendo, chão / caixotes e cestos). A cena aprovada fica intacta em cima, o primeiro plano novo preenche o rodapé, e o slide volta ao padrão `bottom:0` com fade só no topo. Saiu de primeira nos dois. Versionar os raws antes (`img-0X-v1.png`), nunca rm (2026-08-11).
**Regra:** slide de conteúdo do editorial-punch tem **sangria completa sempre** — imagem ancorada em `bottom:0` tocando a borda. "Subir a imagem" = gerar o pedaço de baixo que falta via image-edit da imagem aprovada (a extensão preserva a cena; é o mesmo mecanismo da correção de anomalia de 2026-08-11), não deslocar com offset + fade de rodapé. O offset com fade duplo continua existindo SÓ no slide de CTA dividido (2026-07-28). Complementa 2026-07-23 ("gere a parte que falta de baixo, pois vc subiu elas") — agora com o método que preserva a cena em vez de regerar do zero.
**Nota de texto (mesmo carrossel):** "Aí a venda cai" → **"Aí as vendas caem"** — no coletivo de vendas do dia a dia, o plural é a forma natural de falar (mesmo espírito de "os juros", 2026-08-06).

### 2026-08-14 — Contraste A×B num quadro só: composição "quase-díptico do ringue" (corredor END-ON repartindo o meio) (carrossel 41)
**O que foi feito:** cena de contraste (barco do pescador desanimado × barco vazio com peixes pulando) montada em duas tentativas erradas: (1) píer atravessando o quadro na horizontal com os barcos sangrando nas bordas ("está cortando demais os barcos"); (2) diorama frontal com o píer CONECTANDO os dois barcos ("a ponte não deve conectar as duas imagens, ela só deve repartir ao meio... vista de frente").
**O que o user pediu:** a direção de câmera da imagem do ringue (post 40 da /frase, `40_nunca-perde/imagens/img-06.png`): perspectiva de UM PONTO, o elemento divisor visto DE FRENTE/END-ON nascendo na borda inferior central e fugindo pro fundo até sumir na névoa, câmera um palmo acima do plano (rente demais mata os elementos), lado A à esquerda e lado B à direita com pesos iguais, os dois inteiros no quadro.
**Regra:** quando o beat é contraste A×B **no mesmo quadro** (não em par de slides), a composição-padrão é o **quase-díptico**: divisor central end-on em perspectiva de um ponto + um lado por metade + simetria de pesos. No prompt: "strict one-point perspective, perfectly symmetric", o divisor "seen END-ON, starting at the bottom center edge and receding straight away, vanishing into pale mist at the center, splitting the frame into two equal halves", câmera "a hand's width above the surface", e cada elemento "fully visible, equal visual weight". Combina com base próprio sem "bleeding off" (regra do diorama, 2026-08-11) e formato quadrado 1:1. Referência canônica: o ringue do post 40.

## Como registrar um erro

```
### [data] — [categoria]
**O que foi feito:** descrição do erro
**O que o Rodrigo pediu:** o que corrigiu
**Regra:** frase curta + onde a regra vive (modelo X / voz / motor)
```

### 2026-08-11 — Gancho de dor "já explorada no mercado" perde pro tapa-polêmico (carrossel 31)
**O que foi feito:** capa-espelho da dor da vigilância ("O seu time só faz certo enquanto você está olhando.") seguindo o padrão reconhecimento + lacuna, com o tapa ("EMPRESA TEM QUE SER IGUAL UMA IGREJA.") no slide 2.
**O que o user pediu:** "não está ruim, bate em uma boa dor, mas não faz o empresário parar pois essa abordagem já foi muito explorada no mercado. Podemos começar direto no slide 2, ele serve muito bem como gancho." A capa foi cortada e o grito Anton virou o slide 1.
**Regra:** o teste da capa não é só "dói?" — é "ele JÁ viu essa dor mil vezes no feed?". Dor batida (time que só trabalha vigiado, ninguém quer trabalhar etc.) vira ruído; nesses casos um TAPA polêmico/contraintuitivo (a tese-choque em Anton) segura mais que o espelho. A dupla isca→tapa é opcional: quando a isca é clichê de mercado, abrir direto no tapa. Avaliar sempre: espelho inédito > tapa > espelho batido.

### 2026-08-11 — Frase batida do mercado é ruído até quando a peça ATACA a frase (carrossel 33)
**O que foi feito:** carrossel anti-guru (D3-S10) aberto citando o slogan que a peça derruba: capa com a promessa aspeada ("Sai do operacional.") e o tapa em seguida.
**O que o user pediu:** "a frase 'saia do operacional' já está muito batida e cansativa de ler no mercado, se torna uma premissa mais do mesmo. Podemos trazer esse conceito com outra vestimenta, que case com o pequeno e médio."
**O que corrigiu:** vestir o conceito com julgamento próprio, em bom português — "fugir da própria empresa" (a estranheza da frase já é o argumento) — e nunca repetir o slogan do guru em slide nenhum. A caricatura complementar ("dono de WhatsApp") ficou SÓ como contexto visual do slide da cena (texto fala direto; reforça a regra do carrossel 9: metáfora na imagem, não no texto).
**Regra:** citar o jargão batido do mercado deixa o adversário escolher o vocabulário da conversa — mesmo pra derrubar, a capa vira "mais do mesmo" (estende a regra 2026-08-11 do gancho batido: vale também pra frase-alvo de peça anti-discurso). A vestimenta certa não é sinônimo: é a tradução em bom português que JÁ carrega o julgamento (fugir da própria empresa, abandonar o que é seu). O slogan atacado pode no máximo aparecer aspeado uma vez no miolo como prova, nunca como capa/tese.

### 2026-08-11 — Fechamento "método se aprende" sem entregar nada: desenvolver o primeiro passo antes do treinamento (carrossel 33)
**O que foi feito:** slide de fechamento com "Parar de ser refém tem método. / E método se aprende." emendando direto no treinamento nomeado — a solução ficou só anunciada, nunca mostrada.
**O que o user pediu:** "precisamos desenvolver pelo menos um pouco qual nossa solução para o problema dele. Como vamos resolver isso, pode ser de maneira singela, um primeiro passo por exemplo."
**O que corrigiu:** slide próprio de PRIMEIRO PASSO antes do fechamento: "pega uma função que só você faz, escreve como se faz, treina alguém e acompanha todo santo dia" (o método da casa: descrição de função + treino + follow-up). O fechamento vem depois, amarrando no treinamento.
**Regra:** entre a virada e o fechamento-com-treinamento, dar ao leitor algo pra fazer amanhã de manhã — um primeiro passo singelo e concreto do método da casa. "Tem método e eu ensino" sem amostra soa promessa de palco (justo o que o editorial-punch costuma atacar). O primeiro passo é amostra grátis do método, não o método inteiro.

### 2026-08-11 — Contraste conceitual A×B dividido em 2 slides (manipulação × influência) (carrossel 31)
**O que o user pediu:** dividir o slide "manipulação × influência" em dois: (A) "Isso não é manipulação. / Manipulação é controle." (estrofe única, punch no controle); (B) "É influência. / E influência é livre-arbítrio: / a pessoa escolhe acreditar." (âncora curta + estrofe). "Pra ficar mais impactante visualmente."
**Regra:** contraste conceitual forte (X é isso ≠ Y é aquilo) rende mais como par A/B em slides separados — cada metade ganha a própria imagem (controle = marionete; escolha = porta aberta) e o swipe entrega o reveal. Reforça a regra dos pares A/B (2026-07-24): usar nos contrastes de melhor reveal. Âncora curta ("É influência.") pode abrir o slide B sozinha na própria estrofe.

### 2026-08-11 — Fechamento "é método" virou padrão repetido; o fecho nasce do TEMA e merece espaço (carrossel 32)
**O que foi feito:** slide de fechamento com a fórmula de sempre ("Encher esse caixa é método: dono que aprende tem o que ensinar" + treinamento nomeado), em 1 slide.
**O que o user pediu:** "a solução abordada é método, e isso tem sido a mesma abordagem para a maioria dos carrosséis... a abordagem do final deve ser coerente com o tema do carrossel." Neste (moeda do crescimento), o fecho certo é a **capacitação do dono**: questionar quando foi a última vez que ele investiu de verdade em si, no conhecimento dele. E diferenciar de curso de networking ("anota um monte de insight e não bota nada em prática, porque na teoria é uma coisa, na prática a história é outra"). E o desenvolvimento da solução "merece mais espaço do que 2 frases de uma estrofe".
**O que corrigiu:** fechamento expandido pra 3 slides — (12) investe em máquina/estoque/anúncio, e no conhecimento, quando? (13) não é curso de crachá/insight anotado; teoria × prática; (14) capacitação que muda a segunda-feira + treinamento nomeado. CTA segue em slide próprio (15).
**Regra:** a palavra "método" NÃO é o fechamento default. O fecho se constrói com o conceito que o PRÓPRIO carrossel desenvolveu (aqui: a moeda/capacitação; no 30: o ambiente; etc.) — se o slide de fechamento servisse em outro carrossel, está genérico (teste da substituição aplicado ao fecho). E a solução pode ocupar 2-3 slides de desenvolvimento antes do treinamento nomeado, não 1 estrofe protocolar. Complementa 2026-08-03 (nomear o treinamento continua obrigatório) e 2026-08-11 (CTA em slide próprio).

### 2026-08-11 — Fechamento "fraco": faltou desenvolver o DESEJO e a SOLUÇÃO antes do treinamento (carrossel 32)
**O que foi feito:** fechamento em 1 slide (espelho não muda sozinho + treinamento nomeado) direto após o grito doutrinário, e CTA. O user: "achei fraco. Não desenvolvemos o desejo para ele saber o que vamos mudar de fato e como vamos solucionar a dor que abordamos... elabore mais essa parte, mesmo que tenha que adicionar mais slides."
**O que corrigiu:** o fecho virou 4 slides: (1) **desejo** — a dor invertida como promessa ("esse espelho tem outro lado: reflete o seu melhor / time que cobra porque te vê cobrar"); (2) **o como** — o mecanismo concreto da solução ("exemplo com método: o comportamento certo, repetido todo dia, até virar automático"); (3) **treinamento nomeado**; (4) CTA exclusivo.
**Regra:** evolução de 2026-08-03 (CTA 2 slides) e 2026-08-11 (CTA slide próprio): antes do treinamento nomeado, o fechamento precisa de **um slide de desejo** (o outro lado da dor, o que a vida dele vira) e **um slide de como** (o mecanismo concreto que resolve, não "tem método" genérico). Sequência completa do fecho: desejo → como → treinamento → CTA. Adicionar slides pra isso não é problema; fechamento comprimido = fechamento fraco.

### 2026-08-11 — Dupla de continuidade visual no reveal: mesma cena, sujeito trocado (carrossel 32)
**O que o user pediu:** no beat do espelho, dividir em 2 slides com continuidade de imagem: slide A = a isca ("olha com atenção pra esse time...", o dono no mezanino olhando o time) e slide B = o tapa ("O FILHO É TEU." em Anton), com a imagem no MESMO cenário/enquadramento, mas o time trocado por um pai com o filho pequeno pisando nas pegadas dele. O swipe entrega o reveal pela imagem, não só pelo texto.
**Regra:** quando o reveal é uma releitura da mesma cena (o time visto como filho, o cliente visto como juiz), considerar a **dupla de continuidade**: slide A planta a cena real com a frase-isca em suspense (reticências, sem ênfase), slide B repete o cenário/enquadramento com o sujeito trocado pela metáfora + o grito Anton. As duas imagens se desenham juntas (mesmo universo, mesma luz, mesmo ângulo). Variante do padrão isca → tapa aplicada à IMAGEM.

### 2026-08-11 — Texto encostando no sujeito da foto: subir o bloco é a 1ª correção (carrossel 31)
**O que foi feito:** slides do sino (herói em top:280) e do púlpito (2+2 em top:236) com o bloco de texto quase tocando o topo do sujeito (arco de pedra / névoa dos bancos).
**O que o user pediu:** "suba o bloco textual, está pegando na imagem e atrapalhando a leitura."
**Regra:** quando o texto encosta no sujeito, primeiro SUBIR o bloco (até o piso de ~200px, nunca dentro da zona reservada) — e se ainda ficar apertado, cortar o topo da imagem (EXTRA_TOP) pra faixa problemática descer (púlpito: top:200 + EXTRA_TOP 250 + fade 28). Complementa 2026-07-24 ("quem cede é o bloco de texto") com a ordem: bloco primeiro, crop depois.

### 2026-08-14 — Capa: espelho bom perde pro tapa; imagem do grito pede o choque em CLOSE literal (carrossel 41)
**O que foi feito:** abertura em dupla isca → tapa (capa-espelho "treinou o time / segunda estava tudo igual" + grito "GESTOR É BABÁ DE ADULTO." no slide 2, com a babá conduzindo o empresário pela mão em plano aberto).
**O que o user pediu:** (1) "o slide 1 não tem o mesmo peso que o 2... começar pelo 2, ele é bem mais impactante" — a ordem inverteu: grito virou capa, espelho desceu pro slide 2; (2) na imagem do grito, trocar a cena ilustrativa (conduzir pela mão, plano aberto) por um CLOSE encenando a frase no literal-absurdo: homem adulto de terno com babador, alimentado na boca por mão feminina idosa com colher de criança, boca lambuzada; (3) subir o bloco Anton (estava "pegando na imagem" com espaço negativo demais em cima — foi de top:300 pra top:200).
**Regra:** (1) mesmo um espelho decente perde a capa pro tapa quando o grito é mais forte — reforça 2026-08-11 (espelho inédito > tapa > espelho batido): na dúvida, testar a ordem tapa-primeiro. (2) A imagem do slide-grito não ilustra o conceito, ENCENA a frase no literal mais absurdo possível, em close (babador + colher de criança > duas figuras andando). Quanto mais desconfortável o grito, mais literal e próxima a imagem. (3) Em imagem-close com sujeito grande, o bloco de texto sobe pro piso (~200px).

### 2026-08-14 — Anton fills-column desproporcional quando o parágrafo serif acima é curto (carrossel 41)
**O que foi feito:** slide da virada (2 linhas serif 44px + "FALTOU O QUE VEM DEPOIS." em Anton) com o Anton preenchendo a coluna (930 → 94px).
**O que o user pediu:** "o texto em anton está muito grande, muito desproporcional em relação ao parágrafo de cima" + subir o bloco todo (estava baixo, top:260). Corrigido pra alvo 640 (deu 64px, ~1.5x o corpo) e top:210.
**Regra:** refina a régua do autofit: Anton fills-column (930) só quando o slide é do grito (frase sozinha ou peso máximo). Em slide de virada com estrofe serif curta em cima, o alvo é intermediário (~640, dá ~60-70px a frases de ~24 chars) — maior que o corpo, menor que a coluna. O 'ref' puro (casar a serif) fica pequeno demais (53px ≈ corpo, não é grito); o meio-termo 640 é o ponto.

### 2026-08-18 — Desdobrar slide em dois sem redistribuir a ênfase (carrossel 45)
**O que foi feito:** na revisão do carrossel 45, os slides 2 e 6 foram desdobrados (o punch vermelho de cada um virou slide próprio: o herói "Na sua frente, tudo anda." e o grito "MAS NENHUM DOS DOIS FAZ O TIME QUERER."), e os slides de origem ficaram sem nenhum recurso de dinamismo — sem negrito, sem vermelho, texto chapado.
**O que o user pediu:** "falta aqueles elementos de dinamismo de texto como negrito, itálico, vermelho... isso está sendo um problema que não tínhamos". Corrigido: vermelho negrito no punch local de cada setup ("ela funciona.", "até um certo ponto...") e negrito preto de apoio ("todo mundo faz.", "obedecer"/"cumprir").
**Regra:** ao desdobrar um slide em dois, redistribuir a ênfase: cada metade ganha a própria hierarquia (vermelho negrito no punch local + negrito de apoio quando couber). O punch que saiu pro slide novo não era a única ênfase da dupla — o slide de origem elege um novo punch local. Slide de conteúdo sem nenhum recurso de dinamismo é erro; checar isso em toda reestruturação, não só nos slides novos.

### 2026-08-19 — Metáfora-alegoria reprovada; o filtro é o mapa 1:1, não a origem (carrossel 46)
**O que foi feito:** a semente D1-S11 (porta pra dentro × porta pra fora) foi vestida duas vezes de ALEGORIA — "jogo sem adversário/xadrez" (v1-v2) e "maestro/orquestra/público" (v3-v4, produzida por completo). O user reprovou a copy pronta ("bem ruim de copy"). O rework guiado por `conteudo/analise/analise-roupas.md` e `hipoteses.md` (H4) mostrou o defeito: alegoria com N correspondências gasta slides TRADUZINDO quem é quem ("o público é o seu mercado", "a orquestra é margem, custo, caixa") — perfil do gol-contra (0 com), não do babá-de-adulto (2.943).
**O que corrigiu:** v5 em roupa DIRETO com o batismo nativo da própria fala do Hélio ("da porta pra dentro"), capa "Você não está perdendo pro mercado. Está perdendo dentro de casa." — aprovada.
**Regra (calibrada com o user):** metáfora NOVA segue bem-vinda — babá, igreja e o cowboy do "dono não tira o olho" são invenções e são os tetos do perfil; não matar a criatividade. O filtro é o **mapa 1:1**: cada correspondência se entende de bate-pronto, sem slide de tradução? Precisou explicar quem é quem, troca de roupa (vira direto ou acha batismo melhor). Metáfora-campeã é **batismo** (renomeia a dor numa frase), não **alegoria** (mundo mapeado com manual). E antes de escolher a roupa, conferir se a semente já tem batismo nativo do Hélio — ele entra como **candidato** na mesa, nunca como obrigação. Checar também os vizinhos de tese nos dados (`desempenho.csv`) antes de re-vestir tese já publicada.

### 2026-08-19 — Vão morto de conteúdo passou batido; régua virou script obrigatório (check.py) (carrossel 46)
**O que foi feito:** slides entregues com o assunto da imagem só no terço de baixo e um deserto de névoa entre o texto e a cena (3 e 11), e composição com pedaço faltando (9: a parede divisória começava longe da câmera). O user pegou os três e perguntou por que a régua existente (2/3 de ocupação, disposição-padrão, vão morto) não segurou.
**Diagnóstico de processo (por que a régua falhou):** (1) conhecimento em prosa não é checklist — na hora do render a conferência era de memória; (2) regra "garantida pela receita" deixa de ser conferida — o crop quadrado garante a MOLDURA ocupada, não o CONTEÚDO dentro dela.
**O que corrigiu:** régua mecânica em `_scripts/check.py` + `check.js` (medem, por slide renderizado, onde o bloco de texto termina e onde o conteúdo da imagem começa). Corte calibrado no veredito do user: **vão morto > 380px reprova** (ele aceitou 346/362, reclamou de ~400+); **invasão < 30px** puxa olho humano. Roda depois de TODO render, antes de mostrar/entregar. Os scripts viajam no `_scripts/` copiado entre carrosséis.
**Regras adicionais que a saga do slide 9 reforçou:** (1) flag de invasão em composição de divisor de quadro não se descarta no atacado — o check acusou 10px e a dispensa "é by design" estava errada (o user reprovou em seguida); exceção só passa com folga visível confirmada no render. (2) Correção ESTRUTURAL de geometria (onde um elemento nasce no quadro) não se resolve com image-edit — o gpt-image-2 "conserta" de volta a cena normal (2 edits falharam); depois de 2-3 tentativas, REGERAR com a composição garantida por construção (fórmula do divisor pesado, desfocado, já cortado pela borda inferior — a mesma do ringue do post 40 e da cortina do teatro). (3) Conteúdo que subiu demais depois disso = EXTRA_TOP no pós (a imagem desce; a âncora inferior preserva o nascimento na borda).

### 2026-08-21 — Capa com top:330 herdado do template do carrossel anterior (todas as capas do dia baixas demais) (carrossel 50)
**O que foi feito:** o `_scripts/build.py` é copiado de carrossel em carrossel como template, e a capa veio com `top:330px` fixo (herdado do 49, que herdou da regra de 2026-07-16). Nas capas do dia (sujeito baixo no quadro: navio no rodapé, muita névoa), o texto despencou pro meio do slide — o erro se repetiu em TODOS os carrosséis do dia, de todas as sessões.
**O que o user pediu:** "slide 1 o bloco textual está muito baixo, pode subir bem ele... isso se repetiu em todos os slides capa dos carrosséis de hoje... resolva." Corrigido pra `top:210`.
**Regra:** o `330` da capa NUNCA foi um default — foi calibrado (2026-07-16) pra capa com **sujeito alto** ocupando ~2/3 do slide, onde o texto desce até encostar na imagem. A posição da capa se decide **olhando o render**, por carrossel: sujeito alto → desce até encostar (~330); sujeito baixo → texto no piso (~200-210, abaixo da zona reservada). Valor de `top` da capa no `build.py` copiado do carrossel anterior não é herdável — conferir no primeiro render, sempre. (Reforça 2026-07-23: "a posição do texto da capa acompanha a altura do sujeito na foto".)
> **[Valores de altura superados]** Os números de `top` desta entrada são da época. A calibragem vigente está no CSS do modelo (corpo 240, capa 280, de 11/09). A lição continua: o layout sai do modelo, nunca do build.py anterior.

**Reincidência 2026-09-04 (carrossel 89), com autorização do user pra registrar:** o erro voltou por outra porta — o `_scripts/build.py` do 83 foi copiado inteiro como template e trouxe `top` de 236 a 400 em TODOS os slides de corpo (não só na capa). O user: *"você não pode ser influenciado pelo que não está na skill. Faça com a altura já estabelecida na skill."* Regra operacional: ao copiar `_scripts/` de outro carrossel, **zerar todo `top=` pro padrão do modelo (`top:160` no corpo; capa ~200 com sujeito baixo) antes do primeiro render.** Consequência que veio junto: com o texto em 160, cena gerada em `base_wide` (sujeito na metade de baixo) deixa 400–570px de vão que o teto de recorte de 18% não fecha — **a saída é gerar a cena mais fechada** (`base` + cláusula de cinema "people LARGE and CLOSE, chest up, heads at one fifth from the top"), não esticar o recorte. No 89 isso resolveu 6 slides de uma vez.

### 2026-08-21 — Teto de parágrafos por slide: máx 2; o 3º só quando é bem curto (carrossel 50)
**O que foi feito:** vários slides do carrossel 50 (e de outros do mesmo dia) saíram com 3 parágrafos de texto (2+2+2), seguindo a regra de 2026-07-28 que diz "pode ter 1, 2 ou 3 parágrafos por slide". O user apontou o padrão: "tem 3 parágrafos de texto... notei que nos carrosséis de hoje tem esse erro mais frequente".
**O que o user pediu:** desdobrar — o punch vermelho de um slide de 3 parágrafos vira slide próprio (grito/herói com a própria imagem), e o slide de origem fica com 2 parágrafos. Exceção aceita: 3 parágrafos quando o TERCEIRO é bem curto (ex.: âncora de 1 linha "O seu exame é o faturamento." — "excessão boa da regra"). No fim de carrossel já longo ele pode tolerar 3 parágrafos pontualmente pra não esticar mais (foi outlier declarado, não precedente).
**Regra:** teto de texto do slide editorial-punch = **2 parágrafos**. Um 3º parágrafo só entra se for **1 linha curta** (âncora/punch). Slide que pedir mais que isso = desdobrar: o punch vira slide próprio (padrão do desdobramento de 2026-08-18, redistribuindo a ênfase). Isto REFINA a regra de 2026-07-28 ("1, 2 ou 3 parágrafos"): o "3 parágrafos de 2 linhas" deixou de ser aceitável como padrão.

### 2026-08-27 — Palavra-chave do CTA batizava o PROBLEMA, não o estado desejado (carrossel 60)
**O que foi feito:** a palavra-chave do carrossel da solidão da presidência saiu como **CADEIRA**, derivada do batismo da dor (a cadeira que só um senta, sem revezamento) — no mesmo molde de todas as anteriores: LADRAO, PATRAO, DRAGA, ESCONDIDA, PILOTO. Todas nomeiam a dor.
**O que o user pediu:** "a palavra cadeira não transmite o que ele quer SENTIR em relação ao problema dele. Ele quer se sentir como? Leve?" A palavra virou **LEVE**. Descartada COMUNIDADE, que nomeia o nosso produto e não o estado dele (e era a mesma palavra usada pelo vídeo-fonte).
**Por que importa:** a palavra que o dono digita no comentário é a última coisa que ele faz na peça, e ela devia ser o nome do que ele quer virar, não o nome do que ele é hoje. Comentar o batismo da própria dor é repetir o diagnóstico; comentar o estado desejado é dar o primeiro passo.
**Regra:** a **palavra-chave do CTA nomeia o ESTADO DESEJADO** (LEVE), não o batismo do problema (CADEIRA) nem o nome do nosso produto (COMUNIDADE). O batismo continua governando o TEXTO — ele é a espinha dos slides; só não é mais o candidato automático a palavra-chave. Critérios que permanecem: única no perfil (conferir `conteudo/analise/registro-posts.csv`), caixa alta, sem acento, curta de digitar.
**Contrapartida obrigatória:** palavra de estado desejado cria promessa, então a peça tem que **ganhar** esse estado antes do CTA. Aqui o slide de desejo dizia "a solidão não vai acabar" e prometer leveza depois disso soaria falso — foi reescrito pra a leveza ser consequência e ficar amarrada a desempenho ("Mas você deixa de ser o único que enxerga. / E dono leve decide melhor."), fechando o arco que o slide 2 abriu ("todo mundo rindo, todo mundo leve"). Antes de fechar uma palavra de estado, conferir se algum slide contradiz o estado que ela promete. Ver o modelo → "Fechamento".

### 2026-08-27 — Fonte de terceiro: o default do regime aponta pro lado errado, e a altura do interlocutor escorrega junto (carrossel 58)
**O que foi feito:** o 58 (o cliente virou patrão) foi o primeiro carrossel com semente **externa** — transcrição de reels de terceiro sobre "o cliente tem sempre razão". A cadeia causal da fonte atravessou o processo intacta (slides 7, 8, 9, 12 e 13 iguais do rascunho ao publicado) e a skill recusou sozinha abrir com o slogan da fonte. Mas o mesmo material custou três rodadas de reprovação do user e uma recalibração de nervo às 22:43, com o post já publicado.
**Os três furos, todos herdados da fonte:**
1. **Regime ambíguo.** A regra de 2026-07-30 manda seguir a espinha de "referência estruturada"; a de 2026-08-05 manda tratar roteiro como insumo de tema. Transcrição de reel *parece* estruturada — tem beats e ordem — então o default de 07/30 dispara sozinho e entrega exatamente o que foi reprovado em 05/08 ("uma versão carrossel do roteiro"). O desempate não é inferível do material: sai do que o user diz ao mandar.
2. **Altura do interlocutor.** Os slides 2-3 saíram falando na altura do prestador/vendedor. Segunda ocorrência do MESMO defeito com fonte externa (a 1ª foi o carrossel 13, 28/07: *"parece mais voltado a funcionário, a vendedor do que dono de empresa"*). Reel que performa neste nicho costuma mirar vendedor e prestador — audiência muito maior que dono de PME. Seguir a espinha herda a altura de quem falava.
3. **Sem causa técnica.** A fonte tinha sintoma e postura, nenhum número. O eixo do caixa (custo/margem) foi trazido pelo user às 19:53 e virou os slides 2, 3, 10, 15, o CTA e a DM do Manychat. Sem ele o post fechava sem gancho de venda.
**Regra:** com material pronto de terceiro, antes de escrever: **(1)** perguntar o regime em uma linha — `tema` ou `espinha` (e, se for lista de N itens, 1 peça ou N). Nunca assumir `espinha` só porque a transcrição tem beats. **(2)** Declarar no topo do `carousel-text.md`, decidindo sozinho: o **interlocutor** (nenhum slide fala com quem executa; o dono é sempre o interlocutor — é checagem de contaminação, não escolha) e a **causa técnica** que amarra o CTA. Ver `SKILL.md` → Passo 2, itens 2b e 2c.
**Calibração honesta (registrada de propósito):** isto é **n=1** de fonte de terceiro confirmada. As outras 17 pastas com marca de "transcrição" são transcrição do próprio Hélio (material interno do MBV) — inclusive o recordista 41_babá. O prejuízo medido do 58 foi de **processo** (tempo do user), não de performance: não existe evidência ligando regime, altura ou causa técnica a taxa pior. Estes passos se justificam por custarem quase nada, não por padrão medido. **Plano de morte:** se em 8 carrosséis o user não vetar nenhum campo declarado, os passos 2b/2c saem da skill por falta de trabalho.

### 2026-08-27 — Marca no texto: quem fala é o Hélio, não a escola (2ª ocorrência em 2 dias)
**O que foi feito:** o fechamento dos carrosséis 61 e 62 nomeou o produto como **"Tatsuo Academy"** ("Foi pra isso que eu criei a Tatsuo Academy").
**O que o user pediu:** no 61 — *"que história é essa de falar de Tatsuo Academy? aqui é só Hélio."* No 62, ao ver o erro repetido — *"por que isso está acontecendo??? nunca aconteceu."*
**Levantamento (63 carrosséis do acervo):** "Tatsuo Academy" aparece no texto de slide em **3 pastas apenas — 60, 61 e 62**, todas de 26-27/08. Nas outras 60, o produto sempre foi **"o meu treinamento de gestão pra pequena e média empresa"**; "MBV" só aparecia nos cabeçalhos de fonte, nunca nos slides.
**Origem da contaminação:** o carrossel **60** teve CTA de comunidade e o user autorizou ali, naquele post, puxar pro "ecossistema da Tatsuo Academy". Foi uma autorização **pontual** e virou padrão nos posts seguintes — erro de tratar aprovação de contexto como regra nova.
**Regra:** o produto nos slides e na legenda é nomeado em **1ª pessoa** — "o meu treinamento de gestão pra pequena e média empresa" ou **"o MBV"** ("eu criei o MBV pra ensinar isso"). **"Tatsuo Academy" não entra no texto.** A frase institucional do fecho ("Seja Bem-Vindo ao Fim do Analfabetismo Empresarial") é do próprio Hélio e fica; a hashtag `#TatsuoAcademy` é tag de descoberta e continua.
**Regra de processo (o que realmente falhou):** a correção do 61 foi registrada **só no `carousel-text.md` daquele post** — arquivo que nenhuma sessão futura lê. Correção do user só protege o próximo carrossel quando entra **aqui**. Registrar na pasta do post não conta.

### 2026-08-27 — Número da experiência do Hélio (fato, não estimativa)
**O que foi feito:** legenda do 62 abriu com "eu escuto essas frases há trinta anos" — número inventado pra soar como fala.
**Fato dado pelo user:** o Hélio **empreende há mais de 38 anos**.
**Regra:** quando a legenda invocar o tempo de estrada dele, usar esse fato (38+ anos / quase quarenta anos), nunca um número redondo de enfeite. Reforça a voz: afirmação factual precisa de especificidade, e chute em cima da biografia dele é o pior lugar pra chutar.

### 2026-08-27 — Aspas na borda da linha entram na centralização e entortam o bloco (carrossel 62)
**O que foi feito:** slides com a frase do dono entre aspas em Anton (`&ldquo;NINGUÉM QUER / TRABALHAR.&rdquo;`) saíram com a aspa dentro do fluxo do texto.
**O que o user apontou:** *"a linha de início do parágrafo fica destoante, a de cima começa na aspas onde deveria começar na letra"*. Como o bloco é centralizado, a largura da aspa entra na conta e empurra as letras da 1ª linha pra dentro — a 1ª linha alinha pela aspa e a 2ª pela letra.
**Sugestão do próprio user, que é a técnica correta:** diagramar o texto **sem** as aspas e só depois pendurá-las.
**Regra (aspas penduradas):** aspa em borda de linha recebe margem negativa igual à **largura de avanço do glifo**, medida — não chutada. No Anton deu **0.466em** (script `_scripts/quotewidth.js` do carrossel 62 mede em qualquer fonte). CSS:
```css
.oq{ margin-left:-0.466em; }   /* aspa de abertura */
.cq{ margin-right:-0.466em; }  /* aspa de fechamento */
```
A aspa passa a ocupar largura ZERO na diagramação: o texto centraliza como se ela não existisse e o glifo pende pra fora do bloco. Vale pra Anton e pra serif. **Aspa no meio da linha não precisa** (ex: `chama de "faro"`) — o problema só existe na borda.

### 2026-08-28 — Capa com três linhas; capa é de DUAS linhas (carrossel 72)
**O que foi feito:** capa entregue com setup serif + grito Anton + linha de sussurro ("querer é que cobra caro"), no molde herdado do 68 e do que o próprio `modelo.md` descrevia ("Capa maior + subtítulo itálico").
**O que o user pediu:** *"slide capa deve ter só 2 linhas. Isso é regra."*
**Regra:** capa do editorial-punch tem **2 linhas**: o setup e o grito. Sem sussurro, sem subtítulo, sem terceira linha. A linha boa que sobra não se acomoda embaixo — ou ela entra no slide 2, ou morre. Corrigido também em `modelos/editorial-punch/modelo.md` → "Estrutura por slide", que era a fonte da contaminação.

### 2026-08-28 — Grito que descreve a categoria em vez de nomear o destino (carrossel 72)
**O que foi feito:** o grito do slide 4 saiu **"FORA DO NORMAL EXIGE / ESFORÇO FORA DO NORMAL."** E a capa saiu **"E GOSTAR É DE GRAÇA."**
**O que o user reescreveu:** **"UMA VIDA FORA DO NORMAL EXIGE / ESFORÇO FORA DO NORMAL."** E na capa, **"DESEJAR É DE GRAÇA."**
**Regra:** duas correções da mesma família. (1) Sem "UMA VIDA", "fora do normal" é categoria abstrata e o grito vira lei de física sobre coisas; com "UMA VIDA", o grito nomeia o destino que ele quer e cobra o preço na mesma frase. **Grito nomeia o que ele quer VIRAR, não a classe de coisas de que se fala** (parente da regra da palavra-chave de 2026-08-27). (2) O "E" de ligação enfraquece o grito: sem ele a frase fica de pé sozinha. E "desejar" é mais frio que "gostar", que soa afetivo — em peça de confronto, escolher o verbo sem afeto.
**Escopo:** o resto da direção deste post (registro motivacional, verdade ácida, teto de 12 slides) foi instrução **para esta peça**, não regra nova. Não generalizar — é exatamente o erro registrado em 2026-08-27 (aprovação de contexto virando padrão).

### 2026-08-28 — FABULA: díptico de DUAS gravuras é exceção válida ao "split não usar" (carrossel 69)
**Contexto:** a regra de 2026-08-06 (FABULA v2, item 3) diz **"split de duas metades: não usar"** — ela nasceu de uma imagem única em landscape que o motor entregou partida ao meio, e que o user leu como *"imagem cortada no meio sem motivo"*.
**O que o user pediu agora:** no beat A×B do carrossel 69 ("Nenhum dos dois estava errado. Mas os dois estavam sofrendo."), ele pediu explicitamente *"tela dividida no meio (vertical) com a cara do homem fazendo força e a cara do cavalo fazendo força resistindo, mostrando o esforço dos dois"*. Aprovado depois de pronto.
**O que distingue os dois casos (é isso que vale a pena guardar):** o defeito de 08-06 era **uma** gravura cortada; o acerto aqui são **duas** gravuras retrato independentes, cada uma uma composição completa e fechada, montadas lado a lado no HTML com calha entre elas. O corte deixa de ser acidente do enquadramento e vira moldura dupla de livro ilustrado.
**Regra:** na FABULA, contraste A×B pode ser **díptico** quando (a) o beat é o mesmo instante vivido pelos dois lados, (b) cada painel é gerado como imagem SEPARADA em retrato (`size 1024x1536`, base portrait), e (c) a montagem é em HTML (`.ilustra-box.duo`, flex + `gap:16px`), nunca uma imagem só dividida pelo motor. Se for imagem única, a proibição de 2026-08-06 continua valendo.
**Execução (três coisas que custaram rodada):**
1. **Direção do olhar tem que ser cravada no prompt de cada painel** — "face turned to face the RIGHT edge" no da esquerda e "LEFT edge" no da direita. Sem isso os dois saem de frente e o díptico não conversa.
2. **Emoção: determinação, não agonia.** A 1ª versão saiu com os dois de frente e com cara de dor; o user pediu *"cara de determinados e firmes"* pingando suor. Em beat de esforço mútuo, o que emociona é a firmeza dos dois, não a careta.
3. **`object-position` por painel é obrigatório.** O painel tem ~1:2 e a gravura vem 2:3, então o cover come ~12% de cada lado e decepa focinho/nariz — que é justamente onde mora a expressão. Medir onde está o sujeito e ajustar painel a painel (no 69 ficou 60% no homem e 20% no cavalo).
**CSS canônico:**
```css
.ilustra-box.duo{ display:flex; gap:16px; }
.ilustra-box.duo img{ width:calc(50% - 8px); }
.ilustra-box.duo img:nth-child(1){ object-position:60% center; }  /* ajustar por gravura */
.ilustra-box.duo img:nth-child(2){ object-position:20% center; }
```
**Escopo:** exceção do díptico, não liberação geral de split. A regra de 2026-08-06 segue de pé para imagem única.

### 2026-08-29 — Capa de 3 linhas com sussurro virou padrão sozinha; a capa é de 2 LINHAS (carrossel 68)
**O que foi feito:** a capa do 68 saiu com o formato impacto + punch + sussurro ("Você trata todo mundo bem. / E NINGUÉM TE LEVA A SÉRIO. / e você jura que isso é ingratidão.").
**O que o user disse:** *"todos as capas dos carrosséis estão vindo com estrutura de 3 linhas e uma delas é sussurro... de onde tirou esse padrão? São duas linhas APENAS. POUCAS PALAVRAS ESCOLHIDAS MINUCIOSAMENTE PARA CAPTURAR A ATENÇÃO DO PROSPECT."*
**De onde veio (levantamento):** o sussurro está na capa de 8 carrosséis do acervo — 33, 41_sofre-uma-venda, 45_anda-dez-volta-oito, 46_nunca-e-dinheiro, 50_draga, 50_nem-sonho-tem, 51_empresa-escondida, 58, 61 — inclusive dois marcados como "texto final do user". Ou seja: a terceira linha entrou como imitação do acervo, sem nunca ter sido pedida como regra.
**Regra:** **capa = 2 linhas.** Setup + punch, ou grito Anton de 2 linhas. Sem terceira linha de sussurro. A capa é o slide que faz o prospect parar, e cada palavra a mais dilui. Sussurro segue permitido em slide de conteúdo, nunca na capa.
**Regra de processo:** padrão recorrente no acervo NÃO é regra da casa. Antes de repetir uma estrutura só porque ela aparece em vários carrosséis, conferir se ela está escrita no modelo ou aqui. Repetição de acervo se propaga sozinha entre sessões e vira "padrão" sem ninguém ter aprovado.

### 2026-08-29 — O motor do post que viraliza é ENDOSSO: fala PELO leitor, não SOBRE ele (carrossel 68)
**O que foi feito:** o 68 foi escrito três vezes como diagnóstico do leitor ("você amolece", "você mendiga simpatia", "você chama de ingratidão"), no arco padrão dor → virada → pedrada. O user reprovou as três e mandou o carrossel externo **"ser dono é ser chato"** (post_id `18090467402466147`, 05/03/2026, no `corpus-carrosseis.json`) como calibragem, pedindo a análise do porquê aquele post foi muito acima da média.
**O dado (contra a mediana dos 464 carrosséis com alcance na base):** alcance 491.548 contra 6.116 (80x) · **shares/1k = 35,6 contra 10,9 (3,3x)** · saves/1k 15,6 contra 9,5 (1,6x) · likes/1k 63,0 contra 36,5 (1,7x) · **comentários/1k 1,89 contra 1,71 (1,1x, ou seja, na mediana)**.
**Diagnóstico:** o motor foi ENDOSSO, não discussão. Compartilhamento 3,3x acima com comentário na mediana é a assinatura do post que o leitor usa como **porta-voz** — ele manda pro sócio, pro gerente, pro grupo de empresário, porque o texto diz por ele o que ele não consegue dizer sem parecer tirano. **Ninguém compartilha uma acusação contra si mesmo.**
**As seis diferenças estruturais:**
1. **Cargo, não diagnóstico.** A referência DESCREVE a função ("Ser dono é cobrar resultado. É perguntar de novo. É pedir número."), e o leitor pensa "é exatamente o que eu faço".
2. **Slide citável isolado.** Qualquer slide funciona sozinho num print. Arco encadeado (o slide 7 não existe sem o 5) não sobrevive ao print, e print é o que viaja.
3. **Inimigo externo** (quem manda o dono ser leve), não o leitor.
4. **Responsabilidade tarde e como doutrina.** Lá ela entra no slide 9, depois de 8 slides de validação, na forma "cultura é reflexo do dono". Acusar no slide 2 mata o compartilhamento.
5. **Anáfora é o motor do ritmo**, não a metáfora ("É... É... É...", "Se você tolera X, vai ter X"). Linha curta, 3 a 6 palavras.
6. **CTA de pertencimento** ("se você aguenta essa responsabilidade"), não de tarefa.
**Regra:** em tema de postura do dono, escrever o carrossel como **manifesto de cargo**, não como diagnóstico do leitor. A responsabilidade não sai da peça (regra 6 da legenda continua valendo), ela muda de lugar: entra depois da validação e vestida de doutrina. Uma cutucada pessoal por peça é o teto.
**Ressalva honesta:** o comentário por alcance ficou na MEDIANA. Esta forma entrega alcance e compartilhamento, não taxa de comentário, e a máquina de leads roda em comentário com palavra-chave — o CTA nomeando o treinamento continua sendo trabalho nosso (a referência não fazia isso). É **n=1** nessa forma, e o perfil tem outlier de 300k a 800k quase todo mês. Testar antes de tratar como lei.

### 2026-08-28 — FABULA: gravura de plano largo (zenital/aéreo) não cabe na caixa quase quadrada (carrossel 69)
**O que foi feito:** o slide 9 (zenital, homem na água de um lado e cavalo no seco do outro) foi montado na caixa padrão da FABULA. O homem sumiu: sobrou um borrão de chapéu encostado na borda esquerda.
**Diagnóstico:** não era a gravura, era o enquadramento. A `.ilustra-box` tem 915px de largura e altura variável pelo texto; num slide de 2 estrofes ela fica com ~927px de altura, ou seja **quase quadrada**. Uma gravura landscape 1536×1024 em `object-fit:cover` perde cerca de **um terço da largura**, ~17% de cada lado. Em cena com um sujeito só isso não aparece; em cena de dois sujeitos AFASTADOS, decepa quem está nas pontas.
**Por que `object-position` não resolve:** a conta é `largura visível da gravura = altura_da_fonte × (largura_da_caixa ÷ altura_da_caixa)`. No 9 isso dava 1011px de fonte visível para dois personagens que ocupavam ~1050px. Não existe deslocamento que caiba os dois — mover pra um lado só troca qual dos dois é cortado.
**O que corrigiu:** **abaixar a caixa** (classe `.wide`, `max-height:830px`) e devolver o vão pra cima com `margin-top:auto`, mantendo a gravura ancorada embaixo como em todos os outros slides. A caixa passa a 915×830 e a largura visível da fonte sobe pra ~1129px: os dois cabem inteiros, e a placa ganha proporção de vista aérea, que é o natural desse plano.
**Regra:** plano intrinsecamente largo (zenital, aéreo, panorâmica de dois sujeitos afastados) pede caixa `.wide` na FABULA. **Ordem de defesa:** (1º) cláusula de composição no prompt travando os figurantes no miolo — resolve a maioria e não custa layout (regra 2026-08-06, usada nos slides 11 e 17 deste mesmo post); (2º) `object-position` quando o sujeito está deslocado mas cabe; (3º) `.wide` quando a cena é mais larga do que a caixa consegue mostrar. Conferir com o script `_scripts/check.js`, que mede texto × gravura slide a slide.
**CSS canônico:**
```css
.ilustra-box.wide{ max-height:830px; margin-top:auto; }
.ilustra-box.wide img{ object-position:40% center; }  /* ajustar pela gravura */
```
**Escopo:** vale para o slide cuja gravura é larga, não para o carrossel inteiro — a caixa padrão continua sendo a regra, e fábula segue sendo imagem dominante (a `.wide` ainda deixou 61% da página para a gravura).

### 2026-08-31 — Linguagem: abstração só no GRITO; o corpo do slide pede carne (carrossel 75)
**O que foi feito:** o carrossel da lealdade foi escrito duas vezes em linguagem de argumento — "Contrato compra hora, tarefa e presença", "A dívida está no seu nome. A garantia é a sua casa", "Precisa ser o lugar onde ele conquista o sonho dele". Correto, direto, e sem nada que se possa ver.
**O que o user disse:** primeiro *"podemos ser mais diretos, direto e reto como o hélio é, sempre com tapa (verdade) na cara"*; depois, quando a 2ª versão continuou seca, *"ser direto não é ser ruim, recomece. Muito da minha crítica é que a linguagem não é a linguagem do hélio, houve alguma mudança na linguagem da skill desde que iniciamos o projeto?"*
**Levantamento (a resposta honesta é não):** `voz-tatsuo.md` foi tocado 2 vezes desde o commit inicial (teto de 1.400 caracteres em 27/08 e nada mais que voz); `preferencias.md` nunca mudou; `editorial-punch/modelo.md` mudou só na palavra-chave do CTA e no "capa = 2 linhas". A skill não desviou — o texto desviou.
**O que separa as duas linguagens (comparação lado a lado do acervo):**
- Acervo: "GESTÃO É CHATA PRA CACETE" · "no peito e na raça" · "empurrando com a barriga" (1) · "a fatura entra gorda", "no bolso do dono cai só respingo" (2) · "briga em casa, ansiedade, dinheiro curto" (20) · "dieta, academia, curso, planilha nova. A sua vida é um cemitério de começos" (72, um dia antes).
- Reprovado: enunciados verdadeiros e sem objeto, sem hora, sem número, sem cena.
**Regra:** no editorial-punch, **a abstração mora no grito Anton; o corpo do slide se escreve com coisa que dá pra ver** — hora no relógio ("chega às sete, sai depois das nove"), tempo de casa ("quatro anos na mesma função"), valor em real ("300 reais a mais"), o objeto em cima da mesa (marmita, chaves, capacete), a frase que o dono fala em casa. Teste antes de entregar: em cada slide de corpo, aponte o substantivo concreto. Se o slide inteiro é feito de substantivo abstrato (contrato, expectativa, dedicação, lugar, sonho), reescrever com o objeto que encarna aquilo.
**Onde vive:** `referencias/voz-tatsuo.md` (voz) — esta entrada é o detalhamento operacional para os SLIDES.

### 2026-08-31 — Motor: "no text, no words" no estilo-base NÃO segura texto quando a cena pede documento ou dinheiro (carrossel 75)
**O que foi feito:** o estilo-base do editorial-punch termina com `No text, no words, no letters, no numbers, no logos`. Mesmo assim, no carrossel 75 o gpt-image-2 entregou: (a) um **contrato de trabalho inteiro em inglês e perfeitamente legível** — "EMPLOYMENT CONTRACT", "Acme Manufacturing Company", "Chicago plant", "$6,500.00 per annum"; (b) **cédulas com cara de dólar americano** no envelope de pagamento; (c) uma **nota de um dólar** no lugar de um boleto, porque a cena foi pedida em inglês como "a paper bill" e "bill" virou cédula.
**Diagnóstico:** a proibição no fim do prompt perde para o conteúdo da cena. Se a cena nomeia um objeto cuja natureza é ser escrito (contrato, boleto, holerite, calendário, cédula), o modelo escreve. Casa com o aprendizado do carrossel 73 (o motor escreve AGOSTO/SETEMBRO com precisão, mas erra a lógica do calendário): quando o objeto pede texto, o texto vem.
**Regra (duas partes):**
1. **Ilegibilidade se pede como CONSTRUÇÃO da foto, não como proibição.** Profundidade de campo rasa com o texto explicitamente borrado ("ALL the typed text is completely BLURRED and ILLEGIBLE, reduced to soft grey smudged lines"), ângulo rasante, cédula vista de perfil, folha cortada pela borda. Funcionou de primeira nos três casos. O chalkboard do slide 15 saiu em rabisco ilegível sozinho porque a cena pedia "handwritten routine", não palavras.
2. **Nomear o objeto pelo que ele é, nunca pela tradução.** "bill" = cédula em inglês; boleto brasileiro não tem equivalente e não deve ser tentado. Quando o objeto é cultural e não traduz, **trocar de objeto**: no slide 7 o boleto virou capacete de moto, que é o que o próprio texto do slide listava ("o aluguel, a escola do filho, a moto").
**Régua de conferência:** todo slide cujo assunto seja papel, tela, placa, quadro ou dinheiro entra na lista de risco de texto e se confere no render, um a um. Dinheiro em cena brasileira nunca pode ler como dólar.

### 2026-09-01 — Linguagem do Hélio: 2ª ocorrência em 2 dias, e a régua medida de tamanho de slide (carrossel 77)
**O que foi feito:** a v1 do 77 saiu em linguagem de argumento de novo, e o user repetiu quase palavra por palavra a crítica do carrossel 75 (31/08): *"senti muita diferença do que o hélio falaria de fato... podemos ser mais diretos, direto e reto como o hélio é, sempre com tapa (verdade) na cara. E ser direto não é ser ruim."* Junto, duas perguntas factuais: *"houve alguma mudança na linguagem da skill desde que iniciamos o projeto?"* e *"notou que de umas semanas para cá os textos por slide aumentaram muito de tamanho?"*
**Resposta 1, medida no git (a skill NÃO mudou):** em `voz-tatsuo.md` as seções Tom, Como a frase soa, Proibido e Testes estão **idênticas desde o commit inicial de 14/07**; o arquivo só foi tocado uma vez, em 27/08, e só no teto de 1.400 caracteres da legenda. O `editorial-punch/modelo.md` mudou duas vezes: palavra-chave do CTA (19/08) e "capa = 2 linhas" (31/08). O `preferencias.md` nunca mudou. Nenhuma edição tocou a linguagem dos slides.
**Resposta 2, medida no acervo (o user está certo):** mediana de caracteres por slide em 75 carrosséis com `carousel-text.md` parseável:

| Carrosséis | Mediana chars/slide |
|---|---|
| 1-15 | 112 |
| 16-30 | 117 |
| 31-45 | 105 |
| 46-58 | 114 |
| **59-70** | **140** |
| **71-77** | **180** |

Estável em ~110 por 58 posts, depois sobe. O 73 deu 214 e o 75 deu 225, o dobro da régua histórica. **Inchaço e "não é o Hélio" são o mesmo defeito:** frase longa vira enunciado argumentativo, e enunciado argumentativo não é a voz dele.
> **[TETO SUPERADO em 13/10/2026]** O teto de 130 fazia o Claude cortar artigo e conectivo pra caber, e o texto saía telegráfico (201, 207). Vale agora: corpo de ~110 a ~180 caracteres; estourou, corta-se uma ideia inteira ou divide-se o slide, nunca a palavra de ligação. Ver `voz-tatsuo.md` → "Frase falada inteira".

**Regra (texto original de 01/09; régua numérica, some com a subjetividade):** antes de entregar, medir a mediana de caracteres por slide. **Alvo do corpo: ~110, teto 130.** Acima de 150 o texto virou argumento e se reescreve. Slides de anáfora/grito ficam de fora da conta (30-50 é o normal deles) — medir o corpo separado da abertura.
**Contra-regra, aprendida na mesma sessão:** cortar demais também reprova. A v2 do 77 desceu pra mediana 44 e o user reagiu *"agora achei pouco texto por slide... tente achar um equilíbrio entre os 2"*. Direto não é seco: a v3 fechou com anáfora em 23-40 e corpo em ~104, e foi aprovada. **Curto é o grito; o corpo tem carne** (reforça a entrada de 31/08).

### 2026-09-01 — Slide de texto curto gera vão morto por construção; a fórmula do imgheight (carrossel 77)
**O que foi feito:** no 1º render do 77, seis slides reprovaram no `check.py` (1 a 5 e 10), com até **534px de deserto**. Todos eram slides de texto curto: com 1-2 linhas o bloco termina em y≈320 e a foto, ancorada embaixo na altura natural, só começa em y≈850.
**Diagnóstico:** não é erro de arte, é geometria. Com `width:100%` a imagem 1536×1024 fica com 720px de altura e nasce em y=630; o assunto dentro dela costuma começar mais abaixo ainda. Quanto mais curto o texto, maior o vão — ou seja, **o vão morto é consequência automática do slide curto**, e vai reaparecer em toda peça com abertura em anáfora.
**O que corrigiu:** subir a imagem por `imgheight.json`, calculando a altura em vez de chutar. Com a imagem ancorada embaixo e `object-fit:cover`:

```
(1 − f) = (1350 − assunto_medido) / 720        # medir uma vez, na altura natural
H       = (1350 − (texto_bottom + gap_alvo)) / (1 − f)
```

`f` é a fração da foto acima do assunto; `gap_alvo` = 320 (o teto do check é 380). No 77 isso resolveu os seis de uma vez, na primeira tentativa.
**Custo a conferir:** subir a altura recorta a largura (`perde = 1 − 720/H`). No 77 foi de 13% a 30%. Textura repetida (chapa, concreto) aguenta 30% sem aparecer; **cena com sujeitos afastados nas pontas, não** — conferir no render, é o mesmo risco da entrada de 28/08 sobre a caixa `.wide` da FABULA.
**Regra:** slide de 1-2 linhas já entra com `imgheight` calculado, não com a altura natural. Rodar `measure.js` → `check.py` → aplicar a fórmula → re-renderizar. Nunca ajustar por tentativa e erro.

### 2026-09-01 — `base_wide`: a moldura recuada que matou cara de colagem, linha dura e corte no meio do corpo de uma vez (carrossel 77)
**O que foi feito:** o user reprovou quatro imagens do 77 com queixas que pareciam separadas: *"a imagem tão confusa que pensei que era uma madeira molhada e mofada"* (1), *"parece montagem, cadê a direção de cinema?"* (5), *"a imagem ficou muito para baixo e tem uma linha claramente que divide ela do fundo"* (6), *"parece colagem, cortou o homem no meio"* (13).
**Diagnóstico (é uma causa só, não quatro):** o estilo-base do editorial-punch manda `the camera is CLOSE and the subject is VERY LARGE, filling the bottom three quarters`. Isso produz três efeitos colaterais: (a) close demais tira o contexto e o assunto fica ilegível (a chapa virou madeira mofada); (b) sem instrução de exposição única, o motor compõe elementos com luzes e nitidezes diferentes e o resultado lê como colagem; (c) cena de topo escuro (noite, interior) encontra o fade e cria emenda reta contra o linho.
**O que corrigiu — um segundo base, `base_wide`,** com três cláusulas que o base padrão não tem:
1. **Exposição única, explícita:** `This is ONE single real photographic exposure, never a composite or a collage: every element shares the same light, the same grain and the same depth of field.`
2. **Câmera recuada até a leitura:** `The camera is pulled back enough that the scene is immediately readable at a glance`, com o assunto na METADE inferior (não em três quartos).
3. **Topo estourado, obrigatório:** `The ENTIRE UPPER THIRD is bright blown-out white haze, sky or wall, completely empty`, que é o que faz o fade dissolver sem emenda.
**Bônus de direção que resolveu o "cadê o cinema":** para cena de contraste parado × em movimento, pedir **borrão de movimento de longa exposição** no que anda e nitidez no que está parado. O borrão é a prova ótica de que é uma foto só — foi ele que matou a cara de montagem do slide 5, não a composição.
**Regra:** o `base` padrão continua sendo o default para still-life e objeto em close. **Cena com pessoas, ambiente ou qualquer coisa que precise de contexto pra ser entendida usa `base_wide`.** Os dois vivem no `prompts.json` do carrossel e se escolhem por imagem, no campo `base`.

### 2026-09-01 — Quando o corte da pessoa reprova duas vezes, tirar a pessoa (carrossel 77, slide 15)
**O que foi feito:** o slide de CTA pedia "dinheiro no bolso do dono" e foi a três voltas com gente na cena: v1 homem atrás da mesa (não remetia a dinheiro), v2 mão no bolso da calça — **enquadramento ambíguo, barrado antes de mostrar** —, v3 dinheiro no bolso da camisa e o user: *"cortou a cabeça no meio... pode fazer mais objeto e menos pessoa esse slide."*
**O que resolveu:** tirar a pessoa inteira. Camisa de trabalho pendurada na cadeira com o maço no bolso, chaves e óculos no assento. Sem corpo, não há corte possível — e a cena ganhou um beat que a versão com gente não tinha (fim de expediente, o dia acabou e o dinheiro ficou com o dono).
**Regra:** a faixa inferior do editorial-punch corta o corpo humano em alguma altura sempre, e pescoço/queixo/quadril são os piores lugares. Quando a cena pede "uma pessoa fazendo X" e o enquadramento reprova **duas vezes**, parar de recortar melhor e **trocar a pessoa pelo objeto que carrega a ação** (a camisa pelo dono, o crachá pelo funcionário, a cadeira pela cadeira vazia). Estende a regra de 31/08 do carrossel 74 ("enquadrar o gesto, não o rosto"): às vezes o certo é não ter ninguém no quadro.

### 2026-09-02 — Três erros de imagem numa peça só, e a régua que passa a medir isso (carrossel 81)
**O que foi feito:** o user reprovou o lote inteiro de imagens em duas rodadas: *"as imagens estao vindo com desfoque, isso eu nunca te direcionei a fazer"*, *"cadê a transição suave que sempre fizemos entre a imagem e o fundo?"*, *"ta tudo borrado, meuamigo claude ta tudo zoado"*, *"todas as imagens estão muito para baixo"*, *"tem muito angulo aberto nessas imagens... eu nao te dirigi para isso"*. Três causas independentes, todas minhas.

**1. O `base` do modelo foi SUBSTITUÍDO, não estendido.** Eu reescrevi o estilo-base do editorial-punch trocando *"a câmera é PRÓXIMA e o assunto é MUITO GRANDE, ocupando os três quartos de baixo; só uma FAIXA ESTREITA no topo, cerca de um quinto"* por *"a câmera é recuada o bastante pra cena ser legível; o assunto fica na METADE inferior"*. Isso produziu os dois sintomas de uma vez: ângulo aberto **e** imagem baixa (assunto começando em ~60% da foto em vez de ~25%).
**Regra:** o `base` do modelo é permanente como o próprio modelo. Cláusula nova se **acrescenta** ao base; nunca se reescreve o enquadramento dele. O `base_wide` (28/08) já é a variante autorizada para cena que precisa de contexto — usar ele, não inventar um terceiro.

**2. Desfoque pedido fora do escopo da regra de 31/08.** A regra de ilegibilidade existe para objeto cuja natureza é ser escrito (contrato, boleto, calendário, quadro). Eu apliquei `BLURRED and ILLEGIBLE` + `Shallow depth of field` em **12 das 14** cenas — porta, rua, calçada, gente andando. Medição no acervo: carrossel 73 pediu desfoque em 0 de 10, o 69 em 0 de 3, o 75 em 1 de 16.
**Regra:** desfoque é exceção pontual, nunca cláusula do base. Toda cena leva `EVERYTHING IS IN SHARP CRISP FOCUS, deep depth of field, no blur, no bokeh`. Se um objeto escrito precisa ficar ilegível, a cláusula vai **só naquela cena** e diz que a foto continua nítida.

**3. "Blown-out white" no topo mata a transição — o que funciona é CINZA.** Eu pedia `bright blown-out white haze` e as imagens vinham com o topo em luminância 243-254. Em `mix-blend-mode:multiply`, branco puro é transparência total: a imagem não existe e depois aparece de uma vez, o que o user lê como colagem. As imagens aprovadas do acervo têm topo em ~220.
**A régua, medida com o veredito do user no próprio 81:**

| | média do topo | desvio horizontal |
|---|---|---|
| aprovadas (img 1, 3, 11) | 177–215 | **5–25** |
| reprovadas (img 2, 4, 5) | 91–100 | **45–71** |

São **duas** condições, e precisa das duas: média alta (topo claro, some no multiply) e desvio baixo (superfície contínua — céu ou parede lisa — com NADA atravessando a faixa: telhado, viga, prateleira, placa, cabeça).
**Cláusula que resolveu:** `THE TOP BAND IS A HARD REQUIREMENT: that top fifth must be ONE single continuous evenly-lit pale surface spanning the FULL width, bright and uniform, with NOTHING crossing it at all: no roofline, no beam, no ceiling, no shelf, no sign, no branch, no head, no edge of any object. It must read as smooth blank paper.`
**Ferramenta:** `referencias/topo.py` mede isso e reprova antes de mostrar. Rodar SEMPRE depois de gerar, antes de renderizar. No 81 ele pegou 2 imagens sozinho.

**4. Gente no quadro.** Os aprovados têm figura humana em 30-50% das imagens (75: 5 de 16; 73: 3 de 10). Eu botei em 3 de 14, todas de costas e ao longe, por ter generalizado a regra de 01/09 ("trocar a pessoa pelo objeto"), que era o conserto de **um** slide específico, não uma política. O user: *"de novo sem figura humana"*.
**Regra:** a de 01/09 vale quando o enquadramento da pessoa reprova **duas vezes** naquele slide. Não é default do carrossel.

**5. A régua de vão morto estava frouxa.** O `check.py` tolerava 380px e o user leu 320-380 como *"imagem muito para baixo"*. Novo alvo: **200px, teto 260**, com trava de 18% no recorte lateral (acima disso decepa gente nas pontas). Atenção ao falso positivo: o detector procura pixel escuro e lê céu aberto como deserto — no 81 acusou o slide da feira livre, que o user tinha elogiado. Conferir no olho antes de mexer.

### 2026-09-04 — Vão morto se resolve subindo a IMAGEM, nunca descendo o texto (carrossel 87)
**O que foi feito:** cinco slides do 87 reprovaram no `check.py` por vão morto (274–418px) depois que o `fit.py` travou no teto de recorte de 18%. Eu resolvi **descendo o `top` do texto** (2: 320→430 · 3: 250→430 · 6: 400→540 · 8 · 11), copiando a diagramação do carrossel de referência que o user tinha mandado (texto na altura do meio do slide). O user reprovou: *"a 2 já desceu tentando seguir o padrão do carrossel que mandei como referência, ou seja, você ignorou o combinado para fazer o que a referência influenciou... está errado, nossa skill tem partes que revisam isso!!"*, *"o 3 nem se fala!!!"*, *"slide 6 baixo demais o texto e a imagem, suba"*.
**Diagnóstico:** referência de copy não é referência de layout. O modelo já fixa a altura do texto (`top` ~200–330; capa 236) e a régua de 01/09 diz que o vão morto é consequência da FOTO (assunto baixo demais) e se conserta pelo `imgheight` — o texto não é variável de ajuste. Reforça a entrada de 21/08 e 04/09 ("layout vem da skill, não do carrossel anterior").
**O que corrigiu, em ordem de preferência:**
1. **Subir a imagem** pela fórmula do `fit.py`, mesmo acima da trava de 18%, quando o assunto está centrado e **não há gente nas pontas** (2: H=1043, recorte 31%, cozinheiro no centro — aprovado).
2. Quando o recorte necessário decepa a cena (3: 46% cortaria a porta; 6: 35% cortava a ponta da faca), **trocar a foto** por uma com o assunto mais alto: enquadramento fechado em `base` (3: chef grande na porta, ombros no meio do quadro → H=820, 12%) ou composição vertical (6: faca EM PÉ fincada na tábua no lugar da faca deitada → H=810, 11%).
**Regra:** vão morto nunca se resolve descendo o texto. Ordem: `imgheight` → trocar a foto por assunto mais alto/vertical. A trava de 18% do `fit.py` é guarda pra **gente nas pontas**, não teto absoluto: com assunto centrado e sem pessoa nas bordas, pode passar (conferir no olho).

### 2026-09-04 — `fit.py`/`check.py` não enxergam assunto fino ou vertical; medir o topo do objeto na foto (carrossel 87, slide 6)
**O que foi feito:** com a faca em pé (img-06 v3), o `fit.py` mediu o "assunto" na tábua (y=930) porque a faca ocupa menos de 6% da largura da linha, calculou H=1176 e jogou o cabo da faca dentro do texto (`check.py` acusou INVASÃO a 10px). O detector procura linhas com >6% de pixels escuros — objeto estreito (faca, corda, poste, haste, sino pendurado) passa invisível.
**O que corrigiu:** medir o topo do objeto direto na foto (primeira linha com pixel <60 na faixa central, 35–65% da largura) e fixar H na mão: `H = (1350 − (texto_bottom + 200)) / (1 − topo/altura_da_foto)`. No 6: topo em 157/1024 → H=810.
**Regra:** assunto fino ou vertical não passa pelo `fit.py`/`fitn.py`. Medir o topo do objeto na foto e gravar o H no `imgheight.json` na mão; o `check.py` também vai errar nesses slides (falso positivo ou falso negativo), então a conferência é no olho.

### 2026-09-04 — A imagem transmite o ponto MAIS IMPACTANTE do texto do slide, não o cenário (carrossel 88)
**O que foi feito:** o slide "Todo mundo conhece um talentoso... E a ideia está lá até hoje. **Guardada.**" saiu com a foto de uma mesa de café com o caderno ABERTO, caneta em cima, xícara vazia — o cenário do talentoso, não o punch do slide.
**O que o user disse:** *"essa não passa a mensagem de ideia guardada do texto... sempre a imagem deve transmitir o ponto mais impactante do texto, isso é REGRA."*
**O que corrigiu:** caderno FECHADO no fundo de uma gaveta meio aberta, caneta presa na capa, poeira e papel velho por cima. A foto sozinha diz "guardada".
**Regra:** ao escrever o contexto de cada slide (a seção que guia a imagem), apontar primeiro a palavra-punch do slide e desenhar a cena a partir DELA. Antes de renderizar, conferir slide a slide: "a foto sozinha, sem o texto, diz o punch?". Cenário que só ambienta o arco reprova. Vale também pra capa: no 88 a capa "O talento acorda às nove. A vontade abriu a loja às seis." pediu a dicotomia literal (loja aberta à esquerda, fechada à direita, calçada vazia), não uma loja só.

### 2026-09-04 — Transição foto→linho "suave e imperceptível": o que decide é a CENA fechada, não o fade (carrossel 88)
**O que foi feito:** 6 de 9 slides reprovados na 1ª revisão (*"dá pra ver que tem um degradê, e a ordem é que seja suave, imperceptível"*). Na 2ª rodada eu mexi só no degradê (máscara CSS em curva mais longa + clareamento do topo da foto) e o user reprovou de novo os mesmos slides 3, 5 e 7: *"não mudou porra nenhuma do que falei pra mudar"*.
**Diagnóstico (comparando com o 83, publicado e aprovado):** nas fotos aceitas a cena é FECHADA (`base`): o assunto ocupa o quadro e começa logo abaixo da faixa pálida do topo. Nos meus 3, 5 e 7 a cena era ABERTA (`base_wide`): rua inteira, parede de esquina, chuva, noite — um campo grande de cinza escuro encostando no papel, e no 3 uma névoa dentro da loja. Qualquer rampa de papel pra cinza escuro é um degradê visível, por mais longa que seja. Não existe fade que disfarce campo cinza.
**O que corrigiu de primeira:** regerar as três no `base` fechado, com a cláusula *"NO fog, NO mist, NO haze and NO smoke anywhere inside the scene; only the narrow band at the very top is a pale, evenly lit, continuous surface"*. No slide 3, ainda, sujeito centralizado e "does NOT touch the left or right edges" (a v1 tinha o homem cortado pela borda da própria foto, e nenhum recorte conserta isso).
**Regra (ordem de defesa quando a transição reprova):** (1º) olhar se a foto é aberta: se for, regerar FECHADA e limpa por dentro — é o conserto real; (2º) só depois, como acabamento, o clareamento do topo da própria foto com rampa smoothstep até a fração onde o assunto começa (`dissolve.py`) e a máscara CSS em curva que chega a 100% no início do assunto em vez da reta de 26% (`fade.json`). Scripts em `conteudo/carrosseis/88_loja-as-seis/_scripts/`. Quando a foto é fechada, o acabamento é quase invisível; quando é aberta, ele não salva. Casa com a entrada de 2026-09-02 (item 1: `base_wide` produz ângulo aberto e imagem baixa) e com a memória de 04/09 sobre o `top` do texto: com o texto na posição da skill, a cena TEM que ser fechada pra não deixar vão — as duas regras apontam pro mesmo lugar.
**Calibragem de posição registrada nesta peça:** o user achou `top:160` (corpo) *"muito para cima"* e pediu pra descer *"levemente"* — fechou em corpo 200 e capa 240. É calibragem de uma peça, não mudança do modelo; anotar aqui pra não repetir o 160 seco nem voltar aos 236–354 herdados de outro carrossel.

### 2026-09-04 — Cena de objeto sem cláusula "NO PEOPLE" vira cena com gente, e gente repete em slides seguidos (carrossel 90)
**O que foi feito:** o roteiro do 90 (mercearia) tinha sete stills de objeto (caixa registradora, aventais, quadro de cortiça, cofre, martelo, prateleira) e três cenas com gente. O `base` traz "real working people" no estilo-base, e o motor colocou o dono em três stills que não pediam ninguém: caixa registradora (slide 2, v1), quadro de cortiça (4) e cofre (6), e o funcionário + o dono cortado na borda na prateleira (9). Resultado: gente em quatro slides seguidos (2, 4, 5, 6) e o dono repetido como se fosse o mesmo retrato, contra a regra de variedade do modelo ("gente em cena não repete em slides seguidos", entrada de 03/09).
**O que corrigiu de primeira:** regerar os quatro com a cláusula explícita no fim da cena: *"NO PEOPLE anywhere in the frame, no hands, no faces, no aprons: a still life of objects only."* Nas quatro regerações nenhum boneco apareceu. Quem pediu mão (slide 7, martelo) continuou pedindo "only the hands and forearms, no face" e veio certo.
**Regra:** toda cena de OBJETO leva a cláusula "NO PEOPLE" por escrito, porque o estilo-base pede gente e o motor obedece ao estilo-base quando a cena não nega. Não confiar em "the safe is the only subject": isso não impede o motor de colocar o dono ao lado do cofre. E antes de gerar, contar quantos slides seguidos vão ter gente no roteiro; três é o teto, e stills de objeto são o que quebra a sequência.

### 2026-09-09 — Slide que DESCREVE a situação em vez de dizer a DOR; a capa é o grito mais ácido; uma dor só (carrossel 106)
**O que foi feito:** a v1 do 106 (semente S13, "problema nunca é dinheiro") abriu com narrativa em ordem cronológica ("Dia 10, folha pra pagar, caixa zerado. Você ligou pro gerente do banco. Dois dias depois o limite caiu e você respirou aliviado."), tinha três causas no miolo (preço, venda, gente) e slides de mecanismo explicando ("Entra 100, sai 110. Faltam 10, e o banco empresta os 10."; "EMPRÉSTIMO NÃO TAPA BURACO. ESCONDE."). Levou quatro versões.
**O que o user pediu, em ordem:** (1) *"a dor explorada deve ser mais forte... foque em uma coisa e faça"* (empréstimo, cheque especial, dívida com banco pra tapar rombo da operação que não fecha; perde carro, rancho, casa). (2) *"o slide 8 deveria ser o slide gancho. Slide 1 e 2 não precisa existir, podemos ser direto na dor ao invés de construir a narrativa."* (3) Sobre a reescrita dos slides de abertura: *"o problema não é a copy, mas sim o papel deles... Descrever a situação não é necessário, é necessário falar da dor do ICP direto, a realidade ele já vive! E a linguagem deve ser mais ácida como se o próprio Hélio estivesse falando."* Aprovado como *"carrossel fantástico"*, com pedido de valer pra todos os próximos.
**Antes → depois (o que separa as duas linguagens):**
- Descrição: "Dia 10, folha pra pagar, caixa zerado. Você ligou pro gerente do banco." → Dor direta: "Você abre às sete e fecha às nove. Trabalha mais que qualquer funcionário. **E o único que tira lucro da sua empresa é o banco.**"
- Mecanismo em slide próprio: "Entra 100, sai 110. Faltam 10..." → Dor ácida: "Você não tem mais uma empresa. **Tem uma dívida com placa na porta.** O lucro que era pra ir pro seu bolso vai pro banco no dia 10."
- Grito de tese: "EMPRÉSTIMO NÃO TAPA BURACO. ESCONDE." → Grito de dor: "**VOCÊ VIROU FUNCIONÁRIO DO BANCO. E AINDA AGRADECE O GERENTE.**"
- Capa de abertura ("O empréstimo não foi pra crescer. FOI PRA FECHAR O MÊS.") → o grito mais ácido do miolo virou capa: "**O BANCO NÃO QUEBRA SUA EMPRESA. ELE SÓ FINANCIA A QUEBRA.**" (redação do user).
- Solução genérica ("Clareza é saber, antes de assinar, se a conta da empresa fecha") → casada com o tema: "Clareza é saber, **antes do dia 10**, quanto entra, quanto sai, quanto sobra. Se falta, o conserto é na operação. **Não no limite do banco.**"
**Regra (vale pra TODO carrossel daqui em diante):**
1. **O ICP já vive a realidade. Não descrever a cena; dizer a dor.** Slide de abertura não conta "o que aconteceu" (dia X, ligou, caiu, respirou): diz o que ele SENTE e o que ele PERDEU, na cara, com o objeto na frase (a placa na porta, o dia 10, o carro de garantia, o gerente). Teste: se o slide poderia ser o parágrafo de abertura de uma reportagem sobre ele, está descrevendo; reescrever como tapa.
2. **A capa é o grito mais ácido da peça**, onde quer que ele nasça no rascunho (reforça 2026-07-20). Se o melhor grito está no slide 8, ele é o slide 1 e o que vinha antes morre.
3. **Uma dor só por carrossel.** Nada de três causas, três pilares ou três nascedouros no miolo. O método/MBV entra só na oferta. A causa técnica é UMA e se repete como punch, não como slide de explicação.
4. **Mecanismo não ganha slide próprio.** "Entra 100, sai 110" e "empréstimo esconde o vermelho" só existem como punch dentro de um slide de dor ("Empréstimo pagando empréstimo, **e a operação continua no vermelho**").
5. **Ácido = o Hélio falando com nome e endereço.** Nomear o inimigo (o gerente do banco, não "o mercado"), o gesto que dói ("e ainda agradece o gerente"), o que virou ("funcionário do banco", "dívida com placa na porta"). Verbo duro, ironia seca, zero enunciado.
6. **Slide de solução/doutrina casado com o tema, nunca genérico.** Em fluxo de caixa: dia 10, entra/sai/sobra, parcela de cor, limite do banco. "Clareza é saber se a conta fecha" serve pra qualquer tema, logo não serve pra nenhum (teste da substituição do `voz-tatsuo.md`).
**O que continua valendo junto:** endosso antes da cutucada (2026-08-29) segue de pé, só que endosso aqui é dizer a dor POR ele ("o único que tira lucro é o banco"), não narrar a vida dele; corpo com carne (2026-08-31); teto de ~130 caracteres por slide (2026-09-01); os slides que o user marcou como bons (gerente/carro/capital de giro; limite/carro/rancho/casa; conta que fecha não precisa de banco) são a régua de tom.

### 2026-09-11 — A foto tem que nascer pro slide: parede no tom do fundo padrão como parte da imagem, não foto inteira remendada com degradê (carrossel 111)
**O que foi feito:** capa (salão lotado com balcão na frente) e slide 2 (fachada com a porta de enrolar meio levantada; depois, close das mãos no cadeado com a chapa corrugada subindo até o topo) geradas como fotos de quadro inteiro, com textura até a borda de cima, e coladas no linho com a máscara de 26 %. Nas duas o degradê apareceu.
**O que o user disse:** *"não foi um degradê bem feito, dá pra melhorar. Note que todos os comentários de degradê ruim são de imagens que não são pensadas para caber no slide, mas para um slide inteiro só de imagem"*. E apontou o slide 3 (dono e homem de terno no balcão, parede lisa atrás) como o gabarito: *"a proposta é o fundo da imagem (nosso fundo padrão) fazer parte de verdade da imagem gerada, e não algo que tem que ser feito um degradê para combinar (não que você deva parar de fazer o degradê, muito pelo contrário, é mais sobre a proposta da imagem)"*. Depois corrigiu a minha descrição: *"a parede não é branca (fundo padrão que utilizamos), é texturizada levemente off white; eu não tenho que falar, você tem que pegar direto do padrão"*.
**O que corrigiu de primeira:** cláusula de composição no prompt (sujeito só nos 55 % de baixo; 45 % de cima = parede lisa no tom do padrão, parte da foto, sem nada atravessando). Regeradas 1, 2, 5 e 13: as quatro passaram no `topo.py` com média 252-253 e desvio < 1,5, sem `dissolve.py`. Medido no render: a parede da foto em `multiply` leu 240 contra 243 do linho puro.
**Regra:** (1) a foto é concebida pro slide, com a parede do fundo padrão dentro dela; cena aberta com textura até o topo reprova antes de gerar. (2) A cor e a textura da parede saem do arquivo `_banco-referencias/background para carrosséis.png` (medido 11/09: #F3F3F3, desvio 4,6), nunca de "branco" nem de memória. (3) O degradê continua como acabamento. (4) Com a parede na foto, o `check.py` acusa vão morto falso: julgar no olho. Vive no modelo → "Estilo de imagem".

### 2026-09-11 — Capa toda em Anton reprova; texto levemente mais baixo; slide 13 do caminho diagnóstico sem pessoa (carrossel 111)
**O que foi feito:** capa com as duas frases do user em Anton (3 linhas, 83 px); blocos de texto em corpo 200 / capa 240 (calibragem de 04/09); CTA com o dono na porta da loja.
**O que o user pediu:** *"todo o texto em anton fica muito ruim de ler"* → setup em serif preto 48 px + só o grito em Anton. *"Todos os blocos textuais de todos os slides devem ser descidos levemente a altura"* → corpo 240, capa 280. *"slide 13 - a imagem vai ser só de um caixa com dinheiro faltando, não uma pessoa"* → still da registradora com uma nota e três moedas.
> **[PARTE SUPERADA em 13/10/2026]** Anton em uma linha só quando couber, mesmo abaixo de 80 px (o 201 foi ao ar com o grito a 76 px numa linha). Continua valendo: capa nunca toda em Anton.

**Regra (texto original de 11/09):** capa = setup serif + grito Anton, nunca só Anton; grito longo quebra em 3 linhas curtas em vez de descer a Anton abaixo de ~80 px. Calibragem vigente de altura: corpo 240, capa 280 (registrada no CSS do modelo). Pro slide de CTA, o objeto do tema serve tanto quanto o dono olhando pra câmera; quando o user pedir objeto, é objeto.

### 2026-09-19 — Repost em regime espinha sem o slide de oferta: "link do que?" (carrossel 132)
**O que foi feito:** o repost com arte nossa do "Ser dono é ser chato" (05/03/2026) seguiu a espinha literal do original, que fechava direto no "Comenta COMANDO" sem nomear o treinamento. A peça foi entregue com 13 slides e o CTA "que eu te mando o link no seu direct" sem nenhum slide dizendo link de quê.
**O que o user disse:** *"link do que? não explicou, cadê o desenvolvimento do CTA?"*
**Correção:** entrou o slide 13 de oferta ("Eu tenho um treinamento pra donos de PME onde ensino a montar isso: o rito de cobrar, acompanhar e treinar até o combinado ser cumprido todo dia"), o CTA virou o 14 e a legenda passou a nomear o treinamento antes do "Comenta CHATO".
**Regra:** regime `espinha` governa a ORDEM e os BEATS do original, não o fechamento. Todo carrossel de lead, repost incluído, fecha no padrão do modelo (seção "Fechamento"): slide de oferta com o treinamento nomeado e o que ele ensina, casado com o tema, e SÓ ENTÃO o "Comenta PALAVRA". Original sem oferta (era da global COMANDO/307) ganha o slide; nunca herdar o CTA global. Conferir antes de renderizar: existe um slide que responde "link de quê?".

### 2026-09-29 — Dor do micro-empresário num conteúdo pro ICP de R$3 a R$100 milhões (carrossel 164)
**O que foi feito:** a versão topo do 164 ("trinta anos de empresa e só sobrou a casa") falou a dor de quem sobrevive: "se a empresa fechar amanhã, quantos meses você aguenta?", "trabalhando só pra pagar o mês", "o mês continua fechando no zero", "pagar a conta de luz de casa".
**O que o user disse:** *"você está falando de empresários muito pequenos... o nosso cliente ideal são empresários que faturam de 3 milhões por ano até 100 milhões por ano. Esse cara não trabalha pra pagar o mês. Ele fatura, mas não sobra dinheiro pra ele... põe um pró-labore de 50 mil... quem trabalha pra pagar o mês é o muito pequeno, que tem uma lojinha, um mercadinho; não é pra ele que a gente faz esse conteúdo."*
**Regra:** toda dor, cena e objeto de slide e legenda cabe no porte do ICP (faturamento de R$3 mi a R$100 mi/ano; no CRM, MQL = 10+ funcionários). A dor dele é **faturar muito e não sobrar**: pró-labore alto como único ganho (30, 40, 50 mil), dividendo raro, patrimônio que não sai da empresa, modelo de negócio que o mercado deixou pra trás. Proibido o vocabulário da sobrevivência do micro: fechar o mês no zero, meses de reserva, conta de luz de casa, lojinha, mercadinho. Teste antes de entregar: "um dono com 40 funcionários se reconhece nessa frase?".
**Reincidências na mesma peça de regras que já estavam aqui:** duas dores abertas ao mesmo tempo (faturar e não sobrar × dívida com banco; ver 2026-09-09, "uma dor só"); slides sem ponte, "várias porradas sem conexão" (ver 2026-07-20 e o slide-ponte); oferta do RAIO-X "jogada do nada" (ver o CTA que vende o que o dono quer). Na oferta do RAIO-X, vender com o que a página promete de fato (aula gravada do Hélio, "como eu leio uma empresa em poucos minutos", as 15 perguntas, "por que ela não coloca dinheiro no bolso do dono"; custa R$97 com garantia, então nunca chamar de gratuita) e fechar com a conta que faz o dono se sentir burro de não comentar ("uma aula agora ou mais dez anos tirando o mesmo pró-labore").

---

## Outubro de 2026 (consolidado em 13/10, na preparação da máquina pro novo operador)

> Estas entradas foram conferidas contra o que foi ao ar (texto final, imagem escolhida, legenda publicada), não só contra o que o user disse no meio da rodada. Peça única e escolha artística ficaram de fora de propósito: "a gente enche de regra o negócio e começa a se perder".

### 2026-10 — O tom morno é o erro nº 1 (164, 165, 167, 182, 193, 195, 196, 198, 200, 201)
**O que foi feito:** texto correto, equilibrado e impessoal; coach ("tenha fome de vencer"); passivo ("ver o seu filho crescer longe de você"); abstrato (a bula do 198).
**O que o user pediu:** *"menos genérico, mais hélio, mais pessoalidade, mais agressividade, verdade na cara"*; *"traga sempre o tom de voz do helio, direto, acido, dedo na ferida"*; *"nós somos anti-coach"*; *"o Hélio é muito mais agressivo"*.
**Regra:** ver `voz-tatsuo.md` → "Dedo na ferida é condenar a DOR, não o cara" e o gabarito `voz-helio-gabarito.md`. Antes do CHECKPOINT 1, comparar cada slide com o gabarito.

### 2026-10 — Texto telegráfico pra caber na régua (200, 201, 207)
**O que foi feito:** cortar sujeito, artigo e conectivo pra caber nos 130 caracteres ("Ninguém aguenta doze horas por dia").
**O que o user pediu:** *"perceba como adicionei palavras que tornam mais humano e menos IA"*; *"quero que entenda isso e aplique em todas as partes"*.
**Regra:** frase falada inteira; teto de ~180 por slide; estourou, corta ideia ou divide o slide. Ver `voz-tatsuo.md` → "Frase falada inteira".

### 2026-10 — Fazer só o que foi pedido (165, 193, 182)
**O que foi feito:** no 193 o user pediu pra mudar a redação e o Claude mudou a abordagem; no 165 cortou uma linha que o user tinha elogiado; no 182 interpretou "manchete" e reescreveu uma legenda já aprovada, que foi ao ar errada.
**O que o user disse:** *"não é pra mudar a abordagem... é para mudar como vamos escrever"*.
**Regra:** pedido de redação muda a redação, não a ideia. Pedido de explicação não é pedido de mudança. Texto aprovado não se reescreve sem pedido. No ambíguo, perguntar antes de mexer.

### 2026-10 — O user volta à versão anterior (vale pra todo formato)
**O que acontece:** em vários posts o user pede uma mudança e, vendo a nova, volta pra anterior ("vamos com o original mesmo", 226; "esquece a parte que eu falei", 173; "vou manter a antiga", 230).
**Regra:** nunca descartar a versão anterior (texto, imagem ou legenda): salvar numerada e mostrar a nova ao lado da antiga. A correção feita no meio da rodada só vira lição quando a escolha final confirmar.

### 2026-10 — Texto e quebra que o user manda entram literais
**Regra:** frase, quebra de linha e redação que o user escreve entram palavra por palavra (171, 179, 200, 201, 202, 207). Ajuste vai só como sugestão, ao lado. Exceção: quando ele marca o texto como rascunho ("algo assim", "a ideia é essa, dá pra melhorar", "você vai melhorar").

### 2026-10 — Diagramação do texto (167, 179, 201, 218, 226)
**Regra (essencial, mexe em leitura):** grito em Anton numa linha só quando couber; frase curta de remate não se quebra; slide com texto demais vira dois; 4 linhas = 2+2, nunca 3+1 (já era regra desde 24/06 e foi quebrada no 226).

### 2026-10 — Imagem reaproveitada tem que dizer o punch novo (167, 179)
**O que foi feito:** imagem de outro carrossel reusada sem conferir se conta o punch deste slide (5 refeitas no 179).
**Regra:** imagem do banco ou de post anterior passa pelo mesmo teste da imagem nova: ela diz o ponto mais impactante do texto deste slide? (Reforça 04/09.)

### 2026-10-13 — O Hélio nunca é gerado por IA (decisão do user)
**O que foi feito:** uma imagem gerada de um homem de bigode no balcão foi usada como o Hélio em 164, 167, 179, 184 e 193.
**Regra:** proibido gerar o Hélio por IA. Quando o slide precisa dele, foto real (acervo `~/Desktop/fotos para carrosséis/`) ou um objeto que simbolize. Tratar e limpar o fundo de foto real continua permitido.

### 2026-10-13 — Repost: 90 dias corridos e texto original literal (135, 231)
**Regra:** só repostar post com mais de 90 dias corridos de publicação (o Instagram corta alcance de conteúdo repetido). No repost com arte nova, texto, subtítulo e diagramação da capa do original ficam iguais, palavra por palavra e na mesma quantidade de slides; só entram o slide de oferta e o CTA (ver 2026-09-19). É exceção à regra "capa = 2 linhas, sem subtítulo".
