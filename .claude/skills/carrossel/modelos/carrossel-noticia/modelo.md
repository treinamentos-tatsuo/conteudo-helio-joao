# Modelo: Carrossel Notícia

**Em uma linha:** uma notícia de empresa grande (ou um dado do momento que interessa ao dono de PME) vira **lições pro dono de pequena e média empresa**, em slides curtos com foto em cima e texto embaixo, e fecha numa pergunta sobre a empresa de quem lê.

> Voz: sempre `referencias/voz-tatsuo.md` + gabarito + doutrina. Imagem: `referencias/motor-imagem.md`. Criado em 23/11/2026 a pedido do João, a partir da referência @leonardoleaoof (post da Smart Fit, instagram.com/p/DgDKtlJlApN). Da referência vem só a ESTRUTURA; voz, crença e oferta são da casa. Conversa fixada: **Carrossel Notícia**. Revisto no mesmo dia, depois da v1 do J406 reprovada (ver Aprendizados).

## 1. Quando usar
- Canal: feed do @helio.tatsuo, sozinho ou em **collab com a Tatsuo Academy** (declarar qual no CHECKPOINT 1, porque muda o gancho; ver seção 4).
- Objetivo: pegar carona numa notícia que o dono já viu (marca conhecida, recorde, número oficial) e transformar em aula pra empresa dele. Topo de funil com gancho de atualidade.
- Pauta: empresa grande em notícia (recuperação, crescimento, demissão, fala de CEO) ou dado do momento que pesa no bolso do dono (juros, imposto, inadimplência, quebradeira). As pautas saem do `/pautas` ou da lista que o João trouxer.
- Quando NÃO usar: comentário longo e analítico de notícia, com prints → `thread-x`. Tema sem fato do momento → `editorial-punch`.

## 2. Arco de texto: a notícia e as lições (cerca de 10 slides)
A peça é **pro dono de PME, não sobre a empresa grande**. A empresa da notícia aparece na abertura e volta no máximo uma vez, como lembrete. O resto é a empresa de quem lê.

1. **Capa: a promessa de aula.** "O QUE O DONO DE PEQUENA E MÉDIA EMPRESA PODE APRENDER / COM [O FATO] DA [EMPRESA]." Corpo: uma frase do Hélio tirando o corpo fora ("Eu não conheço os números de lá por dentro. Mas essa notícia ensina.").
2. **O fato**, com o número na manchete. Corpo: quando e o quê, numa frase.
3. **O detalhe da notícia que vira lição depois.** Fecha com um gancho em negrito ("Guarda essa parte.") que se paga numa das lições. É o fio que liga os slides.
4. **A ponte pro ICP:** "e isso não é coisa só de empresa grande", com o dado do momento (fonte no corpo).
5. **Quem é essa empresa:** a empresa com estrada, a que deu certo. Punch em negrito.
6 a 8. **Uma lição por slide**, com a etiqueta "1ª LIÇÃO", "2ª LIÇÃO", "3ª LIÇÃO". Cada lição é uma causa técnica de gestão dita na linguagem do dono. Pelo menos uma em primeira pessoa do Hélio ("Eu já vi muito dono..."), e uma delas paga o gancho do slide 3.
9. **O Hélio com lastro:** "EM 38 ANOS DE EMPRESA, / EU APRENDI UMA COISA." e a frase que fica.
10. **CTA:** a pergunta que encurrala sobre a empresa de quem lê + palavra-chave. Caminho (RAIO-X ou MBV) declarado no CHECKPOINT 1, como em todo carrossel.

Pode ter de 2 a 4 lições, conforme a notícia. O que não muda: a empresa grande só na abertura, as lições sobre a empresa do leitor, o Hélio em primeira pessoa e a oferta só no último slide.

## 3. Nº e formato
- Cerca de 10 slides (8 a 12). Instagram 1080×1350. **Preferir mais slides a mais texto por slide.**

## 4. Estrutura por slide
- **Título:** 2 partes. Linha 1 em branco; linha 2 numa placa carmim. Caixa alta, curto (até ~25 caracteres por linha). Quebra manual com `<br>` sempre que uma palavra ficaria sozinha na linha, inclusive dentro da placa.
- **Corpo: curto.** Uma frase (até ~100 caracteres) e, se tiver, o punch num parágrafo próprio em negrito. Se o corpo precisa de duas frases de informação, a informação vira dois slides.
- **Gancho da capa conforme o perfil:**
  - **Collab com a Tatsuo Academy:** terceira pessoa, tom de aula ("O que o dono de pequena e média empresa pode aprender com...").
  - **Só @helio.tatsuo:** o Hélio falando, em primeira pessoa ou direto com o dono ("Eu vi a notícia da X e pensei na sua empresa."). O "o que o dono pode aprender" soa institucional demais pro perfil pessoal.
- **Nomear o ICP sem puxar o micro:** "pequena e média empresa" ou "dono de empresa". Nunca "pequena empresa" sozinha.
- **Fato tem fonte.** Número só com fonte e período conferidos na matéria (ler a matéria inteira antes de escrever, não só a manchete). Termo jurídico exato (recuperação **extrajudicial** não é judicial). Fonte citada pelo nome de quem fez o levantamento. Matéria em "espaço patrocinado" (ex.: `oglobo.globo.com/patrocinado/...`) cita a empresa autora, nunca o jornal.
- **Nunca afirmar a causa da crise da empresa citada** se a matéria não disser: as lições são pro dono que lê, a empresa citada é espelho, e a capa ou a legenda diz isso ("não conheço os números de lá por dentro"). Risco jurídico.

## 5. Regras visuais
- Fundo `#0A0A0A`. Foto ocupando o topo (1080×900) com fade pro preto entre 430 e 860 px.
- Título Montserrat 900, 64 px (encolhe sozinho até 54 px pra linha 1 caber), letter-spacing -0.02em. Linha 2 em placa `#A91C20` com texto branco (o carmim direto sobre preto fica ilegível; por isso a placa).
- **Etiqueta de lição** acima do título: Montserrat 800, 22 px, caixa alta, branco, contorno de 2 px carmim.
- Corpo Montserrat 500, 33 px, `#E6E6E6`; negrito 800 branco.
- Rodapé: losango carmim + `@HELIO.TATSUO · ARRASTE` (cinza `#6B6B6B`, sem "Arraste" no último) + bolinhas de página, a ativa em carmim. No collab o Instagram já mostra os dois perfis no topo; o rodapé fica com o do Hélio.
- Template pronto: `template/build.py` (copiar pra `_scripts/` da peça e trocar a lista `SLIDES`; o 6º campo de cada slide é a etiqueta, `""` quando não tem). Render: `npx playwright screenshot --viewport-size=1080,1350 --wait-for-timeout=1800 "file:///<caminho>/slide-01.html" slide-01.png` (no Windows, caminho de `pwd -W`).

## 6. Estilo de imagem
- **Fotos da empresa da notícia (abertura): reais.** Foto de imprensa, de divulgação ou de site de shopping. Nunca gerar logo ou loja de marca real por IA. Com mais slides de abertura, usar fotos diferentes da mesma rede.
- **Tratamento das fotos reais:** P&B com o vermelho preservado e puxado pro carmim (`template/tratar.py entrada saida`). A marca aparece e a peça fica com a nossa cara.
- **Fotos do Hélio (lição em primeira pessoa, "38 anos" e CTA): P&B puro**, sem preservar vermelho (parede de tijolo e luz de palco viram mancha vermelha no rosto). Contraste +15%. Do acervo `~/Desktop/fotos para carrosséis/Hélio/` (o `_INDICE.txt` de cada lote descreve as fotos). Uma foto diferente por slide; no "38 anos", ele falando firme; no CTA, sério olhando. O rosto tem que ficar acima do título: ajustar `background-position`.
- **Slides de dado e de lição: imagem P&B gerada** (gpt-image-2, 1536×1024), fotojornalismo, sem texto nem logo legível, com espaço vazio embaixo. Estilo-base do prompt: `Black and white documentary photojournalism photograph, high contrast, deep blacks, natural film grain, shot on 35mm, editorial newspaper style, realistic, no text, no logos, no readable letters anywhere.` A imagem diz o punch do slide (porta de aço baixada pro recorde, galpão com placa desbotada pra "empresa com estrada", gaveta do caixa vazia com a loja cheia pra "faturamento não paga banco", mãos no contrato pra "o banco ganha lugar na mesa").

## 7. Fechamento
Último slide: pergunta que encurrala sobre a empresa de quem lê + "Comenta PALAVRA que eu te mando..." no caminho declarado. Legenda até 1.800 caracteres, na voz do Hélio, abre deixando claro que não fala por dentro da empresa citada, repete as lições com mais carne (primeira, segunda, terceira), fecha com CTA, frase institucional e uma linha de fontes.

## 8. Exemplos prontos
- **J406 Chilli Beans e a dívida com o banco** (`conteudo/carrosseis/J406_chilli-beans-divida-banco/`): recuperação extrajudicial de R$ 340 mi (g1) + recorde de 14.510 empresas (PreservaCred). Collab, 10 slides, 3 lições, CTA RAIOX. A v3 é a aprovada pelo João em 23/11/2026; a v1 reprovada está em `_rodadas/v1.md`.

## 9. Aprendizados
- **23/11, J406 v1 reprovada pelo João:** "os slides não têm uma narrativa fluida, cada slide é uma chuva de informação sem conexão. Falta pessoalidade do Hélio e a grande maioria do carrossel é sobre grande empresa e não pequena e média." Daí o arco de notícia e lições, o fio do "guarda essa parte" e o Hélio em primeira pessoa.
- **23/11, J406 v2:** "ficou com muito texto cada slide... pode ter mais slides." Daí o corpo de uma frase e os ~10 slides.
- Link do Google Notícias não abre no WebFetch (volta só "Google News"); abrir no Chrome, que segue o redirect.
