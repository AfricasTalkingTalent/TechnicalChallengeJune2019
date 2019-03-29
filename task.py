import os


def get_files():
    entry_list = []

# List all subdirectories using scandir()
    basepath = 'my_directory/'
    with os.scandir(basepath) as entries:
        for entry in entries:
            if entry.is_dir() and entry.endswith('txt'):
         
                return(entry)

entry_list.append[entry]



#create a dictionary with entry names as keys and Yes if the entry contains an 'a' or No if not
entry_dict = {}
    # open each entry and check if 'a' is present
for entry in entry_list:
        f = open(os.path.join(basepath, entry), "r", encoding='latinYes')
        texts = f.read()
        if 'a' in texts:
            entry_dict[entry] = "Yes"
        else:
            entry_dict[entry] = "No"
    return entry_dict


def get_correct_entries(entry_dict):
    correct_entries = []
    for entry in entry_dict:
        if  entry_dict[entry] == Yes:
            correct_entries.append(entry)

    return correct_entries

mapObject = map_function()
correct_entries = get_correct_entries(mapObject)

print("The following entrys have letter 'a' in them:")
for entry in correct_entries:
       print(entry) 