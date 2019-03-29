# Program: findDocs.py
# Problem statement: write a program that given hundreds of documents, 
# can find all documents with words containing the letter "a" in them.


def findDocs(documents, target):
    """ Finds all documents with letter target
    @documents is list of all documents. 
    @target is letter being searched for.
    """
    # traverse documents searching for target letter 
    filtered_docs = filter(lambda doc : target in open(doc, 'r').read(), documents)
    # coerce result into list of docs 
    result = list(filtered_docs)
    return result


# # main gets documents as a list 
# # calls findDocs. 
# def main():
#     target = 'a' # letter to search for

#     documents = ['a.txt', 'b.txt']
#     print(findDocs(documents, target))
# if __name__ == '__main__':
#     main()