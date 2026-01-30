import os
import csv
from operator import itemgetter

# -----------------
# Load analyzed tracks
# -----------------
def load_tracks(csv_path="analysis_results.csv"):
    tracks = []
    with open(csv_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert numeric fields to float
            for key in ["Duration (s)", "BPM", "Energy Score",
                        "Mix In (s)", "First Drop (s)",
                        "True Drop (s)", "Mix Out (s)"]:
                if row[key] != "":
                    row[key] = float(row[key])
                else:
                    row[key] = None
            tracks.append(row)
    return tracks

# -----------------
# Camelot key helper
# -----------------
def camelot_to_num(camelot):
    if camelot[-1] in ["A", "B"]:
        return int(camelot[:-1]), camelot[-1]
    return None, None

def are_keys_compatible(key1, key2):
    num1, letter1 = camelot_to_num(key1)
    num2, letter2 = camelot_to_num(key2)
    if letter1 == letter2 and abs(num1 - num2) == 1:  # adjacent numbers same letter
        return True
    if num1 == num2 and letter1 != letter2:  # same number, A ↔ B
        return True
    return False

# -----------------
# Intelligent DJ progression
# -----------------
def score_transition(track_a, track_b):
    score = 0

    # BPM proximity
    if track_a["BPM"] and track_b["BPM"]:
        diff = abs(track_a["BPM"] - track_b["BPM"])
        score += max(0, 10 - diff)  # smaller diff = higher score

    # Harmonic compatibility
    if track_a["Camelot"] and track_b["Camelot"]:
        if are_keys_compatible(track_a["Camelot"], track_b["Camelot"]):
            score += 5

    # Energy flow
    if track_a["Energy Score"] and track_b["Energy Score"]:
        delta = track_b["Energy Score"] - track_a["Energy Score"]
        if 0 <= delta <= 1.5:  # gentle increase
            score += 3
        elif -1 <= delta < 0:  # small decrease allowed
            score += 2

    return score

def create_playlist(tracks):
    if not tracks:
        return []

    # Start with the lowest BPM track (or highest energy if you prefer)
    tracks = sorted(tracks, key=lambda t: t["BPM"])
    playlist = [tracks.pop(0)]

    while tracks:
        last_track = playlist[-1]
        # score all remaining tracks
        scored = [(score_transition(last_track, t), t) for t in tracks]
        # pick the highest scoring next track
        scored.sort(key=itemgetter(0), reverse=True)
        next_track = scored[0][1]
        playlist.append(next_track)
        tracks.remove(next_track)

    return playlist

# -----------------
# Write playlist CSV
# -----------------
def save_playlist(playlist, csv_path="playlist.csv"):
    fieldnames = ["File","Duration (s)","BPM","Key","Camelot",
                  "Energy Score","Mix In (s)","First Drop (s)",
                  "True Drop (s)","Mix Out (s)"]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for track in playlist:
            writer.writerow(track)

# -----------------
# Main
# -----------------
if __name__ == "__main__":
    tracks = load_tracks("analysis_results.csv")
    playlist = create_playlist(tracks)
    save_playlist(playlist)
    print(f"🎧 DJ-style intelligent playlist created: playlist.csv")
