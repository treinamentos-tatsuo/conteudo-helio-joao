> **NESTA MÁQUINA (João): NÃO configurar a API.** Este documento descreve a configuração da máquina de origem. Aqui os dados chegam pelo pacote diário (ver CLAUDE.md → Analytics).

# Handoff — Integração da API do Instagram (mapear o que dá resultado)

> **Status (13/10/2026):** concluído. A base foi montada em 06/08/2026 e a API roda só na máquina principal (token em `~/.tatsuo/ig-token.json`, agendamento `com.tatsuo.ig-update`). **Não repetir este setup em outra máquina** (a máquina do João recebe o dado pelo pacote diário, ver `scripts/pacote/README.md`) e **nunca rodar `pull`**: ele dispara o anti-abuso da Meta e bloqueia a API por dias. No dia a dia, só `update`.
> **Objetivo:** puxar automaticamente o desempenho de todos os posts do Instagram do Hélio (visualizações, comentários, compartilhamentos, salvamentos, alcance), mapear o que mais deu resultado e transformar isso na base dos próximos carrosséis.
> **Caminho escolhido:** B — API oficial da Meta (Instagram API with Instagram Login).

## O que JÁ está pronto (2026-08-05)

- Script de dependência zero em [`scripts/instagram/pull_insights.py`](../scripts/instagram/pull_insights.py) com os comandos: `exchange` (troca token curto→longo), `pull` (puxa mídia + insights → `conteudo/analise/desempenho.json` + `.csv`; usado uma vez pra montar a base, nunca mais rodar), `update` (o do dia a dia: incremental, leve), `refresh` (renova o token).
- Guia de uso em [`scripts/instagram/README.md`](../scripts/instagram/README.md).
- `.gitignore` já protege qualquer resquício de token/secret.

## O que FALTA (só uma pessoa consegue — envolve login, não passa pelo Claude)

1. Criar o app na Meta (passo a passo abaixo) e pegar **App ID** + **App Secret**.
2. Adicionar a conta do Hélio como testadora e gerar um **token de curta duração** com os escopos de insights.
3. Rodar `python3 scripts/instagram/pull_insights.py exchange`. A base já existe (montada em 06/08/2026): daí em diante só `update`, nunca `pull` (bloqueia a API da Meta por dias).
4. Pedir ao Claude: *"varre o `conteudo/analise/desempenho.csv` e monta o `_contexto/o-que-funciona.md`"*.

## Como assumir esta tarefa (handoff entre pessoas)

Uma conversa ao vivo do Claude Code **não muda de dono** — cada pessoa roda o Claude na própria máquina, com sessão local. O que se transfere é o **contexto**, por Git (igual ao resto do workspace).

Para assumir:
1. `git pull` neste repositório.
2. Abrir o Claude Code dentro da pasta `tatsuo-carrossel`.
3. Dizer ao Claude: *"Continue o handoff em `_contexto/handoff-api-instagram.md` — vamos montar a API do Instagram"*.
4. O Claude lê este arquivo e retoma exatamente daqui.

Nada de senha ou login é passado por aqui. O token de acesso (ver abaixo) fica só na máquina de quem executa, **fora do Git** (já está no `.gitignore`).

---

## Por que a API (e não login/senha)

O Instagram não permite login com usuário e senha por ferramenta, e a leitura raspando o painel viola os termos (risco de sinalizar a conta). A via correta é a API oficial da Meta.

**A boa notícia:** para acessar **a própria conta**, o acesso é *Standard Access* — **não precisa de App Review, nem verificação de negócio, nem Página do Facebook vinculada**. Toda a burocracia que assusta na documentação é só pra quem acessa contas de terceiros. Não é o nosso caso.

## Pré-requisitos

- [ ] Conta do Hélio como **Profissional** (Business ou Criador) — provavelmente já é.
- [ ] Acesso à conta do Meta for Developers da empresa (ou criar uma).
- [ ] Alguém com login do Instagram do Hélio disponível na hora de autorizar o app (só uma vez, no navegador do Meta — não passa por aqui).

## Passo a passo do setup

1. **Criar o app** em https://developers.facebook.com/ → *Criar app* → tipo **Business**.
2. Adicionar o produto **Instagram** → *API setup with Instagram login*.
3. Anotar o **App ID** e o **App Secret**.
4. Em *Instagram → API setup*, adicionar a conta do Hélio como testadora e aceitar o convite pela conta.
5. Gerar o **token de acesso** com os escopos:
   - `instagram_business_basic`
   - `instagram_business_manage_insights`
6. Trocar o token de curta duração por um de **longa duração** (~60 dias) — o script faz isso.
7. Guardar o token num arquivo local fora do Git (ex.: `~/.tatsuo/ig-token.json`).

## Métricas por post que a API entrega (o que interessa)

`views` · `reach` · `likes` · `comments` · `saves` · `shares` · `reposts` · `total_interactions` · `follows` · tempo médio de visualização (Reels).

> Cobre exatamente o tripé pedido: **visualização, comentário e compartilhamento**.

## Limitações que precisam estar na mesa

- **Retenção de 2 anos.** Post mais antigo que isso não retorna insights.
- **Até 48h de atraso** — post de ontem ainda não fechou os números.
- Posts publicados **antes** da conta virar profissional não têm insights.
- `impressions` e `video_views` foram descontinuados → hoje é tudo `views`.
- Rate limit folgado pra este uso (leitura de uma conta só).

## O que o script faz (a construir)

Um script Python simples, sem MCP de terceiro com o token da empresa dentro:
1. Lê o token do arquivo local.
2. Pagina `GET /me/media` puxando todos os posts (id, tipo, legenda, timestamp, permalink).
3. Para cada post, chama `/{media-id}/insights` com as métricas acima.
4. Salva tudo em `conteudo/analise/desempenho.json` (dado bruto, versionável) + um `.csv` legível.

## Plano de análise (o que fazer com os dados)

1. **Ranking por métrica separada** — top de alcance ≠ top de compartilhamento. Compartilhamento é o sinal mais forte.
2. **Normalizar pelo tamanho da audiência na época** — pra post velho não parecer fraco só por ter menos seguidor na publicação.
3. **Separar por formato** — carrossel com carrossel, reel com reel.
4. **Extrair o padrão** — gancho, pilar do MBV (Lucratividade / Crescimento / Cultura), estrutura do argumento, grau de confronto na 1ª frase.
5. **Consolidar** em `_contexto/o-que-funciona.md` — arquivo permanente que passa a alimentar a skill `/carrossel`. Todo carrossel novo nasce ancorado no que deu resultado.

## Plano B enquanto a API não sobe

Exportar CSV manual: Meta Business Suite (desktop) → Insights → Conteúdo → período → Exportar dados. Jogar o arquivo em `conteudo/analise/` e pedir a varredura. Serve pra provar valor no mesmo dia.
