# Joseph Maina Karuoya
# a program that given hundreds of documents,
# can find all documents with words containing the letter "a" in them.

# the documents are text files that can be read

# stores all documents with an 'a' in them
documentList = []

# a function to read the documents and check for the character 'a' - or any other letter.
def searchFor(value, documentPaths):
    for documentPath in documentPaths:
        with open(documentPath) as file:

            # try-except in case of any exceptions that may arise
            try:  
                for line in file:
                    if line.__contains__(value):
                        documentList.append(documentPath)
                        break

                file.close()

            except:
                print("Read error.")
                file.close()

# the list of document paths. For evaluation on local machine
# for evaluation purposes, you can add/alter paths.
# the folder contains tes documents to show that it works
documentPaths = [
    r"C:\Users\Prof Gitau\Documents\VSCode Scripts\ATChallenge\findingLetterA.py",
    r"C:\Users\Prof Gitau\Documents\VSCode Scripts\ATChallenge\randomFile.txt",
    r"C:\Users\Prof Gitau\Documents\VSCode Scripts\ATChallenge\randomFile3.txt",
    r"C:\Users\Prof Gitau\Documents\VSCode Scripts\ATChallenge\randomFile4.txt",
    r"C:\Users\Prof Gitau\Documents\VSCode Scripts\ATChallenge\randomFile5.txt",
    r"C:\Users\Prof Gitau\Documents\VSCode Scripts\ATChallenge\randomFile7.txt"
    ]

# this function, in essence, works as a map function, mapping the function to the list of documents
searchFor("a", documentPaths)
print(documentList)