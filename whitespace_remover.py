import os

path = 'C:\\PATH\\TO\\DIRECTORY\\FOLDER\\FOLDER\\'


def replace_whitespace_with_underscore(directory):
    folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]

    for folder in folders:
        old_name = os.path.join(directory, folder)
        new_name = os.path.join(directory, folder.replace(' ', '_').replace('-', ''))
        os.rename(old_name, new_name)


replace_whitespace_with_underscore(path)
