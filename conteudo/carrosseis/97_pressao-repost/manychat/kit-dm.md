# Kit Manychat — carrossel 97 (repost "Se você sente pressão... parabéns", versão estendida)

- **Publicação:** 08/09/2026, ~15h45 (user avisou "postei" e pediu a ativação na mesma mensagem)
- **Post anterior da mesma copy:** 26/07/2025 https://www.instagram.com/p/DMlc6cfxlnb/ (CTA COMANDO, evento 06/08; 102,0 interações/1k; 441 comentários)
- **Por que a palavra mudou:** COMANDO é a palavra da automação GLOBAL e LIVE `Comando!! MBV` (4.889 disparos). Qualquer comentário COMANDO dispararia o cano antigo sem atribuição. O slide 11 original ("Método. Clareza. Comando!") também saiu da peça.
- **Palavra-chave:** RECOMPENSA (aprovada pelo user 08/09). Sem acento, então TRÊS grafias: `RECOMPENSA, recompensa, Recompensa`.
- **Colisão:** RECOMPENSA não existe no registro-posts.csv nem no baseline; pesquisar "recompensa" no painel antes de criar.
- **Automação:** por POST ESPECÍFICO. Nome: `IG | 2026-09-08 | RECOMPENSA | repost pressao`
- **`utm_campaign`:** `2026-09-08-RECOMPENSA` (DD = dia da publicação)
- **Link:** `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-08-RECOMPENSA`
- **Modelo a duplicar:** a automação mais recente no padrão data+palavra (em 08/09: `IG | 2026-09-07 | ESTRUTURA | repost cansado demais`). Trocar data e rabo do UTM (End + Backspace + novo).

## Mensagem da DM (69 caracteres)
Pressão você já aguenta. Quer ver como ser pago pelo risco que corre?

## Texto do botão
`>> Quero ver <<`

## Operação
1. Antes da publicação: duplicar → renomear → palavra + 3 grafias → DM + botão (tudo por `form_input`, nunca digitação) → UTM → conferir link em 3 passadas → salvar STOPPED (post ainda o do modelo).
2. Com o post no ar (user avisa "postei" ou timer): Editar → grade: esperar a capa "Se você sente pressão..." aparecer → selecionar → conferir UTM → Atualização → Ativar → print.

## Resultado (08/09, ~15h45)
- Chrome escolhido por tela de confirmação (`switch_browser`, o user clicou Conectar no "Tatsuo Academy"); T laranja conferido no painel antes de mexer.
- Busca "recompensa" no painel: só a `IG | 2026-09-03 | RISCO | repost empreender…` (a DM dela tem "recompensado"); palavra RISCO, sem colisão.
- Duplicada da `IG | 2026-09-07 | ESTRUTURA | repost cansado demais` (a mais recente com o link `v2-maio-org`), renomeada no modal da lista, tudo por `form_input`: palavra em 3 grafias, DM (69 chars), botão mantido `>> Quero ver <<`, link inteiro trocado (modal do ícone de corrente) e conferido em 3 passadas (Home / Right×61 parou depois de "manychat" / End = `2026-09-08-RECOMPENSA`). Sem bug de comer caractere.
- Post amarrado pela grade "Mostrar Todos": a capa "Se você sente PRESSÃO..." estava em PRIMEIRO ("há 4 minutos", legenda "Tem uma pergunta que a maioria dos donos…"), preview conferido. Atualização OK. **Ativar → LIVE** (botão virou "Interromper"). O `browser_batch` estourou o tempo na espera depois do clique, mas o estado já estava salvo.
- URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260908183639_168134
