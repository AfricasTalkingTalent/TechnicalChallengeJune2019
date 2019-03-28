#task1
import os

class documents:
    pass

#give the directory in which the files are stored
Path = "c:/users/sam/desktop/codefiles/"

#create a list containing the names of the files in the directory
documents = os.listdir(Path)

#iterate through the list
for name in documents:
    if name.endswith(".txt"):  #search for text documents
        try:
            with open(Path + name, "r", encoding="ascii") as doc: #open the documents
                for line in doc:   #read the documents line by line
                    if "a" in line: 
                        print ("Found in %s !" % (name))  #return names of files with words that contain character 'a'
        except:
            pass