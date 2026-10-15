#!/usr/bin/env bash
# gera slides 2..13 em sequencia (proxy reusado). Continua em erro; loga no fim.
cd "$(dirname "$0")/.."
BASE='black-and-white editorial vintage documentary photograph, 1930s to 1940s, desaturated, high contrast, heavy film grain, dramatic chiaroscuro lighting. The subject sits low in the lower-middle of the frame with foreground filling the bottom third and bleeding off the bottom edge. The ENTIRE upper half of the image is bright, pale, empty and hazy, fading to near-white at the very top edge for clean compositing. No text, no words, no letters, no logos, no emojis, no gradients, no added color, no modern objects, no stock photo look.'

declare -a N=(02 03 04 05 06 07 08 09 10 11 12 13)
declare -a S=(
"A man's hand running a finger down a long column of handwritten numbers in an open accounting ledger on a desk, close and deliberate, cuffed shirt sleeve."
"An exhausted businessman in shirt and tie slumped forward over a paper-covered desk, head resting heavily in one hand, worn out, late at night."
"A tall monotonous tower of identical stacked ledgers and paper reports on a desk, endless grey bureaucratic paperwork, oppressive repetition, no people."
"A businessman leaning back in his chair turned away from the work on his desk, staring off into the distance out of frame, distracted and restless."
"A single ornate vintage snake-oil tonic bottle standing on a table, elaborate old apothecary bottle with a decorative blank label and flourishes, a huckster miracle cure, theatrical light, no people, no legible text."
"A dramatic shaft of bright light beaming down through a tall window onto an empty office floor, dust motes floating in the beam, an almost religious glow, no people."
"A businessman seen from behind walking away from his desk toward an open doorway, leaving an open ledger and papers behind on the desk, abandoning his post."
"A dark shadowy figure embracing a seated businessman from behind, wrapping its arms around his shoulders, the man sitting calm and comfortable in his chair, ominous and intimate."
"One man leaning in very close to whisper into the ear of another seated businessman at a desk, a secret being told, conspiratorial mood, two figures."
"Steady weathered hands writing rows of figures into an open ledger on a desk in soft calm morning light, disciplined routine work, close view."
"A single banker lamp glowing alone on an empty desk in a dark deserted office late at night, the only source of light, everyone gone home, no people."
"A determined businessman sitting down firmly at his desk with sleeves rolled up, hands flat on the papers, taking command of his work again, resolute, morning light."
)

LOG=_build/gen-all.log; : > "$LOG"
for i in "${!N[@]}"; do
  n="${N[$i]}"; scene="Scene: ${S[$i]}"
  echo "=== img-$n START $(date +%H:%M:%S) ===" | tee -a "$LOG"
  if bash _build/gen.sh "$scene $BASE" "imagens/_raw/img-$n.png" >>"$LOG" 2>&1; then
    python3 _build/post.py "imagens/_raw/img-$n.png" "imagens/img-$n.png" >>"$LOG" 2>&1 \
      && echo "img-$n OK" | tee -a "$LOG" || echo "img-$n POST-FAIL" | tee -a "$LOG"
  else
    echo "img-$n GEN-FAIL" | tee -a "$LOG"
  fi
done
echo "=== DONE $(date +%H:%M:%S) ===" | tee -a "$LOG"
ls -1 imagens/img-*.png | tee -a "$LOG"
