import os
import io
import sys
import argparse
from datetime import datetime

from PIL import Image
from PyPDF2 import PdfMerger


def merge_folder(folder_path: str) -> str:
    if not os.path.isdir(folder_path):
        raise ValueError(f"Folder tidak ditemukan: {folder_path}")

    exts_pdf = {".pdf"}
    exts_img = {".jpg", ".jpeg", ".png", ".tif", ".tiff", ".bmp", ".webp"}
    valid_exts = exts_pdf | exts_img

    entries = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    # filter: cuma file yang gada kata diawal 'merge' (case-insensitive)
    candidates = [f for f in entries if os.path.splitext(f)[1].lower() in valid_exts and not f.lower().startswith("merge")]
    candidates.sort()

    if not candidates:
        return ""

    merger = PdfMerger()

    for name in candidates:
        path = os.path.join(folder_path, name)
        ext = os.path.splitext(name)[1].lower()

        if ext == ".pdf":
            try:
                merger.append(path)
            except Exception as e:
                print(f"Peringatan: gagal menambahkan PDF {name}: {e}")
        else:
            try:
                with Image.open(path) as img:
                    img_converted = img.convert("RGB")
                    bio = io.BytesIO()
                    img_converted.save(bio, format="PDF")
                    bio.seek(0)
                    merger.append(fileobj=bio)
            except Exception as e:
                print(f"Peringatan: gagal mengonversi gambar {name}: {e}")

    output_name = f"merge {datetime.now().strftime('%Y%m%d - %H-%M')}.pdf"
    output_path = os.path.join(folder_path, output_name)

    with open(output_path, "wb") as out_f:
        merger.write(out_f)

    merger.close()
    return output_path


def main():
    parser = argparse.ArgumentParser(description="Merge semua PDF dan gambar di satu folder menjadi 1 PDF.")
    parser.add_argument("folder", nargs="?", help="Folder yang berisi file untuk digabung. Jika kosong, akan diminta input.")
    args = parser.parse_args()

    folder = args.folder
    if not folder:
        folder = input("Masukkan path folder: ").strip()

    folder = os.path.abspath(folder)

    try:
        result = merge_folder(folder)
        if not result:
            print("Tidak ada file PDF atau gambar (jpg/png/...) yang ditemukan untuk digabung.")
            sys.exit(1)
        print(f"Selesai. File gabungan: {result}")
    except Exception as exc:
        print(f"Gagal: {exc}")
        sys.exit(2)


if __name__ == "__main__":
    main()
