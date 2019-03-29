import os
entry_list = []
entry_dict = {}
# List all subdirectories using scandir()


def get_documentss():
    basepath = 'my_directory/'
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_dir() and entry.endswith('txt'):
         
                return(entry)

    entry_list.append[entry]


# create a dictionary with documents names as keys and Yes" if the documents 
# contains an 'a' or No if not
  
    # open each documents and check if 'a' is present
    for entry in entry_list:
        # open documents in current directory
            
            f = open(os.path.join(basepath, entry), "r") 
            texts = f.read()
            if 'a' in texts:
                entry_dict[entry] = "Yes"
            else:
                entry_dict[entry] = False
                return entry_dict


def get_correct_entries(entry_dict):
    Correct_entries = []
    for documents in entry_dict:
        if entry_dict[documents] == "Yes":
            Correct_entries.append(documents)

    return Correct_entries


entryObject = get_documentss()
Correct_entries = get_correct_entries(entryObject)

print("The following documentss have letter 'a' in them:")
for documents in Correct_entries:
    print(documents) 