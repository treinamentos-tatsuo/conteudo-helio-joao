# Carrossel 69 — A teoria do cavalo teimoso

**Modelo:** fabula (visual) · **Pilar:** Cultura · **Palavra-chave:** FOME · **Slides:** 19

> **v2 — 2026-08-28.** O user trocou o regime: de `tema` para **`espinha`** (seguir os beats da
> fonte na mesma ordem, trabalhando só linguagem e diagramação) e tirou a peça do universo da
> Florestapitalista. A v1 (O Empresário Camelo, fábula original em Florestapitalista) está
> preservada em `v1-camelo.md`.

> **v3 — 2026-08-28 (rodada visual do user).** Sete correções, sendo três de coerência narrativa
> que a v2 não tinha visto:
> 1. **Slide 5** — a gravura já mostrava o homem oferecendo água na boca do cavalo, gesto que só
>    começa no slide 6. Refeita: ele olha a água pensando no bicho, mãos ao lado do corpo.
> 2. **Slide 8** — o homem puxava o cavalo PRA LONGE da água, o que não fecha (se ele quer que o
>    bicho beba, ele puxa PRA água; e o cavalo só resiste porque não quer beber). Refeita com o
>    homem dentro do raso puxando pra dentro e o cavalo fincado no seco.
> 3. **Slide 9** — o user aprovou a imagem, mas ela tinha que casar com o 8. Mesma composição
>    (plano alto, marcas de arrasto), com as posições corrigidas: homem na água, cavalo oposto.
> 4. **Slide 10** — vira **díptico vertical** a pedido do user: cara do homem fazendo força de um
>    lado, cara do cavalo resistindo do outro. *Nota: contraria a regra "split de duas metades:
>    não usar" (erros-frequentes 2026-08-06), que saiu do próprio user; aqui ele pediu o oposto.
>    Executado como duas gravuras retrato separadas compostas em HTML lado a lado, não como uma
>    imagem cortada ao meio — que era o defeito que originou aquela regra.*
> 5. **Slides 11 e 17** — a `object-fit:cover` na caixa alta decapitava os dois personagens, que
>    estavam nas bordas da landscape. Refeitas com cláusula de composição travando os figurantes
>    no miolo do quadro.
> 6. **Slide 12 é NOVO (ponte).** O 11 fechava a história e o 12 já abria a moral: salto seco. O
>    slide-ponte fecha a fábula e arma a lição — *"o homem tinha razão. A água era boa. Só que ter
>    razão nunca fez ninguém beber."*
> 7. **Slide 18 reescrito e slide 19 NOVO (CTA próprio).** O 18 era o CTA misturado com o punch.
>    Agora o 18 devolve a responsabilidade pro dono (ideia do user: *"talvez você não foi capaz de
>    despertar sede"*, ajustada pra a 2ª pessoa correta) e o 19 é só o CTA, amarrando a história ao
>    tempo de estrada do Hélio (38+ anos, fato registrado em erros-frequentes 2026-08-27).

> **v4 — 2026-08-28 (2ª rodada visual).** Duas correções do user:
> - **Slide 9** — na v3 eu troquei o PLANO (virou plano alto oblíquo) quando o pedido era manter o
>   zenital e mexer só na posição dos personagens. Refeito em zenital de verdade (câmera na
>   vertical, sem horizonte e sem céu), com o homem na água à esquerda e o cavalo fincado no seco
>   à direita. Como a gravura zenital é larga, a caixa dela ganhou `max-height:830px` +
>   `margin-top:auto` (classe `.wide`): a caixa quadrada padrão cortava o homem fora do quadro.
> - **Slide 10** — os dois passam a estar de **perfil**, close na cara de cada um no mesmo
>   instante, olhando no fundo dos olhos um do outro (homem virado pra direita, cavalo virado pra
>   esquerda), suando de esforço mas com expressão **determinada e firme**, não de dor. A 1ª
>   versão do díptico tinha os dois de frente e com cara de agonia.

---

## Regime e tratamento da fonte

**Regime: ESPINHA** (definido pelo user, 28/08). A fonte é "a teoria do cavalo teimoso", texto de
terceiro. Os 24 beats dela foram mantidos na ordem e consolidados em 17 slides. Nada de arco novo.

**Sem Florestapitalista** (definido pelo user). Não tem bicho de terno nem vila enxaimel: é um
**homem e um cavalo de verdade, na beira de um rio**. O resto da identidade FABULA continua —
gravura pen & ink P&B, papel envelhecido, moldura `moldura-fabula.png`, serif centralizada no topo,
negrito no punch.

**O que mudou em relação à fonte (três ajustes, o resto é tradução de voz):**
1. **Slide 13** — a lista "como pai, como irmão, como amigo" saiu inteira (corte do user, 28/08:
   dispersa e não é o nosso público). No lugar, a virada vai direta pro dono e já acusa: *"e todo
   dono de empresa já tentou. Beber no lugar do funcionário."*
2. **Slide 16** — a fonte fecha em *"cada um bebe quando chega a hora certa"*. Essa linha põe o
   dono pra esperar e tira ele da conta; vira **"sede não se exige, sede se cria"**. Troca de uma
   linha só, no vocabulário da própria fonte, e é o que sustenta o CTA (sem ela a peça fecha
   mandando o dono ter paciência, e não há o que vender).
3. **Não entrou** o bloco "conduza com gentileza / ame com paciência". Substituído por *"o seu
   papel é conduzir, não é arrastar"*, que já é da própria fonte (beat 20, "orientar, não
   controlar") e não nega cobrança.
4. **Saiu "uma história sobre cuidado"** (corte do user, 28/08). A peça abre direto na cena.
5. **Slide 6 reescrito** (apontamento do user, 28/08): a versão anterior repetia que os dois já
   estavam na margem e a fala "Bebe. Isso é bom pra você." saiu fofa demais pra voz da casa. O
   beat da fonte que importa aqui é *gentle at first* — o que arma a escalada do slide 8. Agora o
   slide mostra o GESTO, não a intenção (essa já é o slide 5): rédea devagar, tapinha no pescoço,
   e o dono pedindo por favor o que já é obrigação.

**Interlocutor:** dono de PME. A fonte fala com pai/irmão/amigo; o slide 13 faz a virada explícita
e do 13 ao 17 quem está em cena é quem manda a empresa andar.

**Causa técnica:** sede se cria devolvendo caminho — problema com dono, hora marcada e cobrança.
O dono que resolve tudo é a rota de fuga da empresa, e enquanto ele for a saída ninguém precisa
querer. É o que o CTA vende.

**Palavra-chave: FOME** (estado desejado, inédita no perfil). Descartada SEDE: em português é
também a matriz da empresa, ambiguidade ruim pro Manychat.

## Legenda (post)

Todo dono já puxou a corda. Levantou a voz, prometeu, ameaçou, apelou. E funcionou um pouco, por
uns dias. Depois voltou tudo.

O erro não é puxar. É achar que puxar é liderar.

Você não consegue querer no lugar de ninguém. Pode explicar, pode pagar melhor, pode gritar. A
vontade continua sendo do outro, e vontade não obedece ordem.

Mas tem uma parte que quase ninguém quer ouvir: se você é o único com sede na sua empresa, isso
também é obra sua.

Sede vem de necessidade, e dentro da maioria das empresas não falta nada pro funcionário. O
problema aparece e você resolve. A decisão trava e você decide. O cliente reclama e você atende.

Você virou a rota de fuga. Enquanto existir uma saída chamada dono, ninguém ali precisa ter sede.

Criar sede não é motivar. É devolver. O problema volta pra quem é dono dele, com prazo e com
cobrança. Incomoda no começo, e é o único jeito de alguém aprender a andar até o rio.

Empresa não se sustenta na energia de um homem só. Se sustenta em estrutura, e estrutura se
aprende. É isso que eu ensino no meu treinamento de gestão pra pequena e média empresa.

Comenta FOME que eu te mostro por onde começar.

Seja Bem-Vindo ao Fim do Analfabetismo Empresarial.

#gestao #lideranca #empreendedorismo #pequenaempresa #TatsuoAcademy

---

## Contexto de imagem de cada slide (gravura pen & ink, plano pela emoção do beat)

**Personagens fixos:** o HOMEM (magro, barba curta, camisa de linho sem colarinho com manga
dobrada, colete escuro, chapéu de aba larga, botas — trabalhador, nunca cavalheiro de cartola) e
o CAVALO (escuro, forte, cabresto de couro e corda comprida, sem sela). **Cenário fixo:** rio
largo, margem de areia e cascalho, juncos, árvores retorcidas, colinas ao fundo.

1. **Capa** — homem e cavalo na beira d'água, o cavalo de cabeça erguida recusando. Plano médio.
2. **A ida** — de costas, os dois descendo a trilha rumo ao rio distante. Plano geral.
3. **A água** — só paisagem, sem figuras: seixos sob a água clara, juncos ao vento. Respiro.
4. **A certeza** — perfil do homem olhando o cavalo com convicção, focinho em primeiro plano.
5. **A boa intenção** — ele olha a água pensando no bicho, mãos ao lado do corpo, o cavalo atrás.
   Nenhum gesto de oferecer ainda. *(v3)*
6. **No jeito** — o homem curvado, mão no pescoço do bicho, corda frouxa. O cavalo desviado.
7. **A recusa** — contra-plongée: a cabeça do cavalo alta contra o céu, o homem pequeno na borda.
8. **A força** — o homem dentro do raso puxando o cavalo PRA a água; o bicho fincado no seco,
   recuando. Corda esticada, respingos nas botas. *(v3)*
9. **A resistência** — **zenital puro** (câmera na vertical, sem horizonte): homem na água à
   esquerda visto de cima, cavalo fincado no seco à direita, corda esticada cruzando a linha
   d'água, marcas de arrasto em arco. Caixa `.wide` pra não cortar ninguém. *(v4)*
10. **Os dois sofrendo** — **díptico vertical**, os dois de perfil no mesmo instante se encarando:
    close do homem virado pra direita | close do cavalo virado pra esquerda. Suando, expressão
    determinada e firme. *(v4)*
11. **A exaustão** — entardecer, os dois juntos no miolo do quadro: ele sentado com o chapéu no
    colo, o cavalo de cabeça baixa ao lado, a corda largada entre os dois. *(v3, recomposta)*
12. **A ponte** — a superfície parada do rio com o reflexo dos dois espelhado e ondulado; os
    corpos ficam fora do quadro, só o reflexo aparece. *(v3, nova)*
13. **Não pode beber por ele** — o homem ajoelhado bebendo da própria mão enquanto o cavalo olha.
14. **Beber no lugar dele** — de trás do cavalo: o balde de água empurrado contra a boca fechada.
15. **Conduzir** — o homem à frente com a corda enrolada no ombro, o cavalo seguindo sozinho.
16. **O desgaste** — chão: a bota furada e o casco lado a lado na areia revirada, corda desfiada
    no meio. *(a versão em macro de mão saiu com anatomia deformada e foi descartada.)*
17. **A virada** — plano alto com folga nas bordas: o cavalo bebendo sozinho, o homem sentado
    longe, corda enrolada ao lado. *(v3, recomposta)*
18. **O único com sede** — o homem sozinho na beira d'água com a corda enrolada na mão; lá atrás,
    pequeno na crista da margem, o cavalo parado que não veio. *(v3, nova)*
19. **CTA** — de costas ao amanhecer, os dois subindo a trilha lado a lado, corda frouxa. O cavalo desviado.
7. **A recusa** — contra-plongée: a cabeça do cavalo alta contra o céu, o homem pequeno na borda.
8. **A força** — o homem puxando com as duas mãos, corpo inclinado pra trás, boca aberta gritando.
9. **A resistência** — plano alto: os dois pequenos e a areia revirada em arcos de arrasto.
10. **Os dois sofrendo** — macro só do punho fechado e da corda esticada saindo do quadro.
11. **A exaustão** — entardecer: ele sentado com o chapéu no colo, o cavalo de cabeça baixa, a
    corda largada no chão entre os dois, o rio intocado atrás.
12. **Não pode beber por ele** — o homem ajoelhado bebendo da própria mão enquanto o cavalo olha.
13. **Beber no lugar dele** — de trás do cavalo: o balde de água empurrado contra a boca fechada.
14. **Conduzir** — o homem à frente com a corda enrolada no ombro, o cavalo seguindo sozinho.
15. **O desgaste** — chão: a bota furada e o casco lado a lado na areia revirada, corda desfiada
    no meio. *(v2 — a versão em macro de mão saiu com anatomia deformada e foi descartada.)*
16. **A virada** — plano alto: o cavalo bebendo sozinho, o homem sentado longe, corda enrolada.
17. **CTA** — de costas ao amanhecer, os dois subindo a trilha lado a lado, corda frouxa.

---

## Texto que renderiza em cada slide

**Slide 1 (capa)**
A teoria do cavalo teimoso.
Uma pequena fábula para pequenos e médios empresários

**Slide 2**
Certa vez, um homem levou o seu cavalo até o rio.

**Slide 3**
Água limpa. Brisa fresca.
**Tudo perfeito.**

**Slide 4**
Ele tinha certeza de que o cavalo ia beber.
"O bicho está cansado, deve estar com sede.
**Essa água vai fazer bem pra ele."**

**Slide 5**
Ele tinha boa intenção.
**Ele se importava.**

**Slide 6**
Primeiro tentou no jeito.
Puxou a rédea devagar. Bateu no pescoço.
**Falou com o bicho como quem pede um favor.**

**Slide 7**
Mas o cavalo não abaixou a cabeça.
Não bebeu. Não se mexeu.
**Simplesmente não estava com sede.**

**Slide 8**
O homem se irritou.
Insistiu mais. Levantou a voz.
**E tentou forçar o cavalo a beber.**

**Slide 9**
Só que quanto mais ele forçava,
**mais o cavalo resistia.**

**Slide 10**
Nenhum dos dois estava errado.
**Mas os dois estavam sofrendo.**

**Slide 11**
No fim, os dois ficaram exaustos.
**E nada tinha mudado.**

**Slide 12** *(v3 — ponte entre a história e a lição)*
O homem tinha razão. A água era boa.
**Só que ter razão nunca fez ninguém beber.**

**Slide 13**
Você pode levar alguém até o rio.
Pode mostrar o caminho. Pode dizer que a água é boa.
**Mas não pode beber por essa pessoa.**

**Slide 14**
E todo dono de empresa já tentou.
**Beber no lugar do funcionário.**

**Slide 15**
O seu papel é conduzir.
**Não é arrastar.**

**Slide 16**
Forçar alguém a mudar não faz essa pessoa crescer.
**Só faz vocês dois se acabarem.**

**Slide 17**
As pessoas se movem quando sentem sede.
**E sede não se exige. Sede se cria.**

**Slide 18** *(v3 — devolve a responsabilidade pro dono)*
Se hoje você é o único com sede dentro da sua empresa,
**talvez você ainda não tenha despertado essa sede em ninguém.**

**Slide 19 (CTA)** *(v3 — slide próprio, amarrado à estrada do Hélio)*
Eu já fui esse homem puxando a corda.
Levei mais de 38 anos de empresa pra aprender
que time não se arrasta. Se constrói.
**Comenta FOME que eu te mostro por onde essa construção começa.**

---

> **Tracking:** palavra única deste post = **FOME** (variantes no Manychat: fome / Fome / FOME).
> Automação de publicação ESPECÍFICA, nunca global.
