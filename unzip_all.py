import os
import zipfile

# minta input dari user
base_path = input("Masukkan path folder berisi file ZIP: ").strip('"')

# validasi folder
if not os.path.exists(base_path):
    print("❌ Folder tidak ditemukan!")
    exit()

zip_found = False

for file_name in os.listdir(base_path):
    if file_name.endswith(".zip"):
        zip_found = True

        zip_path = os.path.join(base_path, file_name)

        # nama folder = nama zip tanpa .zip
        folder_name = file_name.replace(".zip", "")
        extract_path = os.path.join(base_path, folder_name)

        # buat folder
        os.makedirs(extract_path, exist_ok=True)

        # extract
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

        print(f"✅ Extracted: {file_name} -> {folder_name}")

if not zip_found:
    print("⚠️ Tidak ada file ZIP di folder tersebut")
else:
    print("✅ Semua file selesai di-extract")