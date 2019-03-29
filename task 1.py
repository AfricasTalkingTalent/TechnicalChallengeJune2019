#To do:
# 1. Find words in a document containing letter 'a'
# 2. Create a loop that can find words with a in multiple document
# 3. Create a list of documents that contain words with 'a'

#Imports the os module which helps navigate the underlying operating system
import os

#Created a class that will deal with the finding documents containing letter 'a'
class Document_finder:

	#This takes on the directory that holds all the documents to be analysed
    def __init__(self,directory):
        self.directory = directory
    

    def finder(self):

    	#list all the documents being evaluated
        fileList = os.listdir(self.directory)
        print(fileList)
        
        #This is an empty list that will hold all documents found with 'a'
        withA = []

        #loops through each document to find what contains 'a'
        for i in fileList:
            x = open(self.directory + i, 'r').read()
            #print(x)
            if "a" in x:
                withA.append(i)
        
        #Return the documents that have letter 'a' in them
        return withA


#Testing on a number of documents
#the program has to run on the same directory that contains the directory of all documents needed to be analysed
#object1 = Document_finder("test2/")
#object1.finder()