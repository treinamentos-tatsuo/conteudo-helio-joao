# Kit Manychat — carrossel 100 (repost "Você paga mediano... Cabeça de Dono")

- **Publicação:** 09/09/2026 às 19h (user avisou às ~16h; montar STOPPED antes, timer pra ativar às 19h).
- **Post anterior da mesma copy:** 19/08/2025 https://www.instagram.com/p/DNjeiYFRdaV/ (CTA COMANDO, aula de 27/08; 158,4 interações/1k; 2.395 shares; 385 comentários)
- **Caminho de CTA (regra de 09/09):** **diagnóstico gratuito** (call do prospect com um especialista da Tatsuo, nos três pilares). Primeiro post do caminho.
- **Palavra-chave:** DIAGNÓSTICO, palavra FIXA do caminho. Leva acento, então SEIS grafias: `DIAGNOSTICO, diagnostico, Diagnostico, DIAGNÓSTICO, diagnóstico, Diagnóstico`.
- **Rastreio:** código numérico sequencial no UTM (a palavra não muda entre posts do caminho). Este post = **1**.
- **Link:** `https://rtc.tatsuoacademy.com/diagnostico?utm_source=manychat&utm_medium=dm&utm_campaign=1` (base = link da bio do Hélio; formato do UTM a confirmar com o user na montagem)
- **Colisão:** pesquisar "diagnostico" e "diagnóstico" no painel ANTES de criar. Como o link está na bio, pode existir automação antiga (global ou de story) com essa palavra; se houver global LIVE, decisão do user (pausar como a `dividendo` em 07/09, ou conviver).
- **Automação:** por POST ESPECÍFICO. Nome: `IG | 2026-09-09 | DIAGNOSTICO-1 | repost cabeca de dono`
- **Modelo a duplicar:** a mais recente no padrão data+palavra (em 08/09: `IG | 2026-09-08 | NUMERO | repost comeca assim`). Trocar nome, palavra (6 grafias), DM, botão e o link INTEIRO (domínio muda: `diagnostico` em vez de `v2-maio-org`), tudo por `form_input`.

## Mensagem da DM (85 caracteres)
Talvez o mediano seja você. Quer descobrir? Diagnóstico gratuito com um especialista.

## Texto do botão
`>> Quero ver <<` (o campo aceita no máximo 20 caracteres; `>> Quero o diagnóstico <<` foi recusado)

## Operação
1. Antes da publicação: duplicar → renomear → palavra + 6 grafias → DM + botão (por `form_input`) → link inteiro → conferir em 3 passadas (Home / Right×61 / End) → salvar STOPPED (post ainda o do modelo).
2. Com o post no ar: Editar → grade: esperar a capa "Você paga mediano..." aparecer → selecionar → conferir UTM (`End`: `utm_campaign=1`) → Atualização → Ativar → print.

## Montagem (09/09, ~16h35) — STOPPED, aguardando a publicação das 19h
- Chrome escolhido por tela de confirmação (`switch_browser`, o user clicou Conectar no "Tatsuo Academy"); T laranja conferido no painel.
- Colisão: "diagnostico"/"diagnóstico" devolvem só a `DIAGNOSTICO ANIVERSARIO TATSUO` (LIVE, **post específico**, 4 grafias, 7 execuções, há 2 semanas). Sem global. Sem colisão.
- Duplicada da `IG | 2026-09-08 | NUMERO | repost comeca assim`, renomeada no modal Renomear (`form_input`).
- Palavra (6 grafias) e DM por `form_input`: ok de primeira. **No modal do botão, `form_input` NÃO gravou** (título e link voltaram ao valor antigo ao salvar): ali é digitação (`cmd+a` + `type`), como o baseline já dizia. Título com teto de 20 caracteres.
- Link conferido em duas pontas (Home: `https://rtc.tatsuoacademy.com/diagnostico?utm_source=mar…`; End: `utm_campaign=1`), reaberto depois de salvar e conferido de novo.
- Atualização → "As alterações foram salvas". Estado: **STOPPED**, post ainda o do modelo (carrossel 98).
- URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260909191910_866624
- Viewport nesta sessão: 1197→1226 px. Na lista, `⋮` da linha em x≈1119 (hover); Renomear a +47 px, Duplicar a +83. Na automação STOPPED: `Editar` ~(1038, 33), `Ativar` ~(1105, 33); em edição `Atualização` ~(1126–1155, 33).
- Falta às 19h: Editar → grade "Mostrar Todos" → capa "Você paga mediano..." → conferir UTM → Atualização → Ativar → print.

## Ativação (09/09, ~19h25) — LIVE
- Timer das 18h59 acordou a sessão; o carrossel não estava na grade às 19h00, 19h09, 19h12, 19h15 e 19h18 (um reel "1.400 anos de empre…" entrou às 19h: um gatilho "próxima publicação" teria pegado ele). O user avisou "postei agora" às 19h23; a grade "Mostrar Todos" já trazia o carrossel em PRIMEIRO ("Todo dono quer funci…", há 5 minutos → publicado ~19h18).
- Selecionado; preview conferido (capa "Você paga mediano… ENTREGA ESTRUTURA MEDIANA…", legenda "Todo dono quer funcionário com cabeça de dono", 6 curtidas e 2 comentários). Atualização → "As alterações foram salvas".
- Pegadinha: com a página rolada, o botão `>> Quero ver <<` fica em y≈820 e o "+ Adicionar Um Link" em y≈860; um clique em 872 abriu o modal VAZIO (2º botão). Fechei no X sem salvar; o painel seguiu com um botão só. Reabri o botão certo: link intacto nas duas pontas (`…/diagnostico?utm_source=mar…` / `utm_campaign=1`). Cancelar (nada mudou) → **Ativar → LIVE ~19h25**, 7 min depois da publicação.
- Viewport 1226 px: `Editar` ~(1063, 34), `Ativar` ~(1131, 34); em LIVE `Interromper` no lugar do Ativar.
- `browser_batch` com mais de ~9 esperas de 10 s estoura o tempo da ferramenta; pra esperar, usar `until` no shell e uma batch curta pra checar a grade.
