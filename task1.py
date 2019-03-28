def filesReader(filenames):#takes in a list of filenames to read as argument
    try:#checks if the filenames passed exist
        for filename in filenames:#loops throgh all files passed
            with open('filename', 'r') as f:#opens file for reading
                content = f.readelines()#reading lines in the files
                for sentance in content:#loop throgh each line and split words
                    line = sentance.split()
                    for each in line :#loop through every word to turn it to lowercase
                        line2= each.lower()
                        for item in line2:#check if any word in file has letter a
                            if any(i in item for i in 'a'  ):
                                print(filname,'has word with letter a')
                            else:
                                print(filname,'has No word with letter a')

    except FileExistsError:#error to be thrown when file is not found
        print('the file does not exists')
