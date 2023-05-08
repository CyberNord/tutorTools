import os
import zipfile

# zippt alle files in einem folder

path = 'D:\\The\\Path\\to\\your\\folder\\Zip'

print("Starting loop")
for foldername in os.listdir(path):
    if os.path.isdir(os.path.join(path, foldername)):
        zipname = foldername + '.zip'
        with zipfile.ZipFile(os.path.join(path, zipname), 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(os.path.join(path, foldername)):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.join(foldername, file))
print("..Done!")