# Manychat — baseline extraída em 18/08/2026 (leitura via painel)

> Fonte: app.manychat.com → Automação → Minhas automações (conta Tatsuo, 11.792 contatos).
> Execuções = quantas vezes a palavra-chave disparou (≈ comentários de CTA capturados).
> CTR = % dos capturados que clicaram no link do DM (≈ lead qualificado).

## Os dois canos GLOBAIS (qualquer publicação — sem atribuição por post)
| Automação | Palavra | Execuções | CTR |
|---|---|---|---|
| "307" | 307 | **5.452** | 50% |
| "Comando!! MBV" | comando | **4.889** | 58% |

→ ~10,3 mil disparos somados; a ~50–58% de CTR, **≈ 5,5 mil leads clicados** vieram desses dois canos. Mas por serem "qualquer publicação", NÃO dá pra saber qual post gerou o quê. É exatamente o problema que a palavra única por post resolve.

## Automações POR POST ESPECÍFICO (atribuição perfeita — o modelo a seguir)
| Automação | Palavra | Execuções | CTR |
|---|---|---|---|
| Cultura MBV especifico | cultura | **444** | 46,4% |
| Comando!! MBV copy | lucro | 164 | 47,6% |
| roteiro copy 2 | diagnóstico | 34 | 55,9% |
| Pavão, caixa copy | comando | 28 | 42,9% |
| Pavão, caixa | caixa | 14 | 28,6% |
| roteiro copy 3 | preparo | 2 | 50% |
| IG 31/07 TARTARUGA | tartaruga | baixo | 50% |
| IG 31/07 MARGEM (global) | margem | baixo | 7,7% |
| demais (PATRIMÔNIO, PERFIL, GENTE, porta-pra-dentro…) | várias | 0–baixo | — |

## Descobertas
1. **A equipe já usa automação por post específico** (inclusive um padrão de nome bom: "IG | data | PALAVRA | tema") — o que falta é CONSISTÊNCIA e casar com o registro da máquina.
2. **Validação do proxy comentário≈lead em post de CTA:** o post do pavão teve 32 comentários (API) e a automação disparou 28 vezes → **~87% dos comentários eram a palavra-chave**. Em post com CTA, comentário É lead em ~9 de cada 10 casos.
3. **CTR do DM é consistente (~43–58%)** → regra de bolso: **leads clicados ≈ metade dos comentários de CTA**.
4. Variantes de digitação importam: automações boas já cadastram 3–4 formas (CAIXA/Caixa/caixa). A palavra da /etiqueta deve sempre ser cadastrada com as variantes.

## Processo daqui pra frente (fecha o elo lead por post) — atualizado 19/08 após teste operado pelo Claude
**Teste validado:** Claude consegue operar o Manychat via navegador (duplicar → renomear → trocar palavra → salvar → ativar). Automação-teste "teste claude" (palavra claudinho, post do pavão) criada e ativada em 19/08 — o usuário desativa/apaga depois.

**REGRA FIXA (decisão do usuário, 19/08): toda automação nova é "publicação ou Reel ESPECÍFICO" — nunca "qualquer publicação".** Motivo: palavra temática em gatilho global dispara DM em quem comenta a palavra por acaso num post de opinião ("broxa o público") e destrói a atribuição. Evidência: automações globais de palavra temática têm CTR baixo (MARGEM global: 7,7%) vs específicas (43–58%). As duas globais legadas (307, comando) ficam como estão por ora — servem os posts antigos.

**Fluxo operacional (o post é publicado À MÃO pelo usuário — a música importa):**
1. Carrossel pronto → `/etiqueta` gera palavra única + mensagem da DM + texto do botão (alinhados ao tema).
2. Usuário publica no Instagram (escolhe a música) e **avisa o Claude: "postei o [nome], cria o Manychat"**.
3. Claude cria via navegador: duplica o modelo mais recente (o único lote que já sai com UTM) → nome "IG | AAAA-MM-DD | PALAVRA | tema" → palavra + variantes (minúscula/Capitalizada/CAIXA ALTA, sem acento) → seleciona o POST ESPECÍFICO recém-publicado → edita mensagem da DM + botão → **troca o `utm_campaign` do link** → **põe o `utm_content` com o link limpo do post** → ativa → confirma com print.

**PADRÃO DO UTM (decisão do usuário, 27/08/2026): `utm_campaign=AAAA-MM-DD-PALAVRA`** — ex: `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-08-27-LUCRO`. O valor é o mesmo identificador do nome da automação.

**`utm_content` = LINK DO POST (decisão do usuário, 29/09/2026).** Todo link de DM passa a levar, no fim, `&utm_content=` + o link do post no Instagram. Ex: `https://tatsuoacademy.com/raio-x-empresa-lucrativa/?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-28-RAIO-X&utm_content=https://www.instagram.com/p/Dd2NwlQkfrQ/`. Motivo: o CRM joga o `utm_content` num campo próprio do card do lead, e o SDR abre o post de onde o lead veio antes de falar com ele. O `utm_campaign` continua sendo o identificador que o `/ritual` lê; o `utm_content` só acrescenta.
- **Link limpo:** só `https://www.instagram.com/p/CODIGO/` (carrossel/foto) ou `https://www.instagram.com/reel/CODIGO/` (Reel), com a barra final. Nunca o `?igsh=...` do "copiar link" do app: um `?` ou `&` a mais quebra o link inteiro.
- **Quando entra:** o link do post só existe depois da publicação. A automação continua sendo montada STOPPED com o link sem `utm_content`; ele entra no mesmo passo em que o post é amarrado, antes do Ativar. Fonte do código do post: o permalink no preview/grade do easy-builder, ou o `desempenho.json` do dia.
- **Diferente do `utm_campaign`, acrescentar `utm_content` numa automação que já rodou é seguro**: o campaign não muda, então a atribuição não se parte. Só um lead que tenha clicado antes chega sem o link.
- **Retroativo (29/09):** aplicado nas automações dos 7 dias anteriores (22 a 28/09); ver a seção de 29/09 no fim do arquivo.

Por que mudou: até 26/08 o `utm_campaign` carregava só a PALAVRA (`...&utm_campaign=PATRAO`). Como toda automação nova é por post específico, o Manychat já separa as execuções por post mesmo com palavra repetida — mas o CRM não separava: duas automações vivas com a mesma palavra e as duas com UTM cairiam no mesmo balde. Com data+palavra o identificador é único por construção, e **a palavra do CTA fica livre pra repetir** (regra de "palavra única por post" da `/etiqueta` foi aposentada na mesma data).

Primeira automação no padrão novo: `IG | 2026-08-27 | LUCRO | casas bahia noticia` (nasceu com `utm_campaign=LUCRO` e foi corrigida no mesmo dia, com 0 disparos e 0 cliques — trocar UTM depois de o link já ter sido clicado parte a atribuição do mesmo post em dois valores no CRM, então **UTM só se troca enquanto os cliques estiverem zerados**). As automações de 21–26/08 (SONHO, CULTURA, PILOTO, PATRAO) ficam com o UTM só-palavra: já rodaram e não se mexe.

Segunda no padrão novo: `IG | 2026-08-27 | LEVE | solidao da presidencia` (carrossel 60, `utm_campaign=2026-08-27-LEVE`, palavra LEVE/leve/Leve, post específico, criada e ativada pelo Claude ~5 min depois da publicação). **Pegadinha operacional nova:** o campo de texto da DM no easy-builder come caracteres quando o texto entra de uma vez — "dono" virou "doo" em duas tentativas seguidas, sempre na mesma posição. Digitar em pedaços não resolveu; o que resolveu foi selecionar a palavra com duplo clique e digitar letra por letra. **Sempre conferir a mensagem no zoom antes de salvar** — o preview do celular à direita mostra o texto final e serve de segunda checagem.

Terceira no padrão novo: `IG | 2026-08-27 | DONO | come antes de voce` (carrossel 64, `utm_campaign=2026-08-27-DONO`, palavra DONO/dono/Dono, post específico, criada e ativada pelo Claude logo após a publicação). **O bug de comer caractere no campo da DM se repetiu e agora está confirmado como recorrente, não como acaso:** "mostro" virou "mstro" ao colar o texto de uma vez, exatamente como "dono" virou "doo" na LEVE. O conserto que funciona segue o mesmo: **duplo clique na palavra errada e digitar letra por letra** (uma ação de digitação por caractere). Rotina que passou a valer: depois de escrever a DM, **dar zoom no campo e ler a frase inteira palavra por palavra antes de salvar** — foi o zoom que pegou o erro nas duas vezes; o preview do celular à direita mostra o texto final e serve de segunda checagem. O mesmo cuidado vale pro campo do LINK: conferir o começo (tecla Home), o meio (setas) e o fim, porque um caractere comido no meio do UTM quebra a atribuição em silêncio.

Quarta no padrão novo: `IG | 2026-08-28 | VENDA | um setor so` (carrossel 61, `utm_campaign=2026-08-28-VENDA`, palavra VENDA/venda/Venda, post específico, criada e ativada pelo Claude ~30 min depois da publicação de 28/08 17h05). Modelo duplicado: a `IG | 2026-08-28 | FOLGA | dois cansacos`, que já nascia no padrão de UTM novo — como a data é a mesma, só os 5 últimos caracteres do `utm_campaign` mudaram (FOLGA → VENDA). Primeiro caso de **palavra repetível na prática sem risco**: nada colide porque as duas são por post específico e os UTM diferem.

Quinta no padrão novo: `IG | 2026-08-29 | RESPEITO | concurso de popularidade` (carrossel 68, `utm_campaign=2026-08-29-RESPEITO`, palavra RESPEITO/respeito/Respeito, post específico, DM "Time não segue quem quer agradar. Quer ver como se constrói o rumo que faz eles te levarem a sério?" com botão `>> Quero ver <<`). Modelo duplicado: a `IG | 2026-08-29 | FIRME | perna que falta` (mesma data, então só a última palavra do UTM mudou).

**Primeiro caso de automação MONTADA ANTES da publicação.** O user avisou que o post estava agendado pras 17h e pediu tudo pronto pra ativar sozinho na hora. O que funcionou: duplicar, renomear, trocar palavra, DM e UTM com o post **ainda apontando pro post do modelo**, salvar e deixar **STOPPED**. Nada dispara enquanto está parada, então não há risco de a automação nova responder no post do modelo. Às 17h02 um timer de shell (`until [ "$(date +%H%M)" -ge 1702 ]`) acordou o Claude; o post novo já aparecia em primeiro na grade do easy-builder — **a própria grade serve de confirmação de que o post está no ar, sem tocar na API do Instagram**. Selecionar o post, conferir que o UTM sobreviveu, Atualização e Ativar: LIVE às 17h04, quatro minutos depois da publicação. `caffeinate -dimsu` ligado antes, pra o Mac não dormir (a lição de 21/08).

**O bug de comer caractere bateu pela QUARTA vez**, e a receita determinística resolveu de primeira de novo: "se constrói" saiu como "s constrói" ao escrever a DM de uma vez. Corrigido com `cmd+Up` + `Right` × 49 (offset contado fora do navegador) + digitar o "e". Quatro ocorrências em quatro automações seguidas (LEVE, DONO, VENDA, RESPEITO) — **assumir que vai acontecer sempre** e já entrar no campo esperando conferir. O zoom antes de salvar segue sendo o que pega o erro.

**O bug de comer caractere bateu pela TERCEIRA vez — e o conserto por duplo clique FALHOU.** Em 28/08 "vende" virou "vend" ao escrever a DM de uma vez (mesmo padrão de "dono"→"doo" na LEVE e "mostro"→"mstro" na DONO). A receita antiga (duplo clique na palavra errada + digitar letra por letra) **não funcionou**: o duplo clique acertou "Quer" na primeira tentativa e só o espaço/ponto na segunda — mirar em palavra de 4 letras dentro de textarea estreito é chute.

**Receita nova, determinística, que resolveu de primeira** — não depende de mira nenhuma:
1. Clicar em qualquer ponto do textarea.
2. `cmd+Up` → leva o caret pro caractere 0 do campo.
3. `Right` repetido N vezes, com **N = a posição exata onde falta o caractere**, contada no texto pretendido (aqui N=52, logo depois de "vend").
4. Digitar só o caractere que falta.

Contar o offset é trivial e é feito fora do navegador, então não há erro de mira. **Adotar esta como a receita padrão**; a do duplo clique fica como alternativa. A conferência por zoom continua obrigatória antes de salvar — foi ela que pegou o erro pela terceira vez —, com o preview do celular à direita como segunda checagem.

Conferência do link nesta automação (as três passadas da regra): começo por `Home` (`https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=ma…`), meio por 78 setas (`…?utm_source=manychat&utm_medium=dm&utm…`) e fim por `End` (`…utm_campaign=2026-08-28-VENDA`). Nenhum caractere comido.

Sexta no padrão novo: `IG | 2026-09-01 | LIQUIDO | risco tem dono` (carrossel 77, `utm_campaign=2026-09-01-LIQUIDO`, post específico, DM "O risco da empresa é só seu. Quer ver como fazer ela finalmente te pagar por ele?" com botão `>> Me mostra <<`). Modelo duplicado: a `IG | 2026-08-31 | LEAL | lealdade nao vem em contrato`. Criada e ativada pelo Claude com o post já no ar — a própria grade do easy-builder trouxe a capa do 77 em segundo lugar, o que serviu de confirmação de publicação sem tocar na API.

**Primeira palavra-chave com ACENTO no português.** LIQUIDO é escrita "líquido" na vida real, então a grafia sem acento (obrigatória pela regra de match) cobriria só uma parte de quem comenta. Cadastradas SEIS variantes em vez das três habituais: `LIQUIDO, liquido, Liquido, LÍQUIDO, líquido, Líquido`. **Regra que sai daqui:** quando a palavra-chave for uma palavra que o português escreve com acento, cadastrar as duas grafias em três caixas cada — seis no total. Palavra sem acento na origem (LEAL, DONO, FOME) segue com três.

Sétima no padrão novo: `IG | 2026-09-03 | RISCO | repost empreender ja e um risco` (carrossel 82, REPOST do post de 21/05 que tinha CTA "295"; `utm_campaign=2026-09-03-RISCO`, palavra RISCO/risco/Risco, post específico, DM "Você corre o risco todo dia. Quer aprender a ser recompensado à altura dele?" com botão `>> Quero <<`). Modelo duplicado: a `IG | 2026-09-02 | TEMPO | tempo de resposta`. Montada STOPPED antes da publicação (o user publicou à mão em seguida), e amarrada ao post + ativada ~1 min depois do "postei", pela grade do easy-builder (capa do pombo apareceu em segundo na grade; o primeiro slot mostra o post que estava selecionado). Conferido antes de ativar: UTM sobreviveu à troca de post. **Colisão checada:** existe uma automação antiga "RISCO" (global, 23 exec., 6 meses) — está STOPPED, então não dispara. Primeiro caso de palavra reaproveitada de automação legada. **O bug de comer caractere bateu pela SEXTA vez** ("recompensado" → "reompensado"), resolvido com a receita determinística (`cmd+Up` + `Right` × 51 + "c").

**Achado de passagem (03/09), pendente de decisão do user:** a `IG | 2026-09-02 | TEMPO | tempo de resposta` (LIVE, 4 exec.) carrega a DM do SAGRADO ("O primeiro passo você já entendeu, construir o playbook…"), não a DM do kit do 81 ("Quanto tempo a sua empresa demora pra responder um cliente?…"). Apareceu na cópia duplicada. Corrigida na mesma sessão a pedido do user: DM trocada pela do kit + botão `>> Quero saber <<`; link/UTM não tocados (conferido `2026-09-02-TEMPO` no fim). Reativada, LIVE, post do 81 mantido. **O bug de comer caractere bateu pela SÉTIMA vez** ("um cliente" → "umcliente"), resolvido com `cmd+Up` + `Right` × 50 + espaço.

**PEGADINHA NOVA (03/09) — os botões do topo mudam de lugar conforme o status.** Em automação STOPPED o topo é `Editar` (~x 1018) + `Ativar` (~x 1085). Em automação LIVE o topo é `Editar` (~x 982) + `Interromper` (~x 1067), porque "Interromper" é mais largo e empurra tudo pra esquerda. Clicar em (1018, 33) numa automação LIVE **acerta o Interromper e para a automação** — foi o que aconteceu com a TEMPO (ficou parada ~3 min até ser reativada). Regra: em automação LIVE, tirar screenshot e localizar o `Editar` antes de clicar; nunca reaproveitar a coordenada da STOPPED.

Oitava no padrão novo: `IG | 2026-09-03 | RITUAL | ritual de comando` (carrossel 83; `utm_campaign=2026-09-03-RITUAL`; palavra RITUAL/ritual/Ritual; DM "Reunião solta não fecha o mês. Quer ver como montar o ritual que coloca a empresa no ritmo do lucro?" com botão `>> Quero ver <<`). Modelo duplicado: a `IG | 2026-09-03 | RISCO | repost…`. Montada STOPPED ~30 min antes da publicação marcada (17h). Post publicado ~17h05; o carrossel só apareceu na grade do easy-builder uns 4 minutos depois (o 'Mostrar Todos' listava o reel de 2h antes como mais recente). **Pegadinha:** o reset do rádio (global → específico) seleciona automaticamente o PRIMEIRO da grade — se o post novo ainda não indexou, isso pode gravar o post errado; cancelar sem salvar e esperar. Amarrada ao post certo (capa TEM RITUAL; legenda conferida no preview), UTM sobreviveu, ativada ~17h10. **Bug de comer caractere pela OITAVA vez** ("montar" → "montr"), resolvido com `cmd+Up` + `Right` × 49 + "a". Pegadinha de viewport: a janela do Chrome estava em 1148 px de largura nesta sessão (antes 1176) e todas as coordenadas do painel deslocaram; o clique no "⋮" da lista abriu a automação em vez do menu na primeira tentativa. Localizar por zoom antes de clicar quando a largura mudar.

**O bug de comer caractere bateu pela QUINTA vez em cinco automações seguidas** (LEVE, DONO, VENDA, RESPEITO e agora LIQUIDO). Desta vez "ela" saiu como "la" em "como fazer ela finalmente". A receita determinística resolveu de primeira de novo: `cmd+Up` + `Right` × 49 (offset contado fora do navegador, no texto pretendido) + digitar o "e". **Cinco em cinco encerra a discussão sobre acaso:** o defeito é do campo, não da digitação. Entrar no campo da DM já contando que vai acontecer, e nunca salvar sem a conferência por zoom.

**Atalho novo que vale guardar, no campo do LINK:** em vez de redigitar a URL inteira (que é longa e expõe o texto todo ao bug), posicionar o caret no fim com `End`, apagar só o rabo do UTM com `Backspace` × N e digitar o novo. Aqui foram 15 backspaces (`2026-08-31-LEAL`) e a base da URL nunca foi tocada. As três passadas de conferência continuam obrigatórias — e a do meio serve de prova cruzada: pedir `Home` + `Right` × 61 tem que parar exatamente depois de "manychat"; se parar em outro lugar, algum caractere foi comido antes.

**Post apagado e republicado: como recuperar a automação (27/08).** O user apagou o carrossel 60 ~1h depois de publicar e repostou com capa nova. A automação NÃO precisa ser recriada do zero: ela sobrevive inteira (palavra, respostas de comentário, DM, botão e UTM) e só o vínculo do post morre — o slot passa a exibir "Não conseguimos encontrar uma conexão". **O botão "Tentar Novamente" não resolve**, porque a mídia foi apagada e nunca vai reconectar. O que resolve: entrar em Editar e **alternar o rádio pra "qualquer publicação ou Reel" e voltar pra "uma publicação ou Reels específico"** — isso reseta o seletor e traz a grade de posts, com o mais recente já em primeiro. Selecionar o post novo, conferir que o UTM sobreviveu e salvar. Cuidado: nunca clicar em Atualização enquanto o rádio estiver no global. Reaproveitar o mesmo `utm_campaign` é seguro aqui porque a automação estava com 0 envios e 0 cliques (a regra de só trocar UTM com cliques zerados vale na mesma lógica). Se tivesse disparado, o certo seria UTM novo.

Verificado em 27/08: a `Comando!! MBV copy` (LIVE, palavra `lucro`, 164 disparos / 78 cliques, post específico de 22/07) tem o link **sem UTM nenhum** (`https://rtc.tatsuoacademy.com/v2-maio-org` puro). Ou seja: não havia colisão de CRM com a LUCRO nova nem antes da correção — mas isso era acidente, não desenho, e é exatamente o que o padrão data+palavra elimina.
4. Rede de segurança: o `/ritual` diário detecta post novo na API sem automação correspondente e lembra o usuário.
5. Segunda-feira: leitura de execuções/CTR por automação → coluna de leads no registro. Meta da máquina: **execuções × CTR por post** (lead real).

Nona no padrão novo: `IG | 2026-09-04 | PREPARO | time que voce nao prepara` (carrossel 87, repost refeito da copy de 28/07/2025; `utm_campaign=2026-09-04-PREPARO`; palavra PREPARO/preparo/Preparo; DM "Time que entrega não se acha, se forma. Quer ver como eu ensino o dono a fazer isso?" com botão `>> Quero ver <<`). Modelo duplicado: a `IG | 2026-09-04 | JUNTOS | itai doshin` (mesma data, então só o rabo do UTM mudou: End + Backspace × 6 + PREPARO). Montada STOPPED às 16h25, ~35 min antes da publicação marcada (17h), com o post ainda apontando pro do modelo (86). **Bug de comer caractere pela NONA vez** ("como" → "omo"), resolvido com `cmd+Up` + `Right` × 49 + "c". Link conferido em três passadas (Home / Right × 61 parou depois de "manychat" / End). **Colisão checada:** a busca "preparo" no painel só traz a `IG | 2026-08-20 | PREPARO | genchi genbutsu` (LIVE, Reel específico, 60 exec.) — não é global, não dispara neste post. Timer de shell armado pra 17h00; o post atrasou e o Claude ficou em ciclos de checagem (2, 5 e 10 min) recarregando a página e abrindo 'Mostrar Todos' — o carrossel NÃO apareceu em nenhuma passada até 18h00 porque ainda não tinha sido publicado. User avisou 'postei' às ~18h01; a capa já estava em PRIMEIRO na lista ('Todo empresário já disse...', há 3 minutos), selecionada, preview conferido (capa + legenda do 87), UTM sobreviveu à troca de post (End: `2026-09-04-PREPARO`), Atualização e Ativar: **LIVE às 18h02**, ~3 min depois da publicação. Pegadinha de operação: depois de `navigate` na URL do easy-builder, o primeiro clique em Editar não pega (a página ainda carrega); esperar ~15 s e clicar de novo. Regra que fica: quando o post atrasa, o relógio não substitui o aviso — o 'postei' do user continua sendo o gatilho mais rápido.

## Leitura 25/08/2026 — os 4 vídeos de copy (painel, Chrome Tatsuo)

Palavras dos 4 vídeos produzidos: diagnóstico, preparo (×2) e gente. Correção: "Comando!! MBV copy" (lucro, 164 exec.) NÃO é um dos 4 — tinha entrado por engano na conta de 18/08.

| Automação | Palavra | Estado | Execuções | CTR |
|---|---|---|---|---|
| roteiro copy 2 | diagnóstico | LIVE, Reel específico | **68** | 50% |
| IG \| 2026-08-20 \| PREPARO \| genchi genbutsu | preparo | LIVE, Reel específico | **39** | 33,3% |
| roteiro copy 3 | preparo | LIVE, Reel específico | **3** | 66,7% |
| 307 copy | gente | LIVE, Reel específico | **5** | 60% |

**Total: 115 disparos** (≈52 leads clicados aplicando o CTR de cada uma).

Notas da leitura:
1. **As duas de "preparo" NÃO conflitam**: ambas são "Reel específico" (cada uma amarrada ao seu post), então o Manychat separa os disparos corretamente. O desequilíbrio (39 × 3) é diferença de desempenho dos vídeos, não bug de atribuição.
2. **"gente" é a bagunçada** — existem 3 automações LIVE orbitando a palavra: "307 copy" (específico, palavra `gente`, 5 exec.), "GENTE mbv ESPECIFICO" (específico, palavra `gente`, **0 exec.** — provavelmente apontando pro post errado ou nunca disparou) e "#GENTE mbv" (**GLOBAL**, palavra `#gente`, 42 exec., CTR 14,3% — o CTR baixo típico de global). Se o CTA do vídeo pedia "#gente", os 42 disparos são dele e o total dos 4 vídeos sobe pra ~152. A limpar: manter uma só, específica, no padrão da regra fixa.
3. "#GENTE mbv copy" (15 exec.) tem palavra `cultura`, apesar do nome — não é do vídeo "gente".

## Leitura 27/08/2026 — semana 21–27/08 (painel, Chrome "Tatsuo Academy")

| Automação | Palavra | Post | Publicado | Disparos | CTR | UTM? |
|---|---|---|---|---|---|---|
| IG \| 2026-08-21 \| DRAGA | DRAGA | 50_draga | 21/08 | 7 | 57,1% | não |
| DNA | DNA | 51_piloto-automatico | 22/08 | 4 | 100% | não |
| ROTINA | ROTINA | 49_treinamento-diario | 23/08 | 2 | 0% | não |
| ESTRELA | ESTRELA | 50_vendedor-estrela | 24/08 | **23** | 52,2% | não |
| ESCONDIDA | ESCONDIDA | 51_empresa-escondida | 24/08 | 5 | 80% | não |
| LADRAO | LADRAO | 52_ladrao-silencioso | 25/08 | 1 | 100% | não |
| SONHO | SONHO | 50_nem-sonho-tem | 25/08 | **58** | 48,3% | **sim** |
| IG \| 2026-08-25 \| CULTURA | CULTURA | roteiro4_explica-mil-vezes | 25/08 | 22 | 40,9% | **sim** |
| IG \| 2026-08-26 \| PILOTO | PILOTO | 50_piloto-automatico | 26/08 | **0** | N/A | sim |
| IG \| 2026-08-26 \| PATRAO | PATRAO | 58_cliente-virou-patrao | 26/08 | 2 | 50% | sim |
| IG \| 2026-08-21 \| DENTRO | DENTRO | 46_porta-pra-dentro | 21/08 | 0 | N/A | não |

**Total da semana: 124 disparos ≈ 63 leads clicados** (aplicando o CTR de cada uma). Fora da conta: "comando repost" (global, 44 exec., 50%) e PREPARO (20/08, 42 exec., 31%) — não são post da semana.

### Três achados desta leitura
1. **O buraco de atribuição tem tamanho medido.** Dos ~63 leads clicados, só **14 chegam ao CRM com rastro** (11 SONHO + 3 CULTURA). O resto disparou antes do UTM existir — não é "post que não gerou lead", é lead sem etiqueta. O caso mais caro é **ESTRELA: 23 disparos × 52,2% ≈ 12 leads clicados, todos invisíveis**.
2. **Clicou ≠ virou contato.** SONHO: 58 disparos → ~28 cliques → **11 contatos no CRM (39% dos cliques)**. Essa é a primeira medição real da perda entre o clique do DM e o preenchimento do formulário — antes a máquina só tinha "leads clicados" como proxy final.
3. **A palavra é ~50% dos comentários, não 87%.** SONHO 58/116 = 50% · ESTRELA 23/50 = 46% · PATRAO 2/6 = 33% · PILOTO 0/5 = 0% (elogios, nenhum CTA — confirmado pelo user; automação correta). Mediana de 9 posts: 50%. O baseline de 18/08 (pavão, 87%) era outlier e inflava toda estimativa de lead em ~1,7x. Nova regra: contato no CRM ~= 9-10% dos comentarios. Ver H8.

Décima no padrão novo: `IG | 2026-09-05 | OBVIO | o obvio do dono` (carrossel 90; `utm_campaign=2026-09-05-OBVIO`; palavra em SEIS grafias porque "óbvio" leva acento: `OBVIO, obvio, Obvio, ÓBVIO, óbvio, Óbvio`; DM "O óbvio da sua empresa só existe quando é óbvio pro time. Quer ver como eu ensino o dono a fazer isso?" com botão `>> Quero ver <<`). Modelo duplicado: a `IG | 2026-09-04 | PREPARO | time que voce nao prepara` (End + Backspace × 10 + `05-OBVIO`; três passadas de conferência OK). Montada **STOPPED em 04/09 ~18h40, com o post ainda apontando pro 87 (o modelo)**, pra publicação agendada de **05/09 às 13h**. Publicado no horário (2026-09-05 ~13h05); amarrada ao post do 90 na grade (capa dos ovos, 83 curtidas na hora) e ATIVADA às 13h13, LIVE — dentro dos 5 minutos do aviso. **O bug de comer caractere bateu pela SEXTA vez** ("pro" saiu como "po"); receita determinística de novo de primeira: `cmd+Up` + `Right` × 49 + "r".

## 29/08/2026 — vídeo do MBV (aula gratuita 31/08): primeiro uso de "próxima publicação" e primeiro conflito de palavra

**Duas automações no padrão novo, mesma palavra, mesmo destino, UTM separado por data:**
- `IG | 2026-08-29 | MBV | aula gratuita 31-08` — LIVE, `utm_campaign=2026-08-29-MBV`
- `IG | 2026-08-30 | MBV | aula gratuita 31-08` — STOPPED, `utm_campaign=2026-08-30-MBV`

Destino não é o `rtc.tatsuoacademy.com/v2-maio-org` de sempre: é a landing da aula, `https://tatsuoacademy.com/aula-gratuita-31-08/`. UTM idêntico em estrutura (`utm_source=manychat&utm_medium=dm&utm_campaign=AAAA-MM-DD-PALAVRA`), então o `/ritual` casa o lead do mesmo jeito.

### Achado 1: existe um terceiro gatilho, "próxima publicação ou Reel"
Além de "publicação específica" e "qualquer publicação", o easy-builder tem **"próxima publicação ou Reel"**. Ele resolve o furo operacional que a regra fixa de 19/08 não cobria: **dá pra armar a automação ANTES de publicar**, sem esperar o post existir pra amarrar o vínculo. A automação fica LIVE esperando e gruda sozinha no próximo post publicado. Depois de grudar, ela vira específica daquele post — a atribuição fica idêntica à do padrão "post específico".

Consequência prática: **a janela de 5 min entre publicar e ativar deixa de existir** nos casos em que o user avisa antes. O fluxo passa a ser armar e ativar antes, publicar depois.

Cuidado que nasce junto: com o gatilho armado, **o próximo post publicado é o que gruda**, seja ele qual for. Se o user publicar outra coisa no meio, a automação amarra no post errado. E **duas automações "próxima publicação" ativas ao mesmo tempo grudam no MESMO post** — por isso a de 30/08 nasceu STOPPED e só se ativa amanhã, depois da de hoje já ter grudado.

### Achado 2: palavra de CTA pode colidir com automação GLOBAL legada
A palavra do vídeo era MBV, e existia uma automação **`MBV` GLOBAL e LIVE** (qualquer publicação; palavras MBV, mbv, Mbv, mvb, MVB; **1.087 envios / 576 cliques / 53% CTR**; DM "Para acessar o link da imersão.." com botão ">> Clique Aqui <<") apontando pra **imersão**, não pra aula. Ou seja: quem comentasse MBV no vídeo novo podia receber o link errado, sem rastro.

Decisão do user (29/08): **pausar a global MBV até 01/09**, deixando as duas específicas donas da palavra durante a campanha. Custo aceito: posts antigos com CTA MBV ficam sem resposta por ~3 dias (a global fazia ~3-4 disparos/dia). **Religar a global em 01/09.**

Regra que fica: **antes de criar automação nova, pesquisar a palavra do CTA no painel.** As duas globais legadas (307, comando) e a MBV mostram que o acervo tem canos de palavra genérica que atropelam CTA novo. Se a palavra do vídeo já existe numa global, ou pausa a global durante a campanha, ou o link errado sai pra metade dos comentários.

### Achados operacionais do easy-builder
1. **Sair da tela de edição pelo cabeçalho descarta tudo.** Clicar no nome da automação no topo esquerdo não abre renomeação: funciona como voltar, e as edições não salvas somem. **Salvar com "Atualização" antes de qualquer navegação.**
2. **Renomear só existe na LISTA**, no menu `⋮` da linha (Renomear / Duplicar / Mover para / Apagar). Dentro da automação o `⋮` só tem "Apagar".
3. **"Atualização" e "Ativar" demoram 20-40s** com o botão em spinner. Não é travamento. Não clicar de novo nem navegar: esperar o botão voltar a "Editar / Ativar".
4. **Duplicar também é lento e a lista fica desatualizada.** Depois de "Duplicar", esperar sem apertar Escape (Escape cancela) e recarregar a lista pra ver a cópia.
5. **Texto do botão tem teto de 20 caracteres.** ">> Quero minha vaga <<" (22) é recusado com "Tamanho máximo é 20 caracteres"; ">> Quero a vaga <<" (18) passa.
6. `form_input` no ref do campo continua sendo o jeito certo de escrever DM e link: escreve o valor inteiro de uma vez e **não repetiu o bug de comer caractere** (que só aparece com digitação). Conferência por zoom no começo/meio/fim do link feita mesmo assim, e passou limpo.

## 29/08/2026 — `IG | 2026-08-29 | FIRME | perna que falta` (carrossel 62)

Quinta automação no padrão de UTM novo. Criada e ativada pelo Claude depois do aviso do user ("já postei, corre").

- **Modelo duplicado:** `IG | 2026-08-28 | VENDA | um setor so` (post específico, UTM no padrão novo, botão já com o texto que se queria).
- **Palavra:** FIRME / firme / Firme · **post específico:** carrossel 62, capa *"NINGUÉM QUER TRABALHAR."*
- **DM:** "Liderança, método e técnica: as três se aprendem. Quer ver como levantar as suas?" · **botão:** `>> Quero ver <<` (15 caracteres)
- **Link:** `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-08-29-FIRME`
- Respostas de comentário herdadas do modelo (Obrigado! Por favor, veja seu Direct. / Te enviei o link no seu Direct / Opa! Verifica seu Direct).

### O que essa rodada confirma
1. **`form_input` continua imune ao bug de comer caractere.** Nome, palavra, DM e link foram escritos de uma vez, os quatro saíram inteiros. O bug é da digitação (`type`), não do campo. Conferência por zoom feita mesmo assim nos quatro; e o link nas três passadas da regra: começo por `Home` (`https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=ma…`), meio por 78 setas (`/v2-maio-org?utm_source=manychat&utm_medium=dm&utm`) e fim por `End` (`…utm_campaign=2026-08-29-FIRME`). Limpo.
2. **A busca do painel casa PALAVRA-CHAVE, não só nome.** Buscar `firme` devolveu "Nenhuma automação encontrada", enquanto `VENDA` trouxe automações cujo nome não tem "venda" (Auto-DM de links dos comentários, ESTRELA). Ou seja: **a busca serve como teste de colisão de palavra** — é ela que cumpre a regra de 29/08 ("antes de criar automação nova, pesquisar a palavra do CTA no painel"), e não só como localizador.
3. **O gatilho "próxima publicação" armado hoje de manhã grudou no post certo.** A `IG | 2026-08-29 | MBV` já aparece como "publicação ou Reel específico" amarrada ao **vídeo da praia** (8 disparos, 75% CTR) — não no carrossel 62, publicado depois. O risco documentado ("o próximo post publicado é o que gruda") não se materializou porque o vídeo saiu primeiro e a automação grudou na hora. **Confirmado na prática:** depois de grudar, o gatilho vira específico e para de capturar publicação nova. A de 30/08 segue STOPPED e no gatilho "seguinte", como planejado.
4. Sequência de tempo do easy-builder nesta rodada: Duplicar ~10s · Renomear ~4s · Atualização ~30s · Ativar ~30s.

## 29/08/2026 (fim de tarde) — dois posts de domingo armados com antecedência: FOME e CONSTANCIA

Primeiro caso de **lote de posts agendados** resolvido inteiramente antes da publicação. Os dois carrosséis de domingo 30/08 já estavam programados no Instagram (69 cavalo teimoso às 13h, palavra FOME; 72 não tem opção às 17h, palavra CONSTANCIA) e o user pediu as automações prontas "pra só precisar ativar amanhã".

Ambas duplicadas da `IG | 2026-08-29 | FIRME | perna que falta`, salvas **STOPPED** no gatilho **"próxima publicação ou Reel"**:

| Automação | Palavra | DM | Botão | utm_campaign |
|---|---|---|---|---|
| `IG \| 2026-08-30 \| FOME \| cavalo teimoso` | FOME, fome, Fome | "Você não cria vontade puxando corda. Quer ver como se devolve o problema pra quem é dono dele?" | `>> Quero começar <<` | `2026-08-30-FOME` |
| `IG \| 2026-08-30 \| CONSTANCIA \| nao tem opcao` | CONSTANCIA, constancia, Constancia, CONSTÂNCIA, constância, Constância | "Constância não sai de vontade, sai de método. Quer ver o método que sustenta o básico todo dia?" | `>> Quero o método <<` | `2026-08-30-CONSTANCIA` |

### Achado 1: a regra de pesquisar a palavra antes de criar pegou a segunda global do acervo
A busca por `fome` devolveu uma automação **`fome`, GLOBAL e LIVE** (qualquer publicação; palavras fome/Fome/FOME; **32 envios / 8 cliques / 25% CTR**; DM "Para transformar seu time em campeões comprometidos" com botão `>> Clique Aqui <<`; **link sem UTM**). É o segundo caso em dois dias, depois da global MBV — e confirma que o acervo tem mais canos de palavra genérica do que as duas legadas conhecidas (307, comando).

O CTR de 25% é a assinatura típica de global de palavra temática (contra 43–58% das específicas), pelo mesmo motivo já documentado: dispara em quem comenta a palavra por acaso.

Decisão do user: **pausar a global `fome` na manhã de domingo**, junto com a ativação da específica, e religar depois que o post 69 esfriar. Não pausar já na sexta preserva o disparo do fim de semana (~0,5/dia, contra os 3-4/dia que a MBV custava). `constancia` na busca não devolveu nada — palavra limpa.

**A regra fica mais forte, não igual:** pesquisar a palavra do CTA no painel não é conferência de rotina, é o passo que evita mandar link errado. Duas de duas palavras temáticas testadas nesta semana tinham global viva por trás.

### Achado 2: o gatilho "próxima publicação" não escala sozinho — a ORDEM de ativação vira o ativo crítico
Com três automações no gatilho "próxima publicação" esperando (FOME, CONSTANCIA e a MBV de 30/08), o cuidado documentado em 29/08 ("duas ativas ao mesmo tempo grudam no MESMO post") deixa de ser observação e vira restrição operacional: **só uma pode estar LIVE por vez, e a próxima só se ativa depois de confirmar que a anterior já grudou.**

Sequência montada para domingo (tarefas one-shot agendadas):
1. **12:45** — pausar a global `fome` + ativar a FOME (só ela LIVE)
2. **13:07** — confirmar que a FOME virou "publicação específica" amarrada ao carrossel 69, e só então ativar a CONSTANCIA
3. **17:07** — confirmar que a CONSTANCIA grudou no carrossel 72; conferir disparos das duas

O passo 2 é o que segura tudo: se a FOME ainda estiver em "próxima publicação" às 13:07, o post não saiu, e ativar a CONSTANCIA ali faria as duas grudarem no mesmo carrossel.

**Keep-awake disparado ANTES, não agendado:** `caffeinate -dimsu -t 92000` rodado no sábado 16:24, cobrindo até ~17:50 de domingo. É a lição do FDS 21-23/08 (o keep-awake agendado é dependência circular: se o Mac dorme, a tarefa que o acordaria não roda).

### Achado 3: o teto de 20 caracteres do botão é inclusivo
`>> Quero o método <<` tem exatamente 20 caracteres e foi aceito. O registro de 29/08 dizia que 22 é recusado e 18 passa; agora está fechado dos dois lados — **20 é o último valor válido**.

### Confirmações de rotina
- `form_input` seguiu imune ao bug de comer caractere: nome, palavra, DM, texto do botão e link escritos de uma vez, os cinco inteiros nas duas automações.
- Conferência por zoom feita em todos os campos, e o link nas três passadas da regra nas duas automações: começo por `cmd+Up` (`https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=ma…`), meio por 78 setas (`/v2-maio-org?utm_source=manychat&utm_medium=dm&utm`) e fim por `End`. Limpo nas duas.
- Sequência de tempo do easy-builder: Duplicar ~15s · Renomear ~5s · Atualização ~40s (ficou em spinner mais tempo que os 20-30s anteriores).

### Adendo do mesmo dia: quando o user vai estar ausente, ative ANTES

O user avisou (16:45 de sábado) que não estaria por perto no domingo e pediu as páginas do Manychat abertas pra a sessão agendada "mexer sem autorização". **Não é isso que a autorização exige.** O `AskUserQuestion` de escolha de navegador é disparado por haver mais de um Chrome pareado à conta Claude compartilhada, no começo de qualquer sessão — página aberta não muda nada. Sessão agendada sem humano pra clicar trava nesse ponto.

Consequência prática, que vira regra: **em post agendado com o user ausente, ativar a automação ANTES vale mais do que ativar na hora certa.** O gatilho "próxima publicação" troca a exigência "estar no computador às 12:45" pela exigência "não publicar nada no meio" — e a segunda o user controla de qualquer lugar. Foi o que se fez: a FOME (e a pausa da global `fome`) saiu no sábado, ~20h antes do post.

O limite dessa jogada é a fila: só a PRIMEIRA automação da sequência pode ser antecipada, porque duas "próxima publicação" LIVE grudam no mesmo post. A segunda (CONSTANCIA) continua presa a uma janela entre a publicação das 13h e a das 17h. **Fallback registrado para esse caso: o app do Manychat no celular ativa a automação com um toque** — não depende de sessão do Claude nem de navegador pareado.

### Contraprova de 30/08: antecipar ativação em "próxima publicação" tem um pré-requisito

A antecipação recomendada acima **falhou na primeira vez que foi usada**. A FOME foi armada no sábado 16:45 para o post de domingo 13h; no meio, o **carrossel 68 (concurso de popularidade) foi publicado por outra frente de trabalho** e a automação grudou nele. Descoberto às 12:00 de domingo, ~1h antes do post alvo, com **0 envios e 0 cliques** — dano nenhum, e o post 68 já estava coberto pela sua própria automação (`RESPEITO`, específica, 1 disparo).

Conserto: Editar → rádio de volta para "próxima publicação ou Reel" → Atualização. Não foi preciso passar pelo rádio global (o caminho de 27/08 vale para vínculo QUEBRADO por post apagado; para vínculo CERTO no post ERRADO, basta trocar o rádio). DM, botão, palavras e link sobreviveram à edição.

**A regra ganha um pré-requisito:** antecipar ativação em gatilho "próxima publicação" só é seguro quando **a fila de publicação inteira do perfil está sob controle de quem antecipa**. Com mais de uma pessoa (ou mais de uma sessão do Claude) produzindo e publicando no mesmo perfil, uma automação armada com horas de antecedência é uma armadilha silenciosa: ela gruda no primeiro post que aparecer, seja de quem for.

Duas consequências operacionais:
1. **A conferência antes do post alvo deixa de ser opcional.** Toda antecipação tem que vir acompanhada de uma checagem entre a hora de armar e a hora do post.
2. **Enunciar o risco como "não publique o vídeo X" é estreito demais.** O enunciado correto é "nenhuma publicação, de ninguém, até o post alvo" — e se isso não puder ser garantido, não antecipe: arme perto do horário.


## Leitura 31/08/2026 — ritual de segunda (painel, Chrome "Tatsuo Academy")

| Automação | Palavra | Post | Disparos | CTR | UTM? | leads no CRM |
|---|---|---|---|---|---|---|
| IG \| 2026-08-30 \| FOME \| cavalo teimoso | FOME | carrossel 69 | **59** | 45,8% | sim | **3 MQL + 1 reimpactado** |
| IG \| 2026-08-30 \| CONSTANCIA \| nao tem opcao | CONSTANCIA | carrossel 72 | **0** | N/A | sim | 0 |
| IG \| 2026-08-29 \| RESPEITO \| concurso de popularidade | RESPEITO | carrossel 68 | 1 | 100% | sim | 0 |
| IG \| 2026-08-29 \| FIRME \| perna que falta | FIRME | carrossel 62 | 4 | 50% | sim | 0 |
| IG \| 2026-08-28 \| VENDA \| um setor so | VENDA | carrossel 61 | 5 | 40% | sim | 0 |
| IG \| 2026-08-28 \| FOLGA \| dois cansacos | FOLGA | carrossel 63 | 4 | 75% | sim | 1 Q-MQL |
| IG \| 2026-08-27 \| DONO \| come antes de voce | DONO | carrossel 64 | 6 | 83,3% | sim | 1 N-MQL |

A global `fome` **não aparece mais na busca** — a pausa combinada para a manhã de domingo foi
executada. A busca por `fome` devolve só a automação específica do 69.

### Achado 1 (correção de método): o `utm_campaign` mudou de formato e quebrou a leitura de lead
Até 28/08 a campanha era a palavra crua (`SONHO`, `CULTURA`, `PATRAO`). Das automações de 29/08 em
diante ela passou a ser **datada** (`2026-08-30-FOME`, `2026-08-28-folga`). O casamento do
`tabelas_ritual.py` comparava a campanha com a palavra-chave da ficha em igualdade exata — então
**todo post novo aparecia como "sem rastro" mesmo tendo lead**. No ritual de 31/08 isso levou a um
diagnóstico errado ("as palavras novas não trazem lead") que só caiu quando o painel mostrou 59
disparos no FOME. Corrigido com `palavra_da_campanha()`, que aceita os dois formatos. **Lição: mudança
de convenção de nomenclatura é mudança de esquema — quebra leitura em silêncio, sem erro nenhum.**

### Achado 2: a razão disparo/comentário é estável em ~0,40, e o comentário é o gargalo do lead
Nos 19 posts com automação já medida: **disparos × comentários dá rho +0,94**, com razão mediana de
**0,40** — cerca de 4 em cada 10 comentários viram disparo. Contra a taxa de interação do post o rho
é +0,70; contra alcance, só **+0,51**. Ou seja: **o lead segue a conversa, não a circulação.**

Duas exceções, as duas de reel: LUCRO (129 comentários → 13 disparos, razão 0,10) e PILOTO
(8 → 1, razão 0,12). É exatamente o que "comentário ordena, não conta" previa — comentário de reel é
opinião, não palavra de CTA, e o proxy degrada onde o post não pede a palavra.

### Achado 3: automação certa em post que não conversa não produz nada
CONSTANCIA está LIVE, grudada no post certo, com UTM correto — e fez **0 disparos**, porque o
carrossel 72 fez 1 comentário. Não há conserto de automação que resolva isso. O conserto é o post.


## 31/08/2026 — duas automações LIVE para a aula gratuita (carrossel 73 + estático 74)

- `IG | 2026-08-31 | LIVE | fechamento do mes` — **LIVE**, post específico (carrossel 73), `utm_campaign=2026-08-31-LIVE-CARROSSEL`
- `IG | 2026-08-31 | LIVE | trabalhou de graca` — **LIVE desde 12:47** (o user antecipou a publicação; estava montada e parada desde 11:44, e ativar levou 3 min: selecionar o post na grade, conferir que o UTM sobreviveu, Atualização, Ativar). `utm_campaign=2026-08-31-LIVE-ESTATICO`

**Extensão do padrão de UTM:** duas peças no MESMO dia com a MESMA palavra quebram o formato `AAAA-MM-DD-PALAVRA`, que colidiria. Sufixo de peça (`-CARROSSEL`, `-ESTATICO`) resolve e mantém o identificador único por construção. Adotar sempre que houver mais de um post por dia na mesma palavra.

**ERRO GRAVE PEGO A TEMPO — o link do modelo duplicado não é o link da campanha.** As duas nasceram apontando pra `rtc.tatsuoacademy.com/v2-maio-org` (a oferta padrão, herdada da CONSTANCIA), quando a campanha da aula usa `tatsuoacademy.com/aula-gratuita-31-08/`. A do carrossel chegou a ficar LIVE ~10 minutos com o destino errado; corrigida com 0 envios e 0 cliques, então nada se perdeu.
**Regra nova:** duplicar herda o LINK, não só o UTM. **Conferir o domínio e o caminho do link, não apenas o `utm_campaign`** — o UTM certo em cima do destino errado passa em qualquer conferência de três passadas e continua mandando a pessoa pro lugar errado. Antes de ativar, abrir o `kit-cta.md` da campanha (em `conteudo/videos/<data>_<campanha>/`) e comparar o link inteiro.

**O bug de comer caractere bateu pela 5ª, 6ª e 7ª vez — e agora tem posição conhecida.** Ocorrências de hoje: "fecham"→"echam" (offset 49), "vivo"→"vio" (offset 50), "um"→"m" (offset 50), "raciocino"→"aciocino" (offset 50). Somando as anteriores (LEVE 'dono'→'doo', DONO 'mostro'→'mstro', VENDA 'vende'→'vend' offset 52, RESPEITO 'se constrói' offset 49), **o caractere comido cai sempre na faixa 49-52**. Ou seja: não é aleatório, é o campo perdendo UM caractere por volta do 50º toque. A receita determinística (`cmd+Up` + `Right` × N + digitar) resolveu em 100% dos casos. Ideia a testar na próxima: escrever os primeiros ~55 caracteres, pausar, e escrever o resto — pode evitar o bug em vez de consertá-lo.

**Confirmação do padrão de montar-antes-e-ativar-depois (2ª vez, agora com antecipação):** a automação do estático ficou montada e STOPPED por ~1h com o post ainda apontando pro carrossel. Quando o user antecipou a publicação das 17h30 pras 12h45, a ativação levou 3 minutos — e o `utm_campaign` sobreviveu intacto à troca de post, confirmado nas três passadas. **Montar antes vale sempre**, inclusive (e principalmente) quando o horário do post é incerto: quem monta na hora tem pressa, e é com pressa que o link errado passa.

**Leitura rápida do dia (31/08, ~12:50):** `LIVE | fechamento do mes` com 3 disparos e 66,7% de CTR ~1h após a publicação. A global `IG | 2026-08-29 | MBV | aula gratuita 31-08` seguia em 27 disparos / 80% — ou seja, parte do público continua digitando MBV (palavra do vídeo) em vez de LIVE. Os dois canos estão captando pra mesma aula; só a atribuição é que fica separada.

Sexta no padrão novo: `IG | 2026-08-31 | LEAL | lealdade nao vem em contrato` (carrossel 75, `utm_campaign=2026-08-31-LEAL`, palavra LEAL/leal/Leal, post específico, DM "Ninguém veste a camisa por pedido. Quer ver como se constrói um lugar que segura gente boa?" com botão `>> Quero ver <<`). Criada e ativada pelo Claude ~5 min depois da publicação, com o user avisando durante a produção ("já cria o manychat que to postando").

**Modelo duplicado: a `FOME | cavalo teimoso` (30/08), e não a mais recente da lista.** As duas automações do topo eram `LIVE | trabalhou de graca` e `LIVE | fechamento do mes`, que apontam pro destino da aula ao vivo, não pro link padrão do treinamento. **Regra que fica: "modelo mais recente" quer dizer o mais recente COM O LINK CERTO** — conferir o destino antes de duplicar, porque a lista mistura campanhas de destinos diferentes. Como a data do modelo era 30/08 e a nova é 31/08, trocou-se o `utm_campaign` inteiro (15 caracteres exatos: `2026-08-30-FOME` → `2026-08-31-LEAL`), com End + 15 backspaces, sem tocar no resto da URL.

**O bug de comer caractere bateu pela SEXTA vez** — "constrói" saiu como "onstrói", comendo o "c" inicial da palavra. Sexta ocorrência em seis automações seguidas (LEVE, DONO, VENDA, RESPEITO, e agora LEAL): **não é intermitente, é determinístico — assumir sempre**. A receita do `cmd+Up` + `Right × N` resolveu de primeira pela terceira vez seguida; aqui N=52, contado fora do navegador com um `python3 -c` que compara a string pretendida com a que saiu e devolve o índice da primeira divergência. **Vale registrar esse cálculo como o passo padrão** — tira o erro de contagem manual do caminho:
```
python3 -c "
alvo='...'; saiu='...'
i=next(k for k in range(len(saiu)) if alvo[k]!=saiu[k]); print(i, repr(alvo[i]))"
```

**Leitura do campo de LINK: o `javascript_tool` não serve.** Tentar ler o `value` do input por JS devolve `[BLOCKED: Cookie/query string data]` — o guard de privacidade do navegador bloqueia query string. O que funciona é ler visualmente em duas tomadas: clicar no campo, `End` + zoom (mostra a cauda) e `Home` + zoom (mostra a cabeça). Nas duas leituras as pontas se emendam no meio (aqui em "ma|nychat") e cobrem a URL inteira, o que serve de conferência completa.

**A grade do easy-builder confirmou a publicação sem tocar na API do Instagram** (mesma técnica de 29/08): o carrossel apareceu em primeiro na grade com "há 3 minutos", capa e primeiras palavras da legenda conferindo. Continua sendo a forma barata de saber se o post está no ar.


## 01/09/2026 — fechamento da campanha da aula 31/08 e volta da global

**Trocas feitas (conforme combinado em 29/08):**
- `IG | 2026-08-29 | MBV | aula gratuita 31-08` → **STOPPED**
- `IG | 2026-08-31 | LIVE | fechamento do mes` → **STOPPED**
- `IG | 2026-08-31 | LIVE | trabalhou de graca` → **STOPPED**
- `MBV` (global, imersão) → **LIVE** de novo
- `IG | 2026-08-30 | MBV | aula gratuita 31-08` — nunca foi ativada (0 envios); já estava parada

Motivo de parar as três: todas apontavam pra `tatsuoacademy.com/aula-gratuita-31-08/`, e não houve replay. Com elas no ar, quem comentasse hoje receberia link de aula vencida.

### Números finais por peça (a medição da campanha)

| peça | automação | envios | cliques | CTR |
|---|---|---|---|---|
| vídeo (29/08) | `MBV \| aula gratuita 31-08` | **31** | 22 | 71% |
| estático 74 | `LIVE \| trabalhou de graca` | 5 | 5 | **100%** |
| carrossel 73 | `LIVE \| fechamento do mes` | 4 | 2 | 50% |
| **total** | | **40** | **29** | **72,5%** |

### Duas lições, uma delas contra uma recomendação minha

**1. O vídeo foi o motor: 31 dos 40 envios (78%).** Os dois posts de feed juntos fizeram 9. Isso vai contra a recomendação que a máquina deu em 31/08 de manhã, quando eu argumentei — com o dado de comentários/1k alcance (carrossel 2,63 × imagem 0,15) — que o carrossel seria a peça de captação e o estático o reforço. **Na prática os dois foram marginais diante do vídeo.** Ressalvas honestas: o vídeo teve 2 dias no ar contra algumas horas dos posts; e CTA falado parece converter melhor que CTA escrito. Mas o tamanho da diferença não se explica só por isso. **Hipótese pra testar: em campanha de evento, o vídeo com CTA falado é a peça principal e o feed é reforço — o inverso do que a régua de comentários/1k sugere.**

**2. Erro de processo meu: dividi o CTA em duas palavras.** A campanha do vídeo já rodava com **MBV**; eu propus **LIVE** pros dois posts de feed e o user aprovou. Resultado: quem viu o vídeo foi treinado a digitar MBV e provavelmente digitou MBV também nos posts de feed — caindo na global do vídeo, sem separação por peça. Ou seja, os 4 e os 5 envios do carrossel/estático são **piso, não medida**: parte do que eles geraram está dentro dos 31 da MBV, e não dá pra recuperar.
**Regra:** quando já existe campanha rodando com uma palavra, os posts novos da MESMA campanha usam **a mesma palavra**, com automação por post específico. O post específico já separa a atribuição — a palavra diferente não acrescenta rastreio nenhum e ainda divide o CTA de quem já foi treinado.

## 02/09/2026 — o buraco do "307" (e por que a máquina não enxerga o babá)

Leitura do painel de 02/09 achou a automação **`307`: 7.205 execuções, CTR 52,7%, ainda LIVE**, modificada pela última vez há ~4 semanas.

**O gatilho dela é GLOBAL.** Enquanto todas as automações do regime atual disparam em "um Publicação ou Reel **específico**", a 307 dispara em "**alguma** publicação ou Reel" — qualquer comentário com "307" em qualquer post da conta cai nela. Isso a torna inatribuível por desenho: os 7.205 disparos são um caldeirão de pelo menos 8 posts.

**Os posts que dividem esse caldeirão** (17–22/08, a era pré-palavra-única): o babá-de-adulto (17/08 — 6.911 comentários e 832.595 de alcance, o maior carrossel da conta), 33_decidir-no-escuro, 45_contratou-um-curriculo, 45_autoridade-moral, 45_vontade-propria, 45_cara-do-lider, 45_anda-dez-volta-oito e 46_nunca-e-dinheiro. Pelo tamanho relativo, o babá sozinho deve responder pela maior parte — mas "deve" é a palavra certa, porque o painel não separa.

**Consequência para qualquer leitura de placar:** o maior evento de lead da conta é anterior à atribuição e está perdido. Comparações do tipo "o maior lote de leads da história" só valem **de 23/08 em diante**, quando a palavra única virou regra. Antes disso a máquina tem volume, não tem origem.

**Ponta solta operacional:** a 307 continua LIVE com gatilho global. Qualquer pessoa que comente "307" num post de hoje entra por ela, fora de qualquer medição — e some no mesmo caldeirão. Vale decidir se ela é desligada ou mantida como rede de captura genérica; enquanto estiver ligada, ela é ruído permanente na atribuição.

Sétima no padrão novo: `IG | 2026-09-02 | SAGRADO | biblia de vendas` (carrossel 78, `utm_campaign=2026-09-02-SAGRADO`, palavra `SAGRADO, sagrado, Sagrado`, post específico, DM "Quem escreve a bíblia da sua área de vendas é você. Quer ver como começar?" com botão `>> Quero escrever <<`). Modelo duplicado: a `IG | 2026-09-01 | VIRADA | dia da virada`, a mais recente da lista. Criada e ativada pelo Claude com o post já no ar — a capa da bíblia veio em PRIMEIRO na grade do easy-builder, o que serviu de confirmação de publicação sem tocar na API.

**O bug de comer caractere bateu pela SEXTA vez em seis automações seguidas** (LEVE, DONO, VENDA, RESPEITO, LIQUIDO e agora SAGRADO). Desta vez o campo comeu o **espaço** depois de "você." — "você. Quer" virou "você.Quer". Vale registrar que o defeito não come só letra: come espaço também, e espaço comido é mais fácil de passar batido no zoom do que letra faltando, porque a frase continua legível. A receita determinística resolveu de primeira de novo: `cmd+Up` + `Right` × 51 (offset contado fora do navegador, no texto pretendido) + digitar o espaço.

**Pegadinha nova de UI:** clicar no campo do texto do botão **abre o modal "Adicionar um link"** em vez de editar o botão inline — o texto do botão e a URL moram os dois dentro desse modal. O que eu tinha digitado antes do modal abrir caiu direto no campo certo, mas isso foi sorte; o caminho correto é clicar no botão, esperar o modal, e editar os dois campos lá dentro antes de Salvar.

**Atalho do UTM confirmado de novo:** `End` + `Backspace` × 17 (`2026-09-01-VIRADA`) + digitar `2026-09-02-SAGRADO`, sem tocar na base da URL. As três passadas de conferência passaram limpas, e a do meio (`Home` + `Right` × 61 parando exatamente depois de "manychat") continua sendo a melhor prova cruzada de que nada foi comido antes.

Sétima no padrão novo: `IG | 2026-09-02 | TEMPO | tempo de resposta` (carrossel 81, `utm_campaign=2026-09-02-TEMPO`, palavra TEMPO/tempo/Tempo, post específico, DM "O primeiro passo você já entendeu, construir o playbook, que é a parte fácil. O segundo é o mais difícil, fazer com que ele seja executado, quer aprender?" com botão `QUERO`). Modelo duplicado: a `IG | 2026-09-02 | SAGRADO | biblia de vendas` — **mesma data**, então só a última palavra do UTM mudou (7 backspaces em "SAGRADO" + "TEMPO"), e a base da URL nunca foi tocada. LIVE às 19h13, com o post no ar desde 18h50.

**O bug de comer caractere bateu pela SEXTA e SÉTIMA vez — e pela primeira vez DUAS de uma vez na mesma mensagem.** Na primeira DM escrita, "um cliente" saiu "u cliente". Depois, quando o user trocou o texto, a segunda DM perdeu dois caracteres num só envio: "playbook"→"plabook" e "difícil"→"difíci".

**Técnica nova que isso obrigou a inventar — consertar dois buracos sem um deslocar o outro:** se você conserta o primeiro contando do começo, o texto ganha um caractere e o offset do segundo muda. A solução é **consertar um pela frente e o outro por trás, numa tacada só**:
1. `cmd+Up` + `Right` × N (N contado no texto pretendido, do início) + digitar o caractere → conserta o buraco mais à esquerda.
2. `cmd+Down` + `Left` × M (M = quantos caracteres existem DEPOIS do buraco, contado no fim do texto) + digitar o caractere → conserta o mais à direita.
Como um é medido do início e o outro do fim, a inserção de um não afeta o offset do outro. Funcionou de primeira (N=50 pro "y", M=50 pro "l").

**Régua de conferência que se confirmou de novo:** o zoom no campo pegou os dois erros; o preview do celular à direita serviu de segunda checagem e mostrou a DM final correta antes de salvar. As três passadas do link (Home / 61 setas parando exatamente depois de "manychat" / End) saíram limpas.

**Pegadinha operacional nova, de sessão:** a extensão do Chrome caiu **duas vezes** no meio da edição. Na segunda, a sessão perdeu o navegador selecionado E **a lista de navegadores voltou com outros nomes** — o "Tatsuo Academy" que tinha sido nomeado no `switch_browser` sumiu da lista e apareceu um "Pedro mg3". Não dá pra reconectar por dedução: o certo é rodar `switch_browser` de novo e deixar o user clicar Connect na janela certa (foi o que se fez, e voltou a nomear "Tatsuo Academy"). **O trabalho não se perde** enquanto a automação está STOPPED e o que já foi salvo com "Atualização" está gravado — só o que estava digitado e não salvo fica em risco, e neste caso sobreviveu.

## 04/09/2026 — `IG | 2026-09-04 | JUNTOS | itai doshin` (carrossel 89)

Nona no padrão novo. `utm_campaign=2026-09-04-JUNTOS`; palavra JUNTOS/juntos/Juntos; post específico (capa "funcionário bom não fica só por salário"; conferida no preview do celular); DM "Salário segura ninguém. Quer ver como construir um sonho que faz gente boa querer ficar?" com botão `>> Quero ver <<`. Modelo duplicado: a `IG | 2026-09-03 | RITUAL | ritual de comando`. User avisou "já postei" às ~15h00; LIVE às ~15h08 (dentro dos 5 min contando da criação; o pedido chegou junto com o /etiqueta).

- **Pesquisa da palavra antes de criar:** a busca por "juntos" trouxe só a `IG | 2026-07-31 | PATRIMÔNIO | Risco do emp…` (global; palavra PATRIMÔNIO; o match foi no texto da DM, não na palavra). Sem colisão.
- **Post já indexado na grade:** o carrossel apareceu em 2º na grade (o 1º é sempre o post da automação-modelo). Sem espera desta vez.
- **Bug de comer caractere pela NONA vez:** "um sonho" → "u sonho". Receita determinística de novo: `cmd+Up` + `Right` × 49 + "m". Conferido no zoom antes de salvar.
- **Link:** `End` + `Backspace` × 17 (`2026-09-03-RITUAL`) + `2026-09-04-JUNTOS`. Três passadas: fim OK; início `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=ma…`; `Home` + `Right` × 61 parou depois de "manychat" (prova cruzada OK).
- **Nota de numeração:** a pasta nasceu como `86_itai-doshin` e foi renumerada pra **89** na hora da ficha, porque sessões paralelas já tinham criado 86_pneu-vazio, 87_time-que-voce-nao-prepara e dois 88. Conferir `ls conteudo/carrosseis/` antes de numerar quando há mais de uma sessão aberta.

Décima primeira no padrão novo: `IG | 2026-09-05 | METODO | loja as seis` (carrossel 88; `utm_campaign=2026-09-05-METODO`; palavra em SEIS grafias porque "método" leva acento: `METODO, metodo, Metodo, MÉTODO, método, Método`; DM "Vontade você já tem. O que falta é direção e método. Quer ver como eu ensino isso?" com botão `>> Quero o método <<`). Modelo duplicado: a `IG | 2026-09-05 | OBVIO | o obvio do dono` (mesma data, então só o rabo do UTM mudou: End + Backspace × 5 + METODO; três passadas de conferência OK: Home / Right × 61 parou depois de "manychat" / End). Montada **STOPPED em 04/09 ~19h10, com o post ainda apontando pro 87 (herdado do modelo)**, pra publicação agendada de **05/09 às 17h**. Falta, no dia, com o post no ar e o user avisando "postei": Editar → escolher o carrossel 88 na grade (capa: duas lojas, uma aberta e uma fechada, "O talento acorda às nove") → conferir UTM → Atualização → Ativar. **Colisão checada:** a busca "metodo" no painel só traz a `IG | 2026-08-28 | FOLGA | dois cansacos` (bate pelo texto da DM, palavra dela é folga) — nenhuma automação com palavra METODO, nem global. **O bug de comer caractere bateu de novo** ("método" → "métoo"), e desta vez a receita determinística (`cmd+Up` + `Right` × 49 + "d") **não colou** — o "d" foi comido de novo. O que resolveu de primeira: `find` pra pegar a referência do textarea da DM e `form_input` com o texto inteiro, que grava o valor sem passar pela digitação. **Passa a ser a receita padrão pro campo da DM**: `form_input` direto, zoom pra conferir, e o preview do celular como segunda checagem. O campo do texto do botão e o do link (dentro do modal "Adicionar um link", aberto clicando no botão) aceitaram digitação normal. Pegadinha de viewport: a janela mudou de 1148 pra 1176 px de largura no meio da sessão (depois do Atualização) e o `Ativar` foi pra ~(1085, 32).

**Ativação da METODO (05/09):** user avisou "acabei de postar" às 17h04 (post publicado no horário agendado, 17h). O carrossel 88 já aparecia em SEGUNDO na grade do easy-builder (o primeiro slot é o post que estava selecionado, o 87). Selecionado, preview conferido (capa das duas lojas + legenda "Eu tenho um respeito enorme por quem abre cedo"; o post já tinha 28 curtidas e 2 comentários), UTM sobreviveu à troca de post (End: `2026-09-05-METODO`), Atualização e Ativar: **LIVE às ~17h06**, dois minutos depois do aviso. Pegadinha de viewport: a janela estava em 1512 px de largura nesta sessão; `Editar` em ~(1313, 42), `Ativar` em ~(1395, 42) e, depois de LIVE, `Interromper` ocupa ~(1372, 42): não reaproveitar coordenada.

## 06/09/2026 — `IG | 2026-09-06 | DONO | caminho mais dificil` (carrossel 91)

Décima segunda no padrão novo. `utm_campaign=2026-09-06-DONO`; palavra DONO/dono/Dono (três grafias, sem acento na origem); post específico (capa "Faturou mais e continua duro. O problema não é a venda. É você.", o dono de braços cruzados; conferida no preview do celular, o post já tinha 13 curtidas e 2 comentários); DM "Vender mais não vai te salvar. Saber quanto sobra, sim. Quer ver como eu ensino isso ao dono?" com botão `>> Quero ver <<`. Modelo duplicado: a `IG | 2026-09-05 | METODO | loja as seis`. User avisou "vou postar agora, ativa já" às ~13h05 (o Chrome não estava conectado; ele abriu, `list_connected_browsers` trouxe um único navegador "Tatsuo Academy" macOS, confirmado pelo "Olá, Tatsuo!" e o T laranja). **LIVE às ~13h20.** O post já aparecia em SEGUNDO na grade do easy-builder (o primeiro é sempre o post do modelo).

- **Pesquisa da palavra antes de criar:** "dono" trouxe a `IG | 2026-08-27 | DONO | come antes de voce` (LIVE, post específico, 6 exec.) e quatro que batem só pelo texto (OBVIO, FOME, LEVE, PATRIMÔNIO global de palavra PATRIMÔNIO). Nenhuma global com DONO. Segundo caso de palavra reaproveitada de automação por post específico; sem colisão.
- **Sem bug de comer caractere:** todos os quatro campos (palavra, DM, texto do botão e link) foram escritos com `form_input` na referência do campo, nenhum por digitação. Conferência por zoom em cada um; link conferido no fim (`End`: `…utm_campaign=2026-09-06-DONO`) e no começo (`Home`: `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=ma…`). **Receita que fica:** `read_page` com filtro interativo pra pegar as refs e `form_input` em tudo; o bug só existe na digitação.
- **Pegadinha:** o modal "Adicionar um link" fecha sozinho se outra ferramenta rodar entre abrir e preencher (uma chamada de `find` no meio derrubou as refs `ref_155/156`); reabrir e pegar refs novas (`ref_176/177`) resolveu. Abrir o modal e ler as refs na MESMA batch, preencher na seguinte.
- **Pegadinha de data:** a sessão do carrossel tinha escrito 04/09 na ficha e no UTM planejado; o painel ("METODO modificada há 21 horas") denunciou que o dia era 06/09. Conferir `date` antes de gravar ficha e UTM.
- Viewport nesta sessão: 1295 px; `Editar` em ~(1124, 36) e `Ativar` em ~(1195, 36) na STOPPED; depois de LIVE, `Interromper` em ~(1175, 36).

## 06/09/2026 — `IG | 2026-09-06 | BASICO | repost empresario bobo` (carrossel 92)

Décima terceira no padrão novo. Repost do carrossel "O Empresário Bobo" de 17/03/2026, que tinha CTA COMANDO. **Por que a palavra mudou:** a busca "comando" no painel confirmou a `Comando!! MBV` **LIVE e GLOBAL** ("em alguma publicação ou Reel", 4.892 disparos, 58% CTR) e a `comando repost` (LIVE, post específico, 46 disparos) — qualquer COMANDO no repost dispararia o cano global sem atribuição. Palavra escolhida pelo user: **BÁSICO** (a palavra da moral; a primeira proposta, ARROZ, foi rejeitada por soar piada). Como leva acento, seis grafias: `BASICO, basico, Basico, BÁSICO, básico, Básico`. Busca "basico" e "básico": nenhuma automação com a palavra (só a CONSTANCIA bateu, pelo texto da DM).

`utm_campaign=2026-09-06-BASICO`; DM "O básico dos negócios ninguém te ensinou. Quer ver como eu ensino isso pro dono?" com botão `>> Quero ver <<`. Modelo duplicado: a `IG | 2026-09-06 | DONO | caminho mais dificil` (mesma data: só o rabo do UTM mudou). Montada **STOPPED às ~17h53** com o post ainda apontando pro 91, pra publicação marcada às 18h; timer de shell às 18h02.

- **Sem bug de comer caractere:** os quatro campos por `form_input` (receita da DONO confirmada de novo). Pegadinha: o botão "+ Adicionar Um Link" abre um modal VAZIO e criaria um SEGUNDO botão — pra editar o botão existente é preciso clicar no próprio `>> Quero ver <<`, que abre o mesmo modal já preenchido. Cancelei o vazio antes de salvar.
- Viewport nesta sessão: 1295 px na tela do editor; `Editar` em ~(1120, 35), `Atualização` em ~(1219, 36).

**Ativação (06/09):** o user postou às ~17h50, antes da hora marcada; o "acabei de postar" chegou enquanto a montagem terminava. O carrossel 92 já veio em **primeiro** na grade ao abrir Editar (sem espera de indexação). Post selecionado, preview conferido (capa do Bobo + legenda nova), UTM sobreviveu à troca de post, Atualização e Ativar: **LIVE às ~17h54**, quatro minutos depois do aviso (17h50→17h54). Em LIVE o topo virou `Editar` ~(1120, 35) + `Interromper` ~(1194, 36): não reaproveitar a coordenada do Ativar.

## 07/09/2026 — `IG | 2026-09-07 | DIVIDENDO | emprego caro` (carrossel 94)

Décima quarta no padrão novo. Carrossel externo (10 slides no formato print de tweet, arte e copy do marketing; CTA "dividendo" já impresso no slide 10, então a palavra não era escolha). `utm_campaign=2026-09-07-DIVIDENDO`; palavra DIVIDENDO/dividendo/Dividendo (três grafias, sem acento na origem); DM "Quinze mil no bolso não é lucro, é salário. Quer ver como fazer a empresa te pagar dividendo?" (93 chars) com botão `>> Quero ver <<`. Modelo duplicado: a `IG | 2026-09-06 | BASICO | repost empresario bobo` (data e palavra diferentes: link inteiro trocado por `form_input`). Montada **STOPPED às ~08h27** com o post ainda apontando pro 92, pra publicação marcada às **13h**.

- **Sem bug de comer caractere:** nome (modal Renomear), palavra, DM e link por `form_input`; receita da DONO/BASICO confirmada pela terceira vez.
- **COLISÃO COM GLOBAL LEGADA (segundo caso, depois da MBV):** a busca "dividendo" trouxe a automação `dividendo` — **GLOBAL e LIVE** ("qualquer publicação ou Reel"; `Dividendo, dividendo`; 61 envios / 27 cliques / 44% CTR; modificada há ~2 meses), DM "Para acessar o link da imersão.." com botão `>> Clique Aqui <<` (link da imersão, não o `v2-maio-org`). Ela existe desde ~julho e explica os 61 disparos de posts antigos com esse CTA. No carrossel 94, qualquer "dividendo" comentado cai nas duas; o cano global manda o link errado e sem UTM datado. **Decisão do user (07/09, 08h35): pausar a global** — interrompida pelo Claude na mesma hora (STOPPED; 61 envios / 27 cliques preservados). Só a específica do 94 fica dona da palavra. **Religar a global em ~14/09**, fim da janela do post — mesma rotina da MBV (pausada 29/08, religada 01/09). Regra que já valia e se confirma: pesquisar a palavra no painel ANTES de fechar a ficha — desta vez a palavra veio impressa no slide, então a checagem só podia mudar a decisão sobre a global, não a palavra.
- **Observação de passagem:** `IG | 2026-09-06 | DONO | caminho mais dificil` (carrossel 91, publicado 06/09 ~13h) marcava **0 execuções** às 08h20 de 07/09, enquanto a BASICO (92, publicada 17h50) já tinha 28. Confere com a previsão `abaixo` do 91, mas vale conferir no ritual se a automação está amarrada ao post certo.
- **Ativação:** o post das 13h saiu só às ~14h06. Sete checagens da grade entre 13h01 e 13h51 sem o post (cada uma: navegar → esperar ~18 s → Editar → olhar a grade → Cancelar sem salvar); no meio entrou um Reel ("matéria tendenciosa"), que teria roubado um gatilho "próxima publicação" — mais um ponto pra regra do post específico. Às 14h07 o carrossel estava em SEGUNDO na grade e o "postei" do user chegou junto. Selecionado, preview conferido (capa + legenda), UTM sobreviveu (End: `2026-09-07-DIVIDENDO`), Atualização, Ativar: **LIVE às ~14h09**, ~3 min depois da publicação.
- Viewport nesta sessão: 1564 px; na STOPPED `Editar` em ~(1378, 39) e `Ativar` em ~(1456, 39); no modo edição `Cancelar` ~(1373, 39) e `Atualização` ~(1483, 39). Menu `⋮` da lista em x≈1472 (aparece no hover); Renomear a +53 px abaixo do `⋮`, Duplicar a +96.

## 08/09/2026 — `IG | 2026-09-08 | RECOMPENSA | repost pressao` (carrossel 97)

Décima quinta no padrão novo. Repost estendido da copy de 26/07/2025 (16 slides refeitos no editorial-punch; CTA original era COMANDO, palavra da global legada). `utm_campaign=2026-09-08-RECOMPENSA`; palavra RECOMPENSA/recompensa/Recompensa; DM "Pressão você já aguenta. Quer ver como ser pago pelo risco que corre?" (69 chars) com botão `>> Quero ver <<`. Modelo duplicado: a `IG | 2026-09-07 | ESTRUTURA | repost cansado demais` (link `v2-maio-org` conferido). Post publicado à mão pelo user ~15h45; o "postei" veio junto com o pedido de ativação. Montada e ativada na sequência: **LIVE ~15h45**, dentro dos 5 minutos.

- **Colisão checada:** a busca "recompensa" só devolve a RISCO (03/09), porque a DM dela contém "recompensado"; palavra RISCO, não dispara. Sem global com essa palavra.
- **Sem bug de comer caractere** (nome, palavra, DM e link por `form_input`; quinta automação seguida limpa).
- Grade "Mostrar Todos" trouxe o carrossel em PRIMEIRO com "há 4 minutos": confirmação de publicação sem tocar na API.
- Viewport nesta sessão: 1232 px. Na lista, `⋮` da linha em x≈1138 (hover); Renomear a +47 px, Duplicar a +85. Na automação STOPPED: `Editar` ~(1069, 34), `Ativar` ~(1137, 34); em edição `Atualização` ~(1160, 34). O clique em Ativar deixou o `browser_batch` sem resposta por >60 s, mas a ativação tinha pegado (botão "Interromper" no screenshot seguinte): quando a ferramenta estourar o tempo, conferir o estado antes de repetir o clique.
- Pendente: `/etiqueta` do 97 (ficha em `registro-posts.csv`, `data_publicacao` 2026-09-08).

## 08/09/2026 — `IG | 2026-09-08 | NUMERO | repost comeca assim` (carrossel 98)

Décima sexta no padrão novo. Repost da copy de 22/07/2025 (`DMax_pfRD9b`, 119,7 interações/1k, 393 comentários; CTA original COMANDO, palavra da global legada). 13 slides refeitos no editorial-punch. `utm_campaign=2026-09-08-NUMERO`; palavra em SEIS grafias porque "número" leva acento: `NUMERO, numero, Numero, NÚMERO, número, Número`; DM "Fazer você já sabe. Quer ver como enxergar a empresa pelo número e decidir?" (75 chars) com botão `>> Quero ver <<`. Modelo duplicado: a `IG | 2026-09-08 | RECOMPENSA | repost pressao` (mesma data: só o rabo do UTM mudou, link trocado inteiro por `form_input`). O "postei" do user chegou junto com o pedido; montada e ativada na sequência: **LIVE ~17h10**.

- **Palavra escolhida pelo user** entre duas que ele propôs (LUZ ou NUMERO); a proposta inicial da skill era ENXERGAR. NUMERO é o que a peça ganha antes do CTA ("o número na mesa", "enxergar a empresa pelo número").
- **Colisão checada:** "numero" não devolve nada; "número" devolve só a `IG | 2026-08-26 | PATRAO | cliente virou patrao` (bate pelo texto da DM; palavra PATRAO, post específico). Sem global.
- **Sem bug de comer caractere** (nome no modal Renomear, palavra, DM e link por `form_input`; sexta automação seguida limpa).
- A URL nua `cms/easy-builder` (sem id) abre uma automação NOVA em branco, não a lista — a lista é o ícone Automação da barra lateral (`/fb2015128/cms`). Saí sem salvar.
- Grade do editor já trazia o carrossel 98 em PRIMEIRO (capa "Todo empreendedor no Brasil COMEÇA ASSIM:") ao abrir Editar; preview do post e dos comentários conferidos com a capa certa.
- Viewport nesta sessão: 1197 px na captura (1295 no DOM). Na lista, `⋮` da linha em x≈1119 (hover); Renomear a +47 px, Duplicar a +82. Na automação STOPPED: `Editar` ~(1038, 33), `Ativar` ~(1104, 33); em edição `Atualização` ~(1127, 33). O `browser_batch` estourou o tempo no clique em Duplicar, mas a duplicata tinha sido criada (conferir antes de repetir, como no 97).
- URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260908200650_165549
- Etiqueta do 98 gravada na mesma sessão (mediana 58.0-79.0).

## 09/09/2026 — `IG | 2026-09-09 | SUCESSAO | passar a caneta` (carrossel 104)

Décima sétima no padrão novo. Primeira peça da Onda 1 do briefing de sucessão familiar do Rodrigo (par com o 103, ainda em rascunho). `utm_campaign=2026-09-09-SUCESSAO`; palavra em SEIS grafias porque "sucessão" leva acento: `SUCESSAO, sucessao, Sucessao, SUCESSÃO, sucessão, Sucessão`; DM "Passar a caneta sem perder o comando começa com a regra no papel. Quer ver como eu ensino isso?" (96 chars) com botão `>> Quero <<`. Modelo duplicado: a `IG | 2026-09-08 | NUMERO | repost comeca assim` (data diferente: link trocado inteiro por `form_input`). O "postei" do user chegou junto com o pedido de etiqueta + Manychat; montada e ativada na sequência: **LIVE ~16h10**, com o post publicado ~16h03 (a grade dizia "há 2 minutos").

- **Palavra escolhida pelo user** (a proposta da skill era CANETA). É o nome do tema, não o estado desejado; vale como identificador da onda de teste de sucessão.
- **Colisão checada:** a busca "sucess" no painel não devolve nada. Sem global, sem específica.
- **Sem bug de comer caractere** (nome no modal Renomear, palavra, DM, botão e link por `form_input`; sétima automação seguida limpa). Link conferido em três passadas (Home / Right × 61 parou depois de "manychat" / End).
- Grade do editor já trazia o carrossel 104 em PRIMEIRO ao abrir 'Mostrar Todos' ("A briga da fábrica vai…", capa "Dar o cargo pro filho é fácil / DIFÍCIL É PASSAR A CANETA"); preview do post e dos comentários conferidos.
- Seleção de navegador pelo `switch_browser` (user clicou Conectar e nomeou "Tatsuo Academy"); T laranja conferido na barra lateral antes de mexer.
- Viewport nesta sessão: 1197 px. Na lista, `⋮` da linha em x≈1119; menu: Renomear ~+46 px, Duplicar ~+83 px abaixo. STOPPED: `Editar` (1038, 33), `Ativar` (1104, 33); em edição `Atualização` (1127, 33); modal do botão: `Salvar` (765, 242).
- URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260909190630_431273
- Etiqueta do 104 gravada antes (mediana 52.0-78.0) e `data_publicacao=2026-09-09` preenchida nesta sessão.

## 09/09/2026 — `IG | 2026-09-09 | DIAGNOSTICO-1 | repost cabeca de dono` (carrossel 100)

Décima sétima no padrão. **Primeira do caminho DIAGNÓSTICO** (regra do user de 09/09: três caminhos de CTA, diagnóstico gratuito / imersão / isca). Novidades de operação: palavra **fixa** do caminho (`DIAGNOSTICO, diagnostico, Diagnostico, DIAGNÓSTICO, diagnóstico, Diagnóstico`), link `https://rtc.tatsuoacademy.com/diagnostico` (o da bio) e **UTM numérico sequencial** em vez de datado: `utm_campaign=1`. Nome da automação carrega o código (`DIAGNOSTICO-1`). DM "Talvez o mediano seja você. Quer descobrir? Diagnóstico gratuito com um especialista." (85 chars), botão `>> Quero ver <<`. Publicação marcada pelo user pra **19h**; montada STOPPED às ~16h35 com o post do modelo (98), timer de shell às 19h pra amarrar e ativar.

- **Colisão:** só a `DIAGNOSTICO ANIVERSARIO TATSUO` (LIVE, post específico, 7 exec.). Sem global. Como a palavra vai se repetir em todo post do caminho, a checagem passa a ser "existe global com DIAGNOSTICO?", não "a palavra é inédita".
- **`form_input` não gravou no modal do botão** (título e link reverteram ao salvar). Digitação (`cmd+a` + `type`) resolveu; o campo do título tem **teto de 20 caracteres** (`>> Quero o diagnóstico <<` recusado). Palavra e DM continuam por `form_input`.
- Modelo duplicado: `IG | 2026-09-08 | NUMERO | repost comeca assim`. Domínio do link trocado inteiro.
- Viewport 1197→1226 px; coordenadas no kit.

## 09/09/2026 — `IG | 2026-09-10 | LIDER | so o time nomeia` (carrossel 105) — MONTADA STOPPED, ativar 10/09 17h (era 13h; mudado pelo user em 10/09)

Décima oitava no padrão novo. Montada na véspera pra publicação marcada em **10/09 às 17h** (antes 13h); o user avisa e o Claude amarra ao post + ativa (conversa renomeada "Carrossel 105 LIDER — postar 10/09 17h (ativar Manychat)"). `utm_campaign=2026-09-10-LIDER`; palavra em SEIS grafias porque "líder" leva acento: `LIDER, lider, Lider, LÍDER, líder, Líder`; DM "Dono você já é. Quer ver como montar a rotina que faz o time te chamar de líder?" (80 chars) com botão `>> Quero ver <<`. Modelo duplicado: a `IG | 2026-09-09 | SUCESSAO | passar a caneta` (data diferente: link trocado inteiro por `form_input`). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260909192422_579834

- **Colisão checada:** a busca "lider" devolve a global legada **`lider`** (STOPPED há 3 meses, 717 exec., 45,5% CTR, "qualquer publicação", grafias Líder/líder/LIDER/Lider/lider). Parada, não dispara; não mexer nela. Também devolveu a FIRME (sem relação, match de outro campo).
- **Post ainda apontando pro do modelo (104)** — regra de 31/08: amarrar ao post específico DEPOIS de publicado, com o user presente. Checklist de amanhã: Editar → alternar o rádio pra "qualquer" e voltar pra "específico" (reseta a grade) → 'Mostrar Todos' → selecionar a capa "Dono, você se nomeou sozinho / LÍDER, SÓ O TIME NOMEIA" (pescadores olhando pro mestre) → conferir preview → Atualização → Ativar → print. Preencher `data_publicacao=2026-09-10` na ficha do 105.
- **Sem bug de comer caractere** (palavra, DM, botão e link por `form_input`; oitava seguida limpa). Link conferido em três passadas (Home / Right × 61 parou depois de "manychat" / End = `2026-09-10-LIDER`).
- **Pegadinha da lista:** com a busca limpa, clicar em (1119, y) da linha abriu a automação em vez do menu; o `⋮` desta viewport (1226 px) fica em **x≈1147**, só aparece no hover. Dentro de automação LIVE o `⋮` do topo só tem "Apagar" — o Duplicar vive só no menu da lista. STOPPED: `Editar` (1063, 33), `Ativar` (~1132, 33); em edição `Atualização` (1155, 33); modal do link: `Salvar` (783, 247).
- A `IG | 2026-09-09 | DIAGNOSTICO-1 | repo…` (STOPPED, criada minutos antes por outra sessão) é do 100; não é desta conversa.

## 09/09/2026 — `IG | 2026-09-09 | PREPARO | kongo gumi reel` (reel de copy produzido, Lote 2 R3)

Décima nona no padrão novo; primeiro reel de copy produzido montado nesta rotina desde a CULTURA de 25/08. Palavra do roteiro (PREPARO, três grafias); `utm_campaign=2026-09-09-PREPARO`; DM "Empresa que dura não é sorte, é preparo. Quer ver como eu ensino isso na Imersão MBV?" (85 chars), botão `>> Quero ver <<`, link `v2-maio-org` (caminho imersão, como manda a promessa do roteiro). Modelo duplicado: a `IG | 2026-09-09 | SUCESSAO | passar a caneta` (mesma data: End + Backspace × 8 + PREPARO). Kit em `conteudo/videos/2026-09-09_kongo-gumi/`.

- **Colisão checada:** "preparo" devolve só as duas específicas (87 de 04/09, 18 exec.; genchi genbutsu 20/08, 62 exec.). Terceira automação com a palavra, todas específicas; sem global.
- **Sem bug de comer caractere:** palavra e DM por `form_input`; no modal do botão, título por `cmd+a` + digitação e link por `End` + 8 backspaces + `PREPARO` (receita da DIAGNOSTICO-1: o modal não grava `form_input`). Três passadas do link OK (Home / Right × 61 parou depois de "manychat" / End).
- **Legenda:** o user pediu a legenda do vídeo junto com o Manychat. Entreguei primeiro uma legenda desenvolvida (1390 chars, no molde das de carrossel) e foi reprovada na hora: **a legenda de reel de copy produzido é a que está no documento de roteiros, curta** ("1.400 anos de empresa vs. 5 anos... Digita PREPARO..."). Regra: pra reel de roteiro, entregar a LEGENDA e o COMENTÁRIO FIXADO do próprio roteiro, sem reescrever.
- Montada STOPPED ~18h45 com o post ainda no 104 (modelo); o reel não estava na grade (mais recente "há 3 horas"). Amarrar + ativar após o "postei".
- Viewport 1197 px: lista `⋮` em x≈1119 (Renomear +45, Duplicar +82); STOPPED `Editar` (1038, 33), `Ativar` (1104, 33); edição `Atualização` (1127, 33); modal do link `Salvar` (765, 242); 'Mostrar Todos' (149, 299); X do modal da grade (910, 42).
- **Ativação (09/09):** "postei" às ~18h50. A grade NÃO trazia o reel nas três primeiras checagens (mais recente "há 3 horas"), nem depois de alternar o rádio global→específico; apareceu em PRIMEIRO ~10 min depois da publicação ("1.400 anos de empre… há 12 segundos"). Selecionado, preview conferido (capa Kongo Gumi + legenda do roteiro), UTM sobreviveu (End: `2026-09-09-PREPARO`), Atualização (~30 s) e Ativar: **LIVE ~19h02**. Reel demora mais que carrossel pra indexar na grade (aqui ~10 min contra ~4 do carrossel 83). Pegadinha de sessão: a extensão do Chrome caiu entre o STOPPED e o "postei"; `switch_browser` estourou o tempo sem o user ver a confirmação, e `list_connected_browsers` já trazia o "Tatsuo Academy" (ee5937df) reconectado — `select_browser` nele resolveu (T laranja conferido). Batch com mais de ~90 s de waits estoura o tempo da ferramenta: manter cada batch abaixo de ~60 s.
- **Ativação (09/09):** post publicado ~19h18 (marcado 19h; o user avisou 19h23), carrossel em PRIMEIRO na grade "Mostrar Todos". UTM `=1` sobreviveu à troca de post. **LIVE ~19h25**. Pegadinha nova: na página rolada, clique em y≈872 cai no "+ Adicionar Um Link" (modal vazio = segundo botão); o botão existente fica em y≈820. Fechar no X sem salvar. Segunda pegadinha: `browser_batch` com >9 esperas de 10 s estoura; esperar com `until` no shell.

## 10/09/2026 — `IG | 2026-09-10 | PEQUENO | outro bicho` (carrossel 107) — MONTADA STOPPED às 09h05, publicação marcada 13h

Vigésima no padrão novo. Caminho **imersão MBV**; `utm_campaign=2026-09-10-PEQUENO`; palavra em TRÊS grafias (sem acento na origem): `PEQUENO, pequeno, Pequeno`; DM "O manual do grande não cabe em você. Quer o arroz com feijão da gestão feita pro seu tamanho?" (94 chars) com botão `>> Quero <<`. Modelo duplicado: a `IG | 2026-09-10 | LIDER | so o time nomeia` (STOPPED, do 105; mesma data, então só o rabo do UTM mudou: End + Backspace × 5 + PEQUENO). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260910120001_383784

- **Colisão checada:** a busca "pequeno" devolve só a global legada `Auto-DM de links dos comentários` (STOPPED há 1 ano, palavra "comando"; match por outro campo). Sem global viva, sem específica.
- **Post ainda apontando pro do modelo (104, herdado da LIDER)** — regra de 31/08: amarrar ao post específico depois de publicado. Checklist das 13h: Editar → alternar o rádio pra "qualquer" e voltar pra "específico" (reseta a grade) → 'Mostrar Todos' → selecionar a capa "TE VENDERAM QUE / SER PEQUENO É DEFEITO" (pinscher olhando pro São Bernardo na mesa de tosa) → conferir preview (legenda começa "Empresa de quinhentos milhões tem gestor") → Atualização → Ativar → print. Timer de shell armado pras 13h00 como fallback; o "postei" do user continua sendo o gatilho.
- **Sem bug de comer caractere** (nome no modal Renomear por cmd+a + digitação; palavra e DM por `form_input`; botão por cmd+a + digitação; link por End + 5 backspaces). Link conferido em três passadas (Home / Right × 61 parou depois de "manychat" / End = `2026-09-10-PEQUENO`).
- Navegador: `switch_browser` estourou os 2 min sem clique; `list_connected_browsers` trazia o macOS `ee5937df` (mesmo id do "Tatsuo Academy" de ontem) → `AskUserQuestion` com os 3 conectados, user escolheu o Browser 1, T laranja conferido no primeiro screenshot.
- Viewport 1199 px: o "<" do topo (89, 27) mandou pra aba em branco (chrome://), navegar direto em `/fb2015128/cms`; lista `⋮` em x≈1121 no hover (Renomear +45, Duplicar +82); STOPPED `Editar` (1038, 33), `Ativar` (1104, 33); edição `Atualização` (1127, 33); botão existente em y≈852 depois de 10 ticks de scroll; modal do link `Salvar` (765, 242).
- Etiqueta do 107 já com `data_publicacao=2026-09-10` (mediana 55.0-78.0).
- **Ativação (10/09):** o timer das 13h00 acordou o Claude sem "postei" do user. A seleção de navegador tinha caído (lista voltou com 4 Chromes; `AskUserQuestion` obrigatório, user escolheu o `ee5937df` de novo; T laranja conferido). Em Editar, a grade já trazia o carrossel 107 em SEGUNDO (o primeiro slot mostra o post do modelo, o 104): capa "TE VENDERAM QUE / SER PEQUENO É DEFEITO" com 29 curtidas e 2 comentários, ou seja, publicado antes das 13h. Selecionado, preview conferido (capa + legenda "Empresa de quinhentos milhões tem gestor…"), UTM sobreviveu à troca de post (End: `2026-09-10-PEQUENO`, e o tooltip do botão mostra o link inteiro), Atualização e Ativar: **LIVE ~13h20** (o relógio da sessão marcava 13h21 logo depois do print). Sem precisar alternar o rádio global→específico desta vez: o post já estava indexado. Viewport nesta sessão 1204×989: `Editar` (1040, 34), `Atualização` (1131, 34), `Ativar` (1108, 34); o primeiro clique em Editar depois do `navigate` não pegou (pegadinha conhecida), o segundo sim. O `switch_browser` da manhã tinha estourado os 2 min; a seleção por id + T laranja resolveu nas duas vezes.

**Ativação da LIDER (10/09):** horário mudou de 13h pra 17h de manhã (UTM datado, nada a trocar). O "postei, ativa o manychat" chegou com o post já há ~31 min na grade do easy-builder ("Tem dois títulos dent…", capa dos pescadores, em PRIMEIRO no 'Mostrar Todos'). Fluxo: `switch_browser` → T laranja → Editar → 'Mostrar Todos' → clicar no 105 (a grade direta já tinha o 105 em primeiro; não precisou resetar o rádio) → preview conferido (capa + legenda) → Atualização → Ativar → **LIVE ~17h32** ("Sua automação está pronta e funcionando"). Viewport 1176 px nesta sessão: `Editar` (1015, 33), `Atualização` (1106, 33), `Ativar` (1082, 33). Ficha do 105 com `data_publicacao=2026-09-10`.

## 11/09/2026 — `IG | 2026-09-11 | DIAGNOSTICO-3 | banco financia a quebra` (carrossel 106) — MONTADA STOPPED ~12h58, user posta em seguida

Vigésima primeira no padrão novo; terceira do caminho DIAGNÓSTICO (100 = 1, 103 = 2 ainda não montada, 106 = 3, 111 = 4 ainda não montada). Palavra fixa nas 6 grafias; link `https://rtc.tatsuoacademy.com/diagnostico?utm_source=manychat&utm_medium=dm&utm_campaign=3`; DM "Você sabe a parcela de cor. E se a sua conta fecha? Diagnóstico gratuito com um especialista." (95 chars) com botão `>> Quero ver <<`. **Modelo duplicado: a DIAGNOSTICO-1** (mesmo domínio e mesmas grafias: só nome, DM e o último caractere do UTM mudaram — a duplicação mais barata do caminho; vale como regra pros próximos posts de diagnóstico). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260911155625_241974. Kit em `conteudo/carrosseis/106_nao-foi-dinheiro/manychat/kit-dm.md`.

- **Colisão checada:** "diagnos" devolve só a DIAGNOSTICO-1 (LIVE, específica, 2 exec., 50% CTR) e a `DIAGNOSTICO ANIVERSARIO TATSUO` (LIVE, específica, 7 exec.). Sem global.
- **Sem bug de comer caractere** (nome por cmd+a + digitação; DM por `form_input`; link por End + Backspace + `3`). Três passadas do link OK.
- Post ainda apontando pro do modelo (100). Fluxo do "postei": Editar → 'Mostrar Todos' → capa "O BANCO NÃO QUEBRA SUA EMPRESA / ELE SÓ FINANCIA A QUEBRA" (parede rachada com escoras) → preview (legenda "Eu vou te contar como a maioria das empresas pequenas quebra") → UTM `=3` no End → Atualização → Ativar → print. Preencher `data_publicacao` na ficha do 106.
- Navegador: `list_connected_browsers` com 4 Chromes (3 macOS + 1 Windows de colega); `AskUserQuestion` obrigatório, user escolheu o `ee5937df` (Browser 4). T laranja conferido.
- Viewport: lista 1201 px (⋮ em x≈1122; Renomear +46, Duplicar +84); automação 1232 px: `Editar` (1068, 34), `Ativar` (1136, 34), `Atualização` (1160, 34); modal do link `Salvar` (790, 251).
- Etiqueta do 106 já gravada em 09/09 (mediana 52.0-78.0, UTM 3); falta só a `data_publicacao`.
- **Ativação (11/09):** "postei agora" ~13h00; a grade 'Mostrar Todos' já trazia o 106 em PRIMEIRO ("Eu vou te contar com…", há 56 segundos; carrossel indexa em <1 min). Preview conferido (capa das escoras + legenda), UTM `=3` intacto no End, Atualização, Ativar: **LIVE ~13h03**, ~3 min após a publicação. Ficha do 106 com `data_publicacao=2026-09-11`. Viewport 1232 px: `Editar` (1068, 34), `Atualização` (1160, 34), `Ativar` (1136, 34); 'Mostrar Todos' (155, 311); primeiro card da grade (403, 255); X do modal do link (816, 50).

## 11/09/2026 — `IG | 2026-09-11 | DIAGNOSTICO-4 | quebra com a loja cheia` (carrossel 111) — MONTADA STOPPED ~14h02, publicação marcada 17h

Vigésima segunda no padrão novo; quarta do caminho DIAGNÓSTICO (a DIAGNOSTICO-2 do 103 segue sem montar). Palavra fixa nas 6 grafias; link `https://rtc.tatsuoacademy.com/diagnostico?utm_source=manychat&utm_medium=dm&utm_campaign=4`; DM "Vende como nunca e não sobra? Quer saber em quantos dias a venda vira dinheiro? Diagnóstico gratuito." (103 chars) com botão `>> Quero ver <<`. Modelo duplicado: a DIAGNOSTICO-3 (mesma data, mesmo domínio: só nome, DM e o último caractere do UTM). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260911165951_695661. Kit em `conteudo/carrosseis/111_loja-cheia/manychat/kit-dm.md`.

- Colisão: a mesma checagem de ~12h55 (só específicas com DIAGNOSTICO). Sem global.
- Sem bug de comer caractere (nome por cmd+a + digitação; DM por `form_input`; link por End + Backspace + `4`). Três passadas do link OK.
- Post ainda apontando pro do modelo (106). Amarrar + ativar após o "postei" das 17h; timer de shell às 17h como fallback (o "postei" do user continua sendo o gatilho).
- Segunda automação da mesma sessão de navegador: a seleção do Chrome (`ee5937df`) sobreviveu ao fechamento da aba do 106 — não precisou de `AskUserQuestion` de novo.
- **Ativação (11/09):** o user postou antes da hora marcada e avisou "postei, cria o Manychat" às ~16h52, em OUTRA sessão (a do carrossel), não na que montou a automação. Fluxo: `list_connected_browsers` com 5 Chromes (3 macOS locais + 2 Windows de colegas), `AskUserQuestion` obrigatório, user escolheu de novo o `ee5937df`; T laranja conferido. Navegar na URL da automação → Editar (1040, 33 em 1201 px) → o carrossel 111 já estava em PRIMEIRO na grade de 4 (capa do dono olhando a gaveta vazia com os clientes em volta) → selecionado, preview conferido (capa + legenda "Toda vez que eu falo que empresa não quebra…") → modal do link: End `utm_campaign=4`, Home + Right×61 parou depois de `manychat` → X → Atualização (1160, 34 em 1232 px) → Ativar (1107, 33 em 1201 px): **LIVE ~16h57**, ~5 min depois do aviso. Ficha do 111 com `data_publicacao=2026-09-11`. Pegadinha: a largura do viewport oscilou entre 1201 e 1232 px de um screenshot pro outro na mesma aba; conferir a coordenada no print antes de cada clique do topo. O timer de shell das 17h da sessão que montou a automação ficou órfão: avisada por mensagem entre sessões pra não tocar na automação (o risco é clicar em `Interromper` no lugar de `Editar` numa automação LIVE).

## 11/09/2026 — `IG | 2026-09-11 | GENTE | google aristoteles reel` (reel de copy produzido, Lote 2 Cases "contrate por caráter") — LIVE ~19h14

Vigésima terceira no padrão novo; segundo reel de copy produzido nesta rotina (o primeiro foi o Kongo Gumi de 09/09). Palavra do roteiro GENTE em TRÊS grafias (`GENTE, gente, Gente`); `utm_campaign=2026-09-11-GENTE`; caminho **imersão MBV** (link `v2-maio-org`, promessa do roteiro); DM "Contrate por caráter, treine a técnica. Quer ver como eu monto time assim na Imersão MBV?" (92 chars), botão `>> Quero ver <<` herdado. Modelo duplicado: a `IG | 2026-09-09 | PREPARO | kongo gumi reel` (mesmo domínio: End + Backspace × 18 + `2026-09-11-GENTE`). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260911221024_844794. Kit e legenda em `conteudo/videos/2026-09-11_google-aristoteles/`.

- **Legenda entregue primeiro, literal do documento de roteiros** (regra de 09/09): "Buffett, Google e Amazon contratam pelo mesmo critério — e não é competência. Quer montar seu time assim, comigo? Digita GENTE que eu te mando os detalhes da Imersão MBV. 👇" + comentário fixado "Digita GENTE que os detalhes chegam no seu direct."
- **Colisão checada:** "gente" é a palavra bagunçada do baseline de 18/08 e continua assim: `#GENTE mbv` segue LIVE e GLOBAL, mas só casa com cerquilha (`#gente/#Gente/#GENTE`); a global antiga `GENTE` (sem cerquilha) está STOPPED há 6 meses; `GENTE mbv ESPECIFICO` é específica de outro post. Comentário "GENTE" sem cerquilha cai só na automação nova. Se alguém comentar "#gente", vai pra global velha (link antigo): risco pequeno, anotado.
- **Sem bug de comer caractere** (nome por cmd+a + digitação; palavra e DM por `form_input`; link por End + 18 backspaces). Três passadas do link OK.
- **Reel indexou rápido desta vez:** o "postei" chegou ~19h05 com o reel já há ~15 min no ar, e a grade 'Mostrar Todos' o trazia em PRIMEIRO na primeira abertura (capa ainda borrada, em processamento). Contra os ~10 min do Kongo Gumi: a diferença é o intervalo entre publicação e montagem, não o tipo de post.
- Navegador: 2 Chromes na lista (`ee5937df` e `46b005d2`, ambos macOS); `AskUserQuestion` obrigatório, user escolheu o `ee5937df`; T laranja conferido. O `Ativar` funcionou de primeira (sem o clique perdido pós-navigate).
- **Kongo Gumi (PREPARO) marca 0 execuções na lista após 2 dias.** Vale conferir no ritual se os Insights estão atrasados ou se ninguém comentou PREPARO no reel.
- Viewport 1282 px: lista `⋮` em x≈1198 (Renomear +49, Duplicar +89); STOPPED `Editar` (1110, 36), `Ativar` (1181, 36); edição `Atualização` (1206, 36); 'Mostrar Todos' (162, 324); modal do link `Salvar` (821, 262).
- Etiqueta do reel pendente (não pedida nesta conversa).

## 12/09/2026 — `IG | 2026-09-12 | DIAGNOSTICO-5 | o seu CPF nao e limitado` (carrossel 114) — LIVE ~13h25, montada e ativada de uma vez após o "postei"

Vigésima quarta no padrão novo; quinta do caminho DIAGNÓSTICO (100 = 1, 103 = 2 sem montar, 106 = 3, 111 = 4, 114 = 5). Palavra fixa nas 6 grafias; link `https://rtc.tatsuoacademy.com/diagnostico?utm_source=manychat&utm_medium=dm&utm_campaign=5`; DM "Sua empresa é limitada, o seu CPF não é. Quer saber se ela te paga pelo risco? Diagnóstico gratuito." (100 chars) com botão `>> Quero ver <<` herdado. Modelo duplicado: a DIAGNOSTICO-4 (só nome, DM e o último caractere do UTM). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260912162254_957144. Kit em `conteudo/carrosseis/114_limitada/manychat/kit-dm.md`.

- Colisão: "diagnos" devolve DIAGNOSTICO-4 (LIVE, 2 exec., 0% CTR), -3 (5 exec., 80%), -1 (2 exec., 50%) e a do aniversário, todas específicas. Sem global.
- O "postei" chegou com o post já ~2 min na grade: 'Mostrar Todos' trazia o 114 em PRIMEIRO ("Tem uma palavra na…", há 2 minutos), com 1 curtida e 2 comentários no preview. Selecionado, preview conferido (capa "Sua empresa é limitada? / O SEU CPF NÃO É." + legenda), DM por `form_input`, link End + Backspace + `5` (End e Home conferidos), Salvar, Atualização, Ativar: LIVE.
- Navegador: 2 Chromes na lista (`ee5937df` "Tatsuo Academy" macOS + 1 Windows de colega); `AskUserQuestion` obrigatório, user escolheu o `ee5937df`; T laranja conferido.
- Viewport oscilou entre 1503 e 1440 px na mesma aba. Em 1503: lista `⋮` (1415, 416), Duplicar (1367, 508), Renomear (1373, 466), modal Renomear (926, 265). Em 1440: STOPPED `Editar` (1269, 36), `Ativar` (1340, 36); edição `Atualização` (1364, 36); 'Mostrar Todos' (162, 324); primeiro card da grade (498, 235); botão do link (235, 553) após 10 ticks; modal `Salvar` (899, 262).
- Ficha do 114 com `data_publicacao=2026-09-12`.

## 12/09/2026 — `IG | 2026-09-12 | AUTOMATICO | todas as vezes` (carrossel 115) — LIVE ~17:12, montada e ativada de uma vez após o "postei"

Vigésima quinta no padrão novo. Caminho **imersão MBV**; `utm_campaign=2026-09-12-AUTOMATICO`; palavra em SEIS grafias porque "automático" leva acento: `AUTOMATICO, automatico, Automatico, AUTOMÁTICO, automático, Automático`; DM "Quer o time fazendo certo sem você em cima? O rito que ensino no treinamento está aqui:" (87 chars) com botão `>> Quero o rito <<`. Modelo duplicado: a `IG | 2026-09-10 | LIDER | so o time nomeia` (LIVE, 4 exec.; mesma estrutura de 6 grafias; data diferente, link trocado inteiro por `form_input`). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260912200914_481851. Kit em `conteudo/carrosseis/115_todas-as-vezes/manychat/kit-dm.md`.

- **Colisão checada:** a busca "automatico" devolve só a `IG | 2026-08-26 | PILOTO | piloto automatico` (LIVE, post específico, palavra PILOTO; match pelo nome). Sem global, sem específica com a palavra.
- O "postei" chegou ~17h07; 'Mostrar Todos' trazia o 115 em PRIMEIRO ("Tem uma frase que to…", há 2 minutos) com a capa v2 (pergunta em duas linhas + TODAS). Preview conferido (capa + legenda "Tem uma frase que todo dono de empresa já disse…"), 0 curtidas e 2 comentários no preview.
- **Sem bug de comer caractere**: nome no modal Renomear por cmd+a + digitação; palavra, DM, botão e link por `form_input`. Link conferido em três passadas (End = `…2026-09-12-AUTOMATICO` / Home + Right × 61 parou exatamente depois de "manychat").
- Navegador: 3 Chromes na lista (`46b005d2` macOS, `ee5937df` macOS "Tatsuo", `bce20a66` Windows de colega); `AskUserQuestion` obrigatório, user escolheu o `ee5937df`; T laranja conferido no primeiro screenshot.
- Viewport 1503 px na lista: `⋮` (1415, 416) no hover, Renomear (1373, 466), Duplicar (1367, 508), modal Renomear (926, 265). Dentro da automação a viewport passou a 1564×784: STOPPED `Editar` (1324, 38) → em edição `Atualização` (1483, 40), `Ativar` (1455, 40); 'Mostrar Todos' (169, 338 antes / 177, 352 depois); primeiro card da grade (541, 290); botão do link em y≈600 após 10 ticks; modal `Salvar` (978, 285).
- Ficha do 115 com `data_publicacao=2026-09-12`.

## 12/09 — primeira automação de STORY: `RAIO - X stories`

Pedido do user: a `RAIO - X` (criada por ele em 12/09, gatilho global "qualquer publicação", palavra raio-x em 7 grafias, DM "Quer um raio-x da sua empresa para saber onde está \"sumindo\" seu lucro?", botão `>> Quero saber <<`, link `https://tatsuoacademy.com/raio-x-empresa-lucrativa/` sem UTM) responde só a comentário em post; ele queria o mesmo pra resposta de story.

**Como se faz (não é "duplicar"):** a duplicata de uma automação de comentário nasce com o gatilho de comentário travado no easy-builder — não dá pra trocar pra story. O caminho é `Nova Automação` → modelo **"Gere leads com stories"** (Quick Automation, `campaign_type=easy_builder_story_reply_multi_links`). O formulário é o mesmo da de comentário, só que o gatilho é "Quando alguém responder: qualquer story / um story específico" e "E essa resposta contém: palavras ou reações específicas / qualquer". Preencher palavra, DM, `Adicionar Um Link` (texto do botão + URL) → Salvar → Ativar. Nasce com nome padrão "Turn story replies into leads"; renomear na lista pelo `⋮`.

**Resultado:** `RAIO - X stories`, LIVE às ~17h20, qualquer story, mesmas 7 grafias, mesma DM, mesmo botão e mesmo link (conferido reabrindo o modal do link depois de ativar). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20250423134755_303293. Tudo preenchido por `form_input` — o bug de comer caractere não bateu (ele só aparece com `type`).

**Fica registrado:** gatilho de story existe em duas versões, "qualquer story" (usado aqui, espelhando a RAIO - X que é global) e "um story específico" (exige story no ar na hora). Story dura 24 h, então "específico" só faz sentido montado depois de publicar o story.

**Complemento 12/09 (~17h30) — UTM nas duas RAIO - X**, a pedido do user, pra separar clique de feed e de story no site:
- `RAIO - X` (feed, global): `https://tatsuoacademy.com/raio-x-empresa-lucrativa/?utm_source=manychat&utm_medium=dm&utm_campaign=raio-x-feed`
- `RAIO - X stories`: `https://tatsuoacademy.com/raio-x-empresa-lucrativa/?utm_source=manychat&utm_medium=dm&utm_campaign=raio-x-stories`

Editado pelo modal do link (ícone de corrente ao lado do botão, não o "Adicionar Um Link", que cria um segundo botão), link por `form_input`, Salvar, Atualização; as duas seguiram LIVE e o UTM apareceu no modal depois de recarregar. A de stories já tinha 2 envios e 1 clique antes da troca. Pegadinha: o `javascript_tool` bloqueia a leitura de valor com query string — conferir por zoom no modal.

## 13/09/2026 — `IG | 2026-09-13 | MACHADO | aposta dos lenhadores` (carrossel 118, fábula) — MONTADA STOPPED ~14h20, LIVE às 14h42 após o "postado"

Vigésima sexta no padrão novo. Caminho **imersão MBV**; `utm_campaign=2026-09-13-MACHADO`; palavra em três grafias (`MACHADO, machado, Machado`, sem acento na origem); DM "Força e garra você já tem. O que cansa é o machado cego. Quer ver como a imersão afia?" (86 chars) com botão `>> Quero afiar <<`. Modelo duplicado: a `IG | 2026-09-12 | AUTOMATICO | todas as vezes` (LIVE, 14 exec., 42,9%). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260913173623_712831. Kit em `conteudo/carrosseis/118_afiar-o-machado/manychat/kit-dm.md`.

- **O "postei" veio antes do post.** O user mandou "postei, cria o Manychat" e, no meio da montagem, "só mais uma correção visual antes de eu postar" (slide 11). Tratado como o caso RESPEITO: montada inteira com o post ainda apontando pro do modelo (115), salva e deixada STOPPED; amarrar ao 118 na grade + Ativar quando o "postei" de verdade chegar. Nada dispara parada.
- **Colisão checada:** a busca "machado" no painel não devolve nada.
- **Sem bug de comer caractere**: nome no modal Renomear por cmd+a + digitação; palavra, DM, botão e link por `form_input`. Link conferido em três passadas (Home / Right × 61 parou exatamente depois de "manychat" / End = `…2026-09-13-MACHADO`).
- Navegador: 2 Chromes na lista (`ee5937df` e `46b005d2`, os dois macOS locais); `AskUserQuestion` obrigatório, user escolheu o pedido de conexão em todos os Chromes e nomeou "Tatsuo Academy"; T laranja conferido no rodapé da barra lateral.
- Viewport 1503×812 na lista: `⋮` da linha em (1415, y da linha) no hover; Renomear a +50 px; Duplicar a +92 px; modal Renomear: campo (750, 176), botão Renomear (926, 265). A cópia nasce com sufixo " copy" no topo da lista. Dentro da automação STOPPED: `Editar` (1324, 38), `Ativar` (1399, 38); em edição: `Atualização` (1424, 38); ícone de corrente do botão (396, 635) após 10 ticks de scroll; modal do link: `Salvar` (940, 273).
- Ficha do 118 já com `data_publicacao=2026-09-13` (confirmar se o post sair no dia).
- **Ativação:** o "postado" chegou ~14:42; 'Mostrar Todos' trazia o 118 em PRIMEIRO ("Todo dono de empres…", há 2 minutos, capa dos lenhadores); selecionado, preview conferido (capa + legenda "Todo dono de empresa conhece o lenhador de 25 anos…", 1 curtida e 2 comentários), UTM sobreviveu à troca de post (End = `…2026-09-13-MACHADO`), Atualização e Ativar: **LIVE**, ~4 min depois da publicação. Após navegar de novo pra URL da automação, o Editar pegou de primeira com 10 s de espera.

## 13/09/2026 — `IG | 2026-09-13 | CLIMA | domingo a noite` (carrossel 117) — LIVE ~17:20, montada e ativada de uma vez após o "postei"

Vigésima sexta no padrão novo. Caminho **imersão MBV**; `utm_campaign=2026-09-13-CLIMA`; palavra em TRÊS grafias (sem acento na origem): `CLIMA, clima, Clima`; DM "Quer o time chegando na segunda com vontade? Os quatro pilares do clima estão no treinamento:" (94 chars) com botão `>> Quero ver <<`. Modelo duplicado: a `IG | 2026-09-12 | AUTOMATICO | todas as vezes` (LIVE, 16 exec., 37,5% CTR em um dia; link trocado inteiro por `form_input`). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260913201807_682856. Kit em `conteudo/carrosseis/117_domingo-a-noite/manychat/kit-dm.md`.

- **Colisão checada:** a busca "clima" devolve "Nenhuma automação encontrada". Sem global, sem específica.
- O "postei" chegou ~17h16 (domingo). A grade direta ainda não trazia o 117; o 'Mostrar Todos' trazia em PRIMEIRO ("Todo mundo já sentiu…", há 21 segundos), capa do funcionário na máquina de escrever olhando o relógio. Preview conferido (capa + legenda), 0 curtidas e 2 comentários no preview.
- **Sem bug de comer caractere**: nome no modal Renomear por cmd+a + digitação; palavra, DM, botão e link por `form_input`. Link conferido em três passadas (End = `…2026-09-13-CLIMA` / Home + Right × 61 parou exatamente depois de "manychat").
- Navegador: 2 Chromes na lista (`ee5937df` e `46b005d2`, ambos macOS); `AskUserQuestion` obrigatório, user escolheu o `ee5937df`; T laranja conferido.
- Viewport 1503 px o tempo todo: lista `⋮` (1415, 416) no hover, Renomear (1373, 466), Duplicar (1367, 508), modal Renomear (926, 265); STOPPED `Editar` (1324, 38); em edição `Atualização` (1424, 38); depois `Ativar` (1398, 38); 'Mostrar Todos' por `find`; primeiro card do modal (520, 245); botão do link em y≈635 após 10 ticks; modal `Salvar` (939, 272).
- Ficha do 117 com `data_publicacao=2026-09-13`.

## 14/09/2026 — `IG | 2026-09-14 | SOBERANO | ultimo da fila` (carrossel 120) — LIVE ~14h00, montada e ativada de uma vez após o "postei"

Vigésima sétima no padrão novo. Caminho **imersão MBV**; `utm_campaign=2026-09-14-SOBERANO`; palavra em TRÊS grafias (sem acento na origem): `SOBERANO, soberano, Soberano`; DM "Soberano recebe primeiro. Quer ver como desenhar a sua empresa pra parte do dono ser a primeira conta?" (103 chars) com botão `>> Quero ver <<` herdado. Modelo duplicado: a `IG | 2026-09-13 | CLIMA | domingo a noite` (LIVE, 4 exec., 25%; link trocado inteiro por `form_input`). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260914165539_029926. Kit em `conteudo/carrosseis/120_ultimo-da-fila/manychat/kit-dm.md`.

- **Colisão checada:** a busca "soberano" devolve "Nenhuma automação encontrada". Sem global, sem específica.
- **O post demorou uns minutos pra indexar.** No primeiro 'Mostrar Todos' o mais recente era um reel de 3 horas atrás; alternar o rádio global→específico não trouxe (só resetou a seleção pro primeiro card, um reel). Enquanto isso preenchi palavra, DM e link; no 'Mostrar Todos' seguinte (~3 min depois) o 120 já estava em PRIMEIRO ("Toda vez que eu perg…", há 1 minuto, capa serif vermelha do dono com o envelope). Preview conferido (capa + legenda "Toda vez que eu pergunto pra um dono de empresa pequena…", 0 curtidas e 2 comentários). Lição: dá pra montar tudo antes e amarrar o post por último; o reset do rádio não acelera a indexação.
- **Sem bug de comer caractere**: nome no modal Renomear por cmd+a + digitação; palavra, DM e link por `form_input`. Link conferido em três passadas antes de salvar (Home / Right × 61 parou exatamente depois de "manychat" / End = `…2026-09-14-SOBERANO`) e de novo no End depois de amarrar o post: UTM sobreviveu.
- Navegador: 3 Chromes na lista (`ee5937df` "Tatsuo Academy" macOS, `bce20a66` Windows de colega, `46b005d2` macOS); `AskUserQuestion` obrigatório, user escolheu o `ee5937df`; T laranja conferido no primeiro screenshot.
- Viewport 1164 px na lista: `⋮` (1087, 411) no hover da primeira linha, Renomear (1043, 457), Duplicar (1037, 492), modal Renomear: campo (580, 153), botão Renomear (733, 230); a cópia nasce STOPPED no topo. Dentro da automação (1164 → 1191 px depois do Editar): STOPPED `Editar` (1008, 32); em edição `Atualização` (1120, 33); depois `Ativar` (1099, 33); 'Mostrar Todos' (151, 300); primeiro card do modal (389, 217); X do modal da grade (888, 41); corrente do botão (352, 851) após 10 ticks; modal do link: campo (595, 187), `Salvar` (763, 243), X (789, 48).
- Ficha do 120 com `data_publicacao=2026-09-14`.

## 14/09/2026 — `IG | 2026-09-14 | ORGULHO | lenha primeiro` (carrossel 116) — LIVE ~18h30, "postei" do user com o post há ~7 min

Caminho **imersão MBV**; `utm_campaign=2026-09-14-ORGULHO`; palavra em TRÊS grafias (sem acento na origem): `ORGULHO, orgulho, Orgulho`; DM "Time que trabalha por orgulho não se compra. Quer ver como montar a rotina que forma esse time?" (96 chars) com botão `>> Quero ver <<`. Modelo duplicado: a `IG | 2026-09-10 | PEQUENO | outro bicho` (LIVE, do 107; data diferente, então o link foi trocado inteiro por `form_input` no modal). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260914212334_546683. Kit em `conteudo/carrosseis/116_lenha-primeiro/carousel-text.md`.

- **Colisão checada:** a busca "orgulho" devolve "Nenhuma automação encontrada". Nem global, nem específica.
- **Sem bug de comer caractere:** nome no modal Renomear por cmd+a + digitação (conferido por zoom); palavra e DM por `form_input`; botão e link por `form_input` dentro do modal "Adicionar um link" (o clique no texto do botão abre o modal com `Texto do botão` + `Link`; o ícone de corrente ao lado só mostra o tooltip com a URL, não abre o modal). Link conferido no tooltip depois de salvar: termina em `2026-09-14-ORGULHO`.
- **Post:** 'Mostrar Todos' trouxe o 116 em PRIMEIRO ("Seu funcionário entre…", há 7 minutos; thumbnail ainda não carregada, carrossel indexado em <10 min). Preview conferido (capa do escritório em festa "A ALMA COME OUTRA COISA" + legenda "Seu funcionário entrega o mínimo…"). Atualização ("As alterações foram salvas") e Ativar ("Sua automação está pronta e funcionando"): LIVE.
- Navegador: `switch_browser` (user clicou Conectar; retorno "Tatsuo Academy"); T laranja conferido no primeiro screenshot. Viewport 1191 px: lista `⋮` em x≈1085 no hover (Renomear +48, Duplicar +84); STOPPED `Editar` (1032, 33), `Ativar` (1098, 33); edição `Atualização` (1120, 33); 'Mostrar Todos' (150, 301); primeiro card da grade (388, 217); botão da DM (150, 852) abre o modal.
- Achado de passagem: existem no painel uma `RAIO - X` (LIVE, "alguma publicação ou Reel", 1 exec.) e uma `RAIO - X stories` (LIVE, 4 exec.), criadas há 2 dias por outra sessão ou pelo user; são do caminho RAIO-X novo. Não tocadas.
- Ficha do 116 com `data_publicacao=2026-09-14`.

## 15/09/2026 — `IG | 2026-09-15 | REMUNERADO | nao e caridade` (carrossel 121) — LIVE ~13h33, "estou postando agora" junto com o /etiqueta

Caminho **imersão MBV**; `utm_campaign=2026-09-15-REMUNERADO`; palavra em três grafias: `REMUNERADO, remunerado, Remunerado`; DM "15, 30 mil não é salário de dono. Quer ver como ser remunerado hoje com a empresa que você já tem?" (98 chars) com botão `>> Quero ver <<`. Modelo duplicado: a `IG | 2026-09-14 | ORGULHO | lenha primeiro` (link trocado inteiro por `form_input` no modal). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260915163308_139681. Kit em `conteudo/carrosseis/121_nao-e-caridade/manychat/kit-dm.md`.

- **Colisão checada:** "remunerado" devolve "Nenhuma automação encontrada".
- **Navegador:** `AskUserQuestion` obrigatório (3 Chromes na lista, um Windows de colega); user escolheu o `ee5937df` (mesmo id de 10/09); T laranja conferido no primeiro screenshot. Pegadinha nova: o primeiro `navigate` numa aba `chrome://newtab` não troca a URL na hora e o screenshot falha com "Cannot access a chrome:// URL"; o `tabs_context_mcp` seguinte já mostra a aba no Manychat. Não criar aba extra (fechar a extra bagunçou o grupo; um `tabs_context_mcp` com `createIfEmpty` resolveu).
- **Post:** já indexado quando entrei em Editar (2 comentários no preview): a capa do 121 ("EMPRESA NÃO É INSTITUIÇÃO DE CARIDADE", dono de mercearia com a mão em "não") era a SEGUNDA miniatura da grade direta, sem precisar de 'Mostrar Todos'. Selecionado, preview conferido (aba Publicar: capa + legenda "Caridade é o que se faz com o que sobra"), Atualização ("As alterações foram salvas"), Ativar ("Sua automação está pronta e funcionando"): LIVE.
- Viewport 1191 px: lista `⋮` (1113, 421) no hover da primeira linha; Renomear (1068, 468), Duplicar (1062, 505); STOPPED `Editar` (1032, 33), `Ativar` (1098, 33); edição `Atualização` (1120, 33); segunda miniatura da grade (198, 232); botão da DM (200, 851) abre o modal; aba Publicar do preview (730, 822).
- Ficha do 121 com `data_publicacao=2026-09-15`, previsão `mediana` 10-36.


## 15/09/2026 — `IG | 2026-09-15 | LENHA | lenha no funcionario` (carrossel 122) — MONTADA STOPPED ~17h55, LIVE ~18h20 após o "postei"

Caminho **imersão MBV**; `utm_campaign=2026-09-15-LENHA`; palavra em três grafias (sem acento na origem): `LENHA, lenha, Lenha`; DM "Lenha primeiro, calor depois. Quer ver como montar a rotina que acende o seu time todo dia?" (92 chars) com botão `>> Quero ver <<`. Modelo duplicado: a `IG | 2026-09-15 | REMUNERADO | nao e caridade` (LIVE, do 121; mesma data, link trocado inteiro por `form_input` no modal). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260915205347_072231. Kit em `conteudo/carrosseis/122_lenha-no-funcionario/carousel-text.md`.

- **Pegadinha de nome:** o user pediu "o carrossel LENHA". LENHA é a palavra do **122** (lenha no funcionário); o **116** (lenha primeiro) já estava LIVE desde 14/09 com a palavra ORGULHO. Conferir sempre pela palavra do CTA no `registro-posts.csv`, não pelo apelido da pasta.
- **Colisão checada:** a busca "lenha" traz só a ORGULHO (lenha primeiro) e a MACHADO (aposta dos lenhadores), as duas por post específico e com outras palavras. Nada global.
- **Navegador:** a ferramenta já veio com o `ee5937df` em uso (mesmo id de 10, 11 e 15/09) e dispensou o `AskUserQuestion`; T laranja conferido no primeiro screenshot. Pegadinha: o `<` de voltar no topo da automação navegou a aba pra `chrome://newtab` (histórico da aba), não pra lista; ir pela URL `https://app.manychat.com/fb2015128/cms`.
- **Sem bug de comer caractere:** nome por cmd+a + digitação (conferido por zoom); palavra, DM e link por `form_input`. Link conferido em três passadas (End termina em `2026-09-15-LENHA`; Home + Right×61 parou depois de `manychat`).
- Viewport 1164 px: lista `⋮` (1087, 411) no hover da primeira linha; Renomear (1044, 457), Duplicar (1039, 493); modal Renomear: campo (580, 153), botão (733, 230); STOPPED `Editar` (1008, 32), `Ativar` (1073, 32); edição `Atualização` (1095, 32); 'Mostrar Todos' (147, 294); X do modal da grade (888, 41); botão da DM (200, 883) após scroll de 10 ticks; modal do link `Salvar` (746, 237).
- **Espera:** o "vou postar agora" veio ~17h50, mas o post só entrou ~18h14. Grade checada 8 vezes em ~25 min (reload + Editar + 'Mostrar Todos'), sempre com o reel de 2 h atrás em primeiro. O `browser_batch` estoura o tempo com mais de ~80 s de `wait` somados; ciclos de 60-70 s passam. Lição repetida do 87: o relógio não substitui o aviso; quando a grade não traz o post, é porque ele não foi publicado, e não vale ficar preso. Responder o status ao user e esperar o "postei".
- **Ativação:** "postei" ~18h18; reload + Editar (a primeira tentativa de Editar depois do `navigate` não pega; esperar 15 s) + 'Mostrar Todos' trouxe o 122 em PRIMEIRO ("Lenha no seu funcion…", há 4 minutos, capa da acha "LENHA NO SEU FUNCIONÁRIO"). Selecionado, preview conferido (capa + legenda "Lenha no seu funcionário. Eu sei como isso soa…", 4 curtidas e 2 comentários), UTM sobreviveu à troca de post (End = `…2026-09-15-LENHA`), Atualização ("As alterações foram salvas") e Ativar: **LIVE ~18h20**, ~6 min depois da publicação. Viewport virou 1191 px depois do reload: `Editar` (1008, 32) ainda pegou; `Atualização` (1121, 33); `Ativar` (1098, 33); primeiro card da grade (389, 218); botão da DM (205, 851) após 10 ticks; modal do link: campo (595, 187), X (789, 48).
- Ficha do 122 com `data_publicacao=2026-09-15`, previsão rebaixada de `acima` pra `mediana` 12-36 na publicação (intervalo de 1 dia com o 116, mesma semente-mãe; a própria ficha pedia >= 1 semana).


## 16/09/2026 — `IG | 2026-09-16 | RAIZ | cansei de demitir vendedor` (carrossel 119) — LIVE ~14h30, "postei carrossel VENDEDOR" do user ~14h20

Caminho **imersão MBV**; `utm_campaign=2026-09-16-RAIZ`; palavra em três grafias (sem acento na origem): `RAIZ, raiz, Raiz`; DM "Cansou de trocar vendedor? Quer ver como eu monto a vaga e o rito diário que faz gente normal entregar?" (103 chars) com botão `>> Quero ver <<`. Modelo duplicado: a `IG | 2026-09-15 | LENHA | lenha no funcionario` (LIVE, do 122; link trocado inteiro por `form_input` no modal). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260916172251_389741. Kit em `conteudo/carrosseis/119_problema-de-lugar/carousel-text.md`.

- **Pegadinha de nome (de novo):** o user pediu "carrossel VENDEDOR". Não existe pasta com esse nome: é o **119_problema-de-lugar** (capa "CANSEI DE DEMITIR VENDEDOR", palavra RAIZ, entrega em `~/Desktop/carrosseis claude/vendedor/`). Achado pela pasta do Desktop + grep de "VENDEDOR" nos `carousel-text.md`. Conferir sempre capa/palavra no `registro-posts.csv`, não o apelido.
- **Colisão checada:** "raiz" devolve "Nenhuma automação encontrada".
- **Navegador:** a lista veio com 6 Chromes (4 macOS, 2 Windows de colegas); o `ee5937df` já estava `inUse` (mesmo id de 10, 11 e 15/09), sem `AskUserQuestion`; T laranja conferido no primeiro screenshot. A aba `chrome://newtab` do grupo aceitou o `navigate` direto pra `https://app.manychat.com/fb2015128/cms`; a lista levou ~12 s pra renderizar (primeiro screenshot em branco).
- **Sem bug de comer caractere:** nome por cmd+a + digitação (conferido por zoom); palavra, DM e link por `form_input`. Link conferido nas duas pontas (End = `…2026-09-16-RAIZ`; Home = `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=ma…`) e de novo no tooltip da corrente depois de salvar o modal.
- **Post:** já indexado ao entrar em Editar (~10 min depois do "postei"): a capa do 119 (dono com as mãos no rosto, "CANSEI DE DEMITIR VENDEDOR") era a PRIMEIRA miniatura da grade direta, sem 'Mostrar Todos'. Selecionado, preview conferido (aba Publicar: capa + comentário-teste "RAIZ"), Atualização e Ativar ("Sua automação está pronta e funcionando"): **LIVE ~14h30**, ~10 min depois da publicação.
- Viewport 1512 px (maior que os 1164/1191 anteriores; coordenadas mudam): lista `⋮` (1411, 536) no hover da primeira linha; Renomear (1356, 593), Duplicar (1349, 640); modal Renomear: campo (755, 199), botão (953, 299); STOPPED `Editar` (1309, 42), `Ativar` (1393, 42); edição `Atualização` (1421, 42); primeira miniatura da grade (162, 295); botão da DM (200, 607) após 10 ticks abre o modal do link: campo Link (755, 237), `Salvar` (968, 309).
- Ficha do 119 com `data_publicacao=2026-09-16`, previsão rebaixada de `acima` 40-160 pra `mediana` 15-36 na publicação (terceira peça de Cultura/gente em 48 h; 122 do bloco de acompanhamento 1 dia antes em 8 comentários; lote 13-15/09 entre 8 e 18).


## 17/09/2026 — `IG | 2026-09-17 | COMBINADO | convencer um adulto` (carrossel 125) — LIVE ~12h45, "postei carrossel COMBINADO" do user ~12h37

Caminho **imersão MBV**; `utm_campaign=2026-09-17-COMBINADO`; palavra em três grafias (sem acento na origem): `COMBINADO, combinado, Combinado`; DM "Cobrança só vira pessoal sem combinado. Quer ver como montar o combinado e o rito que cobra sem briga?" (101 chars) com botão `>> Quero ver <<`. Modelo duplicado: a `IG | 2026-09-16 | PONTE | ninguem acorda cedo pelo sonho do outro` (LIVE, do 123, 99 exec. / 49,5% CTR em 18 h; a mais recente da lista; link trocado inteiro por `form_input` no modal). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260917154021_072527. Kit em `conteudo/carrosseis/125_nada-pessoal/carousel-text.md`.

- **Colisão checada:** "combinado" traz só a `ROTINA` (LIVE, post específico, palavra rotina; bate pelo texto). Nada global.
- **Navegador:** o `ee5937df` de sempre não estava na lista (2 Chromes: "Pedro mg3" macOS + 1 Windows de colega); `AskUserQuestion` obrigatório, user escolheu a tela de confirmação → `switch_browser` devolveu "Tatsuo Academy"; T laranja conferido no primeiro screenshot. A lista do CMS levou ~18 s pra renderizar depois do `navigate`.
- **Sem bug de comer caractere:** nome por cmd+a + digitação (conferido por zoom, Home e End); palavra, DM e link por `form_input`. Link conferido em três passadas (Home = `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=ma…`; Home + Right×61 parou logo depois de `manychat`; End = `…2026-09-17-COMBINADO`).
- **Post:** já indexado ao entrar em Editar (~8 min depois do "postei"): a capa do 125 ("CONVENCER UM ADULTO A FAZER O TRABALHO DELE", dono de prancheta × funcionário de braços cruzados) era a SEGUNDA miniatura da grade direta, sem 'Mostrar Todos'. Selecionado, preview conferido (capa + legenda "Tem uma parte do trabalho de dono que ninguém avisa…", 2 curtidas e 2 comentários), Atualização ("As alterações foram salvas") e Ativar: **LIVE ~12h45**, ~8 min depois da publicação.
- Viewport 1282×628 (janela menor que as sessões anteriores; coordenadas mudam): busca (520, 208) na tela 1512 antes do redimensionamento; lista `⋮` (1198, 455) no hover da primeira linha; Renomear (1150, 301), Duplicar (1144, 341); modal Renomear: campo (640, 169), botão (808, 254); STOPPED `Editar` (1110, 36), `Ativar` (1181, 36); edição `Atualização` (1206, 36); segunda miniatura da grade (213, 250); botão da DM (168, 459) após 10 ticks abre o modal do link: campo Link (640, 201), `Salvar` (820, 262). LIVE: `Editar` (1071, 36), `Interromper` (1162, 36).
- **Achados de passagem, não tocados:** (1) a `IG | 2026-09-16 | RAIZ | cansei de demitir vendedor` (119) está LIVE há 22 h com **0 execuções e "indisponível"** — ou o post não recebeu comentário RAIZ, ou o vínculo com o post quebrou; conferir no ritual. (2) A `PONTE` (123) foi criada por outra sessão em 16/09 e a ficha do 123 no `registro-posts.csv` ainda está sem `data_publicacao`.
- Ficha do 125 com `data_publicacao=2026-09-17`, previsão `mediana` 14-36.

## 17/09 — `MOP stories` (segunda automação de story)

Pedido do user: story com palavra MOP pro link `mop.altaescala.com.br`. Sem colisão ("mop" não devolve nada na busca). Montada pelo modelo "Gere leads com stories", LIVE às ~14h25: qualquer story; palavra `MOP, mop, Mop`; DM "Aqui está o link do MOP que você pediu. Toca no botão pra acessar." (texto do Claude, o user não deu DM); botão `>> Acessar <<`; link `https://mop.altaescala.com.br/?utm_source=manychat&utm_medium=dm&utm_campaign=mop-stories`. URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260917172321_258976. Renomeada na lista de "Turn story replies into leads" pra `MOP stories`. Tudo por `form_input`, sem bug de caractere.

## 18/09/2026 — `IG | 2026-09-18 | RAIO-X | para de trabalhar` (carrossel 127) — LIVE ~15h17, "postei o carrossel VOLANTE" do user ~15h11

Caminho **RAIO-X** (primeira automação POR POST ESPECÍFICO desse caminho; regra de 14/09). `utm_campaign=2026-09-18-RAIO-X`; link `https://tatsuoacademy.com/raio-x-empresa-lucrativa/?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-18-RAIO-X` (mesma página da global `RAIO - X`, UTM no padrão data+palavra); palavra nas **7 grafias copiadas da global**: `RAIO-X, raio-x, Raio-X, Raio-x, raio-X, RAIOX, raiox`; DM "Ninguém assume o volante sem conhecer o carro. Quer a aula em que você faz o raio-x da sua empresa?" (99 chars) com botão `>> Quero a aula <<` (18). Modelo duplicado: a `IG | 2026-09-17 | FOGUETE | foguete pra lua` (LIVE, do 126, 0 exec. em 21 h; a mais recente da lista; link trocado inteiro por `form_input` no modal). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260918181315_612383. Kit em `conteudo/carrosseis/127_para-de-trabalhar/carousel-text.md`.

- **Colisão checada e ACEITA (decisão registrada, não do user):** a busca "raio" traz só a `RAIO - X` (global, LIVE, "alguma publicação ou Reel", 1 exec. / 100% em 6 dias, utm `raio-x-feed`) e a `RAIO - X stories` (16 exec. / 68,8%). A global foi criada pelo user em 12/09 pro próprio caminho e aponta pra MESMA página, então a colisão não manda link errado: o pior caso é o lead cair no balde `raio-x-feed` em vez de `2026-09-18-RAIO-X` (atribuição mais fraca) ou o comentário receber duas DMs. Regra do Manychat que estou assumindo: gatilho de post específico tem prioridade sobre o de qualquer publicação. **Não pausei a global** (é do user e serve os outros posts). **Verificar no ritual de segunda (21/09):** execuções da específica × da global no período e em qual `utm_campaign` os leads do 127 caíram. Se a global passou na frente, a regra pra próximos RAIO-X vira "pausar a global enquanto houver específica viva" (como no caso MBV de 29/08).
- **Navegador:** 4 Chromes na lista (2 macOS, 2 Windows de colegas); o `ee5937df` já estava `inUse`/`onThisComputer` (mesmo id de 10, 11, 15 e 16/09), sem `AskUserQuestion`; T laranja conferido no primeiro screenshot. A lista do CMS levou ~28 s pra renderizar (primeiro screenshot em branco aos 18 s).
- **Sem bug de comer caractere:** nome por cmd+a + digitação (conferido por zoom, Home e End); palavra, DM, botão e link por `form_input`. Link conferido em três passadas (Home = `https://tatsuoacademy.com/raio-x-empresa-lucrativa/?utm_s…`; Home + Right×70 parou em `manycha|t`, que é a posição 70 contada fora do navegador; End = `…utm_campaign=2026-09-18-RAIO-X`).
- **Post:** indexado ao abrir 'Mostrar Todos' (~4 min depois do "postei"): "Vou te falar uma ver… há 1 minuto" era o PRIMEIRO card (miniatura ainda cinza); na grade direta a capa não tinha aparecido. Ao lado, um Reel "Vendedor não pode f… há 7 minutos" — outra frente publicando no mesmo horário (a lição de 31/08 continua valendo). Selecionado, preview conferido (capa "VOCÊ TRABALHA DEMAIS E COMANDA DE MENOS" + legenda "Vou te falar uma verdade meio chata…", 2 comentários), Atualização (o `browser_batch` estourou o tempo no spinner de ~30 s, mas o salvamento passou: miniatura do 127 e palavra RAIO-X no painel STOPPED) e Ativar: **LIVE ~15h17**, ~6 min depois da publicação.
- Viewport 1512×807 (mesmas coordenadas de 16/09): lista `⋮` (1414, 486) no hover da primeira linha; Renomear (1356, 544), Duplicar (1350, 592); modal Renomear: campo (755, 199), botão (953, 299); STOPPED `Editar` (1309, 42), `Ativar` (1375, 42) depois de salvar; edição `Atualização` (1405, 42); 'Mostrar Todos' (191, 382); primeiro card do modal (491, 300); campo do botão da DM (270, 607) abre o modal do link: `Salvar` (968, 309). LIVE: `Editar` (1244, 42), `Interromper` (1352, 42).
- Ficha do 127 com `data_publicacao=2026-09-18`, previsão mantida `acima` 120-600 (o risco declarado de a mecânica do raio-x não existir na publicação caiu: página no ar desde 12/09).

## 19/09/2026 — `IG | 2026-09-19 | CHATO | ser dono e ser chato repost` (carrossel 132) — LIVE ~17h40, "postei, monte o manychat agora" do user às 17h28

Caminho **imersão MBV**; `utm_campaign=2026-09-19-CHATO`; palavra em três grafias: `CHATO, chato, Chato`; DM "Ser dono é ser chato. Quer ver como montar o rito de cobrar, acompanhar e treinar todo dia?" (91 chars) com botão `>> Quero ver <<`. Modelo duplicado: a `IG | 2026-09-17 | COMBINADO | convencer um adulto` (LIVE, 44 exec. / 34,1% em 2 dias; link trocado inteiro por `form_input` no modal). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260919203117_043869. Kit em `conteudo/carrosseis/132_ser-dono-e-ser-chato-repost/manychat/kit-dm.md`.

- **Colisão checada:** "chato" vazio; "comando" devolve a global `Comando!! MBV` (LIVE, qualquer publicação, 4.894 exec.) e a `comando repost` (LIVE, específica). O repost trocou o CTA original "COMANDO" por CHATO exatamente pra não disparar a global.
- **Navegador:** o `ee5937df` ("Tatsuo Academy") já estava `inUse`; T laranja conferido por zoom no rodapé da barra. Viewport começou em 1503×812 e virou 1440×722 no meio da operação: `⋮` da primeira linha em (1416, 414) e depois em (1356, 396); Renomear +48 px, Duplicar +90 px abaixo do `⋮`.
- **Rename e índice de busca:** a busca "chato" logo depois do Renomear devolveu vazio; a lista sem filtro (ordenada por modificado) já mostrava o nome novo no topo. Não confiar na busca por nome nos primeiros minutos.
- **Post:** já indexado ao entrar em Editar (~15 min após a publicação), SEGUNDA miniatura da grade direta (capa da sapataria); preview conferido com a legenda nova ("Ser dono é ser chato, e ninguém abre empresa sonhando com isso…").
- **Pegadinha de clique:** o painel esquerdo rola sozinho depois de cada `form_input`; clicar por coordenada em ">> Quero ver <<" acertou o textarea da DM duas vezes e o "Adicionar Um Link" uma (abriu modal VAZIO, cancelado sem salvar; teria criado um segundo botão). Regra: screenshot imediatamente antes de clicar no botão do link, ou abrir o modal e conferir que o campo já vem preenchido com o link herdado antes de digitar.
- **Sem bug de comer caractere:** nome por cmd+a + digitação (zoom nas duas pontas); palavra, DM e link por `form_input`; link conferido End/Home e no tooltip da corrente.
- Ficha do 132 com `data_publicacao=2026-09-19`, previsão `mediana` 15-36 mantida.

## 21/09/2026 — `IG | 2026-09-21 | PATO | voce ja viu um pato repost` (carrossel 135) — MONTADA STOPPED ~16h55, LIVE ~17:07 após o "postei, pode ativar"

Caminho **RAIO-X** (segunda específica do caminho); `utm_campaign=2026-09-21-PATO`; link `https://tatsuoacademy.com/raio-x-empresa-lucrativa/?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-21-PATO`; palavra em três grafias: `PATO, pato, Pato`; DM "Você não precisa ser o melhor em nada. Precisa entender a sua empresa. Quer a aula do raio-x?" (93 chars) com botão `>> Quero a aula <<` (herdado). Modelo duplicado: a `IG | 2026-09-18 | RAIO-X | para de trabalhar` (LIVE, 10 exec. / 50% em 3 dias; mesmo link, só o UTM trocado). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260921195023_106765. Kit em `conteudo/carrosseis/135_pato-repost/carousel-text.md`.

- **Pedido do user:** "monte o manychat" antes de publicar (sem horário). Montada e salva STOPPED apontando pro post do modelo (127); a grade 'Mostrar Todos' às ~16h53 tinha em primeiro um reel de clínica de 2 h atrás e a frase da calçada de 7 h: o pato não estava no ar.
- **Ativação:** "postei, pode ativar" ~17:07; o primeiro `Editar` depois do `navigate` não pegou (lição do 122: repetir após ~8 s); 'Mostrar Todos' trouxe o pato em PRIMEIRO ("Você já viu um pato? …", há 1 minuto, capa do pato de perfil). Selecionado, preview conferido (capa + legenda nova "Você já viu um pato? Ele voa, anda e nada…", 1 curtida e 2 comentários), UTM sobreviveu à troca de post (tooltip da corrente = `…utm_campaign=2026-09-21-PATO`), Atualização e Ativar: **LIVE ~17:07**, poucos minutos depois da publicação.
- **Colisão checada:** busca "pato" vazia. A global `RAIO - X` segue LIVE (mesma página; pior caso é o lead cair em `raio-x-feed`), como no 127; conferir no ritual em qual UTM os leads do 127 caíram antes de decidir pausar.
- **Navegador:** o `ee5937df` já estava `inUse`/`onThisComputer` (mesmo id de 10 a 19/09); T laranja visível no rodapé da barra lateral do Manychat (28, 990) no viewport 1148×1061. Lista do CMS renderizou em ~28 s.
- **Sem bug de comer caractere:** nome por cmd+a + digitação (zoom); palavra, DM e link por `form_input`; link conferido em três passadas (End = `…2026-09-21-PATO`; Home; Home + Right×70 = `manycha|t`).
- Viewport 1148×1061: `⋮` da linha em (1073, y da linha) no hover; Renomear +44 px e Duplicar +80 px abaixo do `⋮`; modal Renomear: campo (573, 151), botão (723, 227); STOPPED `Editar` (994, 32), `Ativar` (1058, 32); edição `Atualização` (1079, 32); 'Mostrar Todos' (145, 290); X do modal da grade (876, 41); botão da DM (200, 909) após 10 ticks; modal do link: campo (573, 179), `Salvar` (734, 234).

## 21/09 — `MBV stories` (terceira automação de story)

Pedido do user: palavra MBV nos stories com o link da imersão. Modelo "Gere leads com stories", LIVE às ~19h00: qualquer story; palavra `MBV, mbv, Mbv, MVB, mvb` (mesmas grafias da global MBV de comentário, que segue LIVE e não conflita — gatilho diferente); DM "O MBV é o método que faz a empresa te pagar pelo risco. Quer ver como funciona a imersão?" (89 chars, texto do Claude); botão `>> Quero ver <<`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=mbv-stories`. URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260921215821_135998. Renomeada na lista. Tudo por `form_input`. Pegadinha nova: `wait` do browser_batch tem teto de 10 s.

## 21/09/2026 — `IG | 2026-09-21 | DECISAO | esse alguem e voce` (carrossel 137) — MONTADA STOPPED ~19h10, publicação marcada 19h30

Caminho **imersão MBV**; `utm_campaign=2026-09-21-DECISAO`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-21-DECISAO`; palavra em SEIS grafias (acento na origem): `DECISÃO, DECISAO, decisão, decisao, Decisão, Decisao`; DM "Decisão de dono cabe numa reunião de manhã, com número na mesa. Quer ver como eu ensino a montar isso?" (102 chars) com botão `>> Quero ver <<` (herdado). Modelo duplicado: a `IG | 2026-09-17 | FOGUETE | foguete pra lua` (LIVE, 2 exec. / 50%; mesmo link, UTM trocado inteiro: End + Backspace × 18 + `2026-09-21-DECISAO`). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260921220747_765690. Kit em `conteudo/carrosseis/137_esse-alguem-e-voce/carousel-text.md`.

- **Pedido do user:** "postarei 19:30h, cria o Manychat" (19h06). Montada em ~4 min e salva STOPPED apontando pro post do modelo (126). Timer de shell armado pras 19h33 + `caffeinate` de 90 min; o "postei" do user continua sendo o gatilho.
- **Colisão checada:** busca "decis" vazia. A busca do CMS casa palavras-chave, não o nome: "DECISAO" não achou a cópia recém-renomeada (ainda com as palavras do foguete); "foguete" achou.
- **Navegador:** `ee5937df` já `inUse`/`onThisComputer`; T laranja no rodapé (28, 990), viewport 1148×1061. Coordenadas iguais às da PATO (⋮ da linha em 1072; Renomear +44, Duplicar +80; modal Renomear campo (573, 151) e botão (723, 227); `Editar` (994, 32); `Atualização` (1079, 32); botão da DM (200, 909) após `scroll_to`; modal do link campo (574, 180), `Salvar` (734, 234)).
- **Sem bug de comer caractere:** nome por cmd+a + digitação (zoom); palavra e DM por `form_input`; link por End + backspaces + digitação, conferido em três passadas (End = `…2026-09-21-DECISAO`; Home; Home + Right×70 = `utm_medi|um`).
- **Nota de previsão:** a ficha pedia publicação a partir de 30/09 (tese-irmã do 128, 16/09); o user decidiu publicar 21/09, cinco dias depois. Fica registrado pra leitura do D+7.
- **Ativação (21/09):** o próprio user amarrou ao post e ativou ("eu mesmo ajustei, pode descansar", ~19h30). Timer das 19h33 cancelado. Conferir no ritual se a automação está LIVE no post certo e em qual UTM os leads caem.

## 22/09/2026 — `IG | 2026-09-22 | MODELO | pessimo negocio` (carrossel 140) — LIVE ~15h06, montada e ativada de uma vez após o "postei agora"

Caminho **imersão MBV**; `utm_campaign=2026-09-22-MODELO`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-22-MODELO`; palavra `MODELO, modelo, Modelo` (sem acento na origem, três grafias); DM "Modelo que só gira com dinheiro do banco não é seu. Quer ver como eu ensino a redesenhar o seu?" (96 chars) com botão `>> Quero ver <<` (herdado). Modelo duplicado: a `IG | 2026-09-21 | DECISAO | esse alguem e voce` (LIVE, 8 exec. / 50%; mesmo link, UTM trocado inteiro: End + Backspace × 18 + `2026-09-22-MODELO`). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260922180258_190300. Kit em `conteudo/carrosseis/140_pessimo-negocio/carousel-text.md`.

- **Colisão checada:** busca "modelo" traz a global legada `Modelo` (STOPPED, 41 exec., palavras modelo/MODELO, "alguma publicação", há 2 meses) e a `IG | 2026-07-31 | TARTARUGA` (específica, Reel). A global está parada, não dispara. Se alguém a religar, colide com esta.
- **Navegador:** `ee5937df` "Tatsuo Academy" já `inUse`/`onThisComputer`; T laranja no rodapé (28, 962); viewport **1176×1036** (era 1148: coordenadas deslocadas de novo). ⋮ da linha em (1099, 416); Renomear (1050, 463); Duplicar (1050, 498); modal Renomear campo (588, 155) e botão (741, 233); `Editar` (1018, 33); `Atualização` (1107, 33); `Ativar` (1085, 33); modal do link campo (588, 184), `Salvar` (753, 240).
- **Post:** o carrossel 140 já estava em SEGUNDO na grade do easy-builder (o primeiro é o post do modelo); selecionado por clique na miniatura, preview conferido (capa "Selic a 14% não quebrou…" + legenda "Empresa não é o que você vende").
- **Duas pegadinhas novas:** (1) o `form_input` na DM rola a página, e um clique por coordenada logo depois cai em outro lugar: acertou o toggle "interagir com os comentários" e o DESLIGOU; religado antes de salvar (as três respostas ao comentário sobreviveram). Regra: depois de `form_input`, rolar pro topo e tirar screenshot antes de clicar por coordenada. (2) `find` por "botão da DM com ícone de link" devolveu o "Adicionar Um Link" (botão NOVO), não o link do botão existente; cancelado sem salvar. O link do botão existente se edita clicando no próprio texto ">> Quero ver <<".
- **Sem bug de comer caractere:** nome por cmd+a + digitação (zoom); palavra e DM por `form_input`; link por End + backspaces + digitação, conferido em três passadas (End = `…2026-09-22-MODELO`; Home; Home + Right×70 = `utm_medi|um`).
- Etiqueta: mediana, 12-40 comentários em D+7 (`registro-posts.csv`, data_publicacao 2026-09-22).

## 22/09/2026 — `IG | 2026-09-22 | DRE | crise pra culpar` (carrossel 141) — MONTADA STOPPED ~18h17, LIVE às 18h55 após o "postei, pode ativar"

Caminho **imersão MBV** (o user cogitou RAIO-X e voltou atrás na mesma conversa); `utm_campaign=2026-09-22-DRE`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-22-DRE`; palavra `DRE, dre, Dre` (sigla, três grafias); DM "Crise todo mundo passa. Dono no comando é raro. Quer ver como eu ensino a assumir o seu?" (88 chars) com botão `>> Quero ver <<` (herdado). Modelo duplicado: a `IG | 2026-09-22 | MODELO | pessimo negocio` (LIVE, 0 exec.; mesma data, então só o rabo do UTM mudou: End + Backspace × 6 + `DRE`). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260922211347_513706. Kit em `conteudo/carrosseis/141_crise-pra-culpar/carousel-text.md`.

- **COLISÃO REAL (novo caso):** a busca "dre" traz a **global legada `DRE` LIVE** (Quick Automation PT, "alguma publicação", palavras DRE/dre/Dre, 119 exec. / 53 cliques / 45% CTR, criada 19/04/2026, DM "Para acessar o link do treinamento." + botão `>> Clique Aqui <<`, link não conferido). Diferente de MODELO e RISCO, aqui a global está **no ar**. Decisão: seguir com a específica, que tem prioridade sobre a global no mesmo post (mesmo regime do RAIO-X, 18/09), e **avisar o user**: se a prioridade falhar, o comentário DRE no 141 cai na global, sem UTM datado, e o lead perde atribuição no CRM. Conferir no ritual em qual UTM os leads do 141 caem. Cabe ao user decidir se para a global.
- **Navegador:** `ee5937df` já `inUse`/`onThisComputer`; T laranja no rodapé (28, 990); viewport 1148×1061 (coordenadas da DECISAO valeram: ⋮ da linha em (1072, 406); Renomear (1030, 450); Duplicar (1025, 487); modal Renomear campo (573, 151) e botão (723, 227); `Editar` (994, 32); `Atualização` (1079, 32); botão da DM (200, 909) após `scroll_to`; modal do link campo (574, 180), `Salvar` (734, 234)).
- **Sem bug de comer caractere:** nome por cmd+a + digitação (zoom); palavra e DM por `form_input` (preview do celular conferido); link por End + backspaces + digitação, conferido em três passadas (End = `…2026-09-22-DRE`; Home; Home + Right×70 = `utm_medi|um`). Toggle "interagir com os comentários" conferido ON depois do `form_input` (pegadinha do 140).
- **Post:** salva STOPPED apontando pro post do modelo (140). User avisou "programei para 18:55" durante a montagem. `caffeinate -dimsu -t 5400` ligado e timer de shell armado pras 18h55; o "postei" do user continua sendo o gatilho mais rápido.
- Etiqueta: acima, 40-200 comentários em D+7 (`registro-posts.csv`, data_publicacao 2026-09-22).
- **Ativação (18h55):** "postei, pode ativar" chegou ~18h52 e o carrossel já estava em PRIMEIRO no 'Mostrar Todos' ("A crise é a desculpa…", há 3 minutos); selecionado, preview conferido (capa do farmacêutico + legenda do 141), UTM sobreviveu à troca de post (End = `…2026-09-22-DRE`), Atualização e Ativar: **LIVE às 18h55**, ~3 min depois da publicação. Timer das 18h55 dispensado. Pegadinha de viewport: a janela mudou de 1148 pra 1176 px no meio da ativação (Atualização foi pra (1107, 33), Ativar pra (1085, 33), botão da DM pra (150, 932)); `ref_102` da DM morreu depois da troca de post, o botão do link se acha por `find` (ref do texto ">> Quero ver <<", não o "Adicionar Um Link"). Tela da grade: o slot do post ficou vazio uns segundos depois de salvar e voltou com a capa certa depois do Ativar.
- **Global `DRE` legada PARADA (18h58, a pedido do user):** "pode parar a global DRE". Interromper na própria automação (URL content20260419123340_597110); fechou STOPPED com 119 envios / 53 cliques / 45% CTR de histórico. Motivo: única global viva que colidia com uma específica do dia; agora todo comentário DRE no 141 cai só na `IG | 2026-09-22 | DRE` com UTM datado. Se alguém quiser a palavra DRE de volta em outro post, criar específica, nunca religar esta.

## 23/09/2026 — `IG | 2026-09-23 | BASICO | quatro pilares repost` (carrossel 143) — LIVE ~13h55, montada e amarrada logo após a publicação

Caminho **imersão MBV**; `utm_campaign=2026-09-23-BASICO`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-23-BASICO`; palavra em seis grafias herdadas: `BASICO, basico, Basico, BÁSICO, básico, Básico`; DM "Todo o resto é distração vendida como solução. Quer ver como eu ensino os 4 pilares na ordem certa?" com botão `>> Quero ver <<` (herdado). Modelo duplicado: a `IG | 2026-09-06 | BASICO | repost empresario bobo` (carrossel 92, LIVE, 117 exec. / 56,4%), que continua viva e amarrada ao 92: mesma palavra em posts específicos diferentes, sem colisão. Busca "basico" não trouxe global. URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260923165202_087730. Kit em `conteudo/carrosseis/143_basico-repost/carousel-text.md`.

- Repost do carrossel de 03/01/2026 (253 coment.), já repostado em 15/04/2026 (216 coment.): terceira ida ao ar, >5 meses da última.
- Post já em PRIMEIRO no 'Mostrar Todos' ("A prateleira de soluç…", há 21 s); preview conferido (capa do menino + legenda nova). Link trocado inteiro por `form_input`, conferido End/Home. Toggle de comentários ON conferido. Viewport 1176×1035 (coordenadas da MODELO valeram).

## 23/09/2026 — `IG | 2026-09-23 | 307 | ler o negocio repost` (carrossel 144, repost do "claude 4" de 02/07) — MONTADA STOPPED, LIVE 19h29 após o "postei, pode ativar"

Caminho **imersão MBV**; `utm_campaign=2026-09-23-307`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-23-307`; palavra `307` (impressa no último slide); DM "Empresa fala por número, e quem não lê decide no escuro. Quer ver como eu ensino a ler a sua?" com botão `>> Quero ver <<` (herdado). Modelo duplicado: a `IG | 2026-09-23 | BASICO | quatro pilares repost` (mesma data; link trocado inteiro por `form_input`, conferido End/Home). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260923222514_139741. Toggle de comentários ON conferido.

- **COLISÃO:** a global legada `307` segue LIVE (qualquer publicação, 7.534 exec. / 53,1%). Assumida a prioridade da específica, como no DRE; se os leads do 144 caírem sem o UTM `2026-09-23-307`, a específica perdeu e a global precisa parar durante o repost. Decisão de parar é do user.
- **Ativação (19h29):** post em PRIMEIRO no 'Mostrar Todos' ("Pergunta pra qualque…", há 1 min; permalink /p/DdpYYdikd3l); preview conferido (capa do dólar + legenda nova), Atualização e Ativar: LIVE. Pegadinha: clicar no rodapé do card do post abre 'Ver no Instagram' em aba nova em vez de selecionar; selecionar clicando na miniatura.

## 24/09/2026 — `IG | 2026-09-24 | DIAGNOSTICO | promocao sem preparo` (Reel de copy, roteiro 5 do Lote 1) — LIVE ~12h32, ~2 min depois do "já postei"

Reel de copy produzido "Perdi um ótimo operacional e ganhei um péssimo gerente". O vídeo fala DIAGNÓSTICO no CTA (roteiro escrito antes da pausa do diagnóstico); decisão do user: **palavra DIAGNÓSTICO, destino RAIO-X**. Legenda e comentário fixado do roteiro, literais. Palavra nas 6 grafias do caminho diagnóstico; link `https://tatsuoacademy.com/raio-x-empresa-lucrativa/?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-24-DIAGNOSTICO`; DM "Quer enxergar o que tá travando o seu time? Começa pelo raio-x da sua empresa. A aula tá aqui." (94 chars) com botão `>> Quero a aula <<`. Modelo duplicado: a DIAGNOSTICO-5 (trocados nome, DM, título do botão e link inteiro por digitação no modal). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260924152927_918226.
- Colisão: "diagnos" só traz específicas (DIAGNOSTICO-1/3/4/5 e a do aniversário). Sem global.
- Post: apareceu no 'Mostrar Todos' como primeiro card ("O erro de promoção…", há 13 s); preview conferido (legenda com DIAGNÓSTICO).
- Pegadinha: clicar no nome no topo do editor volta pra lista (não renomeia). Renomear só pelo menu ⋮ da linha na lista.
- Ritual: lead cai em `2026-09-24-DIAGNOSTICO` na página do raio-x; ler como RAIO-X.

## 24/09/2026 — `IG | 2026-09-24 | SOBRA | ta foda empreender no brasil` (carrossel 142) — LIVE ~18h58, post no ar há 1 min

Caminho **RAIO-X**; `utm_campaign=2026-09-24-SOBRA`; link `https://tatsuoacademy.com/raio-x-empresa-lucrativa/?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-24-SOBRA`; palavra em três grafias (`SOBRA, sobra, Sobra` — palavra sem acento na origem); DM "Aguentar você já provou que sabe. Quer saber quanto sobra? Pega a aula aqui." (75 chars) com botão `>> Quero a aula <<` (herdado). Modelo duplicado: a `IG | 2026-09-24 | DIAGNOSTICO | promocao sem preparo` (mesma data e mesmo destino raio-x, então só a última palavra do UTM mudou). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260924215612_518250. Kit em `conteudo/carrosseis/142_aguentar/carousel-text.md`.

- **Colisão:** busca "sobra" trouxe 5 automações (MOP, DIAGNOSTICO-4, DONO, DENTRO, DRAGA) — o match é no TEXTO da DM, não na palavra-chave. Nenhuma tem SOBRA como gatilho, e a única global da lista (MOP) dispara em "MOP". Sem colisão.
- **Post:** primeiro card do 'Mostrar Todos' ("Eu converso com do…", há 1 minuto); preview conferido (capa TÁ F@DA + legenda nova). Toggle de comentários ON e as três respostas herdadas, mantidas.
- **ACHADO OPERACIONAL — o bug de comer caractere não aparece com `form_input`.** Sete ocorrências seguidas estão registradas acima, todas em automação escrita por DIGITAÇÃO no campo. Nesta, os três campos longos (nome da automação, palavra-chave e DM) foram preenchidos por `form_input` no ref do elemento, e **nenhum caractere foi comido**. O link também: trocado inteiro por `form_input` e conferido nas três passadas (Home / 60 setas / End) — `https://tatsuoacademy.com/raio-x-empresa-lucrativa/?utm_s…` · `…?utm_source=manychat&utm_medium=…` · `…utm_campaign=2026-09-24-SOBRA`. **Passa a ser o método padrão; digitar só quando o campo não aceitar `form_input`.** A conferência por zoom continua obrigatória de qualquer jeito.
- Pegadinha confirmada de novo: renomear só pelo menu ⋮ da linha na lista (o nome no topo do editor volta pra lista). E a URL `/cms/automations` dá 404 — a lista vive em `/fb2015128/cms`.
- Ritual: lead cai em `2026-09-24-SOBRA` na página do raio-x.

## 25/09/2026 — `IG | 2026-09-25 | PORTA | recuperacao judicial` (carrossel 148) — LIVE ~17h50, "postei, cria o Manychat" do user

Caminho **RAIO-X** (terceira específica do caminho); `utm_campaign=2026-09-25-PORTA`; link `https://tatsuoacademy.com/raio-x-empresa-lucrativa/?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-25-PORTA`; palavra em três grafias: `PORTA, porta, Porta`; DM "O que me jogou na RJ foi o que eu não sabia. Quer a aula em que você faz o raio-x da sua empresa?" (97 chars) com botão `>> Quero a aula <<` (herdado). Modelo duplicado: a `IG | 2026-09-21 | PATO | voce ja viu um pato repost` (LIVE, 86 exec. / 53,5% em 4 dias; mesmo link, só o rabo do UTM trocado por `form_input`). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260925174232_195416. Kit em `conteudo/carrosseis/148_porta-de-saida/carousel-text.md`.

- **Sessão deslogada:** o primeiro `navigate` caiu na tela de login do Manychat; pedi ao user pra logar (login nunca é do Claude) e ele logou em ~1 min. Lição: se a URL do CMS redirecionar pra `/signin`, parar e pedir o login, sem tentar nada.
- **Colisão checada:** busca "porta" devolve `Porta pra dentro` (LIVE, específica, palavra "porta pra dentro", 0 exec.) e `IG | 2026-08-21 | DENTRO | porta-pra-dentro` (LIVE, específica, palavra "dentro"). Nenhuma global e nenhuma com a palavra "porta" isolada; sem colisão.
- **Sem bug de comer caractere:** nome no modal Renomear por cmd+a + digitação (conferido Home e End); palavra, DM e link por `form_input`; link conferido Home/End e no tooltip da corrente (`…utm_campaign=2026-09-25-PORTA`).
- **Post:** a grade direta já trazia o 148 em SEGUNDO (a capa "SETEMBRO DE 2020 / A MINHA EMPRESA ENTROU EM RECUPERAÇÃO JUDICIAL", autos de processo), sem precisar de 'Mostrar Todos' nem reset do rádio; preview conferido (legenda "Setembro de 2020. A minha empresa entrou em recuperação judicial…", 2 comentários). Atualização e Ativar: **LIVE ~17h50**.
- Navegador: 3 Chromes na lista (1 macOS `ee5937df` já `inUse`/`onThisComputer` + 2 Windows de colegas), sem `AskUserQuestion`; T laranja conferido. Viewport 1253×952: lista `⋮` (1168, 384) no hover; Renomear (1130, 432), Duplicar (1125, 471); modal Renomear campo (625, 163), botão (788, 245); STOPPED `Editar` (1086, 34), `Ativar` (1156, 34); edição `Atualização` (1180, 34); botão da DM (200, 787) abre o modal do link; segundo card da grade (208, 242); aba Publicar do preview (767, 806).
- Ficha do 148 com `data_publicacao=2026-09-25`.

## 25/09/2026 — `IG | 2026-09-25 | BOLSO | 7 coisas MBV dia 1` (carrossel 149) — LIVE ~20h30, post já publicado quando o user pediu "monta o manychat"

Caminho **imersão MBV**; `utm_campaign=2026-09-25-BOLSO`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-25-BOLSO`; palavra `BOLSO, bolso, Bolso` (sem acento na origem); DM "Lucro no papel não paga boleto. Quer ver como transformar o seu em dinheiro no bolso?" (84 chars) com botão `>> Quero ver <<` (herdado). Modelo duplicado: a `IG | 2026-09-22 | DRE | crise pra culpar` (LIVE, 9 exec. / 66,7%; mesmo link, trocado inteiro por `form_input`). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260925232852_256115. Kit em `conteudo/carrosseis/149_lucro-no-papel/carousel-text.md`.

- Carrossel de fotos reais do Hélio no MBV (dia 1, Lucratividade), só copy nossa; montagem do marketing.
- **Colisão checada:** busca "bolso" traz DIVIDENDO (07/09) e DRAGA (21/08), as duas específicas e com "bolso" só no texto da DM. Sem colisão.
- **Post:** o 149 já estava em SEGUNDO na grade direta (capa "Primeiro dia do MBV. / 7 COISAS QUE EU ENSINEI HOJE", Hélio no palco); selecionado pela miniatura, preview conferido (legenda "Em 38 anos como empresário…", 2 comentários anteriores à ativação, que não disparam).
- **Sem bug de comer caractere:** nome no modal Renomear, palavra, DM e link por `form_input`; nome conferido por zoom; link conferido em três passadas (Home; Home + Right×75 = `…utm_medium=dm|&utm`; End = `…2026-09-25-BOLSO`) e de novo no tooltip da corrente depois do Ativar. Toggle de comentários ON com as três respostas herdadas.
- Navegador: 2 Chromes na lista (macOS `ee5937df` `inUse`/`onThisComputer` + 1 Windows de colega), sem `AskUserQuestion`; T laranja conferido. Viewport 1204×1001: ⋮ da linha (1123, 375) no hover; Duplicar (1080, 459); Renomear (1085, 421); botão Renomear do modal (759, 239); `Editar` (1040, 33); `Atualização` (1132, 34); `Ativar` (1109, 33); segundo card da grade (201, 236); aba Publicar do preview (739, 822); `Salvar` do modal do link (772, 246).
- Etiqueta: abaixo, 3-10 comentários em D+7 (`registro-posts.csv`, data_publicacao 2026-09-25).

## 26/09/2026 — `IG | 2026-09-26 | PODIO | 4 elementos do modelo` (carrossel 151) — LIVE ~19h22, post já publicado quando o user pediu "pode criar o manychat agora"

Caminho **RAIO-X** (quarta específica do caminho; primeira peça na voz institucional da apostila); `utm_campaign=2026-09-26-PODIO`; link `https://tatsuoacademy.com/raio-x-empresa-lucrativa/?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-26-PODIO`; palavra em seis grafias: `PODIO, podio, Podio, PÓDIO, pódio, Pódio`; DM "Antes de cobrar mais do piloto, olhe para o carro. Quer a aula em que você faz o raio-x da sua empresa?" (103 chars) com botão `>> Quero a aula <<` (herdado). Modelo duplicado: a `IG | 2026-09-25 | PORTA | recuperacao judicial` (LIVE, 3 exec. / 0% em 1 dia). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260926221939_678191. Kit em `conteudo/carrosseis/151_senna-no-fusca/carousel-text.md`.

- **DM trocada na montagem:** a do kit ("Avalie o seu modelo de negócio nos 4 elementos") prometia o que a aula do raio-x pode não entregar; a nova repete a linha de apoio da capa e mantém a pergunta do caminho RAIO-X.
- **Colisão checada:** buscas "podio" e "pódio" sem resultado. Sem colisão.
- **Post:** o 151 estava em TERCEIRO na grade direta (capa com o Hélio no palco + "OS 4 ELEMENTOS DE UM BOM MODELO DE NEGÓCIO"); selecionado pela miniatura; preview conferido (legenda v2 "Toda empresa corre numa pista…"; o preview marcava 6 curtidas e 2 comentários). No Instagram às 19h32: post no ar há ~15 min (publicado ~19h17, **collab helio.tatsuo + tatsuo.academy**, permalink /p/DdxFqRlEZBD/) e nenhum comentário visível, então nenhum PODIO ficou sem DM. Ativação ~5 min depois da publicação.
- **Sem bug de comer caractere:** nome no modal Renomear, palavra, DM e link por `form_input`; link conferido em três passadas (Home; Home + Right×75 = `…?utm_source=manychat&utm|_medium`; End = `…2026-09-26-PODIO`) e de novo no tooltip da corrente depois do Ativar. Toggle de comentários ON com as três respostas herdadas.
- **Navegador:** 3 Chromes na lista (macOS `ee5937df` `inUse`/`onThisComputer`, macOS `46b005d2` também `onThisComputer`, 1 Windows de colega), sem `AskUserQuestion`; T laranja conferido. Viewport 1204×1001: ⋮ da linha (1109, y da linha) no hover na lista de 26/09; Duplicar (1058, 648) no menu da 2ª linha; Renomear (1063, 475) no menu da 1ª; botão Renomear do modal (758, 240); `Editar` (1042, 34); `Atualização` (1132, 34); `Ativar` (1108, 33); terceiro card da grade (265, 230); aba Publicar do preview (739, 822); `Salvar` do modal do link (772, 247).
- Etiqueta: abaixo, 3-9 comentários em D+7 (`registro-posts.csv`, data_publicacao 2026-09-26).

## 26/09/2026 — `IG | 2026-09-26 | VENDER | 7 coisas MBV dia 2` (carrossel 158) — MONTADA STOPPED ~19h29, LIVE ~20h02 pelo timer das 20h01 (sem "postei"; post já no ar)

Caminho **imersão MBV**; `utm_campaign=2026-09-26-VENDER`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-26-VENDER`; palavra `VENDER, vender, Vender` (sem acento na origem); DM "Crescimento é venda que vira dividendo no seu bolso. Quer ver como eu ensino isso no MBV?" (89 chars) com botão `>> Quero ver <<` (herdado). Modelo duplicado: a `IG | 2026-09-25 | BOLSO | 7 coisas MBV dia 1` (LIVE, 1 exec. / 100%; mesmo link, trocado inteiro por `form_input`). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260926222655_689153. Kit em `conteudo/carrosseis/158_mbv-dia-2-vender/carousel-text.md`.

- **Colisão checada:** busca "vender" traz só a `IG | 2026-09-06 | DONO | caminho mais dificil` (específica; "vender" só no texto da DM; gatilho DONO). Sem colisão.
- **Sem bug de comer caractere:** nome, palavra, DM e link por `form_input`; link conferido em três passadas (Home; Home + Right×70 = `…utm_medi|um=dm`; End = `…2026-09-26-VENDER`).
- **Post:** salva STOPPED apontando pro post do modelo (149). `caffeinate -dimsu -t 5400` ligado às 19h28 e timer de shell armado pras 20h01; o "postei" do user continua sendo o gatilho mais rápido.
- **Ativação (timer 20h01):** o "postei" não veio; o timer acordou a sessão e o post do dia 2 já estava em SEGUNDO na grade direta (capa "Segundo dia do MBV. / 7 COISAS QUE EU ENSINEI HOJE.", Hélio apontando pra plateia; mesmo desenho da capa do dia 1, então conferir pelo preview e não pela miniatura). Selecionado pela miniatura; preview conferido (legenda "Todo dono de empresa conhece o mês em que a venda não vem…"); Atualização e Ativar: **LIVE ~20h02**. Link conferido no tooltip da corrente depois do Ativar (`…utm_campaign=2026-09-26-VENDER`). caffeinate encerrado.
- Etiqueta: abaixo, 2-9 comentários em D+7 (`registro-posts.csv`, data_publicacao 2026-09-26 prevista).

## 27/09/2026 — `IG | 2026-09-27 | TURMA | aftermovie MBV 6` (reel aftermovie da 6ª edição) — MONTADA STOPPED ~18h50, aguardando o "postei"

Caminho **imersão MBV**; `utm_campaign=2026-09-27-TURMA`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-27-TURMA`; palavra `TURMA, turma, Turma`; DM "Três dias pra aprender a comandar a sua empresa. Quer ver como entrar na próxima turma do MBV?" (94 chars) com botão `>> Quero ver <<` (herdado). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260927214810_496633. Kit em `conteudo/videos/2026-09-27_aftermovie-mbv-6/kit-cta.md`.

- **Colisão checada:** busca "turma" só traz a `IG | 2026-07-31 | PERFIL | Curadoria da Im…` (específica, gatilho PERFIL; "turma" só no texto da DM). Sem colisão.
- **ACHADO: a VENDER (carrossel 158, dia 2) está LIVE amarrada a um post que não existe mais.** Duplicar a VENDER devolveu o erro "A publicação do Instagram vinculada a esta automação foi excluída ou não está mais disponível". Bate com o `desempenho.json` puxado às 14h05 de 27/09, que já não tem o carrossel do dia 2 ("Todo dono de empresa conhece o mês em que a venda não vem…"). Se ele foi republicado, a VENDER precisa ser reamarrada (receita de 27/08: alternar o rádio pra "qualquer" e voltar pra "específico"), na conversa do 158. Avisado ao user.
- **Modelo:** por causa disso, duplicada a `IG | 2026-09-25 | BOLSO | 7 coisas MBV dia 1` (mesmo link base). Nome no modal Renomear, palavra, DM e link por `form_input`; conferência por JS (palavra 19 chars, DM 94 chars, link 105 chars = o tamanho esperado), Home no link (`https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=ma…`) e tooltip da corrente depois da Atualização (`…utm_campaign=2026-09-27-TURMA`). Sem bug de comer caractere.
- **Post:** salva STOPPED apontando pro post do 149. Na grade, o aftermovie ainda não aparecia (os 3 mais recentes eram cortes do MBV em tela dividida). Amarrar depois do "postei".
- Navegador: 1 Chrome na lista (macOS `ee5937df`, `inUse`), sem `AskUserQuestion`; T laranja conferido. A viewport mudou no meio da sessão (1512×812 → 1274×628). Na 1274×628: nome da 1ª linha da lista (618, 453); `Editar` (1103, 36); `Ativar` (1174, 36); `Atualização` (1198, 36); corrente do botão da DM (378, 459) com o editor rolado até o botão; `Salvar` do modal do link (817, 262).

## 28/09/2026 — `IG | 2026-09-28 | RAIO-X | ta tudo certo chefe` (carrossel 147) — MONTADA STOPPED ~18h10, LIVE ~19h05 após o "postei, pode ativar"

Caminho **RAIO-X**; `utm_campaign=2026-09-28-RAIO-X`; link `https://tatsuoacademy.com/raio-x-empresa-lucrativa/?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-28-RAIO-X` (116 chars, conferido por JS + Home/End); palavra nas **7 grafias** herdadas: `RAIO-X, raio-x, Raio-X, Raio-x, raio-X, RAIOX, raiox`; DM "Seja sincero: você sabe onde a sua empresa está apodrecendo? Pega a aula aqui." (78 chars) com botão `>> Quero a aula <<` (herdado). Modelo duplicado: a `IG | 2026-09-18 | RAIO-X | para de trabalhar` (carrossel 127, LIVE, 11 exec. / 54,5%), que continua viva e amarrada ao 127: mesma palavra em post específico diferente. URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260928210209_712585. Kit em `conteudo/carrosseis/147_ta-tudo-certo/carousel-text.md`.

- **Colisão:** a global `RAIO - X` (qualquer publicação, 1 exec. em 2 semanas, utm `raio-x-feed`) segue LIVE, mesma página; aceita como no 127. A `RAIO - X stories` é de story, não conflita.
- **Pegadinha nova do Renomear:** o botão ficou girando >15 s depois do `form_input` no nome, mas o nome GRAVOU; a lista filtrada pela busca "raio" é que continuava mostrando o nome antigo. Conferir o rename na lista SEM filtro (ordenada por modificado) antes de tentar de novo. A segunda tentativa, com a lista já re-renderizada, clicou fora das linhas (sem dano).
- **Outra sessão no painel ao mesmo tempo:** `IG | 2026-09-28 | PROBLEMA` (STOPPED) criada ~2 min antes. Não tocada.
- Nome, DM e link por `form_input`; sem bug de comer caractere. Toggle de comentários ON, três respostas herdadas.
- Navegador: 4 Chromes na lista (macOS `ee5937df` `inUse`/`onThisComputer`, macOS `46b005d2`, 2 Windows de colegas), sem `AskUserQuestion`; T laranja conferido. Viewport 1232×974: `Editar` (1065, 34); `Atualização` (1158, 34); corrente do botão da DM (365, 809) com o editor rolado até a DM; campo Link do modal (612, 193); `Salvar` (790, 252); lista sem filtro: nome da 1ª linha (595, 437).
- Salva STOPPED apontando pro post do 127. `caffeinate -dimsu -t 5400` e timer de shell pras 19h03.

## 28/09/2026 — `IG | 2026-09-28 | PROBLEMA | problema bom` (carrossel 146) — LIVE ~1 min depois da publicação, "vou postar agora, faça o manychat"

Caminho **imersão MBV**; `utm_campaign=2026-09-28-PROBLEMA`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-28-PROBLEMA`; palavra `PROBLEMA, problema, Problema`; DM "Problema você vai ter de qualquer jeito. Quer ver como eu ensino a criar o problema bom no MBV?" (95 chars) com botão `>> Quero ver <<` (herdado). Modelo duplicado: a `IG | 2026-09-27 | TURMA | aftermovie MBV 6` (LIVE, 0 exec.). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260928210111_136203. Kit em `conteudo/carrosseis/146_problema-bom/carousel-text.md`.

- **Colisão checada:** busca "problema" só traz a `IG | 2026-07-31 | MARGEM | Lucratividade sistêmica` (global legada, gatilho MARGEM; "problema" só no texto da DM). Sem colisão.
- **Gatilho é "inclui", não "exato":** o Manychat não oferece correspondência exata nesse builder (a lista mostra "comentários que inclua"). PROBLEMA é palavra comum ("meu problema é…"), então comentário de conversa pode disparar a DM. Risco aceito: quem escreve "problema" no post do problema bom está, na pior das hipóteses, recebendo o link do MBV. Conferir no ritual se a taxa de clique da PROBLEMA destoa (sinal de disparo em falso).
- **Sem bug de comer caractere:** nome no modal Renomear, palavra, DM e link por `form_input`; conferência por JS (DM 95 chars, link 108 chars = 105 da TURMA − 5 + 8).
- **Post:** salva STOPPED primeiro (o "Mostrar Todos" travou no carregamento e o 146 ainda não estava na grade); na volta, o 146 estava em PRIMEIRO na grade direta (capa "Tem um desejo que todo dono tem em comum:", dono à mesa olhando a câmera). Selecionado pela miniatura; preview conferido (legenda "Tem dono que passa o ano inteiro pedindo menos problema…"); Atualização e Ativar: **LIVE**. No Instagram: permalink /p/Dd2G4MvFCHg/, publicado "1 min" antes, **zero comentários** (o "2" do preview eram curtidas), então nenhum PROBLEMA ficou sem DM.
- Navegador: 4 Chromes na lista (macOS `ee5937df` `inUse`/`onThisComputer`, macOS `46b005d2`, 2 Windows de colegas), sem `AskUserQuestion`; T laranja conferido. Viewport 1204×1005: ⋮ da 1ª linha (1123, 427); Duplicar (1073, 511); Renomear (1078, 473) no menu da 1ª; botão Renomear do modal (759, 238); `Editar` (1041, 33); `Atualização` (1132, 33); `Ativar` (1108, 33); 1º card da grade (130, 236); botão do link na DM (355, 845) com o painel rolado; `Salvar` do modal do link (770, 246).
- Etiqueta: mediana, 12-38 comentários em D+7 (`registro-posts.csv`, data_publicacao 2026-09-28).
- **Ativação:** o timer das 19h03 acordou antes do post (não estava na grade; o mais recente era um carrossel de outra frente, "Tem dono que passa…", há 1 h); saí sem salvar. O "postei, pode ativar" veio logo depois: o 147 era o PRIMEIRO card do 'Mostrar Todos' ("Tá tudo certo, chefe…", há 12 s); selecionado pela miniatura, preview conferido (capa do caixote + legenda nova), DM e palavra conferidas por JS depois da troca de post, Atualização e Ativar: **LIVE ~19h05**. Link conferido no tooltip da corrente depois do Ativar (`…utm_campaign=2026-09-28-RAIO-X`). Viewport virou 1204×1005 no meio: `Editar` (1042, 33), `Atualização` (1131, 33), `Ativar` (1108, 33), 'Mostrar Todos' (152, 305), primeiro card do modal (393, 221), X do modal (920, 43).

## 29/09/2026 — `utm_content` com o link do post (retroativo nas automações de 22 a 28/09)

Decisão do user: todo link de DM leva `&utm_content=<link limpo do post>` no fim, pro CRM pôr o post no card do lead e o SDR abrir antes de ligar (regra na seção do padrão de UTM, no topo). Aplicado nas 13 automações dos 7 dias anteriores. Cada uma foi conferida recarregando a página e lendo o `utm_content` gravado, e todas continuaram LIVE:

| Automação | `utm_content` | Estado |
|---|---|---|
| 2026-09-22 MODELO | https://www.instagram.com/p/DdmVNhuESdl/ | feito |
| 2026-09-22 DRE | https://www.instagram.com/p/DdmvWgoEWRe/ | feito |
| 2026-09-23 BASICO | https://www.instagram.com/p/DdoyM42kWRG/ | feito |
| 2026-09-23 307 | https://www.instagram.com/p/DdpYYdikd3l/ | feito |
| 2026-09-24 DIAGNOSTICO (reel) | https://www.instagram.com/reel/DdrNbEXR-te/ | feito |
| 2026-09-24 SOBRA | https://www.instagram.com/p/Ddr5zgxkRi2/ | feito |
| 2026-09-25 PORTA | (https://www.instagram.com/p/DduBSH1EZIl/) | **APAGADO** (decisão do user, 29/09): post removido do Instagram; automação sem post, não dispara. Não religar. |
| 2026-09-25 BOLSO | https://www.instagram.com/p/Dduo-9WESCq/ | feito |
| 2026-09-26 PODIO | https://www.instagram.com/p/DdxFqRlEZBD/ | feito |
| 2026-09-26 VENDER | — | **APAGADO** (decisão do user, 29/09): post do dia 2 apagado em 27/09; automação sem post, não dispara. Não religar. |
| 2026-09-27 TURMA (reel) | https://www.instagram.com/reel/DdzohkuxXK1/ | feito (LIVE e amarrada ao aftermovie, conferido pela legenda no preview; 0 envios até agora) |
| 2026-09-28 PROBLEMA | https://www.instagram.com/p/Dd2G4MvFCHg/ | feito |
| 2026-09-28 RAIO-X | https://www.instagram.com/p/Dd2NwlQkfrQ/ | feito |

**Receita que funcionou, só com JS (sem bug de comer caractere e sem coordenada):**
1. Abrir a URL do easy-builder e esperar ~9 s (antes disso o Editar não pega).
2. Clicar em `Editar` pelo texto do botão.
3. Abrir o modal do link clicando na linha do botão da DM: é a folha cujo texto casa `^>>.*<<$`, subindo até o ancestral que tem o `svg` da corrente. **Cuidado:** o "Adicionar Um Link" logo abaixo abre um modal VAZIO (é pra criar botão novo), e o `find` confunde os dois.
4. Pegar o input cujo valor contém `utm`, conferir que termina em `utm_campaign=<AAAA-MM-DD-PALAVRA>` e que ainda não tem `utm_content`, e acrescentar o sufixo pelo setter nativo (`Object.getOwnPropertyDescriptor(HTMLInputElement.prototype,'value').set`) + eventos `input` e `change`.
5. Clicar em `Salvar` (modal) e depois em `Atualização`, recarregar e procurar `utm_content` no HTML da página. O toast "As alterações foram salvas" às vezes não aparece a tempo e o valor grava mesmo assim (PODIO); quem confirma é o recarregar.
- O JS devolve a query string do link como `[BLOCKED: Cookie/query string data]`. Por isso a conferência compara com o valor esperado (`===` / `endsWith`) e o tamanho, sem ler o valor direto.
- Com post morto ("Não conseguimos encontrar uma conexão"), o Atualização não salva nada. Checar isso antes de mexer.

## 29/09/2026 — `IG | 2026-09-29 | RAIO-X | so sobrou a casa` (carrossel 164) — LIVE ~20h41, ~5 h DEPOIS da publicação

Caminho **RAIO-X**; `utm_campaign=2026-09-29-RAIO-X`; `utm_content=https://www.instagram.com/p/Dd4FjSdEY1N/`; link `https://tatsuoacademy.com/raio-x-empresa-lucrativa/?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-29-RAIO-X&utm_content=https://www.instagram.com/p/Dd4FjSdEY1N/` (169 chars, conferido por JS e recarregando); DM "Faturou milhões e só sobrou o pró-labore? Pega a aula em que você faz o raio-x da sua empresa." (94 chars), botão `>> Quero a aula <<` (herdado). Modelo duplicado: a `IG | 2026-09-28 | RAIO-X | ta tudo certo chefe` (carrossel 147, LIVE, 43 exec. / 46,5%). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260929203950_495711. Kit em `conteudo/carrosseis/164_so-sobrou-a-casa/carousel-text.md`.

- **Atraso:** o user avisou "acabei de postar", mas o post já estava no ar havia ~5 h (56 comentários na hora de amarrar). O Chrome conectado de início (`46b005d2`) estava DESLOGADO do Manychat; foi preciso o user abrir a janela da Tatsuo e clicar Conectar (`switch_browser`). Nada foi digitado na tela de login.
- **ACHADO: grafia com ESPAÇO não dispara.** No post, boa parte comentou "Raio X" / "Raio x" (espaço, sem hífen). Nenhuma das 7 grafias bate ("inclui" compara o texto: "raio x" não contém "raio-x" nem "raiox"). Só os "Raio-x" com hífen tinham resposta, provavelmente da global `RAIO - X` (qualquer publicação, utm `raio-x-feed`), já que a específica ainda não existia. Na específica nova entraram mais 5 grafias: `RAIO X, raio x, Raio X, Raio x, raio X` (12 no total, conferido recarregando). Quem comentou com espaço antes disso ficou sem DM (Manychat não é retroativo).
- **Regra daqui pra frente:** automação RAIO-X leva as 12 grafias. **Aplicado a pedido do user (29/09 ~20h55) nas outras quatro, todas conferidas recarregando e todas LIVE:** `2026-09-28 RAIO-X` (147; content20260928210209_712585), `2026-09-18 RAIO-X` (127; content20260918181315_612383), global `RAIO - X` (qualquer publicação; content20260912200014_283670; 14 exec. até aqui) e `RAIO - X stories` (resposta a story; content20250423134755_303293; 17 exec.). Edição feita clicando no campo pela ref do `find` + cmd+a + digitação (o setter por JS sozinho não persistia: o valor voltava duplicado quando se digitava depois). Busca da lista: "RAIO - X" com espaços não filtra; "stories" e a URL `?search=RAIO%20-` filtram.
- Navegador: `46b005d2` (macOS, deslogado) → `switch_browser` → "Tatsuo Academy"; T laranja conferido. Viewport 1204×1005: ⋮ da linha (1110, y) após hover; Duplicar (1058, 645) no menu da 2ª linha; Renomear (1065, 473) no menu da 1ª; botão Renomear (759, 238); `Editar` (1041 ou 1004, 33); `Atualização` (1132, 33); `Ativar` (1108, 33); 1º card da grade (128, 236); botão da DM (343, 845); `Salvar` do link (771, 246). Permalink do post lido na grade do perfil no Instagram (o easy-builder não expõe).

## 29/09/2026 — `IG | 2026-09-29 | ADULTO | quem so faz o que gosta e crianca` (carrossel 167) — MONTADA STOPPED antes do post, LIVE ~1 min depois do "postei"

Caminho **imersão MBV**; `utm_campaign=2026-09-29-ADULTO`; `utm_content=https://www.instagram.com/p/Dd4xS9qEfIO/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-29-ADULTO&utm_content=https://www.instagram.com/p/Dd4xS9qEfIO/` (159 chars, conferido recarregando); palavra `ADULTO, adulto, Adulto`; DM "Fazer o básico todo dia é chato mesmo. Quer ver como eu ensino a parte chata no MBV?" (84 chars), botão `>> Quero ver <<` (herdado). Modelo duplicado: a `IG | 2026-09-28 | PROBLEMA | problema bom` (LIVE, 13 exec. / 69,2%; intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260929215132_991914. Kit em `conteudo/carrosseis/167_crianca/carousel-text.md`.

- Montada STOPPED enquanto o user postava; o post foi achado na grade do perfil (`Dd4xS9qEfIO`, legenda "Eu nasci vendendo…") no mesmo minuto do "postei", selecionado como 2º card da grade do easy-builder (preview conferido: capa do menino emburrado), `utm_content` acrescentado, Atualização e Ativar: **LIVE**.
- Gotchas desta montagem: clicar no NOME da linha abre a automação (quase editei a PROBLEMA; nada foi alterado); o ⋮ de dentro da automação só tem "Apagar", Duplicar só no ⋮ da LISTA (1123, y da linha); o `find` devolveu o "Adicionar Um Link" (modal vazio) como se fosse o botão da DM — o certo é clicar no texto do botão `>> Quero ver <<` (200, 845) com o painel rolado.
- Navegador: `ee5937df` "Tatsuo Academy" já em uso nesta sessão; T laranja conferido.

## 30/09/2026 — `IG | 2026-09-30 | PADRAO | telefone sem fio` (carrossel 165) — LIVE ~14h36, ~4 min depois do "postei agora"

Caminho **imersão MBV**; `utm_campaign=2026-09-30-PADRAO`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-30-PADRAO` (106 chars, conferido por JS + Home/End + tooltip depois do Ativar); palavra em seis grafias: `PADRAO, padrao, Padrao, PADRÃO, padrão, Padrão`; DM "Ou você acompanha o que escreveu, ou cada um faz do seu jeito. Quer ver como eu ensino isso?" (92 chars) com botão `>> Quero ver <<` (herdado). Modelo duplicado: a `IG | 2026-09-27 | TURMA | aftermovie MBV 6`. URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260930173306_856246. Kit em `conteudo/carrosseis/165_telefone-sem-fio/carousel-text.md`.

- **O link da TURMA tinha um `&utm_content=https://www.instagram.com/reel/…`** acrescentado depois (por outra sessão ou pelo user). Aqui o link foi trocado inteiro pelo padrão data+palavra, sem `utm_content`.
- **Post:** primeiro card do 'Mostrar Todos' ("Empresário, seja sinc…", há 58 s); selecionado pela miniatura, preview conferido (capa "Você explicou direitinho. / E FIZERAM TUDO DIFERENTE." + legenda v5); palavra e DM conferidas por JS depois da troca de post.
- Rename pelo modal com `form_input` + botão por ref; conferido na lista sem filtro. Sem bug de comer caractere.
- Navegador: 5 Chromes na lista (macOS `ee5937df` `inUse`/`onThisComputer`, outros 2 macOS e 2 Windows), sem `AskUserQuestion`; T laranja conferido. Viewport 1204×1005 → 1232×974 no meio: `Editar` (1041, 33), `Atualização` (1131, 33), `Ativar` (1135, 34) na 1232.
- Etiqueta: acima, 40-200 comentários em D+7 (`registro-posts.csv`).

## 30/09/2026 — `IG | 2026-09-30 | BASTIDOR | palco e bastidor` (carrossel 169, formato twitter feito pelo user no Canva) — MONTADA STOPPED antes do post, LIVE ~2 min depois do "postei"

Caminho **imersão MBV**; `utm_campaign=2026-09-30-BASTIDOR`; `utm_content=https://www.instagram.com/p/Dd7UJTokdHI/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-09-30-BASTIDOR&utm_content=https://www.instagram.com/p/Dd7UJTokdHI/` (161 chars, conferido recarregando); palavra `BASTIDOR, bastidor, Bastidor` ("bastidores" também dispara, gatilho é "inclui"); DM "Palco você já vê de graça no feed. Quer ver o bastidor que eu abro no MBV?" (74 chars), botão `>> Quero ver <<` (herdado). Modelo duplicado: a `IG | 2026-09-29 | ADULTO | quem so faz o que gosta e crianca` (LIVE, 6 exec. / 50% em ~1 dia; intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20260930212412_977155.

- Post achado na grade do perfil (`Dd7UJTokdHI`, legenda "Todo dia chega no celular do empresário…"), 2º card da grade do easy-builder, preview conferido (print de tweet "Na internet, todo mundo quer ser dono de empresa…"). Navegador `ee5937df`, T laranja conferido.

## 01/10/2026 — `IG | 2026-10-01 | VINCULO | almoco de terca` (carrossel 171) — MONTADA STOPPED antes do post, LIVE ~2 min depois do "postei"

Caminho **imersão MBV**; `utm_campaign=2026-10-01-VINCULO`; `utm_content=https://www.instagram.com/p/Dd9jZ0slCQT/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-01-VINCULO&utm_content=https://www.instagram.com/p/Dd9jZ0slCQT/` (160 chars, conferido recarregando); palavra `VINCULO, vinculo, Vinculo, VÍNCULO, vínculo, Vínculo`; DM "Ninguém sente falta do que nunca marcou. Quer ver como eu ensino a montar a cultura no MBV?" (92 chars), botão `>> Quero ver <<` (herdado). Modelo duplicado: a `IG | 2026-09-30 | BASTIDOR | palco e bastidor` (LIVE, 2 exec. / 100%; intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261001181704_289905. Post achado na grade do perfil (legenda "Faz um teste rápido comigo…"), 2º card da grade do easy-builder, preview conferido (capa do porta-retrato com a marmita). Navegador "Tatsuo Academy", T laranja conferido; a extensão caiu uma vez no meio e reconectou sozinha.

## 01/10/2026 — `IG | 2026-10-01 | MBV | dia do vendedor` (carrossel 173) — MONTADA STOPPED antes do post, LIVE ~1 min depois do "postei"

Caminho **imersão MBV**; `utm_campaign=2026-10-01-MBV`; palavra `MBV, mbv, Mbv` (a global legada `MBV` segue LIVE; a específica tem prioridade no post); DM "Eu resolvia tudo vendendo mais e perdia dinheiro. Quer aprender a parte que a venda não resolve?" (96 chars), botão `>> Quero ver <<` (herdado). Modelo duplicado: a `IG | 2026-10-01 | VINCULO | almoco de terca` (LIVE; intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261001231134_170525. Kit em `conteudo/carrosseis/173_dia-do-vendedor/carousel-text.md`.

- Gotcha: o campo da DM comeu caractere duas vezes (o espaço depois de "dinheiro." e o "u" de "Quer"); corrigido no lugar e conferido por JS antes do Atualização.
- Post `Dd-EK48ESAL` (2º card da grade do easy-builder, preview conferido: capa "MAIS DE 7 BILHÕES DE REAIS"); `utm_content=https://www.instagram.com/p/Dd-EK48ESAL/` (link de 156 chars); Atualização, Ativar, conferido recarregando (LIVE, utm e post no HTML). Navegador `ee5937df` (macOS, em uso), T laranja conferido.

## 02/10/2026 — CORREÇÃO da `IG | 2026-10-01 | MBV | dia do vendedor` (carrossel 173): post apagado e repostado

O 173 foi apagado e repostado (o `Dd-EK48ESAL` deu "Esta página não está disponível"); o post vivo é `Dd-RFHdEVIl` (há ~16 h na hora da descoberta, 0 envios). A automação ficou LIVE amarrada ao post morto ("Não conseguimos encontrar uma conexão"), então nenhum comentário MBV no repost recebeu DM até 02/10 ~14h20. Corrigido: grade forçada a carregar alternando o gatilho (qualquer → específica, sem salvar no meio), post novo selecionado em "Mostrar Todos" (card "MAIS DE 7 BILHÕES"), `utm_content` trocado pra `https://www.instagram.com/p/Dd-RFHdEVIl/`, Atualização; conferido recarregando (LIVE, código novo no HTML, o antigo não). Manychat não é retroativo: quem comentou antes da correção ficou sem DM.
- **Regra nova:** quando o user disser que repostou ou corrigiu a legenda, conferir se o código do post mudou (editar legenda mantém o código; apagar e repostar troca).

## 02/10/2026 — `IG | 2026-10-02 | EXEMPLO | tres regras` (carrossel 172) — LIVE ~5 min depois do "postei"

Caminho **imersão MBV**; `utm_campaign=2026-10-02-EXEMPLO`; `utm_content=https://www.instagram.com/p/Dd__9s-kWB9/` (link de 160 chars); palavra `EXEMPLO, exemplo, Exemplo`; DM "Liderar pelo exemplo se aprende. Quer ver como eu ensino isso no MBV?" (69 chars; o campo comeu o espaço de "eu ensino", corrigido e conferido por JS), botão `>> Quero ver <<` (herdado). Duplicada da MBV do 173 (intocada além da correção acima). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261002171829_663629. Post selecionado em "Mostrar Todos" (card "SEJA EXEMPLO", legenda "Tem uma pergunta que eu faço…"); conferido recarregando (LIVE, utm e post no HTML). Navegador Chrome da Tatsuo, T laranja conferido.

## 02/10/2026 — `IG | 2026-10-02 | GARANTIA | 30 mil nao e salario de dono` (carrossel 183) — LIVE ~5 min depois do "postei"

Caminho **imersão MBV**; `utm_campaign=2026-10-02-GARANTIA`; `utm_content=https://www.instagram.com/p/DeAIdLJlJT7/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-02-GARANTIA&utm_content=https://www.instagram.com/p/DeAIdLJlJT7/`; palavra `GARANTIA, garantia, Garantia` (busca "garantia" no painel: nenhuma automação, sem colisão); DM "Dono que põe a casa na garantia tem que ser pago pelo risco. Quer ver como eu ensino isso no MBV?" (97 chars), botão `>> Quero ver <<` (herdado). Duplicada da `IG | 2026-10-02 | EXEMPLO | tres regras` (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261002183136_508527.

- Post em 1º na grade do easy-builder (capa "R$ 30 MIL NÃO É SALÁRIO DE DONO", legenda "Saiu nesta semana…" no preview); código achado na grade do perfil. Palavra, DM e link por `form_input` (sem bug de comer caractere; conferido por JS). Conferido recarregando: LIVE, utm e código novos no HTML, os do modelo não.
- Gotcha: o "<" do topo da automação aberta por URL direta funciona como voltar do navegador (caiu na nova guia); pra lista, usar o ícone Automação da barra lateral. Navegador `ee5937df` (macOS, em uso), T laranja conferido.

## 03/10/2026 — `IG | 2026-10-03 | BRILHO | brilho nao se treina` (carrossel 182) — LIVE poucos minutos depois do "estou postando"

Caminho **imersão MBV**; `utm_campaign=2026-10-03-BRILHO`; `utm_content=https://www.instagram.com/p/DeCexgUEXP_/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-03-BRILHO&utm_content=https://www.instagram.com/p/DeCexgUEXP_/`; palavra `BRILHO, brilho, Brilho` (busca "brilho" no painel: nenhuma automação, sem colisão); DM "Brilho não se treina, se pega. Quer ver como eu ensino a construir uma casa que acende o time?" (95 chars), botão `>> Quero ver <<` (herdado). Duplicada da `IG | 2026-10-02 | GARANTIA | 30 mil nao e salario de dono` (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261003162616_449779.

- Post em 2º na grade do easy-builder (capa "EM SEIS MESES, ELE FICOU COM A SUA CARA", legenda da 6x1 no preview); código achado na grade do perfil helio.tatsuo. Nome, palavra, DM e link por `form_input`; conferido recarregando: LIVE, utm e código novos no HTML, os do modelo não. Navegador `ee5937df` (único na lista, macOS, em uso), T laranja e "Olá, Tatsuo!" conferidos.
- Gotcha: `/fb2015128/automations` dá 404; a lista é `/fb2015128/cms`.

## 03/10/2026 — `IG | 2026-10-03 | ENTREGA | folha paga duas vezes` (carrossel 180) — MONTADA STOPPED ~18h25, LIVE ~19h05 por alarme da própria sessão (post agendado pelo user pras 19h)

Caminho **imersão MBV**; `utm_campaign=2026-10-03-ENTREGA`; `utm_content=https://www.instagram.com/p/DeDFWO-kvuf/`; palavra `ENTREGA, entrega, Entrega` (a busca "entrega" acha RAIZ, PREPARO e SONHO só pelo texto da DM; todas de post específico, sem colisão); DM "Folha se paga uma vez só. Quer ver como eu ensino o time a entregar o que foi contratado?" (89 chars), botão `>> Quero ver <<` (herdado). Duplicada da `IG | 2026-10-03 | BRILHO | brilho nao se treina` (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261003212219_525367.

- Montada parada ainda presa ao post do BRILHO e sem `utm_content`; às 19h02 um CronCreate da própria sessão (não uma tarefa agendada) achou o post na grade do perfil, trocou o post (2º card, prévia "E O SERVIÇO VOLTA TODO PRA MESA DO DONO"), completou o link, Atualização, Ativar. Conferido recarregando: LIVE, código e utm novos no HTML, o post do BRILHO não. Funcionou porque a sessão já tinha o Chrome `ee5937df` em uso: na hora havia 2 macOS na lista e a ferramenta não pediu escolha.
- Gotcha: a busca do painel demora a indexar nome recém-trocado; pra achar a cópia renomeada, usar a lista sem filtro.

## 04/10/2026 — `IG | 2026-10-04 | SONHO | sonho do funcionario` (carrossel 184) — MONTADA STOPPED ~14h25, LIVE ~15h08 (post agendado pelo user pras 14h40)

Caminho **imersão MBV**; `utm_campaign=2026-10-04-SONHO`; `utm_content=https://www.instagram.com/p/DeFMTrVkVIu/`; palavra `SONHO, sonho, Sonho` (a outra SONHO, de 25/08, é de post específico do 50; sem colisão); DM "Ninguém acorda cedo pelo sonho do patrão. Quer ver como eu ensino a montar essa cultura no MBV?" (93 chars), botão `>> Quero ver <<` (herdado). Duplicada da ENTREGA do 180 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261004171431_455603.

- **Atraso de ~28 min:** o alarme das 14h41 achou o post (`DeFMTrVkVIu`, "1 min", legenda e "Comenta SONHO" conferidas), mas o Manychat caiu entre ~14h44 e ~15h05 (app.manychat.com com timeout de TCP; Google e Instagram normais; voltou e caiu de novo às 14h52). Quando o painel voltou, a grade de posts do easy-builder ficou em quadrados cinza por >40 s, mesmo alternando o gatilho; cancelado sem salvar. Na tentativa das 15h07 a grade carregou: post em 3º card, prévia conferida (capa "QUAL É O SONHO DO SEU FUNCIONÁRIO?"), link completado, Atualização, Ativar. Conferido recarregando: LIVE, `DeFMTrVkVIu` e utm no HTML, `DeDFWO` (post do 180) não.
- Gotcha: a navegação do Chrome pro Manychat logo depois do Instagram mostrou página de erro na mesma aba; aba nova resolveu quando o serviço voltou.
- A AGORA do 179 (`IG | 2026-10-04 | AGORA | dono pago agora`, content20261004172240_834544) foi montada STOPPED junto, com alarme pras 15h41 (post do user às 15h40).

## 04/10/2026 — `IG | 2026-10-04 | AGORA | dono pago agora` (carrossel 179) — MONTADA STOPPED ~14h25, LIVE ~15h49 (post do user ~15h40)

Caminho **imersão MBV**; `utm_campaign=2026-10-04-AGORA`; `utm_content=https://www.instagram.com/p/DeFdjfqkUX0/`; palavra `AGORA, agora, Agora`; DM "Dono tem que ser pago agora, não lá na frente. Quer ver como eu ensino isso no MBV?" (84 chars), botão `>> Quero ver <<` (herdado). Duplicada da ENTREGA do 180 junto com a SONHO. URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261004172240_834544.

- Ativada no "postei" do user (o alarme das 15h41 não chegou a rodar; cancelado depois da ativação). Post achado na grade do perfil (`DeFdjfqkUX0`, "6 min", legenda "Tem uma frase que eu escuto…" + "Comenta AGORA" conferidas); 2º card da grade do easy-builder, prévia conferida (capa "QUANDO A EMPRESA CRESCER, EU ME PAGO."). Manychat ainda oscilando (página de erro em 2 de 3 cargas; curl 000/302/000); na 3ª carregou. Conferido recarregando: LIVE, `DeFdjfqkUX0` e utm no HTML, `DeDFWO` não.

## 05/10/2026 — `IG | 2026-10-05 | ESCOLA | melhores saem pra crescer` (carrossel 188) — MONTADA STOPPED antes do post, LIVE ~2 min depois do "postei"

Caminho **imersão MBV**; `utm_campaign=2026-10-05-ESCOLA`; `utm_content=https://www.instagram.com/p/DeHuKUvkWjt/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-05-ESCOLA&utm_content=https://www.instagram.com/p/DeHuKUvkWjt/`; palavra `ESCOLA, escola, Escola` (inédita); DM "Gente boa fica onde tem escola. Quer ver como eu ensino o dono a fazer o time crescer aqui dentro?" (98 chars), botão `>> Quero ver <<` (herdado). Duplicada da AGORA do 179 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261005171204_286871.

- Post achado na grade do perfil (`DeHuKUvkWjt`, "1 min", legenda e "Comenta ESCOLA" conferidas), 2º card da grade do easy-builder, prévia conferida (capa "OU PRECISAM SAIR PRA CRESCER?"). Conferido recarregando: LIVE, código e utm no HTML, o post do 179 não. Navegador `ee5937df`, viewport 1183: `Editar` (1024, 33).

## 05/10/2026 — `IG | 2026-10-05 | FOCO | pare de se iludir` (carrossel 189) — MONTADA STOPPED 18h22, alarme da sessão às 19h07 (post do user às 19h05)

Caminho **imersão MBV**; `utm_campaign=2026-10-05-FOCO` (+ `utm_content` na ativação); palavra `FOCO, foco, Foco` (inédita); DM "Foco no básico vale mais que mil estratégias. Quer ver como eu ensino a arrumar a casa no MBV?" (94 chars), botão `>> Quero ver <<`. Duplicada da ESCOLA (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261005212054_451669.
- Prova de vida da ESCOLA: o primeiro comentário do post ("Escola", 4 h depois de publicar) gerou 1 disparo em menos de 1 minuto.
- **LIVE ~19h15**, no "postei" do user. O post não saiu às 19h05 (alarmes de 19h07 e 19h11 não acharam nada no perfil e não ativaram); saiu ~19h14 como `DeIQV9tES7n` (legenda "Toda semana aparece…" e "Comenta FOCO" conferidas, "24 s"). 1º card da grade do easy-builder, prévia conferida (capa "PARE DE SE ILUDIR."). Link com `utm_content=https://www.instagram.com/p/DeIQV9tES7n/`. Conferido recarregando: LIVE, código e utm no HTML, o do ESCOLA não. Viewport 1213: `Editar` em (1050, 33).

## 06/10/2026 — `IG | 2026-10-06 | CLAREZA | o preco de ser empresario` (carrossel 193) — LIVE ~3 min depois do "já postei"

Caminho **imersão MBV**; `utm_campaign=2026-10-06-CLAREZA`; `utm_content=https://www.instagram.com/p/DeKjLKzlOEZ/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-06-CLAREZA&utm_content=https://www.instagram.com/p/DeKjLKzlOEZ/` (160 chars, conferido recarregando); palavra `CLAREZA, clareza, Clareza`; DM "Ninguém gosta de falar desse preço. Quer ver como eu ensino a ter clareza da sua empresa no MBV?" (96 chars), botão `>> Quero ver <<` (herdado). Modelo duplicado: a `IG | 2026-10-01 | VINCULO | almoco de terca` (LIVE, 4 exec. / 50%; intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261006193711_815810. Post amarrado como 2º card da grade (preview: capa da varanda com a cadeira de balanço). Botões achados pelo `find` com ref (o viewport mudou de novo pra 1232×964; coordenada fixa não serve mais).

## 06/10/2026 — `IG | 2026-10-06 | VERDADE | deus nao e argumento de venda` (carrossel 202) — MONTADA STOPPED antes do post, LIVE ~2 min depois de o post subir

Caminho **imersão MBV**; `utm_campaign=2026-10-06-VERDADE`; `utm_content=https://www.instagram.com/p/DeKzkOKEVi6/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-06-VERDADE&utm_content=https://www.instagram.com/p/DeKzkOKEVi6/`; palavra `VERDADE, verdade, Verdade` (a busca "verdade" acha só a PREPARO de 20/08 pelo texto da DM, de post específico; sem colisão); DM "Quem tem método não precisa de milagre pra vender. Quer ver como eu ensino gestão de verdade no MBV?" (100 chars), botão `>> Quero ver <<` (herdado). Duplicada da CLAREZA do 193 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261006215719_299290.

- Montada parada com o post ainda do 193 e sem `utm_content`; o post apareceu no perfil (`DeKzkOKEVi6`, legenda "Eu sei que este post vai render comentário bravo…") minutos depois do "vou postar agora". 1º card da grade do easy-builder ("há 50 segundos"), prévia conferida (capa "USAR DEUS PRA VENDER É ABUSAR DE QUEM JÁ ESTÁ DE JOELHOS"). Palavra, DM e link por `form_input`. Conferido recarregando: LIVE, código e utm novos no HTML, o do 193 não. Navegador `ee5937df`, T laranja conferido.
- Gotcha: o menu ⋮ do topo da automação aberta só tem Apagar; renomear é pelo ⋮ da linha na lista.

## 07/10/2026 — `IG | 2026-10-07 | REI | quem executa e rei` (carrossel 196) — MONTADA STOPPED ~14h40, LIVE ~15h04 (post agendado pelo user pras 15h)

Caminho **imersão MBV**; `utm_campaign=2026-10-07-REI`; `utm_content=https://www.instagram.com/p/DeM9BzbFJdD/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-07-REI&utm_content=https://www.instagram.com/p/DeM9BzbFJdD/`; palavra `REI, rei, Rei` (busca "rei" no painel: só a nova, sem colisão); DM "Saber todo mundo sabe. Quer ver como eu ensino a transformar gestão em rotina no MBV?" (85 chars), botão `>> Quero ver <<` (herdado). Duplicada da VERDADE do 202 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261007173941_87591.

- Montada parada presa ao post do 202 e sem `utm_content`; timer de shell às 15h01 achou o post na grade do perfil (`DeM9BzbFJdD`, legenda "Comida que entra…"). Não estava entre os 4 cards da grade do easy-builder; achado em "Mostrar Todos" (1º card, "há 2 minutos", capa "COM OBESIDADE MENTAL."). Palavra, DM e link por `form_input`. Conferido recarregando: LIVE, código e utm novos no HTML, os do 202 não; DM exata no textarea. Navegador `ee5937df`, T laranja conferido.

## 07/10/2026 — `IG | 2026-10-07 | PEGADA | o sucesso deixa pegadas` (carrossel 195) — LIVE ~2 min depois do "já postei"

Caminho **imersão MBV**; `utm_campaign=2026-10-07-PEGADA`; `utm_content=https://www.instagram.com/p/DeNVorrEbxZ/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-07-PEGADA&utm_content=https://www.instagram.com/p/DeNVorrEbxZ/`; palavra `PEGADA, pegada, Pegada` (busca "pegada" no painel: nenhuma automação, sem colisão); DM "Nenhuma pegada passa pelo atalho. Quer ver o caminho que eu ensino no MBV?" (74 chars), botão `>> Quero ver <<` (herdado). Duplicada da REI do 196 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261007213445_090359.

- Montada a partir do "vou postar agora"; o "já postei" chegou com a automação no meio. Código achado na grade do perfil (`DeNVorrEbxZ`, 4º link depois dos 3 fixados; legenda "Vou te falar uma coisa que guru nenhum…"). Não estava nos 4 cards da grade do easy-builder; achado em "Mostrar Todos" (1º card, "há 46 segundos", capa "NENHUMA PASSA PELO ATALHO."). Palavra, DM e link por `form_input`. Conferido recarregando: LIVE, código e utm novos no HTML, os do 196 não; DM exata no HTML. Navegador `ee5937df` (em uso), T laranja conferido; viewport 1182.

## 08/10/2026 — `IG | 2026-10-08 | PROSPERO | regra numero um` (carrossel 199) — MONTADA STOPPED ~13h35, LIVE ~14h09 (post agendado pelo user pras 14h05)

Caminho **imersão MBV**; `utm_campaign=2026-10-08-PROSPERO`; `utm_content=https://www.instagram.com/p/DePbgyvkTi5/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-08-PROSPERO&utm_content=https://www.instagram.com/p/DePbgyvkTi5/`; palavra em SEIS grafias (próspero leva acento): `PROSPERO, prospero, Prospero, PRÓSPERO, próspero, Próspero` (buscas "prospero" e "próspero" no painel: nenhuma automação, sem colisão); DM "Empresa próspera faz gente próspera. Quer ver como eu ensino o dono a cumprir a regra número um?" (98 chars), botão `>> Quero ver <<` (herdado). Duplicada da PEGADA do 195 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261008163142_255155.

- Montada parada presa ao post do 195 e sem `utm_content`; timer de shell (com caffeinate) às 14h06 achou o post na grade do perfil (`DePbgyvkTi5`, 4º link depois dos 3 fixados; legenda "Em algum momento ficou feio…"). Em "Mostrar Todos" era o 1º card ("há 2 minutos", capa "SOBRE A MISSÃO DE UM EMPRESÁRIO."); prévia conferida. Palavra, DM e link por `form_input`. Conferido recarregando: LIVE, código e utm novos no HTML, o post do 195 não. Navegador `ee5937df` (em uso; 4 na lista, 2 Windows de fora).

## 08/10/2026 — `IG | 2026-10-08 | MAESTRO | maestro em gente` (carrossel 204) — MONTADA STOPPED ~18h25, LIVE ~19h04 (post agendado pelo user pras 19h)

Caminho **imersão MBV**; `utm_campaign=2026-10-08-MAESTRO`; `utm_content=https://www.instagram.com/p/DeP9UJeFK1x/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-08-MAESTRO&utm_content=https://www.instagram.com/p/DeP9UJeFK1x/`; palavra `MAESTRO, maestro, Maestro` (busca "maestro" no painel: nenhuma automação, sem colisão); DM "Quem não entende de pessoas não entende de negócios. Quer ver como eu ensino o dono a virar maestro em gente?" (106 chars, a do kit do 204), botão `>> Quero ver <<` (herdado). Duplicada da PROSPERO do 199 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261008211835_439759.

- Montada parada presa ao post do 199 e sem `utm_content`; timer de shell (com caffeinate) às 19h01 achou o post na grade do perfil (`DeP9UJeFK1x`, legenda "Muito dono confunde estar em tudo com estar no comando…", conferida contra o carousel-text). Em "Mostrar Todos" era o 1º card ("há 3 minutos", capa "DOIS CAMINHOS."); prévia conferida. Conferido recarregando: LIVE, código e utm novos no HTML, o post do 199 não; 1 botão só.
- **Gotcha novo:** o `find` por "botão de link" devolveu o `Adicionar Um Link` (cria um SEGUNDO botão, modal com texto e link vazios) em vez do botão existente `>> Quero ver <<`. Pegou porque o modal abriu com "previous: ''" no form_input; cancelado sem salvar. Regra: pra trocar o link, clicar no próprio `>> Quero ver <<` (o modal certo abre com o texto do botão preenchido) e conferir no fim que há 1 botão só.
- Gotcha repetido: depois de `navigate`, o 1º clique em Editar não pega; 2º clique abre.

## 09/10/2026 — `IG | 2026-10-09 | GANA | remedio pro desmotivado` (carrossel 198) — LIVE ~13h46, logo depois do "vou postar agora"

Caminho **imersão MBV**; `utm_campaign=2026-10-09-GANA`; `utm_content=https://www.instagram.com/p/DeR9wWrEWzY/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-09-GANA&utm_content=https://www.instagram.com/p/DeR9wWrEWzY/`; palavra `GANA, gana, Gana` (busca "gana" no painel: nenhuma automação, sem colisão); DM "Quem enxerga o número levanta com gana. Quer ver como eu ensino isso no MBV?" (78 chars, a do kit do 198), botão `>> Quero ver <<` (herdado). Duplicada da MAESTRO do 204 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261009164330_014557.

- O post já estava no perfil quando a automação ficou pronta (`DeR9wWrEWzY`, legenda "Tem segunda que eu também não quero ir…", conferida contra o carousel-text), então link e post entraram juntos, sem passar pelo STOPPED preso ao post anterior. 2º card da grade do easy-builder (capa "LEVANTA E VAI TRABALHAR."); prévia conferida. Link editado clicando no próprio `>> Quero ver <<` (modal abriu com o texto do botão preenchido). Conferido recarregando: LIVE, código e utm novos no HTML, os do 204 não; 1 botão só. Viewport 1176; o ⋮ da linha só aparece no hover.

## 09/10/2026 — `IG | 2026-10-09 | PULSO | empresario nutella` (carrossel 200) — MONTADA STOPPED ~13h56, LIVE ~19h03 (post agendado pelo user pras 19h)

Caminho **imersão MBV**; `utm_campaign=2026-10-09-PULSO`; `utm_content=https://www.instagram.com/p/DeSiCKikW2d/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-09-PULSO&utm_content=https://www.instagram.com/p/DeSiCKikW2d/`; palavra `PULSO, pulso, Pulso` (busca "pulso" no painel: nenhuma automação, sem colisão); DM "Dono de verdade tem pulso. Quer ver como eu ensino gestão no MBV?" (65 chars, a do kit do 200), botão `>> Quero ver <<` (herdado). Duplicada da GANA do 198 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261009165351_718751.

- O user chamou o post de "NUTELA"; a palavra do CTA do 200 é PULSO (slide 15 e legenda), e foi ela que entrou. Montada parada presa ao post do 198 e sem `utm_content`; timer de shell (caffeinate) às 19h01 achou o post no perfil (`DeSiCKikW2d`, legenda "Juro alto, imposto pesado…", conferida contra o carousel-text). 1º card da grade do easy-builder (capa "O FRACO DA SUA EMPRESA É VOCÊ."); prévia conferida. Conferido recarregando: LIVE, código e utm novos no HTML, o post do 198 não; 1 botão só. Viewport 1204.

## 10/10/2026 — `IG | 2026-10-10 | PLACAR | arquibancada grita` (carrossel 206) — MONTADA STOPPED ~09h20, LIVE ~13h03 (post agendado pelo user pras 13h)

Caminho **RAIO-X** (aula paga, R$97); `utm_campaign=2026-10-10-PLACAR`; `utm_content=https://www.instagram.com/p/DeUdswzEXzO/`; link `https://tatsuoacademy.com/raio-x-empresa-lucrativa/?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-10-PLACAR&utm_content=https://www.instagram.com/p/DeUdswzEXzO/`; palavra PRÓPRIA do post, não a fixa RAIO-X: `PLACAR, placar, Placar` (busca "placar" no painel: nenhuma automação); DM "Você sabe o placar da sua empresa? Pega a aula em que eu mostro como ler ela em poucos minutos." (95 chars; escrita pelo Claude, o kit do 206 não trazia DM), botão `>> Quero a aula <<` (herdado). Duplicada da `IG | 2026-09-29 | RAIO-X | so sobrou a casa` (164, intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261010121538_814137.

- Primeira RAIO-X com palavra temática em vez da fixa: as 12 grafias de RAIO-X foram trocadas pelas 3 de PLACAR. A global `RAIO - X` (raio-x-feed) não colide, porque ninguém comenta "raio-x" neste post por CTA.
- **Horário errado na largada:** o user disse 11h; o alarme das 11h01 e checagens até 11h42 não acharam o post. O user corrigiu pra 13h. O alarme das 13h01 achou o post no perfil (`DeUdswzEXzO`, legenda "Toda crítica tem um preço…", conferida contra o carousel-text). 1º card em "Mostrar Todos" ("há 2 minutos", capa "CRITICAR É O GRITO DE QUEM FICOU NA ARQUIBANCADA."); prévia conferida. Conferido recarregando: LIVE, código e utm novos no HTML, o post do 164 não; 1 botão só. Viewport 1440×778.

## 10/10/2026 — `IG | 2026-10-10 | RUMO | sem direcao` (carrossel 205) — MONTADA STOPPED ~09h20, LIVE ~19h04 (post agendado pelo user pras 19h)

Caminho **imersão MBV**; `utm_campaign=2026-10-10-RUMO`; `utm_content=https://www.instagram.com/p/DeVG2iBkToE/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-10-RUMO&utm_content=https://www.instagram.com/p/DeVG2iBkToE/`; palavra `RUMO, rumo, Rumo` (a busca "rumo" acha só a RESPEITO de 29/08 pelo texto da DM, de post específico; e a LUCRO legada STOPPED; sem colisão); DM "Problema sempre vai ter. Quer ver como eu ensino o dono a decidir o rumo da empresa no MBV?" (91 chars; escrita pelo Claude, o kit do 205 não trazia DM), botão `>> Quero ver <<` (herdado). Duplicada da PULSO do 200 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261010121606_682200.

- Montada parada junto com a PLACAR; alarme às 19h01 achou o post no perfil (`DeVG2iBkToE`, legenda "Existe um conforto escondido no incêndio…", conferida contra o carousel-text). 1º card em "Mostrar Todos" ("há 2 minutos", capa "ESTÁ SEM DIREÇÃO."); a frase 221 das 17h estava em 4º. Prévia conferida. Conferido recarregando: LIVE, código e utm novos no HTML, o post do 200 não; 1 botão só. User ausente; operado sozinho pelo Claude.

## 11/10/2026 — `IG | 2026-10-11 | NORTE | empresario coelho` (carrossel 207, fábula) — MONTADA STOPPED ~10h40, LIVE ~13h04 (post agendado pelo user pras 13h)

Caminho **imersão MBV**; `utm_campaign=2026-10-11-NORTE`; `utm_content=https://www.instagram.com/p/DeXCfrUETfK/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-11-NORTE&utm_content=https://www.instagram.com/p/DeXCfrUETfK/`; palavra `NORTE, norte, Norte` (busca "norte": nenhuma automação); DM "Correr sem destino cansa e não chega. Quer ver como eu ensino o dono a definir o norte no MBV?" (94 chars; escrita pelo Claude, o kit do 207 não trazia DM), botão `>> Quero ver <<` (herdado). Duplicada da RUMO do 205 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261011133837_836332.

- Alarme das 13h01 achou o post no perfil (`DeXCfrUETfK`, legenda "Existe um elogio que todo empresário adora ouvir…", conferida contra o carousel-text). 1º card em "Mostrar Todos" ("há 3 minutos", capa "O Empresário Coelho."); prévia conferida. Conferido recarregando: LIVE, código e utm novos no HTML, o post do 205 não; 1 botão só.
- Gotcha repetido: depois de `navigate`, dois cliques por coordenada em Editar não pegaram; o clique pelo ref do `find` ("Editar") abriu de primeira.

## 11/10/2026 — `IG | 2026-10-11 | GRANDE | fe de empresario` (carrossel 201) — MONTADA STOPPED ~10h40, LIVE ~18h59 (post agendado pelo user pras 18h55; era 17h, mudado no meio da montagem)

Caminho **imersão MBV**; `utm_campaign=2026-10-11-GRANDE`; `utm_content=https://www.instagram.com/p/DeXd3fnEVcw/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-11-GRANDE&utm_content=https://www.instagram.com/p/DeXd3fnEVcw/`; palavra `GRANDE, grande, Grande` (o user chamou o post de "FE"; a palavra do CTA do 201 é GRANDE; busca "grande" acha só a PEQUENO de 10/09 pelo texto da DM, de post específico); DM "Fé de empresário tem número e rotina. Quer ver como eu ensino isso no MBV?" (74 chars; escrita pelo Claude, o kit do 201 não trazia DM), botão `>> Quero ver <<` (herdado). Duplicada da RUMO do 205 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261011133817_706180.

- Alarme das 18h56 achou o post no perfil (`DeXd3fnEVcw`, legenda "Existe uma diferença enorme entre o empresário que acredita…", conferida contra o carousel-text). 1º card em "Mostrar Todos" ("há 3 minutos", capa "MAIS DO QUE O DONO ACREDITA."); prévia conferida. Conferido recarregando: LIVE, código e utm novos no HTML, o post do 205 não; 1 botão só.
- Gotcha: dois cliques no Editar pelo ref do `find` não abriram a edição desta vez; esperar ~5 s e clicar pela coordenada (1268, 34) abriu. Não há um caminho que funcione sempre de primeira: alternar ref e coordenada até a grade de posts aparecer.

## 12/10/2026 — `IG | 2026-10-12 | BASE | terceirizar no escuro` (carrossel 218, série Erros do Hélio nº 6) — MONTADA STOPPED ~12h30, LIVE ~13h07 (post ~13h04)

Caminho **imersão MBV**; `utm_campaign=2026-10-12-BASE`; `utm_content=https://www.instagram.com/p/DeZnwLeEUX6/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-12-BASE&utm_content=https://www.instagram.com/p/DeZnwLeEUX6/`; palavra `BASE, base, Base` (busca "base": nenhuma automação); DM "Ninguém cobra o que não entende. Quer ver como eu ensino o dono a ter base de gestão no MBV?" (92 chars; escrita pelo Claude, o kit do 218 não trazia DM), botão `>> Quero ver <<` (herdado). Duplicada da GRANDE do 201 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261012152716_063576.

- Alarme das 13h01 e checagem das 13h04 não acharam o post; o "já postei" do user veio logo depois e o post já estava no perfil (`DeZnwLeEUX6`, legenda "Já fui passado pra trás dentro da minha própria empresa…"). 1º card em "Mostrar Todos" ("há 1 minuto", capa "E A CULPA FOI MINHA."); prévia conferida. Conferido recarregando: LIVE, código e utm novos no HTML, o post do 201 não; 1 botão só. Viewport 1279×684.
- **Gotcha novo:** clicar no ⋮ da linha por coordenada antes de o hover renderizar o botão ABRE a automação (aqui, a GRANDE LIVE). Nada foi alterado; voltar pra lista e clicar de novo com o ⋮ visível. Rotina: hover na linha → screenshot → clicar no ⋮ que apareceu.

## 12/10/2026 — `IG | 2026-10-12 | CLAREZA | seis verdades` (carrossel 220) — MONTADA STOPPED, publicação marcada 15h

Caminho **imersão MBV**; `utm_campaign=2026-10-12-CLAREZA`; palavra `CLAREZA, clareza, Clareza` (a CLAREZA de 06/10 é por post específico, sem conflito); DM "Eu levei 38 anos pra aprender isso. Quer ver como eu ensino a ter clareza da sua empresa no MBV?" (95 chars; o campo comeu o "e" de "eu", corrigido e conferido por JS depois do recarregar), botão `>> Quero ver <<`. Duplicada da `IG | 2026-10-06 | CLAREZA | o preco de ser empresario` (LIVE, 24 exec.; intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261012161406_801461. Falta amarrar ao post + utm_content + ativar depois das 15h.
- **LIVE às 15h06 (timer da sessão, sem o user presente):** post `DeZ1B0Akctx` (2º card da grade do easy-builder; o 1º era o post de 06/10 e o 3º o "E a culpa foi minha", que cheguei a selecionar por engano e troquei antes de salvar; preview conferido: capa "6 VERDADES" + legenda "Quando eu comecei…"), `utm_content=https://www.instagram.com/p/DeZ1B0Akctx/`, Atualização, Ativar; conferido recarregando. Navegador Chrome da Tatsuo já em uso na sessão. Primeiro timer de ativação que funcionou porque a sessão já tinha o Chrome escolhido (a regra de 31/08 refutava sessão AGENDADA nova, não timer dentro da sessão viva).

## 12/10/2026 — `IG | 2026-10-12 | DEZEMBRO | 13o do dono` (carrossel 226) — MONTADA STOPPED ~13h20, LIVE só ~19h50 (post do user às 19h)

Caminho **imersão MBV**; `utm_campaign=2026-10-12-DEZEMBRO`; `utm_content=https://www.instagram.com/p/DeaQc4FEX7s/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-12-DEZEMBRO&utm_content=https://www.instagram.com/p/DeaQc4FEX7s/`; palavra `DEZEMBRO, dezembro, Dezembro` (busca "dezembro": nenhuma automação); DM "O 13º do dono é o dividendo. Quer ver como eu ensino a empresa a pagar quem arriscou no MBV?" (90 chars), botão `>> Quero ver <<` (herdado). Duplicada da BASE do 218 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261012161514_927581.

- **Atraso de ~50 min, erro do Claude:** o alarme da sessão (CronCreate one-shot `1 19 12 10 *`) só foi entregue às 19h49, 48 min atrasado, logo depois de a ativação já ter sido feita à mão; às 19h01 nada chegou à sessão; o atraso só apareceu quando o user perguntou às 19h46. O Chrome da Tatsuo estava aberto (outras conversas ativaram as delas). Na primeira tentativa, às 19h46, a lista de navegadores mostrou só o `46b005d2` (Manychat deslogado, Instagram de outra conta) e eu li isso, errado, como "Chrome da Tatsuo desconectado"; quando o user reabriu, o `ee5937df` voltou com o nome "Tatsuo Academy". Comentários de ~19h00 a ~19h50 ficaram sem DM (o user mandou manualmente).
- Ativação: post em 1º em "Mostrar Todos" ("há 48 minutos", capa "MENOS PRA VOCÊ."), prévia com a legenda "Ninguém na sua empresa precisa pedir o 13º…". Conferido recarregando: LIVE, `DeaQc4FEX7s` e utm no HTML, o post do 218 não; 1 botão só.
- **Lição:** alarme de ativação conferido ANTES da hora (CronList perto das 18h50, ou timer de shell em segundo plano, que avisa ao terminar, como no PULSO de 09/10) e um "ping" de presença no horário; navegador "sumido" da lista com o user dizendo que está aberto = `switch_browser`, nunca concluir que caiu.

## 13/10 — primeira automação de LIVE (Q&A do Hélio, 12h-12h30), palavra RAIO-X

Duas automações, as duas LIVE às ~11h00, link `https://tatsuoacademy.com/raio-x-empresa-lucrativa/`, DM "Quer descobrir onde o lucro da sua empresa está vazando? O raio-x da empresa lucrativa é aqui." (94 chars), botão `>> Quero o raio-x <<`:

1. **`LIVE | 2026-10-13 | RAIO-X | comentario na live`** — Flow Builder (content20261013135501_488508). Não existe Quick Automation pra live: `Nova Automação` → `Começar Do Zero` → `Começar do zero` → `+ Novo Gatilho` → **"Comentários ao vivo"** ("O usuário deixa um comentário em sua transmissão ao vivo"). Gatilho: condição trocada de "mensagem é" pra **"a mensagem contém"**; palavras `raio-x, raiox, raio x` (aqui as palavras-chave NÃO diferenciam maiúsculas, então 3 bastam; chips um a um com Enter). Passo: Instagram → Enviar Mensagem **"como Resposta Privada"**, texto + `+ Botão Adicionar` → título → `Abrir Site` → URL; UTM `live-2026-10-13`. Nome pelo lápis no topo; `Publicar` vira LIVE. Pegadinha: o botão `{}` do modal do botão abre o seletor de variáveis — Escape fecha e o botão já fica salvo (não precisa de Concluído).
2. **`LIVE | 2026-10-13 | RAIO-X | DM palavra-chave`** — Quick Automation "Palavra-chave de DM" (content20250424093659_147100), plano B: quem MANDAR a palavra na DM recebe o link. **Teto de 12 palavras-chave** no gatilho de DM (15 travou o Ativar sem erro visível; o rascunho fica salvo e o easy-builder oferece "Deseja prosseguir ou começar de novo?"). As 12: `RAIO-X, raio-x, Raio-X, Raio-x, raio-X, RAIOX, raiox, Raiox, RAIO X, raio x, Raio X, Raio x`. UTM `live-2026-10-13-dm`.

Modelos "Comentário em tempo real" do catálogo (Envie ofertas nas DMs durante Lives / Converta na Live / Gamifique) são Flow Builder com fluxo de cupom; o "Converta na Live" na prática é gatilho de DM ("Mande uma DM com SIM"). Não usados. A global `RAIO - X` de comentário em post segue LIVE e não conflita (gatilhos diferentes). Primeira vez com gatilho de live: sem teste prévio possível; conferir Envios/Cliques no ritual de 14/10.

**Decisão do user (13/10, 11h10):** as duas automações de live ficam LIVE permanentemente, valem pra qualquer live futura (o gatilho "Comentários ao vivo" não amarra em transmissão específica). **A página do RAIO-X não tem trackeamento**, então o UTM do link não serve pra nada ali — não trocar UTM entre lives, não vale o trabalho.

## 13/10/2026 — `IG | 2026-10-13 | UNIR | liderar e unir` (carrossel 231, repost com arte nova do "Liderar não é mandar. É unir." de 15/07) — LIVE ~14h20, logo depois do "já postei"

Caminho **imersão MBV**; `utm_campaign=2026-10-13-UNIR`; `utm_content=https://www.instagram.com/p/DecUoY1EY3c/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-13-UNIR&utm_content=https://www.instagram.com/p/DecUoY1EY3c/`; palavra `UNIR, unir, Unir` (busca "unir": nenhuma automação); DM "Time que puxa pro mesmo lado não nasce pronto. Quer ver como eu ensino a unir o seu no MBV?" (91 chars), botão `>> Quero ver <<` (herdado). Duplicada da DEZEMBRO do 226 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261013171715_236823.

- Post `DecUoY1EY3c` lido no perfil (legenda "O que é liderar pessoas, de verdade?…"); 1º card da grade do easy-builder; prévia conferida. Já tinha 2 comentários antes da ativação (podem ter ficado sem DM). Conferido recarregando: LIVE, código e utm novos no HTML, o post do 226 não; 1 botão só. Link conferido por igualdade em JS (157 chars).
- Gotchas: a URL `/fb2015128/automations` dá 404; a lista é `/fb2015128/cms?path=/&field=modified&order=desc`. Navegar pra uma automação e logo em seguida pra outra página deixa um redirect atrasado que reabre a automação anterior (nada alterado). O campo da DM comeu o espaço de "Quer ver"; corrigido com `cmd+Up` + `Right` × 51.

## 15/10/2026 — `IG | 2026-10-15 | COMANDO | ultimo a saber` (carrossel 240) — MONTADA STOPPED ~18h40, LIVE ~19h03 (post agendado pelo user pras 19h)

Caminho **imersão MBV**; `utm_campaign=2026-10-15-COMANDO`; `utm_content=https://www.instagram.com/p/Deh-2filKKW/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-15-COMANDO&utm_content=https://www.instagram.com/p/Deh-2filKKW/`; palavra `COMANDO, comando, Comando`; DM "Dono que não olha o número é o último a saber. Quer ver como eu ensino gestão pelo número no MBV?" (97 chars; escrita pelo Claude), botão `>> Quero ver <<` (herdado). Duplicada da TREINO do 238 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261015202904_968600. Primeira automação montada da máquina do João (Windows; Chrome "Browser 3").

- **Colisão (falha minha na escolha da palavra):** a busca "comando" devolve a global `Comando!! MBV` (LIVE, qualquer publicação, 4.898 exec.; 4.889 em 18/08) e a `comando repost` (LIVE, específica). A palavra foi conferida só no `registro-posts.csv` e não no painel; o post já estava agendado com COMANDO no slide, então não dava mais pra trocar (o 132 e o 143 trocaram a palavra exatamente por isso). Proposto ao user pausar a global durante o post; decisão pendente no momento da ativação. Regra prática: conferir a palavra no painel do Manychat ANTES do CHECKPOINT 1, não só no registro.
- O Manychat pediu login nesta máquina (sessão nova); o user entrou e a montagem seguiu.
- Timer de shell (Git Bash, sem caffeinate; keep-awake do app) às 19h01; o post já estava no perfil (`Deh-2filKKW`, legenda "Tem dono que acha que acompanhar é desconfiar…", conferida contra o carousel-text). 1º card em "Mostrar Todos" ("há 2 minutos", capa "E FICA SABENDO DO ERRO PELO CLIENTE."); prévia conferida. Conferido recarregando: LIVE, código e utm novos no HTML, nada do TREINO; 1 botão só.
- Dia com vários carrosséis no perfil (o sapo, "Todo dono já ouviu essa promessa…", "Existe uma conta" às 9h50 e o 240 às 19h).
- **Global pausada (decisão do user, 15/10 ~19h08):** `Comando!! MBV` (qualquer publicação, palavras `comando, Comando`; painel: 4.639 envios, 2.692 cliques, 58%) passou de LIVE pra STOPPED, pra todo COMANDO do 240 cair na específica com UTM. **Religar em 22/10 (D+7 do 240)**, se o user mantiver. URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20250905172616_660638. A `comando repost` (específica de post antigo) ficou LIVE, sem efeito no 240.

## 16/10/2026 — `IG | 2026-10-17 | FOLEGO | vendeu mais foi no banco` (carrossel 244) — MONTADA STOPPED ~15h15 (post marcado pelo user pra 17/10 às 13h; timer às 13h01)

Caminho **imersão MBV**; `utm_campaign=2026-10-17-FOLEGO` (data da publicação); `utm_content` entra na hora de amarrar; palavras `FOLEGO, folego, Folego, FÔLEGO, fôlego, Fôlego` (busca "folego" e "fôlego" no painel em 16/10: nenhuma automação, sem colisão); DM "Crescer sem olhar o prazo é cavar o buraco mais rápido. Quer ver como eu ensino o dono a crescer com caixa no MBV?" (escrita pelo Claude), botão `>> Quero ver <<` (herdado). Duplicada da COMANDO do 240 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261016181310_270770.

- Montada parada, presa ao post do 240 e sem `utm_content`. Conferido recarregando: STOPPED, campaign novo no HTML, nada do COMANDO, 1 botão só.
- Leitura de passagem: a COMANDO (240) estava com 0 execuções em ~23 h no ar, e o post com 2 comentários no total.

## 16/10/2026 — `IG | 2026-10-17 | DELEGAR | so anda com voce` (carrossel 245) — MONTADA STOPPED ~16h05 (post marcado pelo user pra 17/10 às 17h; timer às 17h01)

Caminho **imersão MBV**; `utm_campaign=2026-10-17-DELEGAR` (data da publicação); `utm_content` entra na hora de amarrar; palavras `DELEGAR, delegar, Delegar` (busca "delegar" no painel em 16/10: nenhuma automação, sem colisão); DM "Delegar sem largar a empresa na mão dos outros se aprende. Quer ver como eu ensino isso no MBV?" (95 chars; escrita pelo Claude no kit da etiqueta), botão `>> Quero ver <<` (herdado). Duplicada da FOLEGO do 244 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261016185532_196148.

- Montada parada, presa ao post do 240 (herança da FOLEGO) e sem `utm_content`. Conferido recarregando: STOPPED, campaign novo no HTML, DM inteira (o campo não comeu caractere), nada do FOLEGO, 1 botão só. Link conferido por JS com 107 caracteres (o tamanho exato).
- Timer de shell com DATA (`until [ "$(date +%Y%m%d%H%M)" -ge 202610171701 ]`), porque o post é no dia seguinte: o `until` só com `%H%M` da skill dispararia hoje às 17h01. Keep-awake do app pedido (session_idle). No mesmo dia 17/10 tem também a FOLEGO (244) às 13h, com timer em outra conversa.

## 17/10/2026 — `IG | 2026-10-18 | ENTREGA | creche de adulto` (carrossel 246) — MONTADA STOPPED ~13h20 (post marcado pelo user pra 18/10 às 13h; timer às 13h01)

Caminho **imersão MBV**; `utm_campaign=2026-10-18-ENTREGA` (data da publicação); `utm_content` entra na hora de amarrar; palavras `ENTREGA, entrega, Entrega`; DM "Time que entrega não nasce pronto: se acompanha. Quer ver como eu ensino gestão no MBV?" (escrita pelo Claude no kit da etiqueta), botão `>> Quero ver <<` (herdado). Duplicada da DELEGAR do 245 (intocada, STOPPED até o timer de hoje às 17h01). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261017161029_941249.

- **Colisão (correção do registro de 16/10):** em 16/10 a busca "entrega" foi lida antes de carregar inteira e o kit do 246 disse "nenhuma automação usa a palavra". Em 17/10 a busca completa mostrou a `IG | 2026-10-03 | ENTREGA | folha paga duas vezes` (180), LIVE, mas de **publicação específica**: não dispara no 246, e a palavra não precisa ser inédita (o `utm_campaign` é que identifica o post). Lição: esperar a lista carregar e conferir na tela, não só no texto da página.
- Montada parada, presa ao post do 240 (herança) e sem `utm_content`. Conferido recarregando: STOPPED, campaign novo no HTML, DM inteira, nada da DELEGAR, 1 botão só; link com 107 caracteres.
- Timer de shell com data (`-ge 202610181301`) e keep-awake do app. O timer do 245 (17/10 17h01) segue vivo na mesma conversa.
- O 246 sai um dia depois do 245 (sugestão era 3 dias, pela vizinhança do tema: acompanhamento). Decisão do user.
- **17/10:** timer às 13h01; buscas às 13h01, 13h04, 13h07 e 13h12 sem o post; às 13h22 o post estava no perfil (`DemhpcHETLu`, "há 1 minuto", capa "E NUNCA DEVEU TANTO PRO BANCO.", legenda "Faturamento recorde não paga boleto…"). O agendamento das 13h saiu ~13h21. 1º card em "Mostrar todos" ("há 5 minutos"). `utm_content=https://www.instagram.com/p/DemhpcHETLu/`. **LIVE ~13h27**, uns 6 minutos depois de o post subir (passou dos 5 por causa de dois travamentos do renderer). Conferido recarregando: LIVE, código e utm novos no HTML, o post do 240 não; 1 botão só.
- **Gotcha novo (Windows/Chrome desta máquina):** o editor do Manychat travou o renderer pros screenshots duas vezes (aba fechada e reaberta). Saída que funcionou: operar só por `find` + refs e conferir por JS, sem screenshot. E depois do clique em "Atualização" a automação já apareceu com "Interromper" (LIVE) sem um clique separado em "Ativar" — conferir o estado por JS antes de clicar de novo, senão o 2º clique interrompe.

## 17/10/2026 — `IG | 2026-10-17 | DELEGAR | so anda com voce` (carrossel 245) — LIVE ~17h07 (post às 16h56, marcado pras 17h)

Post `Dem6MhaFHjd` (legenda "Tem dono que se orgulha de não conseguir sair da empresa…", conferida contra o carousel-text), capa no estilo Notas ("Você tem 40 funcionários na folha / e não tira 10 dias de férias."). No editor ele já vinha como 1º card da grade, e a prévia mostrava a capa e a legenda certas; clicado de novo pra garantir. Link completo: `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-17-DELEGAR&utm_content=https://www.instagram.com/p/Dem6MhaFHjd/` (160 caracteres, conferido por JS). Conferido recarregando: LIVE, código novo no HTML, nada do 240 (`Deh-2filKKW`), campaign novo, DM inteira, 1 botão só.

- **Atraso de ~11 min:** o post subiu às 16h56 (horário do `<time>` da página: 19:56 UTC), 4 min antes do combinado, e o timer estava em 17h01. Nenhum comentário no post na hora da ativação, então nenhum lead perdido. Lição: com post programado, armar o timer uns minutos ANTES do horário e, se o post ainda não estiver no perfil, rechecar a cada 2 min.
- O timer de shell com data (`-ge 202610171701`) aguentou a noite inteira (armado 16/10 15h59), com keep-awake do app.
- **18/10, 12h56-13h45: o 246 não saiu no horário marcado.** Timers dispararam às 12h56 e 13h01; o perfil foi checado às 13h05, 13h08, 13h11, 13h17, 13h29 e 13h45, e o post não apareceu. No slot das 13h saiu outro post, a fábula "O Empresário Toupeira" (`DepD_S1kY6v`, 13h00, legenda "Tem dono que sabe tudo da própria empresa…"), conferido e descartado. A ENTREGA ficou STOPPED, sem amarrar; o vigia parou e espera o novo horário do user.
- **18/10 — LIVE às ~18h19 (post às 17h00, não às 13h).** Post `Depfb_WER0E` (legenda "Todo dono sonha com o dia em que vai contratar gente que não precisa ser acompanhada…", capa da mamadeira no estilo sem rosto); 2º card da grade, prévia conferida. Link completo `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-18-ENTREGA&utm_content=https://www.instagram.com/p/Depfb_WER0E/` (160 caracteres). Conferido recarregando: LIVE, código novo, nada do 245/240, campaign novo, DM inteira, 1 botão só.
- **Atraso de ~1h19:** o user mudou o horário (13h → 17h) sem avisar a conversa e só mandou o "já postei" às ~18h15. Na ativação, 2 comentários visíveis no post (aplausos, nenhum com ENTREGA; o contador marcava 3). Bloco de DM + link entregue ao user pra mandar à mão a quem comentou ENTREGA antes das 18h19.
- O painel mostrava "Envios 1, Cliques 1" na automação ainda STOPPED, antes de amarrar: origem desconhecida (talvez teste do próprio painel). Anotado pra conferir na leitura do ritual.

## 20/10/2026 — `IG | 2026-10-20 | MAQUINA | frankenstein` (carrossel J269) — LIVE ~12h52 (post ~12h28, agendado pelo user pras 12h30)

Caminho **imersão MBV**; `utm_campaign=2026-10-20-MAQUINA`; `utm_content=https://www.instagram.com/p/DeuJ6GuEdBT/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-20-MAQUINA&utm_content=https://www.instagram.com/p/DeuJ6GuEdBT/`; palavras `MAQUINA, maquina, Maquina, MÁQUINA, máquina, Máquina`; colisão: busca "maquina" sem resultado, "máquina" devolve a global `Podcast EP 2` (STOPPED, palavras Máquina/maquina) e específicas que só batem no texto da DM: sem colisão viva. DM "Monstro costurado assusta o cliente. Quer ver como eu ensino gestão de pessoas e cultura no MBV?" (escrita pelo Claude). Botão `>> Quero ver <<`. Duplicada da ENTREGA do 246 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261020142002_386201.

- **Atraso de ~24 min (falha de operação):** o pedido chegou às 11h18 com tempo de sobra; a conexão do Claude in Chrome caiu no meio da duplicação e a sessão exigiu escolher o navegador de novo (pergunta ao user), e só voltou às 12h49, com o post já no ar. Ativado na sequência. Um comentário `maquina` de 12h32 (antes da ativação) ficou sem DM: mensagem e link entregues ao user pra mandar à mão.
- O ⋮ da lista abriu a automação ENTREGA (LIVE) na primeira tentativa (pegadinha conhecida); nada foi alterado.
- Post achado: `DeuJ6GuEdBT`, legenda "Quase todo mundo chama o monstro de Frankenstein…", 1º card em "Mostrar todos" ("há 22 minutos"). Conferido recarregando: LIVE, código e utm novos no HTML, nada do 246; 1 botão só.

## 20/10/2026 — `IG | 2026-10-20 | LUCRO | margem repost` (carrossel J273, repost de DVJitIEkdyq de 24/02) — MONTADA STOPPED ~17h31, LIVE ~17h45 (post ~17h43)

Caminho **imersão MBV**; `utm_campaign=2026-10-20-LUCRO`; `utm_content=https://www.instagram.com/p/Deut-eZFKI1/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-20-LUCRO&utm_content=https://www.instagram.com/p/Deut-eZFKI1/`; palavras `LUCRO, lucro, Lucro`; colisão: a global antiga `LUCRO` (multi-trigger) está STOPPED; `IG | 2026-08-27 | LUCRO | casas bahia noticia` é específica (não dispara aqui). DM "Margem é o que define quem manda na sua empresa. Quer ver como eu ensino o dono a achar onde o lucro vaza no MBV?" (escrita pelo Claude). Duplicada da MAQUINA do J269 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261020202908_909365.

- O user postou antes do horário marcado (17h50) e avisou ("já estou postando"); o timer das 17h51 foi parado. Post achado: `Deut-eZFKI1`, legenda "Vou te dar um ângulo que quase nenhum dono encara…", 1º card em "Mostrar todos" ("há 1 minuto"), 0 comentários na hora. Conferido recarregando: LIVE, código e utm novos, nada da MAQUINA; 1 botão só.
- Operado só por `find` + refs e JS (o screenshot do Chrome desta máquina trava no editor).

## 20/10/2026 — `IG | 2026-10-20 | PERTO | perto do time` (carrossel J274) — MONTADA STOPPED ~17h39 (post marcado pras 20h; timer às 20h01)

Caminho **imersão MBV**; `utm_campaign=2026-10-20-PERTO`; palavras `PERTO, perto, Perto` (busca "perto": nenhuma automação); DM "O grande pode pagar mais que você, mas não pode estar mais perto. Quer ver como eu ensino liderança no MBV?" (escrita pelo Claude). Duplicada da MAQUINA do J269 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261020203718_762946. Conferido recarregando: STOPPED, campaign novo, nada da MAQUINA, 1 botão só.
- **20/10 ~20h18, PERTO amarrada ao post certo.** O post saiu ~19h08 (`Deu3snbETP-`), 52 min antes do horário marcado, sem aviso. Às 20h16 a automação já estava LIVE, mas ainda presa ao post do J269 (`DeuJ6GuEdBT`, herdado da cópia): alguém a ativou antes de amarrar (não foi esta sessão; o timer das 20h01 só foi atendido às 20h15). Corrigido: post `Deu3snbETP-` escolhido na grade (1º card, "há 1 hora"), `utm_content=https://www.instagram.com/p/Deu3snbETP-/`, Atualização. Conferido recarregando: LIVE, post novo no HTML, o do J269 não, campaign `2026-10-20-PERTO`, 1 botão só. Um comentário "Perto" de ~19h38 ficou sem DM; mensagem e link entregues ao user pra mandar à mão.
- **Lição:** cópia montada parada continua presa ao post do modelo; se for ativada sem trocar o post, ela dispara no post antigo. Ativar só depois de amarrar.

## 21/10/2026 — `IG | 2026-10-21 | PRONTO | fim da 6x1` (carrossel J255, formato Notas) — MONTADA STOPPED ~09h35, LIVE ~12h33 (post ~12h28, agendado pelo user pras 12h30)

Caminho **imersão MBV**; `utm_campaign=2026-10-21-PRONTO`; `utm_content=https://www.instagram.com/p/Dewu2CfEQgd/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-21-PRONTO&utm_content=https://www.instagram.com/p/Dewu2CfEQgd/`; palavras `PRONTO, pronto, Pronto` (busca "pronto" em 19 e 21/10: nenhuma automação com a palavra); DM "A 6x1 acabou. Quer ver como eu ensino o dono a fazer a conta fechar com 40 horas no MBV?" (escrita pelo Claude). Duplicada da PERTO do J274 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261021122819_170814.

- Timer às 12h31; o post estava no perfil (`Dewu2CfEQgd`, legenda "O Senado aprovou o fim da escala 6x1…", 0 comentários). 1º card em "Mostrar todos" ("há 3 minutos"). Amarrado ANTES de ativar (lição da PERTO). Conferido recarregando: LIVE, post novo no HTML, o da PERTO não, campaign novo, 1 botão só.

## 22/10/2026 — `LIVE | 2026-10-21 | DIAGNOSTICO | comentario na live` (live do Hélio com a frase na parede "quer um diagnóstico grátis da sua empresa? comente diagnóstico") — já estava LIVE, conferida às ~10h30, nada alterado

- Criada fora desta máquina (~00h17 de 22/10, content20261022001732_197708, Flow Builder "Live Comments #1 copy"); não tinha registro aqui.
- Gatilho "Comentários ao vivo", **a mensagem contém** `diagnóstico, diagnostico` (sem diferença de maiúscula).
- DM como Resposta Privada: "Recebi o seu comentário. Preencha aqui: se a sua empresa for selecionada, a minha equipe fala com você." Botão `Quero o diagnóstico` → `https://rtc.tatsuoacademy.com/diagnostico-live/?utm_source=instagram&utm_medium=manychat&utm_campaign=live-diagnostico&ig={{Usuário}}` (o link pedido pelo João, já com UTM e o @ do lead).
- Conferido no editor, saída sem publicar; LIVE e 0 envios antes da live. A `LIVE | 2026-10-13 | RAIO-X | comentario na live` segue ligada e não conflita (palavra diferente).

## 22/10/2026 — `IG | 2026-10-22 | SOBRAL | parabellum cade o dinheiro` (carrossel J282, dia da palestra do Hélio no Parabellum) — MONTADA STOPPED ~18h40, LIVE ~18h51 (post ~18h49)

Caminho **imersão MBV**; `utm_campaign=2026-10-22-SOBRAL`; `utm_content=https://www.instagram.com/p/Dez_NsHkdm_/`; link `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=2026-10-22-SOBRAL&utm_content=https://www.instagram.com/p/Dez_NsHkdm_/`; palavras `SOBRAL, sobral, Sobral` (busca "SOBRAL": nenhuma automação); DM "Descobrir onde está o dinheiro da sua empresa é o que eu ensino no MBV. Quer ver como?" (88 caracteres, escrita pelo Claude; casa com o slide 11 "que eu te mostro, no direct, como fazer isso"); botão `>> Quero ver <<`. Duplicada da PRONTO do J255 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261022213900_458404.

- Montada parada enquanto o João ainda corrigia as imagens; o "postado" do João veio ~18h50. Post achado no perfil (`Dez_NsHkdm_`, legenda "Tem uma confusão que eu vejo em empresa de todo tamanho…"), 1º card em "Mostrar todos" ("há 1 minuto", capa "CADÊ O DINHEIRO?"). Link completado com o `utm_content` antes de ativar. Conferido recarregando: LIVE, post novo no HTML, o da PRONTO não, campaign novo, DM nova, 1 botão só, palavras SOBRAL na tela.
- Máquina Windows: sem caffeinate (não houve timer; ativação na hora).

## 26/10/2026 — `IG | 2026-10-26 | PATRIMONIO | pro-labore de gerente` (carrossel J301, formato Notas) — MONTADA STOPPED ~13h05 (publicação a definir)

Caminho **imersão MBV**; `utm_campaign=2026-10-26-PATRIMONIO` (trocar pela data da publicação se o post sair em outro dia, enquanto tiver 0 cliques); palavras `PATRIMONIO, patrimonio, Patrimonio, PATRIMÔNIO, patrimônio, Patrimônio` (busca "patrimonio" em 26/10: nenhuma automação); DM "Pró-labore paga o trabalho. Dividendo paga o risco. Quer ver como eu ensino o dono a receber os dois no MBV?" (escrita pelo Claude). Duplicada da TUBARAO de 25/10 (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261026155812_208827. Conferido recarregando: STOPPED, campaign novo, nada da TUBARAO, 1 botão só. Presa ao post da TUBARAO até ser amarrada: não ativar antes de trocar o post.
- **26/10 ~13h48, LIVE.** Post `De9qhAzEZHO` (legenda "Tem uma conta que quase nenhum dono faz…"), publicado ~13h01; o "já postei" chegou ~13h45. 1º card em "Mostrar todos" ("há 45 minutos"). `utm_content=https://www.instagram.com/p/De9qhAzEZHO/`. Amarrado antes de ativar. Conferido recarregando: LIVE, post novo no HTML, nada da TUBARAO, campaign `2026-10-26-PATRIMONIO`, 1 botão só. Um comentário "Patrimônio" de ~13h42 (antes da ativação) ficou sem DM: mensagem e link entregues ao user.

## 27/10/2026 — `IG | 2026-10-27 | OPORTUNIDADE | falta cliente nao tecnica` (carrossel J316, formato Notas) — MONTADA STOPPED à tarde, pra 19h

Caminho **imersão MBV**; `utm_campaign=2026-10-27-OPORTUNIDADE`; palavras `OPORTUNIDADE, oportunidade, Oportunidade` (nenhuma automação com a palavra no painel); DM "Técnica nenhuma salva quem não tem cliente na frente. Quer ver como eu ensino o dono a gerar oportunidade no MBV?" (escrita pelo Claude). Duplicada da PATRIMONIO (intocada). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261027193611_214555. Substitui a LIDER (J309, descartado e apagado).
- **27/10 ~20h23, LIVE.** Post `DfBBXx3kd7h` (legenda "Quase todo dono, quando a venda cai…"), publicado ~20h20 (atrasou da previsão de 19h; às 19h43 e 20h05 ainda não estava no perfil). O João pediu "ativa a automação" e o post era o 1º card em "Mostrar todos" ("há 2 minutos"). Amarrado antes de ativar. `utm_content=https://www.instagram.com/p/DfBBXx3kd7h/` acrescentado no botão logo depois. Status LIVE conferido.

## 28/10/2026 — `IG | 2026-10-28 | RITMO | descobre no dia 30` (carrossel J310, formato Notas) — MONTADA STOPPED ~15h20, pras 17h

Caminho **imersão MBV**; `utm_campaign=2026-10-28-RITMO`; palavras `RITMO, ritmo, Ritmo` (busca "ritmo" em 28/10: só a RITUAL de 03/09, sem colisão); DM "Quem só olha o resultado descobre o buraco no dia 30. Quer ver como eu ensino o dono a acompanhar o time todo dia no MBV?" (escrita pelo Claude). Duplicada da OPORTUNIDADE (intocada, LIVE). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261028181535_573103. Conferido recarregando: STOPPED, palavras e DM novas, campaign novo, nada da OPORTUNIDADE, 1 botão só. Presa ao post do J316 até ser amarrada: não ativar antes de trocar o post.
- **28/10 ~17h03, LIVE.** Post `DfDPZgBFIaz` (legenda "Tem dono que só descobre como foi o mês…"), publicado às 17h; 1º card em "Mostrar todos" ("há 1 minuto") no timer das 17h01. Amarrado antes de ativar. `utm_content=https://www.instagram.com/p/DfDPZgBFIaz/` acrescentado no botão logo depois. Conferido recarregando: LIVE, post novo no HTML, campaign `2026-10-28-RITMO`, nada da OPORTUNIDADE.

## 29/10/2026 — `IG | 2026-10-29 | TROFEU | comissao nao e reconhecimento` (carrossel J312, formato Notas) — montada e ativada na hora

Caminho **imersão MBV**; `utm_campaign=2026-10-29-TROFEU`; palavras `TROFEU, trofeu, Trofeu, TROFÉU, troféu, Troféu` (busca "trofeu" em 29/10: nenhuma automação); DM "Comissão paga o resultado. Reconhecimento faz o time querer repetir. Quer ver como eu ensino o dono a reconhecer quem bate meta no MBV?" (escrita pelo Claude). Duplicada da RITMO (intocada, LIVE). URL: https://app.manychat.com/fb2015128/cms/easy-builder/content20261029161725_542556.
- **29/10 ~13h22, LIVE.** O João avisou "vou postar agora" ~13h15; montada STOPPED, salva, amarrada ao post `DfFar9qEWCl` (legenda "Comissão em dia é obrigação, não motivação…", 1º card em "Mostrar todos") e ativada. `utm_content=https://www.instagram.com/p/DfFar9qEWCl/` acrescentado no botão logo depois. Conferido recarregando: LIVE, post novo no HTML, campaign `2026-10-29-TROFEU`, nada da RITMO.
