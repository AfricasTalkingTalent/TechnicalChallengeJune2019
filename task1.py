import os

# Define our class
class Task1:
    
    # Instance attriibutes eg. we have a documents_list which is an empty array,
    #  File type and search term to use
    def __init__(self):
        self.documents_list = []
        self.file_type = ".txt"
        self.search_term = "a"
    
    # Search for the letter in a document. Open the letter and read it one line at a time,
    # looking for the letter "a" in it. If found output the file name, otherwise skip it.
    def getFileContent(self, file):
        with open(file, "r") as f:
            for line in f.readlines():
                if self.search_term in line:
                    return print("\t" + file)
    
    # In this functuin, we get the list of all .txt files in the current directory,
    # and store them in an array. Use the os module for this
    def getDirectoryListing(self):
        # Get our curret working directory
        path = str(os.getcwd()) + "\\"
        # r=root, d=directories, f = files
        for r, d, f in os.walk(path):
            for file in f:
                if self.file_type in file:
                    self.documents_list.append(os.path.join(r, file))
        if(len(self.documents_list) > 0):
            print("\nAll the text documents in this directory with the letter \"a\"  are:")

            # Call the search function for each of the files using the map function.
            list(map(self.getFileContent, self.documents_list))
        else:
            # If no files exist
            print("Sorry, we couldn't find any text documents in this directory and its sub-directories.")


# Start of the program
if __name__ == "__main__":

    # Call the getDIrectory listing method in the Test1 Class
    Task1().getDirectoryListing()