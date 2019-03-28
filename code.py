
"""
This is a simple script that will loop through a sample files and return 
the filenames with words containing letter 'a'
"""
import glob
import errno
import re
#glob is used to get the names of all files in the  directory files
allfiles=glob.glob('./files/*')
#ensuring we can actually see these files
print(allfiles)
#loop over these files
for file in allfiles:
    try:
        #open each file 
        with open(file,encoding="utf8", errors='ignore') as f:
            for line in f:
                #return a list of strings/chunking the words
                line.split()
                #search for strings with letter a
                if re.match(r"a", line):
                        print(line)
            print(file)
    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise