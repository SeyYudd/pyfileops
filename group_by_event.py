import os
import shutil
from datetime import datetime

# input user
source_dir = input("Masukkan folder sumber: ").strip('"')
target_dir = input("Masukkan folder tujuan: ").strip('"')
mode = input("Group by (year/month/day): ").lower()

extensions = (".jpg", ".jpeg", ".png", ".mp4", ".mkv")

if not os.path.exists(source_dir):
    print("❌ Folder sumber tidak ditemukan!")
    exit()

os.makedirs(target_dir, exist_ok=True)

def get_date(file_path):
    # pakai last modified time
    timestamp = os.path.getmtime(file_path)
    return datetime.fromtimestamp(timestamp)

moved = 0

for root, dirs, files in os.walk(source_dir):
    if target_dir in root:
        continue

    for file in files:
        if file.lower().endswith(extensions):
            source_path = os.path.join(root, file)

            file_date = get_date(source_path)

            if mode == "year":
                folder_name = file_date.strftime("%Y")
            elif mode == "month":
                folder_name = file_date.strftime("%Y-%m")
            elif mode == "day":
                folder_name = file_date.strftime("%Y-%m-%d")
            else:
                print("❌ Mode tidak valid!")
                exit()

            dest_folder = os.path.join(target_dir, folder_name)
            os.makedirs(dest_folder, exist_ok=True)

            dest_path = os.path.join(dest_folder, file)

            # handle duplicate
            base, ext = os.path.splitext(file)
            counter = 1
            while os.path.exists(dest_path):
                dest_path = os.path.join(dest_folder, f"{base}_{counter}{ext}")
                counter += 1

            shutil.move(source_path, dest_path)
            moved += 1
            print(f"📦 {file} -> {folder_name}")

print(f"\n✅ Selesai! Total file: {moved}")