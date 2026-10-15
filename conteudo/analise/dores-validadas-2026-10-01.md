# Dores do ICP validadas por desempenho (01/10/2026)

## Como foi feito
- **Base:** `desempenho.json` (pull de 30/09 20:05). Entraram 2.053 posts de jan/2025 a 23/09/2026, só os com 7 dias ou mais de publicados: 1.334 reels, 514 carrosséis e 205 imagens.
- **Classificação:** cada post recebeu uma dor principal da taxonomia em `_dores-taxonomia.md`. Foram 37 códigos. Quem classificou foi um agente lendo a legenda, nos primeiros 500 a 700 caracteres. O rótulo de cada post está em `_dores-rotuladas-2026-10-01.json`.
- **Métrica de desempenho:** percentil do post dentro do mesmo **formato e trimestre**, o que neutraliza o crescimento do perfil e a diferença entre reel e carrossel. Usei três percentis: alcance, compartilhamentos e comentários. A nota de cada post é a média dos três, e 0,50 é a mediana.
- **Teste:** Mann-Whitney de cada dor contra o resto da base, com correção de Benjamini-Hochberg para os 37 testes (o valor q).
- **Robustez:** o campo de palavra-chave do Manychat (`cta_keyword_count`) está vazio na base inteira. Por isso os comentários incluem a palavra-chave. Refiz a conta só com alcance e compartilhamentos, e o ranking não mudou.

## Validadas (acima da mediana com significância)
| Dor (voz do dono) | Código | n | Nota mediana | % acima da mediana | q |
|---|---|---|---|---|---|
| Já expliquei mil vezes e continua errado | C1 | 19 | 0,75 | 74% | 0,03 |
| Contrato gente boa, não preparo nem acompanho, e vivo trocando | C5 | 73 | 0,69 | 63% (40% no top 20) | <0,001 |
| Todo mundo na empresa tem caminho pra ser pago, menos eu (risco sem dividendo) | L5 | 45 | 0,67 | 67% | 0,01 |
| Tenho exatamente o time que eu tolero (não cobro, demoro pra demitir, quero ser gostado) | C6 | 36 | 0,66 | 75% | 0,02 |
| Não acho gente boa / régua baixa atrai gente fraca | C3 | 37 | 0,61 | 70% | 0,04 |
| Trabalho sem parar e a vida passa sem eu estar presente | D2 | 33 | 0,60 | 70% | 0,02 |
| Funcionário sem vontade, não pensa como dono, júnior cobrado como sênior | C2 | 47 | 0,60 | 66% | 0,04 |
| O peso e a pressão de decidir, sustentar e liderar | D4 | 87 | 0,58 | 60% | 0,03 |

## Promissoras (efeito forte, amostra pequena: testar mais)
- **C7: o funcionário tóxico** que entrega resultado e contamina o time, a rádio-peão, o vendedor estrela. n=7, 86% acima da mediana.
- **D3: a solidão do dono.** Na queda, só o nome dele está lá; ele não divide o problema com ninguém. Em 2026 a nota foi 0,72, com n=8.
- **D8: o empresário tratado como vilão,** com o lucro visto como crime. n=8, 38% dos posts no top 20, com o maior post de comentários da base (Casas Bahia/PME).
- **C9: falta líder no meio.** Nota 0,66 só com alcance e compartilhamentos, n=15.

## NÃO validadas como categoria (na mediana ou abaixo dela)
| Dor | Código | n | Nota mediana | 2025 → 2026 |
|---|---|---|---|---|
| Faturo muito e não sobra | L1 | 70 | 0,43 | 0,56 → 0,37 |
| Vendas imprevisíveis | V1 | 82 | 0,42 | 0,49 → 0,34 |
| Não sei se a empresa lucra (DRE, margem) | L2 | 128 | 0,41 | 0,51 → 0,40 |
| A empresa depende de mim, não consigo delegar | D1 | 62 | 0,46 | estável |
| Vivo apagando incêndio | D6 | 50 | 0,43 | 0,45 → 0,33 |
| Marketing não traz cliente | V6 | 60 | 0,32 | abaixo, com q=0,001 |

L1 e V1 têm hits isolados, mas como categoria ficam abaixo da mediana e caíram em 2026. Uma hipótese é saturação: 49 posts de L1 só em 2026. Outra é a validação delas ter vindo de lead/conversão e não de alcance. Esta análise **não mede lead**.

## Limitações
- A classificação lê só a legenda. No reel, a fala do vídeo pode tocar outra dor.
- Cada post tem uma dor só, e posts que misturam duas foram para a principal.
- "Validada" aqui quer dizer que a dor alcança e espalha. Conversão em MQL é outra medida, e para ela o caminho é cruzar com o `leads.json`.

## Nervos do top 10% (complemento, 01/10)
- **Corte:** top 10% de cada formato e trimestre (nota ≥ 0,90). São 169 posts; 129 deles tocam dor.
- **Agrupamento:** feito pelo Claude a partir da frase da dor de cada post. A contagem é aproximada, porque o agrupamento é manual.
- Os nervos de maior alcance são três: pressão como preço do jogo; não preparo e culpo o funcionário; espero de júnior atitude de dono.
- Ponto comum: o nervo que performa devolve a culpa ao dono ou consagra o peso que ele carrega. Reclamação pura contra o funcionário quase não aparece no topo.
