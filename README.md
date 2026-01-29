# SASHflow 🎧

**SASHflow** is a Python‑based audio analysis tool for DJs and electronic music enthusiasts.  
It analyzes audio tracks to extract **BPM**, **musical key** (with *Camelot notation*), and **estimated drop point** — helping you prepare harmonic, energy‑aware mixes.

---

## 🧠 What it Does Now

SASHflow analyzes audio files and reports:

- 🥁 **BPM** (Beat Per Minute)  
- 🎼 **Key** (musical key)  
- 🌀 **Camelot** notation (DJ‑friendly harmonic key)  
- 🔥 **First Drop** location (in seconds) — useful for mix points  
- 📊 **CSV output** for library analysis and playlist building

---

## 📦 Features

✔ BPM detection via *librosa*  
✔ Musical key and Camelot notation  
✔ First drop detection using RMS energy thresholds  
✔ Batch folder analysis  
✔ CSV export for set planning  
✔ Works on Linux/macOS/Windows

---

## ⚙️ Prerequisites

Before using SASHflow, make sure you have:

- Python **3.9+**
- FFmpeg (for audio decoding)
- Git

---

## 🛠 Installation

### Linux / macOS / WSL

```bash
sudo apt update
sudo apt install ffmpeg libsndfile1
git clone https://github.com/simplyunix/sashflow.git
cd sashflow

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
Windows (PowerShell)
git clone https://github.com/simplyunix/sashflow.git
cd sashflow

python -m venv sashflow-env
.\sashflow-env\Scripts\activate

pip install -r requirements.txt
🚀 Usage
Analyze a single file
./scripts/analyze.sh "tracks/house-405231.mp3"
Analyze an entire folder
./scripts/analyze.sh tracks/
This will produce:

analysis_results.csv
Containing:

File,Duration (s),BPM,Key,Camelot,First Drop (s)
track1.mp3,...,...,...,9B,15.5
track2.mp3,...,...,...,8B,18.0
🧾 Example Output
File,Duration (s),BPM,Key,Camelot,First Drop (s)
deep-house-..,.226.2,129.2,A,11B,15.5
house-405231.mp3,190.0,117.5,G,9B,4.0
This CSV can be imported into Excel, Rekordbox, or other DJ tools for planning harmonic and tempo‑aware sets.

🧪 Example CSV Output
After running:
./scripts/analyze.sh tracks
You’ll get a CSV file (analysis_results.csv) with contents like this:
./scripts/analyze.sh tracks
| File                           | Duration (s) | BPM   | Key | Camelot | First Drop (s) |
| ------------------------------ | ------------ | ----- | --- | ------- | -------------- |
| deep-house-12mp3-354595.mp3    | 226.2        | 129.2 | A   | 11B     | 15.5           |
| house-405231.mp3               | 190.0        | 117.5 | G   | 9B      | 4.0            |
| house-music-309375.mp3         | 136.0        | 117.5 | D   | 10B     | 8.0            |
| tech-house-3mp3-353347.mp3     | 171.6        | 123.0 | A#  | 6B      | 15.5           |
| tropical-deep-house-117020.mp3 | 237.4        | 123.0 | C   | 8B      | 15.7           |

🧹 Git Hygiene
Make sure your commits do not include:
.venv/
sashflow-env/
__pycache__/
tracks/
*.mp3
*.wav
*.flac
Recommended .gitignore entries are already included.

📈 Next Steps / Roadmap
This release focuses on analysis. Future planned upgrades include:

📍 Breakdown detection (best mix‑out zones)

📊 Energy profiling and curve plots

🎶 Auto playlist generation sorted by BPM + Camelot

🛠 CLI tool mode (sashflow analyze <path>)

🙌 Contributing
If you’d like to help:

Fork the repo

Create a feature branch

Commit your changes

Submit a pull request

📝 License
MIT License — see the LICENSE file

🙌 We now have
✅ Tracks analyzed (BPM, key, energy, drop)
✅ Smart playlist order generated
✅ Playlist successfully inside Rekordbox

📬 Author
Sasi Chand — Passionate about music, Python, and mixing flows 🌀