import os
import zipfile

# zippt alle files in einem folder

path = 'D:\\The\\Path\\to\\your\\input_folder\\Zip'
zipPath = 'D:\\The\\Path\\to\\your\\output_folder\\Zip'
padding = '_YOUR_PADDING'

if not os.path.exists(zipPath):
    os.makedirs(zipPath)

print("Starting loop")
for foldername in os.listdir(path):
    if os.path.isdir(os.path.join(path, foldername)):
        zipname = foldername + padding + '.zip'
        with zipfile.ZipFile(os.path.join(zipPath, zipname), 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, dirs, files in os.walk(os.path.join(path, foldername)):
                for file in files:
                    zipf.write(os.path.join(root, file), os.path.join(foldername, file))
print("..Done!")
