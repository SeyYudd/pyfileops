============================================================
           FILE MANAGEMENT TOOLKIT (PYTHON)
============================================================
Author: Muhamad Syifa (QA & Design Enthusiast)
Version: 1.0 - 2026
------------------------------------------------------------

[ IMAGE OF FILE ORGANIZATION SYSTEM FLOWCHART ]

[ MAIN SCRIPT: MERGE PDF & IMAGES ]
Menggabungkan PDF dan Gambar (JPG, PNG, WEBP) menjadi 1 PDF.
- Output: "merge YYYYMMDD - HH-MM.pdf"
- Jalankan: python merge_pdfs_images.py "C:\path\folder"

------------------------------------------------------------
[ UTILITY SCRIPTS: MANAJEMEN FILE ]
------------------------------------------------------------

1. file_prefixer.py  -> Tambah kata di AWAL nama file.
   Contoh: Anggur.png -> Rapat_Anggur.png

2. file_suffixer.py  -> Tambah kata di AKHIR (sebelum ekstensi).
   Contoh: Anggur.png -> Anggur_v1.png

3. group_by_type.py  -> Sortir file otomatis ke folder:
   (Images, Documents, Archives, Apps, Others).

4. group_by_text.py  -> Masukkan file ke folder berdasarkan 
   KATA KUNCI yang ada di nama filenya.

5. rename_by_text.py -> Ganti kata tertentu secara massal.
   Contoh: Cari "Draft", ganti jadi "Final".

6. delete_by_text.py -> HAPUS file yang mengandung kata tertentu.
   *Gunakan --dry-run untuk simulasi (aman).*

------------------------------------------------------------
[ CONTOH PERINTAH (POWERSHELL/CMD) ]
------------------------------------------------------------

# Rename massal:
python "file_prefixer.py" "D:\Folder\Target" "Prefix_"

# Sortir berdasarkan kata kunci:
python "group_by_text.py" "D:\Folder\Target" "Project_A"

# Simulasi hapus (tanpa benar-benar menghapus):
python "delete_by_text.py" "D:\Folder\Target" "temp" --dry-run

------------------------------------------------------------
[ TIPS ]
- Gunakan "" (tanda kutip) jika folder/file mengandung spasi.
- Selalu backup data sebelum melakukan operasi massal.
- Cek 'requirements.txt' untuk library yang dibutuhkan.
============================================================

------------------------------------------------------------
[ ADDITIONAL UTILITIES ]
------------------------------------------------------------

# Hapus folder kosong (dry-run / confirm):
python "delete_empty_folders.py" --path "D:\Folder\Target" --dry-run
python "delete_empty_folders.py" "D:\Folder\Target"

# Hapus file berdasarkan ukuran (KB) (dry-run / confirm):
python "delete_by_size.py" --path "D:\Folder\Target" --min 0 --max 10 --dry-run
python "delete_by_size.py" "D:\Folder\Target" 0 10
