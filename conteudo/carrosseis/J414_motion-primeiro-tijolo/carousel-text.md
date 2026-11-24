# J414 · Motion "O primeiro tijolo" (perfil Tatsuo Academy)

**Formato:** vídeo em motion 9:16, 1080x1920, 15,2 s. v2 com narração masculina (voz neural pt-BR-AntonioNeural, Microsoft, via edge-tts; não é a voz do Hélio) e trilha original bem baixa (`motion/musica.py`, sem direito autoral).
**Perfil:** @tatsuo.academy
**Inspiração (só estrutura e mecânica, nunca voz):** reel do @neuronvisuals "Perfectionist × Action Taker" (102 mi de views, 10/10/2026): um boneco acertando o primeiro tijolo com o nível enquanto o outro ergue a parede inteira e senta no topo.
**Padrão visual:** o layout novo da Academy (post DgAy_HqhKI1, "7 sinais"): fundo vermelho escuro com faixa de luz no chão, partículas, reflexo no piso, eyebrow mono "TATSUO · MBV", pílula com ponto branco, pílula central, etiquetas finas com linha guia, legenda em caixa escura com revelação palavra a palavra, marca d'água @TATSUO.ACADEMY no chão. Bonecos brancos com brilho, como na referência.
**Mesmo mecanismo do reel do trampolim (2,1 mi, o maior do perfil):** dois bonecos, contraste entre quem pensa demais e quem faz, pilar Crescimento.

## Texto na tela

| Tempo | Pílula | Legenda |
|---|---|---|
| 0,25–3,55 s | O PLANO | Um ainda está acertando o primeiro tijolo. |
| 3,65–6,85 s | A EXECUÇÃO | O outro já levantou a parede inteira. |
| 7,0–10,1 s | O RESULTADO | Plano perfeito não paga boleto. |
| 10,3–14,5 s | O RESULTADO | Quem executa erra, corrige e chega primeiro. |

Etiquetas: "PERFECCIONISTA · 1 TIJOLO" e "QUEM EXECUTA · N TIJOLOS" (conta de 0 a 55 enquanto a parede sobe). Pílula central: "PILAR CRESCIMENTO".

## Legenda do post

Enquanto um ainda acerta o primeiro tijolo, o outro já levantou a parede inteira.

Na empresa é igual. O dono perfeccionista refaz a apresentação, revisa a tabela de preço pela quinta vez, espera o site ficar pronto pra começar a vender. Tudo precisa estar no nível antes do primeiro passo. Enquanto isso, o concorrente lançou torto, vendeu, ouviu o cliente e ajustou.

Perfeccionismo parece cuidado. Na prática, é medo de errar vestido de qualidade.

No pilar Crescimento do MBV, crescer não vem do plano perfeito. Vem de decidir com o número que você tem, executar, medir e corrigir. Parede se levanta tijolo por tijolo, e o primeiro não precisa ficar perfeito. Precisa ficar no lugar.

Qual tijolo da sua empresa está no nível há meses e ainda não foi assentado?

## Arquivos
- `motion/cena.html`: a animação (SVG + HTML, função `renderAt(t)`).
- `motion/render.js`: `node render.js previa 1,4,9` (grade de quadros) e `node render.js video saida.mp4` (MP4 30 fps), rodando da raiz do repositório.
- `motion/J414_primeiro-tijolo-v1.mp4`: v1 (muda).
- `motion/J414_primeiro-tijolo-v2.mp4`: v2, com narração e trilha. A narração é a legenda falada; cada fala começa no início da legenda (0,25 / 3,65 / 7,0 / 10,3 s). Áudio em `motion/audio/` (n1–n4.mp3) e mixagem: voz +4 dB, trilha a 0,11 (cerca de 14 dB abaixo da voz).

## Status
v1 entregue em 24/11/2026; v2 (narração + trilha, pedido do João) substituiu a v1 na mesma data em `Desktop/POSTS/Video Motion Tatsuo Academy/NP J414_motion-primeiro-tijolo/`. Aguardando revisão do João.
