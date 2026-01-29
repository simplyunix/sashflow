import csv
import os

# Input CSV file (analysis results)
INPUT_CSV = "analysis_results.csv"
# Output M3U8 playlist
OUTPUT_PLAYLIST = "dj_cues.m3u8"

def read_tracks(csv_file):
    tracks = []
    with open(csv_file, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            tracks.append(row)
    return tracks

def camelot_to_number(camelot):
    """
    Convert Camelot key like '8B' to numeric for reference if needed.
    """
    try:
        return int(camelot[:-1])
    except:
        return None

def write_m3u(tracks, output_file):
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("#EXTM3U\n")
        for track in tracks:
            duration = track.get("Duration (s)", "")
            filename = track.get("File", "")
            first_drop = track.get("First Drop (s)", "")
            key = track.get("Key", "")
            camelot = track.get("Camelot", "")
            energy = track.get("Energy Score", "")

            # EXTINF line (duration, track name)
            f.write(f"#EXTINF:{duration},{filename}\n")
            
            # Add cue info as comment
            if first_drop != "":
                f.write(f"#CUE:{first_drop} sec | Key: {key} | Camelot: {camelot} | Energy: {energy}\n")
            
            # Track file path
            f.write(f"{filename}\n\n")

    print(f"🎧 Playlist with cue info created: {output_file}")

if __name__ == "__main__":
    if not os.path.isfile(INPUT_CSV):
        print(f"CSV file not found: {INPUT_CSV}")
    else:
        tracks = read_tracks(INPUT_CSV)
        print(f"Loaded {len(tracks)} tracks")
        write_m3u(tracks, OUTPUT_PLAYLIST)
