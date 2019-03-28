
# HOW TO RUN


>run parser.py providing a directory with documents to parse. for example;

```sh
$python parser.py C:\Users\Davis\Documents
```

# Implementation

## class: Parser

The Parser class defines methods for looking up files in a directory and 
parsing their contents checking if letter "a" is present.

#### methods defined:

##### get_files_in_dir(self, dir_path)
searches for files in a directory i.e dir_path. Returns a list of all files found.

##### text_file_parser(self, file)
parses text(.txt) files. Checks if a text file has letter 'a'

##### pdf_file_parser(self, file)
parses pdf(.pdf) files. Checks if a pdf file has letter 'a'











