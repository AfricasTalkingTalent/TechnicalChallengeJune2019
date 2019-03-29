#  Erick Ogaro, 2019.

# Task 1

# This program has been structured such that the documents
# should be within the same working directory as this code snippet

import os

# Show the user all the available documents in that directory
path = "."

i = 0
text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
print("Total documents available: ")
print(len(text_files))
print(text_files)

# function to search for 'a' in any string pattern
