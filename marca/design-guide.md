# Guia de Design — Tatsuo Academy

> Você pode editar esse arquivo a qualquer momento.
> As skills de carrossel, proposta, slide e documentos leem este arquivo antes de criar qualquer visual.
> Design System completo (CSS, assets, componentes): `marca/Tatsuo Academy Design System/`

---

## Cores

Sistema de três cores — preto, branco e vermelho carmim. Sem cores secundárias.

| Token | Valor | Uso |
|---|---|---|
| `--red-primary` | `#A91C20` | Logo, acentos, botões primários, destaques |
| `--red-deep` | `#6C0302` | Hover/pressed, gradiente escuro |
| `--red-bright` | `#DF0900` | Topo de gradientes vermelhos |
| `--black` | `#0A0A0A` | Fundos escuros, texto primário em claro |
| `--charcoal` | `#1F1F1F` | Superfícies escuras secundárias |
| `--gray-700` | `#3A3A3A` | Texto de corpo |
| `--gray-500` | `#6B6B6B` | Texto secundário, labels, eyebrows |
| `--gray-300` | `#C7C7C7` | Divisores, bordas |
| `--gray-100` | `#F2F2F2` | Superfícies sutis, cards em fundo claro |
| `--white` | `#FFFFFF` | Fundo principal, texto em escuro |

**Regra de uso:** em qualquer tela/documento, usar no máximo duas das três cores {preto, branco, vermelho}. O vermelho nunca ocupa mais de ~30% da área — é acento, não fundo (exceto em placas de destaque isoladas).

- **Cor proibida:** gradientes coloridos, 3D, paletas fora do preto/branco/cinza/vermelho

---

## Tipografia

**Fonte:** Montserrat (Google Fonts)
- Títulos e destaques: Montserrat Black 900 (uppercase, letter-spacing negativo)
- Subtítulos: Montserrat ExtraBold 800 / Bold 700
- Corpo: Montserrat Regular 400 / Medium 500
- Eyebrows/labels: Montserrat SemiBold 600, uppercase, letter-spacing 0.22em, cor `#6B6B6B`
- Wordmark (logo texto): Montserrat Light 300, uppercase, letter-spacing 0.22em

**Escala:**
- H1: 56px / Black 900 / uppercase / ls -0.02em
- H2: 40px / ExtraBold 800
- H3: 32px / Bold 700
- Body: 18px / Regular 400 / cor `#3A3A3A`
- Caption: 13px / cor `#6B6B6B`
- Eyebrow: 12px / SemiBold 600 / uppercase / ls 0.22em / cor `#6B6B6B`

---

## Estilo geral

Visual editorial, minimalista e premium. Fundo branco com traços pretos. Estética de manual inteligente — não de banner de agência. Quando entrar cor, é o vermelho `#A91C20` como acento pontual, nunca como fundo dominante.

---

## Elementos-chave

- **Bordas:** 1px hairline `#C7C7C7` em claro, `rgba(255,255,255,0.14)` em escuro
- **Border-radius:** 0px como padrão (angular e firme). Máximo 4px em cards. Pills com `999px` apenas para tags/eyebrows
- **Botões:** fundo `#A91C20` com texto branco. Hover: `#6C0302`
- **Sombras:** mínimas ou nenhuma. Quando necessário: `0 1px 2px rgba(10,10,10,0.06)`
- **Foco:** outline 2px `#A91C20`, offset 2px

---

## Backgrounds (para slides/documentos de destaque)

Três tratamentos de fundo extraídos do deck oficial:
- **Dark low-poly:** `marca/Tatsuo Academy Design System/assets/bg-dark-lowpoly.png` — fundo escuro com textura facetada. Uso em títulos e declarações de impacto
- **Light chevron:** `marca/Tatsuo Academy Design System/assets/bg-light-chevron.png` — off-white com setas diagonais. Fundo padrão de slides de conteúdo
- **Red gradient:** `marca/Tatsuo Academy Design System/assets/bg-red-gradient.png` — vermelho com vinheta. Uso pontual para slides de destaque máximo

**Para documentos internos (relatórios, guias):** fundo branco `#FFFFFF`. Não usar backgrounds texturizados.

---

## O que NUNCA fazer

- Gradientes coloridos ou degradês
- 3D ou elementos de profundidade artificial
- Ícones prontos com estética de banco de imagem
- Paleta de cores fora do preto/branco/cinza/vermelho
- Visual "motivacional" ou "positivo" excessivo — a marca é firme, não festiva
- Emoji de qualquer tipo
- Exclamações ou perguntas retóricas no copy
- Fundo branco puro em slides (usar sempre uma das plates texturizadas)
- Visual genérico de palestra
- Arte infantil
- Recortes mal integrados na composição
- Aparência amadora

---

## Materiais e imagens conceituais

Quando fizer sentido, usar texturas de **pedra, metal, acrílico ou materiais nobres** — reforçam o tom premium e empresarial. Estilo masculino sem exagero, alto contraste.

Imagens conceituais que dialogam com o conteúdo da marca: empresário, piloto/F1, empresa como carro de corrida, estoque, fábrica, margem de contribuição.

---

## Peças já produzidas / solicitadas

Referência do tipo de material que a marca demanda (formatos e padrões já pedidos):
- Cordão de crachá para o Líderes do Amanhã
- Mockup de credencial premium
- Banner 10m × 0,5m
- Background 8000 × 400px
- Moldura A4 com logo Tatsuo texturizada
- Logo com textura de pedra na cor vinho `#8a1c19`
- Background premium com elementos de liderança

> **Nota de cor:** o material de marca (logo texturizada, peças premium) usa o vinho `#8a1c19`. O design system digital (telas, documentos, carrossel) usa o carmim `#A91C20`. São vermelhos próximos mas distintos — confirmar o contexto antes de aplicar.

---

## Logo

- **Versão padrão (claro):** `marca/Tatsuo Academy Design System/assets/logo-tatsuo-academy.png` — símbolo losango vermelho + wordmark "TATSUO ACADEMY". Usar em fundos brancos/claros
- **Versão on-dark:** `marca/Tatsuo Academy Design System/assets/logo-tatsuo-academy-on-dark.png` — para fundos escuros
- **Só símbolo:** `marca/Tatsuo Academy Design System/assets/logo-mark.png`
- **Versões alternativas (pasta raiz):** `marca/logo-bordo.png`, `marca/logo-preto.png`, `marca/logo-branco.png`
- **Espaço mínimo:** altura do "T" do wordmark em todos os lados
- **Tamanho mínimo:** 24px para o símbolo isolado; 120px de largura para o lockup completo
- **Posicionamento:** topo-esquerdo em títulos; rodapé-esquerdo (pequeno, ~40% opacidade) como marca d'água em conteúdo
- **Não recolorir.** Em fundo escuro, usar a versão on-dark

---

## Iconografia

- Sistema: **Lucide Icons** (CDN) — traço único, geometria limpa, sem floreios
- Stroke-width: 1.75–2 (padrão)
- Tamanhos: 16, 20, 24, 32, 48px
- Cor: `currentColor`
- Sem variantes preenchidas
- Ícone original do deck: `marca/Tatsuo Academy Design System/assets/icon-check-circle.png`

---

## Tom de voz

- Direto, pragmático, confrontacional-mas-respeitoso. Empresário falando com empresário
- Números acima de sensações: "menos achismo, mais leitura"
- Frases curtas. Ponto final. Sem enchimento
- Títulos em CAIXA ALTA para impacto
- Corpo em sentence case
- Sem emoji, sem exclamações, sem perguntas retóricas

---

## Perfil do autor

- **Nome:** Rodrigo Camacho
- **Handle:** *(adicionar handle de rede social se tiver)*
- **Foto:** *(adicionar caminho do arquivo quando disponível — ex: marca/foto-perfil.jpg)*

---

## CSS e tokens oficiais

Arquivo completo de variáveis CSS: `marca/Tatsuo Academy Design System/colors_and_type.css`
Componentes React e slide deck: `marca/Tatsuo Academy Design System/ui_kits/`
Preview visual do sistema: `marca/Tatsuo Academy Design System/preview/`
