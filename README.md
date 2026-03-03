# py-pdf-merger / file management toolkit

Kumpulan script Python kecil buat manajemen file: gabung PDF, rename, hapus, sortir, dan konversi ke PDF.

---

## Instalasi

**Windows (cara cepat):**
klik dua kali `setup_env.bat`, atau jalankan di terminal:
```bat
.\setup_env.bat
```

**Manual:**
```bash
pip install -r requirements.txt
```

Dependensi yang dibutuhkan sudah ada di `requirements.txt` (Pillow, PyPDF2).

---

## Isi Script

| Script | Fungsi |
|---|---|
| `merge_pdfs_images.py` | Gabung semua PDF & gambar jadi 1 file PDF |
| `file_prefixer.py` | Tambah kata di depan nama file |
| `file_suffixer.py` | Tambah kata di belakang nama file (sebelum ekstensi) |
| `group_by_type.py` | Sortir file ke folder berdasarkan ekstensi |
| `group_by_text.py` | Pindah file yang namanya mengandung kata kunci ke subfolder |
| `rename_by_text.py` | Ganti kata tertentu di nama file secara massal |
| `delete_by_text.py` | Hapus file yang namanya mengandung kata kunci |
| `delete_by_size.py` | Hapus file berdasarkan rentang ukuran (KB) |
| `delete_empty_folders.py` | Hapus subfolder yang kosong |
| `rename_sequential.py` | Rename file jadi urutan nomor otomatis |
| `move_duplicate_by_length.py` | Pindah file dengan nama mirip ke folder duplikat |
| `generate_to_pdf.py` | Konversi gambar / TXT jadi PDF |

---

## Cara Pakai

Lihat `README_Using.md` untuk semua contoh perintah lengkap.

> Tips: hampir semua script punya opsi `--dry-run` buat preview sebelum eksekusi beneran.
