# Análise das "roupas" de conteúdo — pelo TEXTO REAL dos slides

> Gerada em 18/08/2026, a partir de 41 carrosséis produzidos no workspace e casados com as métricas
> da API (corpus em `corpus-carrosseis.json`). Classificação pelo gancho real (slides 1–2), não pela legenda.
> Origem: discussão sobre a hipótese "metáfora performa melhor" (conversa de 18/08).
>
> **Nota (29/08):** o corpus ganhou entradas com `"origem": "EXTERNO"` — posts do perfil que NÃO saíram
> do workspace, arquivados só como referência de texto. **Filtre por `origem` antes de recalcular
> qualquer mediana daqui**: as medianas desta página continuam sendo dos 41 carrosséis do workspace.

## Classes ("roupas")
- **metáfora** — batismo/imagem que renomeia a dor: "babá de adulto", "igreja", "cobertor curto"
- **fábula** — narrativa ilustrada FABULA (bicho empresário)
- **cena** — momento/quote reconhecível: "contratei um RH pra cultura", "aumentou o salário e ele saiu"
- **paradoxo** — inversão de expectativa: "cresceu e o bolso nem ficou sabendo"
- **direto** — tese/confronto sem roupa: "dono não tira o olho", "ninguém quer aprender gestão"

## Resultado (mediana por classe)

| roupa | n | mediana com | com/1k reach | melhor | pior |
|---|---|---|---|---|---|
| direto | 14 | 36 | 4,5 | parou-de-olhar (1.160) | protagonista-vitimista (2) |
| metáfora | 10 | 32 | 4,4 | **babá-de-adulto (2.943 🏆)** | **gol-contra (0)** |
| fábula | 3 | 32 | 5,0 | beija-flor (33) | toupeira (24) |
| paradoxo | 10 | 22 | 3,2 | quando-a-casa-cai (163) | modelo-maior (10) |
| cena | 4 | 14 | 2,0 | espelho-do-dono (25) | torcida-que-limpa (2) |

## Leituras

1. **Metáfora é a roupa de MAIOR VARIÂNCIA** — dona do recorde absoluto (2.943) e do zero absoluto (0) no mesmo grupo. Boom ou bust. Não é "melhor"; é a mais alavancada.
2. **Direto é o cavalo de trabalho** — mediana mais alta, nunca flopa feio, e também explode (1.160). A tese afiada sem roupa nenhuma segue sendo a base do perfil.
3. **O que separa a metáfora-recorde da metáfora-flop:** o MAPA. "Igreja" traduz sozinha (fiel→funcionário, pastor→líder, credo/rito/rotina→cultura): mapa 1:1, sem esforço do leitor. "Gol contra/juiz" exige decodificação (juiz=governo? gol contra=erro interno?) sobre nervo morno (culpar externos). **Critério prático: se a metáfora precisa ser explicada, ela não carrega o post.**
4. **Domínio identitário (fé, futebol) não basta por si** — futebol (gol-contra) flopou; igreja explodiu. A carga do domínio multiplica um mapa bom; não salva um mapa ruim.
5. ~~**Fábula** = melhor densidade de conversão (5,0 com/1k), teto de alcance baixo. Papel: meio de funil/salvamento, não topo.~~ → **CORRIGIDO em 31/08/2026, ver abaixo.** A metade "melhor densidade de conversão" se sustenta; a metade "teto de alcance baixo" está **falsificada**.
6. **Cena como roupa de conteúdo** rendeu pouco no corpus (nota: a "cena" forte do recordista estava na LEGENDA; o conteúdo era metáfora — legenda-cena + slide-metáfora pode ser o combo, não a cena sozinha).

## Regra de bolso pra próxima escolha
Nervo validado primeiro (gente/preparo/rito/dono-culpado) → depois a roupa:
- quer teto máximo e aceita variância → **metáfora com mapa 1:1** (teste: dá pra traduzir cada elemento sem explicar?)
- quer consistência → **direto**
- meio de funil/salvamento → **fábula** — *ressalva de 31/08: o "não topo" desta linha caiu junto com a leitura 5. A fábula converte bem E alcança (cavalo 05/06: 51 mil). Escolher fábula pelo nervo, não por posição de funil.*

## Limitações honestas
n pequeno por classe · classificação de um avaliador só · alcance depende do algoritmo (distribuição multiplicativa) · período misto (jul–ago/26). Re-rodar quando o corpus dobrar.

---

## Correção 31/08/2026 — a leitura 5 (fábula) caiu, e o cap que nasceu dela foi aposentado

> Autorizado pelo user em 31/08. O cap "fábula → `mediana` em taxa" saiu do `SKILL.md` da `/etiqueta`.

**O que estava errado.** A leitura 5 desta página foi medida em **comentários** sobre **n=3**, em 18/08. Em 27/08 a métrica-alvo do carrossel virou **interações/1k** e ninguém remediu a fábula na métrica nova. O cap sobreviveu à troca de régua por inércia.

**Os mesmos posts, agora em taxa (interações/1k):**

| fábula | data | reach | taxa |
|---|---|---|---|
| cavalo teimoso | 30/08/26 | 8.448 | **111,3** (top 10% do perfil) |
| cavalo força × modelo | 05/06/26 | **51.168** | **94,0** |
| sapo | 27/02/25 | 3.423 | 73,3 |
| papagaio | 23/08/26 | 5.303 | 71,8 |
| floresta (nariz no tronco) | 09/08/26 | 6.011 | 60,9 |
| floresta | 01/04/26 | 8.014 | 55,8 |
| pavão | 16/08/26 | 8.254 | 49,8 |

Mediana ~71 contra 60,9 do carrossel em geral. **Duas das sete passam do corte de `acima` (76,9); nenhuma cai na banda `abaixo`** — o piso da classe é ~50.

**"Teto de alcance baixo" é o pedaço mais errado.** O cavalo de junho alcançou **51 mil**, e o de agora, 8,4 mil com 224 compartilhamentos. A impressão de teto baixo veio de três fábulas de alcance pequeno num corpus de 41 — amostra, não propriedade do formato.

**Onde o cap custou caro:** ele forçou a previsão cega do carrossel 69 pra `mediana` (50–78) apesar do nervo forte (Cultura + devolver-a-culpa, que a própria régua diz que puxa pra cima). O post fez 111,3. Era a terceira vez que errava pra baixo — papagaio (previsto `mediana`, real 72,51) e o cavalo de junho já tinham avisado.

**A lição estrutural, que vale além da fábula:** *cap medido numa métrica não vale na métrica seguinte.* Quando a máquina troca a métrica-alvo, **todo cap vira hipótese até ser remedido**. Os três que sobraram — Lucratividade, frase nichada, espelho de advertência — nasceram todos antes ou durante a virada de 27/08 e **ainda não foram remedidos em taxa**. Vale a mesma auditoria.

**Limitação desta correção:** n=7, um avaliador só, classificação por legenda. Não é "fábula é a melhor roupa" — é "não há base pra tratar fábula como classe capada". Refazer quando o corpus de fábula dobrar.
