---
name: caixinhas
description: Escreve as caixinhas de pergunta dos stories do Hélio - a pergunta como se fosse o nosso ICP digitando e a resposta curta na voz do Hélio, tirada do MBV, com CTA pro MBV ou pro RAIO-X. Também responde caixinha real de seguidor. Use quando o user disser "caixinha", "caixinha de pergunta", "pergunta dos stories", "responde essa caixinha" ou mandar o texto do story que abriu.
---

# /caixinhas: pergunta e resposta dos stories

## O que é

O user abre uma caixinha de pergunta no story do Hélio e não quer depender do seguidor. **Nós escrevemos a pergunta como se fosse o nosso ICP perguntando pro Hélio**, e escrevemos a resposta do Hélio. Palavras do user (24/09): "São caixinhas de pergunta que nós mesmos vamos escrever, mas como se fosse o nosso prospect." Às vezes chega também uma pergunta real de seguidor pra responder.

**Entrada:**
- O texto do story ou da caixinha que o user abriu. Ex.: "me conta qual foi o seu maior perrengue durante a semana na sua empresa"; "faturamento anual, número de funcionários e maior desafio".
- Quantas perguntas (nas últimas vezes, 3).
- Ou: a pergunta real de um seguidor, mais o que se sabe da pessoa (perfil, voto em enquete).

## Passo 1: antes de escrever

- Abrir as transcrições do MBV em `_contexto/transcricoes-mbv/` (dia 1 Lucratividade, dia 2 Crescimento, dia 3 Cultura) e o guia de voz `_contexto/preferencias.md`. As transcrições não vão pelo Git (são o treinamento pago e ficam só na máquina). **Se a pasta não existir nesta máquina, parar e avisar o user:** sem a fala do Hélio, a resposta não sai.

## Passo 2: a pergunta (quando nós escrevemos)

- **Quem pergunta é o ICP:** dono de empresa que fatura de R$3 a R$100 milhões por ano, com 10 funcionários ou mais. Todo número da pergunta fica dentro desse porte. "900 mil/mês" dá uns 10,8 milhões por ano e serve; "180 mil por mês" dá 2,16 milhões e fica fora; "6 funcionários" fica fora. A dor é a de quem fatura milhões e não vê sobrar, nunca a do micro.
- **Cara de dono digitando no celular**, entre uma coisa e outra: corrido, em minúscula, sem caprichar na pontuação. O user cobra: "essa pergunta um seguidor nosso faria? O nosso ICP? ele escreveria deste jeito?" (05/10). Pergunta limpa, com pontuação certinha, parece montada pra encaixar a resposta.
- **Um detalhe humano, de preferência o ramo:** "vamos colocar uma informação de ramo... as pessoas nunca respondem bonitinho" (11/10).
- **Cabe na caixinha:** uns 100 caracteres. Uma pergunta de 191 foi reprovada ("tem que ser metade disso, no máximo. Não cabe na caixinha"). Contar os caracteres antes de entregar.
- Segue o formato que a caixinha pediu. Se pediu faturamento, funcionários e desafio, a pergunta vem nessa ordem.

## Passo 3: a resposta (voz do Hélio)

- **Curta, é stories.** "Mais curto, é stories" (09/10). "Ser mais humanizado não é ser mais longo e prolixo, é escrever menos IA e mais humano" (05/10). Umas 3 frases mais o CTA.
- Pode ter lista curta e frase de fechamento. A resposta que o próprio user escreveu pra biomédica (exemplo abaixo) tem as duas.
- **Cada afirmação sai da fala do Hélio no MBV**, conferida na transcrição antes de entregar. O user: "isso está totalmente correto? não podemos errar, é o Hélio quem fala isso?" (05/10). Nada de rotina, prazo, promessa ou história que ele não diz. Em 05/10 entraram "escolhe uma pessoa pra decidir em cada área" e "você viaja e faz os 15 minutos por telefone", que o Hélio nunca disse, e tiveram que sair.
- Português revisado. Não misturar te e você na mesma frase.

## Passo 4: o CTA

Quem escreve escolhe pela profundidade do tema: **tema técnico, que faz sentido levar pro treinamento, vai pro MBV; o resto vai pro RAIO-X.**
- **MBV:** "É essa gestão que eu ensino no MBV. Link na bio." O MBV ensina gestão: o CTA não promete o passo a passo do que a resposta falou. O CTA pode sair da própria imagem da resposta, desde que fluido (no 900 mil, o user pediu "coloque cta para MBV fluido e criativo").
- **RAIO-X:** "Responde RAIO-X aqui que eu mando a aula pra você." Só funciona com a automação `RAIO - X stories` ativa no Manychat: lembrar o user de conferir antes de postar. A aula é paga: nunca chamar de gratuita.

## Passo 5: pergunta real de seguidor

- Responder a pergunta como ela veio. Pode abrir com o que está no perfil ou no voto da enquete ("Dei uma olhada no seu perfil e vi que você é dona de clínica estética"), sem nome e sem nenhum dado além disso.
- **Caso, não regra:** em 05/10 a pergunta veio de uma biomédica esteta, fora do ICP ("provavelmente ela não entende nada de negócios nem é nossa ICP"). A resposta ficou útil, com passos que ela consegue fazer no dia seguinte, e sem CTA.

## Passo 6: entrega

- Cada item numerado: a pergunta num bloco e a resposta noutro.
- Depois, **"de onde vem cada resposta"**: o dia do MBV e a fala do Hélio que sustenta cada afirmação.
- Lembretes no fim: `RAIO - X stories` ativa, se alguma resposta usou RAIO-X.
- Texto que o user devolver editado é o final. Só revisar português e tratamento, e dizer o que mudou e por quê.

## Exemplos

### Aprovados (11/10, fechado com "você é fodaaaa")

Caixinha do story: "faturamento anual, número de funcionários e maior desafio".

**1.**
> 8 milhões, 22 funcionários, não consigo sair do operacional

> Com 22 pessoas, se tudo passa por você, é porque você ainda não delegou de verdade. Delegar é dizer o que, como e quando, e acompanhar todo dia. Sem isso você só larga a tarefa e depois volta pra apagar o incêndio. É essa gestão que eu ensino no MBV. Link na bio.

Fonte: dia 3, "delegou ou delargou" e "o que, como, quando".

**2.**
> distribuidora de material elétrico, 25 mi, 60 funcionários. vendo bem mas nunca sobra pra distribuir

> Lucro é número no papel, mas pra distribuir precisa de dinheiro no caixa. Se o seu lucro não aparece no caixa, tem alguma coisa errada no meio do caminho. Responde RAIO-X aqui que eu mando a aula pra você descobrir onde está esse dinheiro.

Fonte: dia 1, "lucro é resultado no papel, dividendo exige caixa". A pergunta tem 100 caracteres. A versão anterior, com região e "trabalho de domingo a domingo", tinha 191 e foi reprovada por não caber.

**3.**
> 4,5 mi, 15 funcionários, achar gente boa e manter

> Gente boa trabalha com você por opção, porque tem outras portas abertas e escolhe a sua. Pra isso ela precisa ver que ao seu lado ganha mais e cresce mais. E pra pagar bem a empresa precisa ter margem. É isso que eu ensino no MBV. Link na bio.

Fonte: dia 3, "profissional bom escolhe com quem vai trabalhar" e "pra pagar bem tem que ter margem".

### Pergunta real fora do ICP (05/10, texto final do user)

Caixinha do story: "qual o maior problema da sua empresa ao longo da semana?". Quem respondeu é biomédica, dona de clínica estética, e votou "gestão" na enquete anterior. A pergunta dela: "Não consigo achar o erro, minha gestão deve ser péssima, mas também não sei como mlehorar" (assim mesmo, digitada no celular).

> Dei uma olhada no seu perfil e vi que você é dona de clínica estética. Bom, vamos lá:
> você estudou anos pra ser boa no que faz, mas ninguém ensinou você a ser dona. O problema está aí.
> Começa pelo básico, que é onde quase todo profissional que abre o próprio negócio se perde:
>
> 1. Separa o seu dinheiro do dinheiro do negócio. Conta separada e um valor fixo pra você todo mês.
> 2. Descobre quanto sobra de cada procedimento depois de pagar o material, o aluguel e o seu tempo. Tem serviço que enche a agenda e não deixa nada.
> 3. Anota toda semana quanto entrou e quanto saiu. Quem não olha o número não encontra o erro.
>
> Ser boa no que faz enche a agenda, mas só a gestão faz sobrar dinheiro.

O texto é do user. A revisão mudou só duas coisas: "ninguém te ensinou" virou "ninguém ensinou você" (a frase começava com "você") e "O problema está aí:" ganhou ponto final.

### Aceitos sem retorno (o user não corrigiu nem aprovou; servem de referência, não de modelo fechado)

**09/10**, story "me conta qual foi o seu maior perrengue durante a semana na sua empresa", versão depois do "mais curto, é stories":

> meu melhor vendedor pediu as contas na terça e ja to vendo cliente indo junto com ele. semana pesada

> Se o vendedor sai e leva o faturamento, quem vendia era ele, não a sua empresa. O jeito de vender tem que estar no papel, escrito por você, pra quem sair não levar a empresa no bolso. É essa gestão que eu ensino no MBV. Link na bio.

> fechei setembro com o maior faturamento do ano e essa semana tive que tirar da minha conta pra pagar a folha. como pode isso

> Faturamento não diz se a empresa está deixando você mais rico ou mais pobre. Lucro é número no papel, e quem paga a folha é o dinheiro no caixa. Se você não sabe onde esse dinheiro está, responde RAIO-X aqui que eu mando a aula pra você.

> expliquei o mesmo processo 3 vezes essa semana e na sexta erraram de novo. to cansado de falar

> Depois de qualquer treinamento, ninguém faz do jeito que eu falei. Escreve o processo, mostra o papel quando errarem e amanhã cobra de novo. Ser dono é ser chato. Fazer isso virar cultura é o que eu ensino no MBV. Link na bio.

Fontes: dia 2 ("se você perde um vendedor... perdeu 30% do faturamento", "quem tem que fazer o playbook são vocês", "depois de um treinamento ninguém vai fazer do jeito que eu falei"); dia 1 ("lucro é resultado no papel, dividendo exige caixa", "mais rico ou mais pobre"); "ser dono é ser chato" é frase do guia de voz.

**05/10**, 900 mil (o user escolheu esta versão da pergunta e pediu o CTA pro MBV):

> Hélio minha empresa fatura 900 mil/mês e mesmo assim todo mês to no banco pegando dinheiro pra pagar fornecedor, não entendo

> Eu te explico. Quando a empresa fatura bem e mesmo assim vive no banco, normalmente é uma de duas coisas.
>
> A primeira é o prazo. Conta quantos dias a mercadoria fica parada no estoque e quantos dias você leva pra receber do cliente, depois compara com o prazo que o fornecedor dá pra você pagar. Se você paga antes de receber, o dinheiro some nesse buraco, e quanto mais você vende maior ele fica.
>
> A segunda é mais grave: a empresa não está dando lucro e o dinheiro do banco, a três por cento ao mês, está tapando isso. Segura por um tempo, mas é igual bicicleta. Quando ela para, tomba.
>
> Antes de pegar o próximo empréstimo, descobre qual das duas é a sua. E se você quer parar de pedalar empurrado pelo banco, vem pro MBV, que é onde eu ensino o dono a enxergar a própria empresa pelos números. O link está na bio.

Fonte: dia 1 (os três prazos, a bicicleta que "na hora que ela parar ela tomba", os três por cento ao mês do capital de giro).

**05/10**, 15 funcionários (versão que ficou depois da conferência, só com o que o Hélio fala):

> 15 funcionários e nada anda sem mim… como tirar férias sem perder a empresa?

> Isso acontece com muito dono, e a culpa não é do seu time. Se nada anda sem você, é porque nunca colocaram no papel o que cada um faz, como faz e até quando. Começa por aí.
>
> Depois, delega e acompanha. Todo dia, no mesmo horário, 15 minutos com o time e três perguntas: o que você fez ontem, o que vai fazer hoje e o que está te travando.
>
> Quando isso virar rotina, a empresa para de depender de você pra tudo.

Fonte: dia 3 (descrição de função com o que, como e quando; "delegai e vigiai"); dia 2 (o rito diário de 15 minutos com as três perguntas). A promessa de férias ficou de fora porque o Hélio não ensina isso.
