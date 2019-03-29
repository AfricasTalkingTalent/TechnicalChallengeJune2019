# Erick Ogaro
# Date: 28th March, 2019

# Task 1

# This program has been structured such that the documents
# should be within the same working directory as this code snippet

# Due to the control structures I've implemented the program
# is able to handle lots of documents at the same time (hundreds)

import os

# Show the user all the available documents in that directory
path = "."

text_files = [f for f in os.listdir(path) if f.endswith('.txt')]
print("We have", len(text_files), "documents in the working directory: ", text_files, "\n")

# Read the documents
document_count = len(text_files)
i = 0
true_count = 0
while document_count > 0:

    # Structure to search for 'a' in any string pattern
    with open(text_files[i]) as fd:
        if 'a' in fd.read():
            print("The character 'a' was FOUND in", text_files[i])
            true_count += 1
        else:
            print("The character 'a' was NOT FOUND in", text_files[i])
    i += 1
    # reduces the document count each time it goes through one
    document_count -= 1

print("\n", true_count, "documents in total had the character 'a' in them.")
