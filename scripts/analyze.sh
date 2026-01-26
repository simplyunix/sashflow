#!/usr/bin/env bash
# SASHflow: Run analysis on an audio track
# Usage: ./analyze.sh <path-to-audio-file>

# Check for argument
if [ -z "$1" ]; then
    echo "Usage: $0 <path-to-audio-file>"
    exit 1
fi

TRACK="$1"

# Check if virtual environment is activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Warning: No virtual environment activated."
    echo "Please activate your venv, e.g.:"
    echo "  source .venv/bin/activate  (Linux/macOS)"
    echo "  .\\sashflow-env\\Scripts\\activate  (Windows)"
fi

# Run the analyzer using the active Python
python3 analysis/bpm_key_scan.py "$TRACK"
