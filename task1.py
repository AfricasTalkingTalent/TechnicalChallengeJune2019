import os

#function for checling path validity
def directory_is_valid(directory):
    if not isinstance(directory, str) or not directory:
        return False
    if not os.path.exists(directory):
        return False
    return True

def map_function():
    listOfFiles = []
    directory = input("Enter the directory of the files") #prompt for file path
    
    if not directory_is_valid(directory):   #check if directory is valid
        print("Invalid directory")
        return "Invalid directory"
    
    #list all files
    entries = os.scandir(directory)
    for entry in entries:
        if os.path.isfile(os.path.join(directory, entry.name)):
            listOfFiles.append(entry.name)
    
    
    #create a dictionary with file names as keys and 1 if the file contains an 'a' or 0 if not
    mapOfFiles = {}
    #open each file and check if 'a' is present
    for filename in listOfFiles:
        f = open(os.path.join(directory, filename), "r", encoding='latin1')
        contents = f.read()
        if 'a' in contents:
            mapOfFiles[filename] = 1
        else:
            mapOfFiles[filename] = 0
    return mapOfFiles
    

#function to select the files with letter 'a' in the content
def reduce_function(mapOfFiles):
    filesWithA = []
    for file in mapOfFiles:
        if mapOfFiles[file] == 1:
            filesWithA.append(file)
    
    return filesWithA

mapObject = map_function()
filesWithA = reduce_function(mapObject)

print("The following files have letter 'a' in them:")
for file in filesWithA:
       print(file)