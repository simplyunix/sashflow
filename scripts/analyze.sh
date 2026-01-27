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
OUTPUT_CSV="analysis_results.csv"

if [ -z "$TARGET" ]; then
  echo "Usage: ./scripts/analyze.sh <audio-file-or-folder>"
  exit 1
fi

# Overwrite CSV with headers if folder or new run
echo "File,Duration (s),BPM,Key,Camelot" > "$OUTPUT_CSV"

analyze_file () {
  FILE="$1"
  echo "----------------------------------------"
  echo "Analyzing: $FILE"

  # Call Python analysis
  python3 - <<EOF
from analysis.bpm_key_scan import analyze_track, CAMELOT_MAP
import os, csv

track_data = analyze_track("$FILE")
csv_file = "$OUTPUT_CSV"

# Append to CSV
with open(csv_file, "a", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["File","Duration (s)","BPM","Key","Camelot"])
    writer.writerow(track_data)
EOF
}

if [ -f "$TARGET" ]; then
  analyze_file "$TARGET"
elif [ -d "$TARGET" ]; then
  # Loop over common audio formats
  for FILE in "$TARGET"/*.{mp3,wav,flac}; do
    [ -e "$FILE" ] || continue
    analyze_file "$FILE"
  done
  echo "----------------------------------------"
  echo "CSV report saved to: $OUTPUT_CSV"
else
  echo "Invalid path: $TARGET"
  exit 1
fi

deactivate
