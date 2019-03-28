#!/usr/bin/python3
"""
    TASK 1: Find documents containing the character "a"
    In this challenge I am assuming that the documents are text files.

    This program checks for a character "a" in text files
    and prints out the file names found containing the character.
    The program assumes that the documents are placed in a directory
    and therefore will take the directory path as an argument. If
    the path is not provided the programs will assume the documents
    are in the current working directory.
"""
import sys
import os
from binaryornot.check import is_binary


def main(path):
    files = []  # Save file names containing the search character
    # Get the files in the directory and process them one by one
    for file in os.listdir(path):
        # Ensure it is a valid text file
        if os.path.isdir(file) or is_binary(file):
            continue

        with open(file, 'r') as f:

            for line in f:
                if "a" in line:
                    files.append(file)  # The file contains the character
                    break  # There is no need to continue since we already found the character

            f.close()

    for file in files:
        print(file)


if __name__ == "__main__":
    # Get the directory path
    if len(sys.argv) == 1:
        path = os.getcwd()
    elif len(sys.argv) == 2:
        path = sys.argv[1]
        os.chdir(path)  # Move to the directory containing the documents
    else:
        print("Usage: %s <path>" % (sys.argv[0]))
        sys.exit()

    main(path)
