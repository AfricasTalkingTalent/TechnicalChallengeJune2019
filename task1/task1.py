'''
CODE BY KIMARU THAGANA
Requred packages:
pip3 install tika
pip3 install python-docx
'''

from docx import Document
from tika import parser
import os
class FileDigest(object):
    def __init__(self,filesList):
        '''

        :param filesList: list of paths to all the files to be evaluated
        '''
        self.filesList=filesList


# evaluate if document is pdf, docx or simple text file. Currently the only supported files
    # These are the most common document file formarts
    def checkExtension(self,document):

        if document.lower().endswith('.pdf'):
            return 1
        elif document.lower().endswith('.txt') or document.lower().endswith('.docx'):
            return 2
        else:
            return False

# use regex to find out if any word contains an a.
    def checkFor_a(self):
        filesWith_a=[] # files containing words with a will be appended here

        for singledocument in self.filesList: # iterate through every file
            singledocument='sampleDocs/'+singledocument
            if self.checkExtension(singledocument)==1: # it is a pdf
                pdf=parser.from_file(singledocument) #read pdf into variable
                if "a" in pdf['content']: # inspect presence of a in document
                    filesWith_a.append(singledocument) # append to list

            elif self.checkExtension(singledocument)==2: # it is a txt or docx
                if singledocument.lower().endswith('.docx'):
                    doc = Document(singledocument)
                    allText = ''
                    for doctext in doc.paragraphs:
                        allText.join(str(doctext.text))
                        if "a" in allText:
                            filesWith_a.append(singledocument)  # append to list
                else:
                    file=open(singledocument,"r").read()
                    if "a" in file: # check presence of a
                        filesWith_a.append(singledocument) # append to list


        return filesWith_a # return a list of files with words containing a


# MAIN RUNNING OF PROGRAM
# assumption is all the documents in question will be in a common folder, sampleDocs
docDigestObj=FileDigest(os.listdir('sampleDocs'))
# instantiate object and pass list of files to examine

print("FILES CONTAINING WORDS WITH A")
for i in docDigestObj.checkFor_a(): # loop through returned list
    print(str(i))
