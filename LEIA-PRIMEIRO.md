# Leia primeiro: a máquina de conteúdo do Hélio

Esta pasta é uma cópia da máquina de conteúdo que produz o Instagram do Hélio Tatsuo. Tudo o que se aprendeu em meses de produção está aqui dentro, nas skills (`.claude/skills/`). Você não precisa saber nada antes de começar: o Claude conhece o método e vai te guiar. O que você precisa é seguir o processo, ler o que ele mostrar e aprovar ou corrigir.

## O que você produz e com qual comando

| O que | Comando | Quando usar |
|---|---|---|
| Carrossel com imagem gerada (o carrossel principal) | `/carrossel` | Tema ou dor do empresário virando 10 a 16 slides. É o formato mais difícil: o texto sempre para pra sua aprovação antes de qualquer imagem. |
| Carrossel com fotos reais do Hélio | `/carrossel` (modelo fotos-reais) | História do Hélio, autoridade com números, "X coisas que eu ensinei hoje no MBV". |
| Carrossel educativo do MBV | `/carrossel` (modelo infográfico) | Conteúdo da apostila, no perfil da Tatsuo Academy. Sem /etiqueta e sem Manychat. |
| Frase do dia (imagem de IA) | `/frase` | Uma frase por dia, às 9h. É o formato mais consistente da casa. |
| Frase com foto do Hélio, ou manuscrita no papel ou no vidro | `/frase-foto` | Você escolhe a variante. |
| Ativar a automação do Manychat de um post | `/manychat` | Na hora em que o carrossel vai ao ar. Faça numa conversa só pra isso. |
| Caixinhas de pergunta dos stories | `/caixinhas` | Perguntas que o Hélio responde nos stories. |
| Ficha do post pra análise | `/etiqueta` | Logo depois de fechar cada carrossel ou frase. |
| Análise do dia | `/ritual` | Depois de importar o pacote de analytics do dia (ver abaixo). |
| Notícias quentes do dia | `/pautas` | Todo dia de manhã. |

## Como o trabalho flui

1. Você traz o tema, a dor ou a frase. Quanto mais concreto, melhor: "o dono que fatura milhões e não consegue tirar dinheiro" rende mais do que "lucratividade".
2. O Claude escreve o texto e para. **Você lê tudo, slide por slide, antes de aprovar.** É nessa hora que o carrossel ganha ou perde.
3. Aprovado o texto, ele monta os slides e gera as imagens.
4. Ele entrega os PNGs e a legenda na área de trabalho e abre pra você conferir.
5. Você posta e avisa o Claude ("postei às 14h"). Ele roda a /etiqueta e, se o post tiver palavra-chave, você abre uma conversa e roda o /manychat.

## O pacote de analytics

Esta máquina não acessa a API do Instagram (se duas máquinas acessarem, a Meta bloqueia). Todo dia você recebe um arquivo `pacote-AAAA-MM-DD.zip` com os dados brutos do dia. Para usar:

```bash
python scripts/pacote/importar_pacote.py ~/Downloads/pacote-AAAA-MM-DD.zip
```

Depois, rode `/ritual`. O Claude analisa os dados sozinho e te entrega o briefing.

## Onde ficam as coisas

- `conteudo/carrosseis/` : todos os carrosséis e frases já feitos, um por pasta, numerados em ordem de publicação.
- `~/Desktop/carrosseis claude/POSTADOS/` e `~/Desktop/frases claude/` : tudo o que já foi entregue e postado (inclusive os "claude 1" a "claude 13"). É aqui que se busca um post antigo pra repostar.
- `~/Desktop/fotos para carrosséis/` : o acervo de fotos reais do Hélio.
- `_contexto/` : o guia de voz e as transcrições do MBV (fonte obrigatória da voz do Hélio; material do treinamento pago, não compartilhar).
- `marca/design-guide.md` : cores, fontes e logo.
- `WINDOWS.md` : esta máquina é Windows; a tradução dos comandos de Mac das skills.

## Três regras que não se discutem

1. O Hélio nunca é gerado por IA. Só foto real dele.
2. A voz do Hélio é direta e ácida: aperta a dor do dono, não fica em frase bonita, não fala como coach.
3. Toda entrega fecha com commit e push no seu repositório.
