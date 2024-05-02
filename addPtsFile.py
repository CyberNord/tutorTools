import os
import shutil

# the program will walk tru all subfolders and place the files in there to a 'sub' - folder
# then a txt 'points' is created with user specified input

path = 'D:\\The\\Path\\to\\your\\folder\\Zip'
text = "your text"

def process_directory(base_path):
    for folder_name in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder_name)

        if os.path.isdir(folder_path):
            sub_folder_path = os.path.join(folder_path, 'sub')

            if not os.path.exists(sub_folder_path):
                os.makedirs(sub_folder_path)

            for filename in os.listdir(folder_path):
                original_file_path = os.path.join(folder_path, filename)
                if os.path.isfile(original_file_path):
                    new_file_path = os.path.join(sub_folder_path, filename)
                    shutil.move(original_file_path, new_file_path)

            points_text_content = "Tutor: RG\nEx1: /8\nEx2: /16\ntestcases Output: \n"
            points_file_path = os.path.join(folder_path, 'points.txt')
            with open(points_file_path, 'w') as file:
                file.write(points_text_content)

    print("Processing completed for all subdirectories in:", base_path)


if __name__ == "__main__":
    process_directory(path)
