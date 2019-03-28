#! /usr/bin/env python

import os
import sys

"""
Solution for task 1;
The approach involves using recursion to find all the filenames and then applying
binary search to find the character. However, sorting mght take some runtime therefore
offsetting the advantage of binary search by an amount.

"""


def get_recursive_file_list(directory):
    """

    :This function gets a list of all the directories, recursively
    :params - directory

    """
    #Initialize a list to store our filenames
    files = list()
    #Use of the handy os.walk() function to collect filenames
    for (dir_path, dir_names, filenames) in os.walk(directory):
        files += [os.path.join(dir_path, file) for file in filenames]
    return files



def binary_search(array, char='a'):
    """
    :A binary search for a (for good runtime). We first sort the array, of course. 
    :params - array and character to search

    """
    array = (sorted(array))
    if len(array) <= 0:
        return
    left_end = 0 
    right_end = len(array)-1
    mid = (left_end + right_end)//2
    #Go through the array
    if (char == array[mid]):
        return mid
    #Implementing recursion
    if (char > array[mid]):
        return binary_search(array[mid+1:], char)
    return binary_search(array[:mid], char)



def file_search(filename):
    """
    :Searches for the character within the single file
    :params: filename

    """
    file = open(filename, 'rt', errors='replace')
    lines = file.readlines()
    for line in lines:
        if binary_search(line):
            return True


def file_traverse(directory):
    """
    :Traverses over the entire tree, searching each file
    :params - top-level directory

    """
    files = list()
    for file in get_recursive_file_list(directory):
        if file_search(file):
            files.append(file)
    return files


def main():
    """
    :Main function...Runnable anywhere
    """
    path = os.getcwd()
    files = file_traverse(path)
    for file in files:
        print(file + '\n')


if __name__ == '__main__':
    main()