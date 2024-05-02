import os
import shutil

# the program will walk tru all subfolders and place the files in there to a 'sub' - folder
# then a txt 'points' is created with user specified input

path = 'D:\\The\\Path\\to\\your\\folder\\Zip'
text = "your text"


def process_directory(base_path):
    # Iterate over directories directly under the base_path
    for folder_name in os.listdir(base_path):
        folder_path = os.path.join(base_path, folder_name)

        # Check if the item is a directory
        if os.path.isdir(folder_path):
            # Path for the 'sub' directory
            sub_folder_path = os.path.join(folder_path, 'sub')

            # Create the 'sub' directory if it does not exist
            if not os.path.exists(sub_folder_path):
                os.makedirs(sub_folder_path)

            # Move all files into the 'sub' folder
            for filename in os.listdir(folder_path):
                original_file_path = os.path.join(folder_path, filename)
                if os.path.isfile(original_file_path):  # Ensure it's a file, not a directory
                    new_file_path = os.path.join(sub_folder_path, filename)
                    shutil.move(original_file_path, new_file_path)

            # Create 'points.txt' with the required content
            points_text_content = text
            points_file_path = os.path.join(folder_path, 'points.txt')
            with open(points_file_path, 'w') as file:
                file.write(points_text_content)

    print("Processing completed for all subdirectories in:", base_path)


if __name__ == "__main__":
    process_directory(path)
