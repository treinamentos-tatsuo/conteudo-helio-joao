# Esta máquina é Windows: tradução dos comandos de Mac

As skills foram escritas num Mac. Nesta máquina (Windows, com o Claude rodando comandos no Git Bash), toda vez que uma skill mandar um destes comandos, usar o equivalente da direita. Não pular o passo: traduzir.

| Na skill (Mac) | Aqui (Windows, Git Bash) |
|---|---|
| `python3 ...` | `python ...` (se `python3` não responder; ver SETUP passo 2) |
| `open -a Preview arquivo.png` / "abrir no Preview" | `explorer.exe "$(cygpath -w arquivo.png)"` (abre no visualizador de fotos) |
| `open pasta` / "abrir a pasta no Finder" | `explorer.exe "$(cygpath -w pasta)"` |
| `caffeinate` (manter o PC acordado durante o timer do /manychat) | Não existe. Antes de armar o timer, garantir que o PC não vai suspender: usar a opção de manter acordado do app do Claude, se aparecer, ou `powercfg /change standby-timeout-ac 0` (e `powercfg /change standby-timeout-ac 30` depois). O timer em si (`sleep` em segundo plano) funciona igual. Também aqui: nunca deixar nada rodando solto em segundo plano enquanto espera o alarme. |
| `LC_ALL=pt_BR.UTF-8 date '+%A %d/%m/%Y'` (conferir o dia da semana) | `python -c "import datetime as d;t=d.date.today();print(['segunda','terça','quarta','quinta','sexta','sábado','domingo'][t.weekday()], t.strftime('%d/%m/%Y'))"` |
| `date -j -f '%d/%m/%Y' '14/10/2026' '+%A'` (dia da semana de outra data) | `python -c "import datetime as d;print(['segunda','terça','quarta','quinta','sexta','sábado','domingo'][d.date(2026,10,14).weekday()])"` |
| `shasum -a 256 -c checksums.txt` | `sha256sum -c checksums.txt` (o importador já confere sozinho) |
| `swift scripts/lift.swift foto.jpg recorte.png` (recorte do Hélio na capa estilo revista do /frase-foto) | Não existe no Windows. Alternativa **ainda não testada**: `python -m pip install "rembg[cpu]"` e `rembg i foto.jpg recorte.png`. Na primeira vez, comparar o resultado com o caso 191 (`.claude/skills/frase-foto/casos/191-feira-capa-revista.jpg`) e mostrar ao João antes de usar. Se não ficar bom, fazer a capa sem o recorte. |
| `~/Library/LaunchAgents`, launchd, `launchctl` | Não se usa aqui (esta máquina não roda coleta de API). |
| `sips` | Já trocado pelo Pillow nos scripts desta cópia. |

## Cuidados do Windows

- **Área de trabalho no OneDrive.** Se o Windows guardar a Área de Trabalho dentro do OneDrive, o caminho real é `~/OneDrive/Desktop` (às vezes `~/OneDrive/Área de Trabalho`), não `~/Desktop`. Conferir no primeiro dia com `ls ~/Desktop ~/OneDrive/Desktop 2>/dev/null` e, se for o caso, usar o caminho certo em toda entrega (`carrosseis claude`, `frases claude`, `fotos para carrosséis`).
- **Fim de linha.** Scripts `.sh` com fim de linha do Windows (CRLF) quebram. O SETUP configura o Git pra não converter; se um `.sh` der erro estranho, converter com `sed -i 's/\r$//' arquivo.sh`.
- **Acentos nos caminhos** (`fotos para carrosséis`) funcionam, mas sempre entre aspas.
- **Fontes dos slides** vêm do Google Fonts: o render precisa de internet.
