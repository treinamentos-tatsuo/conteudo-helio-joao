# Post 74 — Trabalhou de graça (arte da live)

**Formato:** frase única (skill `/frase`) + faixa de convite no rodapé.
**Publicação:** 31/08/2026, ~17h30 (live às 19h). Segundo post do dia; o carrossel 73 saiu às 13h.
**Palavra-chave:** LIVE (mesma do 73; automação por post específico separa os dois no UTM).

## Por que esta peça existe

O carrossel das 13h faz o trabalho de conteúdo e captura. Esta é a **chamada de última hora**: quem viu o carrossel de manhã e esqueceu, e quem só abre o Instagram no fim da tarde. Por isso ela não repete o argumento do carrossel — entrega a dor em uma frase e o convite em uma linha.

## Diferenciação do 73

O carrossel trata do **fechamento sem cálculo** (o dono decreta "mês ruim" sem ter comparado nada). Esta peça vai na consequência mais crua e pessoal: o trabalho do mês inteiro que não virou dinheiro no bolso do dono. Sem sobreposição de formulação.

## A frase

Tem dono que trabalha o mês inteiro
pra descobrir no dia 31 que foi de graça.

## Convite (bloco central)

**Hoje, 19h** (Anton, carmim, 96px)
Aula ao vivo e gratuita para donos de empresa (serif negrito, 30px)

> **Decisão do user (31/08):** a 1ª versão trazia o convite discreto (serif 27px entre duas regras finas) e ficou "misteriosa" demais. Para peça de última hora o convite tem que ser lido em um segundo — a informação passou a Anton grande em carmim. O layout discreto foi arquivado em `instagram/_slide-01-versaoA-descartada.html` e serve para peça de conteúdo puro, sem convite.

## Imagem — cena de dois (decisão final do user, 31/08)

Percurso registrado, porque as duas voltas ensinaram algo:

1. **Homem sozinho na mesa (gerado)** — atmosfera certa, mas o user leu como "dono triste" e pediu o Hélio.
2. **Foto real do Hélio tratada em P&B** — fiel e firme, mas *"quebrou muito"*: retrato de estúdio em fundo de escritório não convive com o sistema de névoa e granulado do resto. Arquivada em `_scripts/_descartadas/slide-01-foto-real-helio.png`.
3. **Cena de dois, gerada** — o user pediu pra voltar à composição original com o Hélio dentro dela, interagindo com o personagem. É a versão final.

**O que a volta ensinou:** o problema nunca foi "genérico × real". Era que a peça precisava de uma CENA, não de um retrato. O homem sozinho não tinha com quem interagir, e a foto real trouxe uma pessoa sem trazer uma cena. Com dois personagens, a imagem passa a contar o convite: o dono parado diante dos papéis e o mais velho apontando o número que ele não estava vendo.

**COMO A SEMELHANÇA FOI RESOLVIDA (método novo, reaproveitável):** a cena gerada saiu com um asiático-brasileiro genérico de cabelo grisalho — nada parecido com o Hélio. O que resolveu foi **image-edit com DUAS `input_image`**: [1] a cena aprovada e [2] um recorte do rosto real dele, com prompt mandando reproduzir a primeira imagem exatamente e trocar SÓ a cabeça do homem mais velho pela da segunda, renderizada no mesmo P&B granulado. Resultado em `img-04.png`: cena idêntica, rosto reconhecível (cabelo escuro com risca lateral, formato do rosto, o sorriso dele).
Isto **contraria a regra "gerar OU banco, nunca misturar"** do motor-imagem — e de propósito: aquela regra existe pra evitar colagem indesejada, e aqui a colagem É o objetivo. Mesma lógica já registrada em 2026-08-11 pra corrigir anomalia ("o gotcha vira vantagem"). Custo: 192s em quality high, contra ~30s de um text-to-image.

**Três passes de image-edit até chegar na versão final** (cada um partindo do resultado do anterior, cena preservada):
1. `img-02` → `img-04`: troca do rosto genérico pelo do Hélio (2 refs: cena + rosto).
2. `img-04` → `img-06`: correção de IDADE — o rosto tinha saído jovem demais (3 refs: cena + 2 ângulos do rosto).
3. `img-06` → `img-07`: **expressão SÉRIA e mais idade** (pedido do user). Sorriso removido, boca em linha reta, sobrancelha baixa, olhar duro nos papéis, rosto mais pesado.

**Por que o passe 3 melhorou a peça, não só a semelhança:** o sorriso amaciava uma frase que é confronto ("trabalhou o mês inteiro pra descobrir no dia 31 que foi de graça"). Com o rosto sério, a imagem passa a concordar com o texto em vez de contradizê-lo. Vale como regra de direção: em peça de confronto, o personagem que ensina não sorri.

4. `img-07` reprovada: **três edits empilhados descolaram a cabeça do corpo**. Cada passe regenera a imagem inteira, e o erro de composição acumula. O user leu como "cabeça colada".

**SOLUÇÃO FINAL — tirar o rosto de cena (`img-08`).** Close das duas mãos sobre a planilha manuscrita: a do dono parada e aberta, sem fazer nada; a do mais velho, marcada pelo tempo, com o indicador firme sobre um número. Sem rosto, sem semelhança pra defender, sem colagem possível.

**Regra que sai daí (vale além desta peça):** quando a peça precisa de uma pessoa específica e não existe foto dela em situação, **enquadrar o gesto, não o rosto**. O gesto carrega a tese e é imune ao problema de identidade. Aqui ficou até melhor que a cena original: a mão jovem parada ao lado da mão velha apontando o número É o carrossel inteiro em uma imagem.
**Teto de edits:** no máximo 2 passes de image-edit sobre a mesma imagem. No terceiro a cena começa a desmontar.

**Imagens:** `img-08.png` (FINAL) · `img-09.png` (variante só com uma mão) · `img-07/06/04/02` (percurso, em `_scripts/_descartadas/`) · `img-02.png` (a mesma cena antes do edit — ele sentado na quina da mesa apontando o número no papel, o dono ouvindo) · `img-01.png` (alternativa — ele em pé, gesto aberto, cena mais espaçada) · `img-03.png` (avulsa, pedida pelo user: o mesmo homem limpando peixe no mesmo cenário; não usada nesta peça).

**Nota honesta sobre semelhança:** o image-edit entrega SEMELHANÇA, não identidade. Lê como ele, não é uma foto dele. Para peça que precise ser inequivocamente o Hélio, o caminho é foto produzida.

## Legenda (post)

Faltam poucas horas.

Hoje, 19h, uma aula gratuita de uma hora para quem é dono de pequena e média empresa. Um mini MBV.

Eu vou mostrar as três coisas que decidem se o seu mês valeu alguma coisa.

A primeira é o lucro. Empresa pequena foi feita para colocar dinheiro no bolso do dono, e a prioridade é o saque de dividendo. Existe uma lógica para isso acontecer, e ela não é sorte.

A segunda é o crescimento. E eu não chamo de venda, porque faturamento é métrica de vaidade. Crescer é vender com qualidade, e vender com qualidade é vender sustentando esse saque.

A terceira é a cultura. Em algum momento a empresa esbarra na limitação do dono, e aí ou você aprende a fazer resultado através de outras pessoas, ou vira aquele empresário reclamão que diz que ninguém quer nada com nada.

Comenta LIVE aqui embaixo que eu te mando o link no seu Direct.

Seja Bem-Vindo ao Fim do Analfabetismo Empresarial.
