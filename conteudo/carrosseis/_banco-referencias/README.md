# Banco de Referências — Carrosséis Tatsuo Academy

Acervo de imagens que serve de **inspiração de estilo** quando a skill `/carrossel` gera fotos novas por IA (gpt-image-2). A IA **não reusa** essas imagens — ela copia o *look* (P&B editorial, desaturado, dramático, foto sangrando embaixo).

## Como usar

1. Jogue suas imagens de acervo nesta pasta (`.jpg` ou `.png`).
2. Peça pra eu **atualizar o catálogo** abaixo — eu descrevo cada imagem com tags.
3. Ao criar um carrossel, você **aponta** quais referências usar: *"usa a 03, 07 e 12"* ou *"usa as de cena-de-trabalho"*.
4. A skill passa essas imagens como referência pro gpt-image-2 gerar a foto de cada slide no mesmo estilo.

## Tags usadas no catálogo

- `cena-de-trabalho` — pessoas/profissionais em situação de trabalho
- `pessoa` — retrato ou figura humana isolada
- `multidao` — grupos, aglomeração
- `objeto-metafora` — objeto com carga simbólica (bandeja, chapéu de chef, martelo)
- `composicao-conceitual` — composição abstrata/conceitual
- `ambiente` — cenário, lugar, espaço sem foco em pessoa

## Fundos canônicos (arquivos fixos de layout, não são referência de estilo)

- `background para carrosséis.png` — linho off-white do **editorial-punch** (todos os slides usam o mesmo arquivo).
- `background infografico escuro.png` — fundo preto granulado com grade de cantos arredondados nas bordas, do modelo **infografico** (voz Tatsuo Academy, série da apostila). 1080×1350. Recriado em 26/09/2026 a partir dos posts de referência do user e aprovado por ele. Se faltar numa máquina, regerar idêntico com `python3 .claude/skills/carrossel/modelos/infografico/fundo/gen_fundo.py 7 "<destino>"`.

## Fundo das imagens 274-299 (recortes enviados pelo user)

Vêm em PNG 1080×1920. Ao **usar como recorte solto** no slide (não como referência de estilo pra IA, aí não importa), tratar o fundo assim:

- **Recorte transparente ou fundo branco** (a maioria): o `mix-blend-mode:multiply` do editorial já apaga branco/transparente contra o linho. **Não precisa fazer nada** — usar direto, cropar no alpha (`getbbox()`).
- **Fundo de cena embutido (céu/parede/estrada cinza):** o multiply NÃO apaga cinza. Nessas, **recortar o sujeito no alpha OU aplicar o fade pro linho** (`mask-image:linear-gradient(...)`, o mesmo das fotos que sangram). São: **276** (céu cinza), **287** (piso da sala), **288** (asfalto da estrada), **292** (parapeito de pedra). A **275** tem uma sombra/nuvem sobre fundo branco, mas isso é elemento do conceito (a sombra que fica), não ruído — manter.

## Catálogo

| Arquivo | Descrição | Tags | Espaço p/ texto |
|---|---|---|---|
| 1.png | Homem de costas manejando uma linha/corda fina que se estende até o chão | objeto-metafora, pessoa | topo/direita |
| 2.png | Duas mãos sustentando um cérebro humano suspenso no ar | objeto-metafora, composicao-conceitual | topo/esquerda |
| 3.png | Mão segurando uma lupa que revela um olho humano gigante | objeto-metafora, composicao-conceitual | topo/esquerda |
| 4.png | Menino antigo em pé, concentrado lendo um livro | pessoa | direita |
| 5.png | Colagem surreal: mulher recebe um jato colorido de palavras vindo da boca de outra pessoa | composicao-conceitual | topo/direita |
| 6.png | Vista de cima de uma máquina de escrever com duas mãos datilografando | objeto-metafora, cena-de-trabalho | topo |
| 7.png | Homem em poltrona escondido atrás de jornal estampado "THE END IS NEAR" | pessoa, objeto-metafora | topo |
| 8.png | Fone de telefone antigo pendurado pelo fio em espiral, no ar | objeto-metafora | direita/base |
| 9.png | Dois senhores sentados num muro lendo jornal e livro, sombras longas | pessoa, ambiente | topo/direita |
| 10.png | Homem subindo uma escada em espiral íngreme na diagonal | pessoa, composicao-conceitual | base/direita |
| 11.png | Homem de terno deitado dormindo sobre uma nuvem flutuante | composicao-conceitual, pessoa | topo |
| 12.png | Homem de terno trabalhando no computador com uma pedra enorme no lugar da cabeça | composicao-conceitual, cena-de-trabalho | topo/direita |
| 13.png | Homem de terno correndo curvado carregando um relógio de bolso gigante nas costas | objeto-metafora, pessoa | topo/direita |
| 14.png | Homem de terno com um despertador no lugar da cabeça, olhando o relógio de pulso | composicao-conceitual, objeto-metafora | direita |
| 15.png | Executivo de terno com óculos VR/luz nos olhos segurando caderno e caneta | pessoa, cena-de-trabalho | topo/direita |
| 16.png | Orador antigo num púlpito de braços abertos diante de uma multidão de chapéus | multidao, cena-de-trabalho | topo |
| 17.png | Homem de terno deitado no chão, recostado, apontando a mão para cima | pessoa | topo/direita |
| 18.png | Figura escura de sobretudo com a mão estendida em primeiro plano | pessoa, composicao-conceitual | topo/direita |
| 19.png | Palestrante num palco escuro com braço erguido diante de plateia iluminada | multidao, cena-de-trabalho | topo |
| 20.png | Mão segurando um martelo de juiz (gavel) | objeto-metafora | topo/esquerda |
| 21.png | Homem de terno olhando por um binóculo, expressão de busca | pessoa, objeto-metafora | direita |
| 22.png | Mão idosa segurando um relógio de bolso aberto pendurado pela corrente | objeto-metafora | direita |
| 23.png | Homem de terno puxando com esforço uma âncora pesada presa por corda | objeto-metafora, pessoa | topo |
| 24.png | Retrato de homem feito de peças de quebra-cabeça, uma peça solta no rosto | composicao-conceitual, pessoa | topo/direita |
| 25.png | Time de rugby em roda (huddle) num campo ao lado da trave, neblina | multidao, ambiente | topo |
| 26.png | Figura pequena e solitária sentada de costas num banco, muito espaço vazio | pessoa, ambiente | topo |
| 27.png | Mão segurando uma seta vermelha apontando para baixo (queda) | objeto-metafora | topo |
| 28.png | Homem de terno pensativo sentado a uma mesa, mão no queixo | pessoa, cena-de-trabalho | topo/esquerda |
| 29.png | Retrato de homem de bigode marcante (estilo Dalí), olhar fixo | pessoa | direita |
| 30.png | Mão empilhando blocos/cubos feitos de notas de dinheiro | objeto-metafora | topo/esquerda |
| 31.png | Boxeador encostado nas cordas do ringue, cabeça baixa | pessoa, ambiente | topo/direita |
| 32.png | Equilibrista andando numa corda bamba esticada, braço erguido | pessoa, composicao-conceitual | base |
| 33.png | Homem de terno curvado com maleta e uma chave de corda gigante nas costas | composicao-conceitual, objeto-metafora | topo |
| 34.png | Estrada de asfalto sinuosa que serpenteia até o horizonte | ambiente, objeto-metafora | topo/direita |
| 35.png | Mão idosa com dedo indicador apontando para cima | objeto-metafora | topo/direita |
| 36.png | Homem de smoking sentado em poltrona com uma lâmpada no lugar da cabeça | composicao-conceitual, objeto-metafora | topo/direita |
| 37.png | Prédio em escombros/desabando, ruína de concreto | ambiente, objeto-metafora | topo/esquerda |
| 38.png | Pessoa sentada segurando jornal/cartaz escrito "THINK BIGGER." | pessoa, objeto-metafora | topo/direita |
| 39.png | Homem de terno listrado (estilo Wolf of Wall Street) apontando para cima e para a esquerda | pessoa | topo/direita |
| 40.png | Homem de terno pensativo, punho na boca, olhar baixo | pessoa | topo/direita |
| 41.png | Homem de terno listrado aplaudindo com expressão de aprovação | pessoa | topo/direita |
| 42.png | Homem de terno sorrindo discreto, sentado e recostado, tom claro | pessoa | topo/esquerda |
| 43.png | Ilustração de homem de terno largado numa cadeira com revista cobrindo o rosto | pessoa, composicao-conceitual | topo/direita |
| 44.png | Silhueta em alto contraste de homem de terno pensativo, mão no queixo | pessoa | topo/esquerda |
| 45.png | Vista de cima de um homem de terno parado, cabeça baixa | pessoa, composicao-conceitual | topo |
| 46.png | Homem idoso de terno em pé com a cabeça inclinada bem para trás, olhando o alto | pessoa | topo/esquerda |
| 47.png | Homem encolhido deitado no chão em posição fetal, abraçando a cabeça | pessoa | topo/direita |
| 48.png | Mãos com luvas erguendo notas de dinheiro empilhadas como tijolos/parede | objeto-metafora | topo/direita |
| 49.png | Homem careca sentado à mesa com a cabeça nas mãos, papéis/contas espalhados | pessoa, cena-de-trabalho | topo/direita |
| 50.png | Retrato de homem de óculos fumando um cigarro, olhar de lado | pessoa | topo/direita |
| 51.png | Pessoa derrubada com a cabeça apoiada numa mesa de toalha branca, cadeira ao lado | pessoa, ambiente | topo/esquerda |
| 52.png | Mão erguida segurando um maço de notas de dinheiro | objeto-metafora | topo |
| 53.png | Chimpanzé de terno xadrez ao telefone numa mesa de escritório (humor) | composicao-conceitual, cena-de-trabalho | topo/direita |
| 54.png | Empresário de costas encarando uma fileira de figuras idênticas sem rosto (conformidade) | pessoa, composicao-conceitual | topo |
| 55.png | Massa de empresários idênticos aplaudindo em uníssono (yes-men) | multidao, composicao-conceitual | topo |
| 56.png | Empresário nítido erguendo a mão, destacando-se de uma massa sem rosto | pessoa, composicao-conceitual | topo |
| 57.png | Chefe autoritário apontando e gritando para um liderado encolhido no chão | pessoa, composicao-conceitual | topo |
| 58.png | Homem de costas encarando o próprio reflexo pensativo no espelho | pessoa, composicao-conceitual | topo |
| 59.png | Empresário subindo uma escada ascendente (crescimento/oportunidade) | pessoa, objeto-metafora | topo |
| 60.png | Empresário no fim do mês encarando confuso um relatório na mesa | pessoa, cena-de-trabalho | topo |
| 61.png | Empresário dando de ombros enquanto pergunta a outro (contador) | pessoa, cena-de-trabalho | topo |
| 62.png | Empresário vendado decidindo no escuro, mãos estendidas | pessoa, composicao-conceitual | topo |
| 63.png | Empresário perdido encarando uma página cheia de números | pessoa, cena-de-trabalho | topo |
| 64.png | Empresário firme de braços cruzados, no comando | pessoa | topo |
| 65.png | Empresário apontando pra frente segurando um relatório | pessoa | topo |
| 66.png | Homem de costas na amurada de um navio olhando o mar (solidão do comando) | pessoa, ambiente | topo |
| 67.png | Homem carregando um barco nas costas enquanto o grupo vai embora | pessoa, composicao-conceitual | topo |
| 68.png | Perfil de homem tenso segurando o leme de um navio (à esquerda) | pessoa, objeto-metafora | topo/direita |
| 69.png | Homem sozinho num pequeno barco no mar revolto (ampliado) | pessoa, ambiente | topo |
| 70.png | Capitão de boné no timão, sereno, olhando o horizonte (à direita) | pessoa, objeto-metafora | topo/esquerda |
| 71.png | Figura solitária no cume de uma montanha nevada | pessoa, ambiente | topo |
| 72.png | Homem de terno escalando uma face rochosa íngreme (à direita) | pessoa, ambiente | topo/esquerda |
| 73.png | Homem de terno se puxando com esforço sobre uma rocha | pessoa, ambiente | topo |
| 74.png | Homem de terno relaxado na beira de um penhasco (conforto/risco) | pessoa, ambiente | topo/direita |
| 75.png | Equilibrista de terno na corda bamba, braços abertos | pessoa, composicao-conceitual | topo |
| 76.png | Alpinista de terno subindo encosta de neve com picareta | pessoa, ambiente | topo/direita |
| 77.png | Livro-razão antigo aberto com colunas de números e óculos de leitura sobre ele, na mesa | objeto-metafora, ambiente | topo |
| 78.png | Homem de terno vintage lendo um jornal financeiro sentado num café, parede clara ao fundo | pessoa, ambiente | topo |
| 79.png | Mãos passando um livro-razão manuscrito por cima da mesa para outra pessoa | objeto-metafora, cena-de-trabalho | topo |
| 80.png | Cadeira de couro vazia à cabeceira de uma mesa de reunião, figuras borradas ao fundo | ambiente, objeto-metafora | topo |
| 81.png | Homem de sobretudo caminhando de costas para dentro da neblina numa estrada vazia | pessoa, ambiente | topo/direita |
| 82.png | Ábaco de madeira ao lado de livro-razão aberto sob luminária de banqueiro | objeto-metafora, ambiente | topo |
| 83.png | Dois homens de terno numa mesa, um sussurrando no ouvido do outro (intérprete) | pessoa, cena-de-trabalho | topo |
| 84.png | Livro-razão aberto iluminado por luminária de banqueiro, óculos de leitura ao lado | objeto-metafora, ambiente | topo |
| 85.png | Jogador de futebol sozinho de costas, camisa nº 10, saindo de campo cabisbaixo num estádio vazio (derrota) | pessoa, ambiente | topo |
| 86.png | Jogador de futebol de joelhos no gramado, rosto nas mãos, chorando sozinho (luto/derrota) | pessoa, ambiente | topo |
| 87.png | Atacante com as mãos na cabeça após perder o gol feito, gol vazio ao lado (chance perdida) | pessoa, ambiente | topo |
| 88.png | Atacante de braços abertos comemorando frio diante de arquibancada lotada em êxtase | pessoa, multidao | topo |
| 89.png | Gol de futebol vazio com a rede, visto de frente, estádio deserto (o gol que não vem) | objeto-metafora, ambiente | topo |
| 90.png | Barreira de jogadores enfileirada de lado numa cobrança de falta, goleiro postado atrás (defesa) | multidao, ambiente | topo |
| 91.png | Goleiro postado no centro do gol, pronto pra defender, torcida ao fundo (guardar o gol) | pessoa, ambiente | topo |
| 92.png | Arquibancada deserta e degraus vazios após o jogo, figura solitária sentada (queda/vazio) | ambiente, pessoa | topo |
| 93.png | Taça da Copa do Mundo sozinha no gramado de um estádio vazio (troféu/campeonato) | objeto-metafora, ambiente | topo |
| 94.png | Time de futebol enfileirado de braços dados antes do jogo, torcida ao fundo (união/disciplina) | multidao, ambiente | topo |
| 95.png | Corredor solitário em disparada numa pista de atletismo vazia ao amanhecer, respiração no ar frio (fome/impulso) | pessoa, ambiente | topo |
| 96.png | Atleta premiado sentado no banco do vestiário, medalhas no pescoço, olhar desligado e acomodado (talento sem fome) | pessoa, ambiente | topo |
| 97.png | Boxeador sozinho enfaixando as mãos num ginásio vazio, cabeça baixa (o trabalho invisível) | pessoa, ambiente | topo |
| 98.png | Atleta empurrando um trenó de treino pesado num campo vazio ao amanhecer, névoa (esforço que ninguém pediu) | pessoa, ambiente | topo |
| 99.png | Treinador de costas diante de uma fileira de atletas perfilados num campo (o líder escolhendo) | multidao, cena-de-trabalho | topo |
| 100.png | Treinador com a mão no ombro de um atleta exausto e curvado, encorajando de perto (acender a fome um a um) | pessoa, cena-de-trabalho | topo |
| 101.png | Equipe de remo de oito puxando em sincronia perfeita na água calma (time em uníssono) | multidao, ambiente | topo |
| 102.png | Treinador à frente com o braço erguido, time de atletas disparando atrás dele num campo (construir o time faminto) | multidao, cena-de-trabalho | topo |
| 103.png | Pescador solitário lançando a rede sobre o mar calmo ao amanhecer, de barco (buscar o cliente) | pessoa, ambiente | topo |
| 104.png | Mãos e braços de um pescador puxando uma rede pesada pra dentro do barco (a venda que se comemora) | pessoa, cena-de-trabalho | topo/direita |
| 105.png | Rede subindo cheia de tranqueira (bota, pneu, lata, entulho) em vez de peixe (a captura que custa) | objeto-metafora, cena-de-trabalho | topo |
| 106.png | Convés de barco tomado de entulho e rede embolada, sem espaço (o cliente errado consumindo a estrutura) | objeto-metafora, ambiente | topo |
| 107.png | Pescador cansado, de costas, lançando uma rede ainda maior ao mar (a teimosia de pescar mais) | pessoa, ambiente | topo |
| 108.png | Mãos do pescador separando a captura no convés e jogando de volta ao mar o que não presta (escolher quem fica) | pessoa, cena-de-trabalho | topo |
| 109.png | Pescador esgotado, curvado na beira do barco, entulho atrás (trabalha muito e sobra pouco) | pessoa, ambiente | topo/direita |
| 110.png | Mãos segurando um cesto com dois peixes grandes contra o mar (menos quantidade, mais qualidade) | objeto-metafora, cena-de-trabalho | topo |
| 111.png | Mãos tirando os peixes podres de um cesto e guardando só os bons (limpar o cesto) | objeto-metafora, cena-de-trabalho | topo |
| 112.png | Pescador sentado remendando e conferindo a malha da rede antes de sair (critério antes da venda) | pessoa, cena-de-trabalho | topo |
| 113.png | Barco de pesca firme rumo ao horizonte aberto (o cliente certo) | ambiente, objeto-metafora | topo |
| 114.png | Rei coroado sentado no trono numa catedral gótica enevoada (empresa não é democracia — capa) | pessoa, ambiente | topo |
| 115.png | Manopla/luva real aberta com a palma pra cima no braço do trono (não é ditador, ouve) | objeto-metafora | topo |
| 116.png | Rei à cabeceira de uma mesa redonda de conselho cercado de conselheiros (a opinião dos outros) | multidao, ambiente | topo |
| 117.png | Rei sozinho sob um facho de luz no trono, corte em sombra (uma pessoa só responde) | pessoa, ambiente | topo |
| 118.png | Coroa real erguida em duas mãos, still-life dramático (o peso da decisão) | objeto-metafora | topo |
| 119.png | Aperto de mãos: mão real com anel + mão calejada do povo (escutar a ponta/operação) | objeto-metafora | topo |
| 120.png | Mão selando um decreto com anel-sinete, vela e pergaminho (bater o martelo sozinho) | objeto-metafora, cena-de-trabalho | topo |
| 121.png | Decreto sem assinar com pena parada e vela baixa (medo de decidir) | objeto-metafora | topo |
| 122.png | Trono vazio com a coroa largada no assento, catedral enevoada (abrir mão de comandar) | ambiente, objeto-metafora | topo |
| 123.png | Mão marcando com o dedo uma rota num mapa antigo do reino (direção — "é por aqui") | objeto-metafora, cena-de-trabalho | topo |
| 124.png | Rei à frente conduzindo exército e povo diante do castelo (puxa o barco, aponta o rumo) | multidao, pessoa | topo |
| 125.png | Castelo em construção com pedreiros e artesãos trabalhando (potencial virando resultado) | ambiente, multidao | topo |
| 126.png | Close na mão firme empunhando o cetro real (decide sozinho) | objeto-metafora | topo |
| 127.png | Mão desembainhando uma espada real no facho de luz (coragem de bater o martelo) | objeto-metafora | topo |
| 128.png | Rei de pé com coroa e cetro comandando o grande salão, corte ao redor (CTA — comando com direção) | pessoa, multidao | topo |
| 129.png | Lanterna acesa isolada no escuro, luz quente contra a escuridão (o número certo ilumina — capa "O número errado") | objeto-metafora | topo |
| 130.png | Livro-caixa antigo fechado sobre uma mesa (o número que ninguém abre) | objeto-metafora | topo |
| 131.png | Carimbo fiscal batendo em documento antigo, tinta borrada (o número que serve ao governo) | objeto-metafora | topo |
| 132.png | Estrada de terra se bifurcando em dois caminhos na neblina (os dois mundos do número) | ambiente | topo |
| 133.png | Mão assinando documento fiscal com caneta-tinteiro (o número que fecha com o fisco) | objeto-metafora, cena-de-trabalho | topo |
| 134.png | Cofre de ferro antigo trancado num chão de madeira (o número obrigatório, guardado) | objeto-metafora | topo |
| 135.png | Dono visto de costas, cabeça baixa sobre mesa cheia de papéis (decidir com o número errado) | pessoa, cena-de-trabalho | topo |
| 136.png | Mapa de papel rasgado ao meio sobre uma mesa (o número que não é seu) | objeto-metafora | topo |
| 137.png | Bússola antiga de latão com agulha travada (o número que aponta a decisão) | objeto-metafora | topo |
| 138.png | Mãos contando notas de dinheiro sobre um balcão (o número que sobra de verdade) | objeto-metafora, cena-de-trabalho | topo |
| 139.png | Balança de latão antiga sobre uma mesa (pesar o que fica bonito x o que é verdade) | objeto-metafora | topo |
| 140.png | Dois caminhos de terra convergindo em um só (o número que comanda a empresa) | ambiente | topo |
| 141.png | Livro-caixa antigo aberto com luz entrando pelas páginas (a ponte com o método: DRE contábil x gerencial) | objeto-metafora | topo |
| 142.png | Porta de madeira entreaberta com luz vazando pra dentro do escuro (parar de tocar no escuro) | ambiente, objeto-metafora | topo |
| 143.png | Mão erguendo uma lanterna acesa iluminando o caminho à frente (CTA — o número que comanda) | objeto-metafora, pessoa | topo |
| 144.png | Portão de fábrica ao amanhecer com uma silhueta solitária diante dele (dono pequeno não sai da operação — capa) | pessoa, ambiente | topo |
| 145.png | Cadeira de praia vazia e desfocada ao longe (a promessa da empresa que roda sozinha) | ambiente | topo |
| 146.png | Escritório de vidro isolado com vista de cima da fábrica (a utopia de administrar de longe) | ambiente, cena-de-trabalho | topo |
| 147.png | Planta industrial vazia estendida sobre uma mesa (não existe empresa autogerenciável) | objeto-metafora, cena-de-trabalho | topo |
| 148.png | Mãos passando uma ferramenta de uma pessoa pra outra (delegar tarefa é obrigação) | pessoa, cena-de-trabalho | topo |
| 149.png | Bota de trabalho gasta largada no chão de fábrica (o tato da operação) | objeto-metafora, ambiente | topo |
| 150.png | Mão tocando uma engrenagem em movimento, sentindo a vibração (sentir a ponta) | objeto-metafora, cena-de-trabalho | topo |
| 151.png | Multidão de trabalhadores borrada ao fundo com uma figura parada em foco (perder o comando) | multidao, pessoa | topo |
| 152.png | Duas portas lado a lado, uma fechada e outra entreaberta (os dois jeitos de se afastar) | ambiente, objeto-metafora | topo |
| 153.png | Escritório visto através de vidro fosco, cadeira vazia de costas (trancado no escritório) | ambiente, cena-de-trabalho | topo |
| 154.png | Mãos empurrando um caixote de madeira pesado pra fora do quadro (terceirizar a responsabilidade) | pessoa, objeto-metafora | topo |
| 155.png | Chave grande de ferro passando de uma mão pra outra (passar a tarefa, não o comando) | objeto-metafora, pessoa | topo |
| 156.png | Sala vazia com uma cadeira de comando iluminada de cima (o dia que você saiu do jogo) | ambiente, objeto-metafora | topo |
| 157.png | Relógio de bolso antigo parado sobre uma bancada de trabalho (perdeu o tesão pela operação) | objeto-metafora | topo |
| 158.png | Portão de fábrica se fechando ao entardecer (sair da operação é o começo do fim) | ambiente | topo |
| 159.png | Mão girando uma engrenagem em movimento, luz forte (CTA — manter o comando) | objeto-metafora, cena-de-trabalho | topo |
| 160.png | Corredor solitário visto de costas subindo uma estrada íngreme ao amanhecer (por que ele, e não eu — capa) | pessoa, ambiente | topo |
| 161.png | Mãos amarrando uma bota de trabalho gasta antes do amanhecer (a troca que ninguém vê) | pessoa, objeto-metafora | topo |
| 162.png | Mão segurando um galho espinhoso com força, apesar da dor (a escolha difícil) | objeto-metafora, pessoa | topo |
| 163.png | Figura solitária trabalhando à noite numa bancada, luz de lampião (enquanto uns descansavam) | pessoa, cena-de-trabalho | topo |
| 164.png | Trabalhador exausto sentado no chão da oficina, cabeça baixa (pagando o preço) | pessoa, cena-de-trabalho | topo |
| 165.png | Pantufas deixadas na porta enquanto botas de trabalho partem pro escuro (a vida confortável que se troca) | objeto-metafora | topo |
| 166.png | Tocha acesa erguida sozinha no escuro (nem todo mundo no topo é protagonista) | objeto-metafora | topo |
| 167.png | Poltrona de couro antiga, intocada, num escritório grande (o negócio herdado pronto) | objeto-metafora, ambiente | topo |
| 168.png | Homem de terno discursando num púlpito de uma sala de conferência chique, visto de trás da plateia (a palestra sobre sucesso) | pessoa, cena-de-trabalho | topo |
| 169.png | Mãos limpas e macias, sem calo, apoiadas numa mesa cara (não pagou o preço de nada) | objeto-metafora, pessoa | topo |
| 170.png | Retrato de família antigo na parede, mãos próximas à moldura (herdeiro de um protagonista) | pessoa, ambiente | topo |
| 171.png | O mesmo retrato de família antigo, em outro ângulo (gastando o troco de quem veio antes) | pessoa, ambiente | topo |
| 172.png | Relógio de bolso herdado sobre uma almofada de veludo (quem pagou x quem herdou) | objeto-metafora | topo |
| 173.png | Encruzilhada vazia ao entardecer, um caminho sumindo na neblina (a herança que não vem) | ambiente | topo |
| 174.png | Mãos passando uma tocha acesa de uma pra outra (CTA — construir a própria história) | pessoa, objeto-metafora | topo |
| 175.png | Ampulheta antiga com a areia quase no fim, luz dramática (o que empurra empresa boa pro desespero — capa) | objeto-metafora | topo |
| 176.png | Folha de calendário de parede antiga com datas circuladas a tinta (pagar antes de receber) | objeto-metafora | topo |
| 177.png | Carteira de couro quase vazia com moedas caindo (o aperto que não acaba) | objeto-metafora | topo |
| 178.png | Cano velho vazando, água pingando num ralo (o ciclo financeiro negativo) | objeto-metafora, ambiente | topo |
| 179.png | Mão assinando um contrato de empréstimo num balcão de banco (correr atrás de dinheiro) | pessoa, cena-de-trabalho | topo |
| 180.png | Pilha de documentos de empréstimo com um mostrador de taxa de juros em cima (cheque especial, juro caro) | objeto-metafora | topo |
| 181.png | Mãos exaustas segurando a gaveta vazia de uma caixa registradora (pagando pra trabalhar) | pessoa, cena-de-trabalho | topo |
| 182.png | Duas cordas separadas sendo amarradas uma na outra (mexer nos prazos dos dois lados) | objeto-metafora | topo |
| 183.png | Aperto de mãos sobre uma mesa com documentos (negociar prazo com o fornecedor) | pessoa, cena-de-trabalho | topo |
| 184.png | Mãos contando moedas rapidamente sobre um balcão (receber mais rápido) | pessoa, objeto-metafora | topo |
| 185.png | Mão soltando moedas que caem de uma palma pra outra (diminuir o prazo do cliente) | objeto-metafora | topo |
| 186.png | Duas mãos se aproximando, quase se tocando (as duas pontas se encostando) | pessoa, composicao-conceitual | topo |
| 187.png | Livro-caixa antigo com duas colunas e uma balança ao lado (a ponte com PMR e PMP) | objeto-metafora | topo |
| 188.png | Ponte estreita de madeira ligando dois penhascos ao entardecer (tirar a empresa do sufoco) | ambiente | topo |
| 189.png | Ampulheta virada, areia escoando cheia e constante (CTA — equilibrar o ciclo financeiro) | objeto-metafora | topo |
| 190.png | Homem caído exausto sobre a mesa à noite, cercado de notas fiscais espalhadas, luminária acesa (continuar vendendo pode matar a empresa — capa) | pessoa, cena-de-trabalho | topo |
| 191.png | Esteira de fábrica correndo vazia, sem produto (venda é movimento, não crescimento) | objeto-metafora, ambiente | topo |
| 192.png | Engrenagens de ferro girando rápido, em close (vender ≠ crescer) | objeto-metafora | topo |
| 193.png | Cata-vento de metal girando ao vento (movimento comercial) | objeto-metafora | topo |
| 194.png | Uma semente virando muda pequena com raízes visíveis abaixo do solo, corte transversal (crescimento real, por dentro) | objeto-metafora, composicao-conceitual | topo |
| 195.png | Pote de vidro enchendo de moedas, gota a gota (dividendo é o que fica dentro) | objeto-metafora | topo |
| 196.png | Mãos cansadas segurando a borda de uma bancada de trabalho (vendendo e trabalhando demais) | pessoa, cena-de-trabalho | topo |
| 197.png | Cofrinho virado de cabeça pra baixo sem nada caindo (não sobra dividendo pro dono) | objeto-metafora | topo |
| 198.png | Balança antiga de latão pesando moedas (a venda deixa dinheiro ou só gira) | objeto-metafora | topo |
| 199.png | Lupa sobre uma pilha de moedas (tem margem? dá lucro?) | objeto-metafora | topo |
| 200.png | Superfície polida e brilhante com uma rachadura revelando o interior (o disfarce mais perigoso) | composicao-conceitual | topo |
| 201.png | Raízes crescendo profundas sob uma pequena planta (movimento cansa, dividendo constrói) | objeto-metafora, composicao-conceitual | topo |
| 202.png | Livro-caixa antigo com uma fórmula escrita entre duas colunas, lápis em cima (a ponte com margem de contribuição) | objeto-metafora | topo |
| 203.png | Árvore firme e parada, raízes profundas visíveis na base, folhas caídas passando ao lado (dividendo constrói) | ambiente, objeto-metafora | topo |
| 204.png | Pote de vidro cheio de moedas, luz forte (CTA — faturamento em dividendo de verdade) | objeto-metafora | topo |
| 205.png | Uma única linha de pegadas retas cruzando a neve intocada, outras dispersas ao redor (quando foi a última vez que quis algo de verdade — capa) | pessoa, ambiente | topo |
| 206.png | Megafone antigo abandonado numa mesa, empoeirado, sem uso (todo empresário diz que quer crescer) | objeto-metafora | topo |
| 207.png | Calendário de parede antigo com a mesma meta escrita à mão, circulada, em anos empilhados (a mesma frase há cinco anos) | objeto-metafora | topo |
| 208.png | Vitrine de loja vazia ao entardecer, reflexo fraco no vidro (vontade de vitrine não muda calendário) | ambiente | topo |
| 209.png | Bússola de latão travada apontando firme numa direção (o que vai ser preciso) | objeto-metafora | topo |
| 210.png | Vela queimando intensa, cera escorrendo rápido (dedicação máxima sem depender de motivação) | objeto-metafora | topo |
| 211.png | Luvas de boxe antigas de couro penduradas num gancho na parede da academia (o cartel invicto) | objeto-metafora | topo |
| 212.png | Canto de ringue de boxe vazio, cordas esticadas, luz dramática (quem quer de verdade, vence sempre) | ambiente, objeto-metafora | topo |
| 213.png | Faca cortando através de cipós emaranhados (o preço do cartel invicto) | objeto-metafora | topo |
| 214.png | Caminho estreito e limpo cortando uma floresta densa (foco é cortar o que não é aquilo) | ambiente | topo |
| 215.png | Luz do amanhecer batendo numa estrada reta (CTA — dedicação real) | ambiente | topo |
| 216.png | Várias mãos diferentes empilhadas no centro, ângulo baixo (liderar não é mandar, é unir — capa) | pessoa, composicao-conceitual | topo |
| 217.png | Ferramentas antigas variadas e desencontradas sobre uma bancada (gente completamente diferente) | objeto-metafora | topo |
| 218.png | Várias cordas separadas sendo trançadas numa só (unir num único objetivo) | objeto-metafora | topo |
| 219.png | Pincel de caligrafia japonesa antigo sobre um tinteiro de pedra (a palavra itaidoshin) | objeto-metafora | topo |
| 220.png | Várias mãos diferentes juntas em círculo, palmas sobrepostas (não é uniformizar, é unidade) | pessoa, composicao-conceitual | topo |
| 221.png | Vários barcos pequenos convergindo pra um único ponto na água (o verdadeiro teste da liderança) | ambiente, composicao-conceitual | topo |
| 222.png | Peças de quebra-cabeça espalhadas, uma peça isolada se afastando (puxar pro seu lado) | objeto-metafora | topo |
| 223.png | Grande mecanismo de engrenagens desencontradas girando suavemente juntas (o objetivo virando de dentro) | objeto-metafora, composicao-conceitual | topo |
| 224.png | Várias tochas separadas se encontrando numa única chama central (itaidoshin não acontece por acaso) | objeto-metafora | topo |
| 225.png | Várias mãos empilhadas, erguidas, luz forte por cima (CTA — unir o time num único itaidoshin) | pessoa, composicao-conceitual | topo |
| 226.png | Farol firme numa tempestade, ondas quebrando na base (líder forte incomoda gente fraca — capa) | ambiente | topo |
| 227.png | Multidão amontoada buscando abrigo, borrada, uma figura em pé separada (poucos preparados pra crescer) | multidao, pessoa | topo |
| 228.png | Uma árvore só, ereta, enquanto as outras se curvam no vento (desconforto x toxicidade) | ambiente | topo |
| 229.png | Três chaves de ferro antigas de tamanhos diferentes penduradas numa parede de madeira (os três tipos de líder) | objeto-metafora | topo |
| 230.png | Bigorna recebendo um golpe de martelo, faíscas (feedback direto, sem teatro) | objeto-metafora, cena-de-trabalho | topo |
| 231.png | Mãos firmes de cirurgião fazendo um trabalho preciso, calmas e focadas (corrige e segue trabalhando) | pessoa, cena-de-trabalho | topo |
| 232.png | Corda esticada sob tensão, sem arrebentar (não alimentar vitimismo) | objeto-metafora | topo |
| 233.png | Mão protetora pairando gentilmente acima de uma planta pequena, sem tocar (passar a mão destrói o potencial) | objeto-metafora, composicao-conceitual | topo |
| 234.png | Pico de montanha imóvel, nuvens de tempestade girando abaixo (padrão alto sob pressão) | ambiente | topo |
| 235.png | Dois homens de costas um pro outro, um ereto e rígido, outro curvado, luz dura de tempestade (fracos abaixam, fortes ficam firmes) | pessoa, composicao-conceitual | topo |
| 236.png | Um único holofote iluminando um palco vazio, sem sombras pra esconder (expõe quem vive de desculpa) | ambiente, composicao-conceitual | topo |
| 237.png | Martelo de juiz firme sobre um bloco de madeira (chamar liderança firme de arrogância) | objeto-metafora | topo |
| 238.png | Facho de farol cortando a neblina, à noite (respeitado em silêncio) | ambiente | topo |
| 239.png | Sol rompendo as nuvens de tempestade sobre o farol firme (CTA — liderar firme sem pedir desculpa) | ambiente | topo |
| 240.png | Homem de mangas curvado sobre uma bancada soterrada de papéis sob uma luminária, trabalho sem glamour (gerada IA — capa "ninguém quer gestão") | pessoa, cena-de-trabalho | topo |
| 241.png | Bebê lambuzado de comida, rindo, macacão sujo, sentado (gerada IA — criança faz o que quer / caos) | pessoa | topo |
| 242.png | Senhor de meia-idade de terno, rosto marcado, olhar sério e resoluto, retrato (gerada IA — adulto responsável) | pessoa | topo |
| 243.png | Empresário próspero de terno segurando um leque de cédulas, satisfeito, cidade ao fundo (gerada IA — empresa nasceu pra te deixar rico) | pessoa | topo |
| 244.png | Fachada monumental de prédio clássico com colunas, imponente vista de baixo (gerada IA — de fora parece um império) | ambiente, objeto-metafora | topo |
| 245.png | Bolso de calça virado do avesso, vazio, uma última moeda caindo (gerada IA — no bolso cai só respingo) | objeto-metafora | topo |
| 246.png | Homem de terno correndo numa esteira, parado no lugar (gerada IA — faturar mais sem sair do lugar) | pessoa, composicao-conceitual | topo |
| 247.png | Duas mãos lado a lado, cada uma com o mesmo pequeno maço de dinheiro (gerada IA — mesmos 30 mil no bolso) | objeto-metafora | topo |
| 248.png | Casinha minúscula ao lado de um complexo fabril colossal, contraste de escala (gerada IA — 1 milhão x 10 milhões) | ambiente | topo |
| 249.png | Homem curvado e esmagado sob uma carga enorme nas costas (gerada IA — dez vezes mais pesada) | pessoa, objeto-metafora | topo |
| 250.png | Empresário com as mãos na cabeça, aflito, cercado por engrenagens e máquinas caóticas (gerada IA — mais coisa pra dar errado) | pessoa, cena-de-trabalho | topo |
| 251.png | Mão aberta com areia escorrendo por entre os dedos sobre chão vazio (gerada IA — faturamento é o que passa pela mão) | objeto-metafora | topo |
| 252.png | Mão despejando areia e, embaixo, uma duna imensa de areia derramada no chão (gerada IA — a riqueza que vazou pelos dedos) | objeto-metafora, composicao-conceitual | topo |
| 253.png | Homem pequeno de costas diante de um monumento colossal e vazio, admirando (gerada IA — o ego do número grande) | pessoa, composicao-conceitual | topo |
| 254.png | Mão pousando cédulas sobre uma pilha de contas/boletos na mesa (gerada IA — é o que sobra que paga a conta) | objeto-metafora, cena-de-trabalho | topo |
| 255.png | Broto verde nascendo do topo de uma pilha de moedas (gerada IA — Lucratividade, o lucro que floresce) | objeto-metafora, composicao-conceitual | topo |
| 256.png | Operários assentando um alicerce maciço de pedra antes das paredes subirem (gerada IA — a base vem primeiro, lucra depois cresce) | cena-de-trabalho, ambiente | topo |
| 257.png | Empresário maduro, tranquilo e confiante, de braços cruzados (gerada IA — o dono próspero de verdade) | pessoa | topo |
| 258.png | Trator de esteira antigo parado atravessado numa estrada de terra, neblina, bloqueando a passagem (gerada IA — capa "a empresa travou em você") | objeto-metafora, ambiente | topo |
| 259.png | Homem com vários braços fazendo tudo ao mesmo tempo (lendo, fumando, tesoura, caneta), colagem surreal, recorte em PNG transparente (enviada pelo user — o dono que faz tudo porque não tem quem faça / sobrecarga-multitarefa) | pessoa, composicao-conceitual | miolo |
| 260.png | Trator de esteira antigo de frente, coberto de barro, recortado no branco (gerada IA — "um verdadeiro trator") | objeto-metafora | topo |
| 261.png | Macacão de trabalho sujo pendurado num prego na parede da oficina (gerada IA — o personagem que virou identidade) | objeto-metafora | topo |
| 262.png | Pilhas altas de pastas e papéis esperando em cima de mesas (gerada IA — o que era velocidade virou fila) | objeto-metafora, cena-de-trabalho | topo |
| 263.png | Funil de metal grande entupido, material parado na boca estreita (gerada IA — tudo passa por você) | objeto-metafora | topo |
| 264.png | Engrenagem de ferro gigante emperrada, dente travado, máquina parada (gerada IA — o motor virou o entrave) | objeto-metafora | topo |
| 265.png | Homem exausto sentado curvado num banco, cabeça baixa, recortado no branco (gerada IA — o sinal chega como cansaço) | pessoa | topo |
| 266.png | Palito de fósforo queimado até o fim, torcido e apagado, com um fio de fumaça subindo (gerada IA — burnout, o peso que aparece em você) | objeto-metafora | topo |
| 267.png | Xícara de café fria e intocada numa mesa de oficina vazia, cadeira afastada (gerada IA — perdeu a vontade) | objeto-metafora, ambiente | topo |
| 268.png | Janela aberta pra um campo largo com grades de ferro na frente (gerada IA — a ilusão da liberdade) | ambiente, composicao-conceitual | topo |
| 269.png | Muro circular de tijolos erguido em volta de um chão vazio, sem saída (gerada IA — você montou essa prisão) | objeto-metafora, composicao-conceitual | topo |
| 270.png | Mão calejada apertando com força um martelo gasto, sem soltar (gerada IA — apego ao que faz melhor) | objeto-metafora | topo |
| 271.png | Macacão de trabalho e paletó pendurados lado a lado num varal (gerada IA — mesma pessoa, outro personagem) | objeto-metafora, composicao-conceitual | topo |
| 272.png | Escada de mão apoiada numa parede alta subindo pra fora do quadro, máquina velha abandonada no chão (gerada IA — coragem de trocar) | objeto-metafora, composicao-conceitual | topo |
| 273.png | Homem de camisa em pé, calmo, braços ao lado do corpo, olhando de lado, recortado no branco (gerada IA — o dono que sai da operação) | pessoa | topo |
| 274.png | Mão de estátua/bronze erguendo uma coroa de louros, recorte transparente (enviada pelo user — vitória, reconhecimento, glória conquistada) | objeto-metafora, pessoa | miolo |
| 275.png | Cowboy minúsculo em pé sobre uma nuvem laçando no vazio, com uma sombra escura projetada no chão branco, colagem surreal (enviada pelo user — cabeça nas nuvens, a ilusão x a sombra que fica) | composicao-conceitual, pessoa | miolo |
| 276.png | Homem de chapéu sentado na beira de uma laje pescando nas nuvens, surreal (enviada pelo user — paciência, pescar oportunidade, isolamento no alto) | composicao-conceitual, pessoa | base |
| 277.png | Mão aberta com a palma pra cima, esperando/pedindo, recorte transparente (enviada pelo user — mão vazia, esperar receber, pedir) | objeto-metafora, pessoa | miolo |
| 278.png | Homem levado pelos ares por um guarda-chuva, flutuando sem controle, surreal (enviada pelo user — ser levado pelo vento, ilusão de leveza, sem chão) | composicao-conceitual, pessoa | miolo |
| 279.png | Mão calejada mostrando UM dedo, recorte transparente (enviada pelo user — contagem 1; série 279-281) | objeto-metafora | miolo |
| 280.png | Mão calejada mostrando DOIS dedos em V, recorte transparente (enviada pelo user — contagem 2; série 279-281) | objeto-metafora | miolo |
| 281.png | Mão calejada mostrando TRÊS dedos, recorte transparente (enviada pelo user — contagem 3; série 279-281) | objeto-metafora | miolo |
| 282.png | Mão calejada apontando pro lado com o indicador, recorte transparente (enviada pelo user — apontar direção, indicar culpado, "é por ali") | objeto-metafora | miolo |
| 283.png | Pernas e sapatos sociais viradas pra cima, alguém caindo/tombado de pernas pro ar, recorte (enviada pelo user — o tombo, o fracasso, virar de cabeça pra baixo) | composicao-conceitual, pessoa | base |
| 284.png | Homem de terno rindo largado numa poltrona Eames com descanso de pés, muito à vontade (enviada pelo user — zona de conforto, acomodação, dono relaxado enquanto devia agir) | pessoa | base |
| 285.png | Mãos de maestro de fraque regendo uma orquestra, recorte transparente (enviada pelo user — reger, orquestrar, comandar a operação) | pessoa, objeto-metafora | miolo |
| 286.png | Homem de chapéu curvado riscando no chão um círculo fechado em volta dos próprios pés, colagem (enviada pelo user — cavar o próprio limite, se prender sozinho, se cercar) | composicao-conceitual, pessoa | base |
| 287.png | Homem deitado no sofá dormindo com o jornal sobre o rosto, papéis caídos no chão, recorte (enviada pelo user — acomodação, ignorar o problema, procrastinar) | pessoa, cena-de-trabalho | base |
| 288.png | Cama largada no meio de uma estrada curva com um homem dormindo, carro passando ao lado, colagem surreal (enviada pelo user — dormir no meio do caminho, parar alheio ao movimento) | composicao-conceitual, pessoa | miolo |
| 289.png | Roupas vazias (suéter e calça) sentadas sozinhas numa cadeira, sem ninguém dentro, recorte (enviada pelo user — a ausência do dono, o vazio, o esvaziamento) | objeto-metafora, composicao-conceitual | base |
| 290.png | Bicho-preguiça sentado meditando em posição de lótus, humor (enviada pelo user — preguiça/lentidão/acomodação com deboche, o oposto do trator) | composicao-conceitual | base |
| 291.png | Multidão de figuras pequenas serpenteando numa fila/onda pelo branco (enviada pelo user — a manada, seguir a fila, a massa que vai junto) | multidao, composicao-conceitual | base |
| 292.png | Homem de terno de costas parado diante de um muro de pedra, olhando o vazio branco além (enviada pelo user — encarar o próprio limite, o muro à frente) | pessoa, composicao-conceitual | base |
| 293.png | Torre altíssima e instável feita de dezenas de cadeiras empilhadas sobre um carro, prestes a desabar, colagem (enviada pelo user — acúmulo insustentável, crescer torto e empilhar sem base) | objeto-metafora, composicao-conceitual | miolo |
| 299.png | Homem de terno recostado tranquilo sobre um carro destruído num ferro-velho (enviada pelo user — calma em meio aos destroços, o dono diante do próprio estrago) | pessoa, composicao-conceitual | base |
| 300.png | Lancha de madeira cortando a agua em primeiro plano com o casco imenso de um transatlantico dissolvido na neblina ao fundo (gerada IA - a escala do pequeno x o grande) | embarcacao, composicao-conceitual | topo |
| 301.png | Ampulheta de navio em latao sobre o conves de madeira com cabo enrolado e carta nautica, mar ao fundo (gerada IA - tempo, o valor que dinheiro nao compra) | objeto-metafora, composicao-conceitual | topo |
| 302.png | Vista aerea de uma lancha fazendo uma curva fechada, rastro de espuma em arco, agua palida em cima (gerada IA - agilidade, corrigir a rota) | embarcacao, composicao-conceitual | topo |
| 303.png | Casco colossal de transatlantico atracado visto de baixo, homens minusculos no cais (gerada IA - o peso e a escala da empresa grande) | objeto-metafora, composicao-conceitual | topo |
| 304.png | Lancha pequena sozinha em agua aberta vista de cima, rastro curto (gerada IA - o negocio enxuto em movimento) | embarcacao | topo |
| 305.png | Vista aerea de uma lancha minuscula fazendo uma curva rapida ao lado do conves inteiro de um transatlantico (gerada IA - a diferenca de escala e de manobra no mesmo quadro) | embarcacao, composicao-conceitual | topo |
| 306.png | Maos calejadas remendando uma rede de pesca com agulha de madeira (gerada IA - proximidade com o cliente, oficio de perto) | pessoa, cena-de-trabalho | topo |
| 307.png | Ponte de comando de transatlantico, parede de mostradores e instrumentos, sem ninguem (gerada IA - a estrutura que precisa de painel pra saber o que o pequeno sente) | cena-de-trabalho, objeto-metafora | topo |
| 308.png | Tubo acustico de latao de navio antigo na antepara, close (gerada IA - comunicacao direta, ordem que chega inteira) | objeto-metafora | topo |
| 309.png | Lata de combustivel amassada e cabo enrolado num conves de madeira molhado (gerada IA - custo fixo baixo, folego) | objeto-metafora | topo |
| 310.png | Sala de maquinas colossal de transatlantico, fileira de caldeiras e tubulacoes, vazia (gerada IA - a maquina que come todo mes) | cena-de-trabalho, composicao-conceitual | topo |
| 311.png | Aviso de papel desbotado pregado numa antepara de metal imensa e vazia (gerada IA - cultura que virou cartaz na parede) | objeto-metafora, composicao-conceitual | topo |
| 312.png | Ancora enorme demais ocupando o conves de um barco pequeno, homem tentando move-la (gerada IA - o pequeno copiando a estrutura do grande) | objeto-metafora, composicao-conceitual | topo |
| 313.png | Cabo de amarracao grosso enrolado num cabeco de pedra no cais (gerada IA - camada, processo e amarra que prendem) | objeto-metafora | topo |
| 314.png | Barco entalado numa eclusa estreita entre duas paredes de concreto (gerada IA - preso no pior dos dois mundos, sem espaco de manobra) | embarcacao, composicao-conceitual | topo |
| 315.png | Esqueleto de casco novo em construcao num estaleiro, cavernas de madeira e andaimes (gerada IA - crescer com estrutura, obra em pe) | cena-de-trabalho, composicao-conceitual | topo |
| 316.png | Carta nautica aberta sobre a mesa com bussola, compasso e regua paralela (gerada IA - rumo, metodo, decisao com numero na mao) | objeto-metafora | topo |
| 317.png | Homem de pe na proa de um barco pequeno olhando o horizonte aberto, recortado no branco (gerada IA - o dono com direcao) | pessoa, embarcacao | miolo |
| 318.png | Dois homens de escritorio, um falando um segredo no ouvido do outro que escuta atento (gerada IA - a dica, o segredo, a informacao privilegiada) | pessoa, cena-de-trabalho | topo |
| 319.png | Mao levantando a rainha do adversario num tabuleiro de xadrez em jogo (gerada IA - roubar do outro, lance decisivo, captura) | objeto-metafora, composicao-conceitual | topo |
| 320.png | Torneiro concentrado no torno em oficina movimentada, colegas ao fundo (gerada IA - o profissional bom empregado, oficio) | pessoa, cena-de-trabalho | topo |
| 321.png | Mao do dono mais velho no ombro do funcionario jovem na bancada, vistos de costas (gerada IA - valorizacao, o bom que tem quem o segure) | pessoa, cena-de-trabalho | topo |
| 322.png | Dono de avental encostado na porta da loja olhando a rua vazia de paralelepipedo (gerada IA - esperar quem nao vem bater na porta) | pessoa, cena-de-trabalho | topo |
| 323.png | Funcionario concentrado atras do balcao visto da rua atraves da vitrine (gerada IA - ele esta bem onde esta, o de fora olhando) | pessoa, cena-de-trabalho | topo |
| 324.png | Feirante no gesto de venda convicto oferecendo ao fregues sobre caixas de frutas (gerada IA - venda de ideia, convencer) | pessoa, cena-de-trabalho | topo |
| 325.png | Escada velha de madeira subindo para uma luz clara vinda de cima (gerada IA - perspectiva, futuro, subida) | objeto-metafora, composicao-conceitual | topo |
| 326.png | Mestre mais velho e aprendiz rindo juntos trabalhando na bancada (gerada IA - aprender, clima leve, orgulho de pertencer) | pessoa, cena-de-trabalho | topo |
| 327.png | Dois homens conversando em mesa redonda de cafe na beira do cais, um falando com gesto convicto (gerada IA - a abordagem, proposta olho no olho) | pessoa | topo |
| 328.png | Escritorio pequeno largado em penumbra, papelada empilhada, cadeira vazia (gerada IA - empresa sem rumo, abandono) | cena-de-trabalho, composicao-conceitual | topo |
| 329.png | Maos de um time sobre folha grande de planejamento em branco, uma apontando, outra com lapis (gerada IA - meta, plano, rumo) | pessoa, objeto-metafora | topo |
| 330.png | Dono de avental no meio do time engajado trabalhando em oficina viva (gerada IA - time com dono presente, ambiente que retem) | pessoa, cena-de-trabalho | topo |
| 331.png | Comerciante de avental cansado apoiado no balcao da mercearia no fim do dia (gerada IA - o dono e a dor do caixa que nao sobra) | pessoa, cena-de-trabalho | topo |
| 332.png | Maos abrindo a gaveta de registradora antiga com poucas notas e moedas (gerada IA - caixa apertado, fim de mes) | objeto-metafora, cena-de-trabalho | topo |
| 333.png | Feirante no auge da venda de bracos abertos sobre banca cheia, fregues pegando (gerada IA - a crenca de que venda resolve tudo) | pessoa, cena-de-trabalho | topo |
| 334.png | Registradora antiga com bobina de papel transbordando em cascata pelo balcao (gerada IA - mes recorde de venda) | objeto-metafora, composicao-conceitual | topo |
| 335.png | Balde de zinco furado jorrando agua pelos furos embaixo de torneira aberta (gerada IA - vender mais sem gestao, dinheiro vazando) | objeto-metafora, composicao-conceitual | topo |
| 336.png | Empresario ajeitando a gravata diante do espelho, rosto so no reflexo (gerada IA - a mentira contada a si mesmo) | pessoa, composicao-conceitual | topo |
| 337.png | Dono na porta da loja olhando a rua, de costas pra papelada acumulada no balcao (gerada IA - culpar o mercado sem olhar pra dentro) | pessoa, cena-de-trabalho | topo |
| 338.png | Mesa coberta de papeis rabiscados, calculadora antiga, lapis e xicara (gerada IA - decisao no achismo) | objeto-metafora, cena-de-trabalho | topo |
| 339.png | Loja fechada de grade de metal abaixada e letreiro apagado, calcada vazia (gerada IA - empresa que quebra) | cena-de-trabalho, composicao-conceitual | topo |
| 340.png | Maos sobre livro-caixa aberto de colunas alinhadas, uma apontando, outra com caneta (gerada IA - gestao, numero na mao) | objeto-metafora, cena-de-trabalho | topo |
| 341.png | Dono exausto sozinho de madrugada curvado no balcao sob lampada unica, loja escura (gerada IA - esforco que nao vira sobra) | pessoa, cena-de-trabalho | topo |
| 342.png | Dono confiante e sereno apoiado no balcao de loja organizada e abastecida (gerada IA - empresa com metodo, controle) | pessoa, cena-de-trabalho | topo |
| 343.png | Dono de avental de costas na calcada olhando a fachada da propria loja com letreiro em branco (gerada IA - o tamanho que ele mede) | pessoa, cena-de-trabalho | topo |
| 344.png | Inauguracao de loja em cidade brasileira: fita cortada na porta, apertos de mao, grupo aplaudindo (gerada IA - o aplauso do falso crescimento) | pessoa, cena-de-trabalho | topo |
| 345.png | Maos abrindo carteira de couro fina com poucas notas dentro (gerada IA - o saque parado) | objeto-metafora, maos | topo |
| 346.png | Balao enorme inflado alem da conta preso a bomba de ar manual antiga (gerada IA - empresa que incha) | objeto-metafora, composicao-conceitual | topo |
| 347.png | Balanca antiga de dois pratos em equilibrio: notas de um lado, contas do outro (gerada IA - entra mais, sai mais) | objeto-metafora, composicao-conceitual | topo |
| 348.png | Maos com caneta apontando a ultima linha de livro-caixa aberto, lupa ao lado (gerada IA - a ultima linha) | objeto-metafora, maos | topo |
| 349.png | Parede com marcas de altura a lapis e mao marcando traco novo com regua dobravel (gerada IA - medir crescimento) | objeto-metafora, maos, composicao-conceitual | topo |
| 350.png | Dono exausto sentado em banquinho no corredor do deposito, engolido por pilhas de caixas (gerada IA - dobrou e empobreceu) | pessoa, cena-de-trabalho | topo |
| 351.png | Dono de mangas arregacadas conferindo prateleiras organizadas com prancheta (gerada IA - rotina de gestao) | pessoa, cena-de-trabalho | topo |
| 352.png | Dono pequeno e confiante de bracos cruzados atras do balcao de mercearia arrumada, parede alta vazia acima (gerada IA - controle, CTA) | pessoa, cena-de-trabalho | topo |
| 353.png | Homem dormindo encolhido em cama de ferro sob cobertor curto, pes de fora (gerada IA - cobertor curto, aperto) | pessoa, composicao-conceitual | topo |
| 354.png | Pes descobertos saindo da ponta do cobertor curto em cama de ferro (gerada IA - descobre o pe) | objeto-metafora, composicao-conceitual | topo |
| 355.png | Feirante puxando lona curta demais sobre as caixas da banca, a outra ponta descoberta (gerada IA - cobre um canto, descobre o outro) | pessoa, cena-de-trabalho | topo |
| 356.png | Comerciante contando notas sobre a gaveta aberta no fim do dia, meio sorriso (gerada IA - mes bom, caixa engorda) | pessoa, cena-de-trabalho | topo |
| 357.png | Mao entregando maco de notas na mao aberta de outro homem sobre o balcao (gerada IA - dinheiro trocando de mao, conta dos outros) | maos, objeto-metafora | topo |
| 358.png | Maos separando notas em duas pilhas desiguais no balcao de madeira (gerada IA - imposto embutido na venda) | maos, objeto-metafora | topo |
| 359.png | Cofre de ferro antigo imenso e fechado contra parede descascada (gerada IA - cofre do governo) | objeto-metafora, composicao-conceitual | topo |
| 360.png | Fila de pessoas de casaco e chapeu diante de guiche antigo, vistas de costas (gerada IA - a fila do saldo) | pessoa, composicao-conceitual | topo |
| 361.png | Homem sentado na beira da cama de madrugada com as maos no rosto (gerada IA - o peso da sobrevivencia) | pessoa, composicao-conceitual | topo |
| 362.png | Despertador antigo de dois sinos sozinho na mesa de cabeceira em penumbra (gerada IA - madrugada, rotina que nao muda) | objeto-metafora, composicao-conceitual | topo |
| 363.png | Maos costurando manta de la grossa com agulha e linha (gerada IA - costurar o cobertor, gestao) | maos, objeto-metafora | topo |
| 364.png | Maos com lapis sobre caderno aberto e caneca de cafe na luz da manha (gerada IA - conhecer os numeros) | maos, cena-de-trabalho | topo |
| 365.png | Homem dormindo sereno coberto por inteiro por cobertor grande na luz do amanhecer (gerada IA - dormir tranquilo, CTA) | pessoa, composicao-conceitual | topo |
| 366.png | Samurai de armadura em seiza meditando na nevoa, olhos fechados, katana embainhada sobre os joelhos (gerada IA - post frase 35, batalha interna) | pessoa, composicao-conceitual, ambiente | topo |
| 367.png | Camera rente ao solo: trilha de sementes na terra arada levando ate semeador de costas ao fundo na nevoa (gerada IA - post frase 36, quem divide multiplica) | pessoa, composicao-conceitual, ambiente | topo |
| 368.png | Vista subaquatica: superficie estourada de luz no topo, mergulhador livre em silhueta descendo de cabeca pra baixo por cabo-guia vertical rumo ao escuro (gerada IA - post frase 37, no raso nao existe pressao; composicao de profundidade vertical) | pessoa, composicao-conceitual, ambiente | topo |
| 369.png | Camera rente a areia molhada: casco colossal de navio encalhado tomando a esquerda e dissolvendo na nevoa (nao cabe no quadro), homem minusculo de costas na base segurando o cabo com a mao esquerda, olhando o barco pequeno de vela que ja navega ao fundo a direita, canais de mare ligando os dois (gerada IA - post frase 39, a mare nao espera barco pronto; escala + "nao caber no quadro" como recurso) | pessoa, embarcacao, composicao-conceitual, ambiente | topo |
| 370.png | Camera rente ao solo em ruina de templo na nevoa: uma unica coluna doria de pe sustentando sozinha a arquitrave inteira de pedra, todas as outras colunas em tocos e tambores quebrados espalhados no chao (gerada IA - post frase 42 v1, o peso procura quem aguenta; a lei visivel sem figura humana) | objeto-metafora, composicao-conceitual, ambiente | topo |
| 371.png | Garganta de rocha na nevoa: laje colossal desprendida do paredao tombada em diagonal, escorada por uma rocha menor cravada por baixo cuja silhueta lembra um vulto curvado com o ombro enfiado sob a laje e os pes fincados, chao fraturado na base, blocos que ja cederam em volta (gerada IA - post frase 42 v7; pareidolia por silhueta contra nevoa, carga diagonal) | objeto-metafora, composicao-conceitual, ambiente | topo |
| 372.png | Aerea na altura do cume, SEM CHAO nem horizonte: parede de montanha tomando a direita inteira e saindo do quadro, nuvem clara a esquerda e banco escuro embaixo; fundido a parede, um homem do tamanho de meia montanha ABRACADO ao macico - cabeca de lado SEM FEICAO (proposital: rosto quebra a peca), bracos estendidos ao longo da parede, costas arqueadas, pernas dissolvendo na rocha sem pes; corpo E paredao feitos dos MESMOS blocos, com as juntas cortando atravessado o corpo e seguindo pra dentro da montanha (gerada IA - post frase 42 FINAL, dirigida por esboco do user; quem carrega e feito do mesmo material da carga) | pessoa, objeto-metafora, composicao-conceitual, ambiente | topo |
| 373.png | POV de dentro do abismo, ar limpo SEM nevoa: paredes escuras lisas em silhueta formando curva de cratera contra ceu branco absoluto, homem minusculo de terno debrucado na borda curva visto de baixo, olhando pra dentro (gerada IA - post frase 56, se voce olha demais para um abismo; chave minimalista escultural: abismo como forma negra limpa, um elemento so, a foto E o abismo olhando de volta) | pessoa, composicao-conceitual, ambiente | topo |
| 374.png | Prateleira antiga de madeira contra parede de reboco clara, carregada de sacas de estopa com feijao/graos e potes de vidro, tabua vergada em arco pronunciado e escultural, sem figura humana (gerada IA - post frase 57, prateleira vazia nao verga; curva como forma quase grafica, primeira geracao aprovada) | objeto-metafora, composicao-conceitual | topo |
| 375.png | Carro antigo alto num macaco hidraulico so, quatro rodas tiradas encostadas na parede, oficina mecanica anos 70 (gerada IA - carrossel 106, o banco financia a quebra, capa) | objeto-metafora, ambiente | topo |
| 376.png | Mecanico dono de oficina dentro do fosso a noite embaixo do carro, lampada nua pendurada, bracos de graxa, cara cansada (gerada IA - carrossel 106, trabalha pro banco) | pessoa, cena-de-trabalho | topo |
| 377.png | Fachada de oficina: porta de enrolar meio abaixada e placa de madeira com tinta comida sem letra, vista de baixo dissolvendo pra luz (gerada IA - carrossel 106, divida com placa na porta) | ambiente, objeto-metafora | topo |
| 378.png | Dono de oficina de macacao apertando a mao do gerente de banco de terno no balcao, mao de graxa, sorriso agradecido; parede lisa (gerada IA - carrossel 106, agradece o gerente) | pessoa, cena-de-trabalho | topo |
| 379.png | Balcao de madeira de oficina: caderno aberto com caneta, gaveta de dinheiro vazia com duas moedas, galpao ao fundo (gerada IA - carrossel 106, cheque especial) | objeto-metafora, cena-de-trabalho | topo |
| 380.png | Dono de oficina assinando papel no balcao, gerente de terno do outro lado com pasta, chave de carro sobre o balcao entre os dois, cachorro ao fundo (gerada IA - carrossel 106, carro de garantia) | pessoa, cena-de-trabalho | topo |
| 381.png | Camera rente ao chao de terra: vaga vazia com mancha de oleo velha e marcas paralelas de pneu indo embora, folhas secas, muro branco dissolvido (gerada IA - carrossel 106, o carro foi) | objeto-metafora, ambiente | topo |
| 382.png | Dono de oficina sentado numa pilha de pneus depois do expediente, carne de parcelas nas maos de graxa, olhar vazio (gerada IA - carrossel 106, sabe a parcela de cor) | pessoa, cena-de-trabalho | topo |
| 383.png | Gerente de banco de terno e pasta em pe no meio da oficina suja de oleo, sorriso de vendedor, dono de costas desfocado na borda esquerda (gerada IA - carrossel 106, o gerente vende dinheiro) | pessoa, composicao-conceitual | topo |
| 384.png | Bancada de oficina: caderno aberto com coluna de tracinhos fechada por um traco, lapis, oculos dobrados, calculadora mecanica de manivela (gerada IA - carrossel 106, quanto entra quanto sai quanto sobra) | objeto-metafora, cena-de-trabalho | topo |
| 385.png | Balcao de oficina em ordem: gaveta de dinheiro fechada, caderno fechado com lapis em cima, telefone de parede no gancho (gerada IA - carrossel 106, conta que fecha nao precisa de banco) | objeto-metafora, ambiente | topo |
| 386.png | Dono de oficina de macacao e consultor de camisa clara lado a lado na bancada, caderno aberto, consultor apontando linha com lapis, dono ouvindo com a mao no queixo (gerada IA - carrossel 106, oferta diagnostico) | pessoa, cena-de-trabalho | topo |
| 387.png | Dono de oficina na porta de enrolar meio aberta, macacao, pano no ombro, olhando firme pra camera, oficina rodando atras (gerada IA - carrossel 106, CTA) | pessoa, cena-de-trabalho | topo |
| 388.png | Parede rachada de predio comercial pequeno sustentada por fora por escoras de madeira cravadas na calcada, topo dissolvendo (gerada IA - carrossel 106 v2, o banco so financia a quebra, capa) | objeto-metafora, ambiente | topo |
| 389.png | Dono de empresa pequena sozinho na mesa a noite, abajur baixo, mao nos olhos, papeis e caderno abertos (gerada IA - carrossel 106 v2, trabalha pro banco) | pessoa, cena-de-trabalho | topo |
| 390.png | Fachada generica de loja: porta de enrolar meio abaixada e placa de madeira com tinta comida sem letra vista de baixo, escuro por baixo da porta (gerada IA - carrossel 106 v2, divida com placa na porta) | ambiente, objeto-metafora | topo |
| 391.png | Dono de camisa simples e gerente de banco de terno sentados frente a frente apertando a mao por cima da mesa, sorriso agradecido, parede lisa (gerada IA - carrossel 106 v2, agradece o gerente) | pessoa, cena-de-trabalho | topo |
| 392.png | Mesa de escritorio: talao de cheque aberto com caneta e caixa de dinheiro de lata aberta e vazia com duas moedas (gerada IA - carrossel 106 v2, cheque especial) | objeto-metafora, cena-de-trabalho | topo |
| 393.png | Agencia bancaria: dono de camisa simples assinando na mesa do gerente, gerente de maos cruzadas, chave de carro na mesa entre os dois (gerada IA - carrossel 106 v2, carro de garantia) | pessoa, cena-de-trabalho | topo |
| 394.png | Portao baixo de casa simples fechado com corrente e cadeado, velocipede de crianca tombado no quintal de cimento, fachada dissolvida (gerada IA - carrossel 106 v2, a divida ja e da familia) | objeto-metafora, ambiente | topo |
| 395.png | Dono sentado no degrau da loja sob a porta meio abaixada, carne de parcelas nas maos, olhar parado (gerada IA - carrossel 106 v2, sabe a parcela de cor) | pessoa, cena-de-trabalho | topo |
| 396.png | Gerente de banco de terno sentado atras da mesa do escritorio simples segurando a pasta, sorriso de vendedor pra camera, ombro do dono desfocado a esquerda; topo estendido no pos (gerada IA - carrossel 106 v2, o gerente vende dinheiro) | pessoa, composicao-conceitual | topo |
| 397.png | Mesa de escritorio: caderno aberto com coluna de tracinhos de contagem fechada por um traco, lapis, oculos, calculadora mecanica, telefone e caixa de lata (gerada IA - carrossel 106 v2, quanto entra quanto sai quanto sobra) | objeto-metafora, cena-de-trabalho | topo |
| 398.png | Mesa de escritorio em ordem: caixa de dinheiro de lata fechada, caderno fechado com lapis em cima, telefone de disco no gancho, os tres juntos no centro (gerada IA - carrossel 106 v2, conta que fecha nao precisa de banco) | objeto-metafora, ambiente | topo |
| 399.png | Dono de camisa simples e consultor de camisa clara lado a lado na mesa, caderno aberto, consultor apontando linha, dono com a mao no queixo (gerada IA - carrossel 106 v2, oferta diagnostico) | pessoa, cena-de-trabalho | topo |
| 400.png | Dono de camisa simples na porta da loja sob a porta de enrolar meio levantada, olhando firme pra camera, escritorio simples atras (gerada IA - carrossel 106 v2, CTA) | pessoa, cena-de-trabalho | topo |
| 401.png | Dono de camisa de manga curta atras do balcao olhando pra gaveta da registradora aberta e vazia, clientes apinhados dos dois lados olhando junto, parede branca lisa ocupando o topo (gerada IA - carrossel 111 v2, capa: quebra por falta de caixa) | pessoa, composicao-conceitual | topo |
| 402.png | Still no balcao: molho de chaves e cadeado aberto ao lado da registradora, caneca de cafe e pano, parede branca lisa no topo (gerada IA - carrossel 111 v3, a licao que salva todo santo dia) | objeto-metafora, cena-de-trabalho | topo |
| 403.png | Dono de camisa de manga curta assinando contrato no balcao enquanto homem de terno com pasta segura o papel sorrindo, salao cheio de geladeiras e caminhao ao fundo (gerada IA - carrossel 111, continuou pegando emprestimo como nunca) | pessoa, cena-de-trabalho | topo |
| 404.png | Fichario de madeira do crediario aberto no balcao, dezenas de carnes em pe com divisorias e elasticos, salao de eletrodomesticos e caminhao ao fundo (gerada IA - carrossel 111, o dinheiro esta na rua no carne) | objeto-metafora, cena-de-trabalho | topo |
| 405.png | Dono entregando carne de crediario na mao do cliente no balcao, os dois grandes de perfil, carregadores levando geladeira a direita, parede branca lisa no topo (gerada IA - carrossel 111 v2, quem banca o cliente e voce) | pessoa, cena-de-trabalho | topo |
| 406.png | Geladeira encaixotada em papelao liso amarrada com corda em pe na carroceria de madeira do caminhao de entrega na porta da loja (gerada IA - carrossel 111, voce nao vendeu voce emprestou) | objeto-metafora, ambiente | topo |
| 407.png | Balcao: pilha alta de carnes com elastico a esquerda e gaveta da registradora aberta com tres moedas a direita, salao de eletrodomesticos atras (gerada IA - carrossel 111, quanto mais vende mais falta) | objeto-metafora, composicao-conceitual | topo |
| 408.png | Caminhao de entrega carregado ate em cima de caixas de eletrodomesticos amarradas saindo pela rua de paralelepipedo, dono de costas na calcada acenando (gerada IA - carrossel 111, o buraco ficou maior) | pessoa, ambiente | topo |
| 409.png | Dono sentado num caixote no deposito a noite, maos juntas no rosto, caixas de eletrodomesticos ate o teto dos dois lados, cofre de ferro aberto e vazio ao lado, lampada nua (gerada IA - carrossel 111, crescer sem caixa e acelerar rumo ao abismo) | pessoa, composicao-conceitual | topo |
| 410.png | Mesa do escritorio: livro-caixa aberto com colunas a lapis ilegiveis, lapis, despertador de corda com campainhas, fichario de carnes ao lado, salao ao fundo (gerada IA - carrossel 111, a conta de dias) | objeto-metafora, cena-de-trabalho | topo |
| 411.png | Salao de loja de eletrodomesticos lotado num sabado: clientes de costas e perfil entre geladeiras e fogoes, vendedor de gravata fina explicando, dono no caixa a direita (gerada IA - carrossel 111, quebra com a loja cheia) | pessoa, cena-de-trabalho | topo |
| 412.png | Consultor de gravata e dono de camisa de manga curta lado a lado no balcao, livro-caixa aberto, consultor apontando linha com a caneta, geladeiras e caminhao ao fundo (gerada IA - carrossel 111, oferta diagnostico) | pessoa, cena-de-trabalho | topo |
| 413.png | Still: registradora de manivela com a gaveta aberta e quase vazia, uma nota amassada e tres moedas, parede branca lisa no topo (gerada IA - carrossel 111 v2, CTA: caixa com dinheiro faltando) | objeto-metafora, composicao-conceitual | topo |
| 414.png | Dono de avental de couro em pe na bancada de corte olhando serio pra camera, maos sobre o couro, par de sapatinhos de crianca na bancada entre as formas, maquina de costura a direita, parede lisa clara (gerada IA - carrossel 114, capa: sua empresa e limitada, o seu CPF nao e) | pessoa, cena-de-trabalho | topo |
| 415.png | Still: contrato social aberto na ultima pagina com carimbo redondo de cartorio e assinatura ilegiveis, oculos dobrados e caneta-tinteiro sobre a pagina, formas de sapato e maquina de costura ao fundo (gerada IA - carrossel 114, voce e o unico que acredita nisso) | objeto-metafora, composicao-conceitual | topo |
| 416.png | Dono de avental e gerente de terno lado a lado na bancada de corte, o dono assinando o contrato e o gerente apontando a linha, ambos olhando pra baixo, parede continua (gerada IA - carrossel 114 v3, o aval ficou no seu CPF) | pessoa, cena-de-trabalho | topo |
| 417.png | Oficial de justica de terno e pasta visto de costas subindo os primeiros degraus da escada interna da fabrica de calcados; dono de avental e dois homens de terno olhando (gerada IA - carrossel 114, se o CNPJ cai a conta pula pro seu CPF) | pessoa, composicao-conceitual | topo |
| 418.png | Dono de avental cortando couro na bancada em primeiro plano; atras, tres homens de terno na mesa da cozinha da familia com tres envelopes, bule esmaltado e xicara (gerada IA - carrossel 114, os tres tem o mesmo endereco: o seu) | pessoa, composicao-conceitual | topo |
| 419.png | Still: oficina de calcados com cadeira de balanco, radio valvulado e abajur trazidos pro meio, cada um com etiqueta de papel amarrada com barbante; bancada de couro e maquina de costura (gerada IA - carrossel 114 v2, sai num edital de leilao) | objeto-metafora, ambiente | topo |
| 420.png | Close da mao do dono de avental segurando uma cortina de renda esticada contra a parede lisa, formas de sapato e maquina de costura atras (gerada IA - carrossel 114 v2, o Ltda nao e muro, e cortina) | maos, objeto-metafora | topo |
| 421.png | Fila no relogio de ponto da oficina: dois funcionarios jovens de avental na frente e o dono, mais velho, no fim da fila com o cartao na mao, de perfil (gerada IA - carrossel 114, um pro-labore de gerente) | pessoa, cena-de-trabalho | topo |
| 422.png | Still: pilha alta de contratos carimbados a esquerda e um envelope de pagamento fino sozinho a direita, sobre o couro da bancada, formas e caixas ao fundo (gerada IA - carrossel 114 v2, o risco e ilimitado, so o que voce tira e limitado) | objeto-metafora, composicao-conceitual | topo |
| 423.png | Dono de avental de bracos cruzados olhando firme pra camera, tres pessoas de terno com pastas atras dele na oficina de calcados (gerada IA - carrossel 114, empresa nasceu pra botar dinheiro no bolso do dono) | pessoa, composicao-conceitual | topo |
| 424.png | Still: folha de contrato com a linha de assinatura vazia, caneta-tinteiro deitada sobre a linha, carimbo de madeira e almofada de tinta ao lado, couro na bancada (gerada IA - carrossel 114 v2, voce nao e dono, e fiador) | objeto-metafora, composicao-conceitual | topo |
| 425.png | Dono de avental, rosto no quadro olhando pra baixo, guardando um envelope no bolso do peito da camisa; formas, maquina de costura e caixas atras (gerada IA - carrossel 114 v3, regra numero 1: dinheiro no bolso do dono) | pessoa, objeto-metafora | topo |
| 426.png | Dono de avental e consultor de camisa clara lado a lado na bancada de corte, livro-caixa aberto, consultor apontando uma linha com a caneta, dono ouvindo serio (gerada IA - carrossel 114 v2, oferta diagnostico) | pessoa, cena-de-trabalho | topo |
| 427.png | Still: molho com duas chaves na mesma argola, uma chave grande antiga de ferro e uma chave pequena de casa, sobre o couro da bancada, formas, caixas e maquina ao fundo (gerada IA - carrossel 114, CTA: o mesmo molho) | objeto-metafora, composicao-conceitual | topo |
| 428.png | Dono do posto de gasolina no meio da fala, dedo em riste, diante de dois frentistas de bone de cabeca baixa, bomba e carro nas bordas, parede lisa (gerada IA - carrossel 115, capa: quantas vezes eu tenho que falar? Todas) | pessoa, cena-de-trabalho | topo |
| 429.png | Carro anos 70 parado na bomba, motorista de braco pra fora da janela olhando pra tras procurando alguem, pano largado em cima da bomba, nenhum frentista (gerada IA - carrossel 115, o cliente esperou de novo e ninguem deu bom dia) | pessoa, composicao-conceitual | topo |
| 430.png | Frentista de bracos cruzados encostado na bomba a esquerda e o dono de costas entrando no escritorio do posto a direita, carro entre eles (gerada IA - carrossel 115 v2, ninguem quer nada com nada, para de corrigir) | pessoa, composicao-conceitual | topo |
| 431.png | Still: mangueira da bomba largada em lacos no concreto com o bico no chao, patio vazio, poste de calibragem e segunda bomba ao fundo (gerada IA - carrossel 115, no dia que voce para a cultura para junto) | objeto-metafora, ambiente | topo |
| 432.png | Still: patio de concreto visto de baixo com duas trilhas de pneu cavadas ate a base da bomba, segunda bomba e poste ao fundo (gerada IA - carrossel 115, o que voce repete ate ninguem mais precisar pensar) | objeto-metafora, composicao-conceitual | topo |
| 433.png | Close dentro de carro antigo: mao do motorista no bolao do cambio, antebraco de camisa de trabalho, painel e volante, parede lisa pelo para-brisa (gerada IA - carrossel 115 v2, a mao vai sozinha) | maos, objeto-metafora | topo |
| 434.png | Tres frentistas de macacao e bone em fila diante do dono com prancheta, conferindo um a um, bombas atras, manha antes de abrir (gerada IA - carrossel 115, quem repete constantemente faz a cultura entrar na mente) | pessoa, cena-de-trabalho | topo |
| 435.png | Still: relogio redondo na parede do posto com prancheta e quadro de turnos pendurados embaixo, entre duas bombas, lata de oleo e banquinho (gerada IA - carrossel 115, o rito vem antes do erro, mesma hora todo dia) | objeto-metafora, ambiente | topo |
| 436.png | Frentista novo de macacao com vinco e bone, maos nos bolsos, sozinho ao lado da bomba olhando perdido, frente de carro chegando na borda (gerada IA - carrossel 115, entra na folha de pagamento, na cultura nao) | pessoa, composicao-conceitual | topo |
| 437.png | Still: pilha de panos de limpar vidro iguais dobrados numa prateleira baixa com lata, funil e almotolia, e um pano igual pendurado no gancho da bomba (gerada IA - carrossel 115, repetir e papel do dono) | objeto-metafora, composicao-conceitual | topo |
| 438.png | Frentista limpando o para-brisa de um carro com o motorista dentro, gesto concentrado, o dono pequeno ao fundo de costas com prancheta (gerada IA - carrossel 115, time cumprindo o combinado todo dia e obra de repeticao) | pessoa, cena-de-trabalho | topo |
| 439.png | Dono do posto de camisa clara e prancheta debaixo do braco olhando firme pra camera, bombas e dois frentistas trabalhando num carro ao fundo (gerada IA - carrossel 115, oferta imersao) | pessoa, cena-de-trabalho | topo |
| 440.png | Still: bomba antiga com o bico encaixado e um pano dobrado em cima, patio limpo, sombra longa de fim de tarde (gerada IA - carrossel 115, CTA: o posto pronto pra amanha) | objeto-metafora, ambiente | topo |
| 441.png | Costureira na maquina com as maos paradas olhando o relogio de parede, o dono pequeno na porta do fundo observando (gerada IA - carrossel 117 v2, capa: conta os minutos e voce chama de falta de vontade) | pessoa, cena-de-trabalho | topo |
| 442.png | Homem de camiseta sentado no sofa da sala no domingo a noite, luz da TV de tubo no rosto, olhando o relogio, uniforme passado pendurado na porta (gerada IA - carrossel 117, domingo sete da noite, a musica do Fantastico) | pessoa, composicao-conceitual | topo |
| 443.png | Still: despertador de corda marcando sete horas na mesinha ao lado do sofa, uniforme dobrado, TV apagada refletindo a sala (gerada IA - carrossel 117, nao e preguica, e a sua empresa que ele nao quer ver na segunda) | objeto-metafora, ambiente | topo |
| 444.png | Duas costureiras centradas nas maquinas, uma de cabeca baixa e a outra erguendo os olhos pro relogio de parede entre elas (gerada IA - carrossel 117 v3, segunda: cara amarrada, olho no relogio) | pessoa, cena-de-trabalho | topo |
| 445.png | Dono de camisa clara de perfil na porta do salao de costura, maos na cintura, duas costureiras de costas nas maquinas (gerada IA - carrossel 117, esse povo nao quer nada? nao quer o que voce oferece) | pessoa, composicao-conceitual | topo |
| 446.png | Dono de pe atras da costureira sentada apontando o dedo pra peca, ela de cabeca baixa, pilha de pecas prontas ao lado (gerada IA - carrossel 117, odeia bronca antes do bom dia e ninguem perceber) | pessoa, cena-de-trabalho | topo |
| 447.png | Still: fachada da confeccao com a porta de enrolar abaixada no domingo, sombra de arvore na parede lisa, calcada vazia (gerada IA - carrossel 117, grito: a tristeza do domingo a noite e o diagnostico da sua empresa) | ambiente, composicao-conceitual | topo |
| 448.png | Still: relogio de ponto na parede da confeccao com o quadro de cartoes em fila, maquina de costura e mesa de corte dos lados (gerada IA - carrossel 117, ninguem acorda animado pra bater ponto) | objeto-metafora, ambiente | topo |
| 449.png | Dono de camisa clara falando com as maos pra quatro costureiras em roda na mesa de corte, uma jovem sorrindo (gerada IA - carrossel 117, gente so acorda com vontade pra um lugar onde aprende, ganha, tem orgulho e se diverte) | pessoa, cena-de-trabalho | topo |
| 450.png | Costureira veterana de cabelo grisalho guiando as maos de uma jovem na maquina de costura, envelope de pagamento fechado na mesa (gerada IA - carrossel 117, teste 1 e 2: aprende? da pra sonhar com o salario?) | pessoa, cena-de-trabalho | topo |
| 451.png | Hora do cafe na confeccao: costureira rindo alto com a xicara, outra mostrando um vestido pronto, o dono ao lado rindo com a xicara (gerada IA - carrossel 117, teste 3 e 4: orgulho? gente rindo?) | pessoa, cena-de-trabalho | topo |
| 452.png | Still: sala vazia de domingo com a TV de tubo ligada em brilho cinza, sofa com a marca do corpo, relogio e uniforme pendurado na porta (gerada IA - carrossel 117, a musica do Fantastico vai continuar batendo ponto) | objeto-metafora, ambiente | topo |
| 453.png | Dono de costas no escritorio pequeno, mao no queixo, olhando pela janela interna o salao com duas costureiras nas maquinas (gerada IA - carrossel 117, grito: clima ruim tem dono) | pessoa, composicao-conceitual | topo |
| 454.png | Duas costureiras centradas nas maquinas viradas uma pra outra, uma falando e a outra rindo enquanto costuram (gerada IA - carrossel 117 v3, time que chega na segunda com vontade) | pessoa, cena-de-trabalho | topo |
| 455.png | Dono de camisa clara de bracos cruzados olhando firme pra camera, costureiras nas maquinas atras, uma sorrindo pra ele (gerada IA - carrossel 117, oferta: aplicar os quatro pilares comigo) | pessoa, cena-de-trabalho | topo |
| 456.png | Still: sofa vazio da sala de domingo com a marca do corpo na almofada, TV de tubo ligada ao lado, uniforme pendurado na porta (gerada IA - carrossel 117, CTA: alguem do seu time esta com o peito apertado agora) | objeto-metafora, ambiente | topo |
| 457.png | Funcionario de camisa e gravata fina na maquina de escrever, maos paradas, cabeca virada pro relogio de parede ao lado, escritorio de contabilidade (gerada IA - carrossel 117 v2, capa: conta os minutos e voce chama de falta de vontade) | pessoa, cena-de-trabalho | topo |
| 458.png | Homem de costas no sofa da sala, TV de tubo no centro com o letreiro FANTASTICO sobre o globo, relogio e uniforme pendurado na porta (gerada IA - carrossel 117 v2, domingo sete da noite, a musica do Fantastico; pedido do user) | pessoa, composicao-conceitual | topo |
| 459.png | Dois atendentes debrucados no balcao de uma loja de autopecas com cara de tedio, um de queixo na mao olhando o relogio de parede (gerada IA - carrossel 117 v2, segunda: cara amarrada, olho no relogio) | pessoa, cena-de-trabalho | topo |
| 460.png | Dono de deposito de perfil na porta, maos na cintura, olhando dois funcionarios de macacao carregando uma caixa sem pressa (gerada IA - carrossel 117 v2, esse povo nao quer nada? nao quer o que voce oferece) | pessoa, composicao-conceitual | topo |
| 461.png | Dono de avental numa grafica com o dedo em riste sobre a folha impressa, o rapaz de cabeca baixa, prensa ao lado (gerada IA - carrossel 117 v2, odeia bronca e cobranca sem sentido) | pessoa, cena-de-trabalho | topo |
| 462.png | Still: relogio de ponto e quadro de cartoes num corredor de fabrica, banco de madeira embaixo, parede lisa (gerada IA - carrossel 117 v2, ninguem acorda animado pra bater ponto) | objeto-metafora, ambiente | topo |
| 463.png | Dono de avental atras do balcao de uma loja de ferragens falando com as maos pra quatro funcionarios em roda, dois sorrindo (gerada IA - carrossel 117 v2, gente so acorda com vontade pra um lugar onde aprende, ganha, tem orgulho e se diverte) | pessoa, cena-de-trabalho | topo |
| 464.png | Barbeiro velho guiando a mao do aprendiz com a tesoura sobre o cliente sentado, envelope no balcao (gerada IA - carrossel 117 v2, teste 1 e 2: aprende? da pra sonhar com o salario?) | pessoa, cena-de-trabalho | topo |
| 465.png | Quatro pedreiros sentados numa viga de concreto com as marmitas na hora do almoco, um rindo alto de cabeca pra tras, outro apontando (gerada IA - carrossel 117 v2, teste 3 e 4: orgulho? gente rindo?) | pessoa, composicao-conceitual | topo |
| 466.png | Dono de costas no escritorio de vidro, mao na nuca, olhando pela janela interna o chao de fabrica com dois funcionarios na bancada (gerada IA - carrossel 117 v2, grito: clima ruim tem dono) | pessoa, composicao-conceitual | topo |
| 467.png | Tres funcionarios rindo enquanto levantam juntos a porta de enrolar da loja na segunda de manha (gerada IA - carrossel 117 v2, time que chega na segunda com vontade) | pessoa, cena-de-trabalho | topo |
| 468.png | Dono de loja de ferragens de bracos cruzados olhando pra camera, dois funcionarios de avental atras no balcao, um sorrindo pra ele (gerada IA - carrossel 117 v2, oferta: aplicar os quatro pilares comigo) | pessoa, cena-de-trabalho | topo |
| 469.png | Noite: homem no sofa curvado pra frente com a mao no cabelo e o rosto tenso de perfil, TV de tubo com o letreiro FANTASTICO sobre o globo, janela escura com cortina, abajur aceso, uniforme pendurado na porta, sem relogio (gerada IA - carrossel 117 v4, domingo a noite: angustia, pedido do user) | pessoa, composicao-conceitual | topo |
| 470.png | Dono de avental atras do balcao da torrefacao olhando pra baixo o envelope de pagamento vazio aberto nas maos, torrador e sacos atras (gerada IA - carrossel 120, capa: empresa que nao remunera o dono nao serve pra nada) | pessoa, cena-de-trabalho | topo |
| 471.png | Dia de pagamento na torrefacao: fila de quatro trabalhadores de avental e boina com envelopes na mao, o dono atras do balcao de maos vazias (gerada IA - carrossel 120, todo mundo recebe antes de voce) | pessoa, cena-de-trabalho | topo |
| 472.png | Still fechado: quatro envelopes kraft grossos em pe lado a lado e um quinto vazio e achatado no fim, parede lisa atras, sem cenario (v2) (gerada IA - carrossel 120, dia 5, 10, 20, 30: voce fica com o resto) | objeto-metafora, ambiente | topo |
| 473.png | Still: lata de folha de flandres do caixa aberta e vazia no balcao, tampa ao lado, graos de cafe espalhados (gerada IA - carrossel 120, faltou dinheiro? problema teu) | objeto-metafora, ambiente | topo |
| 474.png | Tres maos estendidas por cima do balcao com a palma pra cima vindas de fora do quadro: manga de avental, punho de camisa com abotoadura, manga de terno; parede lisa (gerada IA - carrossel 120, funcionario, banco e governo nao aceitam) | composicao-conceitual, maos | topo |
| 475.png | Noite: dono sozinho sentado num saco de cafe no chao do galpao com o envelope vazio nas maos, torrador apagado e lampada nua atras (gerada IA - carrossel 120, trabalhar o mes de graca voce aceita) | pessoa, composicao-conceitual | topo |
| 476.png | Dono de costas, boina e avental, parado diante de uma pilha larga de sacos de juta, parede lisa em cima (gerada IA - carrossel 120, estou reinvestindo, quando valer mais eu tiro) | pessoa, composicao-conceitual | topo |
| 477.png | Escritorio da torrefacao: tres homens de terno sentados na mesa do dono com papeis, o dono de avental em pe no canto encostado na parede, fora da mesa (gerada IA - carrossel 120, papo de empresa grande, de startup) | pessoa, composicao-conceitual | topo |
| 478.png | Still: close de cadeado de ferro fechado numa corrente na porta de ferro, chapa clara lisa subindo ate o topo (gerada IA - carrossel 120, se a sua falir quem perde e voce) | objeto-metafora, ambiente | topo |
| 479.png | Dono de avental, esposa de vestido e filho pequeno de pe na frente da parede lisa da casa, serios olhando pra camera, caminhonete velha ao lado (gerada IA - carrossel 120, casa, carro, familia, CPF em jogo) | pessoa, composicao-conceitual | topo |
| 480.png | Dono sozinho atras do balcao, boina e avental, olhando pra camera com meio sorriso e guardando o envelope grosso no bolso da camisa, torrador e sacos atras (v2; a v1 com a fila de trabalhadores reprovada: parecia que o dono enriquece do trabalho dos outros) (gerada IA - carrossel 120, soberano recebe primeiro) | pessoa, cena-de-trabalho | topo |
| 481.png | Still: balanca de pratos de ferro no balcao com cafe em grao num prato e pesos de latao no outro, torrador e escritorio ao fundo (gerada IA - carrossel 120, dividendo e a primeira conta) | objeto-metafora, ambiente | topo |
| 482.png | Dono trinta anos depois, cabelo branco, avental, atras do mesmo balcao olhando dentro do envelope vazio; fila de trabalhadores jovens com envelopes ao lado (gerada IA - carrossel 120, grito: o que nao paga hoje nao vale nada amanha) | pessoa, cena-de-trabalho | topo |
| 483.png | Dono sentado na mesa do escritorio com a caneta parada e a mao na testa diante de uma folha em branco, abajur aceso, torrefacao ao fundo (gerada IA - carrossel 120, quanto a sua empresa te pagou pelo risco?) | pessoa, composicao-conceitual | topo |
| 484.png | Still: molho de chaves de casa e chave de carro ao lado de um envelope kraft vazio no balcao, graos de cafe, torrefacao ao fundo (gerada IA - carrossel 120, grito: o risco e todo seu, o dinheiro nao) | objeto-metafora, ambiente | topo |
| 485.png | Dono de boina e avental de bracos cruzados ouvindo um homem de camisa clara que aponta pros sacos, junto ao torrador (gerada IA - carrossel 120, oferta: treinamento) | pessoa, cena-de-trabalho | topo |
| 486.png | Still fechado: envelope kraft cheio deitado no balcao de madeira ao lado de uma caneca esmaltada de cafe, parede lisa atras (gerada IA - carrossel 120, CTA: comenta SOBERANO) | objeto-metafora, ambiente | topo |
| 487.png | Dono sentado na mesa do escritorio com as duas maos no rosto, cansado; tres crachas e um curriculo na mesa, telefone de disco, parede lisa atras (gerada IA - carrossel 119, capa: cansei de demitir vendedor) | pessoa, cansaco, escritorio-anos-70 |
| 488.png | Vendedor novo de paleto grande demais ao telefone de disco, perdido; dono de bracos cruzados logo atras, parede lisa (gerada IA - carrossel 119, terceiro nome no mesmo cracha) | pessoa, cena-de-trabalho, escritorio-anos-70 |
| 489.png | Still: tres fichas de proposta lado a lado na mesa com a mesma rasura, caneta; cadeira com paleto, carros na janela (gerada IA - carrossel 119, tres demitidos, o mesmo erro) | objeto-metafora, escritorio-anos-70 |
| 490.png | Still fechado: cadeira giratoria vazia com paleto no encosto, telefone fora do gancho na mesa, parede lisa (gerada IA - carrossel 119, grito: demitiu quem estava sentado em cima do problema) | objeto-metafora, ausencia |
| 491.png | Still fechado: plaquinha de mesa com nome novo colado por cima do antigo, telefone de disco e cinzeiro (gerada IA - carrossel 119, a vaga passa o erro pra quem senta) | objeto-metafora, escritorio-anos-70 |
| 492.png | Dono sozinho a noite sob a luminaria, pilha de curriculos e livro-caixa, mao na testa, cofre ao lado (gerada IA - carrossel 119, demitir e o remedio mais caro) | pessoa, noite, escritorio-anos-70 |
| 493.png | Still: sedan anos 70 empoeirado com placa de preco no para-brisa, sozinho na vaga marcada do patio, parede lisa atras (gerada IA - carrossel 119, grito: outro elenco, mesmo roteiro) | objeto-metafora, carro, patio |
| 494.png | Dono com a mao no capo explicando pro vendedor novo com bloco de notas, carros do patio atras (gerada IA - carrossel 119, gente pronta quem forma e voce) | pessoa, cena-de-trabalho, patio |
| 495.png | Still: folha manuscrita colada na parede ao lado do quadro de giz com tracinhos, encosto da cadeira embaixo (gerada IA - carrossel 119, conserta a vaga que voce ja tem) | objeto-metafora, escritorio-anos-70 |
| 496.png | Still: sala de reuniao vazia, caderno fechado com lapis na mesa, cadeiras afastadas, quadro de giz meio apagado (gerada IA - carrossel 119, treinar sem acompanhar nao adianta nada) | objeto-metafora, ausencia |
| 497.png | Dono apontando uma linha do quadro de giz pro vendedor com xicara de cafe, de manha, carros na janela (gerada IA - carrossel 119, grito: a parte mais dificil e acompanhar todo santo dia) | pessoa, cena-de-trabalho |
| 498.png | Still fechado: quadro de giz com tracinhos por dia da semana, apagador e giz na canaleta; cabideiro com paleto e carros ao fundo (gerada IA - carrossel 119, rito diario, tres perguntas) | objeto-metafora, rotina |
| 499.png | Dono em pe ao lado do vendedor sentado preenchendo a proposta, os dois olhando a ficha, carros na janela (gerada IA - carrossel 119, dono normal que faz o basico bem feito) | pessoa, cena-de-trabalho |
| 500.png | Homem de paleto e bigode ensinando um vendedor jovem com bloco diante dos carros do patio, escritorio de vidro ao fundo (gerada IA - carrossel 119, a proxima troca e por crescimento) | pessoa, patio |
| 501.png | Dono de camisa e gravata frouxa em pe na porta do escritorio de vidro olhando o patio rodar: vendedores com clientes junto aos carros (gerada IA - carrossel 119, oferta: treinamento) | pessoa, patio |
| 502.png | Dono sentado na cadeira do vendedor olhando pra camera, plaquinha de mesa virada pra frente, cracha em branco na mesa (gerada IA - carrossel 119, CTA: comenta RAIZ) | pessoa, olhar-para-camera |
| 516.png | Close: mao de homem com a manga arregacada erguendo uma acha de lenha como se fosse um porrete, contra a parede lisa (gerada IA - carrossel 122, capa: lenha no seu funcionario; o recorte enganoso) | maos, objeto-metafora, lenha |
| 517.png | O zoom out da capa: dono de joelhos pondo a acha na lareira acesa e o funcionario agachado esquentando as maos ao lado (gerada IA - carrossel 122, ninguem esta mandando bater; a realidade do recorte) | pessoa, lareira, ensino |
| 518.png | Caricatura do patrao explorador: homem gordo de terno risca de giz e charuto atras de escrivaninha polida em escritorio de vidro (gerada IA - carrossel 121, patrao explorador nao mora na sua rua) | pessoa, caricatura, contraste |
| 519.png | Still: relogio de ponto antigo na parede com o cartao enfiado e o porta-cartoes ao lado, sem numeros nem texto (gerada IA - carrossel 122, 8 horas por dia com voce) | objeto-metafora, still, relogio-de-ponto |
| 520.png | Still fechado: pasta do banco com papel ilegivel, molho de chaves da casa, chave do carro e caminhaozinho de lata na mesa da cozinha (gerada IA - carrossel 121, casa, carro e familia na aposta) | objeto-metafora, still, casa |
| 521.png | Moca costurando numa maquina de manivela na mesa da cozinha a noite, filha pequena dormindo na cadeira ao lado (gerada IA - carrossel 121 v2 imagens soltas, empreender nao e luxo, e saida) | pessoa, casa, comeco |
| 522.png | Still: carteira de couro velha lotada de notas dobradas saindo por todas as dobras, chaves da loja ao lado (gerada IA - carrossel 121 v3, regra numero 1: bolso do dono) | objeto-metafora, still, bolso |
| 523.png | Entulho de caixas, latas, sacos e tabuas de prateleira desabada, so uma mao e o antebraco saindo de baixo da pilha (gerada IA - carrossel 121 v3, quando a casa cai, cai em cima de voce) | objeto-metafora, soterrado, queda |
| 524.png | Fila de emprego no portao de uma fabrica, o ex-dono de camisa branca com pasta no peito entre homens de bone (gerada IA - carrossel 121 v2 imagens soltas, fecha e vai trabalhar pros outros) | pessoa, derrota, trabalhar-pros-outros |
| 525.png | Close de uma mao de trabalhador aberta com quatro moedas gastas na palma, punho de camisa de trabalho, parede lisa (gerada IA - carrossel 121 v3, nao estou falando de pro-labore: pro-labore e troco) | mao, moedas, troco |
| 526.png | Dono de mercearia de avental e gerente de gravata lado a lado atras do balcao, cada um com um envelope kraft identico (gerada IA - carrossel 121 v2 imagens soltas, pro-labore nao e salario de dono) | pessoa, contraste, envelope |
| 527.png | A venda no balcao da loja de tecidos: dono com fita metrica entregando o pacote e recebendo as notas de perfil da cliente (gerada IA - carrossel 121 v2 imagens soltas, lucro entra no preco antes de vender) | pessoa, venda, negocio |
| 528.png | Mao aberta com a palma pra cima e a cinza fria voando ao vento em riscos e redemoinhos, contra a parede lisa (gerada IA - carrossel 122, quem confunde os dois passa a vida soprando cinza) | maos, objeto-metafora, cinzas |
| 529.png | Still: balde de lata no chao do deposito aparando o pingo de um cano enferrujado, caixas ao lado (gerada IA - carrossel 121 v2 imagens soltas, o dinheiro que escapa) | objeto-metafora, still, vazamento |
| 530.png | Dono de avental de bracos cruzados ouvindo homem de camisa clara que aponta um caderno aberto, balcao de ferragens (gerada IA - carrossel 121 v2 imagens soltas, oferta: remunerado hoje) | pessoa, oferta, conversa |
| 531.png | Still: gaveta de madeira do balcao aberta com um envelope kraft cheio dentro, ao lado das chaves da loja (gerada IA - carrossel 121 v2 imagens soltas, CTA: comenta REMUNERADO) | objeto-metafora, still, cta |
| 503.png | Escritorio de vendas anos 70 em extase: seis homens de terno e gravata frouxa gritando de alegria, o do centro em pe na mesa com os punhos pro alto, papeis voando (gerada IA - carrossel 116, capa: a alma come outra coisa; energia estilo lobo de wall street) | pessoa, celebracao, energia, escritorio |
| 504.png | Still: envelope de pagamento pardo lacrado e caixa de cesta basica em pacotes de papel sobre toalha xadrez de cozinha, caneca de lata (gerada IA - carrossel 116, quite com o bolso) | objeto-metafora, still, cozinha |
| 505.png | Dono de camisa com a mao no ombro do operario jovem de macacao, os dois de perfil, tres operarios olhando ao fundo, chao de fabrica (gerada IA - carrossel 116, a alma come reconhecimento) | pessoa, cena-de-trabalho, fabrica |
| 506.png | Extase da premiacao na festa da empresa: jovem erguendo o trofeu, sorriso aberto, confete no ar, colegas aplaudindo em volta (gerada IA - carrossel 116, perspectiva e proposito) | pessoa, celebracao, confete |
| 507.png | Still: escritorio do dono a noite, mesa com luminaria acesa, cadeira vazia, livro-caixa aberto (ilegivel), telefone de disco, caneca (gerada IA - carrossel 116, ninguem nunca fez isso por ele) | objeto-metafora, still, escritorio, solidao |
| 508.png | Confeccao: costureira jovem ergue o vestido pronto esperando uma palavra; o dono passa de costas anotando na prancheta sem olhar (gerada IA - carrossel 116, empresa onde ninguem e reconhecido: a negligencia repetida) | pessoa, cena-de-trabalho, confeccao |
| 509.png | Still: lareira de tijolo apagada com cinza fria e duas achas carbonizadas, lenha empilhada ao lado, poltrona vazia com manta dobrada (gerada IA - carrossel 116, cobra calor de um time que nunca alimentou) | objeto-metafora, still, lareira, sala |
| 510.png | Maos calejadas pondo mais uma acha na lareira de tijolo com o fogo alto, faiscas e brasa (gerada IA - carrossel 116, alimente a fogueira) | maos, fogo, lareira |
| 511.png | Dono entregando trofeu pequeno a um operario de macacao na frente do time que aplaude, mural de cortica com fotos atras (gerada IA - carrossel 116, e rito) | pessoa, cena-de-trabalho, rito |
| 512.png | Still: o lugar de honra da sala de casa: trofeu polido no centro do aparador sobre paninho de croche, foto da familia, abajur aceso, radio, planta (gerada IA - carrossel 116, o trofeu na mesa dele) | objeto-metafora, still, casa, trofeu |
| 513.png | Operario jovem de macacao em pe na frente do torno, bracos cruzados, peito estufado, sorriso contido olhando pra camera (gerada IA - carrossel 116, trabalha por orgulho) | pessoa, orgulho, olhar-para-camera |
| 514.png | Reuniao da manha no chao de fabrica: dono de prancheta falando pro time de cinco operarios em semicirculo, apontando com a mao aberta (gerada IA - carrossel 116, fechamento: rotina) | pessoa, cena-de-trabalho, reuniao |
| 515.png | De costas: a mao calejada do mais velho no ombro do rapaz de macacao, sem rostos, contra a parede lisa (gerada IA - carrossel 116, CTA: comenta ORGULHO) | maos, gesto, de-costas |
| 516.png | Close: mao de homem com a manga arregacada erguendo uma acha de lenha como se fosse um porrete, contra a parede lisa (gerada IA - carrossel 122, capa: lenha no seu funcionario; o recorte enganoso) | maos, objeto-metafora, lenha |
| 517.png | O zoom out da capa: dono de joelhos pondo a acha na lareira acesa e o funcionario agachado esquentando as maos ao lado (gerada IA - carrossel 122, ninguem esta mandando bater; a realidade do recorte) | pessoa, lareira, ensino |
| 518.png | Dono de bracos cruzados, impaciente, em pe na frente da lareira de tijolo apagada (gerada IA - carrossel 122, voce quer fogo?) | pessoa, lareira |
| 519.png | Still: relogio de ponto antigo na parede com o cartao enfiado e o porta-cartoes ao lado, sem numeros nem texto (gerada IA - carrossel 122, 8 horas por dia com voce) | objeto-metafora, still, relogio-de-ponto |
| 520.png | Mao abanando com abano de palha a cinza fria de uma lareira, poeira de cinza subindo, nenhuma chama (gerada IA - carrossel 122, sopro em cima de cinza) | maos, objeto-metafora, lareira |
| 521.png | Dono sentado na poltrona com manta no colo esfregando as maos na frente da lareira apagada (gerada IA - carrossel 122, esperando calor) | pessoa, lareira, sala |
| 522.png | Mestre sentado ao lado do jovem aprendiz na bancada, as maos dele guiando as maos do jovem na plaina (gerada IA - carrossel 122, sentar do lado e mostrar como faz) | pessoa, cena-de-trabalho, ensino |
| 523.png | Fileira de patos de madeira identicos na bancada e as maos do aprendiz entalhando mais um igual (gerada IA - carrossel 122, tarefa por tarefa, rito por rito) | maos, repeticao, oficina |
| 524.png | Funcionario de macacao sozinho de madrugada levantando a porta de enrolar da loja, rua escura com coqueiro (gerada IA - carrossel 122, se compromete porque quer) | pessoa, de-costas, madrugada |
| 525.png | Maos empilhando achas com cuidado dentro da lareira ainda apagada, caixa de fosforos ao lado (gerada IA - carrossel 122, lenha primeiro, calor depois) | maos, lareira |
| 526.png | Still: lareira de tijolo em chamas altas e a poltrona vazia com a manta na frente dela, lenha ao lado (gerada IA - carrossel 122, o fogo se espalha sozinho) | objeto-metafora, still, fogo, lareira |
| 527.png | Still: fogueira ao ar livre encharcada de chuva, achas pretas e molhadas, cinza escorrendo, folhas grudadas, nenhuma brasa (gerada IA - carrossel 122, fogueira apagada) | objeto-metafora, still, chuva |
| 528.png | Mao aberta com a palma pra cima e a cinza fria voando ao vento em riscos e redemoinhos, contra a parede lisa (gerada IA - carrossel 122, quem confunde os dois passa a vida soprando cinza) | maos, objeto-metafora, cinzas |
| 529.png | Dono de joelhos acendendo a lareira da oficina com um fosforo de manha cedo, tres operarios chegando atras tirando o casaco (gerada IA - carrossel 122, rotina de gestao) | pessoa, cena-de-trabalho, rito |
| 530.png | Time de operarios e o dono em semicirculo em volta de uma fogueira grande a noite, maos estendidas pro fogo, rostos iluminados, rindo (gerada IA - carrossel 122, CTA: comenta LENHA) | pessoa, celebracao, fogo |
| 532.png | Homem de cinquenta anos no balcao de um boteco com xicara de cafe, cotovelos no balcao, olhando pra camera, serio, parede lisa (gerada IA - carrossel 123, abertura: vou te falar uma verdade meio chata) | pessoa, olhar-para-camera |
| 533.png | Cozinha simples de madrugada: homem de roupa de trabalho tomando cafe em pe, mulher servindo com bule esmaltado, filho de pijama com caderno na mesa (gerada IA - carrossel 123, gancho: ninguem acorda cedo pelo sonho do outro) | pessoa, familia, casa |
| 534.png | Dono sozinho a noite no escritorio da propria empresa, so a luminaria acesa, olhando a sala vazia com cadeiras encostadas (gerada IA - carrossel 123, so voce sonha com ela) | pessoa, noite, solidao |
| 535.png | Trabalhador de uniforme no onibus quase vazio de madrugada, testa na janela, olhos fechados, marmita no colo (gerada IA - carrossel 123, grito: ele trabalha pelo sonho dele) | pessoa, onibus, cotidiano |
| 536.png | Still: foto antiga emoldurada na mesa, homem jovem sozinho diante da loja com porta de enrolar e fita de inauguracao; caneta e xicara ao lado (gerada IA - carrossel 123, ninguem do time estava la) | objeto-metafora, memoria |
| 537.png | Ponte de tabuas sobre corrego no interior, homem de roupa de trabalho e chapeu atravessando de lado com sacola no ombro, ceu claro (gerada IA - carrossel 123, a sua empresa e a ponte) | pessoa, ponte, interior |
| 538.png | Ponte de tabuas vista de tras: dois homens atravessando lado a lado, um de camisa social e outro de uniforme, de costas (gerada IA - carrossel 123, grito: sua empresa e o seu sonho e a ponte para o sonho dele) | pessoa, de-costas, ponte |
| 539.png | Still: ponte de tabuas com duas tabuas quebradas no meio e trilha de terra contornando o corrego ao lado (gerada IA - carrossel 123, quando ela para de levar ele encontra outro caminho) | objeto-metafora, ponte, caminho |
| 540.png | Dono e funcionario sentados do mesmo lado da mesa, o dono ouvindo com caderno aberto e caneta parada, o funcionario falando com as maos (gerada IA - carrossel 123, lider sabe pra onde cada um quer ir) | pessoa, escuta, cena-de-trabalho |
| 541.png | Still: relogio de ponto mecanico de parede com a estante de cartoes ao lado, um cartao amarelado e gasto entre cartoes novos (gerada IA - carrossel 123, trocar gente ou formar gente que fica) | objeto-metafora, tempo, rotina |
| 542.png | Dono na porta de uma oficina pequena olhando o time trabalhar: um funcionario experiente ensinando um mais novo na bancada (gerada IA - carrossel 123, oferta: treinamento) | pessoa, oficina, cena-de-trabalho |
| 543.png | Dono sentado no degrau da porta da propria loja no fim do dia, porta de enrolar meio baixada atras, olhando pra camera (gerada IA - carrossel 123, CTA: comenta PONTE) | pessoa, olhar-para-camera |
| 544.png | Galpao de distribuidora de bebidas: dono de prancheta frente a frente com funcionario grandalhao de bracos cruzados e queixo erguido, caixotes e paleteira atras (gerada IA - carrossel 125, capa: convencer um adulto a fazer o trabalho dele) | pessoa, confronto, galpao |
| 545.png | Escritorio de grafica: dono sentado com a mao levantada no meio da frase, funcionario de costas saindo pela porta (gerada IA - carrossel 125, sem ele achar que e pessoal) | pessoa, escritorio, saida |
| 546.png | Balcao de farmacia: dono de jaleco falando baixo e encolhido, funcionaria de uniforme branco de bracos cruzados olhando pro lado (gerada IA - carrossel 125, voce ja cobra pedindo desculpa) | pessoa, balcao, confronto |
| 547.png | Still: mesa de copa depois da festinha, bolo cortado, xicaras usadas, guardanapos, baloes murchos; lousa com tabela vazia na parede (gerada IA - carrossel 125, manter o clima) | objeto-metafora, still, copa |
| 548.png | Dono de camiseta regata sentado na beira da cama de madrugada, cotovelos nos joelhos, telefone apagado na mao, abajur baixo (gerada IA - carrossel 125, acho que eu nao sei explicar) | pessoa, noite, insonia |
| 549.png | Still: folha em branco presa com fita na parede de uma marcenaria e a mao apontando o dedo pra ela, serragem embaixo (gerada IA - carrossel 125, grito: cobranca so vira pessoal quando nao tem combinado) | maos, objeto-metafora, papel |
| 550.png | Borracharia: dois homens frente a frente, os dois de dedo em riste ao mesmo tempo, pneu de caminhao entre eles (gerada IA - carrossel 125, opiniao contra opiniao e briga de gente) | pessoa, confronto, borracharia |
| 551.png | Still: porta de vidro fosco entreaberta com a sombra de um homem parado do outro lado; na mesa, livro-caixa aberto, caneta largada e xicara (gerada IA - carrossel 125, cobranca de surpresa parece perseguicao) | objeto-metafora, still, sombra |
| 552.png | Escritorio de transportadora: dono e funcionario sentados do mesmo lado da mesa olhando uma folha, o dono apontando uma linha com a caneta (gerada IA - carrossel 125, voce nao cobra a pessoa, cobra a pagina) | pessoa, escuta, cena-de-trabalho |
| 553.png | Sala de reuniao de manha: cinco pessoas de pe em volta de um quadro branco com tabela, xicaras na mao, o dono apontando (gerada IA - carrossel 125, mesma hora, mesmo numero, todo mundo na mesa) | pessoa, reuniao, rito |
| 554.png | Still: relogio redondo de fabrica marcando oito horas e, embaixo, prancheta pendurada num prego com folha em branco, parede lisa (gerada IA - carrossel 125, grito: cobranca sem regra e perseguicao, com rito e gestao) | objeto-metafora, still, tempo, rotina |
| 555.png | Still: caneta-tinteiro sobre folha manuscrita com duas assinaturas no pe, mesa de madeira gasta com marca de xicara e cinzeiro (gerada IA - carrossel 125, e sobre o combinado, e quem escreve e voce) | objeto-metafora, still, papel |
| 556.png | Fabrica de estofados: dono calmo na cabeceira da mesa comprida com prancheta debaixo do braco, quatro operarios grampeando tecido em cadeiras (gerada IA - carrossel 125, oferta: treinamento) | pessoa, oficina, cena-de-trabalho |
| 557.png | Still: prancheta pendurada no gancho da parede de um galpao, folha com linhas manuscritas e caneta amarrada por barbante, luz de fim de tarde (gerada IA - carrossel 125, CTA: comenta COMBINADO) | objeto-metafora, still, papel |
| 558.png | Still: onibus urbano anos 60 parado de frente pra um muro no fim de uma rua de terra, porta aberta, ninguem dentro, ceu chapado (gerada IA - carrossel 126, capa: onibus que vai pro fim da rua x foguete pra lua) | objeto-metafora, still, veiculo, fim-de-linha |
| 559.png | Operarios de uniforme vistos de costas num campo aberto olhando um foguete pequeno subindo no horizonte (gerada IA - carrossel 126, gente boa e atraida por crescimento) | pessoa, de-costas, foguete, horizonte |
| 560.png | Dono de camisa de manga curta sozinho na mesa de entrevista, pasta fechada, cadeira do outro lado vazia, olhando o relogio de parede sem numeros (gerada IA - carrossel 126, chance de contratar quase nenhuma) | pessoa, espera, escritorio |
| 561.png | Still: mesa vazia de funcionario que saiu, gaveta aberta e vazia, chaves e cracha em branco em cima, caneca, cadeira encostada (gerada IA - carrossel 126, o melhor pediu a conta) | objeto-metafora, still, mesa, vazio |
| 562.png | Dono e tres operarios de perfil no patio da fabrica, o dono com o braco esticado apontando pra longe e os tres olhando na direcao (gerada IA - carrossel 126, meta e pra bater, sonho e pra puxar) | pessoa, cena-de-trabalho, direcao |
| 563.png | Quatro homens de camisa branca e gravata debrucados numa mesa de desenho com uma planta enorme, reguas e lapis (gerada IA - carrossel 126, ninguem chega na lua sozinho) | pessoa, reuniao, plano |
| 564.png | Balcao do pagamento de fabrica: operario jovem de macacao abrindo envelope kraft grosso com sorriso largo, colega espiando (gerada IA - carrossel 126, ele ganha mais, cresce, se realiza) | pessoa, dinheiro, alegria |
| 565.png | Still: aquario pequeno e raso com dois dedos de agua, um peixinho parado e um castelinho de plastico maior que o peixe, mesa de madeira (gerada IA - carrossel 126, grito: voce nao segura tubarao em aquario raso) | objeto-metafora, still, aquario, raso |
| 566.png | Funcionario de deposito dormindo ao meio-dia numa pilha de sacos de juta, bone sobre o rosto, maos na barriga (gerada IA - carrossel 126, no raso fica quem cabe no raso) | pessoa, sem-rosto, deposito, preguica |
| 567.png | Aquario publico: tubarao grande passando colado no vidro e um menino de costas com a mao espalmada no vidro (gerada IA - carrossel 126, toda profundidade vem com pressao) | pessoa, de-costas, tubarao, profundidade |
| 568.png | Still: capacete de escafandro de cobre riscado num banco de conves, mangueira de ar enrolada e luvas de couro ao lado, mar ao fundo (gerada IA - carrossel 126, o tubarao aguenta, peixe de aquario nao) | objeto-metafora, still, mergulho, pressao |
| 569.png | Still: aviao bimotor antigo abandonado no mato, pneu murcho, capim nas rodas, escada encostada na porta fechada (gerada IA - carrossel 126, grito: ninguem embarca num aviao que nao vai decolar) | objeto-metafora, still, aviao, abandono |
| 570.png | Chao de fabrica as sete da manha: time de uniforme de pe em meio circulo e o dono no meio com a prancheta falando, reuniao de pe (gerada IA - carrossel 126, cria um rito e acompanha todo dia) | pessoa, reuniao, rito, cena-de-trabalho |
| 571.png | Dono de pe ao lado de uma folha grande presa na parede apontando com o lapis, quatro funcionarios sentados olhando (gerada IA - carrossel 126, oferta: treinamento) | pessoa, reuniao, plano |
| 572.png | Close das maos de um homem numa bancada montando um foguete de lata grande feito a mao, chave de fenda, rebites e martelo em volta (gerada IA - carrossel 126, CTA: a sua parte e construir o foguete, comenta FOGUETE) | maos, objeto-metafora, foguete, oficina |
| 573.png | Still: foguete no instante do lancamento visto de muito longe numa planicie vazia, clarao na base, fumaca rente ao chao, torre ao lado, ceu chapado (gerada IA - carrossel 126, grito: todo mundo quer estar num foguete que vai pra lua) | objeto-metafora, still, foguete, horizonte |
| 531.png | Dono de avental atras do balcao atendendo tres clientes de costas, telefone no ombro, caneta na boca, mesa de dono vazia ao fundo (gerada IA - carrossel 127, capa: trabalha demais e comanda de menos) | pessoa, cena-de-trabalho, balcao |
| 532.png | Dono de costas puxando a porta de enrolar da loja pra baixo, fachada lisa (gerada IA - carrossel 127, das sete as nove) | pessoa, de-costas, porta-de-enrolar |
| 533.png | Still: prego na parede com pilha de papeis e boletos espetados transbordando, telefone de disco fora do gancho na prateleira (gerada IA - carrossel 127, gargalo) | objeto-metafora, still |
| 534.png | Still: mesa de dono vazia com cadeira encostada, luminaria apagada, livro-caixa fechado com caneta em cima (gerada IA - carrossel 127, ninguem pensa na empresa) | objeto-metafora, still, escritorio |
| 535.png | Still: motor de caminhao antigo com o capo aberto, correias em movimento (gerada IA - carrossel 127, motor nao escolhe pra onde vai) | objeto-metafora, still, motor |
| 536.png | Still: cabine de caminhao antigo vista pela janela, volante e banco vazios, chave na ignicao (gerada IA - carrossel 127, o volante esta sem ninguem) | objeto-metafora, still, caminhao |
| 537.png | Dono sem avental apontando um quadro de giz cheio de numeros pra tres funcionarios de avental (gerada IA - carrossel 127, trabalhar x comandar) | pessoa, cena-de-trabalho, quadro |
| 538.png | Still: quatro pares de luvas de trabalho em fila na bancada com o chapeu de feltro do dono no centro (gerada IA - carrossel 127, braco se contrata, cabeca e a sua) | objeto-metafora, still |
| 539.png | Still: relogio de ponto com um cartao mais gasto que os outros e marca de xicara, chave grande da loja pendurada ao lado (gerada IA - carrossel 127, dono nao pode ser CLT) | objeto-metafora, still, relogio-de-ponto |
| 540.png | Dono no banco do motorista do caminhao com as maos no volante olhando pra frente, time carregando a carroceria atras (gerada IA - carrossel 127, sai do balcao e senta no volante) | pessoa, caminhao, volante |
| 541.png | Dono debrucado no motor do caminhao com uma lanterna acesa iluminando as pecas (gerada IA - carrossel 127, ninguem assume um volante sem conhecer o carro: raio-x) | pessoa, motor, lanterna |
| 542.png | Still: volante do caminhao visto do banco do motorista, painel com mostradores e a chave na ignicao com chaveiro de couro, parede lisa atras (gerada IA - carrossel 127, CTA: comenta RAIO-X) | objeto-metafora, still, volante |
| 574.png | Sapataria: dono de pe ao lado da bancada apontando com o dedo um ponto da costura do sapato, sapateiro sentado olhando o ponto, prateleira de sapatos ao lado (gerada IA - carrossel 132 repost, capa: ser dono e ser chato) | pessoa, oficina, correcao |
| 575.png | Bar de bairro: o dono atras do balcao rindo com tres fregueses debrucados no balcao, copos e garrafa (gerada IA - carrossel 132 repost, se quer ser amado por todo mundo abre um bar) | pessoa, bar, riso |
| 576.png | Recepcao de hotel pequeno: dono com bloco na mao perguntando, recepcionista de uniforme mostrando uma linha do livro de registros (gerada IA - carrossel 132 repost, cobrar resultado e pedir numero) | pessoa, balcao, cobranca |
| 577.png | Still de maos: marmoraria, maos tirando do lote pronto a peca de marmore com lasca no canto, lote perfeito amarrado ao lado (gerada IA - carrossel 132 repost, combinado que nao e acompanhado vira sugestao) | maos, objeto-metafora, padrao |
| 578.png | Barbearia: barbeiro mais velho de pe atras do aprendiz guiando a mao dele com a tesoura no cliente sentado, espelho ao fundo (gerada IA - carrossel 132 repost, treinar de novo ate o padrao subir) | pessoa, ensino, barbearia |
| 579.png | Lavanderia: dono ao lado de funcionaria de touca refazendo a dobra de um lencol numa pilha torta, mesa comprida (gerada IA - carrossel 132 repost, ficar em cima, cultura nao nasce sozinha) | pessoa, cena-de-trabalho, acompanhamento |
| 580.png | Still: mesa do dono numa oficina de motos, cadeira vazia com casaco no encosto, livro-caixa aberto, chaves e xicara, moto e painel de ferramentas ao fundo (gerada IA - carrossel 132 repost, voce foi feito para comandar) | objeto-metafora, still, comando |
| 581.png | Acougue: dono de avental branco apontando o balcao de marmore por limpar, funcionario jovem de cabeca baixa com o pano na mao, carne no balcao (gerada IA - carrossel 132 repost, coragem de corrigir, confrontar, exigir) | pessoa, confronto, acougue |
| 582.png | Still: vestiario de fabrica com quadro de regras emoldurado e empoeirado na parede, armarios de metal abertos com uniformes jogados e botas no chao (gerada IA - carrossel 132 repost, baixo padrao no dono vira baixo padrao na empresa) | objeto-metafora, still, bagunca |
| 583.png | Still: bancada de sapataria com o servico de ontem intocado, sapato aberto, martelo, linha e caneca de cafe fria, luz da porta entrando de lado (gerada IA - carrossel 132 repost, se voce tolera atraso vai ter atraso) | objeto-metafora, still, atraso |
| 584.png | Recepcao do hotel: dono falando baixo ao lado da recepcionista apontando uma linha do livro, hospede esperando na ponta sem perceber, chaves na parede (gerada IA - carrossel 132 repost, cobrar, acompanhar, treinar) | pessoa, balcao, discricao |
| 585.png | Still: portao de galpao meio aberto calcado com um tijolo, cadeado aberto pendurado, caixas dentro (gerada IA - carrossel 132 repost, se voce nao assume o comando alguem assume) | objeto-metafora, still, portao |
| 586.png | Acougue: dono de avental branco atras do balcao de marmore, maos apoiadas no balcao, olhando pra camera, serio, pecas de carne ao lado (gerada IA - carrossel 132 repost, CTA: comenta CHATO) | pessoa, olhar-para-camera, acougue |
| 587.png | Acougue: dono de avental branco na porta do fundo, bracos cruzados, calmo, vendo dois funcionarios atenderem a fila no balcao, um embrulhando e outro pesando (gerada IA - carrossel 132 repost, oferta: treinamento) | pessoa, acougue, cena-de-trabalho |
| 588.png | Lagoa de sitio: pato branco de perfil andando na beira, pes na lama, agua baixa e ceu liso (gerada IA - carrossel 135 repost, capa: voce ja viu um pato) | animal, pato, lagoa, capa |
| 589.png | Lagoa de sitio: pato em voo rasante e desajeitado sobre a agua, asas abertas, pes esticados, gotas (gerada IA - carrossel 135 repost, voa anda nada mas nada bem feito) | animal, pato, lagoa, movimento |
| 590.png | Marcenaria: dono de avental no meio do galpao com prancheta numa mao e plaina na outra, olhando pro lado (gerada IA - carrossel 135 repost, empresario nao e especialista, e generalista) | pessoa, marcenaria, dono |
| 591.png | Marcenaria: dono debrucado na bancada ao lado do marceneiro apontando o encaixe de uma gaveta (gerada IA - carrossel 135 repost, precisa entender o suficiente pra comandar) | pessoa, marcenaria, apontar, ensinar |
| 592.png | Marcenaria: dono de costas na porta do escritorio entregando uma pasta ao contador sem olhar pra ele (gerada IA - carrossel 135 repost, delegar o que nao entende) | pessoa, de-costas, marcenaria, delegar |
| 593.png | Still: mesa de escritorio de marcenaria com livro-caixa fechado e empoeirado, notas espetadas num prego e caneca vazia (gerada IA - carrossel 135 repost, porque ele mesmo nao tem clareza) | objeto-metafora, still, livro-caixa |
| 594.png | Lagoa de sitio: pato saindo da agua pra margem, metade na agua e metade na lama, pingando (gerada IA - carrossel 135 repost, transitar em todas as areas) | animal, pato, lagoa |
| 595.png | Marcenaria: dono com as maos na plaina mostrando o movimento na tabua pro aprendiz jovem ao lado (gerada IA - carrossel 135 repost, aprende o basico e so depois delega) | pessoa, marcenaria, ensinar, aprendiz |
| 596.png | Still: gaveta de madeira montada torta que nao fecha, sobre a bancada, macete e formao ao lado (gerada IA - carrossel 135 repost, quem nao entende o jogo joga de qualquer jeito) | objeto-metafora, still, marcenaria |
| 597.png | Escritorio a noite: dono de costas na mesa, luminaria acesa, livro-caixa aberto, caneta parada (gerada IA - carrossel 135 repost, quanto entra quanto sai quanto sobra) | pessoa, de-costas, noite, livro-caixa |
| 598.png | Marcenaria: dono com tres dedos levantados falando pro time de quatro marceneiros de avental (gerada IA - carrossel 135 repost, LUCRO CAIXA GENTE) | pessoa, marcenaria, time, tres |
| 599.png | Marcenaria: dono mirando o veio de uma tabua erguida na altura do olho, um olho fechado (gerada IA - carrossel 135 repost, oferta: aula do raio-x) | pessoa, marcenaria, enxergar, raio-x |
| 600.png | Lagoa de sitio: pato parado na margem de frente, olhando pra camera, pes na lama, agua atras (gerada IA - carrossel 135 repost, CTA: comenta PATO) | animal, pato, olhar-pra-camera, cta |
| 601.png | Dono sozinho no escritorio a noite, mao na testa, papeis abertos sob a luminaria, mesas vazias atras (gerada IA - carrossel 137, capa: esse alguem e voce) | pessoa, escritorio, noite, decisao |
| 602.png | Madrugada na feira: homem forte de bone carregando caixote de verdura na caminhonete, sorrindo (gerada IA - carrossel 137, nao e o trabalho que tira o sono) | pessoa, feira, trabalho, madrugada |
| 603.png | Mesa de jantar em casa: esposa falando com as maos, filho comendo, o dono calado olhando pro prato (gerada IA - carrossel 137, decisao nao se divide) | pessoa, familia, silencio |
| 604.png | Still: pilha de envelopes de pagamento e caixa de dinheiro de lata aberta quase vazia, calculadora (gerada IA - carrossel 137, folha de sexta com caixa de quinta) | objeto-metafora, still, dinheiro, folha |
| 605.png | Still: criado-mudo com abajur aceso, molho de chaves da empresa, envelope kraft e copo d'agua cheio (gerada IA - carrossel 137, dorme com voce) | objeto-metafora, still, noite, insonia |
| 606.png | Homem de camiseta de costas na pia da cozinha a noite bebendo agua, casa apagada (gerada IA - carrossel 137, achei isso por anos, estava errado) | pessoa, de-costas, cozinha, noite |
| 607.png | Still: livro-caixa aberto com paginas em branco, lapis, oculos em cima, abajur aceso (gerada IA - carrossel 137, eu decidia no escuro) | objeto-metafora, still, caderno, numero |
| 608.png | Still: porta de enrolar de loja fechada ate a metade a noite com luz acesa dentro, rua vazia (gerada IA - carrossel 137, grito: noite em claro nao e preco de dono, e preco de decidir no escuro) | objeto-metafora, still, fachada, noite |
| 609.png | Dono de camiseta na mesa da cozinha de madrugada, caderno fechado, as duas maos no rosto, xicara vazia (gerada IA - carrossel 137, falta de fundamento, nao de coragem) | pessoa, cozinha, madrugada, angustia |
| 610.png | Still: caderno fechado com caneta em cima e despertador sem numeros no criado-mudo, luz da manha (gerada IA - carrossel 137, decide de dia e dorme de noite) | objeto-metafora, still, manha, caderno |
| 611.png | Manha: dono e tres do time de pe em volta da mesa com xicaras, caderno de numeros aberto, ele apontando uma linha (gerada IA - carrossel 137, cabe numa reuniao de manha) | pessoa, reuniao, rito |
| 612.png | Dono deitado na cama no escuro de olhos abertos olhando pro teto, esposa dormindo de costas ao lado (gerada IA - carrossel 137, ou numa madrugada te assombrando) | pessoa, quarto, insonia |
| 613.png | Dono dormindo de lado, tranquilo, abajur apagado e caderno no criado-mudo (gerada IA - carrossel 137, oferta: de dia, nao de madrugada) | pessoa, quarto, sono |
| 614.png | Dono na porta da empresa de manha cedo com xicara de cafe, descansado, olhando pra camera (gerada IA - carrossel 137, CTA: comenta DECISAO) | pessoa, fachada, manha |
| 615.png | Funcionario jovem dormindo pesado numa rede na varanda a noite, braco pendurado, chinelo caido, rosto escondido (gerada IA - carrossel 137, capa: seu funcionario dorme as 22h porque tem alguem decidindo por ele) | pessoa, sem-rosto, rede, sono |
| 616.png | Dono de camisa de manga curta sentado sozinho na cadeira de espera do banco, senha na mao, olhando pro chao (gerada IA - carrossel 140, hoje ela e um pessimo negocio) | pessoa, banco, espera |
| 617.png | Still: mesa de desenho com planta quase em branco, regua T e lapis (gerada IA - carrossel 140, e o modelo economico do seu negocio) | objeto-metafora, still, desenho, modelo |
| 618.png | Dono de perfil passando um maco de notas pela grade de um guiche de banco, so as maos do outro lado (gerada IA - carrossel 140, o primeiro a receber nao e voce) | pessoa, banco, guiche, dinheiro |
| 619.png | So maos: manga de terno com abotoadura pegando um maco de notas da mao calejada de manga arregacada (gerada IA - carrossel 140, capa: Selic nao quebrou sua empresa, so mostrou quem e o dono do seu lucro) | maos, sem-rosto, dinheiro, banco |
| 620.png | Barco de pesca tombado na lama com a mare baixa, casco a mostra, ceu liso (gerada IA - carrossel 140, aparece o que ele sempre foi) | objeto-metafora, barco, mare-baixa |
| 621.png | Still: viga de madeira grossa serrada, interior oco comido por cupim (gerada IA - carrossel 140, grito: juro alto nao quebra empresa boa, mostra qual era ruim) | objeto-metafora, still, madeira, cupim |
| 622.png | Fachada unica: dono de costas puxando a porta de enrolar pra baixo, vento e papeis voando, parede lisa em cima (gerada IA - carrossel 140, quem depende do banco cai primeiro) | pessoa, de-costas, porta-de-enrolar, vento |
| 623.png | Still: cofre pequeno de ferro aberto com um unico contrato dobrado dentro (gerada IA - carrossel 140, nao e seu, e alugado do banco) | objeto-metafora, still, cofre |
| 624.png | Still: balanca de dois pratos antiga em equilibrio, moedas de um lado e caderno fechado do outro (gerada IA - carrossel 140, isso nao e sorte, e desenho) | objeto-metafora, still, balanca, equilibrio |
| 625.png | Still: camisa de trabalho pendurada num prego na parede lisa, maco de notas dobrado no bolso e caneta (gerada IA - carrossel 140, empresa nasceu pra botar dinheiro no bolso do dono) | objeto-metafora, still, camisa, bolso, dinheiro |
| 626.png | Dono na mesa de dia redesenhando num caderno a lapis, concentrado (gerada IA - carrossel 140, oferta: ler e redesenhar o modelo economico) | pessoa, mesa, caderno, desenho |
| 627.png | Dono atras do balcao de madeira vazio, maos apoiadas, parede lisa atras, olhando pra camera (gerada IA - carrossel 140, CTA: comenta MODELO) | pessoa, balcao, olhar-pra-camera, cta |
| 628.png | Still: contrato aberto na mesa (ilegivel) com caneta-tinteiro e, em cima, chave do carro e chave da casa (gerada IA - carrossel 140, na sua quem assina o aval e voce) | objeto-metafora, still, contrato, aval, chaves |
| 629.png | Dono de farmacia de jaleco atras do balcao vazio, ombros erguidos, palmas pra cima, o gesto do 'e eu posso fazer o que?' (gerada IA - carrossel 141, capa: todo dono que quebra tem uma crise pra culpar, e nenhum tem uma DRE pra mostrar) | pessoa, farmacia, balcao, gesto, desculpa |
| 630.png | Fachada unica com duas lojas vizinhas sem letreiro: a da esquerda com a porta de enrolar fechada, a da direita aberta com cliente entrando de costas (gerada IA - carrossel 141, e ele continua de porta aberta) | fachada, porta-de-enrolar, concorrente, de-costas |
| 631.png | Dono de distribuidora entre engradados de garrafas rabiscando o preco num pedaco de papelao na palma da mao, lapis na orelha (gerada IA - carrossel 141, ele tinha numero, voce tinha achismo) | pessoa, deposito, engradados, achismo, preco |
| 632.png | Dono encostado no balcao da oficina-fabrica reclamando pra um amigo e apontando o polegar por cima do ombro pro funcionario de costas ao fundo (gerada IA - carrossel 141, a sua cultura e reclamar do funcionario) | pessoa, dois-homens, funcionario, reclamacao |
| 633.png | Still: prateleira de madeira vergada carregada de latas sem rotulo, escorada com cabo de vassoura e corda amarrada num prego (gerada IA - carrossel 141, grito: e fragil porque voce toca ela no achismo) | objeto-metafora, still, prateleira, gambiarra, latas |
| 634.png | Still: caixa de sapato transbordando de notas amassadas e papeis dobrados numa mesa de madeira, toco de lapis, caneca (gerada IA - carrossel 141, mas desculpa tem de sobra) | objeto-metafora, still, caixa-de-sapato, papeis, desorganizacao |
| 635.png | Dono de vidracaria de mangas dobradas parado diante de um espelho grande encostado na parede, olhando o proprio reflexo (gerada IA - carrossel 141, grito: e ela so muda quando o dono muda) | pessoa, espelho, reflexo, vidracaria |
| 636.png | Dono de grafica na cabeceira da mesa com tres funcionarios de avental, caderno aberto ilegivel, apontando uma linha com o dedo (gerada IA - carrossel 141, e rotina que cobra o time toda semana) | pessoa, grupo, reuniao, caderno, grafica |
| 637.png | Dono agachado de perfil levantando o canto de um tapete gasto numa loja vazia, assoalho podre com buraco embaixo (gerada IA - carrossel 141, a crise nao abriu o buraco, so te obrigou a olhar pra ele) | pessoa, tapete, buraco, assoalho, revelacao |
| 638.png | Dono andando entre engradados no deposito da distribuidora com prancheta na mao, contando e anotando, luz de dia (gerada IA - carrossel 141, oferta: dominar o lucro, o caixa e a rotina) | pessoa, deposito, prancheta, rotina, contagem |
| 639.png | Dono de grafica de avental, mangas dobradas, bracos cruzados diante da impressora antiga, olhando pra camera (gerada IA - carrossel 141, CTA: comenta DRE) | pessoa, grafica, bracos-cruzados, olhar-pra-camera, cta |
| 640.png | Envelope pardo de salario aberto com notas sobre balcao de madeira, molho de chaves da loja ao lado (gerada IA - carrossel 146, capa: nao e lucro, e o seu salario) | objeto, envelope, salario, dinheiro, chaves |
| 641.png | Homem mais velho de camisa branca apontando dois numeros a giz num quadro pequeno, plateia de costas (gerada IA - carrossel 146, eu uso o meu exemplo na imersao) | pessoa, grupo, sala-de-aula, quadro, treinamento |
| 642.png | Registradora antiga com a gaveta puxada e vazia, so um clipe (gerada IA - carrossel 146, dinheiro que nao existe) | objeto, registradora, gaveta-vazia, caixa |
| 643.png | Balanca de pratos de armazem: prato baixo cheio de moedas, prato alto vazio (gerada IA - carrossel 146, sobrou alguma coisa?) | objeto, balanca, moedas, vazio, comparacao |
| 644.png | Dono de mercearia no balcao com telefone no ombro, caderninho e troco na mao (gerada IA - carrossel 146, segura boleto, cliente, funcionario) | pessoa, balcao, telefone, sobrecarga, mercearia |
| 645.png | Operario de macacao saindo tranquilo da fabrica com marmita na mao (gerada IA - carrossel 146, e dormindo de noite) | pessoa, operario, marmita, tranquilidade, empregado |
| 646.png | Homem de costas subindo ladeira de paralelepipedo com saco enorme nas costas (gerada IA - carrossel 146, o risco voce carregou de graca) | pessoa, peso, saco, ladeira, esforco |
| 647.png | Dois envelopes pardos em pe e o mesmo maco de notas passando de um pro outro (gerada IA - carrossel 146, so mudou a geografia) | objeto, envelopes, dinheiro, transferencia |
| 648.png | Macacao de fabrica pendurado no gancho com cracha em branco, marmita no banco (gerada IA - carrossel 146, melhor ser empregado) | objeto, uniforme, cracha, marmita, empregado |
| 649.png | Cofre de ferro antigo fechado com a chave na fechadura (gerada IA - carrossel 146, o dividendo fica, vira patrimonio) | objeto, cofre, chave, patrimonio |
| 650.png | Dono agachado com lanterna iluminando fresta no fundo da gaveta do caixa, moedas no chao (gerada IA - carrossel 146, ver onde o dinheiro escapa, raio-x) | pessoa, lanterna, gaveta, investigacao, raio-x |
| 651.png | Registradora fechada com envelope pardo gordo em cima e chapeu de feltro ao lado (gerada IA - carrossel 146, CTA: paga o dono) | objeto, registradora, envelope, chapeu, cta |
| 652.png | Dono de serralheria sentado no degrau da porta no fim do dia, luvas na mao, cabeca baixa (gerada IA - carrossel 142, ta f@da empreender no Brasil) | pessoa, serralheria, exaustao, fim de dia, aguento |
| 653.png | Jornal velho dobrado em cima do balcao de madeira com xicara de cafe vazia (manchete ilegivel) (gerada IA - carrossel 142, ta f@da empreender no Brasil) | objeto, jornal, balcao, cafe, noticia |
| 654.png | Espeto de metal no balcao entupido de boletos amassados, data circulada a caneta (gerada IA - carrossel 142, ta f@da empreender no Brasil) | objeto, boletos, espeto, contas, vencimento |
| 655.png | Maos tirando notas dobradas da carteira surrada sobre o balcao, gaveta do caixa aberta so com moedas (gerada IA - carrossel 142, ta f@da empreender no Brasil) | maos, carteira, dinheiro, caixa, bolso do dono |
| 656.png | Caderno de capa dura fechado com elastico, empoeirado, em pe e centralizado na prateleira (gerada IA - carrossel 142, ta f@da empreender no Brasil) | objeto, caderno, fechado, poeira, numero nao lido |
| 657.png | Assoalho de madeira atras do balcao com duas marcas de sapato gastas no mesmo ponto (gerada IA - carrossel 142, ta f@da empreender no Brasil) | objeto, assoalho, marcas, repeticao, mesmo lugar |
| 658.png | Dono sentado em cadeira de plastico na calcada da propria loja olhando a rua vazia (gerada IA - carrossel 142, ta f@da empreender no Brasil) | pessoa, calcada, espera, rua vazia, loja |
| 659.png | Dono escorando com o ombro estante torta carregada de rolos de tecido (gerada IA - carrossel 142, ta f@da empreender no Brasil) | pessoa, esforco, estante, tecido, segurar |
| 660.png | Mao e antebraco girando a chave na fechadura da porta de ferro da loja (gerada IA - carrossel 142, ta f@da empreender no Brasil) | maos, chave, porta, fechar, controle |
| 661.png | Caderno aberto na bancada com duas colunas de numeros a lapis, regua e lapis ao lado (gerada IA - carrossel 142, ta f@da empreender no Brasil) | objeto, caderno, colunas, numeros, controle |
| 662.png | Dono agachado com lanterna iluminando cano velho gotejando, poca no assoalho da malharia (gerada IA - carrossel 142, ta f@da empreender no Brasil) | pessoa, lanterna, vazamento, cano, raio-x |
| 663.png | Dono de serralheria em pe na bancada, mangas dobradas, olhando firme pra camera (gerada IA - carrossel 142, ta f@da empreender no Brasil) | pessoa, serralheria, bancada, firme, cta |
| 664.png | Homem de uns sessenta anos sentado no degrau da porta de casa simples, olhando pro chao (gerada IA - carrossel 146 v3, capa topo: trinta anos de empresa e so sobrou a casa onde mora) | pessoa, velhice, casa, porta, desalento |
| 665.png | Feirante jovem montando a banca de madrugada sob lampada pendurada, caixote de verdura (gerada IA - carrossel 146 v3, eu comecei na feira, uma da manha) | pessoa, feira, madrugada, trabalho, caixote |
| 666.png | Duas maos calejadas de homem velho abertas e vazias sobre mesa de madeira (gerada IA - carrossel 146 v3, e pergunta: cade?) | maos, vazio, velhice, trabalho |
| 667.png | Carteira de couro aberta e vazia na mesa da cozinha, prego com contas pagas atras (gerada IA - carrossel 146 v3, entrou num dia, saiu no outro) | objeto, carteira, vazio, contas, cozinha |
| 668.png | Lata de biscoito florida aberta e vazia com uma moeda no fundo (gerada IA - carrossel 146 v3, o mes fechando no zero) | objeto, lata, poupanca, vazio, moeda |
| 669.png | Homem de regata sentado na beira da cama de madrugada, maos juntas, preocupado (gerada IA - carrossel 146 v3, se a empresa fechar amanha, quantos meses voce aguenta?) | pessoa, noite, insonia, medo, cama |
| 670.png | Homem mais velho de camisa social branca apoiado no balcao olhando pra camera, serio (gerada IA - carrossel 146 v3, depois de 38 anos, eu te falo) | pessoa, balcao, olhar-pra-camera, autoridade, velhice |
| 671.png | Cofrinho de porco de barro inteiro e cheio com pilha de moedas ao lado (gerada IA - carrossel 146 v3, todo mes alguma coisa ficou) | objeto, cofrinho, moedas, poupanca, patrimonio |
| 672.png | Still: pilha de autos de processo amarrados com barbante e folha de calendario de parede com metade dos dias riscados, sem numeros legiveis (capa: setembro de 2020, recuperacao judicial) (gerada IA - carrossel 148) | objeto-metafora, still, processo |
| 673.png | Dono sozinho na cabeceira da mesa de reuniao vazia, cabeca na mao, pasta grossa fechada na frente (isso, nunca) (gerada IA - carrossel 148) | pessoa, solidao, reuniao |
| 674.png | Still: porta de vidro de loja com a porta de enrolar abaixada por dentro, folha em branco colada no vidro, corrente e cadeado (a pandemia fechou a rede em marco) (gerada IA - carrossel 148) | objeto-metafora, still, loja-fechada |
| 675.png | Still: duas poltronas de couro altas vazias na sala de conselho, dois copos d'agua intactos, pasta fechada (dois conselheiros de peso) (gerada IA - carrossel 148) | objeto-metafora, still, conselho |
| 676.png | Still: tres cadeiras vazias em volta de uma mesa redonda coberta de papeis, telefone de disco no centro, xicara de cafe (nenhum dos tres sabia) (gerada IA - carrossel 148) | objeto-metafora, still, reuniao |
| 677.png | Dono em pe na cozinha de casa a noite com o telefone de parede no ouvido e a mao na testa (dono sozinho no telefone com o gerente) (gerada IA - carrossel 148) | pessoa, cozinha, telefone |
| 678.png | Still: encruzilhada de estrada de terra com placa de madeira de tres setas em branco (era a decisao errada, tinha outros caminhos) (gerada IA - carrossel 148) | objeto-metafora, still, estrada |
| 679.png | Dono de costas num corredor de reparticao com portas iguais fechadas dos dois lados, a mao numa macaneta (procurando a porta de saida) (gerada IA - carrossel 148) | pessoa, de-costas, corredor |
| 680.png | Still: lupa pousada sobre livro-caixa de couro fechado e empoeirado, lampiao apagado ao lado (foi o que eu nao sabia) (gerada IA - carrossel 148) | objeto-metafora, still, livro-caixa |
| 681.png | Dono no banco de tras de um carro olhando pela janela, pasta ao lado, fabrica passando pequena ao fundo (cinco anos fora do operacional) (gerada IA - carrossel 148) | pessoa, carro, fabrica |
| 682.png | Still: poltrona de couro vazia na cabeceira da mesa de reuniao, contrato em branco e caneta destampada na frente (a ignorancia e uma socia oculta) (gerada IA - carrossel 148) | objeto-metafora, still, conselho |
| 683.png | Dono de avental olhando pra camera com um livro-caixa aberto em branco virado pro leitor (agora olha pra sua empresa) (gerada IA - carrossel 148) | pessoa, olhar-para-camera, livro-caixa |
| 684.png | Still: balanca antiga de dois pratos com livros de um lado e uma chave grande de loja do outro, o prato da chave caido (os dois precos) (gerada IA - carrossel 148) | objeto-metafora, still, balanca |
| 685.png | Dono debrucado na mesa com uma lanterna acesa sobre o livro-caixa aberto, dedo numa linha (um raio-x antes de decidir) (gerada IA - carrossel 148) | pessoa, lanterna, livro-caixa |
| 686.png | Dono de costas atravessando uma porta de madeira aberta pra luz do dia, a mao na folha da porta (CTA: comenta PORTA) (gerada IA - carrossel 148) | pessoa, de-costas, porta |
| 687.png | Dono de camisa simples sentado a mesa do escritorio da fabrica de colchoes, olhando pra camera (capa: tem um desejo que todo dono tem em comum) (gerada IA - carrossel 146) | pessoa, olhar-para-camera, escritorio |
| 688.png | Still: mesa soterrada de papeis e pastas, telefone de disco fora do gancho, cafe frio (ter menos problema) (gerada IA - carrossel 146) | still, papelada, telefone |
| 689.png | Dono a noite no escritorio sob a luminaria, costas retas, caneta na mao (problema de dono nao acaba; peso, nao derrota) (gerada IA - carrossel 146) | pessoa, noite, luminaria |
| 690.png | Still: molho grande de chaves antigas pendurado num prego ao lado do portao de ferro (ser dono e isso) (gerada IA - carrossel 146) | still, chaves, portao |
| 691.png | Still: planta de ampliacao de galpao aberta na bancada, regua e lapis (vamos criar um problema bom) (gerada IA - carrossel 146) | still, planta, ampliacao |
| 692.png | Dois funcionarios de bracos cruzados na bancada, maquinas de costura cobertas por lona (problema ruim: maquina parada) (gerada IA - carrossel 146) | pessoas, ocioso, estofados |
| 693.png | Barracao de telha metalica com pilhas alinhadas ocupando o patio (problema bom: barracao ficando pequeno) (gerada IA - carrossel 146) | galpao, cheio-organizado, telha-metalica |
| 694.png | Dois barracoes vizinhos de portao aberto: esquerdo vazio e varrido, direito cheio de caixas (so um paga a conta) (gerada IA - carrossel 146) | dicotomia, galpao, vazio-x-cheio |
| 695.png | Still: campainha de balcao cromada intocada num balcao de madeira vazio, poeira em volta (cliente nao se contrata) (gerada IA - carrossel 146) | still, campainha, balcao-vazio |
| 696.png | Perfiladeira antiga rodando, telha metalica nova saindo dos rolos (problema bom e fabricado) (gerada IA - carrossel 146) | maquina, fabrica, telha-metalica |
| 697.png | Fila de caminhoes antigos esperando pra carregar na porta do galpao (uma maquina de vendas / demanda) (gerada IA - carrossel 146) | caminhoes, fila, demanda |
| 698.png | Esteira de expedicao com caixas iguais alinhadas indo pro portao (demanda infinita) (gerada IA - carrossel 146) | still, esteira, expedicao |
| 699.png | Dono recostado sem pressa, cliente de terno inclinado pra frente falando (escolhe o cliente, margem alta) (gerada IA - carrossel 146) | pessoas, negociacao, escritorio |
| 700.png | Doca de carga: dono de prancheta dirigindo o carregamento do caminhao cheio (perder o sono pelo motivo certo) (gerada IA - carrossel 146) | pessoas, carga, caminhao |
| 701.png | Still: livro de pedidos aberto com as duas paginas cheias de lancamentos, lapis na dobra (oferta: a maquina) (gerada IA - carrossel 146) | still, livro-de-pedidos, lapis |
| 702.png | Dono batendo a mao no caminhao carregado que sai do galpao, olhando firme pra camera (CTA: comenta PROBLEMA) (gerada IA - carrossel 146) | pessoa, olhar-para-camera, caminhao |
| 703.png | Still: caixote de frutas, as de cima bonitas e as de baixo podres (apodrece onde o dono nao confere) (gerada IA - carrossel 147) | still, frutas, podre, caixote |
| 704.png | Still: freezer de sorveteria aberto com baldes faltando, gelo nas bordas, prancheta com folha em branco (gerada IA - carrossel 147) | still, freezer, estoque, sorveteria |
| 705.png | Gerente de sorveteria sorrindo com polegar pra cima, sorvete derretendo no balcao (ta tudo certo, chefe) (gerada IA - carrossel 147) | pessoa, sorveteria, ironia, positivo |
| 706.png | Still: gaveta de registradora antiga aberta e vazia, so moedas soltas (buraco no caixa) (gerada IA - carrossel 147) | still, registradora, caixa-vazio |
| 707.png | Maos: dono entregando molho de chaves na mao de outra pessoa sobre o balcao (delegar) (gerada IA - carrossel 147) | maos, chaves, entrega, sorveteria |
| 708.png | Still: panela de pressao no fogo soltando fumaca escura, cozinha vazia, toalha na cadeira (ja queimou) (gerada IA - carrossel 147) | still, panela-de-pressao, cozinha, queimado |
| 709.png | Dono de prancheta e gerente de sorveteria no balcao, gerente respondendo e apontando a vitrine (conferir) (gerada IA - carrossel 147) | pessoas, sorveteria, prancheta, conferir |
| 710.png | Still: carro antigo parado na estrada de terra com capo aberto soltando vapor (quem nao revisa, quebra) (gerada IA - carrossel 147) | still, carro, estrada, quebrado |
| 711.png | Dono agachado no freezer contando baldes com prancheta (deve conferir tudo) (gerada IA - carrossel 147) | pessoa, freezer, contagem, prancheta |
| 712.png | Still: caderno de contas aberto no balcao, colunas a lapis, regua e lapis (dia e hora marcados) (gerada IA - carrossel 147) | still, caderno, contas, rotina |
| 713.png | Dono com caderno falando com tres funcionarios de avental em roda antes de abrir (rito) (gerada IA - carrossel 147) | pessoas, time, reuniao, rito |
| 714.png | Still: mesinha com quatro xicaras de cafe vazias e cadeiras afastadas, nenhum papel (reuniao sem numero) (gerada IA - carrossel 147) | still, mesa, cafe, reuniao |
| 715.png | Still: freezer aberto visto de cima, lanterna acesa iluminando poca de sorvete derretido (onde apodrece) (gerada IA - carrossel 147) | still, freezer, lanterna, vazamento |
| 716.png | Dono de sorveteria atras da vitrine, prancheta no braco, olhando firme pra camera, parede lisa (CTA RAIO-X) (gerada IA - carrossel 147) | pessoa, olhar-para-camera, sorveteria |
| 717.png | Cofre de ferro antigo com a porta aberta e vazio por dentro (gerada IA - carrossel 164, quanto disso virou patrimonio seu?) | objeto, cofre, vazio, patrimonio |
| 718.png | Maos do dono empurrando as chaves de casa sobre a mesa pro gerente do banco, so maos (gerada IA - carrossel 164, e hoje trabalha pra pagar o banco) | maos, banco, chaves, garantia, divida |
| 719.png | Carroca de entrega com cavalo parada no meio-fio enquanto caminhao passa borrado (gerada IA - carrossel 164, o outro viu o mercado mudar e nem percebeu) | objeto, carroca, cavalo, caminhao, mudanca, modelo-defasado |
| 720.png | Dono pequeno de costas ao pe de uma pilha enorme de caixas e engradados no galpao (gerada IA - carrossel 164, o CNPJ ficou grande e o CPF continuou do mesmo tamanho) | pessoa, escala, galpao, caixas, pequeno-grande |
| 721.png | Menino emburrado de bracos cruzados na cadeira de couro grande demais atras da mesa de dono (gerada IA - carrossel 167, capa: quem so faz o que gosta e crianca) | pessoa, crianca, birra, cadeira-de-dono |
| 722.png | Banca de feira de madrugada com caixotes de verdura e fruta sob lampada pendurada (gerada IA - carrossel 167, eu nasci vendendo) | objeto, feira, madrugada, caixote |
| 723.png | Homem mais velho de oculos conferindo livro-caixa com a caneta a mesa (gerada IA - carrossel 167, olho o numero, confiro a margem) | pessoa, livro-caixa, conferencia, rotina |
| 724.png | Pasta de relatorios amarrada com barbante e empoeirada no canto da mesa, xicara ao lado (gerada IA - carrossel 167, o que voce nao faz porque e chato) | objeto, relatorio, poeira, abandono |
| 725.png | Time sentado em volta da mesa de reuniao olhando a cadeira do dono vazia (gerada IA - carrossel 167, a parte chata continua sem dono) | pessoa, grupo, reuniao, cadeira-vazia |
| 726.png | Dono sorrindo apertando a mao do cliente no balcao enquanto a pilha de papeis despenca atras (gerada IA - carrossel 167, gestao nao e a minha praia) | pessoa, aperto-de-mao, papelada, caos |
| 727.png | Sapatinho de crianca tombado ao lado de sapato social de homem no assoalho (gerada IA - carrossel 167, eu chamo de birra) | objeto, sapato, crianca-adulto, contraste |
| 728.png | Relogio de mesa antigo perto das seis ao lado de espeto de contas pagas (gerada IA - carrossel 167, o boleto vence com ou sem a sua vontade) | objeto, relogio, contas, prazo |
| 729.png | Vassoura de palha e pa de lixo encostadas na parede, assoalho varrido (gerada IA - carrossel 167, fazer o basico bem feito todo dia e chato mesmo) | objeto, vassoura, rotina, basico |
| 730.png | Sala de treinamento vista de tras, empresarios sentados e instrutor apontando quadro de giz (gerada IA - carrossel 167, na imersao eu ensino a parte chata) | pessoa, grupo, treinamento, quadro |
| 731.png | Paleto pendurado na cadeira de escritorio, chaves e livro fechado na mesa (gerada IA - carrossel 167, CTA ADULTO) | objeto, paleto, cadeira, chaves, cta |
| 732.png | Dono de fabrica de calcados erguendo contra a luz um sapato montado errado, incredulo (fizeram tudo diferente) (gerada IA - carrossel 165) | pessoa, fabrica, calcados, erro |
| 733.png | Still: caixa de sapato com um pe quase o dobro do outro, ficha do pedido ao lado (a medida que saiu errada) (gerada IA - carrossel 165) | still, sapato, erro, expedicao |
| 734.png | Dono no escritorio envidracado do mezanino, mao na testa, fabrica ao fundo (essa geracao nao quer nada) (gerada IA - carrossel 165) | pessoa, escritorio, frustracao, fabrica |
| 735.png | Still: tres sapatos do mesmo modelo acabados de jeitos diferentes: cadarco, fivela, costura (cada um faz do jeito que entendeu) (gerada IA - carrossel 165) | still, sapatos, padrao, variacao |
| 736.png | Criancas em fila no patio da escola brincando de telefone sem fio, a ultima confusa (anos 60) (gerada IA - carrossel 165) | pessoas, criancas, infancia, telefone-sem-fio |
| 737.png | Still: dois telefones de lata com o barbante todo embolado (a historia chega outra) (gerada IA - carrossel 165) | still, telefone-de-lata, comunicacao, embolado |
| 738.png | Dono de costas saindo pelo portao da fabrica, funcionario jovem com a caixa na mao sem saber o que fazer (delargar) (gerada IA - carrossel 165) | pessoas, fabrica, abandono, delegar |
| 739.png | Still: ficha de producao em branco presa na bancada com retalhos de couro (sem o que, como, quando) (gerada IA - carrossel 165) | still, ficha, bancada, couro |
| 740.png | Funcionario jovem cocando a cabeca diante das pecas de couro cortadas (cumpre o que lembra) (gerada IA - carrossel 165) | pessoa, duvida, bancada, couro |
| 741.png | Still: cartilha escolar antiga aberta com abelha e cachorro numa carteira de madeira (Caminho Suave) (gerada IA - carrossel 165) | still, cartilha, escola, alfabetizacao |
| 742.png | Still: manual de procedimentos grosso aberto ao lado de uma cartilha escolar antiga na bancada (empresa tem cartilha) (gerada IA - carrossel 165) | still, manual, cartilha, processo |
| 743.png | Vendedor mostrando sapato a cliente no showroom com o manual aberto, novato observando (a mesma historia) (gerada IA - carrossel 165) | pessoas, atendimento, cliente, manual |
| 744.png | Dono ensinando dois funcionarios com o manual aberto no chao da fabrica (gerada IA - carrossel 165) | pessoas, treinamento, manual, fabrica |
| 745.png | Dono de fabrica de calcados com o manual debaixo do braco olhando firme pra camera, parede lisa (CTA PADRAO) (gerada IA - carrossel 165) | pessoa, olhar-para-camera, fabrica |
| 746.png | Vendedor jovem sorridente no balcao oferecendo produto ao cliente, gesticulando (gerada IA - carrossel 167, eu sempre gostei de vender) | pessoa, vendedor, balcao, entusiasmo |
| 747.png | Pilha de livros-caixa e pastas de planilha com oculos em cima e caneta parada ao lado (gerada IA - carrossel 167, numero, planilha, reuniao: nunca gostei) | objeto, livro-caixa, pilha, tedio |
| 748.png | Registradora antiga com a gaveta aberta transbordando de notas e moedas (gerada IA - carrossel 167, eu sempre gostei de vender) | objeto, registradora, dinheiro, venda, fartura |
| 749.png | Still: manual de procedimentos esquecido na gaveta da bancada, com po e retalhos de couro por cima (na segunda semana, do jeito dele) (gerada IA - carrossel 165) | still, manual, gaveta, esquecido |
| 750.png | Still: caixote de refugo cheio de sapatos com defeito ao lado do manual fechado e intacto num banco (sem acompanhamento nada funciona) (gerada IA - carrossel 165) | still, refugo, defeito, manual |
| 751.png | Dono comparando um sapato com o desenho do manual aberto, funcionario ao lado mostrando o que fez (rito de acompanhar) (gerada IA - carrossel 165) | pessoas, acompanhamento, conferencia, manual |
| 752.png | Porta-retrato de casamento antigo ao lado de marmita aberta com arroz e feijao (gerada IA - carrossel 171, lembra do casamento, nao do almoco de terca) | objeto, casamento, marmita, memoria |
| 753.png | Prato vazio com garfo e faca cruzados e copo americano em toalha xadrez (gerada IA - carrossel 171, nao lembro o que comi ontem) | objeto, prato, refeicao, esquecimento |
| 754.png | Lata de biscoito cheia de lembrancas: fotos antigas, sapatinho de bebe, fita de cetim (gerada IA - carrossel 171, a cabeca so guarda o que emociona) | objeto, lembrancas, fotos, emocao |
| 755.png | Quadro de metas a giz com a meta batida e o escritorio vazio (gerada IA - carrossel 171, a meta que ninguem comemorou) | objeto, quadro, meta, escritorio-vazio |
| 756.png | Funcionario de costas saindo pelo portao da fabrica com caixa de pertences (gerada IA - carrossel 171, o seu melhor vai embora) | pessoa, saida, demissao, portao |
| 757.png | Marmita aberta sozinha numa mesa comprida de refeitorio vazio (gerada IA - carrossel 171, a sua empresa e um almoco de terca) | objeto, marmita, refeitorio, solidao |
| 758.png | Churrasqueira de tijolo apagada e fria com carvao cinza (gerada IA - carrossel 171, besteira e ser esquecido) | objeto, churrasqueira, frio, abandono |
| 759.png | Time brindando com copos americanos em volta da mesa, dono rindo no meio (gerada IA - carrossel 171, forrada de emocao) | pessoa, grupo, brinde, celebracao |
| 760.png | Dono apertando a mao e dando tapinha no ombro de funcionario antigo na oficina (gerada IA - carrossel 171, a pequena tem uma forca) | pessoa, aperto-de-mao, vinculo, oficina |
| 761.png | Dono sentado num caixote ao lado de funcionario jovem na hora do cafe, conversando de perto (gerada IA - carrossel 171, descobre o sonho deles) | pessoa, conversa, proximidade, cafe |
| 762.png | Bolo de aniversario com velas na mesa do escritorio e maos batendo palmas (gerada IA - carrossel 171, todo mes virando rito) | objeto, bolo, aniversario, rito |
| 763.png | Foto do time emoldurada na parede ao lado do relogio de ponto (gerada IA - carrossel 171, gente escolhe ficar onde a vida foi marcada) | objeto, foto-de-grupo, relogio-de-ponto, pertencimento |
| 764.png | Prato feito comum no balcao: arroz, feijao, bife fino e salada (gerada IA - carrossel 171, e o almoco de terca nao emociona ninguem) | objeto, prato-feito, almoco, rotina |
| 765.png | Estrada de terra reta e longa com a fita de chegada pequena la longe (gerada IA - carrossel 179, quando a empresa crescer eu me pago) | objeto, estrada, linha-de-chegada, distancia |
| 766.png | Planta de galpao novo aberta na mesa com regua, lapis e capacete de obra (gerada IA - carrossel 179, aparece um motivo pra crescer mais um pouco) | objeto, projeto, galpao, expansao |
| 767.png | Calendario de mesa com folhas viradas ao lado de envelope de pagamento fechado e empoeirado (gerada IA - carrossel 179, a sua vez fica pro ano que vem) | objeto, calendario, envelope, adiamento |
| 768.png | Botas de trabalho gastas com sola furada no chao de terra (gerada IA - carrossel 179, dez anos depois, ainda esperando) | objeto, botas, desgaste, espera |
| 769.png | Carrinho de mao de madeira vazio na estrada de terra, cabos pra camera (gerada IA - carrossel 179, quem empurra e voce) | objeto, carrinho-de-mao, empurrar, estrada |
| 770.png | Vidraca de escritorio furada por pedra, pedra no chao (gerada IA - carrossel 179, o tiro pode vir de qualquer lado) | objeto, vidraca, pedra, risco |
| 771.png | Cavalo de carrossel parado num parque vazio (gerada IA - carrossel 179, correu dez anos de graca) | objeto, carrossel, cavalo, circulo |
| 772.png | Dois cofrinhos de barro, um grande e um pequeno, com moedas em cima (gerada IA - carrossel 179, investe em voce tambem, os dois juntos) | objeto, cofrinho, poupanca, dois-juntos |
| 773.png | Pilha de tijolos e saco de cimento com carteira aberta em cima (gerada IA - carrossel 179, voce cresce com o seu dinheiro) | objeto, tijolos, cimento, carteira, investimento |
| 774.png | Envelope de pagamento pardo aberto com notas na mesa do dono (gerada IA - carrossel 179, a sua vez e agora) | objeto, envelope, pagamento, dinheiro, cta |
| 775.png | Maos do dono contando um maco de notas na mesa do escritorio, so maos (gerada IA - carrossel 179, dono tem que ser pago agora) | maos, dinheiro, pagamento, agora |
| 776.png | Alvo de tiro de papel cheio de furos apoiado num cavalete sobre a mesa (gerada IA - carrossel 179, o tiro pode vir de qualquer lado) | objeto, alvo, tiro, risco |
| 777.png | Tenis de corrida gastos ao lado de envelope de pagamento vazio e aberto no banco de madeira (gerada IA - carrossel 179, correu dez anos de graca) | objeto, tenis, envelope-vazio, esforco-sem-retorno |
| 778.png | Maos do dono tirando notas da propria carteira e pondo na gaveta da registradora da empresa (gerada IA - carrossel 179, voce cresce com o seu dinheiro) | maos, carteira, registradora, capital-proprio |
| 779.png | Mesa do dono soterrada de pastas e papeis, abajur aceso, cadeira de couro vazia (gerada IA - carrossel 180, o servico volta todo pra mesa do dono) | objeto, mesa, papelada, sobrecarga, capa |
| 780.png | Dono a noite, sozinho, conferindo o livro-caixa sob o abajur (gerada IA - carrossel 180, quem confere o caixa as dez da noite e voce) | dono, noite, livro-caixa, sobrecarga |
| 781.png | Dois envelopes de pagamento lado a lado, relogio de pulso em cima do segundo (gerada IA - carrossel 180, paga a folha duas vezes: dinheiro e tempo) | objeto, envelope, relogio, tempo, folha |
| 782.png | Dono de gravata consertando o tear com as proprias maos, encarregado de bracos cruzados ao fundo (gerada IA - carrossel 180, e mais rapido eu fazer) | dono, tear, fabrica-textil, fazer-pelo-time |
| 783.png | Mesa de funcionario vazia com uma pasta fechada e uma cadeira (gerada IA - carrossel 180, alguem escreveu o que ele foi contratado pra entregar?) | objeto, mesa, funcao, vazio |
| 784.png | Funcionario novo com prancheta em branco entre os teares, perdido (gerada IA - carrossel 180, ninguem disse o que era) | funcionario, novato, perdido, fabrica-textil |
| 785.png | Quadro de producao com a grade toda vazia, giz parado (gerada IA - carrossel 180, empresa sem gestao) | objeto, quadro, gestao, vazio |
| 786.png | Cadeira de diretor vazia virada pra janela que da pro galpao de teares (gerada IA - carrossel 180, ninguem faz o servico do dono) | objeto, cadeira-vazia, escritorio, fabrica-textil |
| 787.png | Pasta grossa de planejamento empoeirada com oculos em cima (gerada IA - carrossel 180, servico de dono sem ninguem) | objeto, planejamento, poeira, abandono |
| 788.png | Pilha de pastas largada numa mesa, cadeira afastada, ninguem (gerada IA - carrossel 180, delargar) | objeto, pastas, abandono, delargar |
| 789.png | Dono apontando o tear enquanto o encarregado faz o servico, os dois centralizados (gerada IA - carrossel 180, delegar e treinar e acompanhar) | dono, encarregado, treino, delegar, fabrica-textil |
| 790.png | Dono calmo lendo um relatorio na mesa limpa, cafe ao lado (gerada IA - carrossel 180, a hora volta pro lugar dela) | dono, relatorio, foco, calma |
| 791.png | Dono de gravata conversando com dois encarregados no galpao de teares (gerada IA - carrossel 180, oferta: ensino gestao) | dono, time, conversa, fabrica-textil, oferta |
| 792.png | Tecela trabalhando concentrada no tear, galpao em producao (gerada IA - carrossel 180, cta ENTREGA) | funcionaria, tear, producao, entrega, cta |
| 793.png | Dono idoso de cabelo branco atras do balcao de um armazem grande e cheio, olhando a propria carteira aberta e vazia (gerada IA - carrossel 179, capa: quando a empresa crescer eu me pago) | pessoa, velhice, carteira-vazia, empresa-cheia, capa |
| 794.png | Envelope de pagamento fino sobre a mesa grande e vazia do dono, cadeira de couro atras (gerada IA - carrossel 183, R$ 30 mil nao e salario de dono) | envelope, pagamento, mesa-de-dono, capa, salario |
| 795.png | Pilhas de livros-razao e pastas amarradas num arquivo publico (gerada IA - carrossel 183, R$ 30 mil nao e salario de dono) | divida, governo, papelada, arquivo |
| 796.png | Carimbo e pilha de guias no balcao de reparticao (gerada IA - carrossel 183, R$ 30 mil nao e salario de dono) | imposto, governo, carimbo, guias |
| 797.png | Livro de contrato aberto com caneta-tinteiro e molho de chaves de casa em cima (gerada IA - carrossel 183, R$ 30 mil nao e salario de dono) | emprestimo, garantia, chaves, casa, banco |
| 798.png | Cama de crianca arrumada com ursinho de pelucia e sapatinhos no chao (gerada IA - carrossel 183, R$ 30 mil nao e salario de dono) | familia, casa, crianca, risco |
| 799.png | Contracheque e notas ao lado de uma somadora antiga (gerada IA - carrossel 183, R$ 30 mil nao e salario de dono) | salario, pro-labore, somadora, dinheiro |
| 800.png | Prato vazio com talheres na cabeceira de uma mesa de diretoria (gerada IA - carrossel 183, R$ 30 mil nao e salario de dono) | passa-fome, prato-vazio, diretoria |
| 801.png | Criado-mudo com abajur aceso, despertador, chaves e contrato dobrado ao lado da cama (gerada IA - carrossel 183, R$ 30 mil nao e salario de dono) | insonia, garantia, chaves, noite, risco |
| 802.png | Mesa do dono vista do lado dele com a cadeira de visita vazia em frente (gerada IA - carrossel 183, R$ 30 mil nao e salario de dono) | mesa, conversa, cadeira-vazia, dono |
| 803.png | Cofre antigo aberto e vazio com um envelope fino em cima (gerada IA - carrossel 183, R$ 30 mil nao e salario de dono) | cofre-vazio, lucro, dividendo, envelope |
| 804.png | Guarda-chuva preto fechado encostado na mesa, poca de chuva no chao (gerada IA - carrossel 183, R$ 30 mil nao e salario de dono) | incerteza, cenario, chuva, escritorio |
| 805.png | Quatro envelopes pardos cheios de notas enfileirados (gerada IA - carrossel 183, R$ 30 mil nao e salario de dono) | envelopes, dinheiro, pagamento, oferta |
| 806.png | Chave de casa sobre envelope pardo aberto cheio de notas (gerada IA - carrossel 183, R$ 30 mil nao e salario de dono) | chave, casa, dinheiro, garantia, cta |
| 807.png | Operario sozinho no vestiario no fim do turno olhando uma foto pequena na mao (gerada IA - carrossel 184, qual e o sonho do seu funcionario?) | pessoa, vestiario, foto, sonho |
| 808.png | Dono de bracos cruzados e cara impaciente na mesa de reuniao, cadeiras vazias (gerada IA - carrossel 184, facil reclamar do time) | pessoa, dono, impaciencia, reuniao |
| 809.png | Armario de vestiario aberto com a porta forrada de fotos pequenas de familia e casa (gerada IA - carrossel 184, pelo que ele levanta de manha) | objeto, armario, fotos, motivo |
| 810.png | Chaves de casa, livro escolar e carrinho de lata na mesa da cozinha (gerada IA - carrossel 184, a casa, a faculdade do filho, o carro) | objeto, chaves, livro, carrinho, sonho |
| 811.png | Trabalhador de costas subindo a rua de casa a noite com a marmita, janela acesa (gerada IA - carrossel 184, o que enfrenta quando vai pra casa) | pessoa, noite, casa, volta-do-trabalho |
| 812.png | Dono de costas sozinho no galpao vazio no fim do dia (gerada IA - carrossel 184, sua empresa e o seu sonho, nao o dele) | pessoa, dono, galpao, solidao |
| 813.png | Ponte de madeira firme sobre um riacho, vista de lado (gerada IA - carrossel 184, a ponte levou ele mais longe) | objeto, ponte, riacho, caminho |
| 814.png | Time de seis pessoas num galpao novo e maior, orgulhosos, dono no meio (gerada IA - carrossel 184, precisa ver a empresa crescer) | pessoa, grupo, galpao-novo, crescimento |
| 815.png | Dono e funcionaria frente a frente com cafe numa mesa simples, conversa proxima (gerada IA - carrossel 184, senta com cada um e pergunta) | pessoa, conversa, escuta, proximidade |
| 816.png | Escada de madeira com um capacete de trabalho em cada degrau, do gasto ao novo (gerada IA - carrossel 184, plano de carreira) | objeto, escada, capacetes, carreira |
| 817.png | Mural de cortica do refeitorio com fotos do time e bilhetes, banco embaixo (gerada IA - carrossel 184, CTA sonho) | objeto, mural, fotos-do-time, pertencimento |
| 818.png | Mesmo funcionario jovem duas vezes lado a lado: aceso no primeiro dia e apagado meses depois na mesma mesa (ficou com a sua cara) (gerada IA - carrossel 182) | pessoas, contraste, antes-depois, escritorio |
| 819.png | Funcionario jovem de mochila saindo pela porta do escritorio com a mao no interruptor, colegas ainda trabalhando (gerada IA - carrossel 182) | pessoa, saida, horario, escritorio |
| 820.png | Still: pasta de curriculo aberta na mesa do dono com foto 3x4 sorrindo, cafe e caneta (contratei errado) (gerada IA - carrossel 182) | still, curriculo, contratacao, mesa |
| 821.png | Still: duas velas na mesa, uma acesa e a outra acabando de pegar fogo dela (brilho se pega) (gerada IA - carrossel 182) | still, velas, contagio, luz |
| 822.png | Still: duas mesas lado a lado, a do veterano baguncada e a nova ficando igual, cadeiras no mesmo angulo (o ambiente ensina) (gerada IA - carrossel 182) | still, mesas, imitacao, escritorio |
| 823.png | Dono na copa ao telefone com a mao na testa, dois funcionarios de caneca ouvindo de lado (o humor do dono) (gerada IA - carrossel 182) | pessoas, copa, frustracao, ambiente |
| 824.png | Still: nivel de pedreiro sobre a mesa do escritorio (o nivel da casa) (gerada IA - carrossel 182) | still, nivel, regua, escritorio |
| 825.png | Dono debrucado sobre a mesa de vidro da sala de reuniao olhando o proprio reflexo (o time e reflexo) (gerada IA - carrossel 182) | pessoa, reflexo, lideranca, reuniao |
| 826.png | Still: folha com grafico de barras subindo na mesa de reuniao, tres cafes e caneta (meta e numero) (gerada IA - carrossel 182) | still, grafico, meta, reuniao |
| 827.png | Funcionario jovem aceso explicando algo pra dois colegas na mesa (acende os outros) (gerada IA - carrossel 182) | pessoas, ensino, colegas, escritorio |
| 828.png | Dono de bracos cruzados de frente pra camera no escritorio, time trabalhando atras (CTA BRILHO) (gerada IA - carrossel 182) | pessoa, olhar-para-camera, escritorio |
| 829.png | Porta da oficina aberta pra rua, mochila e botas no chao ao lado da bancada (o melhor indo embora; capa ESCOLA) (gerada IA - carrossel 188) | still, oficina, saida, porta |
| 830.png | Dono apertando a mao do funcionario que sai com a caixa de pertences (gerada IA - carrossel 188) | pessoas, despedida, oficina |
| 831.png | Still: caixa de papelao com caneca, luvas e bone sobre bancada vazia (gerada IA - carrossel 188) | still, saida, oficina |
| 832.png | Still: tabuleiro de ferramentas deitado sobre a bancada (gerada IA - carrossel 188) | still, ferramentas, oficina |
| 833.png | Mestre e aprendiz debrucados sobre a mesma peca na bancada (gerada IA - carrossel 188) | pessoas, ensino, mestre-aprendiz, oficina |
| 834.png | Maos calejadas segurando caderno de anotacoes gasto (gerada IA - carrossel 188) | maos, caderno, aprendizado |
| 835.png | Mestre guiando a mao do aprendiz no torno (gerada IA - carrossel 188) | pessoas, ensino, mestre-aprendiz, torno |
| 836.png | Still: uniforme dobrado com luvas sobre banco vazio do vestiario (ultimo dia) (gerada IA - carrossel 188) | still, saida, vestiario |
| 837.png | Aprendiz subindo escada de madeira, colega segurando embaixo (gerada IA - carrossel 188) | pessoas, apoio, crescimento, oficina |
| 838.png | Dono e dois funcionarios olhando a mesma planta aberta na mesa (gerada IA - carrossel 188) | pessoas, gestao, planta, oficina |
| 839.png | Still: tres plainas do menor ao maior alinhadas na bancada (CTA ESCOLA) (gerada IA - carrossel 188) | still, crescimento, ferramentas |
| 840.png | Dono de costas na oficina vendo o melhor funcionario ir embora pela rua com a caixa de ferramentas (capa ESCOLA v2; 829 foi a v1) (gerada IA - carrossel 188) | pessoas, saida, oficina, despedida |
| 841.png | Dono de costas no escritorio vendo o melhor funcionario sair pela porta com a caixa (capa ESCOLA escritorio) (gerada IA - carrossel 188) | pessoas, saida, escritorio, despedida |
| 842.png | Dono apertando a mao do funcionario que sai com a caixa de pertences no escritorio (gerada IA - carrossel 188) | pessoas, despedida, escritorio |
| 843.png | Still: caixa com caneca e porta-retrato sobre mesa de escritorio vazia (gerada IA - carrossel 188) | still, saida, escritorio |
| 844.png | Funcionario jovem entediado diante de pilha de pastas iguais (gerada IA - carrossel 188) | pessoa, tedio, escritorio |
| 845.png | Gerente experiente e jovem debrucados sobre o mesmo documento (gerada IA - carrossel 188) | pessoas, ensino, escritorio |
| 846.png | Maos segurando caderno de anotacoes gasto sobre a mesa (gerada IA - carrossel 188) | maos, caderno, aprendizado |
| 847.png | Gerente em pe ensinando o jovem sentado diante do livro-caixa (gerada IA - carrossel 188) | pessoas, ensino, escritorio |
| 848.png | Still: mesa vazia com paleto dobrado e cracha na cadeira (ultimo dia) (gerada IA - carrossel 188) | still, saida, escritorio |
| 849.png | Gerente entregando pasta grossa ao jovem que se levanta (promocao) (gerada IA - carrossel 188) | pessoas, promocao, confianca, escritorio |
| 850.png | Dono e dois funcionarios olhando o mesmo plano aberto na mesa (gerada IA - carrossel 188) | pessoas, gestao, plano, escritorio |
| 851.png | Still: tres vasos da mesma planta do menor ao maior sobre a mesa (CTA ESCOLA) (gerada IA - carrossel 188) | still, crescimento, planta |
| 852.png | Dono empurrando pilha de revistas e livros e segurando o livro-caixa (capa FOCO) (gerada IA - carrossel 189) | pessoa, foco, caixa, escritorio |
| 853.png | Still: mesa soterrada de revistas, folhetos e livros (estrategias demais) (gerada IA - carrossel 189) | still, excesso, escritorio |
| 854.png | Still: mesa com trofeus e certificados diante de cadeira vazia (ego) (gerada IA - carrossel 189) | still, vaidade, escritorio |
| 855.png | Dono lendo o livro-caixa com maquina de somar (gerada IA - carrossel 189) | pessoa, caixa, numeros, escritorio |
| 856.png | Vendedor anotando pedido com cliente no balcao (gerada IA - carrossel 189) | pessoas, venda, escritorio |
| 857.png | Vendedor e cliente apertando a mao sobre pedido assinado (gerada IA - carrossel 189) | pessoas, venda, negocio |
| 858.png | Dono apontando checklist pro funcionario sentado (exigir e acompanhar) (gerada IA - carrossel 189) | pessoas, cobranca, escritorio |
| 859.png | Still: maquina de somar com fita de papel e livro-caixa (gerada IA - carrossel 189) | still, margem, numeros |
| 860.png | Funcionaria organizando pastas na gaveta do arquivo (arruma a casa) (gerada IA - carrossel 189) | pessoa, organizacao, arquivo |
| 861.png | Still: mesa arrumada com livro-caixa, caneta e cafe (gerada IA - carrossel 189) | still, ordem, escritorio |
| 862.png | Dono revisando numeros com dois funcionarios (gerada IA - carrossel 189) | pessoas, gestao, numeros |
| 863.png | Still: lapis apontado sobre livro-caixa fechado (CTA FOCO) (gerada IA - carrossel 189) | still, foco, minimal |
| 864.png | Still: quatro blocos de madeira empilhados do maior ao menor (pouca coisa, na ordem certa) (gerada IA - carrossel 189 v2) | still, base, ordem |
| 865.png | Still: cofre de metal aberto com macos de dinheiro e livro-caixa (o caixa) (gerada IA - carrossel 189 v2) | still, caixa, dinheiro |
| 866.png | Still: pilha de contas espetadas no espeto de papel e telefone (conta a pagar) (gerada IA - carrossel 189 v2) | still, contas, pressao |
| 867.png | Still: relogio de ponto com cartoes, um fora do lugar (o que voce tolera) (gerada IA - carrossel 189 v2) | still, ponto, cultura |
| 868.png | Boi dormindo na palha e homem de gravata olhando (historia pra boi dormir) (gerada IA - carrossel 189 v2) | animal, boi, ditado |
| 869.png | Varanda de casa simples ao anoitecer, janela da sala acesa, cadeira de balanco vazia (gerada IA - carrossel 193, capa: o preco que ninguem te avisa) | objeto, casa, varanda, cadeira-vazia, familia |
| 870.png | Batente da porta com marcas de altura dos filhos e um sapato de trabalho do pai no chao (gerada IA - carrossel 193, meus filhos cresceram sem eu ver) | objeto, batente, marcas-de-altura, filhos, tempo |
| 871.png | Balanca de pratos com a chave de casa num prato e contas no outro (gerada IA - carrossel 193, mais rico ou mais pobre?) | objeto, balanca, chave, contas, patrimonio |
| 872.png | Livro-caixa fechado e empoeirado com caneta em cima, intocado (gerada IA - carrossel 193, nunca tinha parado pra fazer essa conta) | objeto, livro-caixa, poeira, descaso |
| 873.png | Caixa de correio de parede aberta e vazia (gerada IA - carrossel 193, a ignorancia cobra mensalidade e nao manda boleto) | objeto, caixa-de-correio, vazio, conta-invisivel |
| 874.png | Mesa de jantar de familia com o prato do pai frio e a cadeira da cabeceira vazia (gerada IA - carrossel 193, quem paga e a familia) | objeto, jantar, cadeira-vazia, ausencia |
| 875.png | Cofre de casa aberto e vazio dentro do armario (gerada IA - carrossel 193, a empresa engoliu o que voces juntaram) | objeto, cofre, vazio, patrimonio |
| 876.png | Porteira de sitio fechada com corrente e placa de venda sem letras (gerada IA - carrossel 193, vendeu o sitio pra cobrir o caixa) | objeto, sitio, porteira, venda, patrimonio |
| 877.png | Dono de costas na porta da cozinha a noite com a pasta na mao, familia ao fundo (gerada IA - carrossel 193, em casa ninguem sabe) | pessoa, casa, noite, segredo |
| 878.png | Ampulheta de madeira escorrendo sobre a mesa (gerada IA - carrossel 193, os anos que passaram nao voltam) | objeto, ampulheta, tempo |
| 879.png | Album de fotos de familia aberto com fotos de uma crianca em varias idades (gerada IA - carrossel 193, descobrir pela foto que o filho cresceu) | objeto, album, fotos, filho, tempo |
| 880.png | Livro-caixa aberto organizado com regua e caneta, maos do dono entrando por baixo (gerada IA - carrossel 193, gestao de verdade) | maos, livro-caixa, gestao, clareza |
| 881.png | Sapatinhos de crianca ao lado de sapatos sociais de adulto na soleira de casa (gerada IA - carrossel 193, faz pelos seus filhos) | objeto, sapatos, pai-e-filho, cta |
| 882.png | Estrada de terra com trilha de pegadas de bota e, ao lado, atalho pelo mato sem nenhuma pegada (gerada IA - carrossel 195, pegadas) | paisagem, pegadas, estrada, atalho |
| 883.png | Bifurcacao de terra: uma trilha de pegadas firme no seco, a outra afundando na lama (gerada IA - carrossel 195, pegadas) | paisagem, pegadas, bifurcacao, lama |
| 884.png | Celular aceso largado sobre pilha de contas e boletos na mesa, cafe ao lado (gerada IA - carrossel 195, pegadas) | objeto, celular, contas, escritorio |
| 885.png | Relogio dourado sobre o capo de carro esportivo (gerada IA - carrossel 195, pegadas) | objeto, relogio, carro, ostentacao, guru |
| 886.png | Frasco antigo de tonico milagroso de vendedor ambulante sobre balcao (gerada IA - carrossel 195, pegadas) | objeto, frasco, formula, promessa |
| 887.png | Balde amassado tombado e extintor velho no chao de galpao, mancha queimada (gerada IA - carrossel 195, pegadas) | objeto, balde, extintor, incendio |
| 888.png | Atalho batido no mato terminando na beira de um barranco (gerada IA - carrossel 195, pegadas) | paisagem, atalho, barranco, erro |
| 889.png | Livro velho aberto sobre mesa simples de madeira com lapis curto (gerada IA - carrossel 195, pegadas) | objeto, livro, estudo, origem |
| 890.png | Pilha de livros gastos cheios de marcadores ao lado de uma botina de trabalho (gerada IA - carrossel 195, pegadas) | objeto, livros, botina, estudo |
| 891.png | Par de botas de couro gastas e sujas de terra (gerada IA - carrossel 195, pegadas) | objeto, botas, caminho, trabalho |
| 892.png | Carteira escolar de madeira vazia num canto, tampo riscado (gerada IA - carrossel 195, pegadas) | objeto, escola, carteira, estudo |
| 893.png | Apostila espiral aberta cheia de anotacoes a mao com caneta por cima (gerada IA - carrossel 195, pegadas) | objeto, apostila, anotacoes, estudo |
| 894.png | Pegadas de bota subindo ladeira de terra ao amanhecer (gerada IA - carrossel 195, pegadas) | paisagem, pegadas, ladeira, cta |
| 895.png | Mesa de escritorio soterrada por pilhas de livros e cadernos, obesidade mental (gerada IA - carrossel 196, quem executa e rei) | objeto, livros, excesso, estudo, capa |
| 896.png | Fone de ouvido, celular apagado e tres cadernos abertos cheios de anotacao (gerada IA - carrossel 196, quem executa e rei) | objeto, cadernos, fone, celular, consumo |
| 897.png | Gaveta entreaberta cheia de cadernos e crachas de evento esquecidos (gerada IA - carrossel 196, quem executa e rei) | objeto, gaveta, cadernos, cracha, evento |
| 898.png | Banca de feira de madeira vazia com caixotes no chao (gerada IA - carrossel 196, quem executa e rei) | objeto, feira, banca, caixotes, origem |
| 899.png | Chuteira velha enlameada na beira do gramado (gerada IA - carrossel 196, quem executa e rei) | objeto, chuteira, jogo, esporte, execucao |
| 900.png | Rei de xadrez de pe com as outras pecas caidas (gerada IA - carrossel 196, quem executa e rei) | objeto, xadrez, rei, vitoria |
| 901.png | Anilhas de ferro e barra no chao de academia antiga (gerada IA - carrossel 196, quem executa e rei) | objeto, academia, anilhas, peso, preco |
| 902.png | Relogio de mesa marcando oito horas ao lado de pasta de couro (gerada IA - carrossel 196, quem executa e rei) | objeto, relogio, pasta, reuniao, rotina |
| 903.png | Poltrona de couro com livro virado no braco e pilha de livros (gerada IA - carrossel 196, quem executa e rei) | objeto, poltrona, livros, conforto |
| 904.png | Sala de reuniao vazia com mesa comprida e cadeiras (gerada IA - carrossel 196, quem executa e rei) | ambiente, reuniao, mesa, cadeiras, vazio |
| 905.png | Quadro de cortica com post-its desbotados caindo no chao (gerada IA - carrossel 196, quem executa e rei) | objeto, cortica, post-it, ideias, abandono |
| 906.png | Mao martelando um prego numa tabua (gerada IA - carrossel 196, quem executa e rei) | mao, martelo, prego, fazer, execucao |
| 907.png | Degraus de pedra gastos no meio pelo uso (gerada IA - carrossel 196, quem executa e rei) | objeto, escada, degraus, repeticao, desgaste |
| 908.png | Agenda semanal aberta preenchida com caneta, caderno fechado ao lado (gerada IA - carrossel 196, quem executa e rei) | objeto, agenda, rotina, caneta, gestao |
| 909.png | Coroa de metal gasta numa bancada de oficina com ferramentas (gerada IA - carrossel 196, quem executa e rei) | objeto, coroa, rei, ferramentas, cta |
| 910.png | Porteira de madeira de pomar fechada, fileiras de arvores atras (gerada IA - carrossel 199, regra numero um) | objeto, porteira, pomar, fazenda, entrada |
| 911.png | Macieira jovem quase sem folhas com uma unica maca baixa (gerada IA - carrossel 199, regra numero um) | objeto, macieira, fruto, pomar, escassez |
| 912.png | Pulpito de madeira vazio com microfone antigo e cadeiras vazias (gerada IA - carrossel 199, regra numero um) | objeto, pulpito, palco, palestra, discurso |
| 913.png | Envelope de pagamento fino sozinho numa mesa de reuniao grande (gerada IA - carrossel 199, regra numero um) | objeto, envelope, pagamento, pro-labore, mesa |
| 914.png | Molho de chaves antigas sobre pasta de couro fechada (close) (gerada IA - carrossel 199, regra numero um) | objeto, chaves, casa, patrimonio, risco |
| 915.png | Relogio de ponto antigo com cartao no encaixe (gerada IA - carrossel 199, regra numero um) | objeto, relogio de ponto, emprego, cartao, clt |
| 916.png | Cesto de vime cheio de macas colhidas ao pe de uma arvore (gerada IA - carrossel 199, regra numero um) | objeto, cesto, macas, colheita, dividendo |
| 917.png | Cadeira com paleto e gravata largados, mesa com abajur a noite (gerada IA - carrossel 199, regra numero um) | objeto, cadeira, paleto, cansaco, noite |
| 918.png | Bancada de oficina parada com ferramentas e capacete (gerada IA - carrossel 199, regra numero um) | objeto, bancada, ferramentas, capacete, time |
| 919.png | Mesa de familia posta com pratos e travessa central vazia (gerada IA - carrossel 199, regra numero um) | objeto, mesa, pratos, vazio, dividir |
| 920.png | Lavoura de feijao em fileiras, plantas grandes em primeiro plano (gerada IA - carrossel 199, regra numero um) | objeto, lavoura, plantacao, fileiras, consequencia |
| 921.png | Interior de armazem rural com sacas e caixotes, luz da manha entrando (gerada IA - carrossel 199, regra numero um) | objeto, armazem, sacas, caixotes, manha |
| 922.png | Balanca de pratos antiga com cesto de macas num prato e outro vazio (gerada IA - carrossel 199, regra numero um) | objeto, balanca, macas, rico ou pobre, clareza |
| 923.png | Pomar carregado de frutas com cestos de colheita no chao (gerada IA - carrossel 199, regra numero um) | objeto, pomar, fartura, colheita, prosperidade |
| 924.png | Mao colhendo uma maca madura do galho (gerada IA - carrossel 199, regra numero um) | mao, maca, colheita, prospero, cta |
| 925.png | Homem de terno ajoelhado de costas no corredor de auditorio vazio diante do palco (gerada IA - carrossel 202, deus nao e argumento de venda) | pessoa, ajoelhado, auditorio, fragil, capa |
| 926.png | Maquininha de cartao e microfone sobre pulpito de acrilico (gerada IA - carrossel 202, deus nao e argumento de venda) | objeto, pulpito, maquininha, microfone, venda |
| 927.png | Cadeira dobravel com contrato, caneta e cracha em branco no assento (gerada IA - carrossel 202, deus nao e argumento de venda) | objeto, cadeira, contrato, cracha, fechamento |
| 928.png | Anzol com isca apoiado em pedra molhada a beira d'agua (gerada IA - carrossel 202, deus nao e argumento de venda) | objeto, anzol, isca, pescar, presa |
| 929.png | Empresario sozinho na primeira fileira, maos juntas, olhando o palco (gerada IA - carrossel 202, deus nao e argumento de venda) | pessoa, auditorio, espera, milagre, ansiedade |
| 930.png | Cadeiras dobraveis desarrumadas com copos e papeis no chao apos evento (gerada IA - carrossel 202, deus nao e argumento de venda) | objeto, cadeiras, auditorio vazio, depois, abuso |
| 931.png | Microfone desligado deitado no piso de madeira do palco (gerada IA - carrossel 202, deus nao e argumento de venda) | objeto, microfone, palco, silencio, opiniao |
| 932.png | Vela branca acesa em castical de barro sobre mesa rustica (gerada IA - carrossel 202, deus nao e argumento de venda) | objeto, vela, fe, respeito, silencio |
| 933.png | Proposta comercial impressa com calculadora e caneta em cima (gerada IA - carrossel 202, deus nao e argumento de venda) | objeto, proposta, calculadora, numero, prova |
| 934.png | Porta de saida de auditorio entreaberta com luz do corredor (gerada IA - carrossel 202, deus nao e argumento de venda) | objeto, porta, saida, ir embora, luz |
| 935.png | Mesa de reuniao com relatorios, cafe e cadeiras em volta (gerada IA - carrossel 202, deus nao e argumento de venda) | objeto, reuniao, relatorios, rito semanal, gestao |
| 936.png | Sala de treinamento com mesas, cadernos abertos e canetas (gerada IA - carrossel 202, deus nao e argumento de venda) | objeto, sala de aula, cadernos, treinamento, oferta |
| 937.png | Homem de terno saindo pela porta do auditorio rumo ao corredor claro, de costas (gerada IA - carrossel 202, deus nao e argumento de venda) | pessoa, saida, porta, firmeza, cta |
| 938.png | Caixinha de remedio com tarja preta, despertador tocando e chave do carro no criado-mudo (gerada IA - carrossel 198, remedio pro desmotivado) | objeto, remedio, despertador, levantar, desmotivacao |
| 939.png | Sapatos sociais engraxados e pasta de couro na soleira, prontos pra sair (gerada IA - carrossel 198, remedio pro desmotivado) | objeto, sapatos, pasta, ir trabalhar, disciplina |
| 940.png | Carrinho de lata largado no tapete ao pe da cadeira de diretor vazia (gerada IA - carrossel 198, remedio pro desmotivado) | objeto, brinquedo, crianca, cadeira de dono, imaturidade |
| 941.png | Telefone de disco fora do gancho e pilha de relatorios intocada (gerada IA - carrossel 198, remedio pro desmotivado) | objeto, telefone, relatorios, fuga, procrastinacao |
| 942.png | Cadeira de diretor virada de costas pra mesa, de frente pra parede (gerada IA - carrossel 198, remedio pro desmotivado) | objeto, cadeira, birra, castigo, dono |
| 943.png | Relogio de ponto de fabrica com cartoes no suporte (gerada IA - carrossel 198, remedio pro desmotivado) | objeto, relogio de ponto, cartoes, cobranca, funcionario |
| 944.png | Marmitas e capacetes enfileirados no banco do vestiario da fabrica (gerada IA - carrossel 198, remedio pro desmotivado) | objeto, marmitas, capacetes, familias, folha de pagamento |
| 945.png | Caneta-tinteiro sobre contrato assinado e carimbo (texto ilegivel) (gerada IA - carrossel 198, remedio pro desmotivado) | objeto, contrato, assinatura, aval, escolha |
| 946.png | Chave de carro com chaveiro de couro sobre pilha de boletos amarrados (gerada IA - carrossel 198, remedio pro desmotivado) | objeto, chave, boletos, bonus e onus, dono |
| 947.png | Cinzeiro de vidro grande com fosforo queimado e fio de fumaca (gerada IA - carrossel 198, remedio pro desmotivado) | objeto, fosforo, apagou, motivacao passageira |
| 948.png | Mesa escura com livro-caixa fechado e empoeirado, maquina de somar ao lado (gerada IA - carrossel 198, remedio pro desmotivado) | objeto, escuro, livro-caixa, numero, sem clareza |
| 949.png | Maquina de calcular antiga e livro-caixa aberto sob sol forte de manha (gerada IA - carrossel 198, remedio pro desmotivado) | objeto, calculadora, livro-caixa, clareza, gana |
| 950.png | Agenda aberta com horario circulado e relogio de mesa (gerada IA - carrossel 198, remedio pro desmotivado) | objeto, agenda, rito, rotina, oferta |
| 951.png | Criado-mudo com caixinha de remedio fechada e despertador desligado, cama vazia (gerada IA - carrossel 198, remedio pro desmotivado) | objeto, remedio, despertador, cama vazia, cta |
| 952.png | Luvas de couro de estivador novas, sem uso, sobre pilha de sacas no cais (gerada IA - carrossel 200, empresario nutella) | objeto, luvas novas, sem uso, nutella, capa |
| 953.png | Apito e prancheta (ilegivel) sobre caixote molhado de chuva no cais, navios ao fundo (gerada IA - carrossel 200, empresario nutella) | objeto, apito, prancheta, chuva, reclamacao |
| 954.png | Cabo de amarracao frouxo caido na agua junto ao cabeco do cais (gerada IA - carrossel 200, empresario nutella) | objeto, corda frouxa, solto, fraco |
| 955.png | Banco de madeira vazio no cais com garrafa termica e jornal (gerada IA - carrossel 200, empresario nutella) | objeto, banco vazio, conforto, reclamar |
| 956.png | Saca de cafe largada no chao ao pe da prancha do navio (gerada IA - carrossel 200, empresario nutella) | objeto, saca, peso largado, sem dono |
| 957.png | Estivador de costas subindo a prancha com saca nos ombros (gerada IA - carrossel 200, empresario nutella) | pessoa de costas, estivador, peso, preco |
| 958.png | Telefone de parede antigo com fone fora do gancho, banquinho e caixote no cais (gerada IA - carrossel 200, empresario nutella) | objeto, telefone fora do gancho, fuga, decisao adiada |
| 959.png | Quepe de capitao amassado sobre rolo de corda no cais (gerada IA - carrossel 200, empresario nutella) | objeto, quepe, capitao, lider frouxo |
| 960.png | Mala de lona de marinheiro ao pe da prancha de outro navio (gerada IA - carrossel 200, empresario nutella) | objeto, mala, partida, talento vai embora |
| 961.png | Galpao de carga parado, portao aberto, cadeiras vazias encostadas (gerada IA - carrossel 200, empresario nutella) | lugar, galpao parado, equipe que sobrou |
| 962.png | Mao firme no timao de madeira, baia ao fundo (gerada IA - carrossel 200, empresario nutella) | mao, timao, comando, lider |
| 963.png | Ancora de ferro enorme deitada no cais com corrente (gerada IA - carrossel 200, empresario nutella) | objeto, ancora, peso, ser dono |
| 964.png | Diario de bordo aberto (ilegivel) com bussola em cima, porto ao fundo (gerada IA - carrossel 200, empresario nutella) | objeto, diario de bordo, bussola, numero na mao |
| 965.png | Sino de bordo de bronze num poste de madeira no cais (gerada IA - carrossel 200, empresario nutella) | objeto, sino, rito, oferta |
| 966.png | Cabo de amarracao teso, bem amarrado ao cabeco de ferro (gerada IA - carrossel 200, empresario nutella) | objeto, corda tesa, pulso, firme, cta |
| 967.png | Duas estantes de partitura vazias no palco, cada uma virada pra um lado (gerada IA - carrossel 204, maestro em gente) | objeto, estante, dois caminhos, escolha |
| 968.png | Cadeiras de orquestra com violinos e violoncelo esperando os musicos (gerada IA - carrossel 204, maestro em gente) | objeto, cadeiras vazias, equipe que falta |
| 969.png | Homem-banda de rua tocando tudo sozinho (bumbo, gaita, sanfona, pratos) (gerada IA - carrossel 204, maestro em gente) | pessoa, homem-banda, dono que faz tudo |
| 970.png | Molho enorme de chaves e carimbo sobre a mesa (gerada IA - carrossel 204, maestro em gente) | objeto, chaves, carimbo, tudo passa pela mao do dono |
| 971.png | Fosso de orquestra cheio de estantes e cadeiras vazias (gerada IA - carrossel 204, maestro em gente) | lugar, orquestra vazia, mais gente |
| 972.png | Agenda de papel aberta, paginas lotadas (ilegivel), caneta (gerada IA - carrossel 204, maestro em gente) | objeto, agenda lotada, tamanho da agenda |
| 973.png | Maos de varios musicos afinando instrumentos juntos (gerada IA - carrossel 204, maestro em gente) | maos, time, gente, orquestra |
| 974.png | Homem de gravata tentando segurar violino, trompete e tambor ao mesmo tempo (gerada IA - carrossel 204, maestro em gente) | pessoa, sobrecarga, fazer tudo sozinho |
| 975.png | Metronomo parado sobre piano fechado (gerada IA - carrossel 204, maestro em gente) | objeto, metronomo, crescimento travado |
| 976.png | Homem-banda exausto sentado no meio-fio, instrumentos no chao (gerada IA - carrossel 204, maestro em gente) | pessoa, burnout, cansaco |
| 977.png | Professor corrigindo o arco do violino de um aluno (gerada IA - carrossel 204, maestro em gente) | pessoas, formar gente, ensinar |
| 978.png | Maestro de costas, batuta erguida, orquestra tocando (gerada IA - carrossel 204, maestro em gente) | pessoas, maestro, lideranca, time |
| 979.png | Batuta pousada sobre partitura fechada na estante (gerada IA - carrossel 204, maestro em gente) | objeto, batuta, maestro, tese |
| 980.png | Ensaio de orquestra, musicos tocando juntos (gerada IA - carrossel 204, maestro em gente) | pessoas, orquestra, time, oferta |
| 981.png | Mao do maestro com a batuta em movimento, orquestra embaixo (gerada IA - carrossel 204, maestro em gente) | mao, batuta, comando, cta |
| 982.png | Desvio de trilho com a alavanca parada no meio, trilhos abrindo pra lados opostos (gerada IA - carrossel 205, sem direcao) | objeto, ferrovia, direcao, escolha, capa |
| 983.png | Despertador antigo de duas campainhas a um minuto da hora sobre mesa (gerada IA - carrossel 205, sem direcao) | objeto, urgencia, bomba, tempo |
| 984.png | Telefone de disco fora do gancho e pilha de envelopes amarrados na mesa (gerada IA - carrossel 205, sem direcao) | objeto, problemas, pendencias, decisao adiada |
| 985.png | Painel de sinais ferroviarios com todas as lampadas acesas (gerada IA - carrossel 205, sem direcao) | objeto, urgencia, tudo ao mesmo tempo |
| 986.png | Baldes de areia de incendio e extintor antigo na plataforma, um balde tombado (gerada IA - carrossel 205, sem direcao) | objeto, incendio, apagar fogo |
| 987.png | Homem de terno sozinho no banco da plataforma a noite, cabeca baixa (gerada IA - carrossel 205, sem direcao) | pessoa, cansaco, exaustao, solidao |
| 988.png | Luvas de trabalho e pano largados num banco de madeira (gerada IA - carrossel 205, sem direcao) | objeto, desistencia, jogar a toalha, cansaco |
| 989.png | Mapa ferroviario aberto, bussola e binoculo sobre a mesa (gerada IA - carrossel 205, sem direcao) | objeto, visao de futuro, direcao, plano |
| 990.png | Pai e filho de costas de maos dadas na plataforma olhando o trem (gerada IA - carrossel 205, sem direcao) | pessoas, familia, futuro, visao |
| 991.png | Trilho reto com pedras soltas e dormente rachado (gerada IA - carrossel 205, sem direcao) | objeto, problemas no caminho, imprevisto |
| 992.png | Maos puxando a alavanca de ferro do desvio (gerada IA - carrossel 205, sem direcao) | mao, escolha, decisao, proximo passo |
| 993.png | Locomotiva a vapor avancando de frente nos trilhos (gerada IA - carrossel 205, sem direcao) | objeto, movimento, avancar, esperanca |
| 994.png | Folha manuscrita ilegivel, caneta-tinteiro e relogio de bolso nas sete horas (gerada IA - carrossel 205, sem direcao) | objeto, plano, rito semanal, primeiro passo |
| 995.png | Maquinista de costas na cabine, mao no controle, trilho reto a frente (gerada IA - carrossel 205, sem direcao) | pessoa, comando, direcao, oferta |
| 996.png | Trilho reto ate o horizonte, sem desvios (gerada IA - carrossel 205, sem direcao) | paisagem, rumo, direcao, cta |
| 997.png | Megafone de lata largado no degrau da arquibancada vazia (gerada IA - carrossel 206, arquibancada grita) | objeto, critica, arquibancada, grito |
| 998.png | Chaves de casa sobre pasta de papelao amarrada (gerada IA - carrossel 206, arquibancada grita) | objeto, garantia, risco, patrimonio |
| 999.png | Dois homens rindo na mesa de churrasco, um apontando o dedo (gerada IA - carrossel 206, arquibancada grita) | pessoas, palpite, critica, cunhado |
| 1000.png | Sapatos sociais engraxados e chapeu no degrau da arquibancada (gerada IA - carrossel 206, arquibancada grita) | objeto, quem assiste, de fora, limpo |
| 1001.png | Chuteiras de couro gastas e enlameadas na beira do campo (gerada IA - carrossel 206, arquibancada grita) | objeto, esforco, quem joga, peso |
| 1002.png | Homem sozinho na mesa do escritorio a noite sob o abajur (gerada IA - carrossel 206, arquibancada grita) | pessoa, decisao, solidao do dono, noite |
| 1003.png | Homem de terno de costas no meio do campo de terra vazio (gerada IA - carrossel 206, arquibancada grita) | pessoa, aposta, coragem, campo |
| 1004.png | Placar de madeira baixo com uma placa caida na grama (gerada IA - carrossel 206, arquibancada grita) | objeto, placar, numero, erro |
| 1005.png | Bandeira de torcida rasgada no alambrado (gerada IA - carrossel 206, arquibancada grita) | objeto, barulho, torcida, critica |
| 1006.png | Bola parada na marca do penalti, campo vazio (gerada IA - carrossel 206, arquibancada grita) | objeto, decisao adiada, nao decidir |
| 1007.png | Maos trocando a placa de numero do placar de madeira (gerada IA - carrossel 206, arquibancada grita) | mao, placar, informacao, ajuste |
| 1008.png | Placar de madeira de frente com todos os numeros no lugar (gerada IA - carrossel 206, arquibancada grita) | objeto, placar, verdade, numero |
| 1009.png | Catraca de ferro antiga da entrada do estadio (gerada IA - carrossel 206, arquibancada grita) | objeto, quanto entra, caixa, fluxo |
| 1010.png | Prancheta de tecnico com anotacoes ilegiveis no banco de reservas (gerada IA - carrossel 206, arquibancada grita) | objeto, raio-x, analise, oferta |
| 1011.png | Bola no fundo da rede, gol marcado (gerada IA - carrossel 206, arquibancada grita) | objeto, vitoria, jogo, cta |
| 1012.png | Coelho de terno correndo pela rua de pedra com relogio de bolso e pasta (gerada IA - carrossel 207, empresario coelho, fabula) | pessoa-bicho, pressa, corrida, capa |
| 1013.png | Coelho passando em disparada, bichos da vila virando a cabeca (gerada IA - carrossel 207, empresario coelho, fabula) | bicho, velocidade, admiracao, pressa |
| 1014.png | Grade 2x2: coelho acordando no escuro, abrindo filial, fechando negocio, correndo (gerada IA - carrossel 207, empresario coelho, fabula) | bicho, rotina, esforco, nunca para |
| 1015.png | Coelho correndo olhando aflito o relogio, bichos aplaudindo (gerada IA - carrossel 207, empresario coelho, fabula) | bicho, atraso, ansiedade, aplauso |
| 1016.png | Vista aerea de encruzilhada na floresta, coelho sozinho no centro (gerada IA - carrossel 207, empresario coelho, fabula) | paisagem, encruzilhada, escolha, perdido |
| 1017.png | Contra-plongee: coelho de costas e gato no alto da placa de madeira em branco (gerada IA - carrossel 207, empresario coelho, fabula) | bicho, pergunta, encruzilhada, conselheiro |
| 1018.png | Gato no alto da placa de direcao em branco, pata erguida perguntando (gerada IA - carrossel 207, empresario coelho, fabula) | bicho, pergunta, sabedoria, destino |
| 1019.png | Coelho de costas diante de tres estradas, orelhas caidas (gerada IA - carrossel 207, empresario coelho, fabula) | bicho, duvida, nao sei, caminhos |
| 1020.png | Gato dando de ombros no alto da placa de madeira (gerada IA - carrossel 207, empresario coelho, fabula) | bicho, qualquer caminho, ironia, sabedoria |
| 1021.png | Coelho olhando pra tras a estrada longa cheia de pegadas (gerada IA - carrossel 207, empresario coelho, fabula) | bicho, passado, anos de estrada, reflexao |
| 1022.png | Coelho correndo pela estrada, toca da familia pequena la atras (gerada IA - carrossel 207, empresario coelho, fabula) | bicho, direcao errada, familia, distancia |
| 1023.png | Relogio de bolso e chapeu-coco ao pe da placa de direcao em branco (gerada IA - carrossel 207, empresario coelho, fabula) | objeto, moral, destino, pausa |
| 1024.png | Vista de cima: coelho correndo em circulo em volta de arvore (gerada IA - carrossel 207, empresario coelho, fabula) | bicho, movimento sem direcao, circulo, repeticao |
| 1025.png | Coelho na encruzilhada apontando firme um caminho (gerada IA - carrossel 207, empresario coelho, fabula) | bicho, decisao, rota, correcao |
| 1026.png | Vista aerea de labirinto de sebes com coelho minusculo correndo (gerada IA - carrossel 207, empresario coelho, fabula) | paisagem, labirinto, direcao errada, tragedia |
| 1027.png | Coelho sentado num tronco estudando mapa sem letras (gerada IA - carrossel 207, empresario coelho, fabula) | bicho, planejamento, mapa, oferta |
| 1028.png | Coelho no alto da colina olhando a estrada que termina na toca da familia (gerada IA - carrossel 207, empresario coelho, fabula) | bicho, destino, norte, cta |
| 1029.png | Maquete de predio alto sobre terreno vazio com estacas (gerada IA - carrossel 201, fe de empresario) | obra, visao, fe, capa |
| 1030.png | Planta enrolada e capacete sobre cavaletes em terreno vazio (gerada IA - carrossel 201, fe de empresario) | obra, comeco, fe |
| 1031.png | Botinas de obra afundadas na lama (gerada IA - carrossel 201, fe de empresario) | objeto, parado, raiz, pe no chao |
| 1032.png | Esqueleto de predio inacabado com vergalhoes pra cima (gerada IA - carrossel 201, fe de empresario) | obra, estagnacao, parou |
| 1033.png | Pa cravada em monte de areia e carrinho de mao no fim do dia (gerada IA - carrossel 201, fe de empresario) | obra, esforco, cansaco |
| 1034.png | Engenheiro de costas agachado olhando terreno com a planta (gerada IA - carrossel 201, fe de empresario) | pessoa de costas, visao, antes de existir |
| 1035.png | Capela de madeira vazia com pulpito e cruz (gerada IA - carrossel 201, fe de empresario) | igreja, credo, pregador, lideranca |
| 1036.png | Bandeira de torcida enrolada largada na arquibancada vazia (gerada IA - carrossel 201, fe de empresario) | torcida, ilusao, orcamento |
| 1037.png | Nivel e trena sobre planta presa por tijolo (gerada IA - carrossel 201, fe de empresario) | obra, numero, plano, medida |
| 1038.png | Mesa do barracao com plantas, despertador e caderno (gerada IA - carrossel 201, fe de empresario) | rotina, acompanhamento, semana |
| 1039.png | Predio alto quase pronto com grua, visto de longe (gerada IA - carrossel 201, fe de empresario) | obra, extraordinario, crescimento |
| 1040.png | Mesa de reuniao no barracao com planta e quatro capacetes (gerada IA - carrossel 201, fe de empresario) | reuniao, metodo, oferta |
| 1041.png | Predio modernista pronto com o ultimo andaime saindo (gerada IA - carrossel 201, fe de empresario) | obra, resultado, grande, cta |
| 1042.png | Mesa comprida com envelopes de pagamento em cada lugar e a cadeira do dono sem nada (gerada IA - carrossel 226, 13o do dono) | 13o, dezembro, dono, folha, capa |
| 1043.png | Caneta-tinteiro sobre contrato bancario com calendario de mesa (gerada IA - carrossel 226, 13o do dono) | emprestimo, aval, assinatura, banco |
| 1044.png | Casa terrea de familia com muro baixo e portao, ceu nublado claro (gerada IA - carrossel 226, 13o do dono) | casa, familia, garantia, patrimonio |
| 1045.png | Balcao do departamento pessoal com envelopes, carnes, guias e somadora (gerada IA - carrossel 226, 13o do dono) | folha, 13o, banco, imposto, contador |
| 1046.png | Homem de terno sozinho de costas no fim da mesa da confraternizacao vazia (gerada IA - carrossel 226, 13o do dono) | dono, solidao, risco, fim de ano |
| 1047.png | Holerite fino ao lado de pilha alta de contratos amarrados (gerada IA - carrossel 226, 13o do dono) | pro-labore, risco, assinatura, contraste |
| 1048.png | Cofre de chao aberto e vazio (gerada IA - carrossel 226, 13o do dono) | dividendo, lucro, vazio, dono |
| 1049.png | Mesa de ceia de Natal com livro-caixa fechado sobre um prato (gerada IA - carrossel 226, 13o do dono) | natal, familia, numero, rico ou pobre |
| 1050.png | Pasta de escrituras acorrentada com cadeado ao lado de calendarios velhos (gerada IA - carrossel 226, 13o do dono) | patrimonio, garantia, anos, preso |
| 1051.png | Paleto na cadeira com envelope de dinheiro no bolso interno (gerada IA - carrossel 226, 13o do dono) | dividendo, bolso do dono, regra |
| 1052.png | Mesa organizada com livro-razao aberto, somadora e pastas (gerada IA - carrossel 226, 13o do dono) | gestao, numero, metodo, oferta |
| 1053.png | Prato de ceia com envelope de pagamento aberto cheio de notas (gerada IA - carrossel 226, 13o do dono) | 13o, dezembro, dividendo, cta |
| 1054.png | Maos de seis pessoas diferentes empilhadas no centro de uma mesa de madeira (gerada IA - carrossel 231, liderar e unir) | uniao, time, diversidade, capa |
| 1055.png | Ferramentas de oficios diferentes lado a lado numa bancada (trena, colher de pedreiro, estetoscopio, caneta, chave inglesa, plaina) (gerada IA - carrossel 231, liderar e unir) | diferenca, gente diferente, habilidades |
| 1056.png | Cordas trancadas num cabo so amarrado a argola de ferro num cais (gerada IA - carrossel 231, liderar e unir) | unir, objetivo unico, amarra |
| 1057.png | Barco de remo com oito remadores de corpos e idades diferentes, remos no mesmo angulo (gerada IA - carrossel 231, liderar e unir) | sincronia, itaidoshin, time, um so pensamento |
| 1058.png | Seis pessoas de roupas diferentes puxando a mesma corda (cabo de guerra) (gerada IA - carrossel 231, liderar e unir) | grupo, mesma direcao, sem uniforme, esforco |
| 1059.png | Cesto grande de laranjas no centro rodeado de cestos menores tambem cheios (gerada IA - carrossel 231, liderar e unir) | objetivo da empresa e de cada um, colheita, abundancia |
| 1060.png | Cordas saindo de um no central esticadas em direcoes diferentes (gerada IA - carrossel 231, liderar e unir) | cada um puxa pro seu lado, conflito, tensao |
| 1061.png | Fileira de lampioes diferentes acesos sobre um banco de madeira (gerada IA - carrossel 231, liderar e unir) | de dentro, cada um, chama propria |
| 1062.png | Grupo caminhando atras de um lider numa trilha de campo, de costas (gerada IA - carrossel 231, liderar e unir) | lideranca, seguir, caminho |
| 1063.png | Mesa comprida com cadeiras todas diferentes em volta (gerada IA - carrossel 231, liderar e unir) | cultura, reuniao, oferta, gente diferente |
| 1064.png | Grupo de pessoas diferentes de costas, abracadas ombro a ombro (gerada IA - carrossel 231, liderar e unir) | uniao, time, cta |
