#!/bin/bash
# Fecha o carrossel 78: renderiza os 14 slides, roda a regua de vao morto e entrega no Desktop.
set -e
BASE=/Users/pedrohenrique/Documents/tatsuo-carrossel/conteudo/carrosseis/78_biblia-de-vendas
DEST=~/Desktop/"carrosseis claude"/biblia

echo "== render =="
node "$BASE/_scripts/render.js"

echo
echo "== regua de vao morto =="
python3 "$BASE/_scripts/check.py"

echo
echo "== entrega =="
mkdir -p "$DEST"
cp "$BASE"/instagram/slide-*.png "$DEST"/
cp "$BASE"/legenda.txt "$DEST"/
ls "$DEST"
