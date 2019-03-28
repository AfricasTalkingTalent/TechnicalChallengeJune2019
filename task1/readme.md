## Task 1: Find documents containing the character "a"
In this challenge I am making the following assumptions:
* The program will be offline and all the doucments to be searched are in a single directory.
* The documents are plain text files. Binary documents (e.g with extension .docx) will be ignored.
* No processing is required a part from find documents with words containing the letter "a".

The approach I used was from the thinking that if the files can be read one at a time then there would be no need to create data structures that would unnecessarily use more memory by opening all the files at once and iterating through each.

The program requires the library [BinaryOrNont](https://binaryornot.readthedocs.io/en/latest/) installed.
To run execute:
```bash
python3 check_documents.py <doucuments path>
```
If the documents are in the same directory as the program file:
```bash
python3 check_documents.py
```

At the end the program will just list the files found containing the letter "a".
