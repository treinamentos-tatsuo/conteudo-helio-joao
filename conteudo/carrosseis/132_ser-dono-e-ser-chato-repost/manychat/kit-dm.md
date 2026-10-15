# Kit Manychat — carrossel 132 (repost "Ser dono é ser chato" / CHATO)

- **Publicação:** 19/09/2026, ~17h20 ("postei, monte o manychat agora" às 17h28). Automação montada e ativada de uma vez: **LIVE ~17h40**. URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260919203117_043869
- **Caminho de CTA:** **imersão MBV**. Link: `https://rtc.tatsuoacademy.com/v2-maio-org`.
- **Palavra-chave:** CHATO. Grafias: `CHATO, chato, Chato`.
- **Rastreio:** `utm_campaign=2026-09-19-CHATO`. Link completo: `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-19-CHATO`
- **Automação:** por POST ESPECÍFICO. Nome: `IG | 2026-09-19 | CHATO | ser dono e ser chato repost`
- **Modelo duplicado:** `IG | 2026-09-17 | COMBINADO | convencer um adulto` (LIVE, 44 exec. / 34,1% em 2 dias; mesmo link da imersão, só o UTM trocado).
- **Colisão:** "chato" não devolve nada. "comando" devolve a global `Comando!! MBV` (LIVE, "alguma publicação ou Reel", 4.894 exec.) e a `comando repost`: não conflitam com CHATO; o CTA do repost foi trocado de COMANDO pra CHATO justamente pra não cair na global.

## Mensagem da DM (91 caracteres)
Ser dono é ser chato. Quer ver como montar o rito de cobrar, acompanhar e treinar todo dia?

## Texto do botão
`>> Quero ver <<` (herdado)

## Operação
1. Busca "chato" (vazio) e "comando" (só globais/antigas) → busca "combinado" → ⋮ da COMBINADO → Duplicar → ⋮ da cópia → Renomear (cmd+a + digitação, conferido por zoom nas duas pontas).
2. Abrir a cópia → Editar: o post do 132 já estava indexado como SEGUNDA miniatura da grade direta (capa da sapataria "SER DONO É SER CHATO"), ~15 min depois da publicação; selecionado, preview com a legenda nova.
3. Palavra por `form_input`; DM por `form_input`; link inteiro por `form_input` no modal do botão (End = `…2026-09-19-CHATO`; Home = `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=ma…`); tooltip da corrente conferido depois de salvar.
4. Atualização ("As alterações foram salvas") → Ativar.
- **Pegadinhas desta sessão:** viewport mudou de 1503 pra 1440 px no meio (coordenadas do ⋮ mudaram: 1416,414 → 1356,396); a busca por nome demora a indexar o rename (buscar "chato" logo depois voltou vazio; a lista sem filtro já mostrava o nome novo); o painel esquerdo rola sozinho depois de cada `form_input`, então clique por coordenada em ">> Quero ver <<" acertou o textarea duas vezes e o "Adicionar Um Link" uma (modal vazio, cancelado): tirar screenshot imediatamente antes de clicar no botão.
