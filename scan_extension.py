import os
from collections import Counter

source_dir = input("Masukkan folder yang mau dicek: ").strip('"')

if not os.path.exists(source_dir):
    print("❌ Folder tidak ditemukan!")
    exit()

ext_counter = Counter()
total_files = 0

for root, dirs, files in os.walk(source_dir):
    for file in files:
        total_files += 1
        ext = os.path.splitext(file)[1].lower()
        if ext == "":
            ext = "[no_extension]"
        ext_counter[ext] += 1

print("\n📊 HASIL SCAN:")
print(f"Total file: {total_files}\n")

for ext, count in ext_counter.most_common():
    print(f"{ext} : {count}")

print("\n✅ Selesai scan")