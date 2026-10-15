# O que funciona no perfil do Hélio — análise de desempenho real

> Fonte: API oficial do Instagram (`conteudo/analise/desempenho.csv`), 1.706 posts,
> jan/2025 → ago/2026. Análise feita em 2026-08-14. Métrica-guia: **compartilhamentos**
> (o sinal mais forte de performance orgânica). Base filtrada: posts com alcance > 5k.
> Atualizar este arquivo quando o dado novo for relevante (o `update` roda sozinho; ver `scripts/instagram/README.md`).
> Nunca rodar o `pull` completo: ele dispara o anti-abuso da Meta e bloqueia a API por dias.

## A regra de ouro que os dados mostram

A distribuição é de cauda longa: a mediana do feed é ~250 shares e os hits passam de
20.000. Ninguém "só faz hits" — o jogo é **mirar nas veias comprovadas, publicar com
constância e medir**. Cada post novo é uma tentativa bem mirada, não uma aposta cega.

## Veias temáticas rankeadas (média de shares por post de feed)

| # | Veia | Média | Mediana | Leitura |
|---|------|-------|---------|---------|
| 1 | **Pressão / cansaço / dor / peso** | 1.968 | 253 | A veia mais forte do perfil. TODOS os maiores hits estão aqui. |
| 2 | Propósito / escolha / sonho | 1.513 | 226 | Forte quando confronta ("sonho com CNPJ"). |
| 3 | Time / funcionário / preparo | 1.482 | 246 | Forte quando a culpa volta pro DONO (não quando reclama de funcionário). |
| 4 | Crescimento | 957 | 296 | Consistente, poucos hits gigantes. |
| 5 | Liderança / dono | 864 | 249 | Média. |
| 6 | Lucro / dinheiro / margem | 263 | 98 | A mais fraca em compartilhamento. Tema técnico GUARDA (saves), não ESPALHA. |

## O mecanismo dos vencedores (o padrão que se repete)

Os posts gigantes não motivam nem ensinam. Eles **consagram quem sente a dor** e criam
dois grupos — quem está no jogo × quem olha de fora. Compartilhar é se declarar do
grupo certo. É o mecanismo de:

- **"Tem gente que não cansa… porque nunca entra. Fica na arquibancada"** — IMAGEM ÚNICA,
  38.139 shares, 3,7M alcance, 150k likes (2026-02-18). **O maior post da história do perfil.**
- "PRESSÃO É UM PRIVILÉGIO! Se você sente pressão, está em um jogo" — 18.170 shares (2025-02-15).
- "Que privilégio estar cansado por um desafio que você mesmo escolheu" — 6.182 (2026-02-01).
- "Escolha o seu estresse. Não existe vida sem pressão" — 5.997 (2026-03-28).
- "Todo crescimento vem com pressão" — IMAGEM, 5.990 (2025-11-12).
- "A pressão é o peso da liderança" — IMAGEM, 4.443 (2025-08-31).
- "No raso não existe pressão" — post 37 (2026-08) segue exatamente esse molde.

Segundo mecanismo comprovado: **confronto direto ao dono, com a culpa voltando pra ele**
(nunca pro funcionário/mercado/governo):

- "Você contrata alguém bom… mas não prepara. Não ensina. Não acompanha" — 22.087 shares.
- "Empresário que não prepara o time vive trocando de funcionário achando que o problema é o mercado" — 18.551.
- "Seu time 'não entende'? Eles não fazem porque você não deixou claro" — 11.645.
- "PME não é 'um negócio'. É um sonho com CNPJ" — 17.478.

Terceiro: **paradoxo/dupla leitura** ("Quem divide, multiplica"; o pato que faz tudo e
não é o melhor em nada — 10.122).

## Taxa de compartilhamento (shares/alcance) — o sinal de viralidade

Campeões de taxa (>3,5%) são carrosséis de confronto com pergunta ou resposta a objeção:
"Faltou algum, empresário?" (5,9%), "'Não dá pra achar gente boa' — dá sim, você só não…"
(4,8%), "'Eles não fazem o que eu espero' — claro que não, você nunca deixou claro" (3,7%),
"Tudo aquilo que permanece confortável por tempo demais começa a perder força" (3,8%).
A taxa boa de um post saudável fica em ~1%; hit de verdade passa de 3%.

## Formatos (mediana de shares, alcance > 5k)

| Formato | n | Mediana | Média | Nota |
|---------|---|---------|-------|------|
| Carrossel | 245 | 182 | 1.075 | O formato mais consistente. |
| Imagem única (frase) | 110 | 124 | 743 | Mediana menor, MAS detém o maior hit do perfil (38k). Alto risco/alto teto. |
| Reels | 454 | 80 | 594 | Vive de outra dinâmica (alcance); top reel: "Dinheiro vai e vem. O tempo, não" — 31.800 shares. |

## O que NÃO funciona (fundo do poço, alcance > 5k)

- **Comunicados e institucional** ("🚨 COMUNICADO 🚨" — 1 share; recap do MBV — 3).
- **Homenagens pessoais** (post sobre a esposa — 6 shares; a audiência respeita, não espalha).
- **Tema técnico-financeiro sem camada humana** ("vender no cartão", "quero vender mais" — 7-15 shares; geram saves, não shares).
- **Moralizar cultura/omissão em tom professoral** ("Toda omissão ensina alguma coisa" — 11; "Toda cultura começa quando alguém decide viver primeiro…" — 15).
- Padrão geral: post que ensina sem incomodar GUARDA; post que incomoda ESPALHA. Saves altos + shares baixos = conteúdo de apostila, não de identidade.

## Como isso alimenta a produção (regras práticas)

1. Toda frase nova mira uma veia do topo da tabela (1 a 3), nunca a 6 sem camada humana.
2. O mecanismo é consagração + dois grupos, ou confronto ao dono, ou paradoxo — de
   preferência um só, bem executado (diretriz completa: `.claude/skills/frase/referencias/diretriz-frase-legenda.md`).
3. Cada veia pede símbolo visual INÉDITO a cada post (o mar do post 37 não se repete;
   a próxima frase de pressão precisa de outra imagem).
4. Medir sempre: ler o `conteudo/analise/desempenho.json` 3-4 dias após publicar (insights
   fecham em até 48h). O dado chega sozinho; se o `pulled_at` passar de 24h, rodar só
   `python3 scripts/instagram/pull_insights.py update`, nunca o `pull` (bloqueia a API da Meta
   por dias). Na máquina que recebe o pacote diário, não rodar nada: o dado vem no pacote.
   Registrar o resultado no
   `conteudo/banco-frases.md` e comparar a taxa shares/alcance com a régua de ~1%.
