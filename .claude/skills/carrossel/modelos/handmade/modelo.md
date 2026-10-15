# Modelo: Handmade (desenho a lápis, perfil Tatsuo Academy)

**Em uma linha:** carrossel desenhado "à mão": traço de lápis grafite levemente tremido, bonecos de palito em traço mínimo, setas e rabiscos, letra manuscrita Kalam, caneta e marca-texto só no vermelho `#A91C20`. Parece alguém explicando no papel.

> Criado em 14/10/2026 com o user, a partir de 3 direções de teste (A caderno quadriculado, B folha lisa, C folha presa na mesa). Primeira peça publicada: 237 "time sem treino" (14/10), que é o exemplo de referência deste modelo. Voz: a da Tatsuo Academy dos posts educativos (ver o modelo infográfico, seção 2, e a regra "apostila é fonte, não texto"). Não sobrescrever.

## 1. Quando usar
- **Canal:** feed do Instagram, perfil da **Tatsuo Academy**. Sem `/etiqueta` e sem Manychat; CTA = link da bio pro MBV.
- **Objetivo:** levar UMA ideia de gestão por uma analogia do cotidiano (no 237, o time de futebol que não treina), com o desenho guiando a leitura.
- **Quando NÃO usar:** post do Hélio com dor ácida e foto (editorial-punch, fotos-reais); dado denso com muitos números (infográfico, layout G).

## 2. Texto (a copy vem ANTES do desenho)
- **Ordem obrigatória:** escrever a copy inteira, passar no CHECKPOINT 1, e só depois pensar o desenho de cada slide. O desenho se adapta ao texto, nunca o contrário. Pensar desenho junto com a copy deixou o texto "jogado e nada amarrado" na v1 do 237 (reprovada).
- **Storytelling, não apostila:** a analogia vira cena (o time que só se encontra no vestiário, dez minutos antes do jogo) e cada slide puxa o seguinte. Passagem entre slides amarrada: o fim de um slide abre o próximo ("E o pior: ele está aprendendo" → "E você deixa, porque...").
- **Dedo na ferida pela dor:** a peça aperta a dor ancorada no que o dono valoriza (o cliente que levou anos pra conquistar, o tempo dele apagando incêndio), nunca o caráter dele.
- **Capa:** usa a própria analogia pra provocar, em uma frase que o dono sente na hora. Aprovada no 237: "Você cobra gol de um time / QUE NUNCA TREINOU." Reprovada por fraca: "Seu funcionário está treinando agora / COM O SEU MELHOR CLIENTE" (frase solta, sem a analogia).
- **Português falado:** frase inteira, fluida, sem o vício do ponto final picotando tudo. Pode a fala de empresário ("E amigão, empresa pequena não tem dinheiro pra pagar funcionário sênior, não").
- Corpo até ~180 caracteres por slide. Interlocutor: o dono de PME ("você", "sua empresa"). Oferta promete gestão (MBV).

## 3. Formato
- 1080 × 1350, 8 a 11 slides (o 237 tem 11: capa, 9 de história e CTA).

## 4. Fundos (decidir slide a slide ANTES de desenhar)
- **Slide de texto ou desenho simples** (bonecos, setas, objetos): **B, folha lisa** (#F4F1EA com grão leve).
- **Slide com gráfico, eixo, escala ou tabela:** **A, caderno quadriculado** (grade 44 px #dedad0 + margem vermelha a 55% de opacidade). A grade serve de régua pro olho; em slide de texto ela atrapalha a leitura.
- **Capa:** **C, folha presa com fita sobre o preto** (#0f0f0f, folha levemente girada, sombra). No CTA, C é opcional (o 237 usou).
- Nunca alternar C no meio do carrossel (o arrastar parece outro post). No máximo dois tipos de fundo no miolo (A e B).

## 5. Diagramação do texto (dois blocos, não um paredão)
- **Slides do miolo em dois blocos:** a parte da história em cima (Kalam 400, 42 px, a partir de y ≈ 140), o desenho no meio, e o punch embaixo (Kalam 700, 46 px, `bottom: 150px`). Um bloco único de texto em cima e o desenho embaixo deixou a leitura maçante (reprovado no 237).
- **Marcações a lápis, no máximo UMA por bloco** (mais que isso vira caderno de estudante e nada se destaca):
  - sublinhado vermelho a lápis (`<span class="u">`) na expressão que segura a história ("dez minutos antes do jogo", "em meia hora");
  - marca-texto vermelho (`<span class="mk">`) no trecho que dói, no punch ("anos pra conquistar", "deixa acontecer");
  - palavra circulada (`<span class="o">`) quando o dono entra em cena ("quem entra em campo é você");
  - sublinhado duplo (`<span class="u2">`) com o punch todo em vermelho, uma vez por carrossel no máximo ("Toda semana, o mesmo incêndio.").
- A pontuação colada na palavra circulada vai dentro do span (`você.`), senão o círculo atravessa a vírgula.

## 6. Desenho
- **O desenho nunca escreve o que o texto do slide já disse.** Rótulo e balão acrescentam informação ou dão voz à cena: "cliente há 15 anos" (o texto diz "levou anos pra conquistar"), o funcionário pensando "o chefe resolve", o celular com "cliente chamando", "dia 1 → dia 180", "não cabe no seu caixa". Reprovado no 237: "10 min pro jogo", "o mesmo incêndio", ciclo "ele erra → você resolve" repetindo o texto palavra por palavra. Se o rótulo só repete, troca por cena (no 237, a conta "ensina + repete" virou um quadro de 4 semanas marcado e o dono dizendo "isso!").
- **Ambiente quando a analogia pede:** o campo com gol, área, cones e o time trocando passe; o balcão; o vestiário. Boneco solto no papel em slide que fala do campo ficou sem graça (slide 10 do 237, corrigido).
- **Traço:** rough.js (roughness ~1.5, bowing ~1.5) + filtro de lápis (feTurbulence + feDisplacementMap 2,2 + blur 0,35); grafite #3a3a3a.
- **Vermelho `#A91C20` só como caneta:** setas, círculo rabiscado em volta de quem importa na cena, X, foguinho, marca no quadro. Nunca outro vermelho.
- **Bonecos de palito em traço mínimo:** cabeça em círculo, corpo e membros em linha, sem rosto e sem roupa. Poses: neutro, acena, corre, aponta, braços abertos, mãos na cabeça (perdido), apito, segura, carrega (braços pra cima segurando pilha), relax e sentado.
- **Gráfico (fundo A):** eixos a lápis, uma linha em vermelho (o que dói) e uma tracejada em grafite (o certo), rótulos manuscritos com setas.
- O desenho fica centrado no espaço entre os dois blocos de texto, com folga de pelo menos ~80 px pra cada bloco. Sem paginação. Área de segurança 90/110 px (como o infográfico).

## 7. Código (reaproveitar, não reescrever)
- `lib.js` — a biblioteca de desenho (objeto `H`): `boneco`, `arrow`, `rabisco`, `xis`, `balao`, `chama`, `relogio`, `celular`, `campo`, `balcao`, `cone`, `bola`, `text`, e `decorar()`, que desenha a lápis as marcações `.u`, `.u2` e `.o` medindo as palavras na página.
- `render.js` — gera os PNGs: `node .claude/skills/carrossel/modelos/handmade/render.js <pasta-do-post>/instagram [slide-01.html ...]`. Espera as fontes e o desenho terminarem.
- Ponto de partida de cada post: copiar `conteudo/carrosseis/237_time-sem-treino/_scripts/build.py` (template da página, fundos A/B/C, folha da capa, CSS dos blocos `.P`/`.P2` e das marcações) e trocar só os textos e os desenhos. Cada slide é `S[n] = (fundo, corpo_html, script_js, deslocamento)`; o deslocamento `dy` ou `(dx, dy)` move o desenho inteiro pra centralizar entre os blocos.
- Precisa de internet na renderização (Kalam do Google Fonts e rough.js do jsDelivr).
- O traço tem semente fixa (`seed` sequencial no `lib.js`): o mesmo script gera sempre o mesmo desenho, então ajuste num slide não muda o traço dos outros. Os PNGs postados do 237 são de antes da semente; re-renderizar o 237 dá traço levemente diferente (os oficiais estão em `instagram/`).
- `referencia-testes-build.py` — os testes de estilo de 14/10 (só histórico).

## 8. Fechamento
- Penúltimo slide = a lição na voz do dono ("O seu time vai evoluir exatamente pra onde você treinar."). Último = CTA do MBV (link na bio): "No MBV, imersão de três dias para donos de pequenas e médias empresas, você aprende gestão[, inclusive gestão de X,] nos três pilares: Lucratividade, Crescimento e Cultura." + botão desenhado à mão "QUERO PARTICIPAR DO MBV" + seta + "link na bio".
- Legenda fluida na voz da Tatsuo Academy (o 237 tem ~1300 caracteres), amplia a reflexão, fecha com o CTA e "Seja Bem-Vindo ao Fim do Analfabetismo Empresarial."

## 9. Aprendizados
- 14/10: o user escolheu B (letra e fundo) como base, A só onde tem gráfico, C só na capa; bonecos em traço mínimo.
- 14/10 (237): copy antes do desenho; capa com a analogia; desenho que acrescenta e não repete; ambiente do campo; texto em dois blocos com uma marcação por bloco. Ideia de longo prazo: versão em motion (o traço se desenhando enquanto o Hélio fala), ainda não feita.
