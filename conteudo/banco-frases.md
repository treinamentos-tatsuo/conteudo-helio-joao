# Banco de frases — fila de candidatas do formato /frase

> Fluxo: Claude gera candidatas em lote (método e crivo na skill `/frase`, seção 2) → o user
> **aprova / descarta / ajusta** → aprovada entra na fila → feita vira post. A medição é da
> máquina de análise: a ficha do post fica no `conteudo/analise/registro-posts.csv` (via
> `/etiqueta`) e o `/ritual` fecha cada frase em D+7 pelos compartilhamentos absolutos contra a
> régua viva. Nada aqui chama a API do Instagram (CLAUDE.md). Os status antigos com taxa
> (shares/alcance) ficam como registro da régua anterior.
>
> Status possíveis: `candidata` · `aprovada` · `feita (post N, publicado DATA (dia) ~hora; ...)` ·
> `publicada (post N, DATA)` (entradas antigas) · `descartada (motivo)` · `stand-by`.
> Regra de símbolo: cada frase publicada usa um símbolo visual INÉDITO (não repetir o mar,
> o samurai, o semeador).

## Os dois formatos (estratégia de alternância — user, 2026-08-14)

> **Caiu em 26/08/2026** (nunca nichar: a frase é universal e a empresa só entra na legenda;
> reconfirmado em 10/09 e 24/09). Fica como registro; não alternar.

- **LEI OBSERVADA (filosófica):** princípio universal observado da realidade/natureza,
  metafórico, que ensina pra vida. Ex: "A água nunca vence a pedra pela força", "No raso
  não existe pressão". A imagem É o princípio. Ver adendo na `diretriz-frase-legenda.md`.
- **EMPRESARIAL DIRETA:** confronto/verdade da vida do dono, sem metáfora de natureza.
  Ex: "Gente boa não se demite da empresa. Se demite do dono."
- Alternar os formatos nos dias da semana; o calendário mistura os dois.

## Fila de produção (aprovadas pelo user em 2026-08-14)

### A. O peso procura quem aguenta. — `publicada (post 42, 2026-08-18 — reach 251,5k · 3.405 shares, 1,35%, em 25/08)`

- **Formato:** lei observada (fronteira com a empresarial). **Veia:** pressão/peso (nº 1).
- **Mecanismo:** consagração — quem vive sobrecarregado se reconhece escolhido pelo peso, não vítima. Segunda camada: elogio e sentença ao mesmo tempo (aguentar atrai mais peso).
- **Slide:** vermelho em "quem aguenta" (confirmado pelo user). **Símbolo (FINAL):** a **ruína** — câmera rente ao solo, uma única coluna dórica de pé sustentando a arquitrave inteira, todas as outras em tocos e tambores quebrados no chão, névoa. É a `img-01`, a **primeira geração**, salva no banco como `370.png`.
- **Decisão do user (2026-08-17):** depois de 26 versões perseguindo humanização da rocha (silhueta, pareidolia, corpo de blocos, aérea sem chão), voltar à primeira imagem. Nenhuma superou a leitura limpa do símbolo original.
- **Aprendizado de processo:** quando a primeira geração já entrega a lei, humanizar tende a **competir** com ela em vez de somar. Reconhecer o acerto de primeira e parar.
- **Aprendizados técnicos que ficam** (detalhe no `carousel-text.md` do post 42): escala e enquadramento se resolvem em CSS, conteúdo em geração; image-edit aceita pedido concreto ("mover braço") e ignora ou destrói pedido de dosagem ("mais sutil"); mapear um bloco por membro produz manequim articulado; e figura de rocha **sem feição no rosto** é o que segura a peça — dar traços de rosto quebra.
- **Legenda:** fecha a brecha da interpretação burra (regra 26) — aguentar tudo não é virtude, é diagnóstico de centralização; o limite do dono vira o limite da obra.

### B. Gente boa não se demite da empresa. Se demite do dono. — `publicada (post 43, 2026-08-19 — FLOP: reach 6,9k · 35 shares, 0,51%, em 25/08)`

- **Formato:** empresarial direta (usar nos dias de veia empresarial). **Veia:** time/pertencimento + confronto ao dono.
- **Mecanismo:** polêmica defensável (pessoas deixam chefes, não empresas) com a culpa voltando pro dono — molde dos hits de 22k e 18k shares. Legenda fecha a brecha: é sobre o que o dono controla.
- **Slide:** 2 linhas em 38px, vermelho na 2ª linha inteira ("Se demite do dono."). **Símbolo (final):** duas **cadeiras de escritório** frente a frente numa sala de escritório vazia, uma ainda no lugar e a outra empurrada e girada de costas, ambas vazias, carpete com marcas de rodízio, sombras de persiana riscando o chão, câmera na altura do assento. A tese virando imagem sem personagem — quem sai se despede de quem estava do outro lado, não do prédio. A mesa com crachá (ideia original do banco) foi descartada; a primeira geração em cadeira de madeira/sala residencial foi trocada por ambiente corporativo a pedido do user, que casa melhor com a entrevista de saída da legenda.

### C. Quem nunca perde, também nunca ganha. — `publicada (post 41, 2026-08-15 — reach 37,9k · 288 shares, 0,76%)`

- **Formato:** lei observada. **Veia:** jogo/risco — eco do maior post da história (38k, arquibancada) destilado em lei universal, sem cenário.
- **Mecanismo:** paradoxo — o leitor que nunca perdeu descobre que isso não é mérito, é ausência de jogo. Original do lote ("A arquibancada nunca perde. Também nunca ganha.") foi enxugada pelo user pra forma de lei.
- **Slide:** toda em preto (confirmado pelo user; terceiro post seguido em preto). **Símbolo (ideia do user, final na v6):** "A arquibancada envelhece limpa" virou a imagem — câmera um palmo acima da lona, ringue manchado de luta à direita, corredor vazio centralizado fugindo pra névoa, arquibancada limpa e vazia à esquerda, pesos iguais, sem figura humana (`img-06.png`, slide `slide-01-lateral`).

## Lote 2 — formato LEI OBSERVADA (todas APROVADAS pelo user em 2026-08-14)

### 4. A raiz decide o que o vento leva. — `publicada (post 47, 2026-08-21 — FORTE: reach 96,1k · 1.259 shares, 1,31%, em 25/08)`

- **Lei (tese REALINHADA pelo user, 2026-08-20):** o vento é DISTRIBUIDOR, não ameaça — ele carrega o que a árvore dá (semente ou folha morta), e o que sai de você e chega ao mundo é decidido pela raiz, por aquilo que ela bebe (valores). "Você espalha o que você nutre; espalha o que você é." Frutos fartos não nascem de raiz nutrida de futilidade. A leitura tempestade (raiz segura a árvore) é camada secundária, só menção na legenda.
- **Slide:** 1 linha 44px, vermelho em "A raiz". **Símbolo (FINAL, v8):** copa de macieira carregada entrando pela esquerda, deriva esquerda→direita de folhas e frutos em rajada IRREGULAR (alturas e ângulos diferentes), só névoa atrás e abaixo — sem chão (evita "árvore anã", erro da v6) e sem trilha arrumada em perspectiva (v7, rejeitada por "artificial demais"). Aprendizado: dispersão bonita demais entrega montagem; realismo documental pede imperfeição. 8 versões no total, todas em `imagens/`. Mask padrão 26%.
- **Legenda (FINAL):** alongada, ajustada à mão pelo user e fechada com a pergunta-espelho ANTES do fecho ("E você, o que está nutrindo?" → frase dá a última palavra, regra 31). 2.120 chars — margem de só 80 pro limite do IG. Tríade de punches fruto/tronco/semente completada com "Semente que vira árvore não sai de raiz que se alimenta de aparência." Regra aprendida: um punch por parágrafo, desenvolvido antes de fechar.

### 5. O inverno não pergunta o que você plantou. — `publicada (post 48, 2026-08-20 — reach 13,7k · 117 shares, 0,85%, em 25/08)`

- **Lei:** a estação chega igual pra todo mundo; a diferença é a reserva de quem plantou. Ensina: consequência e preparo, sem moralizar.
- **Slide:** 2 linhas 38px, vermelho em "não pergunta". **Símbolo (FINAL, aprovado em conceito e gerado de primeira):** "Restolho na geada" — câmera rente ao solo, fileiras de restolho de colheita cobertas de geada convergindo num corredor central até o celeiro pequeno na bruma do amanhecer, sol pálido atrás da névoa. Une o símbolo original do banco à composição de profundidade.

### 6. Só a água parada cria lodo. — `publicada (post 38, 2026-08-14 — reach 36,3k · 200 shares, 0,55%)`

- **Lei:** corrente não conhece lodo; estagnação apodrece por natureza. Ensina: movimento/constância (parente da "água e pedra" citada pelo user).
- **Slide:** vermelho em "parada". **Símbolo:** lagoa imóvel e turva na neblina, galho seco caído.

### 7. A maré não espera barco pronto. — `publicada (post 39, 2026-08-17 — reach 59,4k · 528 shares, 0,89%)`

- **Lei:** a janela abre e fecha pela natureza, não pela sua prontidão. Ensina: timing/ação — o preparo eterno é uma forma de ficar em terra.
- **Slide:** vermelho em "não espera". **Símbolo:** barco encalhado na areia com a maré baixando ao fundo, na névoa.

### 8. A colheita é obrigatória. — `publicada (post 40, 2026-08-16 — reach 32,6k · 251 shares, 0,77%)`

- **Origem:** era variante da frase do inverno; desmembrada pelo user (2026-08-14) como frase própria da fila (opção 7 da fila de produção).
- **Lei:** a colheita vale pro bem e pro mal — colhe-se o que se plantou, inclusive o nada. Ensina: consequência inevitável, sem moralizar.
- **Slide:** vermelho em "obrigatória" (user voltou ao vermelho após dois posts todo preto). **Símbolo:** carroça carregada de trigo voltando pela estrada de sulcos na névoa (lado positivo da lei). Versão alternativa ceifeiro com foice gerada e guardada (`40_colheita/imagens/img-02-ceifeiro.png`) — user gostou da leitura morte/medo, escolheu a carroça.

## Lote 3 — candidatas (2026-08-21, aguardando crivo do user)

> As três primeiras vieram de frases trazidas pelo próprio user (adaptadas pra caber no slide
> e ganhar densidade); as quatro seguintes são novas, miradas nas veias do `o-que-funciona.md`.

### 9. Poucos homens caem por fraqueza, a maioria afunda devagar, fingindo que está de pé. — `publicada (post 53, 2026-08-22 — reach 13,6k · 122 shares, 0,90%, em 25/08)`
- **Origem:** user. Decisão do user (2026-08-21): usar a frase ORIGINAL na íntegra (a versão enxuta "Quase ninguém cai. A maioria afunda de pé." fica descartada).
- **Formato:** fronteira lei/empresarial. **Veia:** pressão/dor + orgulho (nº 1).
- **Slide:** 2 linhas 38px, **toda em preto** (decisão do user pras três do lote). **Símbolo (FINAL, v3):** a estátua que o chão engole — estátua inteira de estadista, inclinada ~10° com física real, engolida até o tornozelo pela lama encharcada com lâmina d'água (`53_afunda-de-pe/imagens/img-03.png`). v1 (terno na água) descartada por literal demais; conceito escolhido entre 3 (casa no pântano / estátua / árvore morta de pé).

### 10. O verdadeiro peso de um ser é a lacuna entre quem ele é e quem ele sabe que deveria ser. — `publicada (post 54, 2026-08-24 — D+1: reach 7,6k · 56 shares, 0,73%; maturação D+3 ≈ 27/08)`
- **Origem:** user, na íntegra; em 2026-08-24 trocou "um homem" → "um ser" (ampliar além do masculino; legenda em "você" pela mesma razão).
- **Formato:** lei observada (peso interno). **Veia:** pressão/peso (nº 1) — sequência do post 42 por outro ângulo.
- **Slide:** 2 linhas 38px, toda em preto. **Símbolo (FINAL, v11 de 11 — caça recorde):** o bloco de mármore intacto com martelo e talhadeira empoeirados na base, escala humana, luz rasante dramática (`54_peso-da-lacuna/imagens/img-11-bloco-drama.png`). Aristóteles/Michelangelo: quem ele deveria ser está dentro da pedra; a cobrança silenciosa é a poeira nas ferramentas. Método novo que fechou: PRIMEIRO a sensação (cobrança silenciosa), depois o símbolo — detalhes no `carousel-text.md`.

### 11. Um idiota em movimento chega mais longe que um gênio parado. — `publicada (post 55, 2026-08-23 — reach 40,0k · 497 shares, 1,24%, em 25/08 — D+2, subindo)`
- **Origem:** user, na íntegra.
- **Formato:** paradoxo/confronto. **Veia:** movimento/ação — atenção: veia mais fraca do lote 2 (água parada, 0,55%), mas aqui o confronto idiota×gênio pergunta ao leitor qual ele é.
- **Slide:** 2 linhas 38px, toda em preto. **Símbolo (FINAL, v4 — IDEIA DO USER):** a pedra quadrada rolando — cubo desgastado de perfil em pleno tombo (esq→dir), poeira no contato, lascas das quinas no rastro, chão limpo (`55_idiota-em-movimento/imagens/img-04-pedra-rolando.png`). "A cada tombo se lapida": o movimento é o escultor — fecha com o fim da legenda ("andando, deixa de ser"). Fecho da legenda também do user: "Sejamos Idiotas."

### 16. Se você olha demais para um abismo, o abismo também olha para dentro de você. — `publicada (post 56, 2026-08-25 12:37 — D+2 em 27/08: reach 6,9k · 38 shares, 0,54%; ficha retroativa SEM previsão, fora do placar — FECHADA D+7: 5.33 shares/1k · alcance 8250 · nao-pontua)`
- **Origem:** Nietzsche (*Além do Bem e do Mal* §146), versão do user — "demais" no lugar de "longamente" (planta o excesso como problema), mantido "olha para dentro de você" da tradução clássica. Citação famosa: reconhecimento joga a favor do share.
- **Formato:** lei filosófica. **Veia:** pressão/medo (nº 1). Direcionamento: a atenção esculpe quem você é — o que você encara tempo demais passa a morar em você; empresário só num parágrafo da legenda.
- **Slide:** 2 linhas 38px, **toda em preto**. **Símbolo (FINAL, img-10):** POV de dentro do abismo, minimalista/escultural, sem névoa — paredes escuras lisas em silhueta, homem debruçado na borda curva visto de baixo, céu branco. A foto É o abismo olhando de volta.
- **Aprendizado (2026-08-24):** as 3 primeiras gerações foram rejeitadas por "poluídas" — geologia/textura/entulho competindo com a frase. A chave que o user validou: superfícies lisas, abismo como forma negra limpa quase gráfica, um elemento só, critério "pintor/escultor" (a imagem diz a frase sozinha, sem parecer cenário genérico que serve a qualquer frase). Zoom no rosto testado e revertido; versão sem o homem testada e rejeitada (sem figura não há relação de olhares nem escala).

### 12. Nenhuma lâmina nasce fria. — `candidata`
- **Formato:** lei observada. **Veia:** pressão/fogo (nº 1). Coerência de marca (lâmina ↔ Tatsuo) sem repetir o samurai do post 35.
- **Símbolo (ideia):** forja escura, ferreiro de costas ao fundo, lâmina incandescente na bigorna como única luz, fagulhas.

### 13. Toda empresa cresce até bater no dono. — `candidata`
- **Formato:** empresarial direta. **Veia:** confronto ao dono (molde dos hits de 22k/18k) — o teto da empresa é ele.
- **Símbolo (ideia):** árvore dentro de estufa de vidro pequena demais, copa prensada contra o teto de vidro, névoa fora.

### 14. Farol não persegue navio. — `candidata`
- **Formato:** lei observada. **Veia:** posicionamento/liderança — referência atrai, perseguidor se apaga. Segunda camada larga (cliente, talento, autoridade).
- **Símbolo (ideia):** farol solitário no penhasco, facho cortando a bruma, mar vazio.

### 15. Todo atalho cobra pedágio. — `publicada (post 59, 2026-08-27 10:08 — maturação D+3 ≈ 30/08; previsão: mediana, 90-350 shares — FECHADA D+7: 9.04 shares/1k · alcance 51451 · acertou)`
- **Formato:** lei observada. **Veia:** escolha/consequência — o desconto do atalho é empréstimo.
- **Mecanismo:** ADVERTÊNCIA (grupo 2 do H11) — escolha consciente do user em 27/08, ciente do teto de ~0,9%. Recusou as viradas de autodeclaração propostas ("Quem paga o pedágio chega inteiro." e o dístico "Todo atalho cobra pedágio. / Quem paga na entrada chega inteiro.").
- **Cotidiano:** passa no teste do lote 4 — pedágio, estradinha de terra e suspensão quebrada são causo de qualquer brasileiro. O símbolo antigo do banco (trilha morrendo num barranco) era do tipo distante e foi abandonado.
- **Slide:** 1 linha 44px, **toda em preto** — o vermelho em "pedágio" foi renderizado e descartado pelo user: brigava com as listras da cancela (dois elementos de alto contraste no mesmo quadro). *Aprendizado: quando o símbolo já é gráfico e listrado, o vermelho vira ruído.*
- **Símbolo (FINAL, img-01, primeira geração, conceito 1 de 3):** a cancela sozinha — câmera rente ao chão na estradinha de terra sulcada sumindo na névoa, cancela de pedágio listrada baixada sobre dois postes, sem guarita, sem cobrador, sem ninguém. Sem scale. Descartados: bifurcação asfalto × terra (asfalto leu como vicinal) e guarita no descampado (ilustra o pedágio, não o atalho).
- **Legenda:** espinha do gabarito raso, 1.726 chars; fecha a brecha da regra 26 (atalho ≠ eficiência — eficiência corta o desnecessário, atalho deixa de pagar o necessário), que é por onde o método da Academy entra orgânico.

## Lote 4 — crivado pelo user em 2026-08-26

> Crivo trouxe um CRITÉRIO NOVO (vale pra todas as frases daqui em diante): além de
> universal e autodeclaração positiva, o causo precisa ser **COTIDIANO DO BRASILEIRO** —
> todo mundo tem prateleira em casa e já viu vergar; quase ninguém usa mapa, sobe montanha,
> frequenta forja ou farol. Símbolo distante da realidade = frase fraca mesmo com abordagem
> certa. E a frase precisa de "molho" (tensão/graça na formulação). Nichamento a empresário
> mata o post (H12 reformulada). Resultado: só a 17 sobreviveu; o lote 5 substitui as demais.

### 17. Prateleira vazia não verga. — `publicada (post 57, 2026-08-26 — maturação D+3 ≈ 29/08; img no banco: 374.png)`
- **Formato:** lei observada. **Veia:** pressão/peso (nº 1) — sequência dos dois maiores do formato (37 e 42) por símbolo inédito.
- **Mecanismo:** autodeclaração — vergar deixa de ser vergonha e vira prova de carga: quem verga é quem sustenta. Segunda camada: vergar ≠ quebrar; quem nunca vergou nunca sustentou nada.
- **Slide:** 1 linha 44px, **toda em preto** (user). **Símbolo (FINAL, img-01, primeira geração):** user trocou o contraste de duas prateleiras pelo conceito 3 — **curva escultural** (linha do post 56): close de uma única prateleira antiga carregada de sacas de feijão e potes de vidro, vergada em arco pronunciado contra parede de reboco clara, sem figura humana. Sem scale no slide (crop cortaria as pontas da curva).
- **Legenda:** espinha do gabarito raso; fecha a brecha da regra 26 (vergar segura, vergar demais racha — sobrecarga pede apoio, não coragem); pergunta-espelho antes do fecho; frase dá o ponto final.

### 18. O forno não cria rachadura. Ele revela. — `descartada (user 26/08: clichê demais)`
- **Formato:** lei observada (lei real da cerâmica: a peça racha no forno onde a mão falhou na modelagem). **Veia:** pressão/prova (nº 1).
- **Mecanismo:** autodeclaração de quem já passou no fogo + confronto suave (a crise não quebra nada que estava inteiro — ela mostra onde já estava quebrado). Legenda fecha a brecha: o forno não é vilão, é revelador.
- **Símbolo (ideia):** olaria escura, vasos de barro; um vaso rachado com a luz do forno vazando pela rachadura como única fonte de luz.

### 19. O mapa não sobe a montanha. — `descartada (user 26/08: abstrata/distante da realidade do brasileiro; a IDEIA ação>estudo é boa e pode voltar com causo cotidiano)`
- **Formato:** lei observada. **Veia:** movimento/ação — cavalgando o resultado do post 55 (1,24%).
- **Mecanismo:** dois grupos (quem estuda × quem sobe) + autodeclaração de quem está na subida, cansado e sujo. **Atenção regra 26:** a Tatsuo vende método — a legenda precisa fechar a brecha "então estudar não serve": o mapa importa, mas não substitui a subida; sem mapa se sobe a montanha errada.
- **Símbolo (ideia):** mapa aberto esquecido sobre um marco de pedra em primeiro plano, trilha fugindo centralizada pra montanha na névoa ao fundo.

### 20. Canteiro limpo é obra parada. — `descartada (user 26/08: falta "molho")`
- **Formato:** fronteira lei/empresarial. **Veia:** movimento/construção.
- **Mecanismo:** autodeclaração — consagra a poeira, o barulho e a bagunça de quem está construindo; empresa arrumada demais é empresa parada. Segunda camada: a fase suja É a fase viva.
- **Símbolo (ideia):** canteiro de obra na névoa da manhã, andaimes, poeira suspensa na luz rasante, sem figura humana (ou silhuetas ao fundo).

### (12.) Nenhuma lâmina nasce fria. — `descartada (user 26/08: forja é distante da realidade; ideia renasce cotidiana na 22 do lote 5)`

### (14.) Farol não persegue navio. — `descartada (user 26/08: distante da realidade + forçado; "posicionamento" não é vocabulário do Hélio em post de frase, cujo intuito é fazer refletir)`

### (13.) Toda empresa cresce até bater no dono. — `descartada (user 26/08: nichada a empresário — exatamente o erro do post 43; teste da H12 cancelado, ver hipoteses.md)`

## Lote 5 — cotidiano brasileiro (TODAS APROVADAS pelo user em 2026-08-26)

> Completam a semana com a 17 (prateleira). Todas: princípio universal + autodeclaração
> positiva (H11) + causo cotidiano que qualquer brasileiro já viveu + molho na formulação.
> Zero vocabulário de nicho.

### 21. Sem pressão, o feijão não cozinha. — `publicada (post 65, 2026-08-28 — FECHADA D+7 em 04/09: reach 1,28M · 10.665 shares · 8,34 shares/1k = MEDIANA; previu acima 9,0-13,0 → errou pra baixo. 5º maior alcance da conta; a veia compra distribuição, não intensidade)`
- **Slide:** 1 linha 44px, toda em preto. **Símbolo (FINAL, img-01, primeira geração, conceito 1 de 3):** panela de pressão de alumínio amassada no fogão, jato de vapor no pino, parede encardida quase preta atrás, sem figura humana. *O vapor se dissolvendo no papel virou a transição do slide sozinho — técnica reutilizável: elemento que já é vapor/fumaça/poeira resolve o degradê sem depender do mask.* Imagem subida a pedido do user via `object-fit:cover` em `bottom:0` (reenquadra sem distorcer; v1 guardada).
- **Legenda (2.075 chars, versão A):** dois fechos de brecha pra não virar "sofra mais" — a VÁLVULA (pressão contida E com saída; apertar time sem caminho de saída é estourar gente) e a PANELA VAZIA, acrescentada pelo user, que separa estar sob pressão de estar cozinhando algo ("o apito não prova que tem feijão dentro; prova que tem fogo embaixo").
- **Palpite do user registrado antes do resultado:** "vai ser tão boa quanto a da pressão" (post 37). Convergência: o 37 fez 11,84 shares/1k, dentro da faixa prevista. Intuição e máquina concordam na taxa.
- **Veia:** pressão (nº 1) — eco do hit gigante (37) por símbolo de dentro de casa: a panela de pressão. Lei literal da cozinha brasileira: feijão cru até existir pressão.
- **Mecanismo:** autodeclaração — "a pressão que estou sentindo é o que está me deixando pronto". Segunda camada: sem pressão nada fica pronto; pressão não é castigo, é cozimento.
- **Símbolo (ideia):** panela de pressão antiga no fogão, vapor saindo forte do pino como única coisa em movimento, cozinha simples na luz de janela.

### 28. A pedra é o que amola a faca. — `publicada (post 76, 2026-09-01 — FECHADA D+7: 11.83 shares/1k · alcance 83945 · errou-pra-cima)`
- **Origem:** reformulação do user (31/08) em cima da semente 22. A 22 punha o leitor como faca que apanhou; esta põe a **pedra como sujeito** — os obstáculos, dificuldades e problemas são as pedras, e são eles que amolam a pessoa.
- **Formato:** lei observada. **Veia:** pressão/dor (nº 1) — ângulo do AGENTE, não do processo (o feijão/65 já fez "pressão cozinha"; repetir nervo com ângulo novo, nunca a tese).
- **Slide:** 1 linha 44px, toda em preto. **Símbolo (FINAL, img-03 de 3, pedido do user):** pedra de amolar escavada funda no meio por anos de uso, molhada, numa bancada de madeira crua; faca deitada ao lado com a **lâmina prateada e espelhada** e cabo escuro; gota caindo da bancada; cercado e casa na névoa. Sem figura humana, sem scale.
- **Caça (3 gerações):** img-01 só a pedra (cava dramática, provava só o preço) → img-02 faca com gume escuro (a faca funcionou, mas a cava virou ondulação) → **img-03** as duas coisas juntas: *a pedra perdeu o meio, a faca ganhou o fio*, a única que conta a troca inteira sem texto. Nota técnica: lâmina clara sobrevive ao `multiply` por estar apoiada na madeira escura (regra do véu d'água do 38).
- **Legenda (1.358 chars):** abre pela lei física — amolar TIRA material, e é por perder que o fio aparece — pra impedir que vire "sofra que você melhora". Beat do comportamento em registro de cozinha (faca cega ainda passa em pão, manteiga e queijo; **só não encara mais osso** — "é osso" = é difícil, escolha do user, o idioma faz a ponte sem explicar). Anti-burro sem se anunciar: pedra sozinha não afia, o que separa afiar de estragar é a **inclinação da mão**. Fecho-espelho: "está saindo mais cortante ou só mais fino?".
- **Mecanismo:** consagração pelo obstáculo. Segunda camada (só na imagem): quem afia se gasta afiando.
- **RESSALVA REGISTRADA ANTES DE PUBLICAR — é um teste deliberado do user.** A frase é lei centrada em OBJETO e **não nomeia o leitor**. Pela leitura do espelho isso a põe na faixa mediana: as frases que nomeiam ("quem aguenta", "quem divide", "no raso") rodaram 10,4–13,5 shares/1k; as de objeto (água parada, maré, inverno, colheita) rodaram 5,1–8,9 e nenhuma passou de 9. Foram oferecidas três alternativas que corrigiam isso; o user manteve a própria formulação **explicitamente pra testar a regra**. Se furar a banda mediana, a regra do espelho tem um problema e a gente quer saber.
- **Ressalva 2 (a imagem pode puxar junto):** a cava funda dá ao post uma segunda camada que a frase sozinha não tem — quem compartilha pode estar declarando "eu já fui pedra de alguém" sem a frase dizer isso. A previsão não foi mexida por causa disso; fica anotado pra hora de ler o resultado.
- Sem CTA, sem palavra-chave, sem Manychat — peça de furar a bolha.

### 22. Toda faca afiada já apanhou da pedra. — `feita (absorvida pela 28 → post 76, 2026-09-01)`
- **Veia:** dor/preparo (nº 1) — a ideia da lâmina/forja (12) renascida no quintal brasileiro: a pedra de amolar.
- **Mecanismo:** autodeclaração — quem está apanhando se reconhece sendo afiado, não destruído. Segunda camada: o corte que você admira em alguém custou pedra; ninguém nasce afiado.
- **Símbolo (ideia):** pedra de amolar molhada e gasta em primeiro plano, faca de cozinha deitada sobre ela, fio de água, mãos de trabalho fora de foco ou ausentes.

### 23. Ladeira só pesa pra quem sobe. — `publicada (post 70, 2026-08-29 — FECHADA D+7: 9.80 shares/1k · alcance 118057 · acertou)`
- **Slide:** 1 linha 44px, toda em preto. **Símbolo (FINAL, img-03 de 3, conceito 1 de 3):** ladeira de paralelepípedo íngreme vista do pé, câmera rente à pedra, muros lisos e nus de topo ESCALONADO, calçadas em lances de degraus, figura pequena de costas inclinada na crista, tudo sumindo na névoa. Sem scale.
- **Caça (3 gerações) — aprendizado técnico:** as duas primeiras eram limpas e bonitas mas liam como CORREDOR PLANO (paredes convergindo pra ponto de fuga na altura do olho = perspectiva de rua plana). Pedir "mais íngreme" na v2 não resolveu. *Inclinação se prova com DEGRAU, não com ângulo:* topo de muro escalonado + escadaria lateral denunciam a subida sem sujar a cena.
- **Legenda (1.596 chars):** entra pela porta de trás (quem desce jura que a ladeira é curta), abre o terceiro grupo — quem está parado no ponto, pra quem a ladeira nem existe — e fecha a brecha do "quanto mais pesado, melhor" com cena e fato seco, sem anunciar a ressalva: quem chega arrasada há dez anos e não subiu um metro. Espelho: "está subindo ou só está cansado?".
- **Veia:** peso/cansaço (nº 1) — o mecanismo do maior post da história (cansaço = prova de estar no jogo) num cenário que toda cidade brasileira tem.
- **Mecanismo:** dois grupos (quem sobe sente; quem olha de baixo, não) + autodeclaração: "tá pesado porque estou subindo". Segunda camada: se nada pesa, você está descendo ou parado.
- **Símbolo (ideia):** ladeira de paralelepípedo subindo e sumindo na névoa, câmera rente ao chão no pé da ladeira, figura pequena de costas subindo ao fundo.

### 24. Ninguém elogia o alicerce. — `publicada (post 80, 2026-09-02 — FECHADA D+7: 11.24 shares/1k · alcance 246439 · errou-pra-cima)`
- **Slide:** 1 linha 44px, toda em preto. **Símbolo (FINAL, img-04 de 6, 2ª rodada):** casinha de pedra intacta no alto de uma barranca desmoronada, com a fundação de blocos cortados à mão exposta pelo desmoronamento — muitas vezes maior que a casa. Névoa, sem figura humana. *A proporção é a frase.*
- **Caça (6 gerações em 2 rodadas) — aprendizado de REGISTRO:** a 1ª rodada (canteiro de obra: valas com ferragem, pilar na névoa, fundação vazia) foi reprovada inteira pelo user: *"se eu visse essas imagens sem a frase, seriam apenas um canteiro de obra comum."* O conserto não foi prompt melhor, foi trocar o registro — de documental/mundano (canteiro) pra atemporal/monumental (pedra, ruína), que é o registro da imagem do post 42. Regra que fica: **símbolo de lei observada pede registro atemporal; obra moderna e maquinário matam a leitura.**
- **Legenda (2.100 chars — EXCEÇÃO ao teto de 1.400, aprovada pelo user):** construída na **estrutura-raiz** (molde do post 47), a pedido dele: *"é a versão 2 dessa frase da raiz, só muda os personagens."* Transposição: vento→tempestade, raiz→alicerce, copa/fruto→fachada/sala/vista. A linha que carrega o post é o par direto da melhor linha da raiz: *"O alicerce é a única parte da casa que ninguém fiscaliza. Justamente porque não aparece, ninguém cobra. Até chover..."* — entrega a consagração e fecha a brecha do vitimismo de uma vez.
- **Correções do user registradas:** (1) *"Sumir é o trabalho dela"* cortado — o papel do alicerce é SUSTENTAR, sumir é consequência; não bajular a metáfora contra a tese. (2) Falar do que É VISTO (elogio à cor da parede, à vista da sala) vence falar do que não é visto — ausência o leitor tem que construir na cabeça. (3) Inventário empresarial folha/mês/crise abandonado por ser idêntico ao dos posts 42 e 37: **repetir o mecanismo, nunca o inventário literal.**
- **Veia:** trabalho invisível/sustentação — consagra quem carrega sem aplauso (o dono, o pai, a mãe, quem segura tudo). Elogio vai pra fachada; a casa inteira depende do que ninguém vê.
- **Mecanismo:** autodeclaração — "eu sou o alicerce". Segunda camada: se você precisa de elogio pra sustentar, não é alicerce. Obra é o causo mais brasileiro que existe.
- **Símbolo (ideia):** fundação de obra rente ao solo — vigas baldrame e ferragem nas valas, câmera baixa, casa pronta desfocada na névoa ao fundo (o que o alicerce vai virar).

### 25. Bicicleta parada não para em pé. — `em produção (post 248, 16/10; aprovada pelo João pra produzir; bicicleta já no 209 com outra tese)`
- **Veia:** movimento (validada no 55, 1,24%) — lei física real que toda criança brasileira aprendeu no corpo: equilíbrio só existe andando.
- **Mecanismo:** autodeclaração — "eu me equilibro porque me movo". Segunda camada: quem para esperando se equilibrar (na vida, no negócio) cai; estabilidade é consequência do movimento, não pré-requisito. Molho no jogo "parada não para".
- **Símbolo (ideia):** bicicleta velha de carga em movimento na estrada de terra, leve arrasto de movimento nas rodas, névoa; ou apoiada caída no chão × outra em movimento — a confirmar no conceito.

### 26. Filho no colo não pesa. — `publicada (post 66, 2026-09-03 — FECHADA D+7: 9.27 shares/1k · alcance 40757 · nao-pontua)`
- **Slide:** 1 linha 44px, toda em preto. **Símbolo (FINAL, img-01, primeira geração, conceito 1 de 3):** adulto de costas com criança dormindo no ombro e o braço caído solto, rua estreita na névoa, sem rostos. Subida 90px via `object-fit:cover`.
- **Precedente de conteúdo (user, 28/08):** figura de gênero NÃO MARCADO de propósito — o banco dizia "pai", mas quem mais carrega criança no colo no Brasil são as mães. *"Nosso compromisso é com a verdade e fazer isso com as mulheres mães em um país como o Brasil é ser cruel demais."* Regra que fica: quando o símbolo tiver dono social desproporcional, não marcar.
- **Legenda (1.756 chars):** abre invertendo a frase (criança dormindo PESA) e nomeia o mecanismo real — o que não acontece é a CONTA; o peso não vira dívida. Antídoto duplo obrigatório: sentir o peso não é amar menos (mãe sozinha há três noites nomeada) e propósito não substitui ajuda. Twist final: a frase não é convite pra carregar mais, é critério pra saber o que largar.
- **Veia:** peso escolhido/amor pelo fardo (parente do hit "Escolha o seu estresse", 6k shares) — a lei mais emocional do lote.
- **Mecanismo:** autodeclaração — quem carrega o que ama não chama de fardo. Segunda camada: o peso que esmaga é o que não tem sentido; propósito muda a física. Legenda fecha a brecha (regra 26): não é que quem sente peso não ama — é que o mesmo peso, com sentido, se carrega diferente.
- **Símbolo (ideia):** pai de costas carregando criança adormecida no colo, subindo rua simples na névoa, câmera baixa.
- **Reserva do mesmo filão** (se preferir sem família): "A sacola da própria feira pesa diferente."

### 27. Saco vazio não para em pé. — `publicada (post 71, 2026-08-30 — FECHADA D+7: 1.47 shares/1k · alcance 10204 · errou-pra-baixo)`

- **Origem da ideia (user):** ressignificar o ditado que todo brasileiro fala sem saber de onde vem — "saco vazio não para em pé". Mecanismo novo nomeado pelo user: **gatilho de curiosidade + "nossa, então é isso"** → memória afetiva pelo conteúdo (e pela marca). A legenda entrega a origem histórica real.
- **A história (pesquisada 26/08, fontes no fim):** o ditado NÃO nasceu sobre comida. A trilha documentada: provérbio inglês "An empty sack cannot stand upright" registrado na coletânea de Thomas Fuller (1732); **Benjamin Franklin** o publicou no *Poor Richard's Almanack* (1740, reescrito em 1750), consagrou no *The Way to Wealth* (1758) e voltou a ele na autobiografia. O sentido original de Franklin era **dignidade, não almoço**: "é difícil um saco vazio ficar de pé" = é difícil um homem em miséria/escassez se manter ÍNTEGRO (honesto, de pé moralmente) — a pobreza torna a virtude mais cara. Existem equivalentes no italiano ("sacco vuoto non sta in piedi") e no português de Portugal ("saco vazio não se tem em pé"). No Brasil o sentido escorregou pro literal do corpo: o saco de estopa da roça/armazém (feijão, café) só para em pé cheio → o corpo-saco precisa de comida pra aguentar o trabalho. A migração exata pro contexto de almoço não tem registro documentado (origem popular oral) — a legenda trata essa parte como observação, sem inventar precisão.
- **A ressignificação (volta ao sentido original):** o que enche uma pessoa e a mantém de pé não é só comida — é substância: preparo, valores, reserva, propósito. "Estar de pé" = dignidade. Vazio por dentro, ninguém para em pé por muito tempo.
- **Redação do slide (FECHADA 28/08):** o user escolheu **(c)** "Saco vazio não para em pé." seco, vermelho em "vazio", 44px em 1 linha. O punch "Gente vazia também não." fica fora do slide; a legenda carrega a segunda camada. Os dois slides foram renderizados lado a lado pra decisão. Opção (b) segue descartada.
- **Legendas redigidas (26/08, arco aprovado: cena do almoço → Franklin 1758 → dignidade → vazio que dobra → caixa sutil → espelho → frase fecha; recheio = dignidade com reserva dentro):**
  - **Legenda C** (pro slide seco): abre "Você ouviu essa frase a vida inteira, na hora do almoço…", segura o mistério ("quase ninguém sabe o que ela dizia antes de chegar à mesa"), revela Franklin/1758 ("não falava de comida. Falava de dignidade… Cheio, você recusa. Vazio, você aceita."), saco de estopa, o vazio que dobra ("O caráter continua lá. Só ficou caro demais de sustentar."), caixa ("Reserva é isso — o preço de poder dizer não."), nota honesta do Brasil ("Ninguém registrou quando a frase virou conselho de almoço…"), espelho ("Do que você anda se enchendo — e do que anda vazio?"), fecho "Franklin sabia. Sua avó, do jeito dela, também." + frase seca. ~1.550 chars. Íntegra na conversa de 26/08.
  - **Legenda A** (pro slide com punch): abre pela avó/prato e pivota rápido ("a frase é maior do que a mesa"), mesma espinha Franklin→estopa→dobra→caixa, espelho "E você, anda cheio de quê?", fecho "Sua avó cuidou de uma parte do enchimento. A outra, ninguém põe no seu prato." + dístico completo ("Saco vazio não para em pé. / Gente vazia também não."). Sem a nota histórica do Brasil (diferenciador da C). Íntegra na conversa de 26/08.
  - **Legenda FINAL (1.411 chars; v2 de 28/08): `conteudo/carrosseis/71_saco-vazio/legenda.txt`.** Nasceu da C com três cortes do user (28/08): parágrafo dedicado à origem eliminado (Franklin virou uma frase dentro do parágrafo da avó, fechando no punch), o "Sem…" trocado por princípios/valores/propósito, e "Conteúdo é isso, o poder de dizer não" no lugar de "Reserva é isso". Detalhe no `carousel-text.md` do post 71.
- **Símbolo (FINAL, `img-02.png`):** close do carregador de costas com a saca cheia e firme no ombro, cabeça virada por cima do ombro e inclinada pra baixo, olhar duro, suor pesado; só ele e a saca, névoa vazia em volta. CSS `scale(1.4)`. O 1º conceito (armazém com sacas vazias amassadas no chão, `img-01.png`) foi gerado e descartado pelo user: "focar só na simbologia do cara e do saco nas costas".
- **Atenção de calendário:** prima da 25 (bicicleta — mesmo fecho "não para em pé"). Não publicar as duas na mesma semana coladas; espaçar.
- **Fontes:** Franklin/The Way to Wealth via Library Company (librarycompany.org/BFWriter/poor.htm), goodreads.com/quotes/890653, columbusclassical.org/blog/an-empty-sack; uso brasileiro: chc.org.br/artigo/saco-vazio-nao-para-em-pe, midiaoeste.com.br (005-origem-e-significado), proverbios.blogs.sapo.pt/tag/saco.

## Lote 6 — candidatas (2026-09-04, do ritual do dia; aguardando crivo do user)

> Contexto do ritual: o feijão fechou em 8,34 shares/1k com 1,28M de alcance (veia da pressão
> compra alcance, não taxa — 4º caso). Regra de leitura: taxa é mediana por padrão; `acima` só com
> comparável fechado. As frases 29 e 30 carregam o TESTE PROSPECTIVO da veia da pressão (ficha prevê
> `mediana` em taxa e >50k em alcance, ângulo diferente entre si). A 32 é a VEIA TESTE: propósito/
> escolha (nº 2 da tabela do o-que-funciona), nunca rodada como frase — e serve de controle da
> veia da pressão pelo lado de fora (alcance previsto <50k).

### 29. Pneu vazio não fura. Também não roda. — `publicada (post 86, 2026-09-06 — FECHADA D+7: 5.31 shares/1k · alcance 54753 · errou-pra-cima)`
- **Origem:** candidata do lote 6 ("Pneu vazio não fura"). O user escolheu a variação com a virada dentro do slide ("Também não roda"); "Sem pressão, o pneu não fura" foi evitada por espelhar a estrutura do feijão uma semana depois.
- **Formato:** lei observada. **Veia:** pressão (nº 1) — ângulo NOVO declarado: a ausência de pressão como segurança falsa (feijão = pressão cozinha; pedra = obstáculo amola; ladeira = peso de quem sobe).
- **Dor (confirmada pelo user):** quem montou a vida pra não furar; tirou a pressão de tudo e chama de paz; o sintoma sentido é "minha vida não sai do lugar", e a pessoa nunca liga uma coisa à outra.
- **Mecanismo:** paradoxo em primeira leitura + dois grupos (quem roda × quem está no acostamento). Legenda: pneu é quase só ar (o que carrega o peso é a pressão); rodar vazio ESTRAGA o pneu (quem evita pressão não fica preservado, se rasga em silêncio); brecha: pressão certa ≠ máxima. Inventário de vida, não de empresa (ajuste do user).
- **TESTE PROSPECTIVO DA VEIA DA PRESSÃO (única frase do teste):** ficha prevê `mediana` (7,0–9,0 shares/1k) e alcance >50k, escrito antes de publicar.
- **Imagem (FINAL, img-11 de 11):** sedã antigo empoeirado de lado, inteiro, junto ao meio-fio, pneus vazios, poeira sutil só embaixo, parquímetro atrás, névoa em cima. Regras de briefing que ficaram no `carousel-text.md` do post 86 (uma imagem por vez; lateral e inteiro; manter o degradê; cena urbana real; detalhe-chave sutil).
- **Legenda FINAL (1584 chars):**

> Pneu é quase só ar. A borracha que você vê é a casca; o que aguenta o peso de uma tonelada de carro é a pressão que está dentro dela. Tira o ar e a borracha continua lá, inteira, sem um arranhão. E o carro não sai do lugar.
>
> Pneu vazio tem uma vantagem, e é real: ele não fura. Nunca vai estourar na estrada, nunca vai te deixar na mão no meio da noite. Não tem prego que entre, não tem buraco que estoure. É o pneu mais seguro que existe, se a medida de segurança for nunca ter problema.
>
> Tem gente que monta a vida assim. Vai tirando o ar de tudo, devagar, sem perceber. O curso que largou na metade. A mudança de cidade que ficou pra quando der. A conversa com o pai que nunca aconteceu. O sonho que virou assunto de mesa de bar... cada pressão que sai parece um alívio, e a soma dos alívios é uma vida que não fura nunca. E que não anda.
>
> Rodar com pneu vazio estraga o pneu. A borracha dobra onde não devia, esquenta por dentro, rasga na lateral. Quem insiste em andar sem pressão não fica preservado, se desgasta mais rápido, e de um jeito que não tem conserto.
>
> A vida sem pressão não é uma vida guardada. É uma vida se rasgando em silêncio, no acostamento, enquanto a pessoa se orgulha de nunca ter furado.
>
> Só que pressão certa não é pressão máxima. Cada pneu tem a calibragem certa escrita na lateral, e quem enche além disso não anda melhor, estoura na primeira pedra.
>
> O ponto não é aguentar o máximo. É ter dentro de você exatamente o que precisa pra carregar o que você escolheu carregar.
>
> Você está rodando, ou só não está furando? Pneu vazio não fura. Também não roda.

### 30. Roupa apertada é medida de crescimento. — `publicada (post 85, 2026-09-05 — FECHADA D+7: 3.11 shares/1k · alcance 21239 · errou-pra-baixo)`
- **Origem:** nasceu como "Só aperta a roupa de quem cresceu" (lote 6). O user escolheu, entre quatro variações, a lei seca "Roupa apertada é medida de crescimento" ("medida" com dupla leitura de costura e régua).
- **Dor (redefinida pelo user):** NÃO é "quem cresceu e não percebeu"; é **quem insiste em vestir a roupa velha sabendo que não serve** — medo de amadurecer, de encarar responsabilidade; a roupa antiga remete ao tempo em que ninguém cobrava nada. A ironia que sustenta: a roupa do adulto é mais confortável e mais elegante. Se o medo de crescer pudesse ser visto, seria um adulto de roupa de criança: bizarro, e o incômodo é o efeito desejado no leitor.
- **Formato:** lei observada. **Veia:** amadurecimento/escolha (saiu da veia da pressão: o ângulo virou medo de crescer, não aperto como pressão; **NÃO conta pro teste prospectivo da veia**, que segue com o pneu).
- **Mecanismo:** incômodo pela imagem + consagração no fim (quem trocou de roupa). Risco declarado e aceito pelo user: na regra do espelho, advertência fica em mediana pra baixo; a saída foi fechar a legenda consagrando, não acusando.
- **Registro visual (decisão):** a imagem é uma pessoa, não um símbolo solene — primeira frase do perfil com figura humana "estranha" no centro. Estranheza, não piada: versões com arquinho de leão/hambúrguer/gordura (06–08) foram geradas e preteridas em favor da intermediária (09). Ver `carousel-text.md` do post 85.
- **Legenda:** abertura pela imagem ("Incomoda olhar, né?") a pedido do user, sem a cena da criança; corte de vício de IA ("o que ninguém contou pra ela") feito pelo user; fecho com a provocação dele ("todo mundo tem uma roupa apertada na vida"). Sem parágrafo de empresa.
- **Previsão a escrever na ficha:** `mediana`, faixa alargada 7,0–9,5 shares/1k (sem comparável na base pra imagem com figura estranha; variância de aposta alta). Alcance sem previsão.
- **Legenda FINAL (1791 chars):**

> Incomoda olhar, né? Essa imagem te causou estranheza, e era pra causar. Porque se o medo de crescer pudesse ser visto de fora, ele seria exatamente isso: um adulto vestindo a roupa de quando era criança. Sobrando corpo, faltando tecido. Esquisito. Bizarro.
>
> A roupa não tem culpa. Tecido não cresce e não encolhe, ele nasce num tamanho e morre nele. Tudo que muda entre você e uma roupa é você. Então quando aperta, o corpo já deu a notícia. Só falta a pessoa aceitar.
>
> E tem gente que não aceita. Sente o aperto todo dia e mesmo assim insiste na roupa velha. Não porque serve. Porque ela lembra um tempo em que ninguém esperava nada dela. Roupa de criança é o tempo em que crescer era promessa e não cobrança, em que responsabilidade era assunto dos outros, em que o que precisava ser enfrentado ainda podia esperar. A pessoa não está apegada ao pano. Está apegada ao tamanho que tinha quando nada dependia dela.
>
> Só que roupa apertada não protege nada. Ela marca. Marca no corpo, o dia inteiro, o tamanho que a pessoa se recusa a assumir. E quem vê de fora vê tudo: o botão forçado, a manga curta, o adulto fingindo que está confortável. A única pessoa que acredita no disfarce é quem está dentro dele.
>
> Só que a roupa do adulto é mais confortável. Tem espaço pra respirar, pra andar. E é mais elegante, porque foi feita pro tamanho de quem veste. O peso de assumir a responsabilidade é menor que o peso de evitá-la, porque esse a pessoa carrega e ainda gasta energia escondendo. Quem se recusa a crescer não fica leve. Fica apertado.
>
> E se você leu até aqui achando que isso não é com você, olha de novo. Todo mundo tem uma roupa apertada na vida, e ela está te dando uma medida. O que muda é quem decide continuar vivendo com o que não cabe mais.
>
> Roupa apertada é medida de crescimento.

### 31. Calo não se herda. — `publicada (post 84, 2026-09-04 — FECHADA D+7: 10.35 shares/1k · alcance 597454 · errou-pra-cima)`
- **Origem:** nasceu como "Calo é bolha que ficou" (candidata do lote 6). O user tirou a bolha da frase ("duas analogias enfraquecem o impacto"), preferiu a linha "ninguém nasce com calo", e das quatro variações escolheu **"Calo não se herda."** ("não se compra" foi descartado: fórmula gasta, põe dinheiro na frase e vira contra a casa).
- **Formato:** lei observada do corpo. **Veia:** dor/preparo (nº 1, família). Ângulo: a repetição vira proteção; o calo é adaptação, não teimosia.
- **Mapa de símbolos (user + ajuste):** enxada = a dificuldade que você escolheu segurar (trocou "cabo" por "enxada" pelo simbolismo de trabalho duro) · terreno carpido = o processo, a labuta · calo = a marca que o processo deixou em quem ficou · cama = o alívio moral (NUNCA "pagamento" no sentido de dinheiro; "a conta fecha" foi mantida pelo user).
- **Dor:** de quem constrói algo do zero (empreendedor ou qualquer pessoa que se compromete a construir). **Herdar é só menção breve**, não a dor. **Sem parágrafo explícito de empresa**: a dor já seleciona o público; o espaço vai pro conceito filosófico.
- **Mecanismo:** autodeclaração ("meu calo eu fiz"; "mão de quem segura" no presente inclui quem está na fase da bolha) + dois grupos na cama (mão ardendo dorme sereno × mão lisa arde a cabeça). Cura depois da dor; constância > intensidade ("esforço isolado só faz bolha").
- **Antiburro RETIRADO da legenda por decisão do user** (o corpo endurece só onde a enxada encosta; quem endurece tudo ficou insensível): fica como **resposta pronta pro comentário "então é pra endurecer?"** e como semente de frase própria: **"Insensível não é calejado."** (candidata futura).
- **Ressalva de calendário:** o beat da cama usa a dupla "os dois deitam cansados" — tese-irmã do carrossel 63 (dois cansaços, 28/08, fechou abaixo). User ciente; aqui é beat de legenda em formato frase, não a tese do post.
- **Previsão a escrever na ficha:** `mediana` (7,0–9,0 shares/1k). Alcance sem previsão (fora do classificador da veia da pressão; fica de fora do teste prospectivo).
- **Símbolo (ideia):** palma de mão de trabalho aberta em close, calos marcados, cabo de enxada gasto atravessado; ou o cabo polido pelo uso encostado numa parede, sem mão. Registro atemporal, sem maquinário.
- **Legenda FINAL (1726 chars; teto passou a 1800 em 04/09):**

> Calo é a pele entendendo que a enxada volta amanhã.
>
> No primeiro dia ela reclama. Arde, faz bolha, pede pra você largar. E quem larga, sara e volta liso... já quem segura de novo no dia seguinte, e no outro, ensina o corpo a responder de outro jeito: a pele engrossa justamente onde a enxada machucou. Isso não é teimosia. É o corpo se adaptando pra aguentar o processo. E só acontece na mão de quem segura.
>
> Repara numa coisa: calo não nasce do dia mais pesado. Nasce do dia comum, repetido e repetido. Esforço isolado só faz bolha. O que forma o calo é voltar. A pele não responde à intensidade, responde à constância, e por isso ninguém vê o calo se formando. Ele cresce em silêncio, em dias que parecem iguais, até que um dia a mão não arde mais e você nem lembra quando parou de arder.
>
> E o curioso é que dá pra herdar a enxada, dá pra herdar o terreno, o nome no portão, até o negócio inteiro... O calo, não. Ele só nasce em quem fez.
>
> Quem está construindo alguma coisa do zero conhece essa fase. Todo dia parece o primeiro dia, a mão arde e ninguém vê. Você olha pra quem já chegou lá e a mão dele parece que nasceu assim. Mas não nasceu. Ele só segurou mais vezes do que largou.
>
> No fim do dia, todo mundo deita. É ali que a conta fecha, e a diferença é o que deita junto. Quem carpiu o dia inteiro deita com a mão ardendo, e essa ardência tem um alívio que só quem fez conhece: o terreno ficou pra trás, limpo, e não sobrou nada esperando por amanhã. É o único cansaço que vira descanso. Já quem largou no meio deita com a mão lisa. Nada arde, nada dói. Mas o que ele adiou deita com ele, e é a cabeça que passa a noite ardendo.
>
> O seu cansaço de hoje é de quem segurou, ou de quem largou no meio? Calo não se herda.

### 32. Sonho que não te tira da cama é sono. — `candidata` · **VEIA TESTE**
- **Formato:** lei observada do cotidiano (despertador, cama). **Veia:** propósito/escolha/sonho (nº 2 da tabela: média 1.513 shares por post no perfil; "forte quando confronta" — o hit "sonho com CNPJ", 17k). **Nunca rodada como frase**; só existe em carrossel e reel.
- **Mecanismo:** molho no par sonho/sono + dois grupos + autodeclaração (quem levanta se declara sonhador de verdade). Confronta sem acusar: o sonho não é falso, é só sono.
- **Previsão a escrever na ficha:** `mediana` (6,6–9,0 shares/1k) · **alcance <50k** — é o controle da veia da pressão pelo lado de fora: se uma frase forte fora da veia ficar abaixo de 50k enquanto as duas da veia passam, a hipótese "a veia compra distribuição" ganha o contraste que faltava. Risco declarado: a veia 2 no carrossel é confronto direto; como lei observada pode perder o dente e cair pra advertência (teto ~0,9%). O espelho segura: a frase consagra quem levanta.
- **Símbolo (ideia):** cama de solteiro desfeita com a luz da manhã já alta na parede, despertador de ferro no criado-mudo; ou o par de chinelos ainda ao pé da cama com o sol batendo neles. Sem figura humana.
- **Legenda (esqueleto):** princípio (a diferença entre sonho e desejo não é o tamanho, é o horário: um te levanta, o outro te embala) → o adulto que fala do sonho há dez anos na mesma cama → empresa: a "visão" da parede que não muda a agenda de segunda → brecha fechada (regra 25): não é elogio a acordar às 5h; é sobre o que te tira da cama, não a hora → responsabilidade sem moralismo: sonho é o que você faz antes do café → espelho: "o seu, levanta você ou só te faz dormir melhor?" → frase fecha.
- **Alternativa de teste (se o user preferir testar mecanismo em vez de veia):** provérbio conhecido COM punch de virada no slide, pra separar "provérbio pronto afunda" de "faltou o punch" no caso do saco vazio (hipótese "o provérbio pronto não viaja").

## Descartadas (lote 1, 2026-08-14)

- O conforto também cobra. Só que parcelado.
- Dói mais o que você adiou do que o que você enfrentou.
- O time joga o que o dono treina.
- Todo mundo quer o topo. Ninguém quer a falta de ar.
- Quem nunca arriscou vive de palpite.
- Sem âncora, todo vento vira destino.
- Na zona de conforto, tudo vence.

## Publicadas (referência de calibre)

> ✅ **API normalizada (2026-08-20).** Regra nova no CLAUDE.md: ler métricas de
> `conteudo/analise/desempenho.json`/`.csv` (atualizado todo dia ~9h por agendamento do
> macOS). Se `pulled_at` >24h, rodar SÓ `pull_insights.py update` (incremental).
> **NUNCA rodar `pull` completo** — foi ele que disparou o anti-abuso da Meta em 17/08.

Resultados abaixo do `desempenho.json` de **2026-08-25 09:32** (régua: ~1% shares/alcance saudável, >3% hit):

| Frase | Post | Publicada | Resultado |
|-------|------|-----------|-----------|
| No raso não existe pressão. | 37 | 2026-08-13 | **HIT GIGANTE** — reach 3,16M · 37.884 shares (1,20%) · 21.518 saves · 142,7k likes |
| O peso procura quem aguenta. | 42 | 2026-08-18 | **FORTE** — reach 251,5k · 3.405 shares (1,35%) · 2.578 saves |
| A raiz decide o que o vento leva. | 47 | 2026-08-21 | **FORTE** — reach 96,1k · 1.259 shares (1,31%) · 840 saves |
| Quem divide, multiplica. | 36 | 2026-08-12 | reach 86,0k · 1.072 shares (1,25%) |
| Um idiota em movimento chega mais longe que um gênio parado. | 55 | 2026-08-23 | reach 40,0k · 497 shares (1,24%) — D+2, subindo |
| A maré não espera barco pronto. | 39 | 2026-08-17 | reach 98,9k · 835 shares (0,84%) · 811 saves |
| A colheita é obrigatória. | 40 | 2026-08-16 | reach 42,2k · 344 shares (0,82%) |
| Quem nunca perde, também nunca ganha. | 41* | 2026-08-15 | reach 49,7k · 398 shares (0,80%) — *pasta local `40_nunca-perde` |
| O inverno não pergunta o que você plantou. | 48 | 2026-08-20 | reach 13,7k · 117 shares (0,85%) |
| Poucos homens caem por fraqueza… (afunda de pé) | 53 | 2026-08-22 | reach 13,6k · 122 shares (0,90%) |
| Só a água parada cria lodo. | 38 | 2026-08-14 | reach 45,0k · 231 shares (0,51%) |
| Gente boa não se demite da empresa. Se demite do dono. | 43 | 2026-08-19 | **FLOP** — reach 6,9k · 35 shares (0,51%) |
| (Batalha na cabeça) | 35 | 2026-08-11 | reach 13,6k · 141 shares (1,04%) |
| O verdadeiro peso de um ser é a lacuna… | 54 | 2026-08-24 | D+1: reach 7,6k · 56 shares (0,73%) — cedo pra ler (D+3 ≈ 27/08) |

### Leitura consolidada (2026-08-25) — o espelho do share

Separando as 13 frases maturadas em dois grupos pelo MECANISMO, a separação é perfeita
(rank test, p≈0,001; detalhe na H11 de `conteudo/analise/hipoteses.md`):

- **AUTODECLARAÇÃO POSITIVA** (compartilhar diz algo bom sobre quem compartilha: "eu aguento",
  "sou profundo", "me movo", "divido", "minha raiz é boa") — 35, 36, 37, 42, 47, 55:
  taxa 1,04–1,35% (mediana 1,25%), reach mediano ~91k, e os 3 maiores posts do formato.
- **ADVERTÊNCIA/ENSINO** (a frase adverte, cobra consequência ou acusa; compartilhar não
  eleva quem compartilha) — 38, 39, 40, 41, 43, 48, 53: taxa 0,51–0,90% (mediana 0,82%),
  reach mediano ~42k. NENHUMA passou de 1%.

Regra prática até segunda ordem: frase nova mira o grupo 1 — a lei precisa VESTIR BEM quem
compartilha. Advertências continuam válidas como variação, mas com previsão capada em ~0,9%.

## Lote 7 — candidatas (2026-09-07; user escolheu a pipa)

> Cinco opções propostas pelo Claude no critério do lote 4 (cotidiano brasileiro, universal,
> autodeclaração positiva, molho, símbolo inédito), uma veia por frase. O user escolheu a 33.

### 33. Pipa só sobe contra o vento. — `publicada (post 93, 2026-09-07 — FECHADA D+7: 7.63 shares/1k · alcance 30260 · errou-pra-cima)`
- **Formato:** lei observada. **Veia:** pressão/resistência (nº 1), ângulo NOVO declarado: a oposição é o que eleva (feijão = processo; pedra = agente; ladeira = peso de quem sobe; pneu = ausência de pressão; **pipa = usar o contra**).
- **Mecanismo:** autodeclaração ("o que vem contra mim é o que me sobe"). Segunda camada: vento a favor derruba pipa; quem só tem tudo a favor não sai do chão.
- **Slide:** 1 linha 44px, **toda em preto** (user). **Símbolo (conceito 1 de 3):** laje de cimento, câmera rente, menino de costas pequeno no pé do quadro segurando a linha tensa em diagonal até a pipa escura no meio do céu branco, rabiola pro lado, telhados de morro na névoa. Sem scale.
- **Legenda:** abre pela lei invertida ("Vento a favor derruba pipa"), braço do menino como registro físico, camada universal em categorias (chefe que não cobra, mês sem susto, ninguém diga não), anti-burro como fato seco (vendaval rasga papel; dar linha e recolher), empresa em 3 itens, espelho "segurando ou soltando?", frase fecha.

### 34. Chuveiro só esquenta com a água correndo. — `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`
- **Veia:** movimento (validada no 55). Lei do chuveiro elétrico. Espelho: "esquento porque corro". Prima da 25 (bicicleta): não colar. Símbolo: chuveiro velho com vapor, azulejo escuro.

### 35. Escada não sobe com o pé no chão. — `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`
- **Veia:** propósito/escolha/risco (nº 2). Molho na dupla leitura de "pé no chão" (prudência × parado). Espelho: "eu tirei o pé". Símbolo: primeiro degrau de escada de pedra gasta, câmera rente, resto na névoa.

### 36. Massa só cresce coberta. — `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`
- **Veia:** trabalho invisível/crescimento no escuro (família raiz/alicerce). Espelho: "cresço onde ninguém vê". Legenda cabe na estrutura-raiz (forno leva a fama, fermento decidiu antes). Símbolo: bacia com pano de prato na mesa da cozinha.

### 37. Vaso seco não é culpa da planta. — `em produção (post 249, 16/10; aprovada pelo João pra produzir; advertência)`
- **Veia:** time/preparo com culpa no dono (nº 3) camuflada em cotidiano. É ADVERTÊNCIA (grupo 2): previsão capada ~0,9%. Serve de teste limpo da H12 (o problema do 43 era o nicho, não a tese). Símbolo: vaso murcho na janela, terra rachada.

## Lote 8 — garimpo por cena (2026-09-08; segunda-feira)

> Método registrado com o user: **cena brasileira primeiro, lei física depois, frase por último.** Nasceu
> da rejeição do par sonho/sono (candidata 32): trocadilho vive na língua, não no mundo, e por isso não
> dá imagem nem surpresa. O user diagnosticou "fraca" três rodadas seguidas até a ordem ser invertida.
> Quatro cenas garimpadas: carro no tranco (escolhida), chaleira que cala antes de ferver, concreto que
> só endurece molhado, ferro que trabalha não enferruja.

### 38. Quem pega no tranco não espera bateria. — `publicada (post 96, 2026-09-08 — FECHADA D+7: 7.03 shares/1k · alcance 38243 · errou-pra-cima)`
- **Cena:** segunda de manhã, bateria arriada, três vizinhos empurrando o carro na ladeira, "solta a embreagem". **Lei:** carro no tranco só pega em movimento; depois que pega, é o motor que carrega a bateria.
- **Formato:** lei observada. **Veia:** movimento/começo sem condição ideal (troca de veia deliberada depois de 6 frases de pressão/peso). **Mecanismo:** nomeia o leitor ("quem") + autodeclaração + dois grupos (quem empurra × quem espera a bateria).
- **Lapidação (3 versões):** "Carro no tranco só pega andando" (descrevia a mecânica) → A "Quem pega no tranco não espera bateria" (escolhida: nomeia, dois grupos, molho no ditado) · B "Bateria se espera. Tranco se dá." (eco, ficou de fora da legenda final) · C "Carro no tranco não pega parado".
- **Slide:** 1 linha 44px, toda em preto. **Símbolo (FINAL, img-01, primeira geração, conceito 1 de 3):** ladeira de paralelepípedo molhado rente ao chão, três homens de costas curvados na traseira de um Fusca, pés cravados na pedra, casario antigo, igreja na névoa. Sem rosto, sem scale, sem nada moderno (registro atemporal, lição do alicerce). Topo validado.
- **Legenda (1.798 chars, versão final do user):** abre pela lei ("Carro só pega tranco em movimento"), motor carrega a bateria andando, bateria como categorias universais (dinheiro, ânimo, curso, segunda-feira certa), esperar descarrega, anti-burro (tranco não resolve tanque vazio nem motor fundido), ninguém dá tranco no próprio carro (orgulho × ajuda), empresa em 3 itens + erro do dono, espelho, fecho em dois tempos + frase. User abriu o anti-burro com "E cuidado," e o parágrafo do orgulho com "E olha que curioso," (escolha dele; alertado sobre a regra do anti-burro que não se anuncia).
- **Previsão (ficha):** `acima` 9.3–11.8 shares/1k; comparáveis 55 (11,66, mesma veia) e 42 (13,48). Hipótese que mataria: "provérbio pronto não viaja" (saco vazio 1,47) — não se aplica porque a sentença é nova e o punch está no slide.

### Reservas do garimpo de 08/09 — `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`
- **"A chaleira cala antes de ferver."** — a mais forte em surpresa; consagra quem trabalha em silêncio; segunda camada: quem faz barulho ainda não ferveu. Publicar num dia sem concorrência de cozinha/vapor (feijão 65 usou panela).
- **"Concreto só endurece molhado."** — laje curada com água; o que parece amolecer é o que endurece; laje que seca rápido racha. Fato pouco conhecido = gatilho de curiosidade na legenda.
- **"Ferro que trabalha não enferruja."** — a mais previsível; repete a tese da água parada (38). Última opção.


## Lote 9 — garimpo por cena (2026-09-08) — crivado pelo user no mesmo dia

> Primeira rodada (7 frases + 4 reservas) reprovada na CONSTRUÇÃO: o user aprovou as metáforas da
> cebola, da pipoca, do bolo e da banana, mas achou as frases "mal construídas em português" e o
> desenvolvimento raso. Diagnóstico registrado: eu não traduzo do inglês, mas o molde que uso por
> padrão pra frase é anglófono (sujeito-verbo-complemento na ordem; fórmula "X é o Y que Z";
> paralelismo copiado da ladeira "só... quem"). Correção: construir com os recursos do português
> falado do Brasil — clivagem com "é" ("cresce é de porta fechada"), elipse de ditado ("basta uma
> madura"), ordem invertida ("chora a cebola quem pica"), verbo da casa ("picar", não "cortar"), gíria
> que coincide com a lei física ("vazar", "estourar"). Descartadas: 40 (corda: "não é impactante em
> nenhuma instância"), 44 (freio: "ruim demais"), 43 (pingo/balde: frase ruim; ideia explicada, decisão
> pendente). Reservas da 1ª rodada mantidas abaixo sem mexer.

### 39. Cebola — `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`
- **Cena:** cozinha de casa, tábua de madeira, quem pica de olho ardendo; a mesa cheia come sem lágrima nenhuma. **Lei 1:** o ardor só sai na hora de picar; quem come não sente. **Lei 2 (a que aprofunda):** a mesma cebola que arde crua chega **doce** na panela — refogada, caramelizada, ela vira o açúcar do prato. O que ardeu na tábua chega doce na mesa.
- **Construções (português falado):**
  - A. **"Cebola faz chorar na tábua, não na mesa."** — dois lugares da casa, a lei mora no contraste; "na mesa" já carrega quem só senta pra comer.
  - B. **"Chora a cebola quem pica. Quem come, não."** — ordem invertida de ditado; nomeia os dois grupos com o verbo da casa (picar).
  - C. **"Cebola arde é no olho de quem pica."** — clivagem com "é", a mais oral das três.
- **Veia:** dor de quem faz (família da pressão, sem as palavras do classificador). **Mecanismo:** dois grupos (tábua × mesa) + autodeclaração ("eu sou da tábua"). Espelho positivo: quem compartilha diz "o que chega doce pra vocês ardeu em mim primeiro".
- **Legenda (esqueleto, profundidade de lote 5):** abre pela lei 2, que é a surpresa ("A cebola que arde crua é a mesma que adoça o prato") → a tábua como lugar onde a coisa é feita e a mesa como lugar onde ela é recebida; ninguém prova a lágrima, só o tempero → categorias abertas, sem biografia: quem prepara, quem sustenta, quem chega antes de todo mundo e apaga a luz depois → o ardor tem horário: é na tábua, é sozinho, é antes; quem chega na mesa acha que o prato nasceu pronto → **empresa em 3 itens:** o dono que só senta à mesa e cobra o prato de quem está na tábua; o time que só vê o dono na mesa e não sabe que ele picou a madrugada inteira; e o cliente, que tem direito de nunca saber (a lágrima não é argumento de venda) → **anti-burro (regra 24), como fato seco:** chorar não é mérito nem medida de trabalho — cebola gelada e faca afiada picam igual e ardem menos; quem chora demais pode estar picando errado, não picando mais; e cebola picada que não vai pra panela é só lágrima sem prato → espelho: "hoje você está na tábua ou na mesa? e quem está na tábua por você?" → fecho na frase.
- **Símbolo (ideia):** tábua gasta, faca de cabo de madeira, cebola aberta em metades e o monte picado, câmera rente à mesa, luz de janela de cozinha; mãos no máximo, sem rosto. Inédito.

### 41. Toda transformação exige pressão. — `feita (post 102, 2026-09-09; frase do USER no lugar das construções A/B/C — quis a palavra 'pressão' direta; imagem: UMA pipoca no instante do estouro, clean, image-edit pra corrigir a casca; legenda 1.892 chars refeita 3x — fio único, sem 'Na empresa é o mesmo X')`
- **Cena:** panela de alumínio no fogão, tampa pulando, e no fundo os piruás que ninguém come. **Lei:** o milho estoura porque a casca segura o vapor até a pressão virar explosão; o piruá é o grão de casca rachada — a pressão vazou por uma fresta e ele nunca estoura. Mesmo fogo, mesma panela, mesmo tempo: o que faltou não foi fogo, foi vedação.
- **Construções:**
  - A. **"Quem vaza não estoura."** — a gíria coincide com a lei física: no Brasil "vazar" é sair fora, "estourar" é dar certo ("o negócio estourou"); e na panela é literalmente isso. Não é trocadilho de língua (caso sonho/sono): é a mesma palavra descrevendo o mundo e a vida. Nomeia o leitor.
  - B. **"Piruá é pipoca que vazou antes da hora."** — a versão que explica; menos punch, mais sorriso de reconhecimento.
  - C. **"Milho que vaza vira piruá."** — sentença de ditado, curta, com a palavra-molho no fim.
- **Veia:** pressão (nº 1) com ângulo NOVO declarado: **pressão de dentro que transforma** (feijão = processo; pedra = agente; ladeira = peso; pneu = ausência; pipa = usar o contra; pipoca = segurar por dentro até virar outra coisa). **Mecanismo:** dois grupos (pipoca × piruá) + autodeclaração ("eu não vazo").
- **Legenda (esqueleto):** abre pelo fato pouco conhecido (o piruá não é milho ruim: é milho rachado; a pressão saiu pela fresta antes de virar estouro) → a fresta é pequena e ninguém vê, mas decide tudo → categorias abertas: a fresta de quem reclama pra aliviar, de quem "dá uma saída" a cada aperto, de quem troca de plano no primeiro calor → o piruá ficou o mesmo tempo na mesma panela: não foi falta de fogo, nem de tempo, nem de sorte → **empresa em 3 itens:** o dono que vaza do negócio a cada aperto (muda de ramo, de sócio, de sistema — troca de panela e nunca estoura); o time que vaza na primeira cobrança; e a empresa que "quase estourou" três vezes e ninguém entende por quê → **anti-burro (regras 24/25):** segurar pressão não é engolir tudo calado — milho sem panela só queima, e panela sem óleo gruda; a estrutura em volta é o que deixa a pressão virar estouro em vez de queimadura; e casca rachada muitas vezes vem de antes (milho velho, seco demais): quem chegou rachado precisa de cuidado, não de mais fogo. Não repetir a válvula da legenda do feijão → espelho: "na sua panela, você é o que estoura ou o que vazou?" → fecho.
- **Símbolo (ideia):** panela de alumínio amassada, tampa de vidro erguida pelos estouros, pipoca subindo; em primeiro plano, na mesa, um punhado de piruás escuros; fogão a gás velho, azulejo. Inédito.
- **Risco declarado:** saturação da veia (pipa 7,3 em D+1; 9 frases de pressão em 14 dias). O ângulo novo e a curiosidade do piruá são o que seguram. "Estourar" também é surtar: a legenda fecha essa leitura.

### 42. Bolo — `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`
- **Cena:** forno de fogão antigo, "não abre o forno!", bolo que murchou no meio porque alguém espiou. **Lei 1:** abrir o forno derruba a temperatura e o bolo desaba antes de firmar. **Lei 2 (a que aprofunda):** bolo que murchou **não levanta mais** — pôr de volta no forno não conserta. Crescimento interrompido não retoma de onde parou; recomeça do zero, com outra massa.
- **Construções:**
  - A. **"Bolo cresce é de porta fechada."** — clivagem com "é", oral, a lei virada pro positivo (consagra quem fecha a porta).
  - B. **"Bolo espiado murcha."** — três palavras; "espiado" é o molho, todo mundo já foi pego espiando.
  - C. **"Quem abre o forno come bolo murcho."** — nomeia o leitor e entrega a consequência na mesma frase.
- **Veia:** crescimento (nº 4) / foco / tempo sem plateia. **Mecanismo:** dupla leitura de "porta fechada" — não espiar antes da hora (ansiedade) e não deixar entrar todo mundo (opinião de quem passa, entra-e-sai). Autodeclaração: "eu fecho a porta e deixo crescer".
- **Legenda (esqueleto):** abre pela lei 2, a mais dura ("Bolo murcho não volta pro forno") → o crescimento tem um período em que ele é mole por dentro e ainda não se sustenta: é exatamente aí que dá vontade de espiar → categorias abertas: um curso, uma mudança de vida, um casamento no começo, um filho aprendendo uma coisa — tudo que está crescendo está mole por dentro, e mole por dentro não aguenta a porta aberta → quem espia não é inimigo: é ansiedade, é a vontade de mostrar antes da hora, é a opinião de quem passa pela cozinha → **empresa em 3 itens:** o dono que muda o plano toda semana (abre o forno); o dono que expõe o projeto cru pra opinião de todo mundo e volta com o bolo murcho; o time novo que é trocado antes de assentar → **anti-burro:** porta fechada não é forno desligado — tem fogo, tem tempo marcado, tem receita; e tem hora de abrir: o palito existe. Quem nunca abre queima → espelho: "o que você está espiando antes da hora?" → fecho.
- **Símbolo (ideia):** porta de forno de fogão a gás antigo entreaberta, luz quente vazando pela fresta, forma redonda com bolo afundado no meio; cozinha simples, meia-luz. Inédito.
- **Alternativa da mesma família (microgerência):** "Quem mexe no arroz, empapa." — advertência (grupo 2, capada); guardar pra dia de variação de tom.

### 45. Basta uma madura pra amadurecer a penca. — `publicada (post 101, 2026-09-09 — FECHADA D+7: 6.94 shares/1k · alcance 28393 · acertou)`
- **Cena:** penca no gancho da quitanda ou na fruteira de casa; uma escura no meio das verdes, e em dois dias a penca inteira amarelou. **Lei:** a madura solta etileno e apressa as vizinhas; é a mesma molécula que faz uma podre estragar o cacho. Toda casa sabe a versão prática: quer que dure, separa a madura; quer apressar, junta.
- **Construções:**
  - A. **"Basta uma madura pra amadurecer a penca."** — elipse de ditado ("uma madura", sem dizer banana); ritmo de provérbio novo.
  - B. **"Banana amadurece em penca."** — a lei inteira em três palavras; a segunda camada (gente também) fica por conta de quem lê.
  - C. **"Uma madura apressa a penca. Uma podre também."** — traz o gume duplo pro slide; mais advertência, mais molho.
- **Veia:** exemplo/influência — universal (família, turma, time do bairro, mesa de bar). **Mecanismo:** autodeclaração ("eu sou a madura da penca") + gume duplo na legenda. Molho no verbo "amadurecer" aplicado a gente.
- **Legenda (esqueleto):** abre pelo fato (a banana não amadurece por dentro; amadurece pelo ar, pelo que a vizinha solta) → ninguém amadurece sozinho nem estraga sozinho: você está sempre soltando alguma coisa pra quem está do lado, e a pergunta é o quê → categorias abertas: a casa onde todo mundo amadureceu perto de alguém; a roda onde todo mundo azedou perto de alguém → a verde não escolheu; ficou perto → **empresa em 3 itens:** cultura não se ensina em palestra, vai pelo ar como etileno — pela penca; o gerente azedo que estraga a área inteira sem dizer uma palavra; e o dono, que é a banana em contato com todas → **anti-burro:** não é "corte as verdes" (as verdes é que amadurecem, e é pra isso que a madura serve); e madura demais vira podre — quem amadureceu e parou começa a estragar a penca (o veterano acomodado) → espelho: "o que você está soltando pra quem está do seu lado?" → fecho.
- **Símbolo (ideia):** penca pendurada em gancho de ferro, uma banana escura de casca pintada entre as verdes lisas, parede de quitanda ao fundo, luz lateral dura. Inédito.

### Descartadas do lote 9 (user, 08/09)
- **40. Corda só puxa. Não empurra.** — "não é impactante em nenhuma instância; desenvolvimento ruim".
- **44. Quem tem freio desce mais rápido.** — "ruim demais".
- **43. Ninguém vê o pingo. Todo mundo vê o balde.** — frase "muito ruim"; ideia explicada ao user (torneira pinga a madrugada inteira sem ninguém ouvir; de manhã todo mundo vê o balde cheio — o "sucesso da noite pro dia" é balde que ninguém viu encher). Reconstrução possível: "Balde cheio é pingo que ninguém ouviu." `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`

### Reservas do garimpo de 08/09 (lote 9) — `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`
- **"Terra seca demais não bebe a chuva."** — solo ressecado repele água e vira enxurrada; quem está esgotado não absorve nem a coisa boa que chega. Contrapeso da veia da pressão (regra 25); share por cuidado, não por autodeclaração; previsão capada.
- **"Feijão no algodão brota. Mas não dá vagem."** — toda criança brasileira fez na escola; brota sem terra, nunca frutifica. Começo fácil × sustentar. O feijão já apareceu no 65 — esperar.
- **"Tinta não cobre buraco."** — pintar por cima da parede furada; aparência em cima de base ruim. Advertência (grupo 2), capada.
- **"Brasa sozinha esfria."** — churrasco: carvão junto segura calor, sozinho apaga aceso. Advertência; símbolo bom.

## Lote 10 — TRADUÇÃO DE FILOSOFIA (método novo do user, 2026-09-10)

> **Método:** partir de conceito filosófico já produzido e relevante (Epicteto, Aristóteles, Platão, Sêneca,
> Marco Aurélio, Heráclito, Kant...) e TRADUZIR pro cotidiano brasileiro, nas nossas palavras e no nosso
> jeito simples de falar — "seremos mais um tradutor do que um elaborador, um tradutor que usa a própria
> linguagem" (user). Três degraus: **filosofia** (o pensamento, como resumo da legenda; universal, nunca
> nichado a empresário) → **cena** (o fato cotidiano que encarna o conceito sem explicação) → **frase** (por
> último, em português falado, 2-3 construções). A citação original NUNCA vai pro slide: no lote 3 as três
> frases citadas ao pé da letra (abismo 0,54% · lacuna 0,73% · afunda de pé 0,90%) ficaram abaixo de 1%;
> o que muda agora é que a citação some e fica a tradução. Nada muda na skill /frase: os itens são briefings.
> Origem: o user reprovou dois cardápios de "filosofia" do Claude por serem nichados (5 de 6 falavam de dono).
> O user aprovou os 8 conceitos abaixo em 10/09 ("gostei de todas; podemos fazer todas as 8").

### 46. Epicteto — o que depende de você e o que não depende — `aprovada: construção A (user 10/09)`
- **Filosofia (resumo da legenda):** A chuva não pergunta se você lavou o carro. O trânsito não sabe que você está atrasado. A pessoa passa o dia brigando com o que não manda e esquece do único lugar onde manda: o que faz em seguida. Quem separa as duas coisas para de gastar força com o tempo e gasta com o guarda-chuva. A vida não fica mais fácil; fica mais leve, porque você para de carregar o que nunca foi seu.
- **Cena:** carro lavado no sábado e a chuva de domingo; o guarda-chuva na porta. **Espelho:** "eu cuido do que é meu" (autodeclaração; consagra quem age no que controla).
- **Construções:** A. "A chuva não pergunta se você lavou o carro." · B. "Ninguém manda na chuva. Manda no guarda-chuva." · C. "Chuva não é problema seu. Guarda-chuva é."
- **Símbolo (FINAL):** Fusca recém-lavado tomando chuva pesada, câmera rente ao asfalto, balde e pano na calçada, sem gente. `feita (post 109, 2026-09-10; construção A; legenda 1.817 chars aprovada sem cortes, Epicteto nomeado)`

### 47. Aristóteles — a virtude é hábito (somos o que repetimos) — `aprovada: construção A (user 10/09)`
- **Filosofia:** Ninguém é honesto. A pessoa é honesta hoje, de novo amanhã, de novo quando ninguém está olhando, até que um dia isso vira o nome dela. Caráter não é uma decisão grande, é mil decisões pequenas iguais. E o contrário também: ninguém vira preguiçoso num dia; vira num monte de "amanhã eu faço" que ninguém contou. Você é a soma do que repete, não do que pretende. (Formulação "excelência é hábito" é de Will Durant resumindo Aristóteles — não citar como literal.)
- **Cena:** a trilha de terra batida no terreno baldio / no capim: ninguém abre passando uma vez; abre passando todo dia. **Espelho:** "eu passo todo dia".
- **Construções:** A. "Trilha não se faz passando uma vez." · B. "Caminho na grama é gente passando todo dia." · C. "Ninguém abre trilha de uma passada."
- **Símbolo (FINAL):** trilha de terra batida no capim alto, câmera rente, figura pequena de costas indo pra cidade na névoa. `feita (post 110, 2026-09-11; construção A; legenda 1.846 chars aprovada sem cortes, Aristóteles nomeado, CTA fixo de seguir)`

### 48. Platão — a caverna — `aprovada: construção C (user 10/09)`
- **Filosofia:** Todo mundo cresce num quarto e acha que o quarto é a casa. A vida que os pais tiveram, o salário que o bairro paga, o jeito que sempre se fez. Quem sai desse quarto passa mal no começo, porque a luz de fora dói. E quando volta pra chamar os outros, escuta que ficou metido, que mudou, que esqueceu de onde veio. A sombra é confortável porque todo mundo em volta vê a mesma. Sair custa a companhia.
- **Cena:** abrir a janela/porta do quarto escuro de manhã; a luz que dói no olho de quem dormiu no escuro. **Espelho:** "eu saí do quarto" (consagra quem aguentou a luz).
- **Construções:** A. "Sol dói em olho acostumado com escuro." · B. "Quem acende a luz apanha primeiro." · C. "Luz incomoda quem se acostumou no escuro."
- **Símbolo (FINAL):** close do antebraço e da mão erguidos contra a luz (cenas de quarto rejeitadas: "close mais fechado é melhor, mais metafórico"). `feita (post 112, 2026-09-11; construção C; legenda editada pelo user sobre a v2, 1.978 chars com CTA, Platão em meia linha)`

### 49. Sêneca — sofremos mais na imaginação do que na realidade — `aprovada: construção C (user 10/09)`
- **Filosofia:** A conversa difícil dói uma semana antes e dez minutos durante. A demissão que você adia pesa mais nos meses de adiamento do que no dia. A pessoa carrega o problema na cabeça até ele ficar maior que o problema. E quando finalmente enfrenta, descobre que o pior já tinha passado, e passou onde não existia: na véspera. Quase tudo que a gente adia é adiado por medo de uma coisa que dura menos que o medo.
- **Cena:** a fila da vacina no posto: a agulha dói dez segundos, a fila dói a manhã inteira. **Espelho:** "eu encaro" (consagra quem enfrenta).
- **Construções:** A. "Injeção dói mais na fila." · B. "A agulha dói dez segundos. A fila, a manhã inteira." · C. "O medo dura mais que a agulha."
- **Símbolo (FINAL):** fila reta no corredor do posto vista de trás, menina debruçada pra fora da fila espiando a porta (edição da cena de calçada; zoom 1,75x). Moderação do motor barrou 7x a criança de frente. `feita (post 113, 2026-09-11; construção C; legenda aprovada com parágrafo do dono trocado pra ESTUDAR; Sêneca em meia linha; CTA fixo)`

### 50. Quem espera o rio secar mora na margem. — `feita (post 130, 2026-09-17; frase nasceu das linhas da legenda depois de 2 rodadas de construções rejeitadas; imagem: figura só sentada na margem olhando o rio (a ponte de arcos foi rejeitada: "pouco poética, muita informação"); legenda SEM nome do pensador — regra nova; CTA fixo)`
- **Filosofia:** A pessoa espera o caminho limpar pra andar. Só que o caminho é feito do que está nele. O problema que apareceu não é o que te atrasa, é o que te ensina o próximo passo: a pedra na ladeira é onde o pé se apoia. Quem passa a vida esperando a estrada sem pedra nunca sai da porta; quem anda descobre que foi subindo pelas pedras. **Risco:** vizinha da pedra/faca (76) e da pipa (93) — precisa de cena nova.
- **Cena:** atravessar o riacho pisando nas pedras: a pedra que atrapalha o rio é a que atravessa a gente. **Espelho:** "eu piso na pedra".
- **Construções:** A. "Pedra no rio é ponte." · B. "Quem atravessa o rio pisa na pedra." · C. "A pedra que atrapalha o rio é a que atravessa a gente." (2 linhas)
- **Símbolo (ideia):** riacho de pedras redondas na névoa, câmera rente à água, pé/figura de costas no meio da travessia. `candidata`

### 51. A água de ontem já está no mar. — `feita (post 131, 2026-09-19; legenda escrita antes, frase tirada dela; imagem mínima: homem de pé na correnteza; SEM nome do pensador; CTA fixo) — FECHA O LOTE 10`
- **Filosofia:** A pessoa volta pra cidade onde cresceu e acha que a cidade mudou. Não foi só a cidade. Quem quer "voltar a ser como era" está pedindo pra entrar num rio que já passou. Não existe voltar, existe só continuar. O casamento de dez anos não é o mesmo do primeiro ano; o negócio de hoje não é o que você abriu. Quem aceita isso para de tentar consertar o passado e começa a cuidar do que está passando agora.
- **Cena:** voltar na casa da infância e tudo parecer menor — a casa não encolheu. **Espelho:** "eu cresci".
- **Construções:** A. "A casa da infância não encolheu." · B. "Ninguém volta. Só continua." · C. "A rua da infância ficou menor. Foi você que cresceu." (2 linhas)
- **Símbolo (ideia):** porta de casa antiga de bairro, homem de costas grande demais pro batente, rua estreita na névoa. `candidata`

### 52. Sêneca — não é que a vida seja curta, é que a gente perde muito dela
- **Filosofia:** Ninguém rouba o seu dia inteiro. Roubam vinte minutos aqui, uma tarde ali, "depois eu vejo", e no fim do ano você não sabe pra onde foi. O tempo não some de uma vez, ele vaza. A pessoa protege o dinheiro com senha e deixa o dia aberto pra qualquer um entrar. E a diferença é que dinheiro volta.
- **Cena:** o bolso furado: ninguém perde tudo de uma vez, perde uma moeda por vez sem ouvir cair. **Espelho:** "eu conto meu dia".
- **Construções:** A. "Bolso furado não perde tudo de uma vez." · B. "Ninguém perde o dia inteiro. Perde de vinte em vinte minutos." (2 linhas) · C. "O dia não acaba. Vaza."
- **Símbolo (FINAL):** calçadão de pedra portuguesa rente ao chão, rastro de moedas, homem de costas se afastando na névoa com a mão no bolso. `feita (post 108, 2026-09-10; construção A; legenda 1.764 chars aprovada sem cortes, Sêneca nomeado)`

### 53. Kant — aja como se todo mundo fosse agir igual — `aprovada: construção C (user 10/09)`
- **Filosofia:** Antes de furar a fila, imagina todo mundo furando. Antes de jogar o papel pela janela, imagina a rua inteira fazendo o mesmo. Toda escolha pequena é uma proposta de mundo: "que seja assim pra todos". O que a pessoa faz quando acha que é só ela é exatamente o que ela está pedindo que todo mundo faça. Você não decide só por você, nunca. Você vota.
- **Cena:** a fila (do banco, do ônibus, do posto); o papel jogado na rua limpa. **Espelho:** "eu voto certo" (consagra quem se comporta quando ninguém vê). Risco: pode ler como advertência (grupo 2) — construção precisa consagrar.
- **Construções:** A. "Toda fila furada começa com um só." · B. "Você não fura a fila. Você vota." · C. "Ninguém suja a rua sozinho."
- **Símbolo (FINAL):** um único papel amassado numa rua de paralelepípedo limpa ao amanhecer, cidade histórica na névoa. `feita (post 129, 2026-09-17; construção C; legenda aprovada sem cortes, Kant em meia linha, CTA fixo)`

## Lote 11 — tradução de filosofia, continuação (2026-09-20)

> Mesmo método do lote 10, com as regras que entraram depois: legenda ESCRITA ANTES da frase (a frase nasce das linhas dela), fluida, SEM nome do pensador; imagem mínima (uma figura/objeto + névoa); CTA fixo de seguir. Fonte fica só aqui, pra rastreio.

### 54. O peso é o mesmo, o motivo é que pesa. — `feita (post 133, 2026-09-20; Nietzsche traduzido — quem tem um porquê aguenta quase qualquer como; frase = adaptação do user sobre a construção C (trocou da B adaptada antes de postar); imagem: homem de costas com saco na estrada; legenda 2.083 chars)`
- **Filosofia (resumo):** o mesmo peso cansa diferente conforme o que significa; cansaço vem do vazio, não da quantidade; a maioria troca o como (rotina, emprego, método) e esquece o porquê; porquê não é frase na parede, é o resultado que a pessoa vê acontecer por causa dela.
- **Cena:** saco de cimento nas costas; despertador adiado. **Veia:** propósito/escolha (nº 2). **Espelho:** "eu tenho um porquê".

### 55. Calçada varrida não precisa de discurso. — `feita (post 134, 2026-09-21; Marco Aurélio traduzido — pare de discutir como deve ser um homem bom, seja um; a pedido do user, segundo Marco Aurélio do método; frase, imagem e legenda decididas pelo Claude ("me entregue pronta"); imagem: homem varrendo a calçada ao amanhecer; legenda 2.107 chars)`
- **Filosofia (resumo):** discutir o certo dá a sensação de fazer o certo e é mais barato; quem varre a calçada não aparece na discussão sobre limpeza; o tempo gasto definindo a pessoa boa é tirado de agir bem; o dono descreve a cultura na reunião e faz o contrário depois.
- **Cena:** a mesa de domingo dos opinadores; a calçada varrida. **Espelho:** "eu faço" (consagra quem age sem plateia).

### 56. A falta cresce junto com o prato. — `feita (post 136, 2026-09-22; Epicuro traduzido — nada é suficiente pra quem o suficiente é pouco; 1ª frase "Quem não gosta do pouco não gosta de nada" rejeitada pelo user; legenda editada pelo user (ego; pergunta final) + problema nomeado pelo Claude (o olho treinado na falta); vocabulário: falta, não fome nem ambição; imagem: velho de chapéu com a caneca no banquinho da porta; legenda 2.133 chars)`
- **Filosofia (resumo):** contentamento não é quantidade, é capacidade, e se treina; a fome de mais não passa comendo, cresce com o prato; o dono que vai "ficar tranquilo quando chegar no número" e o número muda; gostar do pouco não é conformismo: quem gosta do pouco cresce mais leve, por vontade e não por buraco.
- **Cena:** café da manhã na cadeira da calçada, caneca lascada, pão de ontem. **Espelho:** "eu sei gostar do que tenho".

### 57. A grama do vizinho só é verde de longe. — `feita (post 138, 2026-09-22; ditado popular ressignificado — eixo COMPARAÇÃO, separado do 136 (quantidade) e do 139 (caráter); imagem: cerca de arame entre grama seca e grama densa, sem gente; legenda editada pelo user; publicação prevista 23/09 9h)`
- **Filosofia (resumo):** a grama do vizinho parece mais verde porque se olha de longe e a própria de perto; a comparação mostra o que você não tem com uma precisão que nunca usa no próprio quintal; o vizinho faz o mesmo do outro lado da cerca; o tempo olhando é o tempo que faltou regando; olhar pra aprender rega, olhar pra medir seca.
- **Cena:** o portão, a cerca baixa, a mangueira enrolada. **Espelho:** "eu rego a minha".

### 58. Confiança se prova no troco, não no cofre. — `feita (post 139, 2026-09-23; máxima "fiel no pouco, fiel no muito" traduzida — eixo CARÁTER provado no pequeno, separado do 136 (quantidade) e do 138 (comparação); imagem: uma moeda só na mesa escura (outpaint pra baixo + composite pra subir a moeda); legenda editada pelo user; publicação prevista 24/09 9h)`
- **Filosofia (resumo):** ninguém entrega o cofre pra quem não devolveu o troco; a única prova de como alguém cuida do muito é como cuidou do pouco; confiança não se declara, se acumula uma moeda por vez; o pouco não é só dinheiro (recado, prazo, tarefa chata); o dono cobra no grande o que não entrega no pequeno; a consciência confere.
- **Cena:** o troco no balcão; o real a mais devolvido sem ninguém pedir. **Espelho:** "eu devolvo inteiro".

## Lote 12 — mecanismo "doeu na hora, era necessário" (2026-09-24)

> Nascido do joelho ralado, que o user chamou de "fenomenal": experiência que todo brasileiro viveu na pele, doeu na hora, e o adulto entende hoje como parte da vida. **Regra do user (24/09): infância é tempero, não cardápio** — só infância descaracteriza a identidade do Hélio (empresário, vida adulta); as de infância saem a cada ~3 dias com vida adulta entre elas. O mecanismo pode ser reaproveitado em cena adulta. Sementes ficam SEM ALTERAÇÃO até a vez delas.

### 59. Ninguém aprende sem ralar o joelho. — `feita (post 145, 2026-09-24; construção do user; imagem: close dos dois joelhos de criança, curativo num e ralado no outro, 8 rodadas; legenda com Merthiolate e tampão do dedo; publicação prevista 25/09 9h)`

### 59b. A vida solta antes de avisar. — `feita (post 209, publicado 2026-10-10 (sábado) ~8h50; lei: a mão que segura solta antes de avisar, você já estava pronto antes de saber; frase do user (tirou 'pai' da proposta A); imagem: mão do adulto soltando o selim, criança já pedalando, rua de terra; legenda v2 com as 5 linhas reservadas)`
- Linhas da v1 do joelho reservadas pra ela: "Todo mundo que sabe andar de bicicleta tem uma cicatriz que não lembra mais onde fez" · "teve a vontade de nunca mais subir naquela coisa. E no dia seguinte a criança subiu de novo" · "Ninguém aprende a se equilibrar olhando os outros pedalar" · "as quedas que estavam ensinando a empresa a andar sem as rodinhas" · "Quem nunca deixou o time cair nunca vai ter um time que pedala". Imagens já geradas: bicicleta caída na rua de terra (145/img-01) e rodinha recém-tirada com parafusos (145/img-02).
- Construção da 1ª rodada: "Ninguém aprende bicicleta sem cair."

### 60. Dente de leite não foi feito pra ficar. — `feita (post 168, 2026-09-30; 4 rodadas de frase — user passou pela lei sem o objeto e voltou pro dente; imagem: mão adulta com o dente entre os dedos, após prateleira 'macabra' e mão de criança 'zoada'; legenda co-escrita; publicado 30/09)`
- Ele caiu pra nascer o de verdade, e ninguém chora hoje pelo dente que perdeu aos sete anos. O adulto ainda segura dentes de leite: o emprego que já não cabe, o jeito antigo de tocar o negócio, a versão de si que precisava cair pra vir a definitiva.
- A. "Dente de leite cai pra nascer o de verdade." · B. "Ninguém fica com o dente de leite pra sempre."

### 61. Soltar da borda da piscina — `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`
- Ninguém aprendeu a nadar segurando na borda; alguém soltou você, e naquele dia isso pareceu crueldade. O adulto vive segurando em bordas (a garantia, o sócio, a mãe que ainda resolve) e chama de prudência.
- A. "Ninguém aprende a nadar segurando na borda." · B. "Quem te soltou na piscina te ensinou a nadar."

### 62. Primeiro o que sustenta, depois o que agrada. — `feita (post 176, 2026-10-04 (domingo) 9h; 3ª de infância; frase = a lei, o feijão fica na imagem: prato de feijão com o pudim coberto esperando atrás; legenda reaberta pela lei)`
- A regra da mesa que toda criança odiou e todo adulto entendeu: primeiro o que sustenta, depois o que agrada. Quem inverte a ordem na vida, no dinheiro e na empresa fica só com a sobremesa, e passa fome.
- A. "Sobremesa vem depois do feijão." · B. "Ninguém pula o feijão e ganha a sobremesa."

### Candidatas não selecionadas (mesmo lote, registro) — `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`
- **Largar a chupeta** — todo mundo chorou pra largar, e largou; o adulto tem chupetas (conforto que acalma e não resolve). "Chupeta ninguém larga sem chorar." · "Todo conforto que acalma é uma chupeta."
- **A porta da escola** — quem foi embora no primeiro dia te ensinou a ficar; quem ama às vezes deixa sozinho de propósito. "Quem te deixou na porta da escola te ensinou a ficar." · "Na porta da escola, ir embora era amor."

### Stand-by (user 24/09: "só quando for necessário, e melhorar antes") — `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`
- **Plantar o que você não vai colher** — a sombra de hoje alguém plantou sem sentar nela; quem só faz o que rende no mês deixa toco. "Quem planta árvore não senta na sombra." · "A sombra de hoje alguém plantou sem ver."
- **Não desenterrar a semente** — a ansiedade mata o processo; tudo que cresce tem um tempo em que parece que nada acontece. "Semente não brota mais rápido de tanto olhar." · "Quem desenterra pra ver se brotou, mata."

### 63. Cozinheiro bom prova antes de servir. — `feita (post 163, 2026-09-28; Sócrates traduzido — quem acha que sabe parou de aprender; construção 3A; imagem: mão erguendo a colher de pau da panela; legenda aprovada sem cortes; publicado 28/09)`
- **Filosofia (resumo):** a certeza é o primeiro tempero a estragar; quem sabe continua desconfiando da própria mão; sabedoria começa ao descobrir o que ainda não se sabe sobre o que se faz todo dia; o dono é o cozinheiro que mais precisa provar e menos prova.
- **Regra do user (24/09):** frase precisa de símbolo real (objeto), não sentimento — coragem/sabedoria abstratas reprovadas até virarem laje/cozinheiro.

### Fila aprovada/pendente (24/09)
- **Laje só se conhece com peso em cima.** (1A, Sêneca — ninguém sabe do que é feito até ser obrigado) — `aprovada, a produzir`
- **Coragem (Aristóteles — medo com direção)** — `feita (post 174, 2026-10-02): "A água não esquenta pra quem fica na borda."` (passou por "Quem não tem medo não tem coragem"; a analogia da água gelada veio do user; imagem: escada da piscina; regra nova: objeto nunca vem de cima pro quadro)
- **Louça de festa (Sêneca — enquanto adiamos, a vida passa)** — `feita (post 175, publicado 2026-10-03 (sábado) 9h): "Toda ocasião especial era um dia comum."` (3 rodadas de frase sobre a louça reprovadas; a louça ficou só na imagem — pilha de pratos no plástico com pó — e a frase diz a lei)

### 64. Laje só se conhece com peso em cima. — `feita (post 166, 2026-09-29; Sêneca traduzido — ninguém sabe do que é feito até ser posto à prova; construção 1A; imagem: laje-objeto com sacos de cimento e rachadura, molde da prateleira, 11 gerações; legenda v4 universal com a laje em um parágrafo; publicado 29/09)`
- **Lições registradas:** (1) imagem de frase "como a prateleira" = objeto contra parede de reboco, sem chão, sem cenário, sem cidade; (2) legenda construída em volta do objeto vira "conteúdo pra pedreiro" — o objeto ocupa UM parágrafo e o resto é a verdade universal; (3) o user pede feedback do Claude sobre a própria legenda antes de aprovar — dar de verdade.

## Lote 13 — LEIS UNIVERSAIS DIRETAS (2026-10-01, "pra diversificar")

> Pedido do user: frase que é a lei nua, sem objeto no slide, no molde de "No raso não existe pressão" e "O peso procura quem aguenta" (as duas melhores da conta). Imagem segue mínima (molde da prateleira). Cinco aprovadas de uma vez; **intercalar com as sementes anteriores** (coragem, louça, borda da piscina, feijão antes da sobremesa). Ordem combinada: B → coragem → A → louça → C → piscina → D → feijão → E.

### 65. O que você evita é o que te governa. — `feita (post 170, 2026-10-01; Epicteto traduzido; 1ª lei direta do lote 13; imagem: pedra no sapato (porta, telefone, cadeado, marionete e sombra passaram); legenda co-escrita com a pedra como metáfora central; publicado 01/10)`
### 66. Ninguém é forte onde nunca foi testado. — `feita (post 181, 2026-10-05 (segunda, ~11h); recomeço pela lei: leitura de Aristóteles (teste CONSTRÓI, força é local), não Sêneca (revela = laje 166); imagem: braço recém-saído do gesso, mão meio aberta testando, gesso serrado ao lado; 9 rodadas de imagem; legenda v5)`
### 67. Não existe calma que não tenha sido conquistada. — `feita (post 187, publicado 2026-10-06 (terça, ~11h); Marco Aurélio; leitura PREPARO: calma = o que sobra quando o preparo respondeu as perguntas; imagem: mala pronta no chão com documento e chave em cima; legenda v3 com a manhã da viagem)`
### 68. Quem precisa de plateia não está pronto. — `feita (post 208, publicado 2026-10-07 (quarta); Sêneca, virtude no escuro; lei: pronto é quem faz igual com a porta aberta e fechada; imagem: tênis de corrida molhado largado na porta de madrugada; legenda v1 aprovada sem edição)`
### 69. Ninguém foge do que carrega dentro. — `feita (post 223, publicado 2026-10-11 (domingo); Sêneca, você viaja com você; imagem: caixas de mudança, a de cima aberta; legenda v5 co-escrita com o user, com o insight da 'limpa' da mudança)`

## Lote 14 — candidatas (2026-10-11, a crivar pelo user)

### 70. A limpa da mudança — `descartada (João 19/10: "as demais podemos excluir da base")`
- **Lei:** a gente só mexe no fundo do armário quando é obrigado; mudança é a única hora em que se joga fora o que acumulou por anos. Frase bruta do user: "é em época de mudança que se mexe".
- **Construções:** A. "Só se mexe no fundo do armário em dia de mudança." · B. "Ninguém abre o fundo da gaveta sem mudança marcada." · C. "A limpa só vem com o caminhão na porta."
- **Atenção:** irmã do 223 (mesma cena); espaçar.

### 78. Todo adulto foi uma criança sem vergonha de errar. — `feita (post 225, publicado 2026-10-12 (domingo, Dia das Crianças) ~09:46; semente nascida no dia; lei observada: vergonha de errar é ensinada; imagem: desenho de mãe e criança preso na geladeira Consul por ímã de loja de gás; linha forte da legenda: "Criança mostra o desenho torto. O adulto esconde.")`
- **Caminhos abertos e não usados (Dia das Crianças, 12/10):** "Criança não lembra do presente. Lembra de quem brincou." (presente × presença) — `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`; chupeta e porta da escola seguem na reserva do lote 12.

### 79. Quem para de sonhar para de realizar. — `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`
- **Construções:** A. "Quem para de sonhar para de realizar." · B. "Ninguém constrói o que não imaginou antes." · C. "Criança não aprende a sonhar. Aprende a parar."
- **Atenção:** veia propósito/sonho (nº 2); irmã do 225, espaçar algumas semanas.

### 71. Varal frouxo não segura roupa. — `feita (post 230, publicado 2026-10-13 (terça) ~10:31; Heráclito traduzido; construção A; imagem: varal de quintal frouxo com a camisa arrastando no chão, postes altos (versão de apartamento gerada e descartada pelo user); legenda v1 aprovada sem edição)`
- **De quem é:** Heráclito (o arco e a lira: a harmonia nasce da tensão dos opostos). **Lei:** é a tensão que sustenta; o que está frouxo não segura nada.
- **Cena:** corda de varal frouxa, a roupa molhada arrasta no chão; esticou, segurou. **Espelho:** "eu aguento esticado".
- **Construções:** A. "Varal frouxo não segura roupa." · B. "Corda só segura esticada." · C. "O que afrouxa, cai."

### 72. O apito é o mesmo. O grito é que muda. — `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`
- **De quem é:** Epicteto (não é o fato que perturba, é o juízo sobre o fato). **Lei:** o fato é um só; o sofrimento é a leitura que cada um faz dele.
- **Cena:** o apito do juiz no estádio: uma torcida comemora, a outra xinga, foi o mesmo apito. **Espelho:** "eu escolho a leitura".
- **Construções:** A. "O apito é o mesmo. O grito é que muda." · B. "Juiz apita uma vez. Cada lado ouve uma coisa." · C. "Ninguém sofre do fato. Sofre da leitura."

### 73. Toda estrada de terra foi desvio um dia. — `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`
- **De quem é:** Marco Aurélio (o que atrapalha o caminho vira o caminho). **Lei:** o obstáculo não fecha a estrada; ele decide por onde ela passa.
- **Cena:** pedra ou atoleiro na estrada de terra, o caminhão abre um desvio, o desvio vira a estrada. **Espelho:** "eu passo por onde dá".
- **Construções:** A. "Toda estrada de terra foi desvio um dia." · B. "A pedra não fecha a estrada. Desenha." · C. "Caminho é o que sobra depois do atoleiro."

### 74. Quem muda de canal toda hora não assiste nada. — `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`
- **De quem é:** Sêneca (quem está em todo lugar não está em lugar nenhum). **Lei:** dispersão é ausência; estar em tudo é não estar em nada.
- **Cena:** o controle remoto, 200 canais, "não tem nada pra ver"; os cinco cursos começados; as três dietas do ano. **Espelho:** "eu fico até o fim".
- **Construções:** A. "Quem muda de canal toda hora não assiste nada." · B. "Duzentos canais e nada pra ver é problema do dedo." · C. "Ninguém termina o filme zapeando."

### 75. Gambiarra é filha da falta. — `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`
- **De quem é:** Platão (a necessidade é a mãe da invenção). **Lei:** é a falta que inventa; quem tem tudo não cria nada.
- **Cena:** a gambiarra brasileira: o arame no cano, o chinelo com o pino de garrafa, a antena de cabide. **Espelho:** "eu me viro". Atenção: pode ler como elogio ao improviso permanente; a legenda fecha a brecha (gambiarra é invenção de emergência, não de método).
- **Construções:** A. "Gambiarra é filha da falta." · B. "Ninguém inventa com a despensa cheia." · C. "A falta é que faz pensar."

### 76. Time de craque não é time. — `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`
- **De quem é:** Aristóteles (o todo é maior que a soma das partes). **Lei:** junto é outra coisa; onze bons separados perdem pra um time.
- **Cena:** a pelada do bairro: o time cheio de craque que perde pro time que se conhece. **Espelho:** "a gente joga junto".
- **Construções:** A. "Time de craque não é time." · B. "Onze craques não fazem um time." · C. "Craque ganha jogo. Time ganha campeonato."

### 77. Quem só vai ao médico com dor chega tarde. — `descartada (João 19/10: "as demais podemos excluir da base")`
- **De quem é:** Sócrates (a vida sem exame não vale ser vivida). **Lei:** olhar pra dentro antes de doer; quem espera o sintoma chega atrasado.
- **Cena:** o exame de sangue anual, o check-up, a revisão do carro. **Espelho:** "eu me examino". Atenção: é ADVERTÊNCIA (grupo 2); previsão capada.
- **Construções:** A. "Quem só vai ao médico com dor chega tarde." · B. "Exame bom é o que se faz sem sentir nada." · C. "Dor é o exame que você não fez."

## Lote 15 — no molde do 230 (varal), pedido do João em 16/10

> "Precisamos de 2 frases no estilo mais filosóficas" como o 230. Cinco sementes de objeto cotidiano com lei física e pensador por baixo; o João escolheu a 80.

### 80. Roupa sempre pega o cheiro da cozinha. — `em produção (post 247, 16/10)`
- **De quem é:** Sêneca (os costumes de quem está em volta grudam). **Lei:** você pega o cheiro de onde fica; quem está dentro não sente, quem chega de fora sente.
- **Construções:** A. "Roupa sempre pega o cheiro da cozinha." · B. "Ninguém sai da fritura cheirando a perfume." · C. "Quem fica, pega o cheiro."

### 81. Caixa d'água furada nunca enche. — `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`
- **Construções:** A. "Caixa d'água furada nunca enche." · B. "Não falta água. Sobra furo." · C. "Pinga por pinga, a caixa esvazia."

### 82. Muda que vive mudando não pega. — `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`
- **De quem é:** Sêneca (planta mudada de lugar muitas vezes não cresce). **Lei:** quem troca o tempo todo não cria raiz.
- **Construções:** A. "Muda que vive mudando não pega." · B. "Planta que troca de vaso toda hora não cria raiz." · C. "Raiz não cresce em vaso trocado."

### 83. Na chuva, guarda-chuva custa o dobro. — `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`
- **De quem é:** Sêneca (preparar-se antes da tempestade). **Lei:** preparo se faz antes; na crise custa o dobro. **Atenção:** vizinha da 187 (mala, preparo) e objeto da 109; não sair junto com a 84.
- **Construções:** A. "Na chuva, guarda-chuva custa o dobro." · B. "Guarda-chuva se compra no sol." · C. "Quem espera a chuva pra se preparar paga o preço do camelô."

### 84. Trânsito só irrita quem esperava rua vazia. — `descartada (João 16/10: "o restante pode descartar e vamos criar novos modelos")`
- **De quem é:** Marco Aurélio (avisar a si mesmo pela manhã do que vai dar errado). **Lei:** o que irrita não é o problema, é a surpresa. **Atenção:** vizinha da 187 (calma); não sair junto com a 83.
- **Construções:** A. "Trânsito só irrita quem esperava rua vazia." · B. "Engarrafamento não estressa quem já saiu sabendo." · C. "Não é o trânsito. É a rua vazia que você imaginou."

## Lote 16 — modelos novos (16/10, a crivar pelo João)

> Pedido do João depois do crivo de 16/10: aprovou a 25 e a 37 pra produzir, mandou melhorar a 70 e a 77, descartou o resto e pediu "novos modelos". Mesmo molde do 230: objeto do dia a dia, lei física ou observada, pensador por baixo.

### 85. Sapato gasta do lado que você pisa. — `descartada (João 19/10: "as demais podemos excluir da base")`
- **De quem é:** Aristóteles (somos o que repetimos). **Lei:** o hábito deixa marca antes de virar nome; ninguém vê como você anda, mas a sola conta.
- **Cena:** um par de sapatos virado, a sola gasta só de um lado. **Construções:** A. "Sapato gasta do lado que você pisa." · B. "A sola conta como você anda." · C. "Todo sapato gasto denuncia o passo."

### 86. Ninguém vê a própria nuca. — `descartada (João 19/10: "as demais podemos excluir da base")`
- **De quem é:** Sócrates (conhece-te a ti mesmo; o exame precisa do outro). **Lei:** o que a gente mais precisa ver em si é justamente o que não alcança sozinho. **Cena:** a barbearia, o barbeiro mostrando a nuca no espelho de mão. **Atenção:** mesma segunda camada do 247 (quem está dentro não sente o próprio cheiro); espaçar.
- **Construções:** A. "Ninguém vê a própria nuca." · B. "Pra ver a nuca precisa de dois espelhos." · C. "Só o barbeiro vê o seu corte de trás."

### 87. Todo bom chefe já lavou muita panela. — `em produção (post J263, 19/10)`
- **De quem é:** Aristóteles (só manda bem quem aprendeu a obedecer). **Lei:** comando se aprende servindo. **Cena:** pia de cozinha de restaurante com a pilha de panelas. Espelho: "eu lavei".
- **Construções:** A. "Todo bom chefe já lavou muita panela." · B. "Ninguém chega no fogão sem passar pela pia." · C. "Cozinheiro que nunca lavou panela não manda na cozinha."

### 88. Ninguém aprende a dirigir sem deixar o carro morrer. — `descartada (João 19/10: "as demais podemos excluir da base")`
- **De quem é:** Epicteto (quem quer progredir aceita parecer tolo). **Lei:** aprender exige passar vergonha em público. **Cena:** o carro de autoescola morto no sinal. **Atenção:** vizinha da 225 (vergonha de errar, 12/10); esperar algumas semanas.
- **Construções:** A. "Ninguém aprende a dirigir sem deixar o carro morrer." · B. "Todo motorista já ouviu buzina no sinal." · C. "Carro morre é na mão de quem está aprendendo."

### 89. Cadeira vazia também vota. — `em produção (post J264, 19/10)`
- **De quem é:** Platão (quem não participa é governado pelos outros). **Lei:** ausência é decisão; quem não aparece aceita o que os outros decidirem. **Cena:** reunião de condomínio, cadeiras de plástico, uma vazia. Espelho: "eu apareço".
- **Construções:** A. "Cadeira vazia também vota." · B. "Quem não vai à reunião paga a conta dela." · C. "Quem falta também decide."

### 90. Amigo de festa não aparece na mudança. — `em produção (post J265, 19/10)`
- **De quem é:** Aristóteles (amizade de prazer × amizade de verdade). **Lei:** amizade se mede no peso, não na festa. **Cena:** a geladeira sendo carregada escada abaixo. **Atenção:** caixas de mudança já no 223 (11/10), com outra tese.
- **Construções:** A. "Amigo de festa não aparece na mudança." · B. "Mudança mostra quem é amigo." · C. "Quem carrega a geladeira é amigo. O resto é convidado."

### 91. Relógio parado também acerta. Duas vezes por dia. — `feita (post J266, publicado 2026-10-21 (quarta); img-02 sem a pilha; legenda v1)`
- **De quem é:** ditado popular ressignificado (Sêneca: um acerto não prova nada). **Lei:** acerto isolado não é competência; competência é acertar todo dia. **Atenção:** pode soar como advertência.
- **Construções:** A. "Relógio parado também acerta. Duas vezes por dia." · B. "Acertar uma vez até relógio parado acerta." · C. "Um acerto não faz relógio."

## Lote 17 — flip chart no perfil do Hélio (19/10, a crivar pelo João)

> O lote 2 do banco da Academy (flip chart) foi lido pelo João como voz da marca: "estão mais para o perfil da Tatsuo Academy do que para o perfil do Hélio". Ficou reservado lá. Este é na voz do Hélio: falado, empresário pra empresário, sem bater em quem empreende. Suporte: flip chart da sala do MBV, letra comum, 2 linhas por cor (padrão do 251).

| # | Preto | Vermelho | Conceito | Lastro / atenção | Status |
|---|---|---|---|---|---|
| 92 | Você não precisa virar contador. | Precisa aprender a ler / o número da sua empresa. | o dono não faz conta de contador; ele lê o número pra decidir | MBV: "vocês não são contadores, vocês são empresários" | candidata |
| 93 | Ninguém abre empresa / pra pagar boleto. | Abre pra ter lucro. / Se não sobra, tem algo errado. | empresa existe pra deixar dinheiro no bolso do dono | âncora: "empresa nasceu pra gerar riqueza no bolso do dono" | candidata |
| 94 | Tem empresário que trabalha / 14 horas por dia | e ganha menos que / o próprio gerente. | o dono sem pró-labore trabalha mais e leva menos | dono não pode ser CLT da própria empresa | candidata |
| 95 | Venda resolve o mês. | Gestão resolve / a empresa. | vender tapa o buraco de agora; gestão impede o próximo | tamanho não paga conta | candidata |
| 96 | O problema da sua empresa / quase nunca é venda. | É o que acontece / depois que o cliente compra. | o cliente volta (ou não) pelo atendimento e pela entrega | MBV: "o problema não é venda, é atender" | candidata |
| 97 | Treinar uma vez / não muda ninguém. | O que muda o time / é repetir até virar hábito. | treinamento vira comportamento só com repetição | MBV: o erro "é achar que treinar uma vez resolve". Atenção: tese vizinha do 246 (18/10) | candidata |
| 98 | Seu time não faz / o que você fala. | Faz o que / você faz. | o exemplo do dono ensina mais que a regra | âncora: "o time copia o que o dono tolera". Atenção: vizinha do 239 (cultura, vidro e papel) | candidata |
| 99 | Dono que faz tudo sozinho / não tem uma empresa. | Tem um emprego / que não pode largar. | sem time e processo, o dono é refém do próprio negócio | Atenção: tese do 245 (16/10) | candidata |
| 100 | Preço só é caro | pra quem não viu valor. | ninguém discute preço quando entende o valor | frase do João ("ninguem questiona preço, quando entende valor"), reescrita; versão 2 de 6 | feita (post 253, fechado 19/10, flip chart; imagem flip-v7: a v5 sem o "o" antes de valor) |

## Lote 18 — modelos novos no molde do 230 (23/10, a crivar pelo João)

> Pedido do João em 23/10 ("precisamos de novas, vamos criar"), depois de postadas a cozinha, a bicicleta, o vaso, o relógio e o chefe. Objeto do dia a dia, lei física ou observada, pensador por baixo.

### 101. Buzina não abre trânsito. — `candidata`
- **De quem é:** Sêneca (a raiva não resolve o que está parado; só cansa quem sente). **Lei:** barulho e impaciência não andam o que está parado. **Cena:** fila de carros parados no sinal, um motorista com a mão na buzina.
- **Construções:** A. "Buzina não abre trânsito." · B. "Ninguém sai do engarrafamento buzinando." · C. "Grito não anda fila."

### 102. Parede torta começa no primeiro tijolo. — `em produção (post J286, 23/10)`
- **De quem é:** Platão (o começo é a parte mais importante do trabalho). **Lei:** o erro pequeno do começo cresce junto com a obra. **Cena:** parede de tijolo em obra, com o prumo mostrando a inclinação.
- **Construções:** A. "Parede torta começa no primeiro tijolo." · B. "Todo prédio torto teve um primeiro tijolo." · C. "O prumo se acerta na primeira fiada."

### 103. Quem nunca se perdeu nunca saiu do bairro. — `em produção (post J289, 24/10)`
- **De quem é:** Nietzsche (quem quer ir longe precisa aceitar se perder). **Lei:** se perder é sinal de que você foi além do que conhecia. Espelho de virtude ("eu fui longe"). **Cena:** mapa de papel dobrado e gasto no banco do carro, ou placa de estrada de terra.
- **Construções:** A. "Quem nunca se perdeu nunca saiu do bairro." · B. "Só se perde quem foi longe." · C. "Caminho conhecido não ensina nada."

### 104. Quem explica a matéria pro colega passa na prova. — `candidata`
- **De quem é:** Sêneca (ensinando, a gente aprende). **Lei:** ensinar é o jeito mais rápido de aprender. **Cena:** caderno aberto com a letra de dois alunos, um explicando.
- **Construções:** A. "Quem explica a matéria pro colega passa na prova." · B. "Ensinar é aprender duas vezes." · C. "Quem ensina a conta não esquece a conta."

### 105. Muda torta se endireita com estaca, não com bronca. — `candidata`
- **De quem é:** Aristóteles (o caráter se forma com hábito guiado). **Lei:** quem está crescendo precisa de estrutura, não de grito. **Cena:** muda pequena amarrada a uma estaca de bambu. **Atenção:** planta já no 249 (vaso seco, 20/10); espaçar.
- **Construções:** A. "Muda torta se endireita com estaca, não com bronca." · B. "Ninguém endireita planta no grito." · C. "Quem cresce precisa de estaca."

### 106. Faca cega corta mais o dedo. — `candidata`
- **De quem é:** Sêneca (o despreparo é mais perigoso que o risco). **Lei:** o que você deixa de afiar machuca quem usa; força no lugar de preparo escorrega. **Atenção:** a faca já apareceu no 76 (a pedra que amola), com outra tese.
- **Construções:** A. "Faca cega corta mais o dedo." · B. "Quem não afia faz força. E quem faz força se corta." · C. "O perigo é a faca sem fio."

### 107. Pipoca não estoura toda ao mesmo tempo. — `candidata`
- **De quem é:** lei observada (cada um tem o seu tempo). **Lei:** comparar o seu tempo com o dos outros é medir milho com relógio errado. **Atenção:** pode soar motivacional; a pipoca já esteve no 102 (pressão), com outra tese.
- **Construções:** A. "Pipoca não estoura toda ao mesmo tempo." · B. "Cada milho estoura na sua hora." · C. "Quem estoura depois não é piruá."

## Lote 19 — as três regras do que funcionou (26/10, a crivar pelo João)

> O João não gostou do que sobrou do lote 18 ("as que sobraram não sei se estou gostando"; "vamos criar mais"). Critério deste lote, tirado das que ele aprovou (bicicleta, cozinha, parede, se perder): (1) objeto que todo brasileiro tem em casa ou na rua; (2) lei física ou observada que ninguém discute; (3) espelho de virtude, quem compartilha sai bem na foto.

### 108. Só jogam pedra em mangueira carregada. — `em produção (post J291, 26/10)`
- **De quem é:** ditado popular ressignificado (Sêneca: a inveja só mira o que tem valor). **Lei:** crítica e ataque vão pra quem está produzindo; árvore sem fruto ninguém olha. Espelho: "se jogam pedra, é porque eu dou fruto". **Cena:** mangueira de quintal carregada, pedras no chão embaixo.
- **Construções:** A. "Só jogam pedra em mangueira carregada." · B. "Ninguém joga pedra em árvore sem fruto." · C. "Pedra no pé de manga é sinal de safra."

### 109. Fogo de palha não cozinha feijão. — `em produção (post J290, 26/10)`
- **De quem é:** Aristóteles (a virtude é hábito, não arroubo). **Lei:** empolgação acende rápido e apaga antes de cozinhar; o que sustenta é a brasa que demora. Espelho: "eu sou lenha, não palha". **Cena:** fogão a lenha com brasa firme debaixo da panela de feijão, e um punhado de palha queimada que já virou cinza ao lado.
- **Construções:** A. "Fogo de palha não cozinha feijão." · B. "Palha acende rápido e apaga antes do feijão." · C. "Feijão se cozinha é na brasa."

### 110. Vela não perde a luz acendendo outra. — `em produção (post J292, 26/10)`
- **De quem é:** Sêneca (o que se ensina não se perde). **Lei:** dividir o que você sabe não diminui você; só aumenta a luz da sala. Espelho: "eu acendo os outros". **Cena:** duas velas num pires, uma acendendo a outra, como em noite de queda de luz.
- **Construções:** A. "Vela não perde a luz acendendo outra." · B. "Quem acende outra vela não fica no escuro." · C. "Luz dividida não apaga."

### 111. Pão só cresce depois de sovado. — `em produção (post J293, 26/10)`
- **De quem é:** Sêneca (a dificuldade forma). **Lei:** a massa que apanha na sova é a que cresce no forno; massa que não foi trabalhada fica dura e baixa. Espelho: "fui sovado". **Atenção:** família da pressão (65 feijão, 102 pipoca).
- **Construções:** A. "Pão só cresce depois de sovado." · B. "Massa que não apanha não cresce." · C. "Todo pão bom já foi sovado."

### 112. Café bom passa devagar. — `em produção (post J294, 26/10)`
- **De quem é:** Sêneca (o que é bom leva tempo). **Lei:** água que passa rápido demais pelo pó faz café fraco; o sabor vem da paciência. Espelho: "eu sou café coado". **Cena:** coador de pano pingando devagar sobre o bule esmaltado.
- **Construções:** A. "Café bom passa devagar." · B. "Coador apressado faz café fraco." · C. "Ninguém apressa café coado."

### 113. Bambu enverga, mas não quebra. — `candidata`
- **De quem é:** Marco Aurélio (adaptar-se ao que vem sem perder a raiz). **Lei:** o que dobra com o vento sobrevive à ventania; o que fica duro quebra. Espelho: "eu envergo e volto". **Atenção:** imagem conhecida, pode soar clichê; a força está no "não quebra".
- **Construções:** A. "Bambu enverga, mas não quebra." · B. "Na ventania, quem não dobra quebra." · C. "Quem enverga volta."

## Lote 20 — mais cinco nas três regras (26/10, a crivar pelo João)

> Pedido do João em 26/10 ("crie mais 5 frases para eu poder escolher"), no mesmo critério do lote 19: objeto do dia a dia, lei que ninguém discute, espelho de virtude.

### 114. Ninguém tropeça deitado. — `candidata`
- **De quem é:** Sêneca (só erra quem está em movimento). **Lei:** tropeço é prova de que você está andando; quem nunca tropeça está parado. Espelho: "eu tropeço porque ando". **Cena:** um tênis com a ponta ralada ao lado de um degrau de calçada quebrado.
- **Construções:** A. "Ninguém tropeça deitado." · B. "Só tropeça quem está andando." · C. "Tropeço é coisa de quem saiu do sofá."

### 115. Canoa só anda pra frente com o remo puxando pra trás. — `candidata`
- **De quem é:** Heráclito (os opostos se puxam). **Lei:** avançar exige um esforço que parece ir na direção contrária: guardar, recuar, estudar, parar pra pensar. Espelho: "eu remo". **Cena:** canoa de madeira na beira do rio com o remo apoiado.
- **Construções:** A. "Canoa só anda pra frente com o remo puxando pra trás." · B. "Quem rema puxa pra trás e vai pra frente." · C. "Todo avanço tem uma remada pra trás."

### 116. Quem acende a churrasqueira come por último. — `candidata`
- **De quem é:** Aristóteles (quem lidera serve primeiro). **Lei:** quem cuida do fogo serve todo mundo antes de se servir; liderar é isso. Espelho de virtude ("eu sou o do fogo"). **Cena:** churrasqueira de tijolo com a carne no espeto e um prato vazio ao lado. **Atenção:** vizinha do chefe que lavou panela (J263), ideia de servir antes de mandar.
- **Construções:** A. "Quem acende a churrasqueira come por último." · B. "O churrasqueiro é o último a sentar." · C. "Quem cuida do fogo serve antes de comer."

### 117. Abacate não amadurece no pé. — `candidata`
- **De quem é:** lei observada (fato pouco conhecido: o abacate só amadurece depois de colhido). **Lei:** tem coisa que só fica pronta depois que você sai de onde nasceu. Espelho: "amadureci quando saí". **Cena:** abacates na fruteira amadurecendo, o pé ao fundo.
- **Construções:** A. "Abacate não amadurece no pé." · B. "Tem fruta que só fica pronta longe da árvore." · C. "Quem não sai do pé não amadurece."

### 118. Caneta que acabou foi a que mais escreveu. — `candidata`
- **De quem é:** lei observada (o desgaste é a marca do uso). **Lei:** o que se gasta é o que foi usado; quem se poupa sobra inteiro e sem história. Espelho de virtude ("eu me gastei fazendo"). **Atenção:** mesmo mecanismo do sapato gasto (85), que o João descartou.
- **Construções:** A. "Caneta que acabou foi a que mais escreveu." · B. "Caneta cheia é a que ninguém usou." · C. "Toda caneta vazia tem uma história."
