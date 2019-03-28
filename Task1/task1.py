# reading all a in a single file
searchFile = open( "myFile.txt", "r" )
# loop through all lines in the file given
for line in searchFile:
    #check if a is in line
    if 'a' in line:
        print (line);
#closes the file
searchFile.close();
