---
name: frase
description: Cria o post de FRASE ÚNICA do Hélio (uma imagem só, um por dia, pronto pras 9h) — uma lei curta em português falado sobre o fundo de papel envelhecido, com imagem P&B gerada por IA, e uma legenda longa que desenvolve a lei e fecha na pergunta-espelho + CTA fixo de seguir. Use quando pedirem "a frase de hoje", "uma frase", "post de frase", "frase com imagem", "vamos de [semente do banco]", "abre um lote de frases" ou mandarem uma frase pra virar post único. NÃO é carrossel (/carrossel) nem frase com foto real do Hélio, papel ou vidro (/frase-foto).
---

# /frase — a frase diária do Hélio

Post de **uma imagem só**, 1080x1350: a frase (uma lei curta) no alto, sobre o fundo de papel envelhecido, e uma imagem P&B gerada por IA na metade de baixo, que mostra o mecanismo da lei. A legenda desenvolve a lei pra vida de qualquer pessoa, passa pelo dono de empresa e fecha na pergunta-espelho + CTA fixo de seguir. O objetivo do formato é **alcance** (furar a bolha), não lead.

"O user", aqui, é quem está operando: quem escolhe, aprova e posta.

**Ler antes de começar:**
1. `_contexto/preferencias.md`: a voz da casa, base de qualquer peça (inclui a regra de escrita humana: sem travessão como pausa, sem vírgula empilhada).
2. `referencias/diretriz-frase-legenda.md`: a diretriz do user pra frase e legenda (a nota do topo diz o que caiu).
3. `referencias/legendas-gabarito-2026-10.md`: cinco legendas publicadas, com a anatomia de cada uma.
4. `conteudo/banco-frases.md`: as sementes e o que já saiu.

Histórico, só pra consulta: `referencias/legenda-campea-raso.md` (gabarito de agosto, com o fecho superado) e `referencias/historico-aprendizados.md` (o que saiu do método; não seguir).

**Ferramentas da skill:** `template/slide-frase.html` (o slide), `template/prompts.json` (o prompt-base), `scripts/gen.py` (gera), `scripts/edit.py` e `scripts/edit_tall.py` (ajustam a própria imagem), `scripts/legenda.py` (conta caracteres e confere a legenda publicada).

Todo comando roda **da raiz do projeto**. Atalhos usados abaixo: `S=.claude/skills/frase` e `P=conteudo/carrosseis/<N>_<nome>` (a pasta do post).

**A pasta do post** segue a mesma numeração dos carrosséis (`<N>` = próximo número livre; seção 10) e tem: `_scripts/prompts.json` (e os logs), `imagens/img-NN.png`, `instagram/slide-01.html` e `.png` (alternativas em `instagram/_rodadas/`), `legenda.txt` (a corrente), `legenda-vN.txt` (as anteriores) e `carousel-text.md` (o registro do post).

Esta skill é independente da `/carrossel` e da `/frase-foto`: nunca editar os arquivos delas daqui. Do resto do projeto, só lê o fundo e o banco de referências (`conteudo/carrosseis/_banco-referencias/`, que vive no Drive).

---

## 1. Cadência e combinados com o user

- **Uma frase por dia, pronta pra sair às 9h** (user, 02/10).
- **Uma frase por vez** (22/09: "Calma, uma frase por vez"). A próxima começa depois que a atual fechou.
- **Mostrar antes de fechar** (23/09: "mostra as construções antes"). Nada fecha sem o "vai" do user. Entrega pronta, decidida sozinha, só se ele pedir.
- **Formato de cada rodada, tudo numa mensagem só** (desde 02/10; antes disso o user cobrou "cadê a imagem" três vezes):
  1. a lei (seção 3);
  2. 2 a 5 construções da frase, com a que está no slide marcada;
  3. a legenda inteira no chat, com o número de caracteres;
  4. 2 a 4 imagens já montadas no slide, cada uma com um nome curto, uma linha do que ela diz e a sua indicação; as duas mais fortes abertas no Preview, todas na pasta do Desktop (seção 9);
  5. o bloco final **"Preciso de você, numa resposta só:"**, numerado (o user responde "1. ... 2. ...").
- **O user edita a legenda direto no `$P/legenda.txt`**, às vezes sem avisar (230). Reler o arquivo antes de qualquer passo e antes de fechar.
- **Versões numeradas, nunca descartar a anterior.** Antes de reescrever a legenda, salvar a atual como `legenda-vN.txt` (a que o user marcou vira `legenda-vN-marcada-user.txt`); a corrente é sempre o `legenda.txt`. Imagem nova é número novo (`img-NN`); slide alternativo é arquivo novo. Mostrar a nova ao lado da antiga. Motivo: em 8 peças o user pediu uma mudança e voltou à versão anterior (223: "eu gostei da primeira... que já não existe mais... e agora?"). Pelo mesmo motivo, **correção pedida no meio da rodada só vira regra se a escolha final confirmar**.
- **Opinar antes de alterar.** Quando o user pergunta "o que você acha?" ou propõe algo, dar a opinião com argumento e esperar, sem mexer no arquivo (11/10: "Me fale antes de alterar"). Concordar quando ele tem razão e discordar com argumento quando não tem (22/09: "sempre com compromisso com a verdade e como melhor resultado, não em me agradar"). Elogio não é ordem: no 225 ele elogiou uma linha da legenda, o Claude a pôs no slide, e ele explicou que "foi só um feedback".
- **Frase que o user manda vai literal** (08/10). Ajuste de ritmo ou de gramática é sugestão: a arte fica com a frase dele até ele aprovar a mudança.
- **Conferir o dia com `date`** antes de escrever qualquer dia da semana, no chat ou nos arquivos: `LC_ALL=pt_BR.UTF-8 date '+%A %d/%m/%Y %H:%M'` (pra outra data: `LC_ALL=pt_BR.UTF-8 date -j -f '%d/%m/%Y' '14/10/2026' '+%A'`). O Claude errou o dia várias vezes em outubro, e dois erros ainda estão nos arquivos do 209 e do 225.
- **Gatilhos:** "vai" / "legenda vai" = aprovada; "pode fechar" = fechar o pacote; "vou postar agora" = abrir o PNG final e a pasta na hora; "postei" = marcar data e hora.
- O user às vezes fala por voz e a transcrição vem embolada: interpretar, sem pedir texto limpo.

## 2. As sementes

As sementes vivem em `conteudo/banco-frases.md`, em lotes numerados, com o status entre crases no título de cada uma: `candidata`, `aprovada`, `feita (...)`, `descartada (motivo)`, `stand-by`.

**De onde vêm hoje:**
- **Ideia de pensador de primeira linha, traduzida pro cotidiano brasileiro** (método do user, 10/09: "Seremos mais um tradutor do que um elaborador"). Sêneca, Epicteto, Marco Aurélio, Aristóteles, Platão, Sócrates, Heráclito, Kant, Epicuro, Nietzsche. Entre eles, quem decide é a ideia (23/09). O cotidiano é a tradução, não a origem: as ideias que partiram do objeto ficaram sem nada por trás (24/09).
- **Lei observada da vida, sem pensador** (225).
- **Infância**, como tempero (ver abaixo).
- **Ditado popular ressignificado**: frase nova por cima do ditado que todo mundo fala, e a legenda explica (138, grama do vizinho).
- **Insight do user dentro de uma legenda**, registrado como candidata (a "limpa" do 223 virou a 70; o sonho do 225 virou a 79).
- Caso, não regra: a data comemorativa do dia, quando o user pede (225, Dia das Crianças).

Não são mais fonte: frase de "veia empresarial direta" (caiu em 26/08: nunca nichar) e garimpar a cena antes de ter a ideia.

**Crivo:** o Claude abre o cardápio e o user escolhe. Lote de 5 a 8 sementes, cada uma com a lei em uma linha, de quem é a ideia, a cena e 2 ou 3 construções. Sem ranking e sem "minha escolha": o Claude só aponta colisão e risco.

**Ordem:**
- Infância é tempero, não cardápio: uma a cada ~3 posts, com vida adulta entre elas, porque só infância "perde a identidade do Hélio" (24/09). O espaçamento não é rígido quando o user escolhe (o 225 saiu dois dias depois do 209).
- Intercalar também lei direta e frase de objeto (seção 4).
- **A mesma tese não sai de novo com poucos dias** (23/09: "muito igual para postarmos com poucos dias"). O mecanismo e o universo podem repetir (24/09: "não é que o universo não pode se repetir, isso não tem nada a ver").

## 3. A lei, antes de tudo

Antes de qualquer frase, legenda ou prompt, escrever em uma linha, na voz da casa: **a lei, a leitura escolhida e de quem é a ideia.** Depois conferir as últimas ~10 frases publicadas (no `registro-posts.csv` ou nos `carousel-text.md`) pra não repetir a tese.

Nasceu no 181: nove rodadas de imagem até o user cortar: "vamos começar de novo, qual a lei, qual a ideia que queremos transmitir? de quem é?". A mesma frase pode ter leituras diferentes, e a leitura decide a legenda e a imagem. Ex.: o peso que revela (166, laje), o teste que constrói (181, gesso), o preparo que traz a calma (187, mala).

A lei vai pro `carousel-text.md`. De quem é a ideia fica só lá e no banco, nunca na legenda.

## 4. A frase

A base é a seção A da `diretriz-frase-legenda.md`: verdade que incomoda, funciona sozinha, provoca antes de ensinar, tem segunda camada, nada de motivacional. O que o user firmou depois:

- **Português falado do Brasil** (08/09: um lote inteiro reprovado por soar traduzido). Recursos: clivagem com "é" ("Bolo cresce é de porta fechada"), elipse de ditado ("Basta uma madura pra amadurecer a penca"), ordem invertida, verbo da casa ("picar", não "cortar"), gíria que coincide com a lei física ("vazar", "estourar"). Fora: o molde "X é o Y que Z".
- **Referência de molde: "No raso não existe pressão."** (29/09: "lembre-se da inspiração 'no raso não existe pressão'"). Saíram nele, por exemplo: "Dente de leite não foi feito pra ficar.", "A água não esquenta pra quem fica na borda.", "Varal frouxo não segura roupa."
- **Duas famílias convivem:** a frase de causo, com o objeto dentro ("Laje só se conhece com peso em cima."), e a lei direta, com o objeto só na imagem ("Toda ocasião especial era um dia comum.", "O que você evita é o que te governa."). Quando a frase sobre o objeto sai fraca, ela vira a lei e o objeto fica só na imagem (175: "A frase não precisa ser necessariamente sobre a louça"; também 176 e 209).
- **Símbolo concreto, na frase ou na imagem** (24/09: "a frase precisa ter um simbolo mais real do que sentimento"). Se a frase é a lei nua, o símbolo está na imagem.
- **Universal, nunca nichada** (26/08). A frase serve pra qualquer pessoa; a empresa só entra na legenda (o 43, nichado a empresário, flopou). O símbolo sai da vida comum do brasileiro (casa, rua, cozinha, obra); teste: "qualquer brasileiro já viveu isso?". Mapa, farol, forja e montanha ficam distantes. Precisa de "molho": a ideia certa dita sem tensão também reprova. Vocabulário de marketing ("posicionamento") não é voz do Hélio.
- **Compartilhável:** quem compartilha tem que sair bem na foto ("eu aguento", "eu me movo"). Frase que adverte ou acusa o leitor circula pouco (24/09: "pouco compartilhável").
- **A palavra exata tem que ser verdadeira pro sujeito.** No 225, "vergonha" e não "medo": criança tem medo, o que ela não tem é vergonha. No 136, "fome" e "ambição" são palavras positivas na casa; o negativo é a "falta".
- **Sensibilidade:** palavra ou desenho que pode excluir ou confundir alguém sai do slide. Casos: "pai" saiu da frase do 209 ("pode ser confundido com religião"; na legenda ficou); o desenho de família virou mãe e criança (225).
- Técnica opcional: quando a legenda sai melhor que a frase, a frase pode nascer de uma linha dela (130, 131, 133).
- Antes de fechar, confirmar a frase final (em 20/09 o user trocou de frase no meio do render).

## 5. A legenda

A base é a seção B da diretriz, com a nota do topo. O que vale hoje:

**Ordem.** A legenda é escrita junto com a frase e vai na mesma rodada. Quando a frase muda, a legenda é adaptada a partir da nova frase, não remendada (02/10: "A legenda precisa ser adaptada agora para a frase, né?").

**O caminho das aprovadas** (padrão, não molde; os cinco gabaritos mostram as variações):
1. abre por gente e cena, ou pela lei em uma linha curta;
2. o objeto físico num parágrafo só;
3. a lei na vida adulta, em categorias abertas;
4. o dono de empresa, entrando pelo personagem;
5. a ressalva, como fato;
6. uma linha de fecho;
7. a pergunta-espelho;
8. o CTA fixo.

**Como o texto anda:**
- **Fio único** (09/09): cada parágrafo nasce de uma palavra ou ideia do anterior; a empresa entra de dentro do fio. Metáforas do mesmo parágrafo casam entre si (quarteirão pede esquina, não tarde).
- **Fluida, não blocada** (18/09): prosa encadeada, com conjunção; o punch curto só no fecho do parágrafo. Frase curta em série soa como slogan empilhado.
- **Concreta** (05/10): três parágrafos de tese seguidos reprovam ("meio abstrato demais"). Abrir por gente e cena e deixar a lei pro fecho do parágrafo.
- **Nunca abrir pelo óbvio nem explicar o objeto:** "todo mundo dorme no escuro claude" (11/09); a pipoca "explicou demais o processo físico" (09/09); a laje "fala muito de laje", virou "conteúdo emocional para pedreiro" (29/09).
- **Verossímil e fisicamente certa:** "Pressão sem panela... não faz sentido" (09/09); "Não tem quem fique calmo nessa hora", sobre a bolsa estourando (05/10).
- **Não anunciar a metáfora** nem pôr um narrador abstrato ("a natureza ensina", "a vida mostra que"): o elemento concreto carrega a lei (14/08).
- **Categorias, não biografia** (01/09): exemplos que o leitor completa com a vida dele ("um casamento com raiz, um trabalho com sentido"), nunca a vida de outra pessoa já contada ("um pai que apanhou calado").
- **A parte universal é a principal** (28/08): ela tem pelo menos tantos exemplos concretos quanto a parte da empresa.
- **Profundidade** é a 2ª e a 3ª camadas da ideia, não a primeira explicada de novo (11/09).
- **Sem o nome do pensador** (17/09: "não fale do pensador ok? vamos só com o pensamento"). Nada de "como dizia X" ou "há dois mil anos".
- **Costura que não liga: consertar com o mínimo.** No 223 o user achou que uma frase de ligação "não dá muita liga"; o Claude reordenou a legenda inteira e ele rejeitou; resolveu trocando só aquela frase.

**O parágrafo do dono:**
- O dono é o da pequena e média empresa, "que conhece o processo todo, já fez de tudo na empresa e ainda faz" (05/10).
- **Nunca decisão de número como gesto emocional** (12/10). "Contratar gerente sem saber liderar" contradiz o que a casa ensina ("para delegar uma área, você tem que entender dessa área"), e "mudar o preço" exige conta, não coragem. Em tema emocional, o dono aparece em gestos emocionais: gravar o vídeo, falar na frente do time, mostrar a ideia antes de estar pronta, pedir ajuda. No 113 (11/09), "demitir e elevar o preço" virou "estudar liderança, gestão".
- A responsabilidade é do dono, sem moralismo (diretriz §16).

**A ressalva** (o parágrafo que fecha a leitura errada da lei) entra como fato, sem avisar que vem ressalva, e cada legenda inventa a forma dela (28/08: "todo parágrafo anti-burro é igual, sendo que eles devem ter sua própria estrutura"; a muleta da época era "Agora, cuidado com...").

**Construções proibidas (cara de IA):**
- "Não é sobre X, é sobre Y" (o user, 01/10: "vicio de linguagem de IA");
- "Na empresa é o mesmo X" e parentes (09/09, "Na empresa o fogão é o mesmo": "virou vicio de IA");
- "Quem já X sabe:" e "Todo mundo que já X sabe:" (13/10: "muito IA");
- "Com a nossa vida funciona igual" (13/10: vício);
- palavra esquisita ("encosta") e frase de efeito que não diz nada claro (01/10).

O princípio vale mais que a lista: **dizer a mesma coisa com outras palavras, nunca com a mesma fórmula fixa.** "Isso não é X" é permitido, mas não pode virar a forma de toda legenda (já está no 134 e no 230).

**Fecho:** a pergunta-espelho e, num parágrafo separado, o **CTA fixo, literal** (11/09: "quero que termine sempre assim"):

> Se você se sentiu provocado a refletir sobre sua vida hoje, me siga. Todo dia pela manhã posto uma reflexão buscando provocar você em direção ao seu aperfeiçoamento pessoal.

O objetivo continua sendo alcance; o CTA é pra quem gostou continuar acompanhando. Sem palavra-chave e sem Manychat.

**Tamanho:** a parede do Instagram é **2.200 caracteres com o CTA**; as aprovadas recentes ficam entre ~1.930 e 2.200. Passou: trocar uma ideia por outra ou cortar uma ideia, nunca o CTA. Contar **caracteres, não bytes** (acento conta 1): `python3 $S/scripts/legenda.py contar $P/legenda.txt`. O `wc -c` conta bytes e já deu dois falsos alarmes (166, 168), e duas legendas foram ao ar cortadas no fim sem ninguém ver (101, 112). Recontar sempre que o user editar.

**Revisão de português, sempre** (02/10: erro de português "não pode acontecer nunca"): concordância, sentido, pronome ambíguo, "porque" × "por que", e nunca "te" com "você/seu" na mesma frase (223: "te digo que você" virou "E você, empresário que me lê"). O `legenda.py contar` aponta as construções proibidas e o te + você, mas não substitui ler a legenda inteira.

## 6. A imagem

**O padrão desde 29/09 é o molde da prateleira:** um objeto, ou uma cena curta, contra uma parede de reboco lisa e clara, apoiado na base, na metade de baixo do quadro. O gabarito é o post 57, "Prateleira vazia não verga" (banco de referências, `374.png`, no Drive). Doze das treze imagens finais entre o 166 e o 230 são assim. É padrão, não proibição de cena: o 209 é uma cena (a mão soltando o selim e a criança pedalando), pedida pelo user ("mais sobre o movimento").

- **Mínima:** a primeira opção é sempre a de menos elementos; pessoa só entra quando a cena precisa dela (17/09: "pouco poética, muita informação na imagem"; 22/09: "não vamos colocar humano").
- **Diz o mecanismo sozinha** (05/10: "não transmitem a mensagem por si só"). Objeto só "gasto" não diz "testado". Teste: quem vê só a imagem com a frase entende o que ela diz?
- **Altura:** o sujeito apoiado na base, terminando abaixo do meio do quadro. Nada entra por cima (02/10: "qualquer objeto que vem de cima vai pegar o texto"); mão ou pé entra pela lateral ou por baixo. Também não pode ficar baixo demais (12/10, geladeira "parecendo mais um forno"; 13/10, varal "muito muito baixo"). Objeto que precisa subir: usar a `base_alto` do `prompts.json`.
- **Real:** o user pega o que tem cara de IA: anatomia (perna faltando, coxa alongada, braço "monstro"), escala (pipoca com casca de ovo) e física (prato "flutuando"; o objeto precisa estar apoiado em algo, e a poeira tem que ser coerente com o que estava parado).
- **Tom realista e do cotidiano:** sem mito, estátua, herói ou surreal (02/10: marionete e sombra "distoantes do padrão nosso"; 05/10: Aquiles "muito mitológico", punho ao alto e raio de luz "mais drama que herói"). Nos dois casos, a ideia rejeitada tinha sido do próprio user.
- **Brasil real, não americanizado nem genérico** (29/09: "nenhum dos dois parece realidade brasileira"; 12/10: a geladeira "norte-americanizada" virou uma Consul de entrada, com ímã de loja de gás do bairro).
- **P&B puro.** Saiu com tom de cor: converter (seção 7).
- **Nunca gerar o Hélio por IA** (proibido, 13/10).
- **2 a 4 opções por rodada**, cada uma com nome e leitura, e a sua indicação.

**Prompt:** copiar `$S/template/prompts.json` pra `$P/_scripts/prompts.json` e escrever as cenas em inglês. A `base` deixa a metade de cima como parede lisa; a `base_alto` deixa só os 30% de cima, pra objeto mais alto (os postes do 230). A cena diz o objeto, onde ele está apoiado, que fica na metade de baixo, e termina em "Nothing else."

## 7. Ajustes de imagem

Pedido de ajuste ("Faça só isso sem mexer em mais nada") muda só o que foi pedido. Do mais leve pro mais pesado:
1. **CSS no slide**, sem regerar (receitas no comentário do template): mover a frase (`top`), zoom no sujeito (`scale` com a origem nele; 113 a 1,75x), ampliar ancorado na base pra subir o objeto, esticar só na vertical até ~9% a mais (225: `scale(1.15,1.24)`), alongar a máscara quando algo escuro sobe até a frase.
2. **Image-edit da própria imagem:** `python3 $S/scripts/edit.py $P img-04.png 9 "<pedido em inglês>"`. Corrige um detalhe mantendo cena, luz e grão (a casca da pipoca no 102, o joelho no 145). Não sai pixel-idêntico: avisar o user.
3. **Outpaint:** `edit_tall.py`, mesmos argumentos, saída em retrato, pra completar a cena pra cima ou pra baixo e compor com a original. Conferir a emenda no zoom (no 136 o composite saiu com o telhado duplicado).
4. **Regerar** com o objeto já na posição certa, quando esticar passaria de ~9% (225, 230).

Toda versão é arquivo novo; a anterior fica. P&B puro: `python3 -c "from PIL import Image; Image.open('$P/imagens/img-32.png').convert('L').convert('RGB').save('$P/imagens/img-32-pb.png')"` (181). Elemento claro (água, fumaça, luz) some no `multiply` quando o entorno também é claro: pedir fundo escuro atrás dele (14/08).

## 8. O slide

- Copiar `$S/template/slide-frase.html` pra `$P/instagram/slide-01.html` e trocar só a frase e o `img-NN`. O template rende o slide publicado do 230 e do 225 pixel a pixel (conferido em 13/10).
- 1080x1350, fundo `#F5F0EB` + `_banco-referencias/background para carrosséis.png`, Source Serif Pro 700, **frase toda em preto** (`#1A1A1A`, como todas as de setembro e outubro), **44px**, `top:300px`, centralizada. Vermelho só se o user pedir.
- **Regra das duas linhas:** cabe numa linha a 44px com folga das margens, fica numa linha. Encostou na margem de 36px, **duas linhas a 44px**, com a quebra no respiro natural da fala (187: "Não existe calma / que não tenha sido conquistada."; o user preferiu a quebra à fonte menor). Nunca diminuir a fonte pra caber.
- Imagem ancorada na base, largura total, `multiply` e fade de 0 a 26% no topo.
- Render: `npx playwright screenshot --viewport-size=1080,1350 --wait-for-timeout=1100 $P/instagram/slide-01.html $P/instagram/slide-01.png`. As alternativas da rodada são `slide-01-b.html`, `-c`...; quando a escolha sai, elas vão pra `$P/instagram/_rodadas/`.
- **Toda rodada termina com os PNGs abertos no Preview**, não só a entrega final.

## 9. Fechamento do pacote

Com a imagem escolhida e o "legenda vai":
1. **Conferir o que vai fechar:** a frase final, a imagem escolhida e o `legenda.txt` relido. Comparar com a sua última versão (`diff $P/legenda-vN.txt $P/legenda.txt`): se o user mexeu, dizer o que mudou, e nunca registrar "aprovada sem edição" sem comparar (no 230 ele tinha cortado a abertura sem avisar). Contar com o `legenda.py contar`.
2. **`$P/carousel-text.md`:** semente (`banco-N`, lote, de quem é a ideia), lei declarada, frase (construção, cor, linhas, `top`), imagem final e o percurso das rodadas, legenda final (versão, caracteres com o CTA, o que o user mudou), publicação (dia da semana conferido com `date` e hora).
3. **Banco:** o status da semente vira `feita (post N, publicado AAAA-MM-DD (dia da semana) ~hora; lei; imagem; percurso curto)`. Insight novo do user entra como candidata no lote aberto.
4. **Etiqueta:** rodar `/etiqueta` (formato `frase`; objetivo `alcance`; o dado final é o total de compartilhamentos em D+7 contra a régua do dia; sem palavra-chave; sem Manychat). O campo `semente` começa pelo número do banco, como nas fichas recentes: `banco-71 (lote 14; lei direta; Heraclito traduzido)`.
5. **Desktop:** `~/Desktop/frases claude/<palavra>/` (uma palavra do tema) com um único `<palavra>.png` (o slide final) e o `legenda.txt`. Durante a decisão as candidatas ficam lá com nome descritivo; no fechamento elas saem (as versões continuam no repositório). Nunca usar `carrosseis claude/`. O user move a pasta pra `POSTADOS/` depois de postar; essa pasta é dele.
6. Abrir o PNG no Preview e a pasta no Finder: `open -a Preview "<png>"` e `open "<pasta>"`.
7. **Commit** conforme a regra de commit da máquina (CLAUDE.md).
8. **No "postei":** marcar data e hora no `carousel-text.md` e na ficha, com o dia da semana tirado do `date`.
9. **Depois de publicado**, quando o post aparecer no `desempenho.json` (atualizado todo dia ~9h): `python3 $S/scripts/legenda.py publicada $P`. O que foi ao ar vale, porque o user mexe na hora de postar: registrar as diferenças no `carousel-text.md`. Se a publicada não terminar no CTA inteiro, avisar o user na hora pra corrigir o post.

## 10. Motor e gotchas

- **Proxy de imagem** (`openai-oauth`, porta 10531, com o login do `~/.codex/auth.json`; setup na skill `gpt-image2-ratos`). Cai quase toda manhã ("fetch failed" ou conexão recusada). Testar: `curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:10531/v1/models`. Subir: `npx -y openai-oauth --port 10531 > proxy.log 2>&1 &`. Relançar sem perguntar e explicar que é instabilidade do túnel, não limite de conta (05/10: "esta falhando pq?"). Erro 401 ou 403 é login vencido: o user roda `npx @openai/codex login`.
- **Gerar:** `python3 $S/scripts/gen.py $P 1 > $P/_scripts/gen-01.log 2>&1 &`, um processo por imagem, em paralelo (20 a 110 s cada). O script avisa se o proxy estiver fora e pula número que já existe.
- **Moderação:** criança de rosto frontal olhando a lente, em ambiente institucional, é barrada (113: sete vezes). De costas, de perfil ou de três quartos passa.
- **Número da pasta:** outras sessões criam posts em paralelo, e houve colisão em quase todo post de 132 a 230. Conferir o próximo número livre logo antes do `mkdir` (`ls conteudo/carrosseis | sort -n | tail -5` e `ls -d conteudo/carrosseis/<N>_*` pro número escolhido). **Nunca renomear a pasta com o gen rodando**: o script grava no caminho que leu ao começar, e a imagem se perde (132 e 135).
- Outra sessão gerando no mesmo proxy é normal: não parar a fila por isso.
- Espera em segundo plano pode morrer quando passa do tempo ou quando a sessão troca: reconferir `$P/imagens/` e os `gen-NN.log`.
- **Dados do Instagram:** nunca chamar a API direto e **nunca rodar `pull_insights.py pull`** (CLAUDE.md). Se o `desempenho.json` tiver mais de 24 h, só `python3 scripts/instagram/pull_insights.py update`.
- **PC novo:** liberar `~/Desktop/frases claude/` nas permissões do app (fica fora do projeto e pede confirmação a cada escrita; 05/10) e fazer o login do Codex.

## Mudar esta skill

Só com o sim do user, e só com o que ele disse ou fez, nada suposto (07/10: "nada que você supôs, somente o que vc tem como base nos fatos"). Correção de uma peça só, ou gosto visual de uma imagem, não vira regra; no máximo vira caso. O que sair do método vai pro `referencias/historico-aprendizados.md`, com a data.
