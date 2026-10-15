# Setup da máquina nova (Windows)

> Pra fazer uma vez, com o Claude ajudando. A máquina de origem é um Mac; esta é Windows. A tradução dos comandos de Mac que aparecem nas skills está em `WINDOWS.md`: o Claude daqui lê esse arquivo antes de rodar qualquer coisa.

## 1. Programas (nesta ordem)

1. **Git for Windows** (https://git-scm.com/download/win). Vem com o Git Bash, que é o terminal que o Claude usa no Windows. Na instalação, deixar as opções padrão.
2. **Python 3** (https://www.python.org/downloads/). Na primeira tela do instalador, marcar **"Add python.exe to PATH"**. Depois, em Configurações > Aplicativos > Configurações avançadas de aplicativos > **Aliases de execução de aplicativo**, desligar `python.exe` e `python3.exe` (os atalhos da Microsoft Store).
3. **Node.js** LTS (https://nodejs.org).
4. **Google Chrome** e a extensão **Claude in Chrome**.
5. **App do Claude** (Claude Desktop, aba Code).

Depois, abrir o **Git Bash** e rodar, um de cada vez:
```bash
git config --global core.autocrlf false
```
```bash
git config --global core.longpaths true
```
```bash
python -m pip install --user pillow numpy
```
```bash
mkdir -p ~/bin && printf '#!/bin/sh\nexec python "$@"\n' > ~/bin/python3 && chmod +x ~/bin/python3
```
(o último cria o atalho `python3`, que as skills usam).

## 2. Onde colocar cada pasta

A pasta `maquina-conteudo-tatsuo` que veio pelo Drive tem:

| Pasta recebida | Vai pra (no Windows) |
|---|---|
| `1-projeto-tatsuo-carrossel/` | `C:\Users\<você>\Documents\tatsuo-carrossel\` (abrir esta pasta no Claude) |
| `2-entregas-postadas\carrosseis claude\` | Área de Trabalho: `carrosseis claude\` |
| `2-entregas-postadas\frases claude\` | Área de Trabalho: `frases claude\` |
| `3-acervo-fotos-helio\` | Área de Trabalho: `fotos para carrosséis\` (o nome tem que ser exatamente este) |
| `4-apostila-mbv`, `5-criativos-trafego-mbv`, `6-roteiros-reels-copy` | Área de Trabalho (consulta) |

Se a Área de Trabalho estiver dentro do OneDrive, avisar o Claude (ver `WINDOWS.md`).

Dentro de `Documents\tatsuo-carrossel`, no Git Bash:
```bash
npm install
```
```bash
npx playwright install chromium
```

## 3. Repositório próprio (Git)

Esta cópia vem sem histórico e sem ligação com a máquina de origem. Criar um repositório **privado** novo (GitHub da empresa ou do João) e, dentro de `Documents\tatsuo-carrossel`:
```bash
git init -b main
```
```bash
git add -A && git commit -m "Máquina de conteúdo do Hélio: cópia inicial (13/10/2026)"
```
Depois ligar ao repositório novo (`git remote add origin <url>` e `git push -u origin main`). Nunca ligar ao repositório da máquina de origem.

O `.gitignore` já deixa fora do Git as imagens, as transcrições e o scouting do MBV, a apostila e os leads (dados pessoais). Elas ficam só no disco: fazer backup da pasta no Drive de vez em quando.

## 4. Logins (cada um faz o seu; nenhuma senha vem na cópia)

- **Geração de imagem (ChatGPT da empresa):** no Git Bash, `npx @openai/codex login` e entrar com a conta ChatGPT da empresa. Cria `C:\Users\<você>\.codex\auth.json`. A skill `gpt-image2-ratos` sobe o proxy sozinha. Teste: pedir uma frase com `/frase` e ver a imagem sair.
- **Chrome + Claude in Chrome:** num perfil do Chrome só pra isso, entrar no Manychat (conta Tatsuo) e no Instagram do Hélio. Dar ao perfil um avatar fácil de reconhecer: o /manychat confere o perfil por screenshot antes de mexer. A conta Claude pode aparecer ligada a outras máquinas: o Claude daqui só opera o navegador deste computador.
- **Instagram API e CRM (GoHighLevel):** NÃO configurar. Esta máquina recebe os dados pelo pacote diário, e os scripts de coleta estão travados.

## 5. Energia (pro /manychat)

O timer que ativa o Manychat na hora do post precisa do PC acordado. Em Configurações > Sistema > Energia, deixar "Suspender" em **Nunca** quando estiver na tomada (ou seguir o que está em `WINDOWS.md`).

## 6. Permissões do Claude

Na máquina de origem o Claude trabalha com autonomia (edita arquivos e roda comandos sem pedir confirmação a cada passo). Decidir com o user se repete aqui. No mínimo, liberar acesso às pastas da Área de Trabalho: `carrosseis claude`, `frases claude` e `fotos para carrosséis`.

## 7. Agendamento (opcional)

Pautas do dia às 7h: criar no app uma tarefa agendada diária às 7h com o prompt:

> Rodar a skill /pautas do projeto Documents\tatsuo-carrossel do começo ao fim, sozinho e sem pedir confirmação: `python scripts/noticias/coletar.py` (com `--horas 48` se a edição de ontem não existir em conteudo/noticias/), escolher 10 notícias do nicho empresarial e 10 do médico pelas regras da skill e salvar em conteudo/noticias/AAAA-MM-DD.md (horário de Brasília) só com manchete e link. Não chamar a API do Instagram, não criar post nem Manychat, não mexer em outro arquivo além de conteudo/noticias/. Relatório: a lista inteira e o caminho do arquivo.

O ritual não se agenda aqui: ele roda depois de importar o pacote do dia.

## 8. Teste de que tudo funciona

1. Renderizar um slide antigo: `npx playwright screenshot --viewport-size=1080,1350 "conteudo/carrosseis/231_liderar-e-unir-repost/instagram/slide-01.html" teste.png` e abrir o `teste.png`.
2. Importar o primeiro pacote: `python scripts/pacote/importar_pacote.py ~/Downloads/pacote-AAAA-MM-DD.zip`.
3. Rodar `/ritual`.
4. Rodar `/pautas`.
5. Pedir uma frase com `/frase` e conferir que a imagem é gerada e abre no visualizador.
