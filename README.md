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
