"""Regular expressions used for describing a search Pattern
When working with files/Documents"""
import re

'''A List containing a sample data of documents'''
documents_list = ['At.txt', 'Atlabs.pdf', 'doc.odt', 'resume.ppt']

'''A Function to help find documents with words with letter a in them'''
def get_docs(documents_list):
    '''An empty list which we shall append to later on. Will contain all
    documents with words that have letter a'''
    docs_with_wordswithlettera = []

    '''Loop through all documents in the document_list'''
    for document in documents_list:
        with open('at.txt', 'r') as f:
            data = f.read#Open and read data in every file at a time looping through each document.
            y = re.findall(r'a', documents_list)#Iterate through words documents to find those with letter a
            if y is not None:#After iteration, if a document contains a word with letter a in it,
                docs_with_wordswithlettera.append(document)#Add the document to the empty list
    return docs_with_wordswithlettera
