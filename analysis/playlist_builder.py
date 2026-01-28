import csv

INPUT_CSV = "analysis_results.csv"
OUTPUT_CSV = "playlist.csv"

def camelot_parts(code):
    num = int(code[:-1])
    letter = code[-1]
    return num, letter

def camelot_distance(c1, c2):
    n1, l1 = camelot_parts(c1)
    n2, l2 = camelot_parts(c2)

    num_diff = min(abs(n1 - n2), 12 - abs(n1 - n2))  # wrap-around wheel
    letter_diff = 0 if l1 == l2 else 1
    return num_diff + letter_diff

tracks = []
with open(INPUT_CSV, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        row["BPM"] = float(row["BPM"])
        row["Energy Score"] = float(row["Energy Score"])
        tracks.append(row)

print(f"Loaded {len(tracks)} tracks")

# Start with lowest BPM & energy (warm-up)
tracks.sort(key=lambda x: (x["BPM"], x["Energy Score"]))
playlist = [tracks.pop(0)]

# Build intelligent flow
while tracks:
    last = playlist[-1]
    next_track = min(
        tracks,
        key=lambda x: (
            abs(x["BPM"] - last["BPM"]),              # tempo closeness
            camelot_distance(x["Camelot"], last["Camelot"]),  # harmonic closeness
            abs(x["Energy Score"] - last["Energy Score"])     # energy smoothness
        )
    )
    playlist.append(next_track)
    tracks.remove(next_track)

with open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=playlist[0].keys())
    writer.writeheader()
    writer.writerows(playlist)

print("🎧 Harmonic energy-flow playlist created:", OUTPUT_CSV)
