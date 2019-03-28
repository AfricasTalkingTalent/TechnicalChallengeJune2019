from glob import glob
import re

class FileDigest(object):
    def __init__(self,filesList):
        '''

        :param filesList: list of paths to all the files to be evaluated
        '''
        self.filesList=filesList


# evaluate if document is pdf or simple text file
    def checkExtension(self):
        pass

# use regex to find out if any word contains an a.
    def checkFor_a(self):
        pass
