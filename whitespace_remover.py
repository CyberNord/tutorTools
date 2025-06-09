import os
import unicodedata

# This little script will remove all whitespace from a folder and its subfolders.
# Additionally, it will replace all special characters.

path = "D:\\PATH\\TO\\FOLDER"

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)

    return ''.join([c for c in nfkd_form if not unicodedata.combining(c)])

def replace_whitespace_with_underscore(directory):
    folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]

    for folder in folders:
        old_name = os.path.join(directory, folder)

        new_name = os.path.join(directory, old_name
                            .replace(' ', '_')
                            .replace('-', '')
                            .replace('`', '')
                            .replace('´', '')
                            .replace('\'', ''))
        cleaned_name = remove_accents(new_name)
        os.rename(old_name, cleaned_name)

        
replace_whitespace_with_underscore(path)

# for future me
# Not working currently on the following special Characters: Š