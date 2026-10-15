# Elementos visuais (traços à mão carmim)

Biblioteca de elementos gráficos desenhados à mão (grafite carmim `#A91C20`), PNG com fundo transparente, recortados na caixa real do traço. Enviados pelo Rodrigo/marketing (16-07-2026). São os **traços oficiais** — usar estes PNGs sobrepostos no HTML, nunca redesenhar em SVG.

> Vivem aqui no `_banco-referencias/` (sincronizado via Google Drive, fora do Git), como as demais imagens.

## Como usar no slide

Sobrepor via `<img>` posicionado em cima do texto (a peça é HTML → PNG via Playwright). Ex. grifo sob uma frase:

```html
<span class="scribble-wrap">Abre pra ganhar dinheiro.<img class="under-img"
  src="../../_banco-referencias/elementos/sublinhado-rabisco.png" alt=""></span>
```
```css
.scribble-wrap{ position:relative; display:inline-block; }
.scribble-wrap .under-img{ position:absolute; left:-3%; width:106%; height:0.58em; bottom:-0.30em; }
```

Sublinhados esticam na largura sem problema. Elipses/círculos: casar com a caixa do texto que envolvem. Setas: posicionar apontando pro elemento que destacam.

## Critério de uso (regra de ouro)

Os elementos existem pra **quebrar a monotonia**, não pra enfeitar. **Máximo ~2 por composição**, cada um com função, **sem repetir o mesmo recurso** (nem a mesma cor de ênfase) no slide:
- **Anton caixa alta** → frase que é um **grito**/tapa. (fonte, não elemento)
- **Grifo/sublinhado** → ênfase mais calma; usar quando já tem Anton e/ou já tem vermelho no slide.
- **Círculo/elipse** → encapsular uma palavra/linha-chave.
- **Seta** → direcionar o olho pra um ponto (ver imagem 3 da referência: seta apontando pro círculo).
- **Cor vermelha no texto** → mais um recurso, gasto com parcimônia (não é mais o punch-padrão).

## Catálogo

| Arquivo | Traço | Proporção (L×A) | Uso |
|---|---|---|---|
| `elipse-larga-1..3.png` | elipse chapada, traço fino | ~445×150 (ar 2.5–3.1) | circundar uma linha de texto |
| `elipse-larga-4.png` | elipse chapada menor | 298×122 | circundar palavra curta |
| `elipse-redonda.png` | elipse encorpada, mais redonda (duplo traço) | 487×289 | encapsular bloco/palavra com peso |
| `elipse-seta.png` | elipse + seta ondulada saindo (combo) | 854×330 | circundar e puxar o olho pra frente |
| `sublinhado-rabisco.png` | sublinhado grafite granulado | 278×35 | grifo de ênfase sob frase |
| `sublinhado-reto.png` | sublinhado reto fino | 481×24 | grifo mais discreto/limpo |
| `sublinhado-curto.png` | sublinhado curto | 145×22 | grifo sob 1–2 palavras |
| `sublinhado-seta.png` | sublinhado que vira seta curva (desce) | 481×162 | grifar e apontar pra baixo |
| `traco-curto.png` | traço curto | 140×28 | marca/divisor pequeno |
| `seta-reta.png` | seta reta horizontal | 778×60 | direção forte, linha do tempo |
| `seta-gancho.png` | seta curta em gancho | 167×156 | apontar de perto |
| `seta-ondulada-1..3.png` | setas onduladas | var. (ar 1.8–3.2) | direção solta/orgânica |
| `bullets.png` | 3 bolinhas (vertical) | 24×256 | marcadores de lista |
| `ticks.png` | 2 tiquinhos de ênfase | 61×63 | brilho lateral em palavra |
| `brilho.png` | ponto/brilho | 37×39 | faísca/destaque pontual |

Ao aprovar um elemento novo no futuro: salvar aqui (nome descritivo), recortar na caixa (tirar transparente em volta) e adicionar linha nesta tabela.
