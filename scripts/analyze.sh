#!/usr/bin/env bash

set -e

# Go to repo root (script may be run from anywhere)
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

cd "$REPO_ROOT"

# Check virtual environment
if [ ! -d ".venv" ]; then
  echo "Virtual environment not found! Please run:"
  echo "  python3 -m venv .venv"
  echo "  source .venv/bin/activate"
  exit 1
fi

source .venv/bin/activate

TARGET="$1"

if [ -z "$TARGET" ]; then
  echo "Usage: ./scripts/analyze.sh <audio-file-or-folder>"
  exit 1
fi

OUTPUT_CSV="analysis_results.csv"

# If folder, prepare CSV
if [ -d "$TARGET" ]; then
  echo "filename,duration_sec,bpm,key" > "$OUTPUT_CSV"
fi

analyze_file () {
  FILE="$1"
  echo "----------------------------------------"
  echo "Analyzing: $FILE"

  RESULT=$(python3 analysis/bpm_key_scan.py "$FILE")

  echo "$RESULT"

  if [ -f "$OUTPUT_CSV" ]; then
    DURATION=$(echo "$RESULT" | grep "Duration" | awk '{print $2}')
    BPM=$(echo "$RESULT" | grep "BPM" | awk '{print $2}')
    KEY=$(echo "$RESULT" | grep "Key" | awk '{print $2}')
    BASENAME=$(basename "$FILE")

    echo "$BASENAME,$DURATION,$BPM,$KEY" >> "$OUTPUT_CSV"
  fi
}

if [ -f "$TARGET" ]; then
  analyze_file "$TARGET"
elif [ -d "$TARGET" ]; then
  for FILE in "$TARGET"/*.mp3; do
    analyze_file "$FILE"
  done
  echo "----------------------------------------"
  echo "CSV report saved to: $OUTPUT_CSV"
else
  echo "Invalid path: $TARGET"
  exit 1
fi

deactivate
