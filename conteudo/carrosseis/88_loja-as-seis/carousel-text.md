# Carrossel 88 — "O talento acorda às nove. A vontade abriu a loja às seis."

**Peça nova no editorial-punch, filha do carrossel de 31/12/2025** ("A vontade come o talento no café da manhã", 482 mil de alcance; ver `briefing.md`). Decisão do user (04/09): caminho C-2, palavra **METODO**. Guarda a FORMA do original (uma frase por slide, princípio universal, inimigo terceiro, slide citável isolado) e troca o concreto: a loja de bairro que abre às seis.

## Declarações de saída

- **Interlocutor:** os slides 1 a 8 falam de um terceiro (o talentoso que espera) e endossam quem abre às seis; nenhum slide diz "empresa" nem "dono" (H12: universal vence nichado). O dono de PME entra pelo espelho e é nomeado só no CTA. Nenhum slide fala com quem executa.
- **Causa técnica:** vontade é combustível, não motor. O que faz a loja crescer é **direção** (meta e número: pra onde) e **método** (rotina de comando que repete todo dia: como). É o que o treinamento vende. Sem isso, o dono de PME abre cedo por dez anos e fecha o mês do mesmo tamanho.
- **Nervo / pilar:** `talento-sem-vontade` (aponta pro terceiro, não pro caráter do dono; H18 não pega) · Cultura. Motor: endosso (regra 2026-08-29): a cutucada única fica no slide 7, tarde e vestida de doutrina.
- **Palavra do CTA:** **METODO** (inédita no registro; é a promessa). COMANDO está barrada: palavra da automação global "Comando!! MBV".

## Universo de imagem (uma história só, da capa ao CTA)

**Loja de bairro brasileira, comércio de rua, P&B editorial.** Portão de enrolar, calçada, balcão de madeira, garrafa térmica, avental. A luz conta a hora: madrugada azul-escura na capa, chuva no meio, poste no fim do dia, manhã cheia no CTA. Estilo-base `base` (fechado) em todas as cenas; `base_wide` só nas 3, 5 e 7 da v1, que ficaram. Gente em 4 de 9 (44%), cabeça inteira ou só mãos, câmera na altura do peito. Topo de toda foto em superfície contínua clara (`topo.py` antes de renderizar).

## Contexto de cada slide (guia a imagem)

1. **Capa** — dicotomia (user 04/09): duas lojas lado a lado na mesma parede; a da ESQUERDA aberta, portão levantado e luz acesa; a da DIREITA fechada, portão baixado; a calçada e a rua vazias entre elas, madrugada. (base) Diz: às seis, uma abriu e a outra não.
2. **O talentoso** — gaveta de escrivaninha meio aberta, o caderno FECHADO no fundo dela com a caneta presa na capa, poeira, papéis velhos por cima. Ninguém. (base) Diz: a ideia está guardada. (v1 era a mesa de café com o caderno aberto; reprovada: não transmitia "guardada". REGRA do user: a imagem transmite o ponto mais impactante do texto.)
3. **Espera** — o dono de avental atrás do balcão servindo café da garrafa térmica na caneca de ágate, o molho de chaves em cima do balcão. (base; o motor entregou a cena já dentro da loja em vez da mesa da cozinha, e ficou melhor: enquanto o outro espera, este já abriu e está tomando o primeiro café.)
4. **Grito** — mãos calejadas abrindo o cadeado da corrente do portão. Só mãos. (base)
5. **Chuva** — fachada da loja na chuva, calçada molhada refletindo a luz acesa, rua vazia, o dono de avental parado na porta com a vassoura, corpo inteiro. (base_wide + cinema)
6. **Dez anos** — o balcão de madeira gasto em primeiro plano, o dono atrás dele de frente pra câmera, grande no quadro, mãos no balcão, prateleiras logo atrás. (base, fechado; v1 em base_wide reprovada: ângulo aberto e imagem baixa)
7. **Cansaço** — fim do dia, portão baixado pela metade, o dono sentado no degrau da loja com o caderno de contas fechado no colo, luz de poste. (base_wide)
8. **Direção e método** — o dono em primeiro plano passando uma caixa por cima do balcão pra um funcionário de avental; um segundo funcionário abastece a prateleira atrás; loja maior e cheia. (base, fechado; v1 em base_wide reprovada)
9. **CTA** — manhã cheia: mãos passando a sacola por cima do balcão pra um cliente, a garrafa térmica da capa no canto. (base) Fecha o arco: a loja que abriu às seis está cheia.

## Legenda (post)

Ver `legenda.txt` (1.778 caracteres).

## Produção (04/09)

**v1 reprovada pelo user** (9 apontamentos): capa em Anton (pediu tudo Source Serif, só "talento" e "vontade" em vermelho negrito) e imagem sem a dicotomia; img-02 não transmitia "guardada" (REGRA: a imagem transmite o ponto mais impactante do texto); degradê visível em quase todos (tem que ser suave e imperceptível); texto abaixo do top da skill (eu tinha copiado os `top` do 87; corpo é 160, capa ~200); ângulo aberto e imagem baixa nos `base_wide` (6 e 8); slide 3 cortando o personagem; slide 9 mal diagramado; hora do slide 4 em número.

**v2 (o que mudou):**
- Texto: corpo `top:160`, capa `top:200`. Capa toda em Source Serif 52 com as duas palavras em vermelho negrito. Slide 4: "às 5h30". Slide 9: estrofe de 2 linhas em 40px + "Comenta METODO" + linha de fecho.
- Imagens regeradas com o `base` fechado: 1 (dicotomia: loja aberta à esquerda, fechada à direita, calçada vazia), 2 (caderno fechado na gaveta), 6 e 8 (balcão de perto). As v1 ficam em `imagens/_v1/`; os originais sem tratamento em `imagens/_raw/`.
- Degradê: dois mecanismos somados. (1) `dissolve.py` clareia o topo da própria foto com rampa smoothstep até a fração onde o assunto começa (por imagem: 18–38%), então a foto nasce do papel sem banda de cinza. (2) A máscara CSS deixou de ser a reta de 26% e virou curva longa que só chega a 100% no início do assunto (`fade.json`, 24–38%). No slide 3 as duas param acima da cabeça (20% / 26%) pra não cortar o personagem.
- Alturas por `fit2.py` (gap alvo 210; recorte lateral até 35% quando o sujeito está no miolo; `object-position: right bottom` no 3 pra segurar o homem na ponta). Alturas finais: 1000 · 1108 · 1000 · 1107 · 1074 · 925 · 1031 · 767 · 964.
- `topo.py` ok nas 9 (média 208–253, desvio ≤2,8).

**v3 (2ª revisão do user):** "texto muito para cima, desça levemente" → corpo `top:200`, capa `top:240` (a skill diz 160/200; o user calibrou pra 200/240 nesta peça). Capa: "falta parede acima das lojas" → regerada com a parede continuando, tabuleta de madeira gasta acima da loja aberta e cartaz rasgado acima da fechada. Slides 3, 5 e 7: "não mudou nada" → o defeito não era o fade, era a CENA: eram fotos abertas (`base_wide`) com campo de cinza escuro (parede, chuva, noite) encostando no papel, e nenhum degradê disfarça isso; no 83 aprovado as fotos são fechadas e o assunto começa logo abaixo do papel. Regeradas as três no `base` fechado, com cláusula "NO fog, NO mist inside the scene" (a v2 do 3 tinha névoa dentro da loja, que lia como degradê). Alturas finais: 988 · 1062 · 900 · 1042 · 1017 · 866 · 1005 · 720 · 906. v2 das quatro em `imagens/_v2/`.

Entrega: `~/Desktop/carrosseis claude/loja-as-seis/`.

## Manychat (04/09, montado STOPPED)

- Automação: `IG | 2026-09-05 | METODO | loja as seis` · `utm_campaign=2026-09-05-METODO` · palavra em 6 grafias (METODO, metodo, Metodo, MÉTODO, método, Método).
- DM: "Vontade você já tem. O que falta é direção e método. Quer ver como eu ensino isso?" · botão `>> Quero o método <<`.
- Publicado em **05/09 às 17h** (agendado). Automação amarrada ao post 88 e **LIVE às ~17h06**, dois minutos depois do aviso do user.
