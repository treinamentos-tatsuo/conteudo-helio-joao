# Kit Manychat — carrossel 106 ("O banco não quebra sua empresa. Ele só financia a quebra.")

- **Publicação:** 11/09/2026 (o user posta depois que a automação estiver montada STOPPED; amarrar ao post e ativar após o "postei").
- **Caminho de CTA (regra de 09/09):** **diagnóstico gratuito**. Terceiro post do caminho (100 = 1, 103 = 2, 106 = 3, 111 = 4).
- **Palavra-chave:** DIAGNÓSTICO, palavra FIXA do caminho. Leva acento, então SEIS grafias: `DIAGNOSTICO, diagnostico, Diagnostico, DIAGNÓSTICO, diagnóstico, Diagnóstico`.
- **Rastreio:** código numérico sequencial no UTM. Este post = **3**.
- **Link:** `https://rtc.tatsuoacademy.com/diagnostico?utm_source=manychat&utm_medium=dm&utm_campaign=3`
- **Colisão:** pesquisar "diagnostico" no painel ANTES de criar. A checagem do caminho é "existe global LIVE com DIAGNOSTICO?" (a palavra se repete em todo post do caminho). Em 09/09 só existia a `DIAGNOSTICO ANIVERSARIO TATSUO` (específica) e a `DIAGNOSTICO-1` (específica, do 100).
- **Automação:** por POST ESPECÍFICO. Nome: `IG | 2026-09-11 | DIAGNOSTICO-3 | banco financia a quebra`
- **Modelo a duplicar:** a `IG | 2026-09-09 | DIAGNOSTICO-1 | repost cabeca de dono` (mesmo domínio `diagnostico`, mesmas 6 grafias; só muda nome, DM e o rabo do UTM: End + Backspace + `3`).

## Mensagem da DM (94 caracteres)
Você sabe a parcela de cor. E se a sua conta fecha? Diagnóstico gratuito com um especialista.

## Texto do botão
`>> Quero ver <<` (teto de 20 caracteres no campo)

## Operação
1. Antes da publicação: duplicar → renomear → conferir as 6 grafias → DM (por `form_input`) → botão + link por digitação no modal (`form_input` não grava ali) → conferir link em 3 passadas (Home / Right×61 / End) → Atualização → deixar STOPPED (post ainda o do modelo, carrossel 100).
2. Com o post no ar: Editar → grade 'Mostrar Todos' → capa "O BANCO NÃO QUEBRA SUA EMPRESA / ELE SÓ FINANCIA A QUEBRA" (parede rachada com escoras) → conferir preview (legenda "Eu vou te contar como a maioria das empresas pequenas quebra") → conferir UTM (`End`: `utm_campaign=3`) → Atualização → Ativar → print. Preencher `data_publicacao` na ficha do 106.

## Montagem (11/09, ~12h58) — STOPPED, aguardando o user postar
- Chrome: `select_browser` no `ee5937df` (Browser 4 na lista; user escolheu no `AskUserQuestion`); T laranja conferido no primeiro screenshot.
- Colisão: "diagnos" devolve só a `IG | 2026-09-09 | DIAGNOSTICO-1 | repost cabeca de dono` (LIVE, específica, 2 exec., 50% CTR) e a `DIAGNOSTICO ANIVERSARIO TATSUO` (LIVE, específica, 7 exec.). Sem global. Sem colisão. Nem a DIAGNOSTICO-2 (103) nem a DIAGNOSTICO-4 (111) existem no painel ainda.
- Duplicada da DIAGNOSTICO-1 (lista → ⋮ → Duplicar; ~15 s); renomeada no modal Renomear (cmd+a + digitação, conferido no zoom).
- Palavra: herdada intacta nas 6 grafias (conferido com End no campo: `…, DIAGNÓSTICO, diagnóstico, Diagnóstico`).
- DM por `form_input` (ok de primeira; preview do celular já mostrou o texto novo). Botão herdado `>> Quero ver <<`, sem mexer.
- Link: só o rabo (End + Backspace + `3`). Conferido em três passadas: Home `https://rtc.tatsuoacademy.com/diagnostico?utm_source=mar…` / Right×61 parou depois de `manychat` / End `utm_campaign=3`.
- Atualização (~30 s) → voltou pra tela de Insights, STOPPED, com a DM nova e o botão no painel esquerdo.
- Post ainda o do modelo (carrossel 100, capa "Você paga mediano…"). Amarrar ao 106 depois do "postei".
- URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260911155625_241974
- Viewport nesta sessão: lista 1201 px (⋮ da linha em x≈1122 no hover; Renomear +46, Duplicar +84); automação 1232 px: STOPPED `Editar` (1068, 34), `Ativar` (1136, 34); em edição `Atualização` (1160, 34), `Cancelar` (1063, 34); botão do link em y≈817 depois de 10 ticks de scroll; modal do link `Salvar` (790, 251); campo do link (615, 194).

## Ativação (11/09, ~13h03) — LIVE
- "postei agora" do user ~13h00. Editar → 'Mostrar Todos': o carrossel 106 já estava em PRIMEIRO na grade ("Eu vou te contar com…", há 56 segundos) — sem precisar alternar o rádio.
- Selecionado; preview conferido (capa "O BANCO NÃO QUEBRA SUA EMPRESA / ELE SÓ FINANCIA A QUEBRA", parede rachada com escoras; legenda "Eu vou te contar como a maioria das empresas pequenas quebra"; 1 curtida, 2 comentários).
- UTM sobreviveu à troca de post (modal do botão, End: `utm_campaign=3`); fechado no X sem salvar.
- Atualização (~30 s) → Ativar → **LIVE ~13h03** (botão virou "Interromper"). ~3 min depois da publicação.
- `data_publicacao=2026-09-11` preenchida na ficha do 106.
