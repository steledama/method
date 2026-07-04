#!/usr/bin/env bash
set -euo pipefail

root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

python3 -B "$root/o3/build_system_image.py"
prettier --write "$root/presentation/index.html"
