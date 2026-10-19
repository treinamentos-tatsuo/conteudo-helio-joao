# 253 — Preço só é caro pra quem não viu valor. (flip chart, perfil do Hélio)

**Perfil:** @helio.tatsuo. **Formato:** frase manuscrita no flip chart da sala do MBV (padrão do 251: letra comum, preto e a virada em vermelho), na voz do Hélio.
**Origem:** frase do João, "ninguem questiona preço, quando entende valor" (19/10), reescrita pelo Claude em 6 versões; o João escolheu a 2. Lastro: MBV, "como se vende o preço".

**Frase:**
- Preto: Preço só é caro
- Vermelho: pra quem não viu valor. (o "o" antes de valor saiu a pedido do João, 19/10, depois de fechado)

**Imagem:** base `base-flip-real.png` (a foto real do flip chart do MBV, a mesma do 251); prompt em `_scripts/prompt-flip-v1.txt` (o do 251 com as linhas trocadas).
- Rodada 1 (19/10): `flip-v1` (letra menor, vermelho mais fechado) e `flip-v2` (letra maior, vermelho mais vivo, como o João preferiu no 251). Grafia e acentos (ç, só, é, não) conferidos. Indicada: v2.
- Rodada 2 (19/10, João: "preencha melhor o espaço do flip chart"): letra grande, bloco com ~85% da largura da folha, em 4 linhas (Preço só / é caro // pra quem não viu / o valor.; a quebra não muda palavra). Prompt em `_scripts/prompt-flip-v2.txt`. `flip-v3` (respiro entre o preto e o vermelho) e `flip-v4` (vermelho colado no preto, "viu" encostando na borda). Grafia e acentos conferidos. Indicada: v3. As v1 e v2 continuam na pasta.
- Rodada 3 (19/10, João: "ficou muito grande agora, tem que ficar um meio termo da primeira para essa; e dê uma falhada na caneta para ficar mais realista"): caneta meio seca no prompt (tinta falhando dentro do traço, pressão irregular). `flip-v5` (4 linhas, bloco com ~60% da largura; prompt `_scripts/prompt-flip-v3-4linhas.txt`) e `flip-v6` (2 linhas, ~75% da largura, "valor." perto da borda; prompt `_scripts/prompt-flip-v3-2linhas.txt`). Grafia e acentos conferidos. Indicada: v5.
**Final (aprovada pelo João em 19/10): `flip-v5`** ("v5, legenda vai. Pode fechar."). Copiada como `instagram/flip-chart.png`.
**Correção (19/10, João: "tirar o 'o' antes da palavra valor"):** image-edit da própria v5 (`_scripts/prompt-sem-o.txt`), gerou `flip-v7` e `flip-v8`, quase iguais; ficou a **v7** como `instagram/flip-chart.png`. A arte com o "o" foi guardada em `instagram/_rodadas/flip-chart-com-o.png`. O image-edit não sai pixel-idêntico, mas a letra, a tinta e a posição se mantiveram.

**Legenda:** `legenda.txt`, 354 caracteres, CTA pro link da bio.

**Legenda aprovada** sem edição (relida antes de fechar).
**Entrega:** `~/Desktop/POSTS/Frase sem rosto/253_preco-caro-valor/` e `~/Desktop/frases claude/preco-valor/`.

**Publicação:** a definir.
