# Modelo: Thread-X

**Em uma linha:** carrossel em formato de **thread do X/Twitter** — cada slide é um "tweet" do Hélio (header com avatar + nome + selo verificado + handle), texto serifado preto alinhado à esquerda, ênfase só em **negrito** (sem vermelho), opcionalmente com mídia de notícia embutida. O modelo de **comentário de notícia / tendência / dado do momento**.

> Voz: sempre `referencias/voz-tatsuo.md`. Operação de imagem: este modelo **não gera imagem por IA** (ver seção 6). Este arquivo define o QUE é o modelo. Não sobrescrever.

---

## 1. Quando usar (propósito / canal)

- **Canal:** feed do Instagram (e versão TikTok opcional).
- **Objetivo:** pegar uma **notícia, tendência, dado ou caso do momento**, comentar na voz do Hélio em formato de thread e amarrar no MBV (quase sempre **Lucratividade / margem / sobra**), fechando com CTA "comenta [número]". Leitura rápida, ritmo de thread.
- **Quando NÃO usar:** tema que pede metáfora visual forte + storytelling emocional encadeado com foto editorial sangrando no rodapé → esse é o **editorial-punch**. Thread-X é mais analítico/opinativo e ancorado em fato real (notícia/dado).

---

## 2. Arco de texto (a espinha)

**Thread**, não storytelling encadeado linha-a-linha. Cada slide é um **tweet** que avança o raciocínio — formato mais analítico/comentário do que o editorial. Não precisa que a última linha de um slide complete a primeira do próximo (embora aconteça às vezes, ex: "...Não vai." abrindo o slide seguinte).

Arco típico (adaptar ao tema):

1. **Capa / gancho** — frase que reposiciona o óbvio ("O tapa na cara que a Globo tomou não é na audiência. … É na margem de contribuição.") OU afirmação seca ("Para o empresário que ainda não entendeu: O estado não é seu amigo."). Pode já trazer card/print de notícia.
2. **Tese** — o reframe central do post ("faturar parecido não significa enriquecer parecido").
3. **Desenvolvimento (vários slides)** — contexto do caso, dados (número em **negrito**), prints de notícia, comparações. Mistura fato + leitura do Hélio. Cada slide adiciona uma camada.
4. **A lição / virada** — "E aqui está a aula que o pequeno e médio precisa enfiar na cabeça", "E é aqui que a maioria dos donos prova que é analfabeto empresarial".
5. **Amarra com o MBV** — margem / sobra / lucratividade / comando / "ler o próprio modelo econômico".
6. **Fechamento + CTA** — "Se você quer [dominar X], **comenta '[número]'**."

**Cada slide é um tweet curto que respira** — não encher. O conteúdo ocupa a metade superior do slide; o resto fica vazio, como um tweet real.

---

## 3. Nº e formato de slides

- **Thread longa:** faixa boa **12–16 slides** (exemplos de referência tiveram 15 e 16). Temas simples podem ir abaixo, mas o formato foi feito pra sustentar thread.
- **Instagram:** 1080 × 1350px (4:5). **TikTok:** 1080 × 1920px (deixar 230px livres embaixo).

---

## 4. Estrutura por slide (cada slide = 1 tweet)

- **Header fixo no topo:** avatar circular do Hélio + "Helio Tatsuo" (negrito) + selo azul verificado + `@helio.tatsuo` (cinza, sans-serif).
- **Corpo** abaixo, **alinhado à esquerda**: 1 a 4 "parágrafos" curtos separados por linha em branco.
- **Padrão recorrente:** linha(s) de **setup em peso normal** + **linha-punch em negrito**. O negrito carrega o ponto. Também usa negrito **inline** em palavra-chave ou no dado ("**32,40% do PIB**", "**onde a margem nasce**").
- **Recursos do formato:**
  - **Listas com bullet (•)**, itens em negrito ("folha / risco trabalhista / risco tributário…").
  - **Anáfora** — repetição do início da linha ("Não sabe… Não sabe… Não sabe", "Olha faturamento. Olha estrutura…").
  - **Abertura curta e seca em negrito** como continuidade do slide anterior ("Não vai.", "É dinheiro no bolso.", "É inaceitável.").
  - Frases staccato ("Plateia parecida. Receita parecida. Sobra muito diferente.").
- **Mídia opcional** (ver seção 6) entre os parágrafos.
- **Comprimento:** corpo na metade superior; não encher o slide. Texto curto, respirado.

---

## 5. Regras visuais

- **Fonte:** **Georgia** (serif) no nome e no corpo. *(Validar com o designer — base assumida é Georgia; primas próximas: Charter, PT Serif.)* Handle em sans-serif do sistema.
- **Cores:** texto quase-preto `#0f1419` (estilo X), handle cinza `#6b7280`, selo azul `#1d9bf0`. **SEM vermelho** — o negrito é o ÚNICO recurso de ênfase (diferença-chave pro editorial-punch).
- **Fundo:** o **mesmo** arquivo do editorial: `conteudo/carrosseis/_banco-referencias/background para carrosséis.png` (textura linho). Fallback de cor: `#F5F0EB`.
- **Avatar:** foto do Hélio, circular, **fixa em todos os slides**: `conteudo/carrosseis/_banco-referencias/avatares/helio.png`.
- **Layout:** header começa no terço superior do slide; corpo logo abaixo, **alinhado à esquerda**, padding lateral ~90px. Conteúdo na metade de cima, resto vazio.
- **Sem:** vermelho, foto editorial sangrando no rodapé (isso é do editorial-punch), texto centralizado, emojis, ornamentos.

Esqueleto do slide:
```html
<div class="slide">
  <div class="tweet">
    <div class="header">
      <img class="avatar" src="../../_banco-referencias/avatares/helio.png" alt="">
      <div class="who">
        <span class="name">Helio Tatsuo <svg class="check">…selo azul…</svg></span>
        <span class="handle">@helio.tatsuo</span>
      </div>
    </div>
    <div class="body">
      <p>linha de setup em peso normal</p>
      <p class="b">linha-punch em negrito</p>
      <!-- opcional: <img class="media" src="../imagens/img-0X.png"> -->
    </div>
  </div>
</div>
```
```css
.slide{ width:1080px; height:1350px; position:relative; overflow:hidden;
  background:#F5F0EB url("../../_banco-referencias/background para carrosséis.png") center/cover no-repeat;
  font-family:Georgia, serif; }
.tweet{ position:absolute; top:300px; left:90px; right:90px; }
.header{ display:flex; align-items:center; gap:22px; margin-bottom:30px; }
.avatar{ width:96px; height:96px; border-radius:50%; object-fit:cover; }
.name{ display:flex; align-items:center; gap:10px; font-weight:700; font-size:42px; color:#0f1419; }
.handle{ font-family:-apple-system,Helvetica,Arial,sans-serif; font-size:32px; color:#6b7280; margin-top:4px; }
.body p{ font-size:44px; line-height:1.42; color:#0f1419; }
.body p.b{ font-weight:700; }
.body p + p{ margin-top:34px; }
.media{ width:100%; border-radius:18px; margin-top:30px; display:block; }
```

---

## 6. Estilo de imagem / mídia

- **Este modelo NÃO gera imagem por IA.** A "imagem" é **mídia real de notícia** (print do site, manchete, foto/frame), **fornecida pelo Rodrigo** — ou nenhuma (thread 100% texto é normal e comum).
- **PERGUNTA OBRIGATÓRIA na criação:** *"Esse carrossel tem mídia de notícia embutida ou não?"*
  - **Sem mídia:** thread puro texto.
  - **Com mídia:** Rodrigo envia os **prints do site** (ele diz em quais slides entram). Encaixar no corpo do slide com cantos arredondados (`border-radius:18px`), largura ~100% do corpo, entre os parágrafos.
- **Card de manchete** (caixa branca com título de matéria em **negrito sans-serif**): pode ser **montado em HTML** quando for só citar o título de uma notícia sem ter o print (ex: o card "Como a Cazé TV quebrou um monopólio…" do post de referência).
- Salvar as mídias recebidas em `conteudo/carrosseis/[N]_[nome]/imagens/` (`img-01.png`…).

---

## 7. Fechamento

- **Último slide:** primeiro amarra a lição ao MBV (margem / sobra / "ler o próprio modelo econômico") e SÓ ENTÃO chama pra ação: **"Se você quer [dominar X], comenta '[número]'."** O número é o da oferta/lead, **fornecido pelo Rodrigo e varia por post** (ex: 307, 295), em negrito.
  - **Palavra-chave única por post (aprovado pelo user em 19/08/2026):** no lugar do número, usar a **palavra-chave ÚNICA deste post** — derivada do batismo/termo central do tema (ex: BABA, DELARGAR), em CAIXA ALTA e sem acento, inédita no perfil (conferir `conteudo/analise/registro-posts.csv`). Propor junto com o texto e submeter à aprovação do user. Formato do CTA continua idêntico: "comenta [PALAVRA]".
- **Legenda:** longa e reflexiva, na voz do Hélio, expande o tema (não resume os slides). Fecha com "comenta [número]" e, **opcionalmente**, a frase institucional "Seja Bem-Vindo ao Fim do Analfabetismo Empresarial." (apareceu em um post de referência, não em outro — é opcional).

---

## 8. Exemplos prontos (referência)

Posts do perfil do Hélio que originaram este modelo (referência de calibragem):
- **Cazé TV × Globo / margem de contribuição** — ~15 slides, COM mídia embutida (card de manchete + prints de notícia/live).
- **"O estado não é seu amigo"** — ~16 slides, 100% texto, SEM mídia. CTA "comenta 295".

Quando o primeiro thread-X for produzido pela skill, salvar em `conteudo/carrosseis/` e apontar aqui como exemplo interno.

---

## 9. Regras específicas / aprendizados

- **Foto do avatar fixa** em todos os slides (uma só, não rotaciona).
- **Zero vermelho** — só negrito como ênfase. É a diferença visual mais forte pro editorial-punch.
- **Mídia sempre via print real** fornecido pelo Rodrigo (ou card de manchete montado em HTML) — nunca imagem gerada por IA.
- **Fonte Georgia** assumida como base; **pendente validação do designer** — se ele apontar outra, atualizar a seção 5 aqui.
- Nome "Helio" sem acento; handle `@helio.tatsuo`.
