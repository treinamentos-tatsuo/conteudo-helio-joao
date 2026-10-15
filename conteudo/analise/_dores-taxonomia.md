# Taxonomia de DORES do empresário (PME, fatura R$3 mi a R$100 mi/ano)

Classifique cada post pela DOR PRINCIPAL que o texto toca: o incômodo que o empresário SENTE e reconheceria como dele. Não é o tema técnico nem a solução: é a dor. Se o post fala da solução, pergunte "qual dor essa solução resolve?".

## Lucratividade
- L1 fatura muito e não sobra / o dinheiro nunca vai pro bolso do dono
- L2 não sabe se a empresa lucra / não conhece os números (DRE, margem, custo, precificação no achismo)
- L3 vende e não tem caixa / caixa apertado / capital de giro / prazo de recebimento
- L4 dívida, banco, empréstimo, juros comendo a sobra
- L5 dono não se remunera / pró-labore × dividendo / risco do dono não recompensado / retirada
- L6 preço e margem: dá desconto, vende barato, guerra de preço, cliente só quer preço
- L7 imposto, governo, burocracia, carga tributária sufocando
- L8 gasto/custo/desperdício fora de controle, dinheiro vazando

## Vendas e Crescimento
- V1 vendas imprevisíveis, cada mês é de um jeito, sem meta/funil/processo comercial
- V2 venda depende do dono / time comercial não vende
- V3 perde cliente, cliente some, não fideliza, atendimento ruim
- V4 empresa estagnada, não cresce, bateu no teto
- V5 cresceu e virou bagunça / crescer sem estrutura / medo de crescer e quebrar
- V6 marketing não traz cliente / não sabe gerar demanda

## Cultura e Gente
- C1 funcionário não faz o que eu mando / já expliquei 10 vezes / faz errado
- C2 time sem iniciativa, sem vontade, não pensa como dono, "geração fraca", ninguém quer nada
- C3 não acha gente boa / contrata errado / currículo bonito que não entrega
- C4 gente boa vai embora / rotatividade / troca de funcionário toda hora
- C5 time despreparado porque o dono não treina, não acompanha, não deixa claro
- C6 dono não cobra, tolera, demora pra demitir, quer ser gostado, não tem autoridade
- C7 funcionário tóxico / estrela que performa e destrói o time / fofoca / clima ruim
- C8 sem comprometimento, sem lealdade, ninguém veste a camisa
- C9 liderança/gestor intermediário fraco, não tem líder no meio
- C10 cultura que não pega: reunião que não cobra, regra no papel, valores na parede

## Dono (o peso de ser dono)
- D1 empresa depende do dono / não consegue delegar / tudo passa por ele / não pode sair de férias
- D2 dono sobrecarregado, cansado, sem tempo, sem vida, trabalha demais
- D3 solidão do dono / decide sozinho / ninguém entende / não tem com quem falar
- D4 pressão, peso, medo, ansiedade de liderar (o peso como sentimento)
- D5 decisão errada, arrependimento, medo de quebrar, apostou e tomou porrada
- D6 falta de processo, organização, rotina: vive apagando incêndio
- D7 sócio, família na empresa, sucessão
- D8 empresário visto como vilão / lucro tratado como crime / desvalorização de quem empreende
- D9 comparação com outros, palco × bastidor, sensação de estar atrasado
- D10 dono que sabe e não faz / procrastina / espera a hora certa / zona de conforto
- D11 dono que só executa e não pensa estrategicamente / sem visão / sem conhecimento de gestão (analfabetismo empresarial)

## Sem dor
- X0 não toca dor de empresário: institucional, evento, comunicado, depoimento genérico, motivacional sem incômodo, vida pessoal, homenagem, chamada pra live/evento

## Saída
Para cada post, uma linha TSV: `id<TAB>codigo<TAB>frase_da_dor`
- codigo: o código acima (um só, o principal). Se nenhuma serve de verdade, use `OUTRA`.
- frase_da_dor: até 15 palavras, na VOZ DO EMPRESÁRIO em 1ª pessoa, como ele diria num café (ex.: "faturo muito e não vejo a cor do dinheiro"). Para X0, escreva `-`.
