from glob import glob
import re

class FileDigest(object):
    def __init__(self,filesList):
        '''

        :param filesList: list of paths to all the files to be evaluated
        '''
        self.filesList=filesList


# evaluate if document is pdf or simple text file. Currently the only supported files
    def checkExtension(self,document):

        if document.lower().endswith('.pdf'):
            return 1
        elif document.lower().endswith('.txt'):
            return 2
        else:
            return False

# use regex to find out if any word contains an a.
    def checkFor_a(self,documentpath):

