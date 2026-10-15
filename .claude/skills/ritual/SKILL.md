---
name: ritual
description: Roda o ritual diário da máquina de análise do Instagram — lê os dados atualizados, lê os posts em D+3 (provisório) e fecha os de D+7 (oficial), compara previsão × realidade, atualiza o placar e devolve o briefing estratégico do dia. Às segundas roda a versão semanal consolidada. Use quando o usuário disser /ritual, "roda o ritual", "análise do dia".
---

# /ritual — o batimento diário da máquina de análise

## Onde roda a coleta (duas máquinas)
A coleta (API do Instagram, CRM GoHighLevel e painel do Manychat) roda **só na máquina principal**: a que tem o token em `~/.tatsuo/ig-token.json` e o agendamento `com.tatsuo.ig-update`. A API da Meta não pode rodar em duas máquinas. Na máquina que recebe o pacote diário (a do João), nada de `update`, `pull`, `pull_leads.py` ou painel do Manychat: o primeiro passo é importar o pacote do dia (`python3 scripts/pacote/importar_pacote.py <zip>`, ver `scripts/pacote/README.md`) e o resto do ritual segue igual, com os dados importados. Se o pacote do dia não chegou, dizer no briefing qual foi o último importado (`conteudo/analise/_pacotes-importados.log`).

## Preparação
1. Conferir o frescor do dado: `conteudo/analise/desempenho.json` → campo `pulled_at`. Se tiver mais de 24h, rodar **SÓ** `python3 scripts/instagram/pull_insights.py update` antes de tudo e avisar que o agendamento falhou. **NUNCA o comando `pull`**: ele varre todos os posts de uma vez, dispara o anti-abuso da Meta e bloqueia a API por dias. O launchd (`com.tatsuo.ig-update`) dispara às 9h, 14h e 20h **e** no boot — se mesmo assim o dado estiver velho, o Mac passou o dia desligado. (Na máquina que recebe o pacote, este passo é a importação do pacote do dia; ver o topo.)
2. **Validar o registro ANTES de ler qualquer coisa, e de novo depois de mexer nele**: `python3 scripts/instagram/validar_registro.py` (zero API). Outras sessões escrevem no mesmo CSV; ficha corrompida ou de regime misturado entra no placar como se fosse dado bom. Erro acusado se corrige antes de seguir.
3. Ler `conteudo/analise/registro-posts.csv` (fichas + previsões) e `conteudo/analise/hipoteses.md`.
4. **As ferramentas da máquina, na ordem.** Todas com zero chamada de API — leem só o disco. Não montar à mão o que o script já monta:
   - `python3 scripts/instagram/reguas.py` — bandas vigentes por formato: o **DADO FINAL** (comentários absolutos em D+7; shares na frase), que fecha o placar, e a **ESTIMATIVA** (taxa por mil), que dá o norte até D+4 e explica o erro no fechamento (e as PRIORIDADES de métrica por `objetivo`)
   - `python3 scripts/analise/tabelas_ritual.py [dias]` — as três tabelas do ritual: trackeamento/leads · carrossel e reel · frase. É aqui que os arquivos de exceção aparecem marcados
   - `python3 scripts/analise/briefing_pdf.py --texto conteudo/analise/_briefing_texto.md` — relatório em PDF. Só na segunda ou quando o user pedir; é o único que tem dependência externa (playwright do `node_modules`)
5. **Os dois arquivos de exceção — ler antes de concluir qualquer coisa:**
   - `_descartados.csv`: o post sai da conta INTEIRO (republicação que morreu, duplicata do mesmo dia). Some das medianas.
   - `_ressalvas.csv`: o post CONTA, mas com UMA dimensão inválida (coluna `escopo`: `lead` · `taxa` · `alcance`). O número está certo; o que não vale é comparar aquele escopo com o dos outros posts. As tabelas marcam a linha com `!` e listam o motivo no rodapé. Criado em 31/08 pelo caso do carrossel 72, que ficou ~17h no ar sem automação: taxa válida, leitura de lead contaminada.

## Ritual diário (qualquer dia)
1. **Leitura provisória em D+3**: posts publicados há 3+ dias. Serve pra decidir o que fazer **amanhã** (repito a veia ou troco?). Fica no briefing, **não** fecha placar e **não** entra no CSV. **Lê-se pela TAXA, e a taxa aqui é estimativa** (regra do user, 14/09: *"as primeiras taxas dos posts são mais para dar um norte do que para atestar a eficiência dele"*): ela diz se a peça está pegando em quem viu antes de o alcance se decidir. Norte, nunca atestado; nenhuma frase do briefing pode afirmar que um post "funcionou" antes do comentário de D+7.
1b. **Fechamento em D+7 — o número oficial**: post publicado há 7 dias fecha a ficha e conta no placar. Casar com o post da API (por data + legenda/pasta). **Os comentários de D+7 vêm sempre do `_snapshots.csv`** (`idade_dias<=7`, a foto mais velha), nunca do total de hoje.
   **Dois defeitos conhecidos (achados em 30/09), tratar assim:**
   - O `tabelas_ritual.py` não casa ficha com post quando há mais de um carrossel no mesmo dia e a legenda do `carousel-text.md` está dentro de bloco de código (```): ele lê a linha "```" e desiste, e a ficha some da tabela. Ficha que devia aparecer e não aparece: casar à mão (mesma data de publicação, mesmo tipo de mídia, 1ª linha real da legenda contra o caption do post) e gravar o `post_id` na ficha. Não editar o script (correção pendente de aprovação do user).
   - Ficha cujo post foi apagado do Instagram (caso do `158_mbv-dia-2-vender`, apagado em 27/09): NÃO fechar com o número de outro post do mesmo dia. Deixar aberta e listar em "Preciso de você".
   *Por que não D+3* (medido 27/08, n=16 posts com as duas leituras): de D+3 pra D+7 os posts FORTES crescem +14,9% em shares e os FRACOS só +4,1% — e a taxa dos fortes fica parada enquanto a dos fracos cai 8,7%. Medir em D+3 **comprime a distância entre post bom e post ruim**, que é exatamente o sinal que calibra a máquina.
1c. **Cauda longa**: post ainda crescendo >15% em D+7 ganha etiqueta de cauda longa e volta pra uma terceira leitura em **D+30** (a janela de snapshot cobre 30 dias).
2. **Placar** (só nos fechados em D+7) — **desde 14/09 o placar fecha no DADO FINAL: comentários absolutos em D+7** (compartilhamentos na frase), lidos na foto de D+7 do `_snapshots.csv` (`idade_dias<=7`, a mais velha), nunca no total de hoje de um post de 20 dias. Rodar `python3 scripts/instagram/reguas.py` (zero API) e preencher no CSV: `resultado_com` (**é este que pontua**: comentários em D+7; na frase, shares em D+7), `resultado_taxa` (a estimativa realizada: interações/1k ou shares/1k, registrada pra explicar o erro, **não pontua**), `resultado_alcance` (o realizado; **não pontua** — alcance não é previsível, medido em 27/08) e `resultado_vs_previsao` (`acertou`/`errou-pra-cima`/`errou-pra-baixo`, comparando o DADO FINAL contra as bandas do absoluto da régua viva).
   **Três regimes, nunca misturados no placar:** (1) até 26/08, absoluto contra régua fixa (marcadas "regime antigo" na faixa); (2) 27/08 a 13/09, taxa contra terços vivos; (3) desde 14/09, comentários em D+7 contra terços vivos de posts maturados. Cada um se conta separado; o regime 3 começa com 0 casos, então por um bom tempo a resposta honesta sobre a competência da máquina é "ainda não dá pra dizer". Ficha do regime 2 que fechar de 14/09 em diante fecha na régua dela (taxa) e entra no placar do regime 2, não do 3.
   **O papel da taxa no fechamento é explicar, não pontuar.** Ao ler um resultado ruim, separar as duas causas: taxa baixa = o conteúdo não pegou. Taxa boa com comentário baixo = o conteúdo pegou em quem viu, e viu pouca gente. São diagnósticos opostos e pedem ações opostas, e é por isso que a taxa continua gravada ao lado.
   **Ficha sem previsão** (retroativa, escrita depois do resultado estar na tela) fecha com `resultado_vs_previsao = nao-pontua`: registra os números, fica fora do placar. Sem isso ela aparece como "fecha hoje" pra sempre.
   *O campo `funil` foi APOSENTADO em 31/08 — não preencher. Ele pedia leitura depois do fato, nenhum script consumiu, e `objetivo` responde melhor a mesma pergunta, declarado antes.*
2b. **Sincronizar o banco de frases** — `python3 scripts/analise/sync_banco_frases.py` (zero API; `--dry-run` pra só ver). Lê o registro e reescreve o status no cabeçalho de cada frase com semente `banco-N`: ficha com data de publicação vira `publicada (post P, DATA)`; ficha fechada em D+7 ganha ` — FECHADA D+7: taxa · alcance · vs previsão`. Status que já tem "FECHADA" nunca é tocado. *Criado em 08/09 porque o banco ficou dizendo "produzida — aguardando publicação" pra 66, 80, 84 e 85 uma semana depois de estarem no ar: o ritual atualizava registro e base, e ninguém atualizava o banco. Rodar todo dia, depois do fechamento do placar.*
2c. **Trackeamento de leads — TODO DIA, não só na segunda** (regra do user, 02/10: a tabela de leads sai preenchida todo dia). É ela que mede a meta do orgânico: **125 MQL por semana**. A coleta abaixo (CRM e Manychat) é só da máquina principal; na que recebe o pacote, `leads.json` e `_disparos.json` chegam nele e o resto do passo (a leitura) é igual.
   - **CRM (GoHighLevel):** `python3 scripts/ghl/pull_leads.py update` (janela padrão 35 dias; credenciais em `~/.config/tatsuo/ghl.env`, NUNCA no Git) e ler `conteudo/analise/leads.json`:
     - **Inscrições por post**: contar contatos pela campanha — novos (`reimpactado=false`) pela `primeira_atribuicao.campaign`, reimpactados (`reimpactado=true`) pela `ultima_atribuicao.campaign`. O GHL deduplica por e-mail: lead antigo que volta por post novo NÃO cria contato — o rastro do post cai na última atribuição (validado 25/08 no teste ponta-a-ponta do reel CULTURA). O `utm_campaign` é a palavra única do post; casar com `palavra_chave` do registro e reportar novos × reimpactados separados (reimpacto conta pro post, mas não é inscrição nova).
     - **Qualidade por post**: das oportunidades de cada contato (só `funil_valido=true` — a conta tem funis de teste que inflam número), reportar estágio do pipeline E a qualificação do comercial, que vive nas TAGS do contato: `mql` / `q-mql` / `n-mql` (ex.: "imersãombv - julho/2026, n-mql"). Post que gera MQL vale mais que post que só gera clique. Planilha-espelho pra conferência humana (somente leitura, perfil Chrome Tatsuo Academy): docs.google.com/spreadsheets/d/1CJJ5v_SOFZ59EBCStl9N19ZwQUF0itAYtiF9Rv6Mn5U
     - Reportar também o % de contatos SEM rastro (`utmSource` vazio) — é o termômetro de quanto do orgânico ainda escapa da atribuição.
     - Cuidado com volume: contato ≠ oportunidade (Manychat cria contato pra interação de DM); pra placar de negócio, a régua são as oportunidades em funil válido.
   - **Manychat (só leitura; não tem API):** carregar as ferramentas do Chrome (`mcp__claude-in-chrome__*`) e chamar `list_connected_browsers`. Só seguir se houver um navegador marcado `inUse` E `onThisComputer`. NUNCA usar `select_browser` nem `switch_browser` em outro navegador (a conta é compartilhada e a lista tem máquinas de colegas). Abrir https://app.manychat.com/fb2015128/cms?path=/&field=modified&order=desc e conferir no screenshot o avatar laranja "T" da conta Tatsuo no canto inferior esquerdo; sem ele, parar a leitura. Caiu na tela de login: NÃO tentar logar, pular e avisar. Ler, sem clicar em Editar/Ativar/Interromper/Apagar nem alterar nada, as execuções e o CTR das automações `IG | AAAA-MM-DD | PALAVRA | tema` dos posts dos últimos 14 dias. Montar ou mexer em automação não é coisa do ritual: isso vive na conversa do post.
   - **Gravar em `conteudo/analise/_disparos.json`**, no formato existente: chave = PALAVRA em caixa alta, valor `{"disparos": N, "ctr": "x%", "post": "<pasta do registro>", "utm": true, "lido_em": "AAAA-MM-DD"}`. Palavra repetida em posts diferentes (ex.: RAIO-X nos posts 127, 147 e 164): a chave fica com o post mais recente e os números dos outros vão no briefing. Leads clicados ≈ execuções × CTR; processo e baseline em `conteudo/analise/manychat-baseline.md`.
   - Sem navegador utilizável: pular o Manychat e dizer isso no briefing (com o user na conversa, dá pra pedir print do painel). O CRM segue normalmente.
3. **Snapshot de decaimento — NÃO É MAIS MANUAL.** O `pull_insights.py` grava o `_snapshots.csv` sozinho ao fim de todo `update` (janela de 30 dias, zero chamada de API, idempotente). *Antes disso era apendado à mão aqui, e por isso faltavam 22, 23 e 25/08 — os dias em que ninguém rodou o ritual.* O que o ritual faz agora é só **conferir**: se a saída do script listou BURACOS, avisar no briefing. Dia sem foto **não é recuperável pela API** (os valores são acumulados de vida) — só de um `desempenho.json` commitado naquele dia. Rede de segurança sem custo: `python3 scripts/instagram/pull_insights.py snapshot`.
4. **Briefing do dia** — ver a seção "Como o briefing é entregue" abaixo. Três blocos curtos, nessa ordem: **Decisões**, **Placar**, **Preciso de você**, e depois a seção separada de **Trackeamento de leads**. O resto fica calculado e guardado, pronto pra abrir se ele pedir.
5. **Fechamento do dia** — pacote do João e Git (seção "Fechamento do dia" abaixo).

## Ritual de segunda-feira (substitui o diário)
Tudo do diário, mais:
1. Re-ranquear a semana: todos os posts dos últimos 7 dias vs medianas por formato (carrossel / frase / reel separados)
1b. **Conciliação de calendário (ClickUp × API)** — frequência de publicação NUNCA sai só da API; a régua é o calendário do ClickUp (integração conectada; lista "HÉLIO TATSUO", id 901306431219, visualização usada pelo user é a de calendário). Via `clickup_filter_tasks` (due_date na semana, include_closed): contar **planejado × concluído × publicado** por natureza do slot (FRASE 9h · CORTE 11/14/16/18h · CAIXINHA 12h · CARROSSEL 13/17h · NOTÍCIA 19h · PRODUZIDO · LIVE). Notas: caixinha É um reel (formato de conteúdo, não story — aparece na API); status "ideias" = não concluído. Reportar taxa de execução (concluído/planejado) e os furos NOMEADOS dos dois lados: tarefa concluída sem post na API (marcou e não postou) e post na API sem tarefa (saiu fora do calendário). Validação de 24/08: 54 planejadas, 44 concluídas = 44 publicadas (batimento perfeito; furos da semana: caixinha e notícia).
2. Revisar `hipoteses.md` inteira: algum status muda? Alguma hipótese nova nasceu da semana?
3. Definir **o teste da semana**: uma aposta deliberada (com previsão escrita) pra hipótese 🟡 mais quente
4. Placar acumulado da máquina: % de acerto das previsões até hoje
5. **Leads da semana**: o trackeamento diário (passo 2c) consolidado nos 7 dias: disparos e CTR das automações da semana, novos × reimpactados e MQL / Q-MQL / N-MQL por post, contra a meta de 125 MQL por semana.

## Como o briefing é entregue (regra do user, 27/08)

O user **não quer aprender análise de dados**. Nas palavras dele: "o especialista de análise de dados é você e eu não preciso saber nada sobre dados, só preciso saber das hipóteses e se eu não concordar aí sim você abre as métricas para defender sua decisão."

Então o briefing é **pirâmide invertida, com dobra**:

1. **Decisões** — o que muda hoje, no imperativo. Máximo 5 linhas.
2. **Placar** — UMA linha: acertei ou errei o que previ, e como está a calibração acumulada. **Inegociável, mesmo no dia mais vazio.** É o recibo que permite ao user delegar a leitura dos dados sem voar cego: no dia em que o acerto desabar, ele vê na hora, sem precisar entender de estatística. Ritual curto sem placar vira carimbo.
3. **Preciso de você** — só o que é decisão dele. Se não tiver nada, escrever "nada".

Depois dos três blocos, numa seção SEPARADA (trackeamento não é performance), o **Trackeamento de leads**: a tabela 1 do `tabelas_ritual.py` (post, data de publicação, palavra, disparos, CTR, leads novos e reimpactados, qualificação MQL/Q/N). Sai todo dia, mesmo que a resposta seja "zero lead". É a leitura da meta do orgânico: 125 MQL por semana.

**Data de publicação em toda linha de post** (regra do user, 27/08), no formato `50_vendedor-estrela (carrossel) 24/08`: no placar, nas decisões, no trackeamento e em qualquer menção a post. Sem a data ele não casa o post com o que aconteceu no calendário naquele dia.

Salvar o briefing completo e o detalhe calculado em `conteudo/analise/ritual-AAAA-MM-DD.md` (data de hoje, horário de Brasília).

Tabela, teste, n, p, delta, faixa: continuam sendo **calculados igual** e ficam prontos pra abrir — só não são mostrados. Ele pede, você abre.

**Nunca citar código de hipótese** (`H11`, `H14`…) no briefing, na ficha ou em conversa. Usar o nome curto entre aspas ("o espelho", "o mapa 1:1") ou, melhor, dizer a regra inteira numa frase que se explica sozinha. Ninguém deveria precisar consultar o `hipoteses.md` pra entender uma decisão. Motivo dele: "fica difícil até mesmo para mim lembrar qual é, imagina para quem assumir o bastão."

**Quando levantar a mão sem ser perguntado** — são as três exceções que fazem a delegação funcionar:
- **sua leitura mudou** (uma regra que você vinha usando não se sustenta mais no dado);
- **seu placar quebrou** (sequência de erros, ou viés direcional novo);
- **um dado contrariou uma hipótese**.

Fora esses três, silêncio quer dizer que está rodando.

## Fechamento do dia (depois do briefing)
1. **Pacote do João (só na máquina principal):** `python3 scripts/pacote/gerar_pacote.py`. Empacota, sem chamar API e sem interpretar nada, os dados brutos do dia (Instagram, CRM, Manychat, logs, o registro só com as colunas factuais e os textos dos posts dos últimos 14 dias) em `~/Desktop/pacote-analytics-joao/pacote-AAAA-MM-DD.zip`. Citar o caminho do zip no relatório final. O que vai dentro está em `scripts/pacote/README.md`.
2. **Git:** commit conforme a regra de commit da máquina (CLAUDE.md), só com os arquivos de `conteudo/analise/` que o ritual tocou (`registro-posts.csv`, `_disparos.json`, `ritual-AAAA-MM-DD.md`) e `conteudo/banco-frases.md` se o sync mexeu. O `leads.json` fica fora do Git (dado pessoal; está no `.gitignore`).

## Camada estatística (regras de método — pedido do user, 24/08)
- **Comparação entre grupos** (pilar, roupa, consciência da dor, etc.): Mann-Whitney U com correção de empates + **Cliff's delta** como tamanho de efeito — nunca t de Student (métricas de social são cauda-longa; normalidade não existe aqui). Relatar sempre n e p; grupo com n<5 é "sinal fraco", nunca conclusão.
- **Taxa por alcance junto do absoluto** (com/1k, shares/1k, saved/1k): separa qualidade do conteúdo de circulação do algoritmo. Conclusão só é forte quando absoluto E taxa apontam na mesma direção.
- **Previsão numérica** (fichas com `previsao_faixa`, desde 24/08): no placar do maturado registrar também o erro percentual vs o ponto médio da faixa e se o real caiu DENTRO da faixa. Meta de calibração: ~80% dos reais dentro da faixa — acima disso as faixas estão largas demais (não informam), muito abaixo estão estreitas demais (excesso de confiança).
- **Calibração da máquina** (toda segunda): placar acumulado de previsões + direção dos erros (teste de sinal binomial) + % de reais dentro da faixa. Viés direcional detectado (ex.: todos os erros pra baixo) → propor ajuste na regra de previsão da /etiqueta, citando o dado.
- **Decaimento**: a janela de snapshot é de **30 dias** (era 7 até 27/08). Quando houver ≥14 dias de fotos, ajustar a curva de vida (mediana da fração do total em D+1/D+3/D+7/D+30 por formato) e usá-la pra projetar posts não maturados — projeção sempre rotulada como projeção. **Gravar todo dia é barato; relatar todo dia é caro** — a curva fina fica guardada, o briefing só fala nos marcos D+3, D+7 e D+30.
- Ambiente sem numpy/scipy: implementar os testes em python puro (aproximação normal com correção de empates), como no ritual de 24/08.
- Sinceridade metodológica: resultado que contraria hipótese ou doutrina entra no briefing do mesmo jeito; classificação suja ou n pequeno é declarado, não escondido.

## Regras
- Nunca editar skills, carrosséis ou os bancos de scouting; o ritual só escreve em `conteudo/analise/`, no status dos cabeçalhos de `conteudo/banco-frases.md` via `sync_banco_frases.py` (autorizado pelo user em 08/09) e no pacote do dia (`~/Desktop/pacote-analytics-joao/`, máquina principal) ou na importação dele (`conteudo/carrosseis/_da-maquina-do-user/`, máquina que recebe).
- Manychat no ritual é só leitura. Não criar post, automação, tarefa no ClickUp nem mandar mensagem a ninguém.
- Não escrever no `_snapshots.csv` à mão: quem grava é o `pull_insights.py`.
- Comentário conta tudo (lead + opinião) — lembrar dessa limitação ao interpretar até a camada Manychat existir.
- Tom do briefing: parceiro estratégico, não relatório burocrático. Se não houve nada maturado no dia, dizer em 2 linhas e não inventar conteúdo.
