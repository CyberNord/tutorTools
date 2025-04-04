import os
import shutil
import zipfile
import random
import tempfile
from pathlib import Path
import patoolib  # make sure this is installed

# This little script will
# 1. take your rar file
# 2. put into one of 10 folders
# 3. zip it to surprise.zip
# 4. loop back to (1) with surprise.zip as new input

# purpose --> annoy someone.

# === CONFIG ===
INPUT_RAR = "D:\\replace\\with\\actual\\path\\here\\target.rar"
NUM_ITERATIONS = 100
NUM_FOLDERS = 10
OUTPUT_DIR = Path("output_zips")
FINAL_OUTPUT = OUTPUT_DIR / "final_surprise.zip"

def extract_rar_to_zip(rar_path: str, zip_path: str):
    with tempfile.TemporaryDirectory() as tmpdir:
        patoolib.extract_archive(rar_path, outdir=tmpdir, verbosity=-1)
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(tmpdir):
                for file in files:
                    file_path = os.path.join(root, file)
                    arcname = os.path.relpath(file_path, tmpdir)
                    zipf.write(file_path, arcname=arcname)

def generate_surprise(initial_zip: str, iterations: int):
    OUTPUT_DIR.mkdir(exist_ok=True)
    current_input = Path(initial_zip)

    for i in range(iterations):
        base_dir = Path(tempfile.mkdtemp())
        subdirs = []

        real_index = random.randint(0, NUM_FOLDERS - 1)

        for j in range(NUM_FOLDERS):
            folder = base_dir / str(j)
            folder.mkdir()
            subdirs.append(folder)
            dest_zip = folder / "suprisepak.zip"

            if j == real_index:
                shutil.copy(current_input, dest_zip)
            else:
                with zipfile.ZipFile(dest_zip, 'w'): pass

        next_zip = OUTPUT_DIR / f"suprisepak_{i}.zip"
        with zipfile.ZipFile(next_zip, 'w', zipfile.ZIP_DEFLATED) as final_zip:
            for folder in subdirs:
                for root, _, files in os.walk(folder):
                    for file in files:
                        full_path = os.path.join(root, file)
                        arcname = os.path.relpath(full_path, base_dir)
                        final_zip.write(full_path, arcname=arcname)

        shutil.rmtree(base_dir)
        current_input = next_zip

    shutil.copy(current_input, FINAL_OUTPUT)
    print(f"✅ Final ZIP created: {FINAL_OUTPUT.absolute()}")

if __name__ == "__main__":
    EXTRACTED_ZIP = "suprisepak.zip"
    extract_rar_to_zip(INPUT_RAR, EXTRACTED_ZIP)
    generate_surprise(EXTRACTED_ZIP, NUM_ITERATIONS)
