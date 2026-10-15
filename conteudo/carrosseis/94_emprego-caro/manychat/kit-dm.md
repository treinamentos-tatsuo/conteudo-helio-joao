# Kit Manychat — carrossel 94 (Emprego caro · print de tweet)

- **Publicação:** 07/09/2026 às 13h (à mão, pelo user)
- **Palavra-chave:** DIVIDENDO (já impressa no slide 10). Sem acento na origem → TRÊS grafias: `DIVIDENDO, dividendo, Dividendo`
- **Colisão:** DIVIDENDO nunca foi palavra de CTA no registro-posts.csv; pesquisar "dividendo" no painel antes de criar (checar se existe global LIVE com essa palavra)
- **Automação:** por POST ESPECÍFICO. Nome: `IG | 2026-09-07 | DIVIDENDO | emprego caro`
- **`utm_campaign`:** `2026-09-07-DIVIDENDO`
- **Link:** `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-07-DIVIDENDO`
- **Modelo a duplicar:** `IG | 2026-09-06 | BASICO | repost empresario bobo` (a mais recente; UTM muda data e palavra: End + Backspace × 17 + `2026-09-07-DIVIDENDO`, ou form_input no campo inteiro)

## Mensagem da DM (93 caracteres)
Quinze mil no bolso não é lucro, é salário. Quer ver como fazer a empresa te pagar dividendo?

## Texto do botão (≤20)
`>> Quero ver <<`

## Operação
1. Antes das 13h: duplicar → renomear → palavra + 3 grafias → DM + botão + link (tudo por `form_input`) → conferir link em 3 passadas → salvar STOPPED (post ainda o do modelo, o 92).
2. Com o post no ar (user avisa "postei"): Editar → grade: capa "Se no fim do mês você coloca R$15 mil no bolso" → selecionar → conferir UTM → Atualização → Ativar → print.

## Resultado (07/09)
- 08:20–08:27: `IG | 2026-09-06 | BASICO | repost empresario bobo` duplicada → renomeada `IG | 2026-09-07 | DIVIDENDO | emprego caro` → palavra `DIVIDENDO, dividendo, Dividendo` → DM (93 chars) + botão `>> Quero ver <<` + link com `utm_campaign=2026-09-07-DIVIDENDO`, tudo por `form_input`. Link conferido em 3 passadas (End / Home / Home + Right×61 parou depois de "manychat"). Atualização salva; **STOPPED**, post ainda o do modelo (92, capa do Bobo).
- **COLISÃO ENCONTRADA:** existe a automação `dividendo` GLOBAL e LIVE ("qualquer publicação ou Reel"; palavras `Dividendo, dividendo`; 61 envios / 27 cliques / 44% CTR; modificada há 2 meses; DM "Para acessar o link da imersão.." + botão `>> Clique Aqui <<`). Mesmo caso da MBV de 29/08: quem comentar "dividendo" no carrossel 94 pode receber o link da IMERSÃO pelo cano global, sem atribuição. Decisão pendente do user: pausar a global durante a janela do post (7 dias) e religar depois, como foi feito com a MBV.
- Falta às 13h, com o post no ar e o user avisando "postei": Editar → grade: capa "Se no fim do mês você coloca R$15 mil no bolso…" → selecionar → conferir UTM (End) → Atualização → Ativar.
- **08h35 — decisão do user: "pausa a global dividendo e deixa só essa ligada".** Global `dividendo` (content20260710012542_133830) interrompida → STOPPED. Só a `IG | 2026-09-07 | DIVIDENDO | emprego caro` responde à palavra a partir da ativação. **Religar a global em ~14/09** (fim da janela do post), como foi feito com a MBV em 01/09.
- **Ativação (07/09):** publicação marcada pras 13h atrasou ~1h. Checagens da grade às 13h01, 13h07, 13h12, 13h23, 13h34, 13h40 e 13h51: nada (entrou um Reel "matéria tendenciosa" no meio, o que teria roubado um gatilho "próxima publicação"). Às ~14h07 o carrossel apareceu em SEGUNDO na grade (o primeiro é sempre o post do modelo, o Bobo); o "postei" do user chegou no mesmo minuto. Selecionado, preview conferido (capa "Se no fim do mês você coloca R$15 mil no bolso" + legenda "Tem dono que se orgulha de tirar quinze mil"; 2 curtidas e 2 comentários), UTM sobreviveu à troca de post (End: `2026-09-07-DIVIDENDO`), Atualização e Ativar: **LIVE às ~14h09**.
