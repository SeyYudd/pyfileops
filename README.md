[ SETUP ]
Untuk Windows:
Cukup jalankan file 'setup_env.bat' dengan cara klik dua kali 
atau ketik .\setup_env.bat di terminal.

Isi file setup_env.bat seharusnya:
@echo off
pip install -r requirements.txt
pause

Merge PDF & Images

Script kecil untuk menggabungkan semua file PDF dan gambar di sebuah folder menjadi satu file PDF.

Fitur:
 - Menggabungkan file dengan ekstensi PDF dan gambar (jpg, png, tif, bmp, webp).
 - Mengabaikan file yang namanya diawali dengan merge.
 - Menyimpan hasil sebagai merge YYYYMMDD - HH-MM.pdf di folder yang sama.

Cara pakai:
1. Install dependencies: python -m pip install -r requirements.txt
2. Jalankan: python merge_pdfs_images.py "C:\path\ke\folder" atau jalankan tanpa argumen untuk diminta memasukkan path.

Jika tidak ada file yang cocok, skrip akan memberi tahu dan keluar.

---

Tambahan: Utility kecil untuk manajemen file
------------------------------------------------

Saya menambahkan beberapa skrip utilitas untuk membantu mengorganisir file di folder:

- `SmartSort-CLI.py` — CLI untuk prefix/suffix/samagroup (lihat contoh di bawah)
- `file_prefixer.py` — interaktif: tambahkan prefix ke nama file (hindari double-prefix)
- `file_suffixer.py` — interaktif: tambahkan suffix sebelum ekstensi (hindari double-suffix)
- `group_by_type.py` — pindahkan file ke folder berdasarkan tipe/ekstensi (Images, Documents, dll)
- `group_by_text.py` — interaktif: pindahkan file yang mengandung kata tertentu ke folder bernama kata tersebut
 - `group_by_text.py` — interaktif: pindahkan file yang mengandung kata tertentu ke folder bernama kata tersebut
 - `delete_by_text.py` — hapus file yang mengandung kata tertentu (interactive / positional). Hati-hati: operasi ini dapat menghapus file permanen.

Contoh penggunaan (PowerShell / CMD):

```powershell
# file_prefixer
# 1) Interactive (prompts):
python "merge PDF/file_prefixer.py"
# 2) Direct (positional):
python "merge PDF/file_prefixer.py" "D:\OneDrive\Personal\Coding\Python\merge PDF\contoh_pdf_1" "Anggur_"
# 3) Flags form:
python "merge PDF/file_prefixer.py" --path "D:\OneDrive\Personal\Coding\Python\merge PDF\contoh_pdf_1" --prefix "Anggur_"

# file_suffixer (default adds suffix '_anggur' if empty)
python "merge PDF/file_suffixer.py"
python "merge PDF/file_suffixer.py" "D:\OneDrive\Personal\Coding\Python\merge PDF\contoh_pdf_1" "_anggur"
python "merge PDF/file_suffixer.py" --path "D:\OneDrive\Personal\Coding\Python\merge PDF\contoh_pdf_1" --suffix "_anggur"

# group_by_type
python "merge PDF/group_by_type.py"
python "merge PDF/group_by_type.py" "D:\OneDrive\Personal\Coding\Python\merge PDF\contoh_pdf_1"
python "merge PDF/group_by_type.py" --path "D:\OneDrive\Personal\Coding\Python\merge PDF\contoh_pdf_1"

# group_by_text (default keyword 'anggur' if empty)
python "merge PDF/group_by_text.py"
python "merge PDF/group_by_text.py" "D:\OneDrive\Personal\Coding\Python\merge PDF\contoh_pdf_1" "anggur"
python "merge PDF/group_by_text.py" --path "D:\OneDrive\Personal\Coding\Python\merge PDF\contoh_pdf_1" --keyword "anggur"
python "merge PDF/delete_by_text.py" --path "D:\OneDrive\Personal\Coding\Python\merge PDF\contoh_pdf_1" --keyword "anggur" --dry-run
python "merge PDF/delete_by_text.py" "D:\OneDrive\Personal\Coding\Python\merge PDF\contoh_pdf_1" "anggur"
python "merge PDF/rename_by_text.py" --path "D:\OneDrive\Personal\Coding\Python\merge PDF\contoh_pdf_1" --old "anggur" --new "ganteng" --dry-run
python "merge PDF/rename_by_text.py" "D:\OneDrive\Personal\Coding\Python\merge PDF\contoh_pdf_1" "anggur" "ganteng"
```

Catatan singkat tiap skrip:

- `file_prefixer.py`: menambahkan prefix ke setiap file. Jika file sudah mulai dengan prefix yang sama, file tersebut dilewati. Jika terjadi nama yang sama, script menambahkan suffix `_1`, `_2`, dll untuk menghindari overwrite.
- `file_suffixer.py`: menambahkan suffix tepat sebelum ekstensi (gunakan `._v1` jika ingin). Menghindari double-suffix dan menangani collision serupa.
- `group_by_type.py`: menggunakan peta ekstensi -> folder (mis. `.png`,`.jpg` -> `Images`, `.pdf` -> `Documents`). File yang tidak dikenal dipindah ke `Others`.
- `group_by_text.py`: minta keyword, buat folder bernama keyword, dan pindahkan file yang mengandung keyword (substring exact). Menangani collision dengan menambahkan counter pada nama file tujuan.

Tips:

- Selalu coba `--dry-run` pada `SmartSort-CLI.py` untuk melihat tindakan tanpa memindahkan file.
- Backup folder penting sebelum menjalankan operasi massal.

General:

Repositori ini berisi skrip kecil untuk menggabungkan PDF/gambar serta utilitas
manajemen file (prefix/suffix/group/rename/delete). Gunakan `README_Using.md` untuk
contoh perintah langsung (positional, flags, dry-run).
