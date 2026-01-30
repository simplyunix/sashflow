import os
import csv
import librosa
import numpy as np

# --------------------------------------------------
# Camelot Key Mapping
# --------------------------------------------------
CAMELOT_MAP = {
    "C": "8B", "G": "9B", "D": "10B", "A": "11B", "E": "12B",
    "B": "1B", "F#": "2B", "C#": "3B", "G#": "4B", "D#": "5B",
    "A#": "6B", "F": "7B",

    "Am": "8A", "Em": "9A", "Bm": "10A", "F#m": "11A", "C#m": "12A",
    "G#m": "1A", "D#m": "2A", "A#m": "3A", "Fm": "4A", "Cm": "5A",
    "Gm": "6A", "Dm": "7A",
}

# --------------------------------------------------
# BPM & KEY
# --------------------------------------------------
def estimate_bpm(y, sr):
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    return round(float(tempo.item()), 1)

def estimate_key(y, sr):
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    chroma_mean = np.mean(chroma, axis=1)
    keys = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]
    return keys[int(np.argmax(chroma_mean))]

# --------------------------------------------------
# ENERGY SCORE
# --------------------------------------------------
def calculate_energy_score(y):
    rms = librosa.feature.rms(y=y)[0]
    avg_energy = float(np.mean(rms))
    peak_energy = float(np.max(rms))
    return round(peak_energy / avg_energy, 2) if avg_energy > 0 else 0

# --------------------------------------------------
# MIX IN / OUT DETECTION
# --------------------------------------------------
def detect_mix_points(y, sr):
    hop_length = 512
    rms = librosa.feature.rms(y=y, hop_length=hop_length)[0]
    times = librosa.frames_to_time(np.arange(len(rms)), sr=sr, hop_length=hop_length)

    avg_energy = np.mean(rms)
    intro_threshold = avg_energy * 0.8
    outro_threshold = avg_energy * 0.75
    high_threshold = avg_energy * 1.4

    # Mix In: first time energy rises above intro threshold
    mix_in_candidates = times[rms > intro_threshold]
    mix_in = mix_in_candidates[0] if len(mix_in_candidates) else 0.0

    # Energy Drop: first high-energy spike after intro
    drop_candidates = times[rms > high_threshold]
    energy_drop = drop_candidates[0] if len(drop_candidates) else None

    # Mix Out: last time energy is above outro threshold
    strong_sections = times[rms > outro_threshold]
    mix_out = strong_sections[-1] if len(strong_sections) else None

    return round(float(mix_in),1), \
           round(float(energy_drop),1) if energy_drop else None, \
           round(float(mix_out),1) if mix_out else None

# --------------------------------------------------
# TRUE MUSICAL DROP (ONSET SPIKE)
# --------------------------------------------------
def detect_true_drop(y, sr):
    onset_env = librosa.onset.onset_strength(y=y, sr=sr)
    times = librosa.frames_to_time(np.arange(len(onset_env)), sr=sr)
    threshold = np.mean(onset_env) * 2.0
    strong = [t for t in times[onset_env > threshold] if t > 5]  # ignore first 5s
    return round(float(strong[0]),1) if strong else None

# --------------------------------------------------
# MAIN TRACK ANALYSIS
# --------------------------------------------------
def analyze_track(path):
    print(f"Analyzing: {path}")

    y, sr = librosa.load(path, mono=True)
    duration = round(librosa.get_duration(y=y, sr=sr),1)

    bpm = estimate_bpm(y, sr)
    key = estimate_key(y, sr)
    camelot = CAMELOT_MAP.get(key, "Unknown")
    energy_score = calculate_energy_score(y)

    mix_in, energy_drop, mix_out = detect_mix_points(y, sr)
    true_drop = detect_true_drop(y, sr)

    print(f"Duration: {duration} sec")
    print(f"BPM: {bpm}")
    print(f"Key: {key} | Camelot: {camelot}")
    print(f"Energy Score: {energy_score}")
    print(f"Mix In Around: {mix_in} sec")
    if true_drop:
        print(f"True Drop At: {true_drop} sec")
    elif energy_drop:
        print(f"Energy Drop Around: {energy_drop} sec")
    if mix_out:
        print(f"Mix Out Around: {mix_out} sec")

    return {
        "File": os.path.basename(path),
        "Duration (s)": duration,
        "BPM": bpm,
        "Key": key,
        "Camelot": camelot,
        "Energy Score": energy_score,
        "Mix In (s)": mix_in,
        "First Drop (s)": energy_drop if energy_drop else "",
        "True Drop (s)": true_drop if true_drop else "",
        "Mix Out (s)": mix_out if mix_out else ""
    }

# --------------------------------------------------
# CSV WRITER
# --------------------------------------------------
def append_to_csv(results, csv_path="analysis_results.csv"):
    fieldnames = [
        "File","Duration (s)","BPM","Key","Camelot",
        "Energy Score","Mix In (s)","First Drop (s)",
        "True Drop (s)","Mix Out (s)"
    ]
    write_header = not os.path.isfile(csv_path) or os.path.getsize(csv_path) == 0
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if write_header:
            writer.writeheader()
        writer.writerow(results)

# --------------------------------------------------
# RUNNER
# --------------------------------------------------
def analyze_path(input_path, csv_path="analysis_results.csv"):
    if os.path.isfile(input_path):
        append_to_csv(analyze_track(input_path), csv_path)
    elif os.path.isdir(input_path):
        for root, _, files in os.walk(input_path):
            for file in sorted(files):
                if file.lower().endswith((".mp3",".wav",".flac")):
                    print("-"*40)
                    append_to_csv(analyze_track(os.path.join(root,file)), csv_path)
    else:
        print("Invalid path:", input_path)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python bpm_key_scan.py <audiofile_or_folder>")
        sys.exit(1)
    analyze_path(sys.argv[1])
