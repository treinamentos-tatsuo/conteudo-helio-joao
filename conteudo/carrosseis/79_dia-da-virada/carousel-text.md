# Carrossel 79 — O dia da virada (D1-S64)

**Modelo:** editorial-punch · **11 slides** · **Tema:** ponto de equilíbrio não é um número abstrato, é uma DATA — o dia do mês em que a empresa termina de pagar todo mundo. Do dia seguinte em diante, todo faturamento vira lucro; e é isso que abre margem pra negociar venda que antes quebraria.

> **Fonte:** semente **D1-S64** de `_contexto/banco-scouting-mbv/dia1-lucratividade.md` — *"Ponto de equilíbrio de 242 mil num faturamento de 300: você trabalha 24 dias do mês sem ganhar nada, só pra empatar. Sobram seis dias pra fazer o lucro. E nesses seis tem sábado e domingo. Até que dia do mês você trabalha só pra pagar as tuas contas?"*
>
> **Pilar:** Lucratividade. MBV não nomeado nos slides.

## Duas declarações de saída (regra da skill)

- **Interlocutor:** dono de PME. Nenhum slide fala com quem executa. Todos os verbos são de quem decide a conta: pagar folha, dar desconto, contratar, segurar custo. Conferido slide a slide.
- **Causa técnica:** **ponto de equilíbrio lido como data.** Saber o dia em que a fila de pagamentos termina muda três decisões concretas: até onde dá pra baixar preço, se cabe custo fixo novo, e quanto custa um dia parado. É isso que o CTA e o treinamento vendem — nunca "vender mais".

## Por que este desenho (o que o dado impôs)

- **Roupa DIRETO, sem metáfora.** Os três piores carrosséis do pilar são metáfora pura (ladrão silencioso 22,7 · porta pra dentro 24,4 · draga 30,7); os dois melhores são diretos com número que vira imagem (empresa escondida 65,3 · come antes de você 59,1).
- **Nervo aponta pro sistema, nunca pro caráter do dono.** Em nenhum slide o leitor é o culpado: o vilão é uma conta que ninguém mostrou pra ele. Dentro de Lucratividade, o único carrossel de nervo acusatório (porta pra dentro, "dono-culpado") é o segundo pior do pilar.
- **Calibragem doutrinária do user (01/09):** o dono de PME **acha que tem lucro** — calcula errado e chama de lucro o pró-labore que ele mesmo arbitrou. Isso NÃO vira slide (virou, na v1, e sobrecarregou a peça): mora na legenda. Cuidado permanente: nunca acusar o dono de sacar demais de propósito; o número é arbitrário, não ganancioso.
- **Contrato de retenção no slide 2.** Tema técnico perde o leitor no meio. O slide 2 nomeia o conceito e promete o ganho de imediato, pagando o preço da leitura adiantado. A promessa não vai pra capa: o acervo tem 0 de 59 capas que prometem ensinar algo, e julgar gancho no olho não prevê nada nesta conta (correlação −0,13 no teste cego). Ver a nota de teste no fim deste arquivo.
- **Camada humana num tema de dinheiro.** O objeto do post não é a planilha, é o tempo de vida do dono: 24 dias dele trabalhados de graça.
- **Palavra-chave do CTA:** **VIRADA** — única, caixa alta, sem acento, derivada do batismo ("o dia da virada"). Ineditismo conferido no `registro-posts.csv`. Alternativa se preferir: DIA25.
- **Previsão pro /etiqueta:** `mediana`. Não é pessimismo: 8 de 8 previsões `acima` em Lucratividade erraram pra baixo, e nenhum dos 8 carrosséis do pilar passou da banda alta.

**Universo de imagem:** documental P&B vintage do **mês passando dentro da empresa real** (PME: comércio, oficina, balcão). O calendário de parede como objeto-herói, o relógio, o envelope, a porta, a mesa do fim do dia. Nada de gráfico, planilha ou dinheiro em cena de dólar.

> **Risco de texto na imagem (regra 31/08):** calendário é objeto que existe pra ser escrito, e o motor escreve — inclusive erra a lógica dos dias. Todo slide com calendário, folhinha ou papel entra na lista de conferência e o prompt pede a ilegibilidade como CONSTRUÇÃO da foto (profundidade rasa, números borrados, ângulo rasante, folha cortada pela borda), nunca como proibição no fim do prompt.

---

## Contexto de imagem de cada slide (v3)

1. **Capa** — img-01: calendário de parede riscado a caneta, números borrados. Still.
2. **Nomeia e promete** — img-04: mãos empurrando a xícara e puxando o caderno. "Senta aqui." Mãos.
3. **O que é** — img-05: dedo pousado sobre um dia da folhinha. Mãos.
4. **A fila (o que é empatar)** — img-02: o dono no balcão no fim do dia, papelada paga do lado. *(humano)*
5. **A conta** — img-18 (NOVA, pedido do user): fila de pessoas enfileiradas esperando pra receber no balcão. *(humano)*
6. **Depois da data** — img-07: manhã cedo, porta abrindo, entregador deixando caixa. *(humano de costas)*
7. **Os quatro dias** — img-08: canto final do calendário com duas cruzes. Still.
8. **A data vira margem** — img-14 (NOVA): aperto de mão fechando negócio sobre o balcão. *(humano)*
9. **O comando** — img-15 (NOVA, substitui as "mãos fantasmas"): o dono inteiro no balcão, decidido, caderno aberto na frente. *(humano)*
10. **Doutrina** — img-16 (NOVA, substitui o relógio): folhinha NOVA e limpa sendo pendurada na parede, nenhum dia riscado ainda. Rima visual invertida com a capa. Mãos.
11. **CTA** — img-17 (NOVA): o dono de pé na própria loja, postura firme, olhando pra frente. *(humano)*

> **Fora:** img-03 (cédulas) e img-09 (balança), das teses cortadas. img-11, img-12 e img-13 saem na v3 por reprovação do user (mãos fantasmas · relógio morto · expressão estranha).

---

## Texto dos slides

### Slide 1 — Capa
> Eu, você, todo empresário
> **TRABALHA DE GRAÇA.**
> ~até um certo dia.~

### Slide 2 — Nomeia e promete
> E isso tem nome: Ponto de Equilíbrio.
>
> Empresário que entende isso
> **SABE O DIA EM QUE COMEÇA A LUCRAR.**

### Slide 3 — O que é (ponte)
> Não é um número na planilha.
> É um dia no calendário.
>
> O dia em que a empresa terminou
> **DE PAGAR TODO MUNDO QUE DEVIA.**
> ~fornecedor, folha de pagamento, banco...~

### Slide 4 — A fila (o que é empatar)
> Vamos supor isso em datas.
> Imagine que dia 5 paga o fornecedor,
> dia 10 a folha, dia 20 o imposto.
>
> Enquanto essa fila não acaba,
> a empresa está no negativo.
> **O ZERO A ZERO É QUANDO O ÚLTIMO RECEBE.**

### Slide 5 — A conta
> Você fatura 300 mil no mês.
> Pra pagar a fila inteira,
> precisa faturar 242 mil reais.
>
> Imagine que essa fila só acabe
> **NO DIA 24.**

### Slide 6 — Depois da data
> Do dia 1 ao 24 você abriu a loja
> pro fornecedor, pro banco e pro governo.
>
> Do dia 25 em diante,
> **TODO FATURAMENTO VIRA LUCRO.**

### Slide 7 — Os quatro dias
> Sobram 6 dias pra fazer o lucro do mês.
> E nesses 6 tem sábado e domingo.
>
> **4 DIAS PRA BOTAR DINHEIRO NO BOLSO.**
> ~seu e da empresa.~

### Slide 8 — A data vira margem
> E é aqui que a data vira dinheiro.
> Depois dela, cada venda é margem inteira.
>
> O desconto que te quebraria no dia 10
> **FECHA NEGÓCIO NO DIA 26.**

### Slide 9 — O comando
> Quem sabe a data para de decidir no escuro.
> Sabe até onde pode baixar o preço.
>
> Sabe se aguenta o funcionário novo.
> **E SABE QUANTO CUSTA CADA DIA PARADO.**

### Slide 10 — Doutrina
> A data não aparece no fim do mês.
> Ela é calculada antes dele começar.
>
> Isso é gestão.
> **O RESTO É TORCER PRA SOBRAR.**

### Slide 11 — Fechamento + CTA
> O mês não começa no dia 1.
> Pra você, ele começa no dia da virada.
>
> Comenta **VIRADA** que eu te mostro
> como achar a sua e puxar ela pra trás.

---

## Legenda (post)

Todo empresário sabe quanto faturou. Quase nenhum sabe até que dia do mês ele trabalha de graça.

O dono aprendeu a olhar o mês como um bloco só: entrou tanto, saiu tanto, sobrou isso. Só que o mês não é um bloco. Ele tem ordem.

Primeiro você paga o fornecedor. Depois a folha. Depois o imposto, o aluguel, a energia. Todo mundo passa na sua frente. Você é o último da fila do seu próprio negócio.

E aqui mora o erro que quase todo dono comete: ele tira um valor no fim do mês, olha pro que tirou e chama aquilo de lucro. Não é. Aquilo é o seu salário, um custo como outro qualquer. Lucro é o que sobra depois que a empresa te paga.

Quando você separa as duas coisas, o ponto de equilíbrio vira uma data no calendário. O dia em que a empresa deixa de trabalhar pros outros e começa a trabalhar pra você.

E tem mais: o lucro do mês inteiro está espremido nos últimos dias. Por isso um mês fraco não come um pedaço do seu lucro. Come quase todo ele.

É o dono que decide o custo fixo. É o dono que aprova o desconto que empurra a data pra frente. É o dono que contrata sem saber quantos dias aquilo custa.

Vender mais sem saber a data não resolve. Só acelera.

Empresa não quebra de repente. Ela quebra num dia que o dono nunca calculou.

Comenta VIRADA que eu te mostro como achar o seu dia e trazer ele pra mais perto do começo do mês.

Seja Bem-Vindo ao Fim do Analfabetismo Empresarial.

