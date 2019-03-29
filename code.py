"""
This is a simple script that will loop through a sample files and return 
the filenames with words containing letter 'a'
"""
import glob
import errno
import re
import ntpath

# glob is used to get the names of all files in the  directory files

allfiles = glob.glob('./files/*')

ntpath.basename("./files/")

lines = []

# ensuring we can actually see these files
print(allfiles)


# strip basename from the file
def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


# loop over these files
def check_files():
    """A method to check for existence of letter 'a' in a file"""
    for file in allfiles:
        try:
            # open each file
            with open(file, encoding="utf8", errors='ignore') as f:
                for line in f:
                    # return a list of strings/chunking the words
                    line.split()
                    # search for strings with letter a
                    if re.match(r"a", line):
                        lines.append(line)
                num_of_lines = len(lines)
                file_name = path_leaf(file)
                if len(lines) > 1:
                    print(file_name, "have" + str(num_of_lines) + "lines with letter 'a'")
                elif len(lines) < 1:
                    print(file_name, "Does not have lines with a word that contains letter 'a'")
                # remove lines from the lines array after reading a file
                del lines[:]
                return True
        except IOError as exc:
            if exc.errno != errno.EISDIR:
                raise


check_files()
