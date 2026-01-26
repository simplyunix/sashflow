# SASHflow 🎧

**SASHflow** is a Python-based audio analysis tool for DJs and electronic music producers.  
It analyzes tracks to extract **BPM**, **musical key**, and (planned) **drop detection** to help prepare smooth mixes for house, trance, and dance anthems.

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

FFmpeg (audio decoding backend)

🚀 Installation
🐧 Linux (Ubuntu 24.04 / macOS / WSL)
Install system dependencies:

sudo apt update
sudo apt install ffmpeg libsndfile1
Clone the repo:

git clone https://github.com/simplyunix/sashflow.git
cd sashflow
Create & activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate
Install Python dependencies:

pip install -r requirements.txt
Run the analyzer:

python analysis/bpm_key_scan.py tracks/house-405231.mp3
🪟 Windows
Clone the repo:

git clone https://github.com/simplyunix/sashflow.git
cd sashflow
Create & activate a virtual environment:

python -m venv sashflow-env
.\sashflow-env\Scripts\activate
Install dependencies:

pip install -r requirements.txt
Run the analyzer:

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
🧼 Git Hygiene (Important)
🚫 Never commit virtual environments or audio libraries

Tracked:

Source code

requirements.txt

README.md

Ignored:

.venv/

sashflow-env/

tracks/

__pycache__/

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
MIT License — see LICENSE


---
