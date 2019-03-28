import re
#in-built python package to work with regular expressions
def Document_Finder(doc_list):
    #doc_list is a list containing hundreds of documents 
    new_list=[]
    # new_list will contain all the documents with words containing 'a' in them
    for document in doc_list:
        with open(document, 'r') as handle:
            data = handle.read()
            #data is text within the document
            x = re.findall('a*', data)
            #x will contain all the occurances of a
            if x is not None:
                new_list.append(document)
    return new_list  
          
