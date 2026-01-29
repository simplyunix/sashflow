import csv
import os

INPUT_CSV = "playlist.csv"
TRACKS_FOLDER = "tracks"   # relative folder
OUTPUT_M3U = "rekordbox_playlist.m3u8"


def export_m3u():
    if not os.path.exists(INPUT_CSV):
        print("playlist.csv not found. Run playlist_builder.py first.")
        return

    with open(INPUT_CSV, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        tracks = list(reader)

    if not tracks:
        print("No tracks found in playlist.csv")
        return

    with open(OUTPUT_M3U, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")

        for track in tracks:
            filename = track["File"]

            # 🔥 RELATIVE PATH (this is the key fix)
            rel_path = os.path.join(TRACKS_FOLDER, filename).replace("\\", "/")

            f.write(f"#EXTINF:-1,{filename}\n")
            f.write(rel_path + "\n")

    print(f"🎧 Rekordbox playlist exported: {OUTPUT_M3U}")


if __name__ == "__main__":
    export_m3u()
