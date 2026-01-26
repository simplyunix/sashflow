# SASHflow 🎧

**SASHflow** is a Python-based audio analysis tool for DJs and electronic music producers.  
It analyzes tracks to extract **BPM**, **musical key**, and (planned) **drop detection**, helping you prepare smooth mixes for house, trance, and dance anthems.

---

## ✨ Features

- 🎵 BPM detection  
- 🎼 Musical key detection  
- 🔥 Drop detection *(planned)*  
- 🐍 Lightweight, Python-first workflow  
- 🧑‍💻 Cross-platform (Linux, macOS, Windows)

---

## 📦 Project Structure

```text
sashflow/
├── analysis/           # Audio analysis modules
│   └── bpm_key_scan.py
├── scripts/            # Dev / helper scripts
├── tracks/             # Example tracks (optional, not tracked)
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
🔧 Prerequisites
Python 3.9+

Git

FFmpeg (for audio decoding)

🚀 Installation
🐧 Linux (Ubuntu 24.04 / WSL / macOS)
# Install system dependencies
sudo apt update
sudo apt install ffmpeg libsndfile1

# Clone the repository
git clone https://github.com/simplyunix/sashflow.git
cd sashflow

# Create & activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install Python dependencies
pip install -r requirements.txt

# Run the analyzer
python analysis/bpm_key_scan.py tracks/house-405231.mp3
🪟 Windows
# Clone the repository
git clone https://github.com/simplyunix/sashflow.git
cd sashflow

# Create & activate virtual environment
python -m venv sashflow-env
.\sashflow-env\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the analyzer
python analysis\bpm_key_scan.py "tracks\house-405231.mp3"
🧪 Output
The analyzer returns:

Track duration (seconds)

Estimated BPM

Musical key

Example:

Duration: 190.0 sec
BPM: 117.5
Key: G

### Analyze a folder

Analyze all supported audio files in a directory:

```bash
scripts/analyze.sh tracks/

🧼 Git Hygiene (Important)
🚫 Never commit virtual environments or audio libraries.

Quick Start / Cleanup

Activate the virtual environment:

Linux/macOS (.venv)

source .venv/bin/activate
Windows (sashflow-env)

.\sashflow-env\Scripts\activate
Run the analyzer:

python analysis/bpm_key_scan.py <path-to-audio-file>
Example:

python analysis/bpm_key_scan.py tracks/house-405231.mp3
Deactivate the virtual environment when done:

Linux/macOS / Windows

deactivate
This returns your shell to the system Python, keeping your environment clean for the next session.

✅ Tracked Files
Source code (analysis/)

requirements.txt

README.md

Small example tracks (optional)

❌ Ignored
.venv/
sashflow-env/
tracks/
__pycache__/
*.pyc
.DS_Store
Thumbs.db
🛣 Roadmap
Drop detection using energy + spectral flux

Beat-grid alignment

Track-to-track mix suggestions

CLI tool (sashflow analyze track.mp3)

Rekordbox / Serato export (long-term)

🤝 Contributing
Fork the repo

Create a feature branch

Commit clean changes

Open a Pull Request

📄 License
MIT License — see LICENSE file


---

This version is:

- ✅ Fully cross-platform  
- ✅ Properly formatted for GitHub markdown  
- ✅ Includes virtual environment instructions and cleanup  
- ✅ Safe Git hygiene advice for `.venv` and `sashflow-env`  
