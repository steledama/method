#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

python3 -B "$root/tools/build_system_image.py"
prettier --write "$root/index.html"
