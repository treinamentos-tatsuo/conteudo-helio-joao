# 251 — Vender mais não resolve falta de lucro. (flip chart, perfil Tatsuo Academy)

**Perfil:** Tatsuo Academy (não o @helio.tatsuo). Sem /etiqueta (decisão do João em 11/10) e sem Manychat.
**Formato:** frase manuscrita no FLIP CHART (primeira peça desse suporte), na voz da Academy. Frase nº 5 do lote 1 de `conteudo/banco-frases-academy.md`, aprovada pelo João em 16/10.
**Origem:** remodelagem da 57 do Hélio ("Prateleira vazia não verga."). Tese do carrossel 229 (crescer consome caixa).
**Previsto:** domingo, 18/10.

**Frase final (letra comum, 2 linhas por cor, padrão do João para o flip chart):**
- Preto: Vender mais não resolve / falta de lucro.
- Vermelho: Sem margem, crescer só / acelera o prejuízo.

**Base do flip chart:** não existe foto real de flip chart no acervo (só um, minúsculo, no canto do palco em MBV-TATSUOAC-328). A base foi feita por image-edit sobre a foto real do escritório (`vidro-base-mid.png`): o escritório é real e o flip chart foi acrescentado. Prompt em `_scripts/prompt-base-flip.txt`. Quando houver foto real do flip chart, trocar a base.
- Rodada 1 (16/10): `base-flip-v1` e `base-flip-v2` (a v2 tem a bandeja com marcadores, mais real). Escolhida: v2.

**Escrita:** prompt em `_scripts/prompt-flip-v1.txt` (o do papel, adaptado: marcador de ponta chanfrada, letra de aula, 3 linhas por cor porque a folha é estreita; a quebra não muda palavra).
- Rodada 1 (16/10): `flip-v1` (letra mais regular) e `flip-v2` (letra mais solta, mais cara de mão). Grafia e acentos (NÃO, SÓ, PREJUÍZO) conferidos nas duas. Nas duas, "ACELERA" fica perto da borda direita da folha. Recomendada: v2.

**Legenda:** `legenda.txt`.

**Publicação:** prevista para domingo, 18/10.

**Correção do João (16/10): "o modelo de flip chart está errado".** O flip chart certo é o da sala do MBV: cavalete de madeira, sala escura de treinamento, mesas brancas. Ele mandou 3 fotos reais; a dele em branco virou a base (`imagens/base-flip-real.png`; original e referência escrita em `imagens/referencias-joao/`). As v1 e v2 (flip chart gerado no escritório) ficam guardadas.
- Rodada 2 (16/10): prompt em `_scripts/prompt-flip-real-v1.txt` (pede antes para limpar as manchinhas e os rabiscos da dobra de cima). `flip-v3` (letra mais solta) e `flip-v4` (letra mais limpa e legível). Grafia e acentos conferidos nas duas. Corte com `corta.py --zoom 1.2 --top 330` (`flip-v3-zoom.png`, `flip-v4-zoom.png`): o flip chart enche o quadro. Recomendada: v4-zoom.

**Correção do João (16/10): "esse é o modelo de fonte e forma de escrita".** Ele mandou uma referência (`imagens/referencias-joao/modelo-letra-sapo.png`) com letra comum de caneta fina, em minúsculas com maiúscula só no começo da frase, 2 linhas por cor, texto no alto do meio da folha, bastante papel em branco embaixo e a dobra de cima com os rabiscos originais. A caixa alta saiu.
- **Frase no padrão novo:** Preto: Vender mais não resolve / falta de lucro. Vermelho: Sem margem, crescer só / acelera o prejuízo.
- Rodada 3 (16/10): prompt em `_scripts/prompt-flip-real-v2.txt`. Gerou `flip-v5` (vermelho mais vivo) e `flip-v6` (vermelho mais perto do carmim, bloco um pouco mais alto). Conferi grafia e acentos nas duas. Corte padrão, sem zoom, como na referência. Recomendada: v6.

**Final (aprovada pelo João em 16/10): `flip-v5`** ("a segunda opção ficou melhor"; ele preferiu a v5, que tem o vermelho mais vivo, à v6 recomendada). Copiada como `instagram/flip-chart.png`. A legenda foi aprovada junto.
**Entrega:** `~/Desktop/POSTS/FRASE TATSUO ACADEMY/251_vender-mais-sem-margem/`.
