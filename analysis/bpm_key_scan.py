import sys
import librosa
import numpy as np

CAMELOT_MAP = {
    "C": "8B",  "G": "9B",  "D": "10B", "A": "11B", "E": "12B",
    "B": "1B",  "F#": "2B", "C#": "3B", "G#": "4B",  "D#": "5B",
    "A#": "6B", "F": "7B",

    "Am": "8A",  "Em": "9A",  "Bm": "10A", "F#m": "11A", "C#m": "12A",
    "G#m": "1A", "D#m": "2A", "A#m": "3A",  "Fm": "4A",  "Cm": "5A",
    "Gm": "6A",  "Dm": "7A",
}

def estimate_bpm(y, sr):
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    return round(float(tempo.item()), 1)

def estimate_key(y, sr):
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    chroma_mean = np.mean(chroma, axis=1)

    keys = [
        "C", "C#", "D", "D#", "E", "F",
        "F#", "G", "G#", "A", "A#", "B"
    ]

    key_index = np.argmax(chroma_mean)
    return keys[key_index]

def analyze_track(path):
    print(f"Analyzing: {path}")

    y, sr = librosa.load(path, mono=True)
    duration = librosa.get_duration(y=y, sr=sr)

    bpm = estimate_bpm(y, sr)
    key = estimate_key(y, sr)

    print(f"Duration: {round(duration, 1)} sec")
    print(f"BPM: {bpm}")
    # print(f"Key: {key}")
    camelot = CAMELOT_MAP.get(key, "Unknown")
    print(f"Key: {key}  |  Camelot: {camelot}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bpm_key_scan.py <audiofile>")
        sys.exit(1)

    analyze_track(sys.argv[1])
