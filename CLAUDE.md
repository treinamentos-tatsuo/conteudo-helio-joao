# Tatsuo Academy — Máquina de conteúdo do Hélio (PC do João)

## O que é esta máquina

Cópia completa da máquina de conteúdo que produz o Instagram do Hélio Tatsuo (carrosséis, frases, caixinhas, Manychat, análise). Foi entregue pronta em 13/10/2026 e é **independente**: repositório próprio, sem ligação com a máquina de origem. Nada daqui vai pra lá, e de lá só chega o pacote diário de analytics (ver abaixo). Nunca adicionar como remoto o repositório de origem nem tentar sincronizar com ele.

Comece por `LEIA-PRIMEIRO.md` (o que se produz e com qual comando) e `SETUP-MAQUINA-NOVA.md` (instalação).

**Esta máquina é Windows.** As skills foram escritas num Mac: antes de rodar qualquer comando que elas mandem (`python3`, `open`/Preview/Finder, `caffeinate`, `date -j`, `swift`), traduzir pela tabela de `WINDOWS.md`. Os caminhos `~/Desktop/...` das skills são a Área de Trabalho deste Windows (conferir se ela está no OneDrive, ver `WINDOWS.md`).

## Quem opera e como trabalhar com ele

O operador é o **João**. Ele está aprendendo: chega sem saber o método e costuma errar. O padrão das peças não cai por causa disso. O seu papel:

- **Seja incisivo e questione.** Quando um pedido dele piorar o texto em relação ao padrão (voz, doutrina, ICP, diagramação), diga isso com argumento e mostre ao lado o exemplo aprovado do gabarito (`.claude/skills/carrossel/referencias/voz-helio-gabarito.md`). Não aplique calado uma mudança que você sabe que piora.
- **Explique o porquê.** Toda regra tem uma razão (o dado, a reprovação, a doutrina). Quando ele perguntar ou insistir, explique. Se precisar, dê uma aula curta: use o que for necessário pra ele entender, com exemplo real das pastas.
- **Nunca deixe o padrão cair.** As frases (`/frase`) são o formato mais consistente e você acerta bastante. O mais difícil são os **carrosséis**: o texto sempre para no CHECKPOINT 1 pra aprovação dele, e você compara cada slide com o gabarito antes de mostrar.
- **A decisão é dele.** Depois de argumentar, se ele mantiver, faça como ele pediu e registre a divergência no `carousel-text.md` da peça.
- **Mudança nas skills:** só com a aprovação dele. Proponha o registro quando uma correção for regra (mexe em leitura, impacto ou doutrina, e se repetiu ou ele disse "sempre/nunca"). Correção de uma peça só e escolha artística não viram regra: "a gente enche de regra o negócio e começa a se perder".
- **Autonomia:** aja sem pedir permissão a cada passo. A única parada obrigatória é o texto do carrossel (CHECKPOINT 1) antes de qualquer HTML ou imagem.

## Estrutura

- `conteudo/carrosseis/` — um carrossel ou frase por pasta, em **ordem de publicação**: `J[N]_nome-do-post/` com `carousel-text.md` (texto + legenda), `imagens/` e `instagram/` (HTML + PNG). **Toda pasta de post criada nesta máquina começa com J** (regra do João, 19/10/2026; as de 240 em diante foram renomeadas, as até 239 vieram da instalação e ficam sem J). O próximo número é sempre o maior J existente mais um (`ls conteudo/carrosseis | grep -oE '^J[0-9]+' | tr -d J | sort -n | tail -1`, mais 1): conferir logo antes do `mkdir`, porque outras sessões criam pastas ao mesmo tempo. Nunca renomear pasta com geração de imagem rodando. A coluna `pasta` do `registro-posts.csv` leva o nome com o J.
- `conteudo/carrosseis/_banco-referencias/` — acervo P&B de referência de estilo. O `README.md` é o catálogo.
- `conteudo/carrosseis/_da-maquina-do-user/` — textos dos posts feitos na máquina de origem, chegados pelo pacote de analytics.
- `~/Desktop/carrosseis claude/POSTADOS/` e `~/Desktop/frases claude/` — tudo o que já foi entregue e postado (inclusive "claude 1" a "claude 13"). É onde se busca post antigo pra repostar.
- `~/Desktop/fotos para carrosséis/` — acervo de fotos reais do Hélio.
- `~/Desktop/POSTS/` — **entrega por conversa.** Uma subpasta com o nome exato de cada conversa fixada no app (Caixinhas, Carrossel Tatsuo Academy, Carrossel foto, Carrossel sem rosto, Frase sem rosto, Frase foto). Ao fechar uma peça, copiar o material final (PNGs + `carousel-text.md` com a legenda; nas caixinhas, o texto) pra `POSTS/<título da conversa atual>/<pasta da peça>/`. O original continua em `conteudo/carrosseis/` (é o que vai pro commit). Se a subpasta não existir, criar com o título da conversa; se a conversa não for uma das fixadas, perguntar ao João onde salvar.
- `G:\Meu Drive\POST CLAUDE\` (Google Drive deste PC) — **cópia diária no Drive** (pedido do João, 19/10/2026). Duas pastas: `HÉLIO TATSUO/` (posts do @helio.tatsuo) e `TATSUO ACADEMY/` (posts do perfil da Academy). No primeiro post fechado do dia, criar dentro de cada uma a pasta da data (`AAAA-MM-DD`, ex.: `2026-10-19`); cada post fechado no dia vai pra pasta do dia do perfil dele: `POST CLAUDE/<perfil>/<data>/<pasta da peça>/`, com o mesmo material da entrega em POSTS (PNGs finais, sem as versões intermediárias, `carousel-text.md` e `legenda.txt`). Vale junto com a entrega em `~/Desktop/POSTS/`, não no lugar dela.
- `_contexto/` — guia de voz (`preferencias.md`), transcrições do MBV e banco de scouting (material do treinamento pago: não compartilhar).

## As skills

- `/carrossel` — carrossel (modelos: editorial-punch com imagem gerada, fotos-reais com fotos do Hélio, infográfico educativo do MBV no perfil da Tatsuo Academy, fábula, thread-x, handmade com desenho a lápis e bonecos no perfil da Tatsuo Academy). Voz em `referencias/voz-tatsuo.md`, gabarito em `referencias/voz-helio-gabarito.md`, doutrina em `referencias/doutrina.md`.
- `/frase` — frase única do dia com imagem gerada (9h).
- `/frase-foto` — frase com foto real do Hélio, ou manuscrita no papel ou no vidro. Quem escolhe a variante é o João.
- `/manychat` — monta e ativa a automação do post na hora da publicação (conversa dedicada).
- `/caixinhas` — caixinhas de pergunta dos stories.
- `/etiqueta` — ficha do post logo depois de fechar.
- `/ritual` — análise diária, a partir do pacote importado.
- `/pautas` — notícias quentes do dia.

## Analytics: esta máquina NÃO acessa a API

A API da Meta bloqueia quando roda em duas máquinas. Por isso, aqui:

- **Proibido rodar** `scripts/instagram/pull_insights.py` (nem `update`, nem `pull`), `scripts/ghl/pull_leads.py` e qualquer leitura do painel do Manychat pra analytics. Os scripts estão travados nesta cópia.
- **O dado chega pelo pacote diário** `pacote-AAAA-MM-DD.zip` (dados brutos, sem interpretação). Importar com:
  `python3 scripts/pacote/importar_pacote.py <caminho-do-zip>`
  O importador confere os checksums e copia os dados pra `conteudo/analise/`, sem sobrescrever o `registro-posts.csv` daqui.
- Depois de importar, `/ritual` faz a análise **por conta própria**: você interpreta os dados sozinho. O pacote não traz análise da máquina de origem, de propósito.
- Se o `pulled_at` do `desempenho.json` estiver velho, a saída é pedir o pacote mais recente ao user, nunca chamar a API.
- O `leads.json` tem dados pessoais de leads: não copiar pra fora do projeto nem colar em conversa.

## Pautas do dia

`/pautas` roda a coleta `python3 scripts/noticias/coletar.py` (Google Notícias, Trends e feeds, sem chave de API) e entrega 10 manchetes do nicho empresarial e 10 do médico, só manchete e link. Pode ser agendada pra 7h no app (ver `SETUP-MAQUINA-NOVA.md`).

## Commit (regra desta máquina)

**Commit e push sempre**, no repositório do João, ao fechar cada entrega (carrossel, frase, etiqueta, Manychat, ritual). As skills dizem "commit conforme a regra de commit da máquina": aqui, isso quer dizer commitar e dar push no fim. Nunca commitar credencial nem o `leads.json` fora do que já está versionado.

## Tom de voz

Direto, firme, didático, sem enrolação. Linguagem de empresário da vida real. Sem jargão corporativo. Sem guru, sem coach. A frase de fechamento institucional da marca é: "Seja Bem-Vindo ao Fim do Analfabetismo Empresarial." Ver `_contexto/preferencias.md` (guia original, base obrigatória) e `.claude/skills/carrossel/referencias/voz-tatsuo.md`.

**Fontes de voz, crença e público:** só o guia original (`_contexto/preferencias.md`), as transcrições dos três dias do MBV (`_contexto/transcricoes-mbv/`) e os dados do próprio projeto. Os roteiros e perfis de referência (`_contexto/metodo-roteiros-helio.md`) servem só pra estrutura (palavra-chave, intenção, virada, contraste), nunca pra voz, crença ou público.

## Marca

Cores, tipografia e logo em `marca/design-guide.md`. Preto, branco e vermelho carmim (`#A91C20`). Sem cores secundárias, sem gradiente, sem emoji.

## Sobre a Tatsuo Academy

Empresa de educação empresarial criada por Hélio Tatsuo. Missão: acabar com o analfabetismo empresarial de pequenas e médias empresas brasileiras. O Hélio fala como empresário pra empresário, nunca como coach ou palestrante. A metodologia central é o MBV, com três pilares: Lucratividade, Crescimento e Cultura. O perfil é do Hélio (@helio.tatsuo); os posts da apostila vão pro perfil da Tatsuo Academy.

## Geração de imagem

Skill `.claude/skills/gpt-image2-ratos/` (motor gpt-image-2 via login OAuth do ChatGPT da empresa, sem custo de API). Precisa de `~/.codex/auth.json` logado via Codex CLI (ver `SETUP-MAQUINA-NOVA.md`). O Hélio nunca é gerado por IA.
