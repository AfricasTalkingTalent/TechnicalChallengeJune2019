from glob import glob
from tika import parser
import os
class FileDigest(object):
    def __init__(self,filesList):
        '''

        :param filesList: list of paths to all the files to be evaluated
        '''
        self.filesList=filesList
        print(filesList)


# evaluate if document is pdf or simple text file. Currently the only supported files
    def checkExtension(self,document):

        if document.lower().endswith('.pdf'):
            return 1
        elif document.lower().endswith('.txt'):
            return 2
        else:
            return False

# use regex to find out if any word contains an a.
    def checkFor_a(self):
        filesWith_a=[] # files containing words with a will be appended here

        for singledocument in self.filesList: # iterate through every file
            singledocument='sampleDocs/'+singledocument
            if self.checkExtension(singledocument)==1: # it is a pdf
                pdf=parser.from_file(singledocument)
                if "a" in pdf['content']:
                    filesWith_a.append(singledocument)
            elif self.checkExtension(singledocument)==2: # it is a txt
                file=open(singledocument,"r").read()
                if "a" in file:
                    filesWith_a.append(singledocument)
                    break
                else:
                   continue

        return filesWith_a


# MAIN RUNNING OF PROGRAM

docDigestObj=FileDigest(os.listdir('sampleDocs'))

print("FILES CONTAINING WORDS WITH A")
for i in docDigestObj.checkFor_a():
    print(str(i)+"\n")



