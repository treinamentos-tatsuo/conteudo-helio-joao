# Post 65 — Sem pressão, o feijão não cozinha.

**Formato:** frase única. **Semente:** banco de frases nº 21 (lote 5, cotidiano brasileiro).
**Slide:** 1 linha, 44px, toda em preto.

## Frase

Sem pressão, o feijão não cozinha.

- **Formato:** lei observada. **Veia:** pressão — a nº 1 do perfil, onde estão todos os maiores hits.
- **Mecanismo:** AUTODECLARAÇÃO — "a pressão que estou sentindo é o que está me deixando pronto".
  Quem compartilha se declara em cozimento, não em sofrimento. Segunda camada: sem pressão nada
  fica pronto; pressão não é castigo, é o processo.
- **Cotidiano:** panela de pressão é objeto de toda casa brasileira, e todo mundo já ouviu o pino chiar.

## Imagem (img-01, conceito 1 de 3, primeira geração)

Close numa panela de pressão de alumínio velha e amassada na boca do fogão, jato grosso de vapor
saindo do pino, parede encardida e quase preta atrás. Sem figura humana. Sem scale no slide.

- **Cuidado técnico aplicado:** vapor é branco e sumiria no `mix-blend-mode:multiply` — o prompt
  pediu parede escura e encardida atrás (mesmo conserto da cachoeira do post 38 e da cancela do 59).
  Funcionou de primeira e o jato ficou o elemento mais legível do quadro.
- **Não precisou alongar o fade:** o vapor é claro, então a faixa do texto ficou limpa com o mask
  padrão de 26%.
- **Conceitos descartados (não chegaram a ser gerados — user escolheu no cardápio):** cozinha ao
  amanhecer com o vapor cortando a luz da janela (dividia atenção entre panela e ambiente) e o
  contraste de duas panelas, uma fechada fervendo e outra aberta com feijão cru.

## Legenda

Ver `legenda.txt` (2.075 caracteres, 10 parágrafos — 125 de folga até o limite do Instagram).
Espinha do gabarito raso: lei sem narrador (a água que não passa dos cem) → o concreto (a panela
fechada, o pino, o vapor) → a vida montada sem pressão → empresa como mais um lugar do mesmo fogo
→ **antídoto da regra 24/26: panela de pressão é pressão COM VÁLVULA** (sem tampa nada cozinha,
sem válvula explode; apertar time sem caminho de saída é estourar gente) → a hora de abrir (o dono
que muda de rumo a cada dois meses) → **a panela vazia** → pergunta-espelho → a frase fecha.

### Os dois fechos de brecha (o que faz a legenda não virar "sofra mais")

1. **A válvula.** Sem ela a frase leria como apologia do aperto. A panela resolve sozinha porque
   não é só pressão: é pressão contida E com saída.
2. **A panela vazia também apita** (acrescentada a pedido do user, 28/08). Separa *estar sob
   pressão* de *estar cozinhando alguma coisa* — a distinção que a frase sozinha não faz. Sem ela,
   quem se orgulha do próprio esgotamento lê o post como elogio. Com ela, a pergunta vira "pressão
   em cima de quê?", e a responsabilidade volta pro dono (regra 16). Punch: *"O apito não prova que
   tem feijão dentro. Prova que tem fogo embaixo."*

**Versão descartada (B):** mantinha o bloco "E tem o resto: fogo constante, tempo certo, e não
abrir antes da hora". Custava só 50 caracteres a mais que a A — a escolha não foi por economia e
sim por ritmo: "fogo constante" e "tempo certo" entravam e saíam sem trabalhar, e vindo logo após
o parágrafo da válvula (que já é uma lista de condições) davam sensação de ladainha justo onde o
texto precisa acelerar pra pergunta-espelho. Na A esse trecho virou uma frase só.

## Aprendizados técnicos deste post

- **A fumaça É o degradê.** O que o user mais elogiou não foi projeto: pedi metade superior clara
  e parede escura atrás, e a geração entregou o vapor se dissolvendo no papel envelhecido sozinho.
  Vale como técnica reutilizável — elemento que já é vapor, fumaça, poeira ou névoa resolve a
  transição pro fundo sem depender do mask.
- **Subir imagem é CSS, nunca regeração.** Pedido de "sobe um pouco" resolvido com
  `height:1135px; object-fit:cover; object-position:center top` ancorado em `bottom:0` — reenquadra
  sem distorcer (cover preserva proporção) e sem abrir faixa de papel nu no pé, que era o problema
  do `bottom:55px` registrado no post 57. Enquadramento anterior preservado em `slide-01-v1.png`.
- **Elemento branco contra fundo escuro, de novo.** Terceira confirmação (cachoeira do 38, cancela
  do 59, vapor aqui): elemento claro some no `multiply` se o entorno for claro. Pedir fundo escuro
  atrás resolve na primeira geração.
