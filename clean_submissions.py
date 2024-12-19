import os
import shutil


def clean_submissions(main_dir):
    """
    Cleans the submissions directory by keeping only 'extract_file'
    in each student's folder and deleting all other files and subfolders.
    """

    for student_folder in os.listdir(main_dir):
        student_path = os.path.join(main_dir, student_folder)

        if not os.path.isdir(student_path):
            continue

        target_file = os.path.join(student_path, extract_file)

        if os.path.exists(target_file):
            for item in os.listdir(student_path):
                item_path = os.path.join(student_path, item)
                if item_path != target_file:
                    if os.path.isdir(item_path):
                        shutil.rmtree(item_path)
                    else:
                        os.remove(item_path)
        else:
            shutil.rmtree(student_path)


if __name__ == "__main__":

    main_directory = "D:\\PATH\\TO\\FOLDER"
    extract_file = "NAME_OF_FILE"
    clean_submissions(main_directory)
