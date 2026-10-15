#!/usr/bin/env python3
"""Image-edit em cima da PRÓPRIA imagem gerada (micro-ajuste "só isso, sem mexer em mais nada"):
mantém cena, luz e grão e muda só o que foi pedido. Não é pixel-idêntico (o motor re-renderiza).
Base: o edit.py do post 175_louca (o mesmo do 102, 145 e 166), com a pasta do post como argumento.

Uso, sempre da raiz do projeto:
  python3 .claude/skills/frase/scripts/edit.py <pasta> <imagem-de-origem> <n-novo> "<pedido em inglês>"
  ex.: python3 .claude/skills/frase/scripts/edit.py conteudo/carrosseis/175_louca img-01.png 5 \
       "Move only the plate stack slightly to the left. Change nothing else: same light, same wall, same grain."

Lê <pasta>/imagens/<imagem-de-origem> e grava <pasta>/imagens/img-<n-novo>.png. Nunca sobrescreve:
se img-<n-novo> já existe, para. A original fica intacta.

Dois caminhos pelo proxy openai-oauth (porta 10531), tentados nesta ordem:
  1. /v1/images/edits (multipart, gpt-image-2, prompt em --form-string): o caminho de image-edit que a
     skill gpt-image2-ratos documenta e que os posts de papel e vidro usam desde 07/10/2026;
  2. /v1/responses com o modelo gpt-5.5 chamando a tool image_generation: o caminho que fez todos os
     micro-ajustes desta skill até 02/10/2026 (175).
Testado em 13/10/2026: o caminho 1 respondeu em 24 s, mantendo a cena (saída em 1254x1254; o slide usa
a largura toda, então a resolução não muda nada).
Se os dois falharem, avisar o user com o conteúdo de <pasta>/_scripts/_err-edit-NN.txt.
"""
import base64, json, pathlib, subprocess, sys, time

SIZE = "1024x1024"
PROXY = "http://127.0.0.1:10531"

if len(sys.argv) < 5:
    sys.exit(__doc__)
POST = pathlib.Path(sys.argv[1]).resolve()
SCR = POST / "_scripts"
IMG = POST / "imagens"
src = IMG / sys.argv[2]
n = int(sys.argv[3])
prompt = sys.argv[4]
out = IMG / f"img-{n:02d}.png"
if not src.exists():
    sys.exit(f"Não achei a imagem de origem: {src}")
if out.exists():
    sys.exit(f"{out.name} já existe. Use um número novo: a versão anterior nunca é sobrescrita.")
SCR.mkdir(parents=True, exist_ok=True)
erros = []


def via_images_edits():
    r = subprocess.run(["curl", "-sS", "-m", "500", "-X", "POST", f"{PROXY}/v1/images/edits",
                        "-F", "model=gpt-image-2", "-F", f"image=@{src}", "-F", f"size={SIZE}",
                        "-F", "quality=high", "--form-string", f"prompt=Edit this image: {prompt}"],
                       capture_output=True, text=True, timeout=600)
    try:
        return json.loads(r.stdout)["data"][0]["b64_json"]
    except Exception:
        erros.append("/v1/images/edits:\n" + r.stdout[-3000:] + "\n" + r.stderr[-1000:])
        return None


def via_responses():
    b64in = base64.b64encode(src.read_bytes()).decode()
    payload = {
        "model": "gpt-5.5",
        "input": [
            {"role": "developer", "content": "You are an image editing assistant. Your sole function is to invoke the image_generation tool. Never respond with plain text."},
            {"role": "user", "content": [
                {"type": "input_image", "image_url": f"data:image/png;base64,{b64in}"},
                {"type": "input_text", "text": f"Edit this image: {prompt}"}]}],
        "tools": [{"type": "image_generation", "quality": "high", "size": SIZE, "moderation": "low"}],
        "tool_choice": "required", "stream": True}
    pf = SCR / f"_payload-edit-{n:02d}.json"
    pf.write_text(json.dumps(payload))
    r = subprocess.run(["curl", "-sS", "-N", "-X", "POST", f"{PROXY}/v1/responses",
                        "-H", "Content-Type: application/json", "-H", "Accept: text/event-stream", "-d", f"@{pf}"],
                       capture_output=True, text=True, timeout=600)
    pf.unlink(missing_ok=True)
    for block in r.stdout.split("\n\n"):
        data = "".join(l[6:] for l in block.split("\n") if l.startswith("data: "))
        if not data or data == "[DONE]":
            continue
        try:
            e = json.loads(data)
        except json.JSONDecodeError:
            continue
        if e.get("type") == "response.output_item.done":
            item = e.get("item", {})
            if item.get("type") == "image_generation_call" and item.get("result"):
                return item["result"]
    erros.append("/v1/responses:\n" + r.stdout[-3000:] + "\n" + r.stderr[-1000:])
    return None


t0 = time.time()
for nome, via in (("images/edits", via_images_edits), ("responses", via_responses)):
    b64 = via()
    if b64:
        out.write_bytes(base64.b64decode(b64))
        print(f"[{n:02d}] OK em {time.time()-t0:.0f}s via {nome} -> {out.name} (editada de {src.name})")
        print("FIM")
        sys.exit(0)
(SCR / f"_err-edit-{n:02d}.txt").write_text("\n\n".join(erros))
print(f"[{n:02d}] FALHOU nos dois caminhos ({time.time()-t0:.0f}s); ver _scripts/_err-edit-{n:02d}.txt")
sys.exit(1)
