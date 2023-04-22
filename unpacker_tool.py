import os
import zipfile
import shutil

# how to use:
# place zip file in directory. usually ...Tutor_...\...\Ass...\Zip
# set the path_unzip
# rename the zipfile to something short eg. "ass2.zip"
# apply the name in path_work
# run the programm

path_unzip = 'D:\\OneDrive\\Informatik\\Tutor_SS23\\ESoft\\Ass3\\Zip'
# path_unzip = 'D:\\OneDrive\\Informatik\\Tutor_SS23\\AlgoDat1_SS23\\Ass2\\Zip'
path_work = path_unzip + '\\ass3'
dest_folder = path_work + '_zips'



def unzip_and_remove_space(path):
    print("unpack files in path & replaces \' \' to \'_\'")
    for filename in os.listdir(path):
        if filename.endswith('.zip'):
            with zipfile.ZipFile(os.path.join(path, filename), 'r') as zipf:
                zipf.extractall(os.path.join(path, os.path.splitext(filename)[0]))

            for extracted_filename in os.listdir(os.path.join(path, os.path.splitext(filename)[0])):
                new_filename = extracted_filename.replace(' ', '_')
                os.rename(os.path.join(path, os.path.splitext(filename)[0], extracted_filename),
                          os.path.join(path, os.path.splitext(filename)[0], new_filename))



def extract_zip_files(path):
    print("extract all zip files in sub-folders of a folder")
    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith('.zip'):
                file_path = os.path.join(root, filename)
                with zipfile.ZipFile(file_path, 'r') as zip_ref:
                    zip_ref.extractall(root)



def rename_zip_files(path):
    print("rename all zip files in sub-folders of a folder to its parent folder's name")
    for root, dirs, files in os.walk(path):
        for filename in files:
            if filename.endswith('.zip'):
                zip_folder_name = os.path.basename(root)
                old_file_path = os.path.join(root, filename)
                new_file_path = os.path.join(root, zip_folder_name + '.zip')
                count = 1
                while os.path.exists(new_file_path):
                    new_file_name = f"{zip_folder_name}_{count}.zip"
                    new_file_path = os.path.join(root, new_file_name)
                    count += 1
                os.rename(old_file_path, new_file_path)



def move_zip_files(source_path, destination_path):
    print("moves all zip files in sub-folders of a folder to a specified folder")
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for root, dirs, files in os.walk(source_path):
        for filename in files:
            if filename.endswith('.zip'):
                old_file_path = os.path.join(root, filename)
                new_file_path = os.path.join(destination_path, filename)
                shutil.move(old_file_path, new_file_path)

unzip_and_remove_space(path_unzip)
extract_zip_files(path_work)
rename_zip_files(path_work)
move_zip_files(path_work, dest_folder)

print("done")
