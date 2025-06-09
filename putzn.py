import os

path = "D:\\PATH\\TO\\FOLDER"

# Define allowed extensions
allowed_extensions = ['.java', '.txt', '.rar']

def putzn(directory, allowed_exts):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if not any(file.endswith(ext) for ext in allowed_exts):
                print(f"Deleting {file_path}")
                os.remove(file_path)

putzn(path, allowed_extensions)