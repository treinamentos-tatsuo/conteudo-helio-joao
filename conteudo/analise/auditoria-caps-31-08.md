# Auditoria dos caps de previsão — 31/08/2026

> Pedida pelo user depois que o cap da fábula foi aposentado. Método: recalcular cada classe na
> métrica-alvo VIGENTE (carrossel = interações/1k; frase = shares/1k), não na métrica em que o cap
> nasceu. Régua do dia: carrossel abaixo <42,49 · acima >76,93 · frase abaixo <6,35 · acima >8,95.
> Teste de significância por permutação (20 mil embaralhamentos, unilateral) — `scipy` não está
> instalado nesta máquina.

## Placar da auditoria

| cap | veredito | efeito | p |
|---|---|---|---|
| Lucratividade → capar em `mediana` | **SUSTENTADO** | −20,1 na mediana | 0,0003 |
| frase nichada a empresário → `abaixo` | **NÃO SUSTENTADO** | −2,35 | 0,17 |
| frase com espelho de advertência → `mediana` pra baixo | **SUSTENTADO COM FORÇA** | −3,79 | <0,0001 |

---

## Cap 1 — Lucratividade: fica

**Corpus grande** (469 carrosséis com taxa; pilar inferido por palavra-chave dominante — exige ≥3 acertos e o dobro do 2º colocado; 240 ficaram sem dominância e fora da conta):

| pilar | n | mediana | % acima | % abaixo |
|---|---|---|---|---|
| Cultura | 136 | **75,7** | 48,5% | 16,2% |
| Crescimento | 17 | 59,5 | 47,1% | 17,6% |
| **Lucratividade** | 76 | **55,5** | **25,0%** | **35,5%** |
| (todos) | 469 | 61,6 | 32,0% | 28,4% |

Diferença de medianas Lucratividade × resto classificado: **−20,1 · p=0,0003**.

**Fichas classificadas à mão** (n pequeno, mas é o dado limpo): Lucratividade carrossel n=5 — mediana **52,8**, máximo 65,3, **nenhuma acima do corte**. Cultura carrossel n=8 — mediana 69,3, duas acima.

**Ressalva honesta:** 25% dos posts de Lucratividade PASSAM do corte (contra 32% da base). O cap é duro num efeito que é real mas parcial — ele custa 1 acerto de `acima` a cada 4 posts do pilar. Dado o viés de otimismo documentado (7 erros pra cima contra 1 pra baixo), o custo é aceitável. **Manter.**

---

## Cap 2 — frase nichada a empresário: cai

n=5 nichadas contra 43 universais, na janela de 90 dias.

| classe | n | mediana | % acima | % abaixo |
|---|---|---|---|---|
| nichada a empresário | 5 | 6,01 | **40,0%** | 60,0% |
| universal | 43 | 8,36 | 34,9% | 30,2% |

**p=0,17 — não significativo.** E o sentido do "% acima" é o contrário do que o cap afirma: as nichadas passam do corte com frequência *maior* que as universais.

As cinco, uma a uma:

| frase | shares/1k |
|---|---|
| "Ser dono é ser solitário." | **12,94** |
| "Ninguém respeita uma regra que o próprio líder escolhe ignorar." | **10,18** |
| "…empresário aguenta cansaço." | 6,01 |
| "A vida não avisa quando um instante comum vira saudade." (falso positivo do classificador) | 4,26 |
| "Toda omissão ensina alguma coisa." | 1,82 |

**A leitura que explica melhor os dados:** as duas que ganharam são de **virtude/identidade** — quem compartilha "Ser dono é ser solitário" está se declarando dono. As duas que perderam são **advertência**. Ou seja, o que separa não parece ser o nicho: é o espelho (cap 3). O nicho provavelmente é variável espúria correlacionada com ele.

**Proposta: rebaixar de cap a hipótese.** Com n=5 e p=0,17 não há base pra proibir `abaixo`… nem pra proibir `acima`. Uma frase nichada com espelho de virtude deve poder disputar `acima` normalmente.

---

## Cap 3 — espelho de advertência: fica, e é o mais forte de todos

| classe | n | mediana | % acima | % abaixo |
|---|---|---|---|---|
| **advertência / cobrança** | 18 | **5,26** | **0,0%** | **83,3%** |
| virtude / lei neutra | 28 | **9,05** | **57,1%** | 3,6% |

Diferença **−3,79 · p<0,0001**. **Nenhuma das 18 advertências passou do corte.** Dezesseis das 28 de virtude passaram.

Fundo da lista (advertência): "perdas que a nossa omissão permite" 0,90 · "saco vazio não para em pé" 1,16 · "toda omissão ensina alguma coisa" 1,82 · "a vida adulta começa quando a vontade deixa de ser o centro" 3,38.
Topo (virtude): "o peso não se distribui por justiça" 13,68 · "o vento não cria nada" 13,38 · "ser dono é ser solitário" 12,94 · "não existe profundidade sem pressão" 11,74.

**O mecanismo é comportamental e coerente:** compartilhar é um ato público. Quem compartilha uma frase de virtude está dizendo algo sobre si ("eu aguento", "eu ando"). Quem compartilha uma advertência está repassando uma cobrança — não ganha nada em imagem, e ainda arrisca parecer que está cutucando alguém. O share é o único formato onde o custo social do texto pesa mais que a concordância com ele.

**Limitação séria e declarada:** a classificação advertência × virtude foi feita por **um avaliador só (Claude), e depois de ver as taxas** — há risco real de ordenar pelo resultado. Dois fatos atenuam, mas não anulam: (1) a regra do espelho **já estava escrita na skill antes desta medição**, com o mecanismo nomeado — a hipótese é pré-registrada, só a rotulagem é posterior; (2) a classificação não é limpa por resultado — há advertências em 7,44/7,34/7,10 e virtudes em 6,01/8,29/8,32. **A validação correta é uma reclassificação cega**, de preferência por outra pessoa, antes de tratar o tamanho do efeito como firme.

---

## O achado que vale mais que os três

**Cap medido numa métrica não sobrevive à troca de métrica — e cap sem mecanismo não sobrevive a nada.**

Os dois caps que ficaram de pé têm **mecanismo comportamental nomeado**: o de Lucratividade (tema técnico não gera auto-reconhecimento; o público sente a falta de dinheiro e ignora a causa) e o do espelho (compartilhar é ato público). O que caiu — "frase nichada" — era **descritivo**: uma correlação observada sem explicação de por que existiria. Foi exatamente o que não se sustentou, junto com a fábula, que também era descritivo ("teto de alcance baixo").

**Regra proposta pra criar cap daqui pra frente:** só vira cap o que tiver (1) mecanismo comportamental explícito, (2) medição na métrica-alvo vigente e (3) n≥15 na classe. O resto entra como hipótese no `hipoteses.md` e espera dado.
