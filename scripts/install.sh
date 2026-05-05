#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TARGET="${CODEX_HOME:-$HOME/.codex}/skills"

mkdir -p "$TARGET"

if [ "$#" -eq 0 ]; then
  mapfile -t skills < <(find "$ROOT/skills" -mindepth 1 -maxdepth 1 -type d -exec basename {} \; | sort)
else
  skills=("$@")
fi

for skill in "${skills[@]}"; do
  src="$ROOT/skills/$skill"
  dst="$TARGET/$skill"
  if [ ! -f "$src/SKILL.md" ]; then
    echo "skip: $skill does not look like a skill folder" >&2
    continue
  fi
  mkdir -p "$dst"
  rsync -a --delete --exclude '.git' --exclude '.DS_Store' --exclude '._*' "$src/" "$dst/"
  echo "installed: $skill -> $dst"
done
