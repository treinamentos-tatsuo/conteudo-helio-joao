# Modelo: Carrossel Notícia

**Em uma linha:** uma notícia de empresa grande (ou um dado do momento que interessa ao dono de PME) contada em slides curtos com foto em cima e texto embaixo, que viram a leitura do Hélio e fecham numa pergunta sobre a empresa de quem lê.

> Voz: sempre `referencias/voz-tatsuo.md` + gabarito + doutrina. Imagem: `referencias/motor-imagem.md`. Criado em 23/11/2026 a pedido do João, a partir da referência @leonardoleaoof (post da Smart Fit, instagram.com/p/DgDKtlJlApN). Da referência vem só a ESTRUTURA; voz, crença e oferta são da casa. Conversa fixada: **Carrossel Notícia**.

## 1. Quando usar
- Canal: feed do @helio.tatsuo.
- Objetivo: pegar carona numa notícia que o dono já viu (marca conhecida, recorde, número oficial) e transformar em espelho: "isso também está acontecendo na sua empresa?". Topo de funil com gancho de atualidade.
- Pauta: empresa grande em notícia (recuperação, crescimento, demissão, fala de CEO) ou dado do momento que pesa no bolso do dono (juros, imposto, inadimplência, quebradeira). As pautas saem do `/pautas` ou da lista que o João trouxer.
- Quando NÃO usar: comentário longo e analítico de notícia, com prints e 12+ slides → `thread-x`. Tema sem fato do momento → `editorial-punch`.

## 2. Arco de texto (7 slides)
1. **Capa: o fato com a marca.** O nome da empresa e o número na manchete ("CHILLI BEANS DEVE R$ 340 MILHÕES / PRO BANCO E FOI RENEGOCIAR."). Corpo: quando, quem, e um gancho de que não é caso isolado.
2. **A pergunta pro dono.** Vira a notícia pra empresa de quem lê ("A SUA OPERAÇÃO / PAGA OS JUROS DO BANCO?"). Corpo curto, manda arrastar.
3. **O dado que dimensiona** (fonte + período no corpo).
4. **A virada de público:** mostra que é problema do ICP (empresa com estrada, não novata nem micro). Fecha com um punch em negrito.
5. **A causa que as próprias empresas/dados apontam.**
6. **A leitura do Hélio** (foto dele): primeira pessoa com lastro ("Em 38 anos de empresa, eu aprendi..."), a causa técnica de gestão, punch em negrito.
7. **CTA** (foto dele): a pergunta que encurrala + palavra-chave. Caminho (RAIO-X ou MBV) declarado no CHECKPOINT 1, como em todo carrossel.

Os slides 2 a 5 podem trocar de ordem conforme a notícia; o que não muda: capa com a marca, a leitura do Hélio só no 6, a oferta só no 7.

## 3. Nº e formato
- 7 slides (6 a 8 se a notícia pedir). Instagram 1080×1350.

## 4. Estrutura por slide
- **Título:** 2 partes. Linha 1 em branco; linha 2 numa placa carmim. Caixa alta, curto (até ~35 caracteres por parte). Quebra manual com `<br>` quando a linha 1 deixaria uma palavra sozinha.
- **Corpo:** 110 a 180 caracteres, frase falada inteira. Punch opcional num parágrafo próprio em negrito.
- **Fato tem fonte.** Número só com fonte e período conferidos na matéria (ler a matéria inteira antes de escrever, não só a manchete). Fonte citada pelo nome de quem fez o levantamento. Matéria em "espaço patrocinado" (ex.: `oglobo.globo.com/patrocinado/...`) cita a empresa autora, nunca o jornal.
- **Nunca afirmar a causa da crise da empresa citada** se a matéria não disser: o Hélio usa o caso como espelho e a legenda deixa isso dito ("não conheço os números de lá por dentro"). Risco jurídico.

## 5. Regras visuais
- Fundo `#0A0A0A`. Foto ocupando o topo (1080×900) com fade pro preto entre 430 e 860 px.
- Título Montserrat 900, 64 px (encolhe sozinho até 54 px pra linha 1 caber), letter-spacing -0.02em. Linha 2 em placa `#A91C20` com texto branco (o carmim direto sobre preto fica ilegível; por isso a placa).
- Corpo Montserrat 500, 33 px, `#E6E6E6`; negrito 800 branco.
- Rodapé: losango carmim + `@HELIO.TATSUO · ARRASTE` (cinza `#6B6B6B`, sem "Arraste" no último) + bolinhas de página, a ativa em carmim.
- Template pronto: `template/build.py` (copiar pra `_scripts/` da peça e trocar a lista `SLIDES`). Render: `npx playwright screenshot --viewport-size=1080,1350 --wait-for-timeout=1800 "file:///<caminho>/slide-01.html" slide-01.png` (no Windows, caminho de `pwd -W`).

## 6. Estilo de imagem
- **Fotos da empresa da notícia (capa e slide 2): reais.** Foto de imprensa, de divulgação ou de site de shopping. Nunca gerar logo ou loja de marca real por IA.
- **Tratamento das fotos reais:** P&B com o vermelho preservado e puxado pro carmim (`template/tratar.py entrada saida`). A marca aparece e a peça fica com a nossa cara.
- **Fotos do Hélio (6 e 7): P&B puro**, sem preservar vermelho (parede de tijolo e luz de palco viram mancha vermelha no rosto). Contraste +15%. Do acervo `~/Desktop/fotos para carrosséis/Hélio/`; slide 6 com ele explicando, slide 7 sério olhando. O rosto tem que ficar acima do título: ajustar `background-position`.
- **Slides de dado (3 a 5): imagem P&B gerada** (gpt-image-2, 1536×1024), fotojornalismo, sem texto nem logo legível, com espaço vazio embaixo. Estilo-base do prompt: `Black and white documentary photojournalism photograph, high contrast, deep blacks, natural film grain, shot on 35mm, editorial newspaper style, realistic, no text, no logos, no readable letters anywhere.` A imagem diz o punch do slide (porta de aço baixada pro recorde, galpão com placa desbotada pra "empresa com estrada", mãos no contrato do banco pra causa).

## 7. Fechamento
Slide 7: pergunta que encurrala sobre a empresa de quem lê + "Comenta PALAVRA que eu te mando..." no caminho declarado. Legenda até 1.800 caracteres, na voz do Hélio, abre deixando claro que não fala por dentro da empresa citada, expande a tese, fecha com CTA, frase institucional e uma linha de fontes.

## 8. Exemplos prontos
- **J406 Chilli Beans e a fila da dívida** (`conteudo/carrosseis/J406_chilli-beans-divida-banco/`): recuperação extrajudicial de R$ 340 mi (g1) + recorde de 14.510 empresas (PreservaCred). CTA RAIOX. Primeiro do modelo, aprovado pelo João em 23/11/2026.

## 9. Aprendizados
- Link do Google Notícias não abre no WebFetch (volta só "Google News"); abrir no Chrome, que segue o redirect.
- (Atualizar conforme o João corrigir.)
