from analysis.bpm_key_scan import analyze_track
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python main.py <audio_file>")
        sys.exit(1)

    analyze_track(sys.argv[1])
