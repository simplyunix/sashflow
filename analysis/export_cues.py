import csv
import os

INPUT_CSV = "analysis_results.csv"
OUTPUT_CSV = "dj_cues.csv"

CUE_LABELS = [
    ("Mix In (s)", "MIX IN"),
    ("True Drop (s)", "DROP"),
    ("First Drop (s)", "ENERGY"),
    ("Mix Out (s)", "MIX OUT"),
]

def format_time(seconds):
    """Convert seconds to mm:ss.mmm format used by DJ software"""
    seconds = float(seconds)
    mins = int(seconds // 60)
    secs = seconds % 60
    return f"{mins:02d}:{secs:06.3f}"

def export_cues():
    if not os.path.isfile(INPUT_CSV):
        print("analysis_results.csv not found. Run analysis first.")
        return

    with open(INPUT_CSV, newline="", encoding="utf-8") as infile, \
         open(OUTPUT_CSV, "w", newline="", encoding="utf-8") as outfile:

        reader = csv.DictReader(infile)
        fieldnames = ["File", "Cue Name", "Time"]
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            file_name = row["File"]

            for column, label in CUE_LABELS:
                value = row.get(column, "").strip()
                if value:
                    try:
                        time_str = format_time(value)
                        writer.writerow({
                            "File": file_name,
                            "Cue Name": label,
                            "Time": time_str
                        })
                    except ValueError:
                        continue

    print(f"🎧 Cue file created: {OUTPUT_CSV}")

if __name__ == "__main__":
    export_cues()
