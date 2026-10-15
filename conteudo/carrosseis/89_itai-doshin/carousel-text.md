# Carrossel 89 — Itai Doshin (adaptação do post de 20/02/2026)

Fonte, dados e copy original intacta em `briefing.md`. Modelo: **editorial-punch**, modo `espinha` (mesmos beats, mesma ordem; trabalho só de linguagem e diagramação). Palavra-chave: **JUNTOS** (inédita no `registro-posts.csv`).

## Declarações de saída

- **Interlocutor:** dono de PME do começo ao fim. Nenhum slide fala com quem executa; o "cara", o "time" e o "funcionário bom" são sempre objeto da decisão do dono.
- **Causa técnica:** pilar Cultura do MBV. Rotatividade de gente boa não é preço de mercado, é ausência de sonho compartilhado; e sonho compartilhado não é discurso, é rotina de gestão (decisão, padrão, cobrança, reconhecimento, exemplo). É isso que o treinamento vende.

## Mudanças em relação ao original (aprovadas em 04/09)

1. Capa em um slide só (setup + grito), no lugar dos slides 1 e 2.
2. Slide 2: "o que segura alguém" → "o que faz alguém ficar de verdade" (doutrina 11/08: a pessoa escolhe ficar).
3. Slide 11: "emanados" → "irmanados".
4. Slide 15 original dividido em dois (14 e 15): o "como" ganha slide próprio.
5. CTA: "cultura" → **JUNTOS**.
6. Legenda nova (a original repetia os slides).

## Contexto de cada slide (guia da imagem) — v2, conceito próprio

**Universo único, da capa ao CTA: uma padaria de bairro brasileira.** Madrugada, forno, farinha, gente de verdade. Nada herdado das fotos do post original (v1 copiava os motivos do original e foi reprovada pelo user em 04/09: *"eu quero como se fosse nos moldes atuais, você só se baseia na copy e faz os slides novos, com imagens novas pensadas no seu conceito. Sem grifado nem nada"*). As 16 da v1 estão em `imagens/_v1-copia-do-original/`.

Todas: P&B editorial vintage, landscape 1536×1024, base/base_wide do 83, cláusula de cinema nas cenas com gente (cabeça inteira, luz lateral, câmera na altura do peito). Prompts em `_scripts/prompts.json`.

1. **Capa.** Vestiário da padaria: avental dobrado no banco com o envelope do pagamento fechado em cima, armário aberto e vazio. Pago e foi embora.
2. Envelope de pagamento passando de mão em mão sobre o balcão enfarinhado. Obrigação, transação.
3. Close no padeiro jovem encostado na porta dos fundos ao amanhecer, olhando a luz (v3; v1 de dentro pra fora reprovou no topo.py, v2 aberta foi reprovada pelo user: "mais focada no personagem que ângulo aberto").
4. Mão cansada enfiando o cartão no relógio de ponto mecânico antes do amanhecer.
5. Três padeiros tirando a fornada do forno de tijolo juntos, vapor, rindo.
6. Cinco do time espremidos no banco do café da manhã, cesta de pão e canecas de lata.
7. Funcionário de noite com o braço dentro da masseira quebrada, lanterna na boca, chaves no chão.
8. Dono sozinho atrás do balcão vazio depois de fechar, chaves na mão, cadeiras viradas.
9. Dono na cabeceira da mesa discursando de braços abertos, dedo pro alto; ninguém do time olha pra ele (caneca, bocejo, porta). v2; a mesa com calculadora e gráfico foi reprovada pelo user ("ruim demais").
10. Padeiro entregando o pão quente pra uma criança no balcão, avó ao lado.
11. De cima: mãos diferentes (jovem, velha, tatuada) na mesma massa.
12. Padaria inteira em movimento, cada um no seu posto (forno, balcão, entrega, mesa).
13. Funcionário saindo pela porta dos fundos de mochila; avental e touca largados no gancho.
14. Dono grisalho e aprendiz lado a lado às quatro da manhã, mãos na mesma massa.
15. Time inteiro na frente da loja sob a porta de aço meio aberta, braços nos ombros, amanhecer.
16. **CTA.** Mãos diferentes empurrando a porta de aço pra cima, luz entrando.

**Diagramação:** setup em Source Serif preta + grito em Anton carmim. Sem grifo, sem elemento à mão, sem kanji/ensō. **Altura do texto = padrão da skill: `top:160` no corpo, `top:200` na capa (sujeito baixo).** A v2 saiu com `top` 236–400 herdado do `build.py` do 83 e o user reprovou ("você não pode ser influenciado pelo que não está na skill") — mesma armadilha da entrada de 21/08 do `erros-frequentes.md`.

**Cenas regeradas mais fechadas (v3) por causa do texto no piso da skill:** 5, 6, 8, 10, 12, 15 saíram de `base_wide` pra `base` + cláusula de cinema com "people LARGE and CLOSE, chest up, heads at one fifth from the top". Com o texto em 160 o `base_wide` (sujeito na metade de baixo) deixa 400–570px de vão e o teto de recorte de 18% não alcança; cena fechada resolve na geração, não no recorte. Recortes finais em `_scripts/imgheight.json` (24–42% nas cenas em que as pontas eram dispensáveis: 2, 3, 4, 7, 9, 11, 14, 16). Vão morto final ≤ 246px em todos, exceto o 2 (338 pelo detector; o envelope claro engana a régua, no olho está no lugar).

## Legenda (post)

Salário é obrigação. Paga a presença, paga a função, e precisa ser justo. Mas dinheiro nunca fez ninguém proteger o time, comprar a briga ou recusar uma proposta melhor. Quem acha que paga bem e por isso merece lealdade está confundindo contrato com pertencimento.

Eu vejo muito dono cometer o mesmo erro. Ele reúne o time, fala do tamanho que quer alcançar, do faturamento que quer bater, da empresa que quer construir. E espera que todo mundo se emocione. Ninguém se emociona. Ninguém acorda animado pra realizar o sonho de outra pessoa.

A pessoa fica quando enxerga o lugar dela dentro do que está sendo construído. Quando entende que, ao ajudar a empresa a crescer, ela também está ganhando: dinheiro com dignidade, conhecimento que eleva a vida dela, orgulho do que entrega, prazer em fazer parte. Ela não fica pelo dono. Fica pelo futuro dela. E o dia que essa chave vira, ela entrega porque quer.

Os japoneses chamam isso de Itai Doshin: corpos diferentes, um único coração. Não é todo mundo pensar igual nem abrir mão do próprio interesse. É cada um no seu papel, sabendo pra onde o grupo vai e por que vale a pena chegar junto.

Só que isso não nasce de frase bonita. Nasce do jeito que você decide, cobra, promove, reconhece e dá exemplo todo dia. Cultura é o sonho confirmado pela rotina. Quando a rotina desmente o discurso, o time acredita na rotina.

Comenta JUNTOS que eu te mostro como colocar Itai Doshin em prática na sua empresa.

Seja Bem-Vindo ao Fim do Analfabetismo Empresarial.

## Slides (texto que renderiza)

Convenção: linha em **negrito** = punch vermelho (Anton caixa alta ou serif bold carmim, conforme o slide); `//` = respiro entre estrofes. Grifos da v1 removidos a pedido do user (04/09).

1. Deixa eu te falar uma verdade meio chata: / **funcionário bom não fica só por salário.**
2. Salário é o básico. / **O que faz alguém ficar de verdade é outra coisa.**
3. **O sonho.**
4. Porque ninguém acorda animado / **pra bater ponto.**
5. Acorda animado / **pra fazer parte de algo.**
6. Quando a empresa tem sonho, / o cara não tem só um trabalho. // **Ele sente que tem um lugar.**
7. E aí muda tudo. / Ele não faz só tarefa. // **Ele compra a briga.**
8. Agora vem a pergunta que incomoda: / **qual é o sonho que a sua empresa tá oferecendo?**
9. **E não é o seu sonho, tá?**
10. É o sonho que o time consegue falar / sem pensar muito: // **"eu tô aqui por isso."**
11. Os japoneses têm um nome bonito pra isso: / **Itai Doshin.** // Corpos diferentes, / **irmanados num único coração.**
12. Cada um num papel... / **mas todo mundo puxando pro mesmo sonho.**
13. Sem isso, eles só enxergam escala. / **Escala não dá pertencimento.** // Escala dá rotatividade. / Apareceu algo melhor, o cara vai.
14. Por isso cultura não é frase na parede. // Cultura é o sonho vivido todo dia, / **em decisão, rotina, padrão e exemplo.**
15. Quer gente leal? / **Então constrói um sonho que valha a pena viver junto.**
16. Comenta **JUNTOS** / que eu te mostro como colocar Itai Doshin em prática na sua empresa.
