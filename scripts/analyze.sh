#!/usr/bin/env bash

# -----------------------------------------
# SASHflow analyze script
# Usage: ./analyze.sh path/to/track.mp3
# -----------------------------------------

# Fail on any error
set -e

# Check argument
if [ -z "$1" ]; then
  echo "Usage: $0 <path-to-audio-file>"
  exit 1
fi

TRACK="$1"

# Activate virtual environment (Unix/macOS)
if [ -f ../.venv/bin/activate ]; then
    source ../.venv/bin/activate
else
    echo "Virtual environment not found! Please run:"
    echo "  python3 -m venv ../.venv"
    echo "  source ../.venv/bin/activate"
    exit 1
fi

# Run the analyzer
python3 ../analysis/bpm_key_scan.py "$TRACK"
