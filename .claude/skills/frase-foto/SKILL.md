---
name: frase-foto
description: Cria post de FRASE ÚNICA com FOTO REAL para o Instagram do Hélio, em duas variantes - (A) a frase sobre fotos reais do Hélio no palco, em faixas empilhadas com fundo preto, texto branco e degradê preto; (B) a frase escrita à mão no PAPEL sobre a nossa mesa ou no VIDRO da nossa sala, primeira frase em preto e a segunda em vermelho. Legenda curta na voz do Hélio, com CTA pro link da bio. Use quando pedirem "frase com foto do Hélio", "frase com fotos", "faz essa com as fotos do Hélio", "frase no vidro", "frase no papel", "escreve no vidro". NÃO é a /frase (papel envelhecido, imagem gerada por IA, legenda longa) nem o /carrossel (vários slides).
---

# /frase-foto: frase com foto real (Hélio no palco, papel ou vidro)

Post de **uma imagem só**, 1080x1350. Duas variantes:
- **A. Fotos do Hélio:** fotos reais do acervo, "como se o Hélio tivesse falado isso no palco e a gente estivesse tirando foto do momento" (02/10).
- **B. Papel ou vidro:** a frase escrita à mão numa folha sobre a nossa mesa de mármore ou no vidro da nossa sala. A foto do escritório é real; só a escrita é gerada (image-edit).

**Quem escolhe a variante (fotos, papel ou vidro) é a pessoa que está fazendo, não o Claude.** Se ela não disse, perguntar, sem recomendar.

**Não confundir com a /frase.** Aqui não tem papel envelhecido, serifa da /frase nem cena gerada por IA. Na variante A é fundo preto, texto branco e o Hélio em foco. Misturar os dois formatos foi reprovado em 06/10.

## Antes de começar

Conferir na máquina:
- **Acervo de fotos** em `~/Desktop/fotos para carrosséis/` (pastas `Hélio/`, `publico/`, `detalhes/`, `antigas/`). Ele não está no Git. Sem ele a variante A não existe: parar e pedir a cópia.
- **Render:** Node + Playwright. Uma vez, na raiz do projeto: `npm install` e `npx playwright install chromium`. As fontes vêm do Google Fonts (precisa de internet); a Times New Roman é do macOS.
- **Python 3 com Pillow** (`pip3 install pillow`). numpy e opencv-python só pra capa de revista.
- **Variante B:** proxy do gpt-image-2 na porta 10531, logado com a conta da empresa (`~/.codex/auth.json`). Como subir: `.claude/skills/gpt-image2-ratos/SKILL.md`.

Todos os comandos rodam **da raiz do projeto**. Atalhos: `F=.claude/skills/frase-foto` e `P=conteudo/carrosseis/N_slug` (a pasta do post).

## 1. A frase

- **Frase que a pessoa mandou vai palavra por palavra**, inclusive frase tirada de outro perfil. Se der pra deixar mais com a cara do Hélio, ou se tiver erro de português, mostrar a original e a sugestão lado a lado e esperar o sim. Nunca aplicar antes ("Eu mandei uma frase e você fez outra", 08/10).
- Quando o Claude propõe a frase, ela precisa:
  - funcionar **sozinha, sem contexto**: quem não conhece o Hélio entende;
  - soar como o Hélio **fala**, nunca como frase criada ("mais humano. E menos criado", 12/10);
  - **não bater no empresário**: enaltecer quem empreende.
  
  Proibido "Não é sobre X, é sobre Y". Fórmula fixa repetida também não ("Quem já X sabe:", "Com a nossa vida funciona igual"): dizer a mesma coisa com outras palavras. O mecanismo pode repetir em poucos dias; a mesma tese não. Fonte de voz: só a do CLAUDE.md (guia original, transcrições do MBV, dados do projeto). Frase proposta pelo Claude espera a escolha da pessoa antes de montar.
- **Pasta do post:** próximo número livre em `conteudo/carrosseis/` com prefixo J (regra do João, 19/10: pasta `J[N]_nome`, N = maior J existente mais um, `ls conteudo/carrosseis | grep -oE '^J[0-9]+' | tr -d J | sort -n | tail -1`, mais 1). Conferir de novo logo antes do `mkdir`: outras sessões criam pastas ao mesmo tempo (colidiu no 187 e no 218). Criar `$P/imagens/`, `$P/instagram/` e `$P/carousel-text.md` (frase, variante, fotos usadas com o horário, versões).

## 2A. Fotos do Hélio

### Escolher as fotos
`python3 $F/scripts/fotos.py` lista a pasta `Hélio/` por horário (o da foto, não o da exportação) e grava uma folha de miniaturas numeradas (o caminho sai no fim). A miniatura só serve pra achar a foto; a escolha é sempre olhando o arquivo grande.

- **O Hélio é o único protagonista.** Plateia ao fundo pode; faixa que é só plateia não.
- **Todas as faixas são do mesmo momento:** segundos a poucos minutos de diferença, mesmo cenário ("as duas fotos são do mesmo momento. E tem que ser assim mesmo", 08/10).
- **A expressão casa com o texto de cada faixa** (sério em "firme", sorrindo em "humano"). Se o mesmo momento não tiver a expressão ideal, o mesmo momento vence.
- **Sem careta.** Abrir o rosto grande antes de usar (reprovado no 191 e no 217).
- **Cabeça e rosto inteiros**, nunca cortados nem cobertos por degradê ou texto.
- **Foto pode voltar ao feed**, só não a mesma foto num intervalo de 3 dias. Conferir: `grep -l "<nome da foto>" conteudo/carrosseis/*/carousel-text.md` e a data desses posts.
- **Vetadas:** DSCF3322 a DSCF3327 (quadro com os nomes antigos dos pilares). O `fotos.py` marca.
- **Hélio gerado ou alterado por IA: proibido** (rosto, ângulo, expressão, corpo). Tratar a foto real pode: recortar, escurecer, P&B, limpar o fundo (ex.: apagar a barra da tela atrás dele, como no 190). Se a foto pedida não existe no acervo (ex.: contra-plongée de verdade), avisar e sugerir fotografar no próximo evento.

### Quantas faixas
- **Frase curta:** 2 faixas, com jogo de palavra grande e linha pequena.
- **Frase média ou longa:** 2 faixas partidas no ponto de sentido, ou foto única.
- **3 faixas só quando o texto são 3 frases completas.** Uma frase só nunca se pica em 3 ("separando demais, tá difícil de entender", 08/10).
- Quando a frase cabe nos dois jeitos (faixas ou foto única), quem decide é a pessoa.

### Tratar a foto
`python3 $F/scripts/prepara_foto.py "<foto>" $P/imagens/foto-cima.jpg --tam 1080x675 --cx 0.5 --cy 0.4` recorta no tamanho da faixa (`--pb` pra preto e branco; opções no topo do script). Outro jeito: usar a foto inteira e enquadrar no HTML pelo `width/left/top` do `<img>`, como no 185.
- Cor, P&B ou uma de cada: escolha da peça, sem padrão.
- **Texto caindo nas costas do Hélio? Não espelhar a foto** (o olhar inverte junto). Posicionar a foto original com o Hélio do lado oposto ao olhar e completar o quadro com degradê preto lateral (`templates/a-2faixas-lateral.html`).
- **Nunca colar o Hélio recortado em fundo preto chapado** ("dá pra ver que ele tá todo recortado... muito amador", 06/10). O fundo real fica, escurecido.

### Diagramar
Antes de diagramar e antes de entregar, abrir `referencias/gente-boa.jpg` (a arte do user que é a referência do formato) e comparar.

- Fundo preto, **texto branco**, Hélio em foco.
- **A frase tem que estar "legível pra caramba"** (06/10). Nada claro atrás das letras sem degradê por baixo.
- **Nunca no rodapé.** Nos finais aprovados: em faixas, o bloco de cima termina de 40 a 95 px acima da emenda e o de baixo fica de 155 a 240 px acima do pé; em foto única, a frase fica no preto aberto acima do Hélio (descer a foto se precisar), no máximo até perto do centro.
- **Margem lateral mínima de 90 px** em qualquer layout, inclusive na capa de revista. Se a linha passar, diminuir a fonte ou quebrar a linha, nunca a margem. O `render.js` mede e avisa.
- **Degradê preto** no pé de cada faixa (leitura) e **na emenda** entre as fotos: a faixa de baixo nasce quase preta e abre devagar, senão a troca de foto fica "como se fosse um soco" (08/10).
- **Frase curta = jogo de tamanho:** linha pequena e palavra forte grande, com contraste de 2 a 2,5x. O texto fica na parte livre da foto, **do lado pra onde o Hélio olha**, e as linhas pequenas **coladas** na palavra grande, sem espaço sobrando (rascunho do user em `referencias/tetris-rascunho-user.jpg`).
- **Frase longa = o básico:** texto inteiro, sem firula, mas sem ficar "reto": dar personalidade com contraste de peso ou trocando a fonte só na palavra-chave.

Templates (copiar pra `$P/instagram/slide-01.html` e trocar fotos, textos e posições; o topo de cada arquivo explica o que mexer):

| arquivo | quando usar | origem | como ficou |
|---|---|---|---|
| `templates/a-2faixas-curta.html` | frase curta, jogo de tamanho | 185 | - |
| `templates/a-2faixas-tetris.html` | frase curta, linha pequena encaixada na palavra grande | 215 | `casos/215-lider-forte.jpg` |
| `templates/a-2faixas-lateral.html` | Hélio de um lado, degradê lateral do outro | 190 | - |
| `templates/a-2faixas-fonte-trocada.html` | frase média partida em 2, fonte trocada na palavra-chave | 217 | `casos/217-visao-lanterna.jpg` |
| `templates/a-foto-unica.html` | foto única, frase no preto em cima | 221 | `casos/221-dez-mil-vezes.jpg` |
| `templates/a-3faixas.html` | 3 frases completas | 177 | - |
| `templates/a-capa-revista.html` | foto única com a palavra-soco atrás da cabeça (camadas pelo `scripts/capa_revista.py` + `scripts/lift.swift`) | 191 | `casos/191-feira-capa-revista.jpg` |

### Render
`node $F/scripts/render.js $P/instagram/slide-01.html` grava `slide-01.png` e mede a margem. Abrir o PNG e conferir antes de mostrar: rosto inteiro e sem careta, texto fora do rodapé e legível, degradê na emenda, margem OK, e a comparação com a `gente-boa.jpg`.

## 2B. Papel ou vidro

1. **Base pronta, nunca regerar a cena:** `cp $F/bases/vidro-base-mid.png $P/imagens/base-vidro.png` (vidro da sala, zoom intermediário, emenda do vidro à direita) ou `cp $F/bases/mesa-v3.png $P/imagens/base-papel.png` (folha A4 no nosso mármore, vista quase de cima, mesa limpa).
2. **Quebra da frase**, em caixa alta: **a primeira frase em preto, a segunda em vermelho**, onde está a virada. O raciocínio tem que estar inteiro escrito, porque a legenda não completa a frase ("Tá muito aberto", 12/10). Papel: 2 linhas por cor. Vidro: 2 linhas por cor, ou 3 se a frase pedir (210). A quebra não muda palavra; se precisar mexer em pontuação ou palavra pra caber, sugerir e esperar o sim.
3. **Escrever:** pegar o prompt em `templates/b-prompt-vidro.txt` ou `templates/b-prompt-papel.txt` e trocar só as linhas e os acentos.
   `$F/scripts/edit.sh $P/imagens/base-vidro.png $P/imagens/vidro-v1.png "<PROMPT>"` (de 1 a 3 minutos; o script manda o prompt com `--form-string`, sem isso o motor inventa outra frase).
4. **Cortar pro post:** `python3 $F/scripts/corta.py $P/imagens/vidro-v1.png $P/instagram/vidro.png` (papel: `papel-v1.png` vira `papel-mesa.png`). O script grava junto o `-texto.png`, um zoom só do texto.
5. **Conferir no zoom, letra por letra e acento por acento** (o motor já pôs acento em DEMAIS). E conferir:
   - a tinta parece caneta de verdade, falhada e com pressão irregular. Perfeita demais fica "colada" (07/10); falhada demais fica "quebrada" (12/10). Nos dois casos, gerar de novo (`vidro-v2.png`, `v3`...);
   - vidro: texto à esquerda da emenda sem cruzar, um pouco acima do meio, longe do teto, fundo bem desfocado;
   - papel: letra de tamanho de nota, centralizada, com margem branca em volta.

## 3. Legenda (`$P/legenda.txt`)

Como se o próprio Hélio tivesse escrito embaixo da foto.
- **Por volta de 300 caracteres, uma ideia só**, primeira pessoa, voz falada. Sem desenvolver a frase em camadas, sem regra de quantidade de blocos. Contar os caracteres antes de entregar.
- **Nunca narrar a cena** ("hoje escrevi isso no vidro", "depois de uma reunião"): "fica muito forçado" (07/10).
- **Toda legenda leva a autoridade do tempo de mercado do Hélio**, como intenção, com palavras novas a cada post. "Estou no jogo há 38 anos" não é frase fixa (já saiu igual em 5 legendas seguidas). Fatos confirmados, se precisar de número: antes da Hoken ele vendia colchão; a Hoken vendeu 9 bilhões em 4 continentes; MBA na FGV.
- **CTA pro link da bio, construído e casado com o tema da frase.** Exemplo de estrutura: "Se quiser <o que a frase pede> na sua empresa, o link tá na bio." (variar as palavras). Nunca "Clica no link da bio." solto ("Isso não é ser sutil", 07/10). Nunca CTA de seguir.
- **Sem pitch do MBV, sem "Seja Bem-Vindo ao Fim do Analfabetismo Empresarial", sem palavra-chave, sem Manychat.**
- Revisão de português antes de entregar (concordância; nunca "te" e "você" na mesma frase). Se citar os pilares: Lucratividade, Crescimento e Cultura.

## 4. Entrega e fechamento

- **Correção no meio da rodada:** antes de refazer, salvar a versão anterior numerada (`instagram/v1-.../`, `imagens/vidro-v1.png`, `legenda-v1.txt`) e mostrar a nova ao lado da antiga. Nunca apagar a anterior: o user volta nela com frequência. A correção só vale se a escolha final confirmar.
- Mostrar sempre o post inteiro: o PNG e a legenda completa.
- **Entrega em `~/Desktop/frases claude/<palavra>/`**: o PNG (`<palavra>.png` na variante A; `vidro.png` ou `papel-mesa.png` na B) e o `legenda.txt`. Nunca em `carrosseis claude/`. Ao terminar: `open -a Preview <png>` e `open <pasta>`.
- Atualizar `$P/carousel-text.md` com a versão final e as fotos usadas (arquivo e horário).
- **`/etiqueta`**: formato `frase`, objetivo `alcance`.
- **Commit** conforme a regra de commit da máquina (CLAUDE.md).

## Casos (exemplos aprovados; mostram como ficou, não são regra)

As legendas abaixo repetem "Estou no jogo há 38 anos". Hoje vale a intenção (autoridade pelo tempo de mercado) com palavras novas a cada post.

**215, "Um líder forte é firme / sem deixar de ser humano."** (variante A, publicado 11/10). Imagem: `casos/215-lider-forte.jpg` (original: `~/Desktop/frases claude/POSTADOS/lider-firme-humano/lider-firme-humano.png`).
O user mandou a frase já quebrada e pediu o destaque em "líder forte"; "sem deixar de ser" entrou encaixado depois do h de "humano." (rascunho dele em `referencias/tetris-rascunho-user.jpg`). As fotos são as da arte "Gente boa", reusadas 10 dias depois a pedido dele. Ele queria o Hélio sorrindo embaixo, mas não havia foto sorrindo do mesmo momento, e ficou a original. A margem saiu com 70 px, antes da regra de 90.
```
Cobrar não é ser duro, e acolher não é ser mole.

Estou no jogo há 38 anos e aprendi que o time respeita quem diz a verdade olhando no olho e continua do lado quando a coisa aperta. Uma coisa sem a outra não sustenta ninguém.

Se quiser entender como liderar desse jeito na sua empresa, o link tá na bio.
```
(Ao publicar, o user juntou as duas frases curtas do começo numa só.)

**217, "A visão do futuro é a lanterna que guia // a liderança no presente."** (variante A, publicado 08/10). Imagem: `casos/217-visao-lanterna.jpg` (original: `~/Desktop/frases claude/POSTADOS/visao-lanterna/visao-lanterna.png`).
Em 3 faixas a frase ficou picada e o user passou pra 2, partida no sentido. A foto de cima foi trocada por causa de careta. O degradê da emenda e as linhas pequenas coladas na palavra grande foram pedidos dele. P&B em cima e cor embaixo foi escolha desta peça.
```
Quem só olha pro problema de hoje vive apagando incêndio. Quem enxerga onde quer chegar sabe qual incêndio deixar queimar e qual apagar primeiro.

Estou no jogo há 38 anos e aprendi que o time segue quem sabe pra onde está indo.

Se quiser enxergar mais longe na sua empresa, o link tá na bio.
```

**210, vidro: "NINGUÉM QUEBRA / POR TRABALHAR / DEMAIS." + "QUEBRA POR / TRABALHAR ERRADO / POR TEMPO DEMAIS."** (variante B, publicado 07/10). Imagem: `casos/210-vidro.jpg` (original: `~/Desktop/frases claude/POSTADOS/quebra-trabalhar-errado/vidro.png`).
A primeira versão saiu com cara de texto colado e muito zoom. Ficou boa em dois passos: base limpa com zoom intermediário, depois a escrita com tinta falhada. Pra subir o texto: `corta.py --zoom 1.06 --top 160`. Saiu em 3 linhas por cor.
```
Esforço não falta pra quem tem empresa. O que falta, muitas vezes, é parar e conferir se o caminho está certo.

Estou no jogo há 38 anos e sei bem como é isso. Trabalhar muito nunca foi o problema.

Se quiser entender onde está o erro na sua empresa, o link tá na bio.
```

**212, papel: "CADA EMPRESA QUE SOBREVIVE / NO BRASIL É UMA PROVA VIVA:" + "TALENTO E TEIMOSIA / VENCEM A BUROCRACIA."** (variante B, publicado 08/10). Imagem: `casos/212-papel.jpg` (original: `~/Desktop/frases claude/POSTADOS/teimosia-burocracia/papel-mesa.png`).
Como é uma dor que quem empreende no Brasil sente na pele, o user pediu o convite pra comentar antes do link. A frase dele foi adaptada pra quebra ("de que" virou dois-pontos e entrou "a burocracia") sem perguntar antes; hoje isso seria sugestão.
```
Abrir empresa no Brasil já é um ato de coragem. Manter ela de pé, ano após ano, é outra coisa.

Quem conseguiu sabe do que eu estou falando. Você concorda? Me conta aqui nos comentários.

E se quiser ir mais fundo nisso, o link tá na bio.
```

## Arquivos desta skill

- `templates/`: os HTML da variante A (tabela acima) e os prompts da variante B (`b-prompt-vidro.txt`, `b-prompt-papel.txt`).
- `scripts/`: `fotos.py` (lista e folha de miniaturas), `prepara_foto.py` (recorte da foto), `render.js` (PNG + margem), `edit.sh` (escrita no papel/vidro), `corta.py` (corte pro post + zoom do texto), `capa_revista.py` e `lift.swift` (só capa de revista).
- `bases/`: `vidro-base-mid.png` e `mesa-v3.png`, as bases aprovadas do 210 (reusadas do 212 ao 228).
- `referencias/`: `gente-boa.jpg` (a referência do formato, feita pelo user) e `tetris-rascunho-user.jpg`.
- `casos/`: as imagens finais dos casos acima e dos templates.
