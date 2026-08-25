#!/bin/bash
# Scanne un fichier avec toutes les règles YARA du kit
set -euo pipefail
TARGET="${1:-}"
RULES_DIR="$(dirname "$0")/../yara"
[ -z "$TARGET" ] && { echo "Usage: $0 <file>"; exit 1; }

echo "[+] Scanning $TARGET with rules from $RULES_DIR"
for r in "$RULES_DIR"/*.yar; do
    echo "--- $r ---"
    yara -w "$r" "$TARGET" || true
done
