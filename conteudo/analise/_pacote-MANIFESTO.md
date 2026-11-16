# Pacote de dados brutos do analytics — 2026-11-15

Gerado em 2026-11-15 12:03 (horário de Brasília) por `scripts/pacote/gerar_pacote.py`, na máquina principal (a única que coleta: API do Instagram, CRM GoHighLevel e painel do Manychat).

> **Aviso:** dados brutos, sem interpretação; leads.json contém dados pessoais de leads, manter em canal privado.

Este manifesto só descreve os arquivos: o que é, de onde vem, quando foi coletado, quantos registros e quais colunas. Nenhum número aqui foi analisado ou comparado.

## Como importar

Na máquina que recebe: `python3 scripts/pacote/importar_pacote.py <caminho do zip>`. O importador confere o `checksums.txt` antes de copiar qualquer coisa. Conferência manual, dentro da pasta extraída: `shasum -a 256 -c checksums.txt`.

## Arquivos

| Arquivo no pacote | Vai para (na importação) | Origem | Coleta | Registros | Tamanho |
|---|---|---|---|---|---|
| `analise/desempenho.json` | `conteudo/analise/desempenho.json` | `scripts/instagram/pull_insights.py update` (API do Instagram, Graph API com login do Instagram) | 2026-11-15 11:44 | 2595 posts | 4.3 MB |
| `analise/desempenho.csv` | `conteudo/analise/desempenho.csv` | `scripts/instagram/pull_insights.py update` (mesma coleta do desempenho.json, em tabela) | mesma do desempenho.json (arquivo gravado em 2026-11-15 11:44) | 2595 posts | 750.3 KB |
| `analise/_snapshots.csv` | `conteudo/analise/_snapshots.csv` | `scripts/instagram/pull_insights.py update` (gravado no fim de todo update, sem chamada extra) | último dia fotografado 2026-11-15 (arquivo gravado em 2026-11-15 11:44) | 19698 linhas | 889.9 KB |
| `analise/leads.json` | `conteudo/analise/leads.json` | `scripts/ghl/pull_leads.py update` (API do GoHighLevel v2, CRM) | 2026-11-15 12:01 | 6378 contatos, 1770 oportunidades | 7.7 MB |
| `analise/_disparos.json` | `conteudo/analise/_disparos.json` | leitura manual do painel do Manychat no navegador (só leitura; o Manychat não tem API), feita no ritual | 2026-10-19 12:15 | 129 palavras | 16.8 KB |
| `analise/_painel-manychat.csv` | `conteudo/analise/_painel-manychat.csv` | histórico das leituras do painel do Manychat (uma linha por automação por leitura, com `lido_em`), feito no ritual; desde 19/10 é a régua de performance do post | última escrita 2026-11-13 19:47 | 522 linhas | 45.7 KB |
| `analise/_painel-instagram.csv` | `conteudo/analise/_painel-instagram.csv` | digitado à mão a partir de captura de tela do painel do Instagram (dado da conta, não vem da API) | 2026-08-31 16:28 | 2 linhas | 276 B |
| `analise/_update.log` | `conteudo/analise/_update.log` | saída do agendamento do macOS `com.tatsuo.ig-update`, que roda `pull_insights.py update` às 9h, 14h, 20h e no boot | última escrita 2026-11-15 11:44 | 51142 linhas | 3.7 MB |
| `analise/_pull.log` | `conteudo/analise/_pull.log` | saída do único `pull_insights.py pull` completo (06/08/2026), que montou a base | última escrita 2026-08-06 11:30 | 3439 linhas | 115.2 KB |
| `analise/registro-posts-factual.csv` | `conteudo/analise/_registro-maquina-user.csv` | recorte de `conteudo/analise/registro-posts.csv` (fichas da skill /etiqueta), só colunas factuais | arquivo gravado em 2026-11-14 14:27 | 225 fichas | 37.8 KB |

## Detalhe por arquivo

### `analise/desempenho.json`

Origem: `scripts/instagram/pull_insights.py update` (API do Instagram, Graph API com login do Instagram).

- `pulled_at`: 2026-11-15 11:44 (horário local da máquina principal, Brasília). `count`: 2595.
- Posts publicados de 2025-01-02 a 2026-11-15. Por tipo: CAROUSEL_ALBUM/FEED 709, IMAGE/FEED 344, VIDEO/REELS 1542.
- Campos de cada post: `caption_full`, `caption_preview`, `comments_count`, `comments_read`, `cta_keyword`, `cta_keyword_count`, `cta_share`, `cta_top_tokens`, `id`, `media_product_type`, `media_type`, `metrics`, `permalink`, `timestamp`.
- Métricas em `metrics`: `comments`, `follows`, `ig_reels_avg_watch_time`, `ig_reels_video_view_total_time`, `likes`, `profile_visits`, `reach`, `saved`, `shares`, `total_interactions`, `views`.
- `timestamp` é o horário de publicação como a API devolve (UTC, ex. `2026-10-13T15:36:50+0000`).
- `caption_full` é a legenda inteira com as quebras de linha trocadas por espaço; `caption_preview`, os primeiros 140 caracteres.
- Métricas pedidas por tipo: IMAGE e CAROUSEL_ALBUM = reach, likes, comments, saved, shares, total_interactions, views, follows, profile_visits. VIDEO/REELS = reach, likes, comments, saved, shares, total_interactions, views, ig_reels_avg_watch_time, ig_reels_video_view_total_time (a API não entrega follows nem profile_visits para vídeo). Os dois tempos de reel vêm em milissegundos, como a API devolve.
- Todo valor de métrica é o acumulado de vida do post no momento em que ele foi lido.
- O `update` relê só os posts publicados nos últimos 30 dias (e acrescenta os novos). Post mais velho que isso guarda o número da última vez que foi lido.
- `comments_read`, `cta_keyword`, `cta_keyword_count`, `cta_share`, `cta_top_tokens` foram calculados só pelo `pull` completo de 06/08/2026, lendo os comentários. O `update` não lê comentário: guarda o valor antigo, e post novo vem com 0 ou vazio nesses campos.

### `analise/desempenho.csv`

Origem: `scripts/instagram/pull_insights.py update` (mesma coleta do desempenho.json, em tabela).

- 2595 linhas, uma por post. Mesma coleta do `desempenho.json` (é reescrito junto com ele).
- Colunas: `timestamp`, `media_type`, `media_product_type`, `id`, `permalink`, `caption_preview`, `comments_count`, `comments_read`, `cta_keyword`, `cta_keyword_count`, `cta_share`, `comments`, `follows`, `ig_reels_avg_watch_time`, `ig_reels_video_view_total_time`, `likes`, `profile_visits`, `reach`, `saved`, `shares`, `total_interactions`, `views`.
- Não tem `caption_full` nem `cta_top_tokens` (só no JSON). Célula vazia = a API não devolveu aquela métrica para aquele tipo de post.

### `analise/_snapshots.csv`

Origem: `scripts/instagram/pull_insights.py update` (gravado no fim de todo update, sem chamada extra).

- 19698 linhas; 82 dias fotografados, de 2026-08-18 a 2026-11-15; 369 posts na foto do último dia.
- Colunas: `data_snapshot`, `post_id`, `idade_dias`, `comments`, `reach`, `saved`, `shares`.
- Uma linha por post por dia, para todo post com 0 a 30 dias de idade na data da foto. `idade_dias` = `data_snapshot` menos a data do `timestamp` de publicação.
- `comments`, `reach`, `saved`, `shares` são o acumulado de vida naquele dia (a API não dá série diária; ela só existe porque o update fotografa todo dia).
- Rodar o update mais de uma vez no mesmo dia substitui as linhas daquele dia pela leitura mais recente; nunca duplica.
- Dia sem foto não se recupera pela API. Dias sem foto entre o primeiro e o último: 2026-08-19, 2026-08-22, 2026-08-23, 2026-09-16, 2026-09-18, 2026-10-22, 2026-11-10, 2026-11-11.

### `analise/leads.json`

Origem: `scripts/ghl/pull_leads.py update` (API do GoHighLevel v2, CRM).

- `pulled_at`: 2026-11-15 12:01 (Brasília). `janela_dias`: 35 (contatos de 00h de 35 dias atrás até a hora da coleta).
- `total_contatos`: 6378; `total_reimpactados`: 2280; `total_oportunidades`: 1770.
- Duas buscas no CRM: contatos CRIADOS na janela (`reimpactado=false`) e contatos ATUALIZADOS na janela que não foram criados nela (`reimpactado=true`). O GoHighLevel junta contato pelo e-mail: lead antigo que volta não cria contato novo, só atualiza o existente.
- Campos de cada contato: `customFields`, `dt_atualizacao_brt`, `dt_criacao_brt`, `email`, `id`, `nome`, `oportunidades`, `phone`, `primeira_atribuicao`, `reimpactado`, `source`, `tags`, `ultima_atribuicao`.
- `dt_criacao_brt` e `dt_atualizacao_brt` estão em horário de Brasília. `tags` são as etiquetas do contato no CRM (é onde o comercial marca `mql`, `q-mql`, `n-mql`). `customFields` vem como a API entrega.
- `primeira_atribuicao` (attributionSource do CRM) e `ultima_atribuicao` (lastAttributionSource): `campaign`, `campaignId`, `medium`, `mediumId`, `referrer`, `sessionSource`, `url`, `utmContent`, `utmMedium`, `utmSource`; `null` quando o CRM não tem rastro.
- `oportunidades` (só as do período, ligadas a contatos da lista): `estagio`, `fonte`, `funil`, `funil_valido`, `id`, `nome`, `status`, `valor`. `funil_valido=true` = um dos "Funil de Vendas" de `FUNIS_VALIDOS` no `pull_leads.py` (desde 19/10 inclui o Oficial); os demais funis da conta vêm com `false`.
- **Dados pessoais** (nome, e-mail, telefone): manter em canal privado.

### `analise/_disparos.json`

Origem: leitura manual do painel do Manychat no navegador (só leitura; o Manychat não tem API), feita no ritual.

- `_lido_em`: 2026-10-19 12:15 (última leitura do painel). `_fonte`: painel Manychat (app.manychat.com > Automacao), leitura manual — nao ha API. Atualizar a cada ritual.
- 129 palavras-chave. Chave = palavra do CTA em caixa alta. Campos: `campanha`, `cliques`, `ctr`, `disparos`, `estado`, `lido_em`, `palavra`, `post`, `utm`.
- `disparos` = execuções da automação no painel; `ctr` = porcentagem de clique no botão do DM como o painel mostra; `post` = pasta do post no registro desta máquina; `utm` = se o link do DM leva UTM; `lido_em` = data em que aquela chave foi lida pela última vez.
- Campos que só algumas chaves têm: `cliques` (cliques no botão, quando o painel mostrava o número), `campanha` (o utm_campaign do link), `estado` (situação da automação anotada na leitura), `palavra` (a palavra real, quando a chave leva sufixo de data para não colidir com outra).
- Chaves que começam com `_` são notas do arquivo: `_fonte`, `_lido_em`, `_nota_utm`.
- Quando a mesma palavra foi usada em mais de um post, a chave guarda a automação do post mais recente.
- Chaves por data de leitura: (sem lido_em): 7, 2026-09-14: 1, 2026-09-21: 7, 2026-10-16: 1, 2026-10-19: 61, 2026-10-20: 4, 2026-10-21: 3, 2026-10-23: 16, 2026-10-27: 2, 2026-10-30: 4, 2026-11-03: 1, 2026-11-09: 12, 2026-11-13: 10.

### `analise/_painel-manychat.csv`

Origem: histórico das leituras do painel do Manychat (uma linha por automação por leitura, com `lido_em`), feito no ritual; desde 19/10 é a régua de performance do post.

- 522 linhas, 45.7 KB. Última escrita: 2026-11-13 19:47.
- Saída do `pull` completo de 06/08/2026 (lista de mídia desde 2025-01-01, insights e comentários de cada post). Não muda mais.

### `analise/_painel-instagram.csv`

Origem: digitado à mão a partir de captura de tela do painel do Instagram (dado da conta, não vem da API).

- 2 linhas, uma por janela semanal da conta: 2026-08-15 a 2026-08-21; 2026-08-22 a 2026-08-28.
- Colunas: `janela_ini`, `janela_fim`, `visualizacoes`, `seguidores_liquidos`, `interacoes`, `visitas_perfil`, `toques_bio`, `visualizadores`, `capturado_em`.
- Digitado à mão a partir de captura de tela do painel do Instagram (são números da conta inteira, que a API por post não dá).

### `analise/_update.log`

Origem: saída do agendamento do macOS `com.tatsuo.ig-update`, que roda `pull_insights.py update` às 9h, 14h, 20h e no boot.

- 51142 linhas, 3.7 MB. Última escrita: 2026-11-15 11:44.
- Acumula a saída de todas as rodadas do agendamento, sem data por rodada. Cada rodada lista os posts da janela de 30 dias (data, tipo, reach, comentários, novo/atualizado), fecha com "Base atualizada: N posts" e a linha do snapshot do dia.
- Erros de rede e de API aparecem aqui como o Python imprime (ex. falha de DNS quando o Mac está sem internet).

### `analise/_pull.log`

Origem: saída do único `pull_insights.py pull` completo (06/08/2026), que montou a base.

- 3439 linhas, 115.2 KB. Última escrita: 2026-08-06 11:30.
- Saída do `pull` completo de 06/08/2026 (lista de mídia desde 2025-01-01, insights e comentários de cada post). Não muda mais.

### `analise/registro-posts-factual.csv`

Origem: recorte de `conteudo/analise/registro-posts.csv` (fichas da skill /etiqueta), só colunas factuais.

- 225 fichas (uma por post produzido na máquina principal, gravadas pela skill /etiqueta). 206 com `post_id`; 221 com `data_publicacao` (de 2026-08-18 a 2026-11-13).
- Colunas (só as factuais do registro-posts.csv): `data`, `data_publicacao`, `post_id`, `pasta`, `formato`, `semente`, `pilar`, `funil`, `objetivo`, `palavra_chave`.
- `data` = dia da ficha; `data_publicacao` = dia em que foi ao ar; `post_id` = id da mídia na API (vazio enquanto não foi casado com o post); `pasta` = conteudo/carrosseis/<pasta> na máquina principal; `formato` = carrossel, frase ou reel; `semente` = de onde veio a ideia; `pilar` = Lucratividade, Crescimento ou Cultura; `funil` = campo aposentado em 31/08/2026 (vazio desde então); `objetivo` = lead, seguidor ou alcance, declarado na criação; `palavra_chave` = palavra do CTA de comentário (vazio quando o post não tem).
- As outras colunas do registro original (previsão, faixa, justificativa, resultados, nervo, consciência da dor, mecanismo, roupa) ficaram de fora: são análise da máquina principal.

## Textos dos posts publicados de 2026-11-01 a 2026-11-15

Para cada ficha do registro com `data_publicacao` nessa janela, vêm os arquivos `carousel-text.md` (texto dos slides, legenda e as notas de produção, como estão na pasta do post) e `legenda.txt` (quando a pasta tem esse arquivo). Na importação vão para `conteudo/carrosseis/_da-maquina-do-user/<pasta>/`.

Única alteração: no `carousel-text.md`, a linha que começa com "Etiqueta:" (a previsão de desempenho gravada pela /etiqueta) é retirada, porque previsão é análise da máquina principal. A última coluna diz quantas linhas saíram de cada arquivo. O resto vai literal.

| Pasta | Publicado em | Formato | post_id | Arquivos | Linhas retiradas |
|---|---|---|---|---|---|
| `281_dre-cobrando-caro-repost` | 2026-11-05 | carrossel | 18116146445119507 | carousel-text.md, legenda.txt | 0 |
| `282_nem-deus-da-jeito-repost` | 2026-11-06 | carrossel | 17989293785886155 | carousel-text.md, legenda.txt | 0 |
| `283_peso-de-quem-comanda-repost` | 2026-11-07 | carrossel | 18136403549499464 | carousel-text.md, legenda.txt | 0 |
| `284_previsibilidade-repost` | 2026-11-08 | carrossel | 18169073233490553 | carousel-text.md, legenda.txt | 0 |
| `285_gente-boa-empregada-repost` | 2026-11-09 | carrossel | 17941457016380854 | carousel-text.md, legenda.txt | 0 |
| `288_preso-operacional-repost` | 2026-11-10 | carrossel | 17951629257343525 | carousel-text.md, legenda.txt | 0 |
| `286_empresa-igreja-repost` | 2026-11-11 | carrossel | 18643529539063957 | carousel-text.md, legenda.txt | 0 |
| `289_quebrar-sorrindo-repost` | 2026-11-12 | carrossel | 17896025148683768 | carousel-text.md, legenda.txt | 0 |
| `290_dois-tipos-de-funcionario-repost` | 2026-11-12 | carrossel | 17983833470912304 | carousel-text.md, legenda.txt | 0 |
| `287_parou-de-olhar-repost` | 2026-11-13 | carrossel | 17917631379538274 | carousel-text.md, legenda.txt | 0 |
| `294_risco-de-dono-repost` | 2026-11-13 | carrossel | 18144571876613764 | carousel-text.md, legenda.txt | 0 |

## O que não vem no pacote

- Token, chave e credencial de qualquer API (ficam só na máquina principal).
- A análise da máquina principal: as colunas de previsão e resultado do registro, `hipoteses.md`, os briefings do ritual, as listas de exceção (`_descartados.csv`, `_ressalvas.csv`, `_cauda-longa.csv`), `manychat-baseline.md` e relatórios.
- Imagens (os PNGs dos posts ficam no Google Drive).

## Integridade

`checksums.txt` tem o sha256 de todos os arquivos do pacote, inclusive este manifesto e o `pacote.json` (só não de si mesmo).
