FILE MANAGEMENT TOOLKIT - CONTOH PERINTAH
Ganti "D:\Folder\Target" dengan path folder kamu sendiri.
Tips: selalu coba --dry-run dulu biar aman.

==============================merge_pdfs_images==============================
gabung semua PDF & gambar jadi 1 file PDF
1. # tanya folder dulu (interaktif)
python "merge_pdfs_images.py"
2. # langsung kasih path-nya
python "merge_pdfs_images.py" "D:\Folder\Target"

==============================file_prefixer==============================
tambah kata di depan nama file  ->  Anggur.png jadi Rapat_Anggur.png
1. # tanya folder & prefix (interaktif)
python "file_prefixer.py"
2. # langsung kasih folder + prefix-nya
python "file_prefixer.py" "D:\Folder\Target" "Rapat_"
3. # pakai flag
python "file_prefixer.py" --path "D:\Folder\Target" --prefix "Rapat_"

==============================file_suffixer==============================
tambah kata di belakang nama file  ->  Anggur.png jadi Anggur_v1.png
1. # tanya folder & suffix (interaktif)
python "file_suffixer.py"
2. # langsung kasih folder + suffix-nya
python "file_suffixer.py" "D:\Folder\Target" "_v1"
3. # pakai flag
python "file_suffixer.py" --path "D:\Folder\Target" --suffix "_v1"

==============================group_by_type==============================
sortir file ke folder otomatis: Images, Documents, Archives, Apps, Others
1. # tanya folder (interaktif)
python "group_by_type.py"
2. # langsung kasih path-nya
python "group_by_type.py" "D:\Folder\Target"
3. # pakai flag
python "group_by_type.py" --path "D:\Folder\Target"

==============================group_by_text==============================
pindah file yang namanya ada kata kunci ke subfolder baru
1. # tanya folder & kata kunci (interaktif)
python "group_by_text.py"
2. # langsung kasih folder + kata kunci
python "group_by_text.py" "D:\Folder\Target" "Project_A"
3. # pakai flag
python "group_by_text.py" --path "D:\Folder\Target" --keyword "Project_A"

==============================rename_by_text==============================
ganti kata tertentu di nama file  ->  Draft_Laporan.pdf jadi Final_Laporan.pdf
1. # tanya semua input (interaktif)
python "rename_by_text.py"
2. # langsung kasih folder + kata lama + kata baru
python "rename_by_text.py" "D:\Folder\Target" "Draft" "Final"
3. # pakai flag
python "rename_by_text.py" --path "D:\Folder\Target" --old "Draft" --new "Final"
4. # preview dulu tanpa rename beneran
python "rename_by_text.py" --path "D:\Folder\Target" --old "Draft" --new "Final" --dry-run
5. # langsung eksekusi tanpa konfirmasi
python "rename_by_text.py" --path "D:\Folder\Target" --old "Draft" --new "Final" --yes

==============================delete_by_text==============================
hapus file yang namanya mengandung kata kunci
1. # tanya folder & kata kunci (interaktif)
python "delete_by_text.py"
2. # langsung kasih folder + kata kunci
python "delete_by_text.py" "D:\Folder\Target" "temp"
3. # pakai flag
python "delete_by_text.py" --path "D:\Folder\Target" --keyword "temp"
4. # preview dulu tanpa hapus beneran
python "delete_by_text.py" --path "D:\Folder\Target" --keyword "temp" --dry-run
5. # langsung hapus tanpa konfirmasi
python "delete_by_text.py" --path "D:\Folder\Target" --keyword "temp" --yes

==============================delete_by_size==============================
hapus file berdasarkan rentang ukuran (KB)
1. # tanya semua input (interaktif)
python "delete_by_size.py"
2. # langsung kasih folder + ukuran min & max (KB)
python "delete_by_size.py" "D:\Folder\Target" 0 10
3. # pakai flag
python "delete_by_size.py" --path "D:\Folder\Target" --min 0 --max 10
4. # preview dulu
python "delete_by_size.py" --path "D:\Folder\Target" --min 0 --max 10 --dry-run
5. # langsung hapus tanpa konfirmasi
python "delete_by_size.py" --path "D:\Folder\Target" --min 0 --max 10 --yes

==============================delete_empty_folders==============================
hapus subfolder yang kosong
1. # tanya folder (interaktif)
python "delete_empty_folders.py"
2. # langsung kasih path-nya
python "delete_empty_folders.py" "D:\Folder\Target"
3. # preview dulu
python "delete_empty_folders.py" --path "D:\Folder\Target" --dry-run
4. # langsung hapus tanpa konfirmasi
python "delete_empty_folders.py" --path "D:\Folder\Target" --yes

==============================rename_sequential==============================
rename file jadi urutan nomor  ->  001.jpg, 002.jpg, 003.jpg
opsi: --prefix (nama depan), --start (nomor awal), --digits (panjang angka), --ext (filter ekstensi), --new-ext (ganti ekstensi)
1. # tanya folder (interaktif)
python "rename_sequential.py"
2. # langsung kasih path-nya
python "rename_sequential.py" "D:\Folder\Target"
3. # kasih prefix + padding 3 digit
python "rename_sequential.py" --path "D:\Folder\Target" --prefix "FOTO_" --digits 3
4. # mulai dari nomor 5
python "rename_sequential.py" --path "D:\Folder\Target" --prefix "DOC_" --start 5
5. # filter cuma file .jpg
python "rename_sequential.py" --path "D:\Folder\Target" --prefix "IMG_" --ext jpg
6. # preview dulu
python "rename_sequential.py" --path "D:\Folder\Target" --prefix "FOTO_" --dry-run
7. # langsung tanpa konfirmasi
python "rename_sequential.py" --path "D:\Folder\Target" --prefix "FOTO_" --yes

==============================move_duplicate_by_length==============================
pindah file yang nama depannya mirip ke folder "THIS IS DUPLICATE"
opsi: --length (jumlah karakter, default 50), --include-ext y/n (ikutkan ekstensi saat bandingkan)
1. # tanya semua input (interaktif)
python "move_duplicate_by_length.py"
2. # langsung kasih path-nya
python "move_duplicate_by_length.py" "D:\Folder\Target"
3. # bandingkan 50 karakter pertama, tanpa ekstensi
python "move_duplicate_by_length.py" --path "D:\Folder\Target" --length 50 --include-ext n
4. # bandingkan dengan ekstensi ikut dihitung
python "move_duplicate_by_length.py" --path "D:\Folder\Target" --length 50 --include-ext y
5. # preview dulu
python "move_duplicate_by_length.py" --path "D:\Folder\Target" --length 50 --dry-run
6. # langsung pindah tanpa konfirmasi
python "move_duplicate_by_length.py" --path "D:\Folder\Target" --length 50 --yes

==============================generate_to_pdf==============================
konversi gambar (PNG, JPG, BMP, GIF, WEBP) dan TXT jadi PDF
1. # konversi satu file langsung
python "generate_to_pdf.py" "D:\Folder\Target\foto.jpg"
2. # konversi satu file pakai flag
python "generate_to_pdf.py" --path "D:\Folder\Target\foto.jpg"
3. # konversi semua file di folder
python "generate_to_pdf.py" --path "D:\Folder\Target" --batch
4. # preview dulu tanpa konversi beneran
python "generate_to_pdf.py" --path "D:\Folder\Target" --batch --dry-run
