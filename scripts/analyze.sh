#!/usr/bin/env bash
set -e

# Always run from repo root
REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

# Ensure virtual environment is active
if [[ -z "$VIRTUAL_ENV" ]]; then
  if [[ -d ".venv" ]]; then
    source .venv/bin/activate
  else
    echo "Virtual environment not found!"
    echo "Run:"
    echo "  python3 -m venv .venv"
    echo "  source .venv/bin/activate"
    exit 1
  fi
fi

TARGET="$1"

if [[ -z "$TARGET" ]]; then
  echo "Usage:"
  echo "  scripts/analyze.sh <audio-file | folder>"
  exit 1
fi

# If single file
if [[ -f "$TARGET" ]]; then
  python3 analysis/bpm_key_scan.py "$TARGET"
  exit 0
fi

# If directory
if [[ -d "$TARGET" ]]; then
  shopt -s nullglob
  FILES=("$TARGET"/*.mp3 "$TARGET"/*.wav "$TARGET"/*.flac)

  if [[ ${#FILES[@]} -eq 0 ]]; then
    echo "No audio files found in $TARGET"
    exit 0
  fi

  for file in "${FILES[@]}"; do
    echo "----------------------------------------"
    python3 analysis/bpm_key_scan.py "$file"
  done

  exit 0
fi

echo "Error: '$TARGET' is not a file or directory"
exit 1
