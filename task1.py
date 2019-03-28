def contains_a(documents):
    # filter goes through the list of documents provided.
    # for each:
    # 1. opens the file to be read => open(x,"r")
    # 2. gets the content of each file => (open(x,"r")).read()
    # 3. checks if 'a' is in the contents => 'a' in (open(x,"r")).read()
    # 4. based on this boolean, returns a list of files that returned true from step 3
    return list(filter(lambda x: 'a' in (open(x,"r")).read(), documents))
