"""
A function that checks and returns all files with letter "a"

Will work with the any directory
"""
import os
#link to the document
basepath = "../Task1"
file = []
files = []
#checks for files and directory in the path
for entry in os.listdir(basepath):
    #outputs only the files
    if os.path.isfile(os.path.join(basepath, entry)):
        #reads all files
        searchFile = open( entry , "r" );
        #loop through the file line by line
        for line in searchFile:
            #checks if "a" is in line
            if 'a' in line:
                #appends all entries to a file
                file.append(entry);
                #loops through all entries to ensure no duplicates
                for name in file:
                    if name not in files:
                        files.append(name);
#outputs as a list
print(files);
#closes the opened files
searchFile.close();