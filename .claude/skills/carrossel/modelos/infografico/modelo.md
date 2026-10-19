# Modelo: Infográfico educativo (voz Tatsuo Academy)

**Em uma linha:** carrossel educativo que traduz UM item da apostila do MBV pro Instagram, com um recurso visual por slide (framework, gráfico, linha do tempo), na voz da **Tatsuo Academy**: fundo escuro texturizado, Montserrat, vermelho só `#A91C20` e CTA de link na bio com o botão "QUERO PARTICIPAR DO MBV". Vai pro perfil da Tatsuo Academy: **sem /etiqueta e sem Manychat**.

> Criado em 26/09/2026 (série de vendas, post 152) e redefinido entre 07 e 12/10/2026 nos posts 213, 222, 224 e 229. O padrão vigente é o do **224** (layout F) e do **229** (layout G). A estética de 26/09 (Anton + Open Sans, cards vinho, faixa vermelha, vários tons de vermelho, CTA "Comente PALAVRA") é histórico: não copiar. **Voz:** NÃO é `referencias/voz-tatsuo.md` (Hélio); ver a seção 2. **Imagem:** não usa foto nem IA.

---

## 1. Quando usar (propósito / canal)

- **Canal:** feed do perfil da **Tatsuo Academy** (não o do Hélio), 1080 × 1350.
- **Objetivo:** ensinar um conceito do método de forma visual e levar ao MBV pelo link da bio.
- **Fonte:** a apostila do MBV (edição de setembro/2026, `Apostila Setembro v.final.pdf`, 200 páginas). **Ela não está no Git.** Nesta máquina fica em `_contexto/apostila-mbv/` (fora do Git). Sem a apostila na máquina, pedir o PDF antes de começar: post da apostila não se escreve de memória.
- **Pauta:** quando pedirem sugestão, abrir a apostila e propor 1 item com o porquê (contraria o que o dono acredita, tem número que choca, vira framework visual, leva ao CTA) e 2 a 4 alternativas com a página. Quem escolhe é quem pediu (às vezes o user escolhe outro e compara com a sugestão, como no 224).
  - Páginas já usadas ou já sugeridas: p. 1-2 (analfabeto empresarial, três pilares, visão sistêmica: 224); p. 17 e 49-55 (matrizes, Balanço Japonês: 222); p. 27-28 (três alavancas do lucro) e p. 37 (juro da antecipação), sugeridas no 229; p. 44 (efeito do crescimento no caixa: 229); p. 8-11 e 24 (os 4 elementos do modelo de negócio: 256 em carrossel e 257 em tela única); p. 58-130 (Crescimento, vendas: série de 26/09).
  - Já feitos (não repetir sem pedido): modelo de negócio (213, refeito no 256/257 a pedido do João), Balanço Japonês (222), três pilares (224), vender mais (229). Antes de sugerir, conferir em `conteudo/carrosseis/` os `carousel-text.md` que citam a apostila.
- **Quando NÃO usar:** peça na voz do Hélio ou com foto dele (`fotos-reais`, `editorial-punch`), fábula, comentário de notícia (`thread-x`), frase única (skill `/frase`).

## 2. Voz e texto

- **Voz da marca, não do Hélio** (user, 26/09, 07/10 e 10/10: "É mais estilo do Tatsuo Academy que hélio"). Direta, didática, sem primeira pessoa e sem anedota. Fala com "o empresário", "o dono", "a empresa" e, quando ajuda, com "você". Português escrito ("para", não "pra"). Exceção declarada à regra de 27/08 ("quem fala é o Hélio"): aqui "Tatsuo Academy" e "MBV" aparecem.
- **Educativo, não punch** (07/10, 213; 11/10, 224): cada conceito diz **o que é e por que importa** pra empresa, com fundamento. Sem frase de impacto e sem frase de efeito de rodapé. "É educativo, não é para dar punch nos outros."
- **A apostila é fonte, não texto** (12/10, 229): ela garante conceito, número e lógica; o texto do post é **mastigado** pra quem nunca ouviu o termo ("a maioria dos empresários não sabe o que a gente tá falando... Entende nem que é ciclo financeiro"). Cada termo técnico vira a cena que o dono vive ("paga o fornecedor hoje, o cliente paga daqui a 40 dias, o dinheiro fica preso"); termo técnico só se for explicado na mesma frase. A conta aparece destrinchada ("R$ 10 mil × 40 dias = R$ 400 mil"), nunca só o resultado. Número que o Claude deriva (ex.: 200 ÷ 25 = 8 meses) é avisado no CHECKPOINT 1.
- **Slide denso se divide** (07/10 e 10/10): "mesmo assim tem muito texto"; "o slide 3 tem muito texto, pode ser dividido em dois". Texto que não cabe na forma do framework se corta ou vai pra outro slide. O 222 passou de 5 pra 8 slides assim.
- **Refação de post de terceiro: texto do zero** (07/10, duas vezes, e 10/10): da referência fica só a ideia e o framework. Cada linha nasce da apostila. No fim, conferir que nenhuma expressão da referência sobreviveu. Nuance do 222: "Mude o que for necessário, o que não for necessário pode manter" (vale pro conteúdo, não pra copiar frases ruins).
- **Uma ideia por post** funcionou nos três últimos (222, 224, 229). Arcos que deram certo (exemplos, não molde):
  - 222: pergunta que o dono não sabe responder (capa) → por que é difícil responder → por que o dono se engana → CTA.
  - 229: a tese contraintuitiva com o gráfico (capa) → o mecanismo → a conta → de onde sai o dinheiro → CTA.
  - 224: o framework num slide só + CTA.
- **CHECKPOINT 1** (como em todo modelo): texto de todos os slides + legenda, com a página da apostila de onde sai o conteúdo, antes de qualquer HTML.

## 3. Nº e formato

- 1080 × 1350 (4:5). De 2 slides (framework + CTA, como o 224) a 8 (222), ou **1 tela só no Frame Work** (layout H, seção 6.3).
- No carrossel, o CTA é **sempre um slide próprio** (pedido no 213: "um novo slide, só com a CTA"; seguido no 222, 224 e 229). No Frame Work (tela única) ele vai numa faixa no rodapé da própria tela.

## 4. Camadas (o processo, nesta ordem)

1. **Fundo:** arquivo fixo `conteudo/carrosseis/_banco-referencias/background infografico escuro.png` (vem pelo Google Drive), copiado pra `<post>/imagens/fundo.png`, com vinheta radial leve por cima. Nunca desenhar o fundo em CSS: o fundo sintético saiu "chapado" e foi reprovado (26/09). Se o arquivo faltar, regerar idêntico com `python3 .claude/skills/carrossel/modelos/infografico/fundo/gen_fundo.py 7 "<destino>"`.
2. **Elementos:** formas, setas e gráficos em CSS/SVG, só com as cores da seção 5.
3. **Ícones:** só do kit `icones/` (Tabler outline, catalogado em `icones/README.md`). Ícone novo entra no kit depois de conferido no fundo escuro. Nunca ícone gerado por IA.
4. **Texto:** fonte real (Montserrat). Nunca texto dentro de imagem gerada.

**Produção em código, não no Canva** (decisão do user, 26/09). Cada post tem `_scripts/build.py`, que gera os `instagram/slide-XX.html`. **Partir do código do 224 (layout F) ou do 229 (layout G)**, copiados em `frameworks/`. O `build.py` e o `base.css` desta pasta montam os layouts A a E com o visual antigo (Anton, Open Sans, vinhos): servem só como ideia de estrutura, e o visual tem que ser trocado pelo da seção 5.

## 5. Regras visuais (padrão vigente: 224 e 229)

| Elemento | Valor |
|---|---|
| Fundo | `imagens/fundo.png` + vinheta `radial-gradient(ellipse at 50% 45%, rgba(0,0,0,0) 55%, rgba(0,0,0,.45) 100%)` |
| Fonte | **Montserrat** em tudo (decisão do user, 13/10): 800 nos títulos, 600 no subtítulo, 500 no corpo, 700-800 em rótulo, etiqueta e botão. Anton, Open Sans e Source Serif ficaram nos posts antigos e não entram |
| Vermelho | **só `#A91C20`**, inclusive em texto sobre preto, badge, seta e etiqueta. Faltou contraste: resolver com peso ou tamanho, nunca com outro tom, nem o da referência ("Não quero que você use outra cor sem ser a nossa padrão", 11/10) |
| Tons de apoio | branco; grafite `#1f1f1f` / `#2c2c2c` nas formas; cinzas de texto `#bdbdbd` a `#e8e8e8` |
| Título da capa ou do framework | **bloco branco** (raio 6, sombra), caixa alta, 1ª linha preta, 2ª em `#A91C20`. Nos slides internos do 229 o título vai sem bloco (branco + 2ª linha vermelha) |
| Destaque | **por fundo**: etiqueta `#A91C20` com texto branco, ou bloco branco com texto vermelho e contorno vermelho. Sublinhado e negrito sozinhos não destacam ("Colocar sublinhado não mudou nada. Bota um fundo", 12/10) |
| Composição | mais centro que esquerda: "Pode ser um ou outro alinhado à esquerda, mas tudo centro quase" (10/10). Tudo alinhado à esquerda "parece que é coisa de apostila" |
| Recurso visual | um por slide, que guia o olhar (layouts F e G). Lista de partes de um todo vira framework visual ("Por que você não faz um framework disso?", 10/10) |
| Paginação | **nenhuma** ("Um de dois, dois de dois, pode tirar, isso aí não faz sentido nenhum", 11/10). "ARRASTE →" no rodapé até o penúltimo é o que os três últimos posts usaram |

**Post de Instagram, não apostila** (reprovado 4 vezes: 213, 222 duas vezes, 224): "muito amador... muito flat"; "Material didático de apostila não tá parecendo um post de Instagram"; "Olha como ele preenche bem a imagem. Dá pra ler. É autoexplicativo". O que passou: tipografia grande que ocupa o quadro, destaque em bloco de cor, poucos elementos, cada slide se explica sozinho.

**Texto inteiro dentro da forma** (222 e 224): "Tem texto saindo dele. Tem que ficar o texto todo dentro." Posição de texto em forma se acha medindo, não no olho (ver 6.1).

**Área de segurança (07/10):** nada de conteúdo a menos de **90 px das laterais** e **110 px do topo e da base** (texto, formas, títulos). "Tudo que está muito perto das bordas... tem que respeitar a margem, pô." Só o símbolo do logo pode ficar na faixa de baixo, a no mínimo 60 px da borda. O `render.js` acusa. Com pouco texto, centralizar o bloco na vertical em vez de colar no topo.

**Referência externa dá só o layout** (11/10): a composição pode vir de outro perfil; cor, fonte e marca são sempre as nossas.

**Proibido:** fundo desenhado em CSS; qualquer vermelho que não seja `#A91C20`; gradiente de cor (só a vinheta do fundo e o grafite sutil das formas); emoji; texto estourando a forma; paginação; CTA em fundo vermelho chapado só com texto.

## 6. Layouts

| Código | Layout | Situação |
|---|---|---|
| A | Grade de cards numerados, 2 colunas | série de 26/09: estrutura reaproveitável, visual antigo |
| B | Hub: círculo central com 4 a 6 nós | idem |
| C | Templo/pilares | idem |
| D | Comparativo em 2 colunas (A × B) | idem |
| E | Funil com quantidade e taxa por degrau | idem |
| F | **Círculo em fatias** (seção 6.1) | **vigente**, registrado pelo user em 11/10 (post 224) |
| G | **Carrossel explicativo com gráficos** (seção 6.2) | **vigente**, registrado pelo user em 12/10 (post 229) |
| H | **Frame Work: o framework numa tela só** (seção 6.3) | **vigente**, registrado pelo João em 19/10 (post 257) |

Layout novo: construir na primeira vez, mostrar ao user, registrar aqui só com o sim dele.

### 6.1 Framework F: círculo em fatias (post 224)

Use quando o conteúdo é um conjunto de 3 (ou 4) partes de um todo: pilares, etapas, destinos do dinheiro. Código de referência: `frameworks/circulo-em-fatias_build-224.py` (copiar pra `<post>/_scripts/build.py`); busca de posição: `frameworks/circulo-em-fatias_busca-posicao.js`.

**Composição (1080 × 1350):**
- **Título em bloco branco**, igual ao botão do CTA: caixa branca (raio 6, sombra), Montserrat 800 caixa alta, 1ª linha preta (~50 px), 2ª linha em `#A91C20` maior (~64 px). Largura ~860, topo a ~112 px.
- **Subtítulo** curto embaixo (Montserrat 600 ~26 px, branco) com o trecho final sublinhado em `#A91C20`. Ex.: "Entenda o papel de cada um *na sua empresa*".
- **Círculo grande** (centro 540 × 770, raio ~430) dividido em fatias por **vãos pretos grossos** (16 px); fatias em grafite (#1f1f1f → #121212); **contorno vermelho fino** só no arco externo de cada fatia.
- **Centro:** anel vermelho (raio ~105) com miolo preto (~68) e ícone branco do kit (ex.: `building-store`).
- **Badges:** círculos vermelhos (Ø 100) com ícone branco, na borda do círculo, com anel preto em volta. Nas fatias de cima ficam na **borda superior** (240° e 300°), nunca no meio da fatia; na de baixo, no fundo (90°, puxado 12 px pra dentro pra respeitar a margem).
- **Conteúdo de cada fatia = um bloco só, centralizado:** nome do pilar numa **etiqueta vermelha** (`#A91C20`, texto branco Montserrat 800 ~27 px, raio 6) + parágrafo (Montserrat 500 ~21 px, entrelinha 1.4) com a definição e a consequência na mesma frase corrida. Sem rótulo do tipo "Por que importa:" e sem setas.
- **Posição do bloco:** no centro geométrico da fatia, à mesma distância do centro do círculo nas três (~250 px), blocos das fatias de cima espelhados. Achar por medição: `node .claude/skills/carrossel/modelos/infografico/frameworks/circulo-em-fatias_busca-posicao.js <post>/instagram/slide-01.html` mede cada linha contra a borda, o anel central, os divisores e os badges e devolve a posição. Folga mínima aceitável: ~12 px.
- **Slide de CTA que acompanha:** mesma linguagem (fundo escuro, título no mesmo estilo, cartões com contorno vermelho e o badge de cada pilar, botão branco "QUERO PARTICIPAR DO MBV" com contorno vermelho, "LINK NA BIO →" branco, negrito e legível).

**Proibido neste framework:** texto preso no topo da fatia; badge disputando o meio da fatia com o texto; texto encostando no anel central ou nos divisores.

### 6.2 Layout G: carrossel explicativo com gráficos (post 229)

Use quando o post explica um mecanismo com números (dinheiro, prazo, crescimento, margem). Princípio do user: **cada slide tem um recurso visual que guia o olhar** ("gráfico, setinha, desenho, coisa guiando o olhar"), e o texto explica o que o gráfico mostra. Nunca número solto sem desenho. Código de referência: `frameworks/graficos-explicativos_build-229.py` (copiar pra `<post>/_scripts/build.py`).

**Texto:** a conta aparece destrinchada no próprio gráfico (ex.: "R$ 10 mil × 40 dias = R$ 400 mil"). Um slide = um passo do raciocínio, encadeado com o seguinte.

**Recursos visuais do kit (todos em SVG, cores da marca):**
- **Capa com gráfico-tese:** ordem fixa: título no bloco branco → gráfico → frase-leitura do gráfico (branco, negrito, ~30 px) → gancho num **bloco branco com texto vermelho e contorno vermelho** ("Entenda por que isso acontece →"). Ex.: barras vermelhas subindo (vendas) × linha branca com seta descendo (caixa), com etiquetas "▲ mais vendas / ▼ menos dinheiro no caixa".
- **Linha do tempo:** dois badges grandes (início em vermelho, fim em branco com ícone vermelho), seta vermelha grossa entre eles com faixa translúcida, rótulo no meio com ícone (ex.: cadeado + "40 dias com o dinheiro preso"), "Dia 0 / Dia 40" embaixo.
- **Barras comparativas:** barras grafite com contorno; o acréscimo empilhado em vermelho; seta branca curva de uma barra pra outra; a conta em etiqueta branca acima de cada barra.
- **Gráfico mês a mês:** barras vermelhas abaixo do zero diminuindo (opacidade decrescente), linha do zero, seta pontilhada branca até o ponto de virada (círculo branco), nota curta em caixa alta no espaço vazio sem cruzar a seta.
- **Diagrama de caminhos:** bloco branco no topo com o valor ("R$ 200 mil / para crescer"), três setas vermelhas curvas abrindo pra três badges com ícone, cada um com título curto + uma frase.
- **Cartões A × B:** um grafite com contorno cinza (o lado "bom") e um vermelho cheio (o lado que dói), número grande + legenda curta.
- **Fecho de slide:** frase-síntese em bloco branco com texto vermelho e contorno vermelho, ou em cartão escuro com o trecho-chave em vermelho.

**Regras:** etiqueta que não pode quebrar linha leva `white-space:nowrap`; nada de rótulo cruzando seta ou barra; o `render.js` tem que passar e a conferência no olho também (colisão que a régua não mede: texto sobre a seta do SVG).

### 6.3 Layout H: Frame Work, o framework numa tela só (post 257)

Formato da conversa fixada "Frame Work Tatsuo Academy" (entrega em `Desktop/POSTS/Frame Work Tatsuo Academy/`). Pedido do João em 19/10, depois de ver o 256 em carrossel: "quero que desenvolva post únicos de apenas uma tela". Um item da apostila vira um framework visual que se explica sozinho, num post único. Código de referência: `frameworks/frame-work-tela-unica_build-257.py` (copiar pra `<post>/_scripts/build.py`).

- **Cabeçalho (mudado pelo João em 19/10, na linha do post da Academy instagram.com/p/Deq_zH3payF):** título em **Anton**, caixa alta, sem bloco branco, 1ª linha branca e 2ª em `#A91C20`, as duas no mesmo tamanho (72 px, entrelinha 1.2 pra o acento não encostar na linha de cima, topo em 110 px); subtítulo de uma linha em **Source Serif 4** (28 px, branco) com o trecho final sublinhado em vermelho. É exceção declarada à regra "Montserrat em tudo" (seção 5), só no cabeçalho do Frame Work: o resto da tela continua em Montserrat. O vermelho continua sendo só o `#A91C20` (a referência usa um vermelho mais vivo, que não entra).
- **Composição:** cabeçalho acima, o framework ocupando o miolo e o CTA no rodapé: botão branco "QUERO PARTICIPAR DO MBV" com contorno vermelho + "LINK NA BIO →" ao lado. Sem "ARRASTE" e sem paginação.
- **Framework do 257:** o círculo em fatias do layout F (6.1) em 4 quadrantes, com o nome em etiqueta vermelha e a definição curta (uma frase da apostila) dentro de cada fatia, e badge com ícone na borda externa. Outras formas (pirâmide, linha do tempo, árvore de decisão, A × B) entram quando o conteúdo pedir: construir na primeira vez, mostrar ao João e registrar aqui com o sim dele.
- **Texto da tela:** só o essencial do framework (nome + uma frase por parte). O que não cabe (exemplo, conta, "por que importa") vai pra legenda, que no Frame Work faz o papel dos slides internos: abre pela tese, desenvolve cada parte em um parágrafo com o exemplo da apostila e fecha no convite do MBV + link da bio + "Seja Bem-Vindo ao Fim do Analfabetismo Empresarial." (a do 257 tem ~1.500 caracteres).
- **Checkpoint:** o texto da tela e a legenda passam pelo João antes do HTML, como em todo modelo.
- **Folga no círculo:** etiqueta e parágrafo a pelo menos ~10 px da borda, dos divisores e do anel central; achar a posição no olho depois do render (no 257 a etiqueta "MARGEM DE CONTRIBUIÇÃO ALTA" encostou na borda e o bloco desceu 18 px).

## 7. Imagem

Não usa foto, imagem gerada por IA nem banco de imagens. O visual é todo das camadas 1 a 4. (Foto do Hélio nunca é gerada por IA, em modelo nenhum.)

## 8. Réguas (antes de mostrar)

- Da raiz do projeto: `node .claude/skills/carrossel/modelos/infografico/render.js conteudo/carrosseis/<post>/instagram` renderiza os `slide-XX.html` em PNG e confere:
  - texto estourando o próprio contêiner;
  - elemento saindo da página;
  - título de card batendo no círculo do número (layout A);
  - sobreposição entre elementos marcados `.solo`;
  - área de segurança de 90/110 px nos elementos `.solo`.
  A régua só mede o que está dentro de `.conteudo` e marcado com a classe `solo`: marcar cada bloco. Falhou, corrigir antes de mostrar.
- Se o render reclamar que não acha o Playwright: na raiz do projeto, `npm install` e `npx playwright install chromium`.
- **Olho:** abrir os PNGs e conferir o que a régua não vê (rótulo sobre seta, texto encostando em forma, ícone cortado).

## 9. Fechamento e entrega

- **O CTA está no slide e vende** (pedido 5 vezes entre 26/09 e 11/10: "Esses posts têm que ter CTA, tá? É, no slide também"; "Tem que vender o CTA também, pô"). Estrutura do 224 e do 229: pergunta que puxa o tema do post → sintomas ou ponte, quando couber → oferta do MBV → botão branco "QUERO PARTICIPAR DO MBV" → "LINK NA BIO →" legível.
- **CTA na mesma linguagem do miolo**: fundo escuro, cartões com contorno vermelho, badges. Nunca só texto em fundo vermelho chapado (reprovado no 224, 11/10: "A diferença do slide 1 pro slide 2 é totalmente gritante").
- **Oferta:** o MBV ligado ao tema do post. Texto do 229 (o 224 usou quase o mesmo): "No MBV, imersão de três dias para donos de pequenas e médias empresas, você aprende a fazer a gestão dos três pilares: Lucratividade, Crescimento e Cultura." No 222, a pedido do user, o CTA vendeu a ferramenta do post, que o MBV ensina. "Imersão" ou "treinamento" conforme o conteúdo, com preferência por "treinamento" (decisão do user, 13/10).
- **Legenda:** voz da marca, didática e encadeada, abre pela tese do post (não repete o título). Fecha com o convite pro MBV + link da bio e "Seja Bem-Vindo ao Fim do Analfabetismo Empresarial." Sem palavra-chave e sem "Comente". Tamanho sem regra própria: as do 213, 222, 224 e 229 ficaram entre ~800 e ~1.100 caracteres. Exemplo de fecho (229): "No MBV, imersão de três dias da Tatsuo Academy para donos de pequenas e médias empresas, você aprende a fazer a gestão dos três pilares: Lucratividade, Crescimento e Cultura. Clique no link da bio e garanta a sua participação."
- **Sem `/etiqueta` e sem Manychat:** o perfil é da Tatsuo Academy, que a máquina de análise não lê ("não faz sentido etiquetar", user, 11/10). Escrever isso no topo do `carousel-text.md`, como no 229.
- **Pasta:** `conteudo/carrosseis/[N]_[nome]/` com `carousel-text.md` (fonte com página, modelo, perfil, slides e legenda), `imagens/fundo.png`, `_scripts/build.py` e `instagram/slide-XX.html` + `.png`.
- **Rodada de correção guarda a anterior:** salvar o build anterior numerado em `_scripts/` (ex.: `build_v1_anel.py`, `build_v8_reprovado.py`) e mostrar a versão nova ao lado da antiga. O user volta à anterior com frequência (no 222: "eu gostei mais do anterior... Vamos voltar para o anterior").
- **Entrega:** copiar os PNGs + `legenda.txt` pra `~/Desktop/carrosseis claude/<palavra>/`, abrir no Preview e a pasta no Finder. Commit conforme a regra de commit da máquina (CLAUDE.md).

## 10. Exemplos e referências

- **Vigentes:** `conteudo/carrosseis/224_tres-pilares/` (layout F + CTA), `229_vender-mais/` (layout G, 6 slides) e `J257_quatro-elementos-tela-unica/` (layout H, tela única). O `J256_quatro-elementos-modelo/` é o mesmo tema em carrossel (F na capa + G no miolo), salvo e não publicado. O código deles está em `frameworks/`.
- **Conteúdo bom, visual superado:** `222_balanco-japones/` (8 slides; framework em quatro quadrantes; ainda com título em Anton, corpo em Source Serif, paginação "01/08" e CTA em fundo vermelho chapado, tudo superado no 224) e `213_quatro-elementos-do-modelo/` (grade 2 × 2 em Anton + Source Serif).
- **Histórico (não copiar o visual):** a série de vendas de 26/09 (152), com Anton + Open Sans, cards vinho e CTA por Manychat.

## 11. Casos (exemplos que ensinam; não são regra)

- **12/10, 229:** a v1 transcreveu a apostila ("Entende nem que é ciclo financeiro"); a v2, com texto bom e só números, pediu gráfico e setas; a v3 deixou o texto "mais explicativo" com a conta destrinchada. Na capa, a ordem título → gráfico → frase → gancho em bloco. Virou o layout G.
- **11/10, 224:** a v1 (anel pequeno + colunas embaixo) saiu "bem amador, bem ruim"; o padrão veio da referência do Alfredo (círculo ocupando o slide, conteúdo dentro das fatias, badges na borda), com a nossa cor. Depois: título em bloco branco, sem "Por que importa" (a consequência entrou no parágrafo), bloco no centro da fatia como o da Cultura, nome do pilar em etiqueta. Virou o layout F. O user também recuou de uma instrução própria ao ler o texto ("Não é pra fazer igual eu falei, que tá muito ruim"): por isso o texto passa pelo CHECKPOINT antes do HTML.
- **10/10, 222:** o primeiro design (círculos numerados, grade, fios, texto pequeno) foi "material didático de apostila"; depois, "tira esse aspecto de tudo alinhado à esquerda". A lista dos quatro destinos do lucro virou um círculo em quatro, e os slides densos viraram dois cada. Uma versão "como alguém ensinando", corrida, ficou "muito cru" e o user voltou à anterior: correção do meio da rodada só vale se a final confirmar.
- **07/10, 213:** item técnico explicado pela definição, sem lista de exemplos ("se for usar exemplo, vou ter que detalhar bastante"); no 229, ao contrário, a conta trabalhada foi pedida. Capa só com os nomes dos 4 elementos e a explicação em slides próprios, dois por slide. Números 1, 2, 3 em todo slide cansaram: no último, bolinha. A consequência foi destacada à parte em fundo vermelho; no 224 o user pediu o oposto (junto do parágrafo). Pedido de "mais profissional" sobre layout já aprovado: o redesenho foi reprovado ("Volta ao padrão antigo, e dê finos ajustes").
- **28/09, 152:** o diagrama "entra oportunidade, a máquina gira e sai venda" pareceu "muito amador": cada quadro tem que se explicar sozinho.
- **26/09, kit:** um ícone de traço aberto (aperto de mão) pareceu "cortado"; daí o kit curado em `icones/`.
