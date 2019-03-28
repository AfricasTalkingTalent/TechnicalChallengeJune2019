import os
import argparse
import glob

#argument parser for capturing the dirpath for searching for documents. in command line you'll specify the dirpath as argument after the -f
try:
    ap=argparse.ArgumentParser()
    ap.add_argument('-f','--dirpath',required=True,
                    help="Directory to search for documents")
    args=vars(ap.parse_args())
    dirpath=args['dirpath']

    #funciton for finding character 'a' inside document X
    def find_a(X):
        with open(X,'r') as f:
            for line in f:
                if 'a' in line:
                    return True
        return False


    files=glob.glob(dirpath+"/*.*")     #capturing all documents that follow format *.*
    files=[file for file in files if not os.path.isdir(file)]   #excluding directories which may be named with a '.' and be confused as a document
    results=list(map(find_a,files)) #mapping the find_a function to the list of files in the directory

    #creates a list of documents whose index number in the results file have bool True
    docs=[file for file in files if results[(files.index(file))] is True]

    if docs==[]:
        print("No documents found containing 'a'.")
    else:
        for doc in docs:
            print(doc)

except Exception as e:
    print("Fatal error: "+e)