# Cinco coisas que eu queria que o Hélio de 38 anos atrás soubesse — TEXTO APROVADO (14/10)
Montagem com fotos do Hélio em outra conversa (o user já tem as fotos).

1. Capa: 5 coisas que eu queria que o Hélio de 38 anos atrás soubesse.
2. Ponte: Se eu pudesse voltar no tempo e ensinar só cinco coisas pro menino que saiu da feira e construiu uma empresa que vendeu mais de 9 bilhões em 4 continentes, seriam estas.
3. Lição 1: Primeiro arruma a casa, depois vai pra rua. Dá pra errar lá fora, vendendo e arriscando. Aqui dentro, no custo, no gasto e no caixa, não dá. (v9, 14/10: o user pediu pra exemplificar o 'aqui dentro')
4. Lição 2: Ser um bom vendedor não faz de você um bom empresário. Eu vendia muito e não sabia nada de gestão. O mercado está cheio de vendedor brilhante com empresa quebrada.
5. Lição 3: Empresa existe pra gerar dividendo pro dono. Faturamento não é lucro, e lucro não é dividendo. Se a sua empresa não constrói patrimônio pra você, qual é o sentido de ser empresário?
6. Lição 4: Empresa se faz com gente. Não queira fazer tudo sozinho. Aprenda a delegar. Sua empresa nunca vai ser maior que o time que você forma. (v9, 14/10: o user pediu conselho ao Hélio do passado, não confissão; 'delegar' pela doutrina da casa)
7. Lição 5: Trabalhar muito sem fundamento cobra um preço alto. E não é só em dinheiro: eu perdi momentos com meu pai e com meus filhos que não voltam mais.
8. CTA: O que eu levei 38 anos pra aprender, hoje eu ensino em três dias na Imersão MBV. Comenta MBV que eu te mando como participar.

Palavra-chave: MBV (Manychat por post específico na hora da publicação).

## Montagem (14/10, modelo fotos-reais; código em `_scripts/build.py`, base do 220)

- **Declarações:** interlocutor dono de PME; uma dor: o dono que trabalha muito sem fundamento (vende, faz tudo sozinho) e não constrói patrimônio; causa técnica: falta de gestão (Lucratividade, Crescimento, Cultura); caminho **imersão MBV**; palavra **MBV** (a global legada `MBV` segue LIVE em "qualquer publicação"; a específica do post tem prioridade).
- **Fotos:** 1 `Hélio/MBV-230` em COR (olhar firme, de baixo, tijolo vermelho) · 2 `antigas/Captura 19.04.47` (o Hélio na feira; recorte sem legenda e sem a marca da revista) · 3 **gerada**: escritório arrumado à noite, livro-caixa e cofre na mesa, a rua esperando lá fora · 4 **gerada**: sapatos gastos e mala de vendedor ao lado de um livro de contas empoeirado · 5 **gerada**: chave de casa e foto da casa na mesa do dono (patrimônio) · 6 **gerada**: fileira de aventais e luvas de trabalho, um pra cada pessoa do time · 7 **gerada**: bicicleta de criança, cadeira e bola no quintal ao entardecer, casa acesa e ninguém fora · 8 `Hélio/0011` em COR (falando, papéis na mão; só o Hélio).
- **Composições:** 1 base com caixa carmim "5 COISAS"; 2 base com "seriam estas." em marca-texto; 3 à esquerda; 4 centralizado com marca-texto; 5 à esquerda; 6 dividido; 7 centralizado com marca-texto; 8 fecho com MBV em caixa carmim. Rótulo "LIÇÃO N". Capa e fecho em cor, miolo P&B (como no 220).
- **Texto literal do user**, sem mudança. Sugestões não aplicadas: "cinco coisas" (slide 2) e "três dias" (slide 8) em algarismo, pela regra do modelo; "Sua empresa" → "A sua empresa" (slide 6).

## Legenda (post) — FINAL do user (14/10, literal; sem o fecho institucional)

```
Essas são as cinco coisas que eu ensinaria pro meu eu do passado, o menino que acordava de madrugada pra limpar peixe na feira e achava que, para ter sucesso, bastava trabalhar e vender.

Eu levei anos pra entender que vender muito não é a mesma coisa que enriquecer, e que a ponte entre as duas se chama gestão. A conta de não saber disso não vem só no balanço. Vem na mesa do jantar e nos dias que não voltam mais.

Eu não posso voltar. Mas você, que ainda está no meio do caminho, pode encurtar essa estrada.

Comenta MBV que eu te mando como participar da Imersão MBV, o meu treinamento de gestão pra donos de PME.
```

## v2 (14/10, revisão do user)

- **Capa:** a linha "que eu queria que o Hélio de 38 anos atrás soubesse" passou do peso 600 pro 400 (mesma Source Serif Pro; o semibold em branco sobre preto lia "arredondado, grosso").
- **Slide 2, dualidade:** à esquerda, **gerado a pedido do user**, o menino de ~20 anos DE COSTAS limpando peixe na feira de madrugada (P&B; nissei, cabelo liso e preto; rosto nunca aparece); à direita, o Hélio hoje (`Hélio/0020`, em cor, de perfil, braços abertos, telão vermelho do MBV). A foto da Dinheiro saiu porque é uma releitura com o Hélio já mais velho. Exceção pontual à regra "o Hélio nunca é gerado por IA", pedida pelo user, sem rosto. Montagem em `_scripts/dual.py`.
- **Lições:** a frase da lição em texto branco sobre fundo carmim (`.hlt`); o resto em branco normal, sem vermelho.
- **Lição 1:** imagem nova, clara (escritório de dia, rua movimentada lá fora); a escura ficou em `imagens/_src/gen-03-v1.png`.
- **CTA:** `Hélio/MBV-244` (sorriso aberto, tijolo vermelho); a 0011 tinha careta. Build anterior em `_scripts/build_v1.py`.

## v3 (14/10)

- **Capa serrilhada:** a MBV-230 tem ruído de ISO alto (palco escuro) e o tratamento de cor aplicava nitidez + grão por cima. `grade_color()` virou versão limpa (desfoque leve de 0,6 px antes, autocontraste suave, sem nitidez nem grão). Vale pra capa e pro CTA.
- **Slide 2:** o Hélio de hoje fora do palco do MBV, como empresário real (`Hélio/SN-HOKEN-E-4`, sorrindo no escritório); os dois lados no mesmo P&B e fundidos num degradê largo de 260 px, pra virar uma imagem só (o escritório claro foi escurecido pra conversar com a madrugada da feira). Montagem em `_scripts/dual.py` (v2 guardada em `dual_v2.py`).
- **CTA:** a MBV-244 subiu e cresceu (sem o vazio em cima, longe do texto). Build anterior em `_scripts/build_v2.py`.

## v4 (14/10)

- **Fotos do Hélio SEM tratamento nem filtro** (pedido do user: "só quando eu pedir"): só recorte e redimensionamento (`RAW` no `build.py`). As imagens geradas seguem com o P&B.
- **Capa:** a MBV-230 tem granulação de ISO alto no próprio arquivo (palco escuro) e continuava pixelada mesmo crua. Trocada pela `Hélio/DSCF3076` (câmera Fuji, nítida, olhar firme, fundo vermelho), em cor.
- **Slide 2:** o Hélio de hoje (SN-HOKEN-E-4) em COR, sem tratamento; o menino da feira segue em P&B, fundido no mesmo degradê largo.
- **CTA:** foto subida, degradê mais baixo (menos preto) e texto descido (base a 180 px). Builds anteriores em `_scripts/build_v3.py` e `dual_v3.py`.

## v5 (14/10)

- **Capa:** `Hélio/MBV-207` (sorriso, mão aberta = o "5", plano aberto; a DSCF3076 tinha cara esquisita), crua, em cor. Já saiu no 220 (12/10, slide 12), mais de 3 dias antes.
- **Slide 2:** planos ABERTOS nos dois lados (o menino da feira quase inteiro; o Hélio de braços abertos no escritório, SN-HOKEN-E-4), só na parte de cima, degradê de 220 px entre eles. `_scripts/dual.py` (v4 em `dual_v4.py`).
- **CTA:** a 244 desceu um pouco (cabeça longe do topo); as cabeças da plateia embaixo ficam. Build anterior em `_scripts/build_v4.py`.

## v6 (14/10)

- **Slide 2:** sem dualidade. Só a feira, gerada em plano ABERTO (o menino nissei de costas limpando peixe, a feira de madrugada e a cidade ao fundo), P&B, tela cheia. A versão em close ficou em `imagens/_src/gen-02-v2-close.png`.
- **Degradê do user em todos os slides:** `imagens/degrade-base.png` (cópia de `iCloud/INSERTS/IMAGENS/degrade.png`, transparente até 55% e preto na base), sobreposto 2x e começando um pouco mais alto (3x nos slides 2 e 8, onde a foto é clara atrás do texto; no 6 também invertido no topo). Sai o degradê CSS que deixava a metade de baixo toda preta.
- **Rótulo "LIÇÃO N" em branco** (o carmim sumia sobre a foto escura).
- **CTA:** a cabeça do Hélio na altura que o user marcou; as cabeças da plateia continuam embaixo do texto. Build anterior em `_scripts/build_v5.py`.

## v7 (14/10)

- **Regra do degradê (user):** o `degrade.png` dele vale SÓ nos slides com foto do Hélio (1 e 8), em 3 camadas e começando mais alto (`.ovc`). Nas imagens geradas (2 a 7) volta o degradê CSS antigo, porque com o degradê dele o texto não lia.
- **Imagens geradas mais suaves:** saiu o `grade()` (curva em S, clareza, nitidez, grão: "cheias de filtro, muito contraste, muito pesada"); agora só P&B, contraste 0,82 e pretos levantados (`soft()`).
- **Texto:** capa e CTA com o bloco perto do centro (a foto da capa subiu pra o Hélio ficar acima do "5 COISAS"); nos slides 2 a 7 o bloco de baixo subiu (base a 210 px); no 6 o título de cima ficou onde estava. Build anterior em `_scripts/build_v6.py`.

## v8 (14/10)

- Capa e CTA voltaram ao texto e ao degradê da v6 (texto perto do centro ficou "muito pra cima"; build da v7 em `_scripts/build_v7.py`).
- Slides 2 a 7: bloco de baixo no meio-termo entre a v6 (150 px) e a v7 (210 px): base a 180 px.

## Kit Manychat — LIVE 14/10 ~13h49

- `IG | 2026-10-14 | MBV | cinco coisas 38 anos` · palavras `MBV, mbv, Mbv` · DM "Eu levei 38 anos pra aprender isso. Quer ver como eu ensino gestão no MBV?" · botão `>> Quero ver <<`
- Link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-14-MBV&utm_content=https://www.instagram.com/p/Dee2PfoETMw/`
- Post: https://www.instagram.com/p/Dee2PfoETMw/ (publicado 14/10/2026 ~13h46)
