#import os library to access filesystem and re for regex
import os
import re

#directory to search from
directory = '/home'
#iterating through directory to find txt and py files
for filename in os.listdir(directory):
    if filename.endswith(".txt") or filename.endswith(".py"): 
        mystring = open(filename, 'r')
        for line in re.findall(r'\w+', str(mystring)):
            if 'a' in line: 
                print ("The letter 'a' appears in the following files", filename)
                mystring.close()
        continue
    else:
        continue