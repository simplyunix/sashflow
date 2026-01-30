import os
import csv
import re

# ---------------- CONFIG ----------------
INPUT_CSV = "playlist.csv"       # from playlist_builder
TRACKS_FOLDER = "tracks"         # relative path to tracks folder
OUTPUT_M3U = "rekordbox_playlist.m3u8"

# ---------------- SANITIZE ----------------
def sanitize_filename(name):
    """Replace unsafe characters for Windows / DJ software."""
    return re.sub(r'[\\/:*?"<>|&()]', "_", name)

def sanitize_files(root_folder):
    """Sanitize all filenames in the tracks folder."""
    print(f"Scanning and sanitizing: {root_folder}\n")
    for root, _, files in os.walk(root_folder):
        for file in files:
            old_path = os.path.join(root, file)
            new_name = sanitize_filename(file)
            if new_name != file:
                new_path = os.path.join(root, new_name)
                if not os.path.exists(new_path):
                    os.rename(old_path, new_path)
                    print(f"Renamed:\n  {file}\n  → {new_name}\n")
                else:
                    print(f"Skipped (already exists): {new_name}")
    print("Done ✔\n")

# ---------------- LOAD TRACKS ----------------
def read_tracks(csv_file):
    if not os.path.isfile(csv_file):
        print(f"CSV file not found: {csv_file}")
        return []
    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

# ---------------- EXPORT M3U ----------------
def export_m3u(tracks, output_file):
    if not tracks:
        print("No tracks to export.")
        return

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for track in tracks:
            filename = sanitize_filename(track["File"])
            rel_path = os.path.join(TRACKS_FOLDER, filename).replace("\\", "/")

            # Duration fallback to -1 if not available
            duration = track.get("Duration (s)", -1)

            # Write EXTINF with track name
            f.write(f"#EXTINF:{duration},{filename}\n")

            # Cue info as comment
            cues = []
            for cue_name in ["Mix In (s)", "First Drop (s)", "True Drop (s)", "Mix Out (s)"]:
                if track.get(cue_name):
                    cues.append(f"{cue_name}: {track[cue_name]}s")
            if cues:
                f.write("#CUE: " + " | ".join(cues) + "\n")

            # Track file relative path
            f.write(rel_path + "\n\n")

    print(f"🎧 Rekordbox playlist exported: {output_file}")

# ---------------- MAIN ----------------
if __name__ == "__main__":
    # 1️⃣ Sanitize filenames
    sanitize_files(TRACKS_FOLDER)

    # 2️⃣ Load tracks from playlist CSV
    tracks = read_tracks(INPUT_CSV)
    print(f"Loaded {len(tracks)} tracks from {INPUT_CSV}")

    # 3️⃣ Export M3U playlist
    export_m3u(tracks, OUTPUT_M3U)
