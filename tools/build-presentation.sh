#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

pandoc "$root/interpretations/metodo-in-sintesi.md" \
  --standalone \
  --from=markdown-native_divs \
  --to=revealjs \
  --slide-level=2 \
  --css=reveal.css \
  -V revealjs-url=https://cdn.jsdelivr.net/npm/reveal.js@5.1.0 \
  -V theme=white \
  -V width=1180 \
  -V height=740 \
  -V margin=0.05 \
  -V center=false \
  -V slideNumber=true \
  -o "$root/interpretations/index.html"

prettier --write "$root/interpretations/index.html"
