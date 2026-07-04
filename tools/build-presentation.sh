#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

pandoc "$root/interpretations/metodo-in-sintesi.md" \
  --standalone \
  --from=markdown-native_divs \
  --to=revealjs \
  --slide-level=2 \
  --css=../assets/deck.css \
  -V revealjs-url=https://cdn.jsdelivr.net/npm/reveal.js@5.1.0 \
  -V theme=white \
  -V width=1180 \
  -V height=740 \
  -V margin=0.05 \
  -V center=false \
  -V slideNumber=true \
  -o "$root/views/interpretations.html"

python3 -B "$root/tools/build_views.py" tasks "$tmp/tasks.md"
python3 -B "$root/tools/build_views.py" verdict "$tmp/verdict.md"

for name in tasks verdict; do
  pandoc "$tmp/$name.md" \
    --standalone \
    --from=markdown-native_divs \
    --to=revealjs \
    --slide-level=2 \
    --css=../assets/reveal.css \
    -V revealjs-url=https://cdn.jsdelivr.net/npm/reveal.js@5.1.0 \
    -V theme=white \
    -V width=1180 \
    -V height=740 \
    -V margin=0.05 \
    -V center=false \
    -V slideNumber=true \
    -o "$root/views/$name.html"
done

prettier --write "$root/views/interpretations.html" "$root/views/tasks.html" "$root/views/verdict.html"
