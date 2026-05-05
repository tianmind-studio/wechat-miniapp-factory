#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
VALIDATOR="${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py"

if [ ! -f "$VALIDATOR" ]; then
  find "$ROOT/skills" -mindepth 1 -maxdepth 1 -type d | while read -r dir; do
    test -f "$dir/SKILL.md" || { echo "missing SKILL.md: $dir" >&2; exit 1; }
    echo "found skill: $(basename "$dir")"
  done
  exit 0
fi

find "$ROOT/skills" -mindepth 1 -maxdepth 1 -type d | sort | while read -r dir; do
  echo "validating: $(basename "$dir")"
  python3 "$VALIDATOR" "$dir"
done
