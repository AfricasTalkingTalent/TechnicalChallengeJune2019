import os
import sys


# This function list down all the files in a directory using the (listdir) method.
def get_files(directory):
    files = os.listdir(directory)
    return files

def get_file_content(filename): # This function returns all the contents in a file.

    f= open(filename) # Here we are opening the file using the python buld in method called open.

    return f.read()# Here we return the read files

def main(directory, search): # This is the main function, we pass in two arguments: directory and search
    
    for file in get_files(directory): # At this point, we loop through the directory to find the files containing letter a
        
        files_containing_letter_a = os.path.join(directory, file)
        if search in get_file_content(files_containing_letter_a):# Here, if the searched file exist, it will print out
            print(file)

if __name__ == '__main__':
    folder_name = sys.argv[1]
    search_string = sys.argv[2]
    main(folder_name, search_string)