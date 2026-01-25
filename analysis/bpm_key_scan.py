import sys
import librosa
import numpy as np

def estimate_bpm(y, sr):
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    return round(float(tempo), 1)

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
    print(f"Key: {key}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python bpm_key_scan.py <audiofile>")
        sys.exit(1)

    analyze_track(sys.argv[1])