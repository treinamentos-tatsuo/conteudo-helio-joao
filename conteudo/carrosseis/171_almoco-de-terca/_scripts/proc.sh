#!/bin/zsh
# proc.sh N [N...]: post -> topo -> build+render em altura natural -> fit (mantém H já fixados) -> build -> render -> check
cd "$(dirname "$0")"
python3 post.py "$@" && python3 topo.py "$@" && python3 build.py >/dev/null && node render.js "$@" >/dev/null && python3 fit.py | grep -v "sem assunto\|mantido\|ja OK" ; python3 build.py >/dev/null && node render.js "$@" >/dev/null && python3 check.py "$@"
