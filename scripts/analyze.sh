#!/usr/bin/env bash
set -e

# Go to repo root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

# Activate virtual environment
if [ ! -d ".venv" ]; then
    echo "Virtual environment not found!"
    echo "Run: python3 -m venv .venv && source .venv/bin/activate"
    exit 1
fi
source .venv/bin/activate

TARGET="$1"
if [ -z "$TARGET" ]; then
    echo "Usage: ./scripts/analyze.sh <audiofile-or-folder>"
    exit 1
fi

# Remove old CSV
CSV_FILE="analysis_results.csv"
[ -f "$CSV_FILE" ] && rm "$CSV_FILE"

# Run Python analysis
python3 analysis/bpm_key_scan.py "$TARGET"

echo "----------------------------------------"
echo "CSV report saved to: $CSV_FILE"

deactivate