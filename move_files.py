import os
import shutil

# input dari user
source_dir = input("Masukkan folder sumber (Takeout): ").strip('"')
target_dir = input("Masukkan folder tujuan: ").strip('"')
extensions = input("Masukkan ekstensi (contoh: .jpg,.png): ").lower().split(",")

# validasi
if not os.path.exists(source_dir):
    print("❌ Folder sumber tidak ditemukan!")
    exit()

os.makedirs(target_dir, exist_ok=True)

moved_count = 0

# jalanin recursive
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if any(file.lower().endswith(ext) for ext in extensions):
            source_path = os.path.join(root, file)
            target_path = os.path.join(target_dir, file)

            # handle nama file duplicate
            base, ext = os.path.splitext(file)
            counter = 1
            while os.path.exists(target_path):
                target_path = os.path.join(target_dir, f"{base}_{counter}{ext}")
                counter += 1

            shutil.move(source_path, target_path)
            moved_count += 1
            print(f"📦 Moved: {file}")

print(f"\n✅ Selesai! Total file dipindahkan: {moved_count}")