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

# Detect energy for drop points
def detect_energy_sections(y, sr):
    hop_length = 512
    rms = librosa.feature.rms(y=y, hop_length=hop_length)[0]
    times = librosa.frames_to_time(range(len(rms)), sr=sr, hop_length=hop_length)

    avg_energy = np.mean(rms)
    low_threshold = avg_energy * 0.6
    high_threshold = avg_energy * 1.4

    low_energy_times = times[rms < low_threshold]
    high_energy_times = times[rms > high_threshold]

    return low_energy_times, high_energy_times

def detect_first_drop(high_energy_times):
    if len(high_energy_times) == 0:
        return None
    return round(float(high_energy_times[0]), 1)

# Analyze a single track
def analyze_track(path):
    print(f"Analyzing: {path}")

    y, sr = librosa.load(path, mono=True)
    duration = librosa.get_duration(y=y, sr=sr)

    bpm = estimate_bpm(y, sr)
    key = estimate_key(y, sr)
    camelot = CAMELOT_MAP.get(key, "Unknown")

    low_energy, high_energy = detect_energy_sections(y, sr)
    first_drop = detect_first_drop(high_energy)

    print(f"Duration: {round(duration,1)} sec")
    print(f"BPM: {bpm}")
    print(f"Key: {key}  |  Camelot: {camelot}")
    if first_drop is not None:
        print(f"First Drop Around: {first_drop} sec")

    return {
        "File": os.path.basename(path),
        "Duration (s)": round(duration,1),
        "BPM": bpm,
        "Key": key,
        "Camelot": camelot,
        "First Drop (s)": first_drop if first_drop is not None else ""
    }

# Append results to CSV
def append_to_csv(results, csv_path="analysis_results.csv"):
    fieldnames = ["File","Duration (s)","BPM","Key","Camelot","First Drop (s)"]
    write_header = not os.path.isfile(csv_path) or os.path.getsize(csv_path) == 0

    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerow(results)

# Analyze file or folder (with subfolders)
def analyze_path(input_path, csv_path="analysis_results.csv"):
    if os.path.isfile(input_path):
        results = analyze_track(input_path)
        append_to_csv(results, csv_path)
    elif os.path.isdir(input_path):
        for root, _, files in os.walk(input_path):
            for file in sorted(files):
                if file.lower().endswith((".mp3",".wav",".flac")):
                    full_path = os.path.join(root, file)
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