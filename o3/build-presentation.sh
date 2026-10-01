#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

# I percorsi dei plugin di reveal.js li scrive il template di pandoc, non noi:
# fino alla 3.11 sono quelli della serie 5 (plugin/notes/notes.js), dalla 3.12
# quelli della 6 (dist/plugin/notes.js). Un URL che non corrisponde lascia le
# slide bianche senza errori, quindi la versione si deriva da pandoc.
pandoc_version="$(pandoc --version | head -n 1 | awk '{print $2}')"
IFS=. read -r pandoc_major pandoc_minor _ <<<"$pandoc_version"
if [[ ! "$pandoc_major" =~ ^[0-9]+$ || ! "$pandoc_minor" =~ ^[0-9]+$ ]]; then
  echo "build-presentation: versione di pandoc non riconosciuta: '$pandoc_version'" >&2
  exit 1
fi
if ((pandoc_major > 3 || (pandoc_major == 3 && pandoc_minor >= 12))); then
  revealjs_url=https://cdn.jsdelivr.net/npm/reveal.js@6.0.2
else
  revealjs_url=https://cdn.jsdelivr.net/npm/reveal.js@5.1.0
fi

pandoc "$root/i2/metodo-in-sintesi.md" \
  --standalone \
  --from=markdown-native_divs \
  --to=revealjs \
  --slide-level=2 \
  --css=assets/interpretations.css \
  -V revealjs-url="$revealjs_url" \
  -V theme=white \
  -V width=1180 \
  -V height=740 \
  -V margin=0.05 \
  -V center=false \
  -V slideNumber=true \
  -o "$root/presentation/interpretations.html"

python3 -B "$root/o3/build_views.py" tasks "$tmp/tasks.md"
python3 -B "$root/o3/build_views.py" verdict "$tmp/verdict.md"

for name in tasks verdict; do
  pandoc "$tmp/$name.md" \
    --standalone \
    --from=markdown-native_divs \
    --to=revealjs \
    --slide-level=2 \
    --css=assets/interpretations.css \
    -V revealjs-url="$revealjs_url" \
    -V theme=white \
    -V width=1180 \
    -V height=740 \
    -V margin=0.05 \
    -V center=false \
    -V slideNumber=true \
    -o "$root/presentation/$name.html"
done

python3 -B "$root/o3/build_lists.py" prescriptions "$root/presentation/prescriptions.html"
python3 -B "$root/o3/build_lists.py" perceptions "$root/presentation/perceptions.html"

prettier --write "$root/presentation/interpretations.html" "$root/presentation/tasks.html" \
  "$root/presentation/verdict.html" "$root/presentation/prescriptions.html" \
  "$root/presentation/perceptions.html"
