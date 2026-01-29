import os
import re

ROOT_FOLDER = r"C:\Music\sashflow\tracks"   # 👈 change if your tracks folder is elsewhere

def sanitize_filename(name):
    # Replace unsafe characters with underscore
    return re.sub(r'[\\/:*?"<>|&()]', "_", name)

def sanitize_files(root_folder):
    print(f"Scanning: {root_folder}\n")

    for root, _, files in os.walk(root_folder):
        for file in files:
            old_path = os.path.join(root, file)
            new_name = sanitize_filename(file)

            if new_name != file:
                new_path = os.path.join(root, new_name)

                # Avoid overwriting
                if not os.path.exists(new_path):
                    os.rename(old_path, new_path)
                    print(f"Renamed:\n  {file}\n  → {new_name}\n")
                else:
                    print(f"Skipped (already exists): {new_name}")

    print("Done ✔")

if __name__ == "__main__":
    sanitize_files(ROOT_FOLDER)
