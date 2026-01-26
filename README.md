# SASHflow

SASHflow is a Python tool for DJs to analyze audio tracks and prepare mixes.  
It can detect **BPM**, **musical key**, and later support **drop detection** for house, trance, and dance anthems.

---

## Features

- BPM detection  
- Key detection  
- Drop detection (planned)  
- Lightweight, Python-based workflow  

---

## Prerequisites

- Python 3.9 or higher  
- Git  
- FFmpeg (for audio decoding)  

---

## Installation

### Windows

1. **Clone the repository**

```powershell
git clone https://github.com/simplyunix/sashflow.git
cd sashflow

2. Create a virtual environment

```powershell
python -m venv sashflow-env
.\sashflow-env\Scripts\activate

3. Install Python dependencies

```powershell
pip install -r requirements.txt

4. Run the analyser

```powershell
python analysis\bpm_key_scan.py "tracks\house-405231.mp3"

Linux (Ubuntu 24.04 / WSL / Mac)

Install system dependencies

sudo apt update
sudo apt install ffmpeg libsndfile1


Create a virtual environment

python3 -m venv .venv
source .venv/bin/activate


Install Python dependencies

pip install -r requirements.txt


Run the analyzer

python analysis/bpm_key_scan.py tracks/house-405231.mp3

Git Hygiene

Do not commit your virtual environment

Windows: sashflow-env/

Linux: .venv/

Recommended .gitignore entries:

# Python
*.pyc
__pycache__/

# Virtual environments
sashflow-env/
.venv/

# OS files
.DS_Store
Thumbs.db


Commit only:

Source code (analysis/)

requirements.txt

README.md

Small example tracks (optional)

Usage
python analysis/bpm_key_scan.py <path-to-mp3>


Returns: Duration, BPM, Key

Works cross-platform with proper dependencies installed

Contribution

Fork the repo

Create a feature branch

Submit a pull request

License

MIT License – see LICENSE file
