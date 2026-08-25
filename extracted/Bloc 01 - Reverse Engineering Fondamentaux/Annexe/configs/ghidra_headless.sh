#!/bin/bash
# Analyse headless Ghidra (batch)
# Usage: ./ghidra_headless.sh <binary> [<output_dir>]
set -euo pipefail

BINARY="${1:-}"
OUT="${2:-/tmp/ghidra_out}"
GHIDRA="${GHIDRA_HOME:-/opt/ghidra}"

[ -z "$BINARY" ] && { echo "Usage: $0 <binary>"; exit 1; }
[ ! -x "$GHIDRA/support/analyzeHeadless" ] && {
    echo "[-] Ghidra introuvable à $GHIDRA"
    echo "    Téléchargez-le : https://github.com/NationalSecurityAgency/ghidra/releases"
    exit 1
}

mkdir -p "$OUT"
PROJECT="cybersup_tmp"

"$GHIDRA/support/analyzeHeadless" "$OUT" "$PROJECT" \
    -import "$BINARY" \
    -postScript ExtractDisassembly.java \
    -deleteProject
