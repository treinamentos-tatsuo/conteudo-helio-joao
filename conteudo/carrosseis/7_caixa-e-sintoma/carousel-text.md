# Carrossel 7 — Caixa é sintoma, nunca é a causa

**Modelo:** editorial-punch · **Tema:** o empresário trata falta de caixa como se fosse a doença, e por isso trata sempre a coisa errada. Toma empréstimo pra tapar capital de giro sem saber de onde o dinheiro está vazando. O caixa não é a causa: é o lugar onde a operação mal feita aparece.

**Espinha:** sintoma × causa. A tensão não é "faturamento não é riqueza" (isso é o carrossel 2). Aqui a tensão é de **diagnóstico**: o dono olha o extrato e acha que descobriu o problema. O extrato só dá a temperatura, nunca o lugar da infecção. Enquanto ele trata o sintoma com dívida, a causa continua comendo por dentro — e a empresa não quebra de repente, quebra em parcelas.

> **Fonte:** transcrição de vídeo de terceiro (input do user, 2026-07-24). Aproveitado: 9 milhões de empresas inadimplentes, confusão faturamento × caixa, capital de giro tratado como dinheiro do dono, Casas Bahia, o descasamento (vende em 12x, paga em 60 dias), empréstimo pra cobrir giro como roleta russa, "caixa é sintoma, a causa está na operação".
>
> **Checagem dos números (obrigatória — a transcrição tem dois erros):**
> - **9 milhões de CNPJs negativados** — CONFIRMADO. Serasa Experian: 8,9 milhões em março, 9 milhões em abril de 2026, alta de 1,5 milhão em 12 meses. Usado no slide 2 com o delta de 1 ano, que é mais forte que o número seco.
> - **"1 em cada 3 CNPJs"** — NÃO usado. Não achei a base do denominador; com ~22 milhões de empresas ativas a proporção seria maior que 1/3, e afirmação factual sem fonte não entra (regra da voz).
> - **"Casa Bahia faturou 30 milhões em 2024"** — ERRADO na fonte. A receita líquida do Grupo Casas Bahia em 2024 foi de **R$ 27,2 bilhões** (queda de 5,7% sobre 2023). Corrigido no slide 9.
> - **"1 bilhão de prejuízo no primeiro trimestre"** — o número existe, mas **não é de 2024**. No 1T24 o prejuízo foi de R$ 261 milhões. O prejuízo de **R$ 1,064 bilhão** é do **1º trimestre de 2026** (receita líquida de R$ 7,4 bi no tri). O slide 9 usa os dois com o ano certo — e a distância entre eles ("faturou 27 bi em 2024, perdeu 1 bi num trimestre de 2026") entrega o ponto melhor do que a versão errada entregava.
>
> **Tratamento:** a transcrição é uma lista de dores soltas. Nada entra cru (regra 2026-07-20). Capital de giro vira "o dinheiro que entrou já tem dono"; o descasamento de prazo vira "você virou o banco do seu cliente"; empréstimo vira "você comprou tempo e pagou juro por ele"; "o lucro fica perdido em algum lugar" vira a causa concreta (preço não calculado, custo não medido). CMV/CSV não aparecem por sigla — viram "o custo de cada venda que você faz", que é como o dono de PME fala.
>
> **MBV:** não citado por nome nem em pilares. A ponte de método entra no slide 16 (custo por venda, preço que sustenta, prazo que o caixa aguenta) e o resto carrega no CTA. Tema é Lucratividade puro, mas nomear pilar aqui esfria — o slide já é o método.
>
> **Interlocutor:** dono de pequena e média empresa. Nada de tesouraria, hedge, capital structure, valuation. A Casas Bahia entra como prova de que volume não protege, não como espelho.
>
> **Regras permanentes aplicadas:** Source Serif Pro padrão 44px · todo serif vermelho vai em negrito · máx ~2 recursos de ênfase por slide, sem repetir recurso nem cor no mesmo slide · gancho no slide 1 · rodapé em `bottom:~200-210px` · Anton casa a margem da linha de referência (ou preenche a coluna quando é a linha mais larga) · imagem quadrada sangrando no rodapé, metade de cima pálida · seta só com alvo visível.
>
> **Ajustes feitos depois do 1º render (2026-07-24):**
> 1. **Capa** desceu de `top:330px` pra `440px` — o aparelho de eletrocardiograma é baixo no quadro e sobrava um vão morto entre o texto e a máquina.
> 2. **Anton em 2 linhas** nos slides 7 e 15 (a frase de uma linha só dava 77-83px, menor que o esperado pra um grito). Depois o alvo do autofit teve que **descer** (840px no 7, 760px no 15) porque o bloco cheio caía em cima do frasco de soro e do monitor. Aprendizado registrado no log: em foto sangrada o teto do bloco é a linha do sujeito, não os 930px de coluna.
> 3. **Cortar o topo da imagem NÃO desce o sujeito** — a foto é ancorada no rodapé com escala fixa, então `EXTRA_TOP` só encurta o quadro. Quem cede é o bloco de texto. Usado só no slide 6, pra matar a emenda de topo (junto com `fade:32%`).
> 4. **Elipse do slide 3** com geometria reduzida (`1.50em` / `-0.22em`) — a padrão (`1.78em`) atravessava a linha de cima.
> 5. **Figura solta do CTA (17)** cortada na cintura (`KEEP_TOP 0.60`) — de corpo inteiro ela saía com ~240px de largura e sumia no slide.
> 6. **Slide 2** (ajuste do user): a segunda estrofe foi pra vermelho negrito.
> 7. **Slide 10** (ajuste do user): o braço do foco cirúrgico atravessava a faixa de texto. Topo da foto cortado em 230px (`EXTRA_TOP`) e fade pra 26% — a foto começa abaixo do bloco, o texto voltou a ficar limpo.
> 8. **Desaturação obrigatória no pós** (`convert("L")`) — a imagem 9 voltou com uma mancha azulada mesmo com o prompt pedindo P&B.

**Universo de imagem:** **diagnóstico clínico vintage.** P&B documental, anos 50-60, hospital e consultório antigos. O universo é autorizado pela própria fala do Hélio ("caixa é sintoma") e resolve o carrossel inteiro: o que se mede, o que se vê e o que está por baixo. Motivos: fita de eletrocardiograma saindo do aparelho, sala de espera lotada, homem de terno sentado na maca, frasco de comprimidos derramado, estetoscópio sobre o prontuário, bolsa de transfusão pendurada, frasco de soro quase vazio, relógio de enfermaria, ala hospitalar imensa e vazia, sala de cirurgia vista de cima, termômetro de mercúrio, negatoscópio com a chapa iluminada, seringa e ampola, atadura manchada, monitor com o traçado enfraquecendo, microscópio na bancada, homem olhando a radiografia contra a janela.

**Figura humana em 3 slides só** (3, 10, 17). O resto conta por instrumento, sala e objeto.

---

## Contexto de imagem de cada slide (guia — refinar na fase de imagem)

1. **Capa / gancho** — fita de eletrocardiograma saindo de um aparelho antigo, traçado irregular, o papel dobrando e caindo. O sintoma que denuncia. Foto, sangra.
2. **9 milhões** — sala de espera de hospital antigo, fileiras longas de cadeiras ocupadas, gente até o fundo do corredor. Foto, sangra.
3. **Quebraram vendendo** — homem de terno bem posto sentado na beira da maca do consultório, ombros caídos. Parecia saudável. Foto, sangra.
4. **A Selic** — frasco de comprimidos tombado na bancada, cápsulas derramadas. A explicação pronta que todo mundo engole. Still-life, sangra.
5. **O diagnóstico** — estetoscópio pousado em cima de um prontuário aberto, caneta ao lado. Still-life, sangra.
6. **O dinheiro já tem dono** — bolsa de transfusão pendurada no suporte, tubo descendo. O sangue passa pelo braço, não é dele. Foto, sangra.
7. **Gasta o que não é seu (Anton)** — frasco de soro de vidro invertido, quase vazio, última gota. Still-life, sangra.
8. **12 vezes × 60 dias** — relógio grande de parede de enfermaria, ponteiros marcados, parede descascada. Foto, sangra.
9. **Casas Bahia** — ala hospitalar colossal, macas enfileiradas até o fundo, ninguém. Grande porte, nenhuma proteção. Foto, sangra.
10. **A conta não fechou dentro** — sala de cirurgia vista de cima, equipe debruçada sobre a mesa, foco de luz. Foto, sangra.
11. **CAIXA É SINTOMA (herói)** — termômetro clínico de mercúrio em close, a coluna subindo, sobre pano claro. Figura solta / still-life no miolo.
12. **Onde é a infecção** — negatoscópio com a chapa de raio-x iluminada, um dedo apontando uma mancha. Foto, sangra.
13. **O empréstimo** — seringa e ampola sobre a bandeja de metal. Alivia a dor, não cura. Still-life, sangra.
14. **O furo continua** — atadura enrolada, mancha escura vazando por baixo de um curativo novo. Close, sangra.
15. **Não quebra de repente (Anton)** — monitor/osciloscópio antigo com o traçado achatando na tela. Foto, sangra.
16. **Gestão / método** — microscópio antigo na bancada, lâminas e caderno de anotação ao lado, luz de janela. Foto, sangra.
17. **Fechamento + CTA** — homem de pé segurando a radiografia contra a janela, luz forte atravessando a chapa. Ele está enxergando. Recorte, miolo.

---

## Legenda (post)

Tem uma frase que eu escuto quase toda semana de dono de empresa: "Hélio, meu problema é caixa."

Ele chega com o extrato na mão, a planilha aberta, a conta do mês que não fechou de novo. Fala do banco, fala do juro, fala do cliente que atrasou.

E termina sempre no mesmo lugar: "está difícil, a Selic está impossível."

Mas será que o caixa é o problema?

Eu acredito que não.

Caixa é sintoma. Nunca é causa. O extrato da sua empresa é um termômetro: ele te diz que tem febre, ele não te diz onde é a infecção.

E o empresário brasileiro trata a febre a vida inteira. Toma empréstimo pra cobrir capital de giro sem saber de onde o dinheiro está vazando. Alivia a dor, não cura nada, e ainda paga juro pelo alívio.

Sabe qual é a raiz disso? Uma confusão que quase ninguém teve coragem de te explicar.

Ele confunde faturamento com caixa. E confunde capital de giro com o dinheiro dele.

O dinheiro que entrou hoje na sua conta já tem dono. Uma parte é do fornecedor, uma parte é do imposto, uma parte é da folha do dia dez. Você não está com dinheiro em caixa, você está segurando o dinheiro dos outros por alguns dias.

Só que ele olha o saldo e enxerga lucro. Compra, contrata, aumenta o próprio pró-labore. E gasta o que ainda não era dele.

Some a isso o descasamento que virou hábito no Brasil: você recebe do cliente em doze vezes e paga o fornecedor em sessenta dias. Paga no curto, recebe no longo. Isso não é um detalhe operacional, é uma decisão de financiamento que você tomou sem perceber que estava tomando.

É a operação que define o preço que você cobra. É a operação que define o custo de cada venda que você faz. É a operação que define o prazo que o seu caixa consegue bancar.

Preço errado vira prejuízo com nota fiscal.

Custo que ninguém mede vira lucro que some sem explicação.

E prazo que o caixa não aguenta vira dívida que você chama de "problema de mercado".

Por isso eu digo que o papel do dono não é ficar administrando o saldo do dia. É entender o modelo econômico da própria empresa, saber onde ele está pisando, e conhecer o custo do que ele vende antes de vender.

Porque empresa nenhuma quebra de repente. Ela quebra em parcelas, enquanto o dono olha pro lugar errado.

Comenta 307 que eu te mostro como enxergar onde o lucro da sua empresa está ficando preso, em vez de tapar buraco com dívida todo mês.

Seja Bem-Vindo ao Fim do Analfabetismo Empresarial.

#gestao #empreendedorismo #fluxodecaixa #lucratividade #TatsuoAcademy

---

## Texto que renderiza em cada slide

> **17 slides.** Tamanho padrão Source Serif Pro = 44px; só desvia pra casar com Anton ou pra respeitar margem.
>
> **Layouts:** *Herói* (linha única centrada + remate): 11, 15. *Duas linhas* (estrofe única): 3, 5. *Dois blocos no topo*: 2, 4, 6, 8, 9, 10, 12, 13, 14, 16. *Split com "..."*: 2 → 3. *Sanduíche*: 17.
>
> **Capa:** setup menor em cima, impacto maior embaixo. A linha de impacto tem 24 caracteres, cabe folgado em uma linha só.

| # | Beat | Recurso de ênfase |
|---|---|---|
| 1 | Capa / gancho | vermelho |
| 2 | O dado (9 milhões) + split | vermelho negrito na 2ª estrofe |
| 3 | Quebraram vendendo | elipse |
| 4 | A desculpa (Selic) | vermelho |
| 5 | O diagnóstico | vermelho |
| 6 | O dinheiro já tem dono | vermelho |
| 7 | Gasta o que não é seu | Anton vermelho |
| 8 | 12 vezes × 60 dias | estrofe inteira em vermelho |
| 9 | Casas Bahia (prova) | vermelho |
| 10 | A conta não fechou dentro | grifo |
| 11 | CAIXA É SINTOMA (herói) | Anton vermelho |
| 12 | Onde é a infecção | vermelho |
| 13 | O empréstimo | vermelho |
| 14 | O furo continua | grifo |
| 15 | Não quebra de repente (herói) | Anton vermelho |
| 16 | Gestão / método | grifo |
| 17 | Fechamento + CTA | grifo + CTA "Comenta 307," |

### Slide 1 — Capa / gancho
**Setup (menor, em cima):** Você não tem problema de caixa.
**Impacto (maior, embaixo):** O caixa <red>só te entregou</red>.

### Slide 2 — O dado
9 milhões de CNPJs negativados no Brasil.
1,5 milhão a mais do que um ano atrás.

<red>E quase nenhum deles quebrou...</red>

### Slide 3 — Quebraram vendendo
...por falta de venda.
Quebraram <elipse>vendendo</elipse>.

### Slide 4 — A desculpa
Aí você me diz que o problema é a Selic.
Que o juro está impossível.

Eu não vou discordar do juro.
<red>Vou discordar do diagnóstico.</red>

### Slide 5 — O diagnóstico
Juro caro não cria o seu problema.
<red>Ele só cobra mais caro por ele.</red>

### Slide 6 — O dinheiro já tem dono
O dinheiro que entrou hoje já tem dono.
Fornecedor, imposto, folha.

Você não está com dinheiro em caixa.
<red>Você está com o dinheiro dos outros.</red>

### Slide 7 — Gasta o que não é seu
Só que você olha o saldo e vê lucro.

<anton-red>E GASTA O QUE AINDA NÃO É SEU.</anton-red>

### Slide 8 — 12 vezes × 60 dias
Você recebe do cliente em 12 vezes
e paga o fornecedor em 60 dias.

<red>Virou o banco do seu cliente.</red>
<red>Sem cobrar nada por isso.</red>

### Slide 9 — Casas Bahia (prova)
A Casas Bahia faturou 27 bilhões em 2024.

No primeiro trimestre de 2026,
<red>perdeu 1 bilhão.</red>

### Slide 10 — A conta não fechou dentro
Não faltou cliente.
Não faltou venda.

A conta não fechou
<grifo>dentro da própria operação.</grifo>

### Slide 11 — Herói
<anton-red>CAIXA É SINTOMA.</anton-red>
Nunca é a causa.

### Slide 12 — Onde é a infecção
O extrato te dá a temperatura.
Não te dá o lugar da infecção.

Ela está no preço que você não calculou
<red>e no custo que você nunca mediu.</red>

### Slide 13 — O empréstimo
Aí você toma empréstimo pra tapar o giro
e dorme achando que resolveu.

Você não resolveu nada.
<red>Comprou tempo e pagou juro por ele.</red>

### Slide 14 — O furo continua
O furo continua lá, comendo por dentro.
E agora a dívida cresce em cima dele.

Você trocou um problema de operação
<grifo>por um problema de dívida.</grifo>

### Slide 15 — Herói
<anton-red>NINGUÉM QUEBRA DE REPENTE.</anton-red>
A empresa quebra em parcelas.

### Slide 16 — Gestão / método
Gestão não é olhar o saldo no fim do dia.
É saber o custo de cada venda que você faz.

O preço que sustenta a empresa
<grifo>e o prazo que o seu caixa aguenta.</grifo>

### Slide 17 — Fechamento + CTA
Pare de tratar o sintoma.
<grifo>Vá atrás da causa.</grifo>

**CTA (grande):** Comenta <red>307</red>,
**Ponte (menor):** que eu te mostro onde o seu lucro está ficando preso.
