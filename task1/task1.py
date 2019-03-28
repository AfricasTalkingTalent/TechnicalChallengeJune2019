from os import listdir
from os.path import isfile, join, isdir


# we first need to get files in the directory
def input_dir(pwd):
        # check if the dir entered is a directory
    if isdir(pwd):
        # to make a list of all files in the directory.
        files_dir = []
        for files in listdir(pwd):
            if isfile(join(pwd, files)):
                files_dir.append(files)
        return files_dir
    else:
        return "check the directory and try again"


def find_a(pwd, files_dir):
    # dictionary to store if files have a or not
    # key is file_name value is 1 for a , 0 for no
    file_dict = {}

    # open and read file contents for reach file
    for file in files_dir:
        with open(join(pwd, file), 'r') as file_contents:
            content = file_contents.read()
            if 'a' in content:
                file_dict[file] = 1
            else:
                file_dict[file] = 0

    return file_dict


def decision(file_dict):
    # list of files with a
    files_a = []

    for f in file_dict:
        if file_dict[f] == 1:
            files_a.append(f)
    return files_a


input_directory = input("Enter files location \n")

file_obj = input_dir(input_directory)
finding_a = find_a(input_directory, file_obj)
files_a = decision(finding_a)

# output results
print("\nThe files with 'a' are :")
for p in files_a:
    print(p)
