import shutil
import sys
import os
import zipfile

# Modified version of B.Fürst

# Parameters: PATH_TO_ZIP + CHOSEN_GROUP + GROUPS_TO_CORRECT
# PATH_TO_ZIP: get all submissions from the Moodle and do not rename it.
# CHOSEN_GROUP: The group number you're assigned to
# GROUPS_TO_CORRECT: How many groups you have to correct.


NO_GROUPS = 5
ASS_NO = "Ass04"

# BASE_PATH is the folder where the structure is created. Do not forget to add a Slash at the end
BASE_PATH = "C:\\PATH\\TO\\DIRECTORY\\FOLDER\\FOLDER\\"


def split(list_a, chunk_size):
    for i in range(0, len(list_a), chunk_size):
        yield list_a[i:i + chunk_size]


if len(sys.argv) < 3 or len(sys.argv) > 4:
    print(
        "Wrong number of arguments.\nProvide the zip file as first argument and the chosen group(s) as the second(third).")
    exit()

source_file = sys.argv[1]
chosenGroup = []

try:
    cg = int(sys.argv[2]) - 1
    chosenGroup.append(cg)
except:
    print("Second argument needs to be a number between 0 and ", NO_GROUPS)
    exit()

if len(sys.argv) == 4:
    try:
        cg = int(sys.argv[3]) - 1
        chosenGroup.append(cg)
    except:
        print("Third argument needs to be a number between 0 and", NO_GROUPS)
        exit()

if any(map(lambda x: x < 0 or x > NO_GROUPS - 1, chosenGroup)):
    print("Group number outside legal range. Should be between 1 and", NO_GROUPS)
    exit()

print(source_file)
if not source_file.endswith(".zip"):
    print("First argument has to be a zip file")
    exit()

path = BASE_PATH + ASS_NO
try:
    os.makedirs(path, exist_ok=True)
except Exception as e:  # Catch any other exception that might occur
    print(f"Unexpected error while creating directory {path}: {e}")
    exit()
if os.path.exists(path):
    print(path + " is already present! Do you want to erase the directory and start over again?")
    ans = input("Enter y to proceed or anything else to cancel: ").lower()
    if ans == "y":
        print("Replacing old files and starting fresh!")
        shutil.rmtree(path)
        os.makedirs(path, exist_ok=True)
    else:
        print("Operation cancelled!")
        exit()
else:
    os.makedirs(path, exist_ok=True)

with zipfile.ZipFile(source_file, "r") as zip_ref:
    zip_ref.extractall(path)

files = sorted(list(os.listdir(path)))
nOAssingments = len(files)
groupSize = nOAssingments // NO_GROUPS
rest = nOAssingments % NO_GROUPS

groups = []
chosenFiles = []

for _ in range(0, rest):
    groups.append(files[:groupSize + 1])
    files = files[-(len(files) - (groupSize + 1)):]

for _ in range(0, NO_GROUPS - rest):
    groups.append(files[:groupSize])
    files = files[-(len(files) - groupSize):]

for cg in chosenGroup:
    chosenFiles.append(groups[cg])

rest = []

for i in range(0, NO_GROUPS):
    if not i in chosenGroup:
        rest.append(groups[i])

with open(os.path.join(path, "_pts.txt"), "a", encoding="utf-8") as pts_file:
    for fileList in chosenFiles:
        for file in fileList:
            if not file.startswith("_"):
                s = file.split("_")
                p = s[0]
                full_path = os.path.join(path, file)
                if os.path.isfile(full_path):  # Ensure it's a file
                    try:
                        with zipfile.ZipFile(full_path) as zip_ref:
                            zip_ref.extractall(os.path.join(path, p))
                        os.remove(full_path)
                    except PermissionError as e:
                        print(f"Permission error accessing {full_path}: {e}")
                    except zipfile.BadZipFile as e:
                        print(f"Bad Zip File {full_path}: {e}")
                    except Exception as e:
                        print(f"Unexpected error with {full_path}: {e}")
                else:
                    # unzip files within the path
                    if os.path.isdir(full_path):
                        zip_files = [f for f in os.listdir(full_path) if f.endswith('.zip')]
                        if len(zip_files) == 1:
                            pts_file.write("[ /24 ]  " + p + "\n")
                            zip_file_path = os.path.join(full_path, zip_files[0])
                            try:
                                with zipfile.ZipFile(zip_file_path) as zip_ref:
                                    zip_ref.extractall(full_path)
                            except Exception as e:
                                print(f"Unexpected error with {zip_file_path}: {e}")
                        else:
                            pts_file.write("[ /24 ]  " + p + "\n")
                            print(f"Skipped {full_path}, contains no zip file or more than one.")
                    else:
                        print(f"Skipped {full_path}, not a file or recognizable directory or file.")
os.mkdir(path + "/_Done")
os.mkdir(path + "/_Korrekturen")
os.mkdir(path + "/_Korrekturen/_Uploaded")
os.mkdir(path + "/_Rest")
for fl in rest:
    for file in fl:
        shutil.move(os.path.join(path, file), os.path.join(path + "/_Rest", file))
print("Extracted", sum(map(len, chosenFiles)), "files and placed them in", path, "\nPlaced the remaining",
      sum(map(len, rest)), "files in /_Rest.")
ans = input("Delete " + source_file + "? Enter y or anything else to cancel: ").lower()
if ans == "y":
    os.remove(source_file)
    print("Removed", source_file, "!")
