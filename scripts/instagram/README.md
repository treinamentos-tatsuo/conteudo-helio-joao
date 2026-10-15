# Puxador de desempenho do Instagram

Script de dependência zero (só Python 3 padrão) que puxa o desempenho de todos os
posts do Instagram do Hélio via API oficial da Meta e salva em `conteudo/analise/`.

## Setup (uma vez)

Já feito na máquina principal. Não repetir em outra máquina (ver "Rodando").

Antes de rodar o script, é preciso criar o app na Meta e gerar um token.
Passo a passo completo em [`_contexto/handoff-api-instagram.md`](../../_contexto/handoff-api-instagram.md).

Resumo do que **você** faz no navegador (o Claude não faz — envolve login):

1. https://developers.facebook.com/ → **Criar app** → tipo **Business**.
2. Adicionar produto **Instagram** → **API setup with Instagram login**.
3. Anotar **App ID** e **App Secret**.
4. Adicionar a conta do Hélio como testadora e aceitar o convite pela conta.
5. Gerar um **token de curta duração** com os escopos:
   `instagram_business_basic` + `instagram_business_manage_insights`.

## Rodando

> **NUNCA rodar `pull`.** O `pull` completo varre todos os posts de uma vez e já disparou o
> anti-abuso da Meta (17/08/2026), bloqueando a API por dias. O comando do dia a dia é o `update`.

> **A API roda numa máquina só**: a principal, que tem o token em `~/.tatsuo/ig-token.json` e o
> agendamento `com.tatsuo.ig-update`. Na máquina do João não se roda nenhum comando deste script:
> o dado chega pelo pacote diário (`scripts/pacote/README.md`).

```bash
# dia a dia: incremental e leve (posts novos + releitura dos últimos 30 dias).
# Já roda sozinho às 9h, 14h e 20h e no boot (launchd com.tatsuo.ig-update).
# Rodar à mão só se o pulled_at do desempenho.json passar de 24h.
python3 scripts/instagram/pull_insights.py update

# regrava o snapshot de hoje a partir do disco, sem chamar a API
python3 scripts/instagram/pull_insights.py snapshot

# (a cada ~50 dias) renova o token antes de expirar
python3 scripts/instagram/pull_insights.py refresh

# (só no setup, uma vez) troca o token curto por um longo (~60 dias). Pergunta App ID /
# Secret / token em modo oculto: nada aparece na tela nem vai pro histórico do shell.
python3 scripts/instagram/pull_insights.py exchange
```

Saída:
- `conteudo/analise/desempenho.json` — dado bruto, um registro por post.
- `conteudo/analise/desempenho.csv` — legível, uma linha por post.
- `conteudo/analise/_snapshots.csv` — foto diária dos posts com até 30 dias (a API só dá o acumulado).
- `conteudo/analise/_update.log` — o que o `update` imprimiu em cada rodada do agendamento.

## Onde fica o token

`~/.tatsuo/ig-token.json` — **fora do repositório**, permissão 600. Nunca entra no Git e só existe
na máquina principal. Não copiar pra outra máquina: duas máquinas chamando a API é o que não pode.
