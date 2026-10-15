# Histórico de aprendizados da /frase — NÃO SEGUIR

> **Histórico, não regra.** O método vigente está no `SKILL.md`. Aqui fica o que saiu do corpo da
> skill na reescrita de 13/10/2026, com a data e o motivo, pra consulta. Se algo daqui parecer útil
> de novo, só volta pra skill com o sim do user. O texto integral das versões anteriores do
> `SKILL.md` está no Git: `git log -p -- .claude/skills/frase/SKILL.md`.

## 1. Regras que foram substituídas

| Antes | Hoje | Quando mudou |
|---|---|---|
| Palavra-punch em vermelho `#A91C20` como padrão (11/08); "confirmar a cor no checkpoint" (14/08) | Frase toda em preto; vermelho só se o user pedir | prática desde 13/08; todas as frases de setembro e outubro saíram em preto |
| Frase curta a 44px e frase longa em 2 linhas a 38px (12/08), depois 40px | Duas linhas a 44px, quebra no respiro da fala | 05/10 (187) |
| Crop-zoom `scale(1.4)` no personagem por padrão; composição de profundidade sem zoom (12/08) | Zoom só como ajuste pontual, quando o user pede | prática de setembro e outubro |
| Propor 3 conceitos de imagem; "composição de profundidade/misteriosa vence"; "exemplar mais dramático/icônico" (catarata, galeão; 12/08 a 14/08) | Molde da prateleira: mínima, objeto apoiado na base, nada épico | 17/09 a 29/09; 05/10 |
| Prompt-base com "névoa densa" na metade de cima | Prompt-base com parede de reboco lisa (`template/prompts.json`) | 29/09 |
| Alternar a frase filosófica com frase de "veia empresarial direta" (14/08) | Nunca nichar; a empresa só entra na legenda | 26/08; reconfirmado em 10/09 e 24/09 |
| Propor versões encurtadas que apontam o dedo pro leitor, "sua cabeça/sua empresa" (Passo 1) | Frase universal em português falado | 26/08 e 08/09 |
| Garimpar a cena primeiro e a frase depois (lotes 8 e 9) | Ideia (de pensador ou lei observada) → cena → frase | 10/09 e 24/09 |
| O user manda a legenda pronta (Passo 5) | O Claude escreve junto com a frase; o user edita no `legenda.txt` | setembro |
| Legenda escrita antes da frase final, e a frase tirada de uma linha dela (método de 07/10, §3) | A lei primeiro; frase do banco; legenda junto; frase a partir da legenda é técnica opcional | prática desde 05/10 |
| A frase volta no fim da legenda como ponto final, nada depois dela (diretriz §30 e §31, gabarito do raso, estrutura-raiz; exceção de cadência de 28/08) | Pergunta-espelho + CTA fixo de seguir | 11/09 |
| "Post de frase não leva CTA" | CTA fixo de seguir; o objetivo continua alcance | 11/09 |
| O pensador citado em meia linha (11/09) | Nunca nomear o pensador | 17/09 |
| Teto de 1.400 caracteres, depois 1.800; ~2.100 só na estrutura-raiz | Parede de 2.200 com o CTA, contando caracteres | setembro |
| Medir com `pull_insights.py pull` 3 ou 4 dias depois; régua de taxa shares/alcance (~1% saudável) | Dado local atualizado todo dia, nunca `pull` (CLAUDE.md); fecha em D+7 com compartilhamentos absolutos (regime 3 da `/etiqueta`) | 14/09 |
| Entrega pronta, com frase, imagem e legenda decididas pelo Claude | Mostrar antes (a de 21/09 foi pedido do user naquele dia) | 23/09 |
| Infância como padrão | Infância é tempero, uma a cada ~3 posts | 24/09 |
| "Ponte curta pra vida: Com a nossa vida funciona igual." (estrutura-raiz, item 7) | Proibida | 13/10 |
| "Isso aqui não é X" queimado junto com "Agora, cuidado com..." (28/08) | "Isso não é X" permitido, sem virar fórmula | 13/10 |
| Checkpoint "frase aprovada antes de gerar qualquer imagem ou HTML" (12/08) | Formato da rodada: lei, construções, legenda e imagens juntas; nada fecha sem o "vai" | 02/10 |
| "Seguir `.claude/skills/carrossel/referencias/motor-imagem.md`" | Scripts da própria skill (`scripts/`) | 13/10 (o arquivo da carrossel descrevia um caminho antigo) |

## 2. O que saiu ou não virou regra na verificação de 13/10

- **Varrer universos recentes antes de escolher o cenário** (estava no método de 07/10; veio do carrossel 105, 09/09): saiu. Pra frase, em 24/09 o user disse que o universo pode repetir ("isso não tem nada a ver"); o que não repete é a tese.
- **Ler `_contexto/o-que-funciona.md` antes de propor** (Passo 1, 14/08): saiu. O arquivo é a análise de 14/08 e manda rodar `pull`, que o CLAUDE.md proíbe.
- **Oferecer salvar a imagem aprovada no banco de referências** (Passo 6, 12/08): saiu da skill. O fluxo de imagem nova pro banco está no CLAUDE.md.
- **"O user mantém o que pareça IA se for melhor textualmente"** (174, 02/10): caiu com a proibição de "Quem já X sabe:" (13/10); no 230 ele mesmo apagou uma abertura desse tipo.
- **Não repetir o mecanismo com poucos dias:** não é regra (13/10). O que não repete é a tese.
- **Escolher a imagem que conta a mesma história da legenda:** não é regra. No 166 o user escolheu a que contava outra coisa.
- **Imagem "de classe média, nunca pobre":** não é regra. No 230 o user pediu "menos pobre", viu a versão de apartamento e voltou pro quintal ("vou manter [a antiga]").
- **Fazer a frase do dia seguinte na véspera:** sem regra (13/10).
- **Casos que ficaram como exemplo, não regra:** imagem no lado positivo da lei (38, 14/08); dente "macabro" e mão de criança "zoada" trocada por mão adulta (168; depois houve criança no 209 e no 225 sem problema); data comemorativa (225); cor residual na imagem (181); "doente mentalmente" trocado por "azedo por dentro" (101, troca do Claude).

## 3. Texto antigo do SKILL.md, movido sem edição

Os três blocos abaixo saíram do corpo da skill como estavam. O que deles continua valendo foi
reescrito no `SKILL.md` (ressalva sem anúncio, categorias sem biografia, a parte universal como a
principal, "não anunciar a metáfora", os truques técnicos de máscara, sangria e multiply).

### 3.1 Aprendizados (12/08 a 28/08)

- **2026-08-12 (post 36):** fonte de frase curta: 56 → "menor" → 30 → "pequeno demais" → **44px aprovado**. Faixa boa: 38-44.
- **2026-08-12 (post 36):** o usuário trocou um conceito frontal já renderizado por uma composição de profundidade (câmera rente ao solo, semeador de costas ao fundo, trilha semeada até a lente). Priorizar esse tipo de composição já na proposta de conceitos.
- **2026-08-11 (post 35):** negrito no texto TODO (não só o vermelho); negrito alarga a linha — conferir quebra (nada de palavra órfã; alargar padding ou segurar com nowrap).
- **2026-08-13 (post 37):** o user mandou a diretriz consolidada que usava no ChatGPT → salva em `referencias/diretriz-frase-legenda.md`, agora é a base obrigatória de frase + legenda desta skill.
- **2026-08-13 (post 37):** frase toda em preto a pedido do user ("desta vez") — o vermelho continua padrão, mas perguntar/confirmar quando houver dúvida. Temas de dor/pressão performam bem no perfil (refs: "Pressão é combustível", "Cansar é privilégio de quem está no jogo").
- **2026-08-14:** o user nomeou a fórmula preferida: **LEI OBSERVADA** — princípio universal observado da realidade/natureza, metafórico, que ensina pra vida ("A água nunca vence a pedra pela força"; "No raso não existe pressão"). A imagem deve SER o princípio; frase e imagem nascem juntas. Alternar no calendário com frases de veia empresarial direta. Detalhes no adendo da `referencias/diretriz-frase-legenda.md` e no `conteudo/banco-frases.md`.
- **2026-08-14 (post 38):** quando a frase tem lado negativo e positivo (água parada × água corrente), o user preferiu a imagem no lado POSITIVO/aspiracional da lei (o riacho vivo, não a lagoa podre) — propor por esse ângulo primeiro. E segundo post seguido com texto todo em preto: o preto está virando o padrão de fato; propor preto e oferecer o vermelho como opção.
- **2026-08-14 (post 38):** entre símbolos corretos, escolher o de MAIOR força visual imediata: a correnteza estava boa, mas a cachoeira comunica "movimento" num relance ("cachoeira é mais forte visualmente" — user). Na proposta de conceito, preferir o exemplar mais dramático/icônico do princípio.
- **2026-08-14 (post 38, técnico):** elemento BRANCO/claro (véu d'água, fumaça, luz) some no `mix-blend-mode:multiply` se o entorno também for claro — pedir no prompt um fundo ESCURO atrás do elemento claro (ex: "white water against a very dark, almost black wet cliff"). Foi o conserto da v3 → v4 da cachoeira.
- **2026-08-14 (post 38, v5 final):** "cachoeira" na cabeça do user = **CATARATA**: volume monstruoso (estilo Iguaçu) e a **crista visível** (o rio vertendo na borda, o início da queda), não uma coluna fina vista de baixo. Quando pedir força/movimento de água, propor direto a catarata vista de perto da borda. Levou 5 versões (lagoa → riacho → cachoeira na névoa → coluna no paredão → catarata) — checar a escala e o ponto de vista do símbolo com o user antes de gerar.
- **2026-08-14 (post 40):** o user voltou ao VERMELHO na palavra-punch depois de dois posts todo preto — a cor não virou regra fixa, é escolha por post: sempre confirmar no checkpoint. E gerar 2 versões de imagem pra escolha funcionou bem (carroça × ceifeiro); ele valorizou no ceifeiro a segunda camada sombria (foice = morte/medo), mesmo escolhendo a carroça — simbolismo com leitura dupla é ponto a favor na proposta de conceitos.
- **2026-08-14 (legenda):** correção do user na legenda do 38: **falar de natureza não é dizer "a natureza…"** — nunca escalar narrador abstrato nem desenhar a moral; o elemento concreto carrega a lei. A legenda do post 37 (raso) virou o gabarito oficial: `referencias/legenda-campea-raso.md`.
- **2026-08-14 (post 40):** o user trocou o conceito aprovado (lutador na arena, câmera baixa) por uma **frase da própria legenda virando a imagem** ("A arquibancada envelhece limpa" → plongée do ringue manchado cercado de arquibancada limpa, SEM figura humana). Dois aprendizados: (1) ao propor conceitos, garimpar a legenda — a melhor imagem pode ser uma linha dela; (2) contraste entre dois estados do mesmo lugar (sujo×limpo, marcado×intacto) carrega a frase sem precisar de personagem.
- **2026-08-14 (post 40, composição final):** o user evoluiu o contraste pra um quase-díptico: câmera um palmo acima da lona (rente ao horizonte puro mataria as manchas — elas vivem no plano horizontal; subir um palmo e pedir manchas também no apron/cordas resolve), elemento sujo à direita, corredor vazio CENTRALIZADO fugindo pra névoa, elemento limpo à esquerda, pesos iguais. Pra ajuste de enquadramento de uma imagem já aprovada (centralizar, rebalancear), o modo **image-edit com a própria imagem de entrada** funciona bem — mantém cena e clima, só recompõe (v5→v6). O aviso do motor-imagem contra image-edit vale pra REFERÊNCIAS externas, não pra reenquadrar a própria geração.
- **2026-08-14 (post 40, técnico):** quando a imagem é um CONTRASTE entre dois elementos, os DOIS precisam ficar legíveis — na v3 a névoa do prompt-base engoliu a arquibancada (o contraponto) cedo demais. Conserto: pedir o segundo elemento ocupando o terço médio do quadro em fileiras nítidas ("rising in clearly visible tiers filling the MIDDLE THIRD") e restringir a bruma ("ONLY THE TOP QUARTER is pale/hazy"). O prompt-base pede metade superior clara; reduzir pra um quarto quando o contraponto precisa de altura.
- **2026-08-14 (post 39, técnico):** quando um elemento ESCURO sobe até o topo da imagem (casco gigante, árvore, parede), ele invade a faixa da frase mesmo com o fade padrão de 26% — alongar o mask (`transparent 0% → rgba(0,0,0,.35) 26% → #000 46%`) clareia a área do texto sem regerar a imagem.
- **2026-08-14 (post 39, escala):** o user ampliou o símbolo até o extremo: barco encalhado → navio de escala de galeão "tão grande que não dá pra ver inteiro" (o topo some na névoa). Reforça a regra do exemplar mais dramático — e "não caber no quadro" é um recurso válido pra dar escala.
- **2026-08-14 (post 39, técnico):** pra micro-ajuste numa imagem já aprovada (ex: virar a cabeça do personagem), o **image-edit com a própria imagem gerada como input** funciona muito bem: manteve composição/luz/grão quase idênticos mudando só o pedido. Avisar o user que não é pixel-idêntico (re-renderiza). O alerta do motor-imagem contra image-edit vale pra FOTOS DE REFERÊNCIA externas (vira colagem), não pra editar a própria geração.
- **2026-08-26 (crivo do lote 4 — critério do COTIDIANO BRASILEIRO, registrado com aprovação do user):** vale pra TODA frase daqui em diante. (1) **Nunca nichar a empresário** — a frase parte de princípio universal que serve pra qualquer pessoa (observação filosófica de um causo da vida); o direcionamento empresarial é menção sutil, na legenda. O post 43 ("Gente boa não se demite da empresa. Se demite do dono."), nichado, flopou: 0,51%, pior taxa do formato (H12 em `conteudo/analise/hipoteses.md`). (2) **O causo precisa ser cotidiano do brasileiro** — todo mundo tem prateleira em casa e já viu vergar ("Prateleira vazia não verga" = "fenomenal"); mapa, montanha, farol, forja e olaria são distantes da realidade do brasileiro que quer vencer na vida → frase abstrata/sem impacto mesmo com abordagem certa. Teste: "qualquer brasileiro já viveu isso?" — o símbolo sai da casa, da rua, da cozinha, da obra. (3) A formulação precisa de **"molho"** — tensão/graça; abordagem certa sem molho também é rejeitada (ex: "Canteiro limpo é obra parada"). (4) **Vocabulário de marketing ("posicionamento") não é voz do Hélio** em post de frase — o intuito é fazer refletir. Ver também a leitura "espelho do share" (H11) no `conteudo/banco-frases.md`: a frase precisa vestir bem quem compartilha (autodeclaração positiva), não advertir.
- **2026-08-26 (post 57, técnico — sangria inferior):** subir levemente uma imagem ancorada no pé (`bottom:55px`) abre uma faixa de papel nu na base do slide — mesmo com fade, o pé fica mais claro que o resto e lê como emenda. Conserto sem regerar: **esticar a altura da imagem na mesma medida, ancorada em `bottom:0`** (ex: `height:1135px` num quadro de 1080 = conteúdo sobe 55px e a imagem segue preenchendo até a borda). Distorção vertical de ~5% é imperceptível em cena de objeto/parede; acima disso, conferir no render.
- **2026-08-28 (post 67, exceção de fecho — autorizada pelo user):** a regra 30/31 da diretriz manda a frase voltar no fim como ponto final. Ela pode voltar **com uma conjunção de fala** quando o texto pede a cadência de quem repete um ditado em voz alta. No 67 o fecho ficou "Franklin sabia. Sua avó, do jeito dela, também. / **Que** saco vazio não para em pé." — o "Que" amarra a frase na fala da avó do primeiro parágrafo ("come, **que** saco vazio não para em pé"), fechando o círculo do texto. **Limite da exceção:** só conjunção que já apareceu no corpo da legenda, e nunca palavra que mude o sentido ou acrescente moral — continua proibido escrever qualquer coisa DEPOIS da frase. O padrão segue sendo o fecho idêntico ao slide; isto é licença de cadência, não porta aberta pra reescrever a frase no fim.

### 3.2 A estrutura-raiz (02/09)

> O que caiu nela: a ponte "Com a nossa vida funciona igual" (item 7, proibida em 13/10), o fecho em
> dois tempos com a frase como última palavra (itens 14 e 15, substituídos pela pergunta-espelho + CTA
> em 11/09) e o teto de 1.400 que ela furava (hoje a parede é 2.200 pra toda legenda de frase).

A legenda do **post 47 ("A raiz decide o que o vento leva")** é o segundo gabarito desta skill, ao
lado da `legenda-campea-raso.md`. Ela fez 1,31% de taxa (FORTE) com **2.120 caracteres** — e o
user autorizou explicitamente furar o teto de 1.400 quando a peça for construída nela
(*"mantém em 2100 e registra a exceção"*, post 80/alicerce). Alvo ~2.100, parede dura 2.200 (limite do IG).

**Quando usar:** frases cuja lei é *"o que se decide/constrói no escuro determina o que aparece na
superfície"* — e em que existe um **agente aparente** que leva a fama de decidir e não decide nada
(o vento, a tempestade, a crise, a sorte). Se a frase não tem esse falso culpado, use o molde do raso.

**Os movimentos, na ordem (íntegra em `conteudo/carrosseis/47_raiz/carousel-text.md`):**
1. Nega o agente aparente em uma linha seca ("O vento não cria nada. Ele só carrega.")
2. Anáfora de negação, 3-4 verbos ("não escolhe, não separa, não julga, não melhora")
3. Aponta pra onde a decisão foi tomada: **"onde ninguém vê"**
4. Apresenta o sujeito real, que trabalha no escuro
5. Hierarquia de atenção: o mundo aplaude a parte errada (3 itens visíveis)
6. **TRÍADE DE PUNCHES** — três linhas paralelas, mesma sintaxe, um punch cada. É a assinatura
   estrutural do molde; é o primeiro item a se perder se comprimir, e por isso não se comprime.
7. Ponte curta pra vida: "Com a nossa vida funciona igual."
8. Camada humana em **categorias** que o leitor preenche (nunca vinheta biográfica)
9. A impossibilidade de fingir ("Dá pra enganar a plateia... não dá pra enganar o vento")
10. Empresa entra com nome próprio, 3 itens concretos
11. Nega a fonte falsa e nomeia a verdadeira ("não sai do marketing, sai da raiz")
12. O erro típico do dono, nomeado sem acusar
13. **A linha de escolha pura:** "é a única parte que ninguém vê. Justamente por isso, ninguém cobra."
    Faz dois trabalhos de uma vez — entrega a consagração E fecha a brecha do vitimismo (quem não é
    elogiado também não é fiscalizado: é liberdade, não injustiça). É o parágrafo mais forte do molde.
14. Pergunta-espelho curta, ANTES do fecho
15. Fecho em dois tempos (nega o agente aparente + a frase dá a última palavra)

**Transposição registrada:** o post 80 (alicerce) é a v2 declarada deste molde — mesma lei, personagens
trocados (vento→tempestade, raiz→alicerce, copa/fruto→fachada/sala/vista). Diagnóstico do user:
*"ela é a versão 2 dessa frase da raiz, só muda os personagens."* Quando uma frase nova cair nessa
família, transpor o molde em vez de inventar arco novo.

### 3.3 As três regras de construção da legenda (28/08 e 01/09)

> O que caiu nelas: "isso aqui não é X" como fórmula queimada (hoje permitida, sem virar fórmula, 13/10)
> e "enquanto a frase for física, todo exemplo universal tem que ser físico" (hoje o objeto ocupa um
> parágrafo e o resto é a lei na vida adulta, 09/09).

Vieram de três rodadas de revisão em cima da legenda do 66 (filho no colo). Valem pra TODA legenda de frase.

- **2026-08-28 — DESENVOLVIMENTO É TEXTURA, NÃO TAMANHO.** O user leu a v2 e disse: "a parte empresarial está maior que a parte universal, que é o principal". Em caracteres a universal era maior — mas a empresarial tinha **três exemplos concretos** (a tarefa, a decisão, o cliente) e a universal tinha **um**. É isso que o leitor sente como "desenvolvida". Régua prática: **contar exemplos concretos dos dois lados, não linhas.** A universal precisa ter pelo menos tantos quanto a empresarial — de preferência mais, já que as regras 13-14 da diretriz mandam "primeiro a vida, depois a empresa". Na v4 ficou 3×3, com a universal em 2,5× o tamanho da empresarial.
  *Corolário estrutural descoberto no mesmo passe:* se a frase tem lado positivo e negativo, **o lado negativo também precisa nascer na camada universal**. Na v2 o peso imposto só aparecia na parte da empresa — ou seja, a lei negativa nascia no negócio, quando devia nascer na vida. Com o exemplo universal na frente, o parágrafo empresarial vira a **segunda ocorrência** da mesma lei, que é o efeito que a diretriz quer.

- **2026-08-28 — O PARÁGRAFO QUE FECHA A BRECHA NUNCA SE ANUNCIA.** O user pegou um tique: dois posts seguidos abriram o "anti-burro" com a **mesma fórmula literal** — "Agora, cuidado com a leitura preguiçosa disso aqui" (65) e "Agora, cuidado com o uso disso contra as pessoas" (66); o 59 fez parente disso ("E isso aqui não é elogio ao caminho longo"). Dois problemas: vira costura reconhecível pra quem acompanha o perfil, e **anunciar é postura defensiva** — avisa que o autor está preocupado com o que vão pensar, e enfraquece justo o parágrafo que precisa ser o mais firme do texto. A ressalva forte entra **como fato dentro do fluxo**, sem aviso: no 66 virou "A mãe que está na terceira noite sem dormir tem o braço doendo igual ao de qualquer um." Palavras do user: *"todo parágrafo anti-burro é igual, sendo que eles devem ter sua própria estrutura e não ser somente iguais, igual só no propósito deles."*
  **Fórmulas QUEIMADAS (não reutilizar):** "Agora, cuidado com…" · "isso aqui não é X" · qualquer abertura que avise que vem uma ressalva. Cada post inventa a própria forma de entregá-la — cena, contra-exemplo, fato seco, personagem que encarna a exceção.

- **2026-09-01 — A CAMADA UNIVERSAL NÃO USA BIOGRAFIA INDIVIDUAL.** Regra irmã da de baixo, e criada porque a de baixo não foi suficiente: ela fala em "registro sensorial da frase", e dá pra obedecer a letra dela escrevendo cena humana específica. Não dá mais. Na legenda do 76 (pedra/faca) a versão B ilustrou "quem afia também se gasta" com três vinhetas de vida — *"um pai que apanhou calado pra você não apanhar", "uma mãe que trabalhou dobrado", "um chefe antigo que te corrigiu na frente dos outros"*. O user cortou: *"quando vamos para o âmbito de pessoas fica meio complicado colocar sobre essas experiências em específico… partimos do princípio universal, e trabalhar com elementos da natureza elimina essa complicação de experiências individuais demais."*
  **O problema:** biografia específica exige que o leitor tenha tido AQUELA vida. Quem não teve pai ausente, quem não teve mãe que dobrou turno, quem nunca teve chefe — sai do texto. Elemento natural ou físico não cobra pedágio de história pessoal: pedra, água, metal, fogo, peso e maré são de todo mundo.
  **A régua prática — categoria universal SIM, vinheta biográfica NÃO.** O gabarito do raso faz o certo: "um casamento com raiz, um trabalho com sentido, uma obra que fique de pé" são CATEGORIAS que qualquer leitor preenche com a própria vida. "Um pai que apanhou calado" é a vida de outra pessoa, já preenchida, e o leitor só assiste. Teste antes de gravar: *este exemplo o leitor completa com a história dele, ou eu já contei a história de alguém?*
  **Como chegar no humano sem biografia:** deixar o fato físico deduzir. No 73 o parágrafo das vinhetas virou "O atrito não escolhe lado. O que ela tirou das facas, tirou de si junto" — a mesma segunda camada, sem contar a vida de ninguém.

- **2026-08-28 — ENQUANTO A FRASE FOR FÍSICA, TODO EXEMPLO UNIVERSAL TEM QUE SER FÍSICO.** A v3 tinha um parágrafo sobre peso não escolhido feito de fardos **sociais** (o favor que virou obrigação, a conta no nome de outro, o parente empurrado pela família). O user reagiu: *"achei esse parágrafo meio distante… não sei o motivo. Talvez distancie demais da frase original, perde o fio da meada."* O diagnóstico: "filho no colo" vive nos BRAÇOS, e o parágrafo tinha abandonado o corpo — todo o resto era físico (o braço queimando, três horas em pé, o corpo da avó). Conserto: o **mesmo braço** segurando a sacola que alguém passou pra "segurar um minutinho" — mesmo membro, mesmo peso, experiência oposta, argumento que não dá pra contestar porque não tem variável de fora.
  *Regra derivada:* quando um exemplo soar "distante" e ninguém souber dizer por quê, **conferir se ele saiu do registro sensorial da frase** (corpo, casa, rua, cozinha) e voltou pro abstrato. Quase sempre é isso.
  *E amarrar o vocabulário:* o parágrafo novo fecha em "contando", que puxa "a conta" da abertura e "ela só nunca somou" da avó. Punch novo tende a querer metáfora nova (a v3 abria "vem com juros", uma segunda metáfora financeira); **preferir repuxar a corda que já está no texto** a abrir uma segunda.
