import os
import csv
import librosa
import numpy as np

# Camelot key mapping
CAMELOT_MAP = {
    "C": "8B",  "G": "9B",  "D": "10B", "A": "11B", "E": "12B",
    "B": "1B",  "F#": "2B", "C#": "3B", "G#": "4B",  "D#": "5B",
    "A#": "6B", "F": "7B",

    "Am": "8A",  "Em": "9A",  "Bm": "10A", "F#m": "11A", "C#m": "12A",
    "G#m": "1A", "D#m": "2A", "A#m": "3A",  "Fm": "4A",  "Cm": "5A",
    "Gm": "6A",  "Dm": "7A",
}

# Estimate BPM
def estimate_bpm(y, sr):
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    return round(float(tempo.item()), 1)

# Estimate musical key
def estimate_key(y, sr):
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    chroma_mean = np.mean(chroma, axis=1)

    keys = ["C", "C#", "D", "D#", "E", "F", 
            "F#", "G", "G#", "A", "A#", "B"]

    key_index = np.argmax(chroma_mean)
    return keys[key_index]

# Analyze a single track
def analyze_track(path):
    print(f"Analyzing: {path}")
    y, sr = librosa.load(path, mono=True)
    duration = librosa.get_duration(y=y, sr=sr)
    bpm = estimate_bpm(y, sr)
    key = estimate_key(y, sr)
    camelot = CAMELOT_MAP.get(key, "Unknown")

    print(f"Duration: {round(duration,1)} sec | BPM: {bpm} | Key: {key} | Camelot: {camelot}")

    # Return as dict for CSV-friendly integration
    return {
        "File": os.path.basename(path),
        "Duration (s)": round(duration,1),
        "BPM": bpm,
        "Key": key,
        "Camelot": camelot
    }

# Append single track results to CSV
def append_to_csv(results, csv_path="analysis_results.csv"):
    file_exists = os.path.isfile(csv_path)

    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["File","Duration (s)","BPM","Key","Camelot"])
        if not file_exists:
            writer.writeheader()
        writer.writerow(results)

# Analyze single file or folder
def analyze_path(input_path, csv_path="analysis_results.csv"):
    if os.path.isfile(input_path):
        results = analyze_track(input_path)
        append_to_csv(results, csv_path)

    elif os.path.isdir(input_path):
        for file in sorted(os.listdir(input_path)):
            if file.lower().endswith((".mp3", ".wav", ".flac")):
                full_path = os.path.join(input_path, file)
                print("-" * 40)
                results = analyze_track(full_path)
                append_to_csv(results, csv_path)
    else:
        print("Invalid path:", input_path)

# CLI entry
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python bpm_key_scan.py <audiofile_or_folder>")
        sys.exit(1)
    analyze_path(sys.argv[1])
