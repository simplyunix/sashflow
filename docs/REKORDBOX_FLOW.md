🎧 Full SashFlow → Rekordbox Workflow

1️⃣ Analyze all tracks

python analysis/bpm_key_scan.py tracks


✔ Detects BPM, Key, Camelot, Energy
✔ Finds Mix In / Mix Out / Drop points
✔ Writes everything to analysis_results.csv

2️⃣ Build the DJ playlist

python analysis/playlist_builder.py


✔ Sorts tracks using BPM + Camelot + Energy flow
✔ Outputs playlist.csv (this is your set order)

3️⃣ Export Rekordbox playlist with cues

python export_rekordbox_cues.py


✔ Sanitizes filenames in /tracks
✔ Reads playlist.csv
✔ Creates rekordbox_playlist.m3u8
✔ Embeds DJ cue times as comments
✔ Uses relative paths so Rekordbox can find the files

🔥 Then in Rekordbox

File → Import Playlist → Import from File → select rekordbox_playlist.m3u8

Your tracks should appear in DJ set order, ready for analysis and cue placement.