import os
import sys


class DocFinder:
    """
    Class that finds documents containing the letter a

    """
    def __init__(self, path):
        """Constructor method for DocFinder

        Arguments:
            path {Str} -- path to the directory containing required files
        """
        self.path = path

    def run(self):
        """Prints out the filenames of documents containing the letter a
        """
        for file in self.valid_files():
            print(file)

    def valid_files(self):
        """Generator that yields files containing a
        """
        for file in self.get_files_in_path():
            if self.file_contains_a(file):
                yield file

    def get_files_in_path(self):
        """Generator that yields all files in the specified path
        """
        if not self.path:
            raise Exception('Empty path')
        for r, _, f in os.walk(self.path):
            for file in f:
                if ".txt" in file:
                    yield os.path.join(r, file)

    @staticmethod
    def file_contains_a(file_name):
        """Returns true if a file contains the letter a

        Arguments:
            file_name {Str} -- file name of the document to search
        """
        with open(file_name) as file:
            content = file.read()
            return 'a' in content

if __name__ == "__main__":
    args = sys.argv
    # check if any argument has been passed
    if len(args) > 1:
        path = args[1]
        doc_finder = DocFinder(path)
        doc_finder.run()
