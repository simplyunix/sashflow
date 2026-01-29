✅ THE BUILD (clean rebuild in correct order)
1️⃣ Make sure tracks are ONLY here now
C:\Music\sashflow\tracks

If they are sitting directly in sashflow root, move them into a tracks folder so paths stay predictable.

2️⃣ Delete old generated files
In C:\Music\sashflow\ delete:

analysis_results.csv
playlist.csv
rekordbox_playlist.m3u8

We want zero old paths cached

3️⃣ Re-scan tracks (fresh paths)

Activate venv, then:

python analysis/bpm_key_scan.py tracks

Check inside analysis_results.csv — you should ONLY see filenames, not full paths. Good.

4️⃣ Rebuild playlist
python analysis/playlist_builder.py

5️⃣ Re-export Rekordbox playlist
python analysis/export_rekordbox.py


Now open the file and confirm it looks like this:

#EXTM3U
#EXTINF:-1,house-music-309375.mp3
C:\Music\sashflow\tracks\house-music-309375.mp3

The path MUST match exactly where the file lives on disk.

6️⃣ Import into Rekordbox
File → Import Playlist → rekordbox_playlist.m3u8
