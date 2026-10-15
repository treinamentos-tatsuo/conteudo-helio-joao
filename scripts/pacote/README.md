# Pacote diário de dados brutos (máquina principal → máquina do João)

A API da Meta não pode rodar em duas máquinas. Por isso a coleta de dados (Instagram, CRM GoHighLevel e leitura do painel do Manychat) acontece só na máquina principal, e a máquina do João recebe tudo por um pacote diário. O pacote leva o dado bruto, sem interpretação: cada máquina faz a própria análise.

Nenhum dos dois scripts chama API. Os dois usam só o Python 3 padrão.

## `gerar_pacote.py` (roda na máquina principal)

```bash
python3 scripts/pacote/gerar_pacote.py
```

Gera `~/Desktop/pacote-analytics-joao/pacote-AAAA-MM-DD.zip` (data de Brasília). Rodar de novo no mesmo dia substitui o zip do dia. Roda todo dia no fim do ritual, antes do Git.

O que vai no zip:
- `analise/`: `desempenho.json`, `desempenho.csv`, `_snapshots.csv` (Instagram), `leads.json` (CRM), `_disparos.json` (Manychat), `_painel-instagram.csv`, `_update.log`, `_pull.log`, e `registro-posts-factual.csv` (o registro de posts só com as colunas factuais: data, data_publicacao, post_id, pasta, formato, semente, pilar, funil, objetivo, palavra_chave).
- `posts/<pasta>/`: `carousel-text.md` e `legenda.txt` dos posts publicados nos últimos 14 dias. Do `carousel-text.md` sai só a linha "Etiqueta:" (a previsão).
- `MANIFESTO.md`: o que é cada arquivo, de onde vem, quando foi coletado, quantos registros, quais colunas.
- `checksums.txt` (sha256 de cada arquivo) e `pacote.json` (metadados pro importador).

Não vai: token ou credencial, previsões e resultados do registro, `hipoteses.md`, briefings do ritual, `_descartados.csv`, `_ressalvas.csv`, `_cauda-longa.csv`, imagens. Se aparecer padrão de token em qualquer arquivo, o script para e não gera nada.

`leads.json` tem nome, e-mail e telefone de leads: o zip só anda por canal privado.

## `importar_pacote.py` (roda na máquina do João)

```bash
python3 scripts/pacote/importar_pacote.py ~/Downloads/pacote-AAAA-MM-DD.zip
```

1. Confere o sha256 de cada arquivo. Se um só não bater, nada é copiado.
2. Copia `analise/*` para `conteudo/analise/`. O `registro-posts-factual.csv` vira `conteudo/analise/_registro-maquina-user.csv` e o manifesto vira `conteudo/analise/_pacote-MANIFESTO.md`. O `registro-posts.csv` do João nunca é tocado.
3. Copia `posts/<pasta>/` para `conteudo/carrosseis/_da-maquina-do-user/<pasta>/`. Essas pastas são só consulta: não contam na numeração dos carrosséis do João.
4. Anota cada importação (e cada recusa) em `conteudo/analise/_pacotes-importados.log`.

Recusa sozinho: zip adulterado, arquivo com caminho estranho, pacote mais velho que o último importado (a não ser com `--forcar`) e qualquer tentativa de importar no próprio projeto que gerou o pacote. Só entram os nomes de arquivo previstos; o resto é ignorado e anotado no log.

`--destino /caminho/do/projeto` importa em outro projeto (serve pra teste).
