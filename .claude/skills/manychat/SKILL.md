---
name: manychat
description: Monta e ativa a automação do Manychat de um carrossel do Hélio (CTA "Comenta PALAVRA"), amarrada ao post específico, com DM curta, botão e link com UTM, e LIVE em até 5 minutos da publicação. Três pedidos do user - "vou postar agora o X, monta o manychat" (monta e ativa), "programei o X pra HH:MM, monta e deixa o timer" (monta parada e arma o timer de shell), "já postei" / "postei, pode ativar" (amarra e ativa na hora). Use na conversa do próprio carrossel ou numa conversa dedicada, nunca na do /ritual. Não serve pra frase, post da apostila nem reel.
---

# /manychat: automação do post específico

## Regras que não mudam

- **LIVE em até 5 minutos da publicação.** 20 minutos já foi rejeitado por perder lead. Comentário feito antes da ativação não recebe DM (o Manychat não é retroativo).
- **Toda automação é de publicação específica.** Nunca "qualquer publicação" e nunca o gatilho "próxima publicação" (em 30 e 31/08 ele grudou em post errado duas vezes).
- **O pedido do user já é a autorização**, inclusive pra ativar sozinho pelo timer. Palavras dele: "pode editar e ativar o Manychat, inclusive pelo timer... Deu de autorização" (04/10) e "eu quero que você gerencie sozinho" (10/10). Não pedir de novo. Só chamar o user quando travar: navegador, login, Manychat fora do ar, post que não aparece.
- **Onde rodar:** na conversa do próprio carrossel ou numa conversa dedicada ao Manychat. Nunca na do `/ritual`, que só lê o painel.
- **O que não leva automação específica:** frase, post da apostila (perfil da Tatsuo Academy) e reel. Reel fica só com a automação global do MBV. Se o pedido for de um desses, dizer isso e parar.

## Passo 1: achar o post e o kit

1. Rodar `date`. A data do nome e do UTM é a do dia da publicação.
2. **O user chama o post pelo apelido, não pela palavra.** Casos reais: NUTELA era o 200 com palavra PULSO; FE era o 201 com GRANDE; "carrossel base" era o 218 com BASE; "sonho 2" era o 184. Procurar a pasta em `conteudo/carrosseis/[N]_*/`. O apelido também pode ser o nome da pasta de entrega em `~/Desktop/carrosseis claude/` (o user move o que já postou pra `POSTADOS/` e às vezes renomeia).
3. **A palavra real é a do slide de CTA** ("Comenta PALAVRA") no `carousel-text.md`, conferida na legenda. É ela que entra, nunca o apelido.
4. **O kit** fica na linha "Manychat (quando publicar)" do `carousel-text.md` (caminho, grafias, link, DM, botão). Nos carrosséis antigos, em `manychat/kit-dm.md`. Nem todo carrossel tem (201, 205, 207 e 218 não tinham). Sem DM no kit: escrever a partir do post (regras no passo 3) e avisar no relato: "a DM é minha; se quiser outro texto, me fala antes das HH".
5. **O caminho** (imersão MBV ou RAIO-X) é o que o slide de CTA e a legenda pedem.

## Passo 2: navegador (Claude in Chrome)

Carregar as ferramentas numa chamada só:
`ToolSearch select:mcp__claude-in-chrome__tabs_context_mcp,mcp__claude-in-chrome__navigate,mcp__claude-in-chrome__computer,mcp__claude-in-chrome__read_page,mcp__claude-in-chrome__tabs_create_mcp,mcp__claude-in-chrome__tabs_close_mcp,mcp__claude-in-chrome__find,mcp__claude-in-chrome__form_input,mcp__claude-in-chrome__javascript_tool,mcp__claude-in-chrome__get_page_text,mcp__claude-in-chrome__list_connected_browsers,mcp__claude-in-chrome__select_browser,mcp__claude-in-chrome__switch_browser`

**A conta Claude é compartilhada.** A lista de `list_connected_browsers` mostra navegadores de colegas, outras máquinas e outros perfis desta máquina. Por isso:
- Operar só o navegador que vem com `inUse: true` e `onThisComputer: true`. Mesmo assim, no primeiro screenshot do Manychat, conferir que é o perfil logado na conta Tatsuo. Na máquina do user, por exemplo, o sinal é o avatar "T" laranja no rodapé da barra lateral e a saudação "Olá, Tatsuo!". Em outra máquina, o sinal é o do perfil de lá. O deviceId e o nome "Browser N" mudam de uma sessão pra outra: não servem pra identificar.
- **Nunca navegar num navegador da lista pra "testar" se é ele.** Em 25/08 isso abriu uma aba no Mac de um colega.
- Nenhum navegador em uso, ou o certo sumiu da lista e o user diz que está aberto: `switch_browser` (o user clica em Conectar na janela certa). **Nunca concluir que o navegador caiu.** Em 12/10 a lista mostrou só outro perfil, o Claude concluiu que o Chrome da Tatsuo tinha caído, e não tinha: "Já estava aberto o Chrome da Tatsu, tanto que outras conversas ativaram a automação também."
- Manychat ou Instagram pedindo login: parar e pedir ao user. Nunca tentar logar.
- Trabalhar numa aba nova e fechar no fim.
- A largura da janela muda entre sessões. Screenshot ou `find` antes de cada clique; nunca reaproveitar coordenada.

## Passo 3: montar a automação parada

Endereços da conta (`fb2015128`):
- Lista: `https://app.manychat.com/fb2015128/cms?path=/&field=modified&order=desc` (o caminho `/automations` dá 404)
- Busca: `https://app.manychat.com/fb2015128/cms?search=PALAVRA&path=/&field=modified&order=desc`

1. **Colisão.** Buscar a palavra, com e sem acento. A busca acha palavra-chave e também texto de DM. Só é colisão uma automação **global viva** ("qualquer publicação ou Reel") com a mesma palavra; específica de outro post não dispara neste. Global viva com a mesma palavra: avisar o user e propor pausar a global enquanto o post roda. Globais conhecidas: `307`, `Comando!! MBV`, `MBV`, `RAIO - X` (feed) e `MOP`.
2. **Modelo.** A automação mais recente do **mesmo caminho** (MBV ou RAIO-X). Conferir o domínio do link dela, porque a cópia herda o link. O modelo nunca é alterado.
3. **Duplicar** pelo `⋮` da linha na lista: passar o mouse na linha, tirar screenshot e clicar no `⋮` que apareceu. Clicar antes de o `⋮` aparecer abre a automação (em 12/10 abriu uma LIVE; nada foi alterado). A cópia nasce "... copy" no topo em uns 10 a 15 segundos.
4. **Renomear** pelo `⋮` da linha (o `⋮` de dentro da automação só tem Apagar): `IG | AAAA-MM-DD | PALAVRA | tema curto sem acento`.
5. **Editar.** O primeiro clique em Editar depois de abrir a página costuma não pegar. Esperar uns segundos e repetir, alternando o ref do `find` e a coordenada, até a edição abrir.
6. **Palavras-chave.**
   - 3 grafias: `PALAVRA, palavra, Palavra`.
   - 6 se a palavra leva acento no português: as 3 sem acento e as 3 com (`PROSPERO, prospero, Prospero, PRÓSPERO, próspero, Próspero`).
   - A palavra fixa RAIO-X leva 12: `RAIO-X, raio-x, Raio-X, Raio-x, raio-X, RAIOX, raiox, Raiox, RAIO X, raio x, Raio X, Raio x`. Post do caminho RAIO-X com palavra própria (PLACAR, 10/10) leva só as 3 da palavra.
7. **DM.** Curta: uns 100 caracteres, 1 ou 2 frases (o user cortou 30% de uma DM longa). Padrão do MBV: o punch do post + "Quer ver como eu ensino [X] no MBV?". O MBV ensina gestão: não prometer o passo a passo do post. No RAIO-X: "Pega a aula em que eu mostro..."; a aula é paga, nunca chamar de gratuita. Revisar o português e não misturar te e você.
   - Escrever com `form_input`. **O campo come caractere** (sempre por volta do 50º). Conferir por JS. Se faltou um: clicar no campo, `cmd+Up`, `Right` × N (N é a posição do caractere que falta, contada fora do navegador) e digitar só ele.
8. **Botão e link.** Clicar no **próprio botão** `>> Quero ver <<` (MBV) ou `>> Quero a aula <<` (RAIO-X); o modal certo abre com o texto do botão preenchido. **Nunca** "+ Adicionar Um Link", que cria um segundo botão. Se o `form_input` não gravar no modal, `cmd+a` e digitar.
   - MBV: `https://rtc.tatsuoacademy.com/v2-maio-org?utm_source=manychat&utm_medium=dm&utm_campaign=AAAA-MM-DD-PALAVRA`
   - RAIO-X: `https://tatsuoacademy.com/raio-x-empresa-lucrativa/?utm_source=manychat&utm_medium=dm&utm_campaign=AAAA-MM-DD-PALAVRA`. A página do RAIO-X não tem trackeamento: a atribuição desse caminho vem só dos envios e cliques do Manychat. O link segue o mesmo formato, sem gastar tempo com o UTM.
   - O `utm_campaign` só se troca enquanto a automação tem 0 cliques; depois disso a atribuição se parte em dois no CRM.
9. **Post ainda não saiu:** Atualização e deixar **STOPPED**. Ela fica presa ao post do modelo e sem `utm_content`, mas parada não dispara. Recarregar e conferir por JS: parada, palavras, DM e campaign novos, nada do modelo, um botão só.
   **Post já no ar quando a montagem termina** (GANA, 09/10): amarrar e completar o link de uma vez (passo 5), sem passar pela parada.

## Passo 4: timer (post programado)

Só o timer de shell em segundo plano, dentro desta conversa. É o único método que disparou na hora em todas as vezes (agosto a 12/10). Comando, com `run_in_background: true` e **sem `timeout`**:

```
(caffeinate -dimsu -t SEGUNDOS >/dev/null 2>&1 &); until [ "$(date +%H%M)" -ge HHMM ]; do sleep 20; done; date
```

- `HHMM` = horário do post + 1 minuto (post às 19h → `1901`).
- `SEGUNDOS` = de agora até uns 30 minutos depois do post. O caffeinate segura o Mac acordado (no fim de semana de 21-23/08 o Mac dormiu e duas ativações atrasaram de 17 a 20 horas). Dentro do `( ... &)` ele sai do controle da conversa, que é o certo.
- O fim do comando é o que reacorda a conversa. O `until` compara a hora do mesmo dia: não serve pra horário depois da meia-noite.
- **Montar a automação parada nesta mesma conversa antes de armar.** Quando o timer toca, o navegador já está escolhido e a ativação sai sem o user (foi assim em todas as ativações por timer de 07 a 12/10).
- Avisar o user que esta conversa e o app do Claude têm que ficar abertos até a ativação.
- **Dois posts no mesmo dia** (10 e 11/10): montar as duas paradas de uma vez e armar um timer por horário, os dois juntos. Os dois acordaram na hora. Nesse caso o caffeinate pode ir num comando normal, uma vez só, cobrindo até depois do último post: `(caffeinate -dimsu -t SEGUNDOS >/dev/null 2>&1 &); date +%H:%M`.
- **O horário muda com frequência** (AGORA, GRANDE, PLACAR, LIDER e DRE mudaram; FOCO e BASE saíram atrasados). User mudou o horário: armar o timer novo e parar o pendente do horário velho (TaskStop com o id da tarefa, ou `pkill -f "sleep N"` numa checagem, como em 10/10).

**Nunca:**
- **CronCreate.** Falhou três vezes, sempre com um comando em segundo plano vivo na conversa: no retry da SONHO e na AGORA (04/10) o alarme nunca chegou, e no DEZEMBRO (12/10) chegou 48 minutos atrasado, com o post no ar e sem DM.
- **Tarefa agendada** (sessão nova). Ela não consegue escolher o navegador e não roda com o Mac dormindo: no fim de semana de 21-23/08, 3 de 4 falharam.
- **Caffeinate ou vigia rodando sozinho em segundo plano** (`run_in_background` só com o caffeinate, ou um laço de `curl` esperando o Manychat voltar). Foi isso que travou os alarmes de 04/10 e o do DEZEMBRO em 12/10. O caffeinate vai sempre dentro do `( ... &)`, como nos comandos acima.

## Passo 5: amarrar ao post e ativar

1. **Achar o post no perfil**, numa aba nova em `https://www.instagram.com/helio.tatsuo/`, com este JS:
   ```
   [...document.querySelectorAll('a[href*="/p/"], a[href*="/reel/"]')].slice(0,8).map(a=>a.getAttribute('href')+' | '+(a.querySelector('img')?.alt||'').slice(0,90))
   ```
   Os 3 primeiros costumam ser fixados. Conferir a legenda contra o `carousel-text.md`. Nunca chamar a API do Instagram pra isso (regra do CLAUDE.md).
2. **O post não está lá:** rechecar com `sleep N; date +%H:%M` em segundo plano, avisando o user a cada volta (em 10 e 12/10 foi 2, 3, 5, 10 e 15 minutos). O horário passado pode estar errado (PLACAR: o user disse 11h e era 13h). **Nunca ativar em post errado.** O "já postei" do user corta o ciclo: matar o `sleep` pendente e amarrar.
3. **No editor:** Editar e abrir a grade de posts. Se o post não estiver nos 4 primeiros cards, "Mostrar Todos". Escolher pela **capa, pela legenda na prévia e pelo "há N minutos"**, nunca pela posição: frases e reels de outras frentes saem no meio (em 10/10 a frase das 17h estava na frente do RUMO). Grade em quadrados cinza com o Manychat instável: cancelar sem salvar e tentar de novo (04/10).
4. **Completar o link** no próprio botão: `&utm_content=https://www.instagram.com/p/CODIGO/`. Link limpo, com a barra no fim, sem o `?igsh=` do "copiar link" (um `?` a mais quebra o link inteiro). O `utm_content` vai pro card do lead no CRM e o SDR abre o post antes de ligar (decisão do user, 29/09).
5. **Atualização e depois Ativar.** Cada um leva de 20 a 40 segundos de espera: não clicar de novo. Se o `browser_batch` estourar no meio, olhar a tela antes de repetir. Em automação LIVE, o botão no lugar do Ativar vira **Interromper**: conferir antes de clicar ali.
6. **Recarregar e conferir por JS** (o JS não lê query string direto; comparar por `includes`):
   ```
   const h=document.documentElement.innerHTML; ({live:/LIVE/.test(document.body.innerText.slice(0,400)), novo:h.includes('CODIGO_DO_POST'), modelo:h.includes('CODIGO_DO_POST_DO_MODELO'), camp:h.includes('AAAA-MM-DD-PALAVRA'), dm:h.includes('TEXTO EXATO DA DM'), botoes:(document.body.innerText.match(/>> Quero ver <</g)||[]).length})
   ```
   Tem que dar: `live`, `novo`, `camp` e `dm` verdadeiros, `modelo` falso e `botoes` igual a 1 (no RAIO-X, contar `>> Quero a aula <<`).

## Passo 6: se passou dos 5 minutos

Ativar primeiro, explicar depois. O relato **termina com a DM e o link completo** (o mesmo `utm_campaign` e `utm_content` da automação), em bloco pronto pro user mandar à mão, um por um, a quem comentou antes da ativação. Pedido do user em 12/10: "No final da explicação, eu quero a mensagem que é para eu mandar um por um na DM com o link." Como é o mesmo link, quem clicar cai na mesma campanha no CRM. Registrar o atraso e a causa no baseline.

## Passo 7: fechar

1. Desligar o caffeinate com o mesmo número do timer (`pkill -f "caffeinate -dimsu -t SEGUNDOS"`) e conferir com `pgrep -fl caffeinate`. Se ainda houver outro post no dia com timer armado, deixar o caffeinate até o último. Fechar a aba do Instagram.
2. **Registrar no fim de `conteudo/analise/manychat-baseline.md`**, no formato das entradas de outubro:
   - título ``## DD/MM/AAAA — `NOME DA AUTOMAÇÃO` (carrossel N) — MONTADA STOPPED ~HHhMM, LIVE ~HHhMM (post ...)``;
   - caminho, `utm_campaign`, `utm_content`, link completo, palavras, resultado da busca de colisão, DM com o nº de caracteres (e se foi escrita pelo Claude), botão, modelo duplicado (intocado), URL da automação;
   - o post achado (código, começo da legenda, card da grade, capa), o que foi conferido recarregando e qualquer pegadinha nova.
3. Pôr a data de publicação na ficha do post em `conteudo/analise/registro-posts.csv`. Rodar `/etiqueta` se o user pediu.
4. Commit conforme a regra de commit da máquina (CLAUDE.md).

## O relato pro user

Curto, sempre no mesmo formato:
- Primeira linha: "O Manychat do X ficou ativo às HHhMM, uns N minutos depois de o post subir às HHhMM."
- Post achado (código e começo da legenda) e a capa conferida na prévia.
- Palavras e o resultado da busca de colisão.
- DM e botão (avisar se a DM é do Claude).
- Link: caminho, `utm_campaign` e `utm_content`.
- Conferência depois de recarregar: ativa, post novo, UTM novo, um botão só, nada do modelo.
- Mac de volta ao normal e registro feito.
- Montada parada (post programado): o mesmo resumo, mais o horário do timer e o que vai acontecer nele.
- Atrasou: o bloco de DM e link do passo 6 no fim.

## Casos que já aconteceram

- **Post apagado e repostado** (27/08 e 02/10). A automação fica LIVE presa ao post morto ("Não conseguimos encontrar uma conexão") e não dispara; "Tentar Novamente" não resolve. Em Editar, alternar o rádio pra "qualquer publicação" e voltar pra "publicação específica" **sem salvar no meio** (isso recarrega a grade), escolher o post novo, trocar o `utm_content` e salvar. Quando o user disser que repostou ou mexeu no post, conferir se o código mudou: editar a legenda mantém o código, apagar e repostar troca.
- **Manychat fora do ar** (04/10). Avisar o user e tentar de novo, em aba nova, quando o serviço voltar. Nada de vigia em segundo plano. O app do Manychat no celular do user é uma saída que pode ser oferecida.
- **Automações que já existem e não se montam por post.** Stories: `RAIO - X stories`, `MOP stories` e `MBV stories`, que valem pra qualquer story (criadas pelo modelo "Gere leads com stories"). Live: `LIVE | 2026-10-13 | RAIO-X | comentario na live` (gatilho "Comentários ao vivo") e `LIVE | 2026-10-13 | RAIO-X | DM palavra-chave` (plano B; o gatilho de DM aceita no máximo 12 palavras). As de live ficam ligadas pra qualquer live (decisão do user, 13/10). Como foram montadas está no baseline (12/09 e 13/10).
