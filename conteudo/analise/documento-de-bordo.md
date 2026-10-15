# Documento de bordo — a máquina de análise

*Tatsuo Academy · escrito em 27/08/2026 · leitura de 10 minutos*

Esta máquina existe pra responder uma pergunta só: **o que colocar no feed pra gerar conversa e lead, e não só aplauso.** Ela junta o histórico de 1.865 posts, a ficha de cada post novo e o resultado real medido 3 a 7 dias depois. Ela decide sobre o que falar (a veia), como vestir (a roupa), em que formato (frase ou carrossel) e qual palavra-chave puxa o lead. Ela **não** decide o que é bonito, e não substitui o crivo do Hélio.

**A regra de ouro, da qual tudo o mais deriva: post que ensina sem incomodar fica GUARDADO (salvamento); post que incomoda ESPALHA (compartilhamento).** Apostila é útil e morre no salvo. Identidade viaja.

---

## 0. A régua não mora aqui (leia isto primeiro)

Este documento **não traz número de régua**, de propósito. Régua escrita à mão em arquivo de texto apodrece em silêncio — foi exatamente o que aconteceu até 27/08/2026, quando a `/etiqueta` mandava calibrar carrossel por 36 comentários (o real era 17,5) e frase por 67 compartilhamentos (o real era 147).

A régua vigente sai daqui, na hora, sem gastar API:

```bash
python3 scripts/instagram/reguas.py
```

**O que se prevê é TAXA, nunca número absoluto.** Carrossel em interações por mil alcançados, frase em compartilhamentos por mil. Motivo: `absoluto = taxa × alcance`, e o alcance é loteria — testado em 27/08 por quatro caminhos independentes, nenhuma variável conhecida antes de publicar explica mais de ~7% dele. **Alcance não se prevê**, nem em banda grosseira: acertar o terço vale 35,7% contra 33,3% de sorteio. Ele só é registrado depois, pra separar "conteúdo fraco" de "conteúdo pouco visto".

**Atualização de 14/09/2026 (decisão do user, vale sobre o parágrafo acima).** A taxa ficou como **estimativa**; o **dado final é o absoluto em D+7**: comentários no carrossel e no reel, compartilhamentos na frase. Nas palavras dele: *"as primeiras taxas dos posts são mais para dar um norte do que para atestar a eficiência dele; todas as análises devem ser feitas usando o D7 com base no total de comentários e não a taxa."* O que sustenta: a taxa não neutraliza o tamanho (seção 2, hipótese 🟢 de 02/09) e lead anda com comentário contado (ρ +0,94), não com comentário por mil. O papel da taxa, declarado na saída do script: (1) antes de publicar, ler os comparáveis descontando o alcance e escolher a banda; (2) de D+1 a D+4, o norte (a peça está pegando em quem viu?); (3) no fechamento, explicar o erro (taxa alta com comentário baixo = pegou em quem viu e viu pouca gente; taxa baixa = não pegou). É o **regime 3** do placar: 1 = absoluto contra régua fixa (até 26/08), 2 = taxa (27/08 a 13/09), 3 = absoluto em D+7 contra terços vivos de posts maturados. Cada regime se conta separado, e a armadilha da seção 6 (a mesma palavra de veredito com sentido invertido) ganha um terceiro lado.

Mas atenção ao que isso **não** significa: taxa e alcance não são jogos separados. São o mesmo jogo (ρ=+0,70 no carrossel). Post de taxa alta alcança ~9× mais, e o absoluto cresce mais que proporcionalmente à taxa (expoente 1,39). **Um post morno não é metade de um bom — é um décimo dele.**

---

## 1. Antes de tudo: qual régua você está usando

Metade dos mal-entendidos desta máquina vem de comparar número de régua diferente. Diga sempre qual está em uso.

| Régua | Número | Quando usar |
|---|---|---|
| **Régua da casa** (todo post de feed, jul–ago/26, n=161) | mediana de **73 compartilhamentos** | Comparar qualquer post publicado |
| **Régua de quem foi visto** (alcance > 5 mil, n=106) | mediana de **158 compartilhamentos** | Julgar conteúdo sem punir má distribuição |
| **Taxa de compartilhamento** (shares ÷ alcance) | mediana **0,94%** · topo 25% **1,54%** · topo 10% **2,29%** · 3%+ é hit raro | A melhor régua de viralidade, porque desconta o alcance |
| **Frase** (n=43) | **3 comentários** · **147 compartilhamentos** · alcance 14.884 | Escrever previsão de frase — a métrica-alvo é COMPARTILHAMENTO |
| **Carrossel** (n=118) | **17,5 comentários** · 69 compartilhamentos · alcance 5.856 | Escrever previsão de carrossel — a métrica-alvo é COMENTÁRIO |

*Fotografia de 27/08 (jul–ago/26, só feed), guardada como referência histórica. **Para trabalhar, rode o script da seção 0** — estes números envelhecem.*

Duas armadilhas de régua que já custaram caro:

- **As réguas que as skills citam estão velhas.** A `/etiqueta` manda calibrar carrossel por 36 comentários (real: 17,5) e frase por 67 compartilhamentos (real: 147). A de carrossel é o **dobro** da realidade e a de frase é **menos da metade** — erram em direções opostas, o que faz o placar parecer pior no carrossel e melhor na frase do que é. Corrigir isso é a dívida mais barata e mais urgente da máquina.
- **Cada formato tem a sua métrica.** Frase viaja por compartilhamento e quase não gera comentário (mediana 3). Carrossel conversa (mediana 17,5) e é de onde sai o lead. Nunca julgue frase por comentário nem carrossel por alcance.
- **Compartilhamento e comentário medem coisas diferentes.** As veias são medidas em compartilhamento (quanto espalha). As roupas, em comentário (quanto conversa, que é o proxy de lead). Um post pode ganhar numa e perder na outra.

---

## 2. O que a gente acredita

Ordenado por **quanto isso deve mudar o que você faz**, não por ordem de descoberta. Cada regra diz o quanto confiar nela e com que tamanho de amostra.

---

### 2.1 As que mudam a decisão inteira

#### **O alcance manda**
Quem decide o número de um carrossel não é o texto, é quantas pessoas o Instagram entregou. Abaixo de 10 mil de alcance, nenhum carrossel do registro passou da mediana — nenhum, sem exceção.
**Confiança: medido, amostra pequena — 10 carrosséis do registro.** A correlação entre alcance e comentários é +0,90 (o alcance explica 81% do resultado). Os 3 acertos do placar tiveram alcance de 10.122, 16.797 e 38.996; os 7 erros tiveram 1.880 a 9.122. Separação perfeita. Uma regra burra — "alcance ≥ 10 mil, prevê acima" — acerta 10 de 10, contra 33% da máquina.
**Ressalva que impede a conclusão fácil:** essa regra burra **não pode ser usada pra prever**, porque o alcance só se conhece *depois* de publicar. Ela não prova que a máquina é pior que uma heurística simples — prova que boa parte do que a máquina tenta prever é decidido pela distribuição, não pelo texto. É uma medida do teto do que dá pra prever, não um substituto.
**Faça:** ao julgar um post fraco, olhe o alcance **antes** de culpar o texto. Post com 1.900 de alcance e 9 comentários não foi rejeitado — foi pouco visto. E ao escrever previsão, saiba que você está prevendo uma variável que não controla.

#### **Alcança ou conversa**
A frase é vista por muito mais gente. O carrossel faz muito mais gente agir. Todo lead vem de carrossel.
**Confiança: sustentada — é o efeito mais forte já medido aqui.** Frase (n=49) tem mediana de 14.551 de alcance; carrossel (n=184), 5.616. Confirmado em três janelas de tempo independentes. Mas por mil pessoas alcançadas o carrossel ganha em tudo: 18× mais comentário (2,66 contra 0,15), mais compartilhamento (11,29 contra 8,41), mais salvamento (8,37 contra 5,93). E **100% dos leads rastreados da semana vieram de carrossel e reel** — a frase gera zero por desenho, porque o chamado de palavra-chave só existe no carrossel.
**Faça:** escolha o formato pelo objetivo da semana, e escolha consciente. Frase quando a meta é topo (alcance, seguidor). Carrossel quando a meta é lead. Hoje metade dos slots vai no formato que não converte — isso é uma decisão de negócio, não um erro de dado.

#### **A culpa volta pro dono**
O post grande mostra que o problema que o empresário culpa nos outros nasce dele. Nunca reclama do funcionário, do mercado, do governo ou da Selic.
**Confiança: sustentada na prática, mas sem contagem escrita.** É a regra com a evidência formal mais frouxa das que estão marcadas como firmes: o arquivo de hipóteses diz "presente em todos os campeões" e não lista o n. O que existe são os quatro maiores carrosséis da história do perfil, todos fazendo isso: "você contrata alguém bom mas não prepara" (22.087 shares), "existe um dia que todo empresário conhece: o dia seguinte ao treinamento" (21.600 shares e 6.242 comentários), "empresário que não prepara o time vive trocando de funcionário achando que o problema é o mercado" (18.551), "PME não é um negócio, é um sonho com CNPJ" (17.478).
**Faça:** em toda peça, pergunte pra quem o dedo aponta. Se aponta pra fora do dono, reescreva. Se a peça não devolve responsabilidade nem vira a leitura do avesso, provavelmente é conteúdo morno.

#### **A arquibancada**
O post gigante não motiva nem ensina. Ele consagra quem está sofrendo e divide o mundo em dois grupos: quem está no jogo e quem olha de fora. Compartilhar é se declarar do grupo certo.
**Confiança: sustentada — 7 casos acima de 4.000 compartilhamentos com o mesmo molde.** Os dois maiores posts da história do perfil são desse molde e da mesma veia: "Não existe profundidade sem pressão" (39.029 shares, 3,27 milhões de alcance, 13/08/2026 — **o recordista atual**) e "Tem gente que não cansa porque nunca entra; fica na arquibancada" (38.139 shares).
**Faça:** o post não pode dizer "aguenta firme". Tem que dizer "o que você sente é o preço de estar dentro — quem não sente é porque não entrou".

#### **O peso é a veia mais forte da casa**
Pressão, cansaço, dor e peso é a veia de maior teto que existe aqui. Média de 1.968 compartilhamentos por post, contra 263 da veia de dinheiro — 7,5×.
**Confiança: sustentada, e reconfirmada hoje** num recorte independente dos últimos 365 dias (pressão 2.375 de média; dinheiro 301). O ranking inteiro se sustenta: peso > sonho com CNPJ (1.513) > gente (1.482) > crescimento (957) > liderança (864) > dinheiro (263).
**Faça:** toda semana precisa de pelo menos um post de peso/pressão/cansaço.

#### **Dinheiro guarda, não espalha**
Tema técnico-financeiro é a pior veia em compartilhamento. As pessoas guardam a apostila; não se declaram por ela.
**Confiança: sustentada no ranking (1/7 da média do topo); em teste como diagnóstico.** O que ainda não fechou é a causa: em 27/08 um post de Lucratividade fez só 9 comentários mas teve a **maior taxa de compartilhamento do dia** (2,33%), acima dos dois de Cultura — foi pouco visto, não rejeitado. Entre pilares o efeito é grande mas não fecha (p=0,067).
**Faça:** duas coisas, e a segunda é ordem do dono. Primeira: post de lucro, margem ou preço só entra com pessoa e cena no centro. Segunda: **prever lucratividade sempre como "mediana", nunca "acima"** — 5 de 5 previsões otimistas erraram pra baixo (12, 12, 0, 14, 9 comentários).

#### **Gente puxa conversa**
Post sobre pessoas, líder e equipe gera muito mais comentário do que post sobre dinheiro e número.
**Confiança: sustentada.** 10 dos 12 posts com 500+ comentários são de Cultura. Na comparação consolidada de 27/08: Cultura n=8, mediana 49 comentários; Lucratividade n=5, mediana 12.
**Faça:** quando a semana precisa de conversa e lead, escolha semente de gente e cultura. Dinheiro entra pelo lado humano ou entra sabendo que rende pouco comentário.

---

### 2.2 As que mudam como você escreve

#### **O espelho**
Compartilhar é vestir a frase. Frase que faz quem compartilha parecer bom ("eu aguento o peso", "eu sou profundo") espalha muito mais do que frase que adverte, cobra ou acusa.
**Confiança: em teste, mas é a mais perto de fechar — 13 frases maturadas (posts 35 a 55), separação perfeita.** Autodeclaração: 1,04% a 1,35% de taxa de compartilhamento. Advertência: 0,51% a 0,90%. Nenhuma advertência bateu nenhuma autodeclaração. **Ressalva honesta:** essa classificação foi feita depois de ver os dados. Já entrou 1 caso limpo, classificado antes (post 54, cobrança pura, previsto e realizado em 0,59%). Faltam 2.
**Faça:** ao fechar uma frase, pergunte "quem compartilhar isso está dizendo o quê sobre si mesmo?". Se a resposta for "que eu estou aquém", a frase rende metade. Classifique **antes** de publicar e anote. Publicar advertência de propósito é legítimo — só saiba que o teto é ~0,9%.
**E a regra que decide empate: quando a veia e o espelho discordarem, o espelho manda.**

#### **O nicho encolhe**
Frase que fala direto com empresário rende menos que princípio universal. E o causo tem que ser coisa que qualquer brasileiro já viveu — prateleira vergando, feijão, ladeira — nunca símbolo distante (mapa, farol, forja, olaria).
**Confiança: em teste, n=1 medido + doutrina do dono.** O caso é o post 43 ("Gente boa não se demite da empresa. Se demite do dono"), que era molde de dois carrosséis campeões (22k e 18k) e flopou como frase: 6,9 mil de alcance, 0,51% de share — a pior taxa do formato. A leitura de que a causa foi o nicho (e não o formato) é interpretação do dono, não medição. O teste foi cancelado de propósito: não se publica frase nichada nem pra testar.
**Faça:** escreva a frase como verdade universal, com o recorte empresarial aparecendo de leve só na legenda. E aplique os dois filtros do dono: **"qualquer brasileiro já viveu isso?"** e **"tem molho?"** — abordagem certa sem tensão nem graça é rejeitada do mesmo jeito ("Canteiro limpo é obra parada" estava certíssima e foi cortada por falta de sal).

#### **A frase anda sozinha**
Se a frase só fica boa depois que alguém lê a legenda, ela ainda não está boa. A legenda aumenta o significado; nunca salva.
**Confiança: doutrina do dono, não medição** — mas é o crivo que produziu os dois recordes do perfil.
**Faça:** teste no feed, sem legenda: parou o scroll? A reação que se quer é "isso é verdade" e "isso é sobre mim", nunca "que frase linda". A fórmula que mais performa é **a lei observada**: um princípio universal tirado da realidade, de preferência da natureza ("No raso não existe pressão", "A água nunca vence a pedra pela força"). Ninguém discute física.

#### **Não desenhe a metáfora**
Falar de natureza não é dizer "a natureza…". Nunca escale narrador abstrato.
**Confiança: doutrina — foi a correção mais importante que o dono já fez numa legenda.**
**Faça:** fale do elemento concreto (o mar, o metro, o mergulhador, a margem) e deixe o leitor extrair a lei sozinho. Anunciar a moral enfraquece. Na legenda, a empresa entra como mais um lugar da mesma lei, nunca como "na empresa é igual". E a frase volta no fim, ressignificada, com **nada depois dela**.

#### **O direto é o cavalo de trabalho**
Tese afiada, sem roupa nenhuma, é a base do perfil: maior mediana de comentário (36, n=14), nunca floppa feio, e ainda explode (melhor caso: 1.160).
**Confiança: em teste, n=14 numa tabela de um avaliador só.**
**Faça:** quando faltar ideia, quando o prazo apertar, quando a semana precisar de consistência — direto. É a escolha padrão.

#### **A metáfora aposta alto**
Metáfora é dona do recorde absoluto e do zero absoluto no mesmo grupo. Não é melhor que o direto: é mais alavancada.
**Confiança: em teste, casos contados a dedo (n=10 na tabela de roupas).** Babá-de-adulto fez 2.943 comentários na leitura da época — hoje está em **6.242 comentários, 21.600 shares e 781.681 de alcance**. Gol-contra, no mesmo grupo, fez **0**. A mediana da metáfora (32) não é melhor que a do direto (36); o que muda é o tamanho do prêmio e do tombo.
**Faça:** use metáfora quando quiser teto e aceitar perder o slot. Não monte a semana inteira de metáfora, e não use em semana que precisa bater meta.

#### **O mapa 1:1**
Se a metáfora precisa ser explicada — se cada peça dela não tem par óbvio na vida da empresa — o post não anda.
**Confiança: em teste, 3 casos, e já com limite conhecido.** Igreja traduz sozinha (fiel = funcionário, pastor = líder, credo = cultura) e fez 592. Gol contra exige decodificação (o juiz é o governo?) e fez 0. Mas "anda dez, volta oito" tinha mapa limpo, foi prevista alta e fez 12.
**Faça:** use como filtro de eliminação, nunca como promessa. Traduza cada elemento em voz alta antes de fechar; se travar em um, troque de metáfora. Mapa limpo só significa que ela não vai morrer por esse motivo — **não autoriza prever acima da média**.

#### **A tese satura, o nervo não**
Repetir logo em seguida a tese de um post que acabou de viralizar mata o post novo. Repetir o mesmo nervo por outro ângulo, não.
**Confiança: em teste, n=1 e com segunda causa declarada.** "Treinamento-diário" repetiu a tese do recordista 6 dias depois e fez 4 comentários — o pior Cultura do registro. "Contratou-um-currículo", mesmo nervo e tese distante, publicado 1 dia depois do recorde, fez 174. Mas a que flopou também usava a roupa mais fraca da tabela (cena, mediana 14) — há duas causas possíveis.
**Faça:** depois de um viral, espere 2 a 3 semanas pra voltar na mesma tese. Voltar ao mesmo nervo por outro ângulo pode ser imediato.

#### **Cena embaixo, metáfora em cima**
Cena como roupa de slide é a pior da tabela (mediana 14, n=4). Mas o recordista tinha cena na legenda e metáfora no slide.
**Confiança: baixa — n=1, retrospectivo, e o teste montado não valeu.** O teste de 24/08 não conta: a legenda que foi ao ar abriu em tese, não em cena. Condição declarada não cumprida.
**Faça:** cena vai pra legenda, metáfora vai pro slide. E se for testar, escreva a legenda-cena **antes** de renderizar as imagens e confira que foi essa que subiu.

---

### 2.3 Os filtros que evitam desperdício

#### **Um em dez**
Comentário serve muito bem pra dizer qual post foi melhor. Não serve pra estimar lead: de cada dez comentários, cerca de **um** vira contato no CRM.
**Confiança: sólida como ordenador, frágil como conversor.** Como ranqueador: 9 posts lidos no painel do Manychat, correlação de ordem 0,921 — ordenar por comentário dá quase a mesma ordem que ordenar por lead. Como conversor: a cadeia inteira foi medida **uma vez só** (116 comentários → 58 disparos → ~28 cliques → 11 contatos). A conta antiga de 87% vinha de um caso outlier; a mediana real de comentários que trazem a palavra é 50%.
**Faça:** continue ranqueando por comentário — o placar não precisa mudar de métrica. Mas ao prometer lead, **divida por dez, não por dois**. E não se assuste com post pequeno que dá zero lead: em alcance baixo quem comenta é a audiência fiel elogiando, não leitor novo executando o chamado.

#### **O fundo do poço**
Quatro tipos de post foram vistos (alcance acima de 5 mil) e mesmo assim ninguém espalhou. Não é problema de distribuição, é o conteúdo.
**Confiança: sustentada, casos claros.** Comunicado institucional: **1 compartilhamento** (recap do MBV: 3). Homenagem pessoal: **6**. Técnico-financeiro sem camada humana: 7 a 15. Moralizar cultura em tom professoral: 11 e 15.
**Faça:** comunicado vai pro story, nunca ocupa slot de feed. Homenagem é decisão pessoal — pode fazer, só não confunda o número baixo com fracasso de estratégia. Cultura entra pela cena de quem sofre com ela, nunca pelo púlpito.

#### **Terreno conhecido**
Metáfora tirada de terreno de identidade (fé, futebol, família) multiplica o efeito quando o mapa já é bom, mas não salva metáfora mal montada.
**Confiança: intuição plausível — 3 anedotas, e o teste proposto nunca rodou.** Igreja explodiu, futebol flopou, "empresa não é família" repetiu bem 3 vezes.
**Faça:** não escolha metáfora só porque o assunto é popular. Escolha pelo mapa; aí sim prefira o terreno que todo mundo vive.

#### **A fábula converte, mas não alcança**
A fábula tem a melhor densidade de conversão da tabela (5,0 comentários por mil alcançados) e teto de alcance baixo.
**Confiança: a mais fraca do documento — sem n, sem comparação, sem teste desenhado.** É a única regra aqui que está literalmente na fila, sem evidência escrita além desse número solto.
**Faça:** trate fábula como peça de meio de funil: chamada forte de palavra-chave, e não cobre alcance dela. Quem quiser defender ou derrubar isso precisa levantar o histórico de fábulas do zero.

---

### 2.4 As que já morreram — pode parar de fazer

#### **A janela nobre — REFUTADA**
A ideia de que o primeiro post do dia pega quase 3× o alcance dos seguintes. O número bruto era forte (74 posts de agosto: 16.418 contra 5.854), mas era artefato: o primeiro post do dia costuma ser uma frase, e frase alcança mais de qualquer jeito. **Separando por formato, o efeito some no carrossel em três janelas de tempo independentes.**
**Faça:** pare de brigar por slot de horário no carrossel. Não muda nada. O teste de "publicar Cultura na janela nobre" foi cancelado antes de rodar, porque gastaria um slot pra medir zero.
**Lição de método que ficou:** não reporte achado antes de separar por formato.

#### **O conselho inventado — REFUTADA**
A ideia de montar um conselho de personas de IA pra dar nota nos ganchos e prever o que vai bombar. Teste cego, 5 personas, 40 ganchos reais, sem ver as métricas: correlação com o resultado real de **+0,08**. Ruído puro. A melhor persona chegou a +0,26.
**Faça:** não use. Dado real manda. (Ressalva registrada: o conselho pôs o recordista real em 1º, então talvez sirva como farejador de teto alto — mas só voltaria com desenho diferente.)

---

### Rastreio (só pra quem for cavar no `hipoteses.md`)

| Nome curto | Código no arquivo |
|---|---|
| Gente puxa conversa | H1 |
| A culpa volta pro dono | H2 |
| A metáfora aposta alto | H3 |
| O mapa 1:1 | H4 |
| Terreno conhecido | H5 |
| Cena embaixo, metáfora em cima | H6 |
| A fábula converte, mas não alcança | H7 |
| Um em dez | H8 |
| O conselho inventado | H9 |
| Dinheiro guarda, não espalha | H10 |
| O espelho | H11 |
| O nicho encolhe | H12 |
| A tese satura, o nervo não | H13 |
| A janela nobre | H14 |
| Alcança ou conversa | H15 |

Arquivo: `/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/analise/hipoteses.md`. **O alcance manda** e **o fundo do poço** não têm código — vieram da auditoria do placar e do `o-que-funciona.md`.

---

## 3. Vocabulário

| Palavra | O que quer dizer |
|---|---|
| **Veia** | O assunto que o post cutuca — peso, gente, dinheiro, sonho. Medida em compartilhamento. |
| **Nervo** | A dor específica dentro da veia (preparo de gente, retirada do dono). Pode se repetir à vontade. |
| **Tese** | O argumento exato daquele post. Diferente do nervo — e a tese satura, o nervo não. |
| **Roupa** | Como o conteúdo se apresenta no gancho (slides 1–2): direto, metáfora, fábula, paradoxo, cena. Medida em comentário. |
| **Semente** | A ideia crua de onde o post nasce, tirada do banco. Quem escolhe é o dono, sem ranking. |
| **Mecanismo** | O gatilho que faz apertar compartilhar: a arquibancada, a culpa volta pro dono, o paradoxo, o espelho. Um por post, bem executado. |
| **Espelho** | O que a pessoa diz sobre si mesma ao compartilhar. Autodeclaração espalha; advertência não. |
| **Molho** | Tensão ou graça na formulação. Sem molho, abordagem certa é rejeitada. |
| **Palavra-chave** | A palavra do CTA, CAIXA ALTA, uma por post, que dispara a DM do Manychat e rastreia o lead. |
| **Maturação** | O tempo até o número parar de mexer. Leitura provisória em D+3, oficial em D+7. |
| **Ficha** | A linha do post no `registro-posts.csv`: pilar, nervo, roupa, mecanismo, palavra, previsão. |
| **Placar** | Previsão escrita antes × resultado medido depois. |

---

## 4. Como um post nasce e morre

1. **Criação** — `/carrossel` ou `/frase`. Briefing → modelo → **texto** → HTML → PNG → imagens por IA. O texto **para pra aprovação** antes de qualquer HTML ou imagem. Pasta: `conteudo/carrosseis/[N]_nome-do-post/` (o número é a ordem de publicação). Entrega final vai pro Desktop.
2. **Etiqueta** — `/etiqueta`, depois de finalizar e **antes de publicar**. Grava uma linha no `registro-posts.csv` com a ficha, a palavra-chave única e a previsão (categoria + faixa numérica + justificativa). Sai junto o kit da DM: mensagem de 1–2 frases (~100 caracteres) e texto do botão. O campo `funil` sai vazio de propósito.
3. **Publicação** — **manual, pelo dono, no app do Instagram.** Ninguém automatiza: a escolha da música faz parte do post. O Claude nunca publica.
4. **Manychat** — em **até 5 minutos** da publicação. Duplica o modelo, renomeia no padrão `IG | AAAA-MM-DD | PALAVRA | tema`, cadastra a palavra com as três variantes (minúscula, Capitalizada, CAIXA ALTA, sem acento), aponta pro **post específico**, edita DM e botão **com UTM**, ativa e confirma com print.
5. **Maturação** — 3 dias no mínimo. Os insights da Meta só fecham em ~48h.
6. **Ritual** — `/ritual`, todo dia. Fecha o placar do que maturou, preenche `resultado_com`, `resultado_vs_previsao` e o `funil`, apenda o snapshot de decaimento e devolve um briefing de até 15 linhas. **Segunda-feira** roda a versão consolidada: re-ranqueia a semana, concilia o ClickUp, lê o painel do Manychat, puxa o CRM e recalibra as previsões.

---

## 5. As regras duras

Cada uma tem nome. Se lembrar do nome, lembra da regra.

**O pull queima a API.** Nunca rode `pull_insights.py pull`. Ele varre os 1.865 posts de uma vez e já disparou o anti-abuso da Meta, bloqueando a API por dias. O único comando permitido no dia a dia:
```
python3 /Users/pedrohenrique/Documents/tatsuo-carrossel/scripts/instagram/pull_insights.py update
```
**Aviso pra quem assumir:** o `scripts/instagram/README.md`, o `_contexto/o-que-funciona.md` e o `_contexto/handoff-api-instagram.md` foram corrigidos em 13/10/2026 e já mandam usar só o `update`. Ainda falam em `pull` o `conteudo/banco-frases.md` (linha 6) e o docstring e a mensagem de sucesso do próprio `pull_insights.py`. Ignore essas linhas.

**Ninguém liga pra API na conversa.** O dado já está no disco, atualizado sozinho três vezes por dia (9h, 14h, 20h). Só rode `update` se o campo `pulled_at` do `desempenho.json` passar de 24h — e avise que o agendamento falhou.

**O texto para antes da imagem.** No carrossel e na frase, o texto vai a aprovação antes de qualquer HTML ou imagem. É o único checkpoint obrigatório do fluxo criativo. Já foi furado e custou carrossel inteiro refeito.

**Palavra única por post.** CAIXA ALTA, uma só, sem acento e sem cedilha (acento quebra o match), e nunca usada antes — confira no `registro-posts.csv`. Palavra repetida = dois posts disputando o mesmo rastro = atribuição de lead destruída.

**Automação sempre no post específico.** Nunca "qualquer publicação". Gatilho global dispara DM pra quem comentou a palavra por acaso e apaga a atribuição. O dado prova: automação global deu 7,7% de CTR; as específicas dão 43–58%.

**UTM no link é obrigatório.** Numa semana, ~63 leads clicaram e só 14 chegaram ao CRM com rastro. Não foi post que não gerou lead — foi lead sem etiqueta.

**Previsão antes, resultado depois.** Previsão escrita depois de ver o número entra no estudo de padrões, mas **não entra no placar** — senão a máquina mede a própria memória. Três posts já foram declarados retroativos e ficam fora (33, 51, 56).

**Funil é leitura, não decisão.** O campo nasce vazio. A copy dita a profundidade; forçar isso na criação mata a naturalidade. Quem preenche é o ritual, olhando o comportamento real.

**Snapshot honesto.** Nunca grave a data de hoje com números velhos. Buraco no histórico é honesto; linha reta falsa mente dizendo que o post parou de crescer e contamina a curva de decaimento. O script aborta sozinho se você tentar.

**Segredo nunca entra no Git.** Token do Instagram em `~/.tatsuo/ig-token.json`. Credencial do CRM em `~/.config/tatsuo/ghl.env`. `leads.json` tem PII (nome, e-mail, telefone) e é gitignored. As transcrições e o banco de scouting do MBV são IP pago e ficam local. Nunca commite, nunca cole em conversa.

**O ritual não sai da caixa dele.** `/ritual` só escreve dentro de `conteudo/analise/`. Nunca edita skill, carrossel ou banco de scouting.

**Esta máquina é a fonte da verdade.** `git push` sim; `pull`, `fetch` e `merge` **nunca**. Push rejeitado = pare e avise, não resolva por conta própria.

**Duas vias de sincronização, e elas não se cruzam.** Texto, HTML e aprendizado vão pelo Git. Imagem vai **só** pelo Google Drive — `conteudo/carrosseis/**/*.png` está no `.gitignore`. Quem clonar o repositório esperando as imagens não vai encontrá-las.

**Renove o token antes que ele morra.** `pull_insights.py refresh`. **O token atual expira em 05/10/2026.**

**O Mac precisa estar acordado.** O agendamento existe em três horários porque o das 9h quase nunca disparava. Mac dormindo já atrasou uma ativação de Manychat um fim de semana inteiro. `caffeinate` antes de sair, e **nunca** confie o Manychat a uma tarefa agendada.

---

## 6. O placar — e a verdade sobre ele

A máquina escreve uma previsão antes de cada post e confere depois. Auditoria de 27/08/2026, casando as 27 linhas do registro com os 1.865 posts da API.

### Quanto tem de placar, de verdade

| | n |
|---|---|
| Linhas no registro | 27 |
| Com previsão escrita antes | 24 |
| Com faixa numérica | 7 |
| Com resultado preenchido | 19 |
| **Previsão + resultado = o placar** | **17** |
| Realmente maturados (72h+) | 15 |
| Fechados pela régua nova de D+7 | **4** |

Cinco posts já têm número na API há dias e ninguém preencheu (SONHO 116, PILOTO 5, LADRAO 2, CULTURA 49, PRATELEIRA 597). Esses números já estão no arquivo de hipóteses e não no registro: **o placar oficial está mais atrasado que o arquivo de hipóteses.**

### O número, sem enfeite

**6 acertos em 17 = 35,3%.** Chutar ao acaso entre três categorias dá 33,3%. A chance de tirar 6 acertos por pura sorte é 52% — ou seja, não há sinal nenhum.

Só nos 15 maturados: **5 acertos = 33%**. E o mundo entregou 8 "abaixo", 6 "acima" e 1 "mediana".

| Estratégia | Acerto |
|---|---|
| Chutar sempre "abaixo" | **53%** |
| Chutar sempre "acima" | 40% |
| **A máquina** | **33%** |
| Chutar sempre "mediana" | 7% |

Um post-it na parede escrito "abaixo" teria batido o sistema por 20 pontos.

**A conclusão honesta: com 15 a 17 casos, o placar não sustenta afirmação nenhuma sobre a competência de previsão do sistema — nem a favor, nem contra.** Não é "a máquina prevê bem". Também não é "a máquina prevê mal". É "a amostra não permite dizer". Pra saber se o sistema bate o acaso seriam necessários **cerca de 40 posts com previsão registrada — faltam uns 25**, o que dá dois meses e meio no ritmo atual.

### As duas coisas que dá pra afirmar

**1. Existe viés otimista, e é o único achado sólido.** 10 erros pra baixo contra 1 pra cima (p=0,012). A causa está na entrada: das 24 previsões escritas, **18 foram "acima", 6 "mediana" e ZERO "abaixo"**. *A ficha só sabe elogiar.*
Mas parte do otimismo é **régua torta, não previsão ruim**: trocando a régua velha de 36 comentários pela mediana empírica de jul–ago (17,5), o placar sobe de 33% pra **47%** e os erros caem de 9 pra 6.

**2. A previsão aposta na variável errada.** 81% do resultado de um carrossel vem do alcance, e o alcance não entra na previsão. Quando se controla o alcance (comentários por mil alcançados), a previsão não separa nada. Enquanto a métrica-alvo for número absoluto, o placar mede loteria de distribuição com verniz de análise editorial.

### As faixas numéricas: ainda não dá pra medir

**Zero das 7 faixas está maturada** — a mais velha tem 47 horas. Leitura provisória: 3 dentro, 4 fora, contra a meta declarada de 80%. **Os 4 que erraram erraram todos pro mesmo lado, por 92% a 100%.** Se isso se confirmar, o problema não é a largura do intervalo — é o intervalo inteiro estar ancorado alto demais. Pra estimar cobertura com margem razoável faltam 13 a 18 faixas maturadas.

### Higiene: quatro coisas que impedem o sucessor de reproduzir o placar

1. **A régua da frase não existe em lugar nenhum que funcione.** A skill `/etiqueta` documenta 67 shares; a ficha do post 59 cita 357. Nenhum dos dois reproduz os vereditos gravados. O único limiar coerente com o CSV é ~117–151 shares — número que não aparece em documento nenhum. **O placar da frase não é auditável hoje.**
2. **A régua do carrossel (36 comentários) está 1,5 a 2× acima da mediana real.**
3. **A linha 28 do `registro-posts.csv` (`56_abismo`) tem 16 campos em vez de 17** — falta `data_publicacao`, e tudo depois dele lê deslocado. Qualquer script que leia por coluna erra esse post. Agravante: a skill `/etiqueta` documenta o cabeçalho sem esse campo — o CSV evoluiu e a skill ficou pra trás.
4. **Resultado congela em D+3 e nunca é revisado.** Registro contra hoje: contratou 153→206, raiz 1.077→1.441, afunda 152→187. Posts grandes crescem até 1,35× depois do D+3; posts pequenos, nada. Ler em D+3 comprime exatamente o topo — e a skill mudou pra D+7 sem recontar o que já está gravado.

---

### Releitura de 30/08/2026 — o viés tem nome e direção

Segunda auditoria, 37 fichas no registro, 6 fechadas em D+7 neste dia.

**A distribuição das previsões:** 24 `acima`, 10 `mediana`, **zero `abaixo`** em 34 fichas com previsão escrita. A máquina nunca usou um terço da própria régua.

**O placar dos maturados (n=14):** 43% de acerto contra 33,3% de acaso — e o dado que importa não é esse, é a **direção do erro**: 7 erros pra cima contra 1 pra baixo (teste de sinal, p=0,035). Incluindo os que ainda não fecharam (D+3 a D+6, n=11, 7 pra cima contra 0), fica **14 contra 1**. Isso não é ruído: é otimismo sistemático.

**O teste mais duro que rodamos até hoje.** Como alcance e taxa andam juntos (ρ≈+0,70), parte do acerto pode ser só ter adivinhado que o post ia circular. Descontando o alcance (regressão da taxa sobre log do alcance) e testando se a previsão acerta o que **sobra**: ρ=−0,02 (p=0,95). Contra a taxa bruta: ρ=+0,09 (p=0,74). **Nas 14 fichas que temos, a previsão não carrega informação nenhuma.**

Honestidade sobre esse número: n=14 é pouco, e 13 das 14 previsões são só `acima` ou `mediana` — com o intervalo espremido em duas categorias, o teste tem pouquíssimo poder. Ele **não** prova que a máquina é incapaz; prova que, com o que existe hoje, não dá pra distinguir a máquina de um chute otimista. E enquanto ela nunca escrever `abaixo`, esse teste nunca vai poder dar outra resposta — porque não há variação pra medir. Foi por isso que a `/etiqueta` ganhou portão mecânico em 30/08: `mediana` virou o default e `acima` passou a exigir dois comparáveis históricos nomeados com taxa.

### ⚠️ Armadilha: a mesma palavra significa o oposto nos dois regimes

Nas fichas **anteriores a 27/08**, `resultado_vs_previsao` foi escrito contra o **número absoluto**: ali `errou-pra-baixo` quer dizer que o real veio abaixo do previsto — ou seja, **a máquina foi otimista**.

Nas fichas de **27/08 em diante**, o veredito é contra as **bandas de taxa**: ali quem descreve otimismo é `errou-pra-cima` (previu banda melhor do que deu).

**A mesma coluna, a mesma palavra, o sentido invertido.** Quem somar `resultado_vs_previsao` inteira um dia vai ler o viés ao contrário do que ele é. Em 30/08 as 17 fichas antigas com veredito ganharam um aviso em maiúsculas no começo da própria `justificativa`; o validador não pega isso sozinho porque os dois valores são legais nas duas épocas. **Placar antigo e novo se contam separados — sempre.**

---

## 7. O que ainda não sabemos

**Perguntas em aberto, com o que falta pra fechar cada uma.**

- **Por que o algoritmo distribui mais a frase que o carrossel?** A explicação óbvia está descartada pelo próprio dado: o carrossel tem taxa de compartilhamento *maior*. Ninguém sabe. Teste sugerido: mesma tese em frase e em carrossel, com uma semana de distância.
- **Quanto comentário vira lead, de verdade?** A cadeia inteira foi medida uma vez só. Faltam **2 a 3 posts com rastreio completo** (comentários → disparos → cliques → contatos no CRM) pra fixar os percentuais.
- **O espelho fecha ou não?** Faltam **2 frases classificadas antes de publicar** e conferidas depois.
- **Cena na legenda + metáfora no slide funciona?** O teste nunca rodou direito. Precisa ser re-rodado com a legenda-cena escrita **antes** do render, e conferindo que foi ela que subiu.
- **Lucratividade é morna, ou só mal distribuída?** Falta repetir uma lucratividade no primeiro horário do dia pra separar as duas causas.
- **Terreno de identidade multiplica mesmo?** O teste proposto — duas sementes do mesmo nervo, uma identitária e uma neutra — nunca foi montado. Hoje são 3 anedotas.
- **A fábula converte?** Não existe base escrita. Pra defender ou derrubar, alguém precisa levantar o histórico de fábulas do zero.
- **"A culpa volta pro dono" tem quantos casos?** É a regra mais usada da casa e a única marcada como firme sem n escrito. Vale contar e registrar.
- **O sistema prevê melhor que sorte?** Faltam ~25 posts com previsão registrada. E antes disso, vale trocar a régua velha e passar a usar a categoria "abaixo", que nunca foi usada uma vez sequer.
- **As roupas ainda valem?** A tabela tem 3 a 14 casos por classe, classificação de um avaliador só e período misto. Re-rodar quando o corpus dobrar — e **congelar as métricas numa data única, declarada**, porque comparar posts colhidos em maturidades diferentes é o erro silencioso mais provável desse arquivo.

---

## Fecho

A distribuição desta casa é de cauda longa: a mediana é de dezenas a centenas, e os hits passam de 20 mil. **Ninguém "só faz hits".** O jogo é mirar nas veias comprovadas, publicar com constância e medir. Cada post é uma tentativa bem mirada, não uma aposta cega.

E quando o número não fizer sentido, a ordem de checagem é sempre a mesma: **primeiro o alcance, depois a régua, e só então o texto.**