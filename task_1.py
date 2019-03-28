'''
Author: Stephen Mwanzi
Africa's Talking Technical Challenge: Test One
This is a simple program that can find all documents in a file directory
or text with words containing the letter "a" in them
'''

#import the os module to enable the app to read the directory
import os 

#specify the letter(s) that should be searched
keyword = ['a']

#get the list of all files in the books directory and save it to the list all_files
all_files = os.listdir("books/")

'''
alternatively, you can save the list
of the books in a text file and read its
contents using the open('txt_file_name','stream_mode') function
we then can save the streamed content to a string named books_titles
'''
books = open('mybooks.txt','r')
book_titles =books.read()

'''
if we read from a text file or a text string
we use this function that will split the string,
remove the double quotes and split the string with the
comma(,) as the delimiter
'''
def AT_Books(string): 
    li = list(string.split(",")) 
    return li 

#find matching books in the text string containing the search keyword
matching_books_in_text = [s for s in AT_Books(book_titles) if any(xs in s for xs in keyword)]

#find matching books in the directory that contain the search keyword
matching_books_in_directory =  [s for s in all_files if any(xs in s for xs in keyword)]

#use the str() function on the list containing the found books in order to be able to concatenate it with the preceding string
print("Books in your text-file or string that satisfied your search are: " + str(matching_books_in_text))
for x in matching_books_in_text:
    print(str(matching_books_in_text.index(x) +1) + ": " + x )

print( "Books in your directory that satisfy your search are: ")

for x in matching_books_in_directory:
    print(str(matching_books_in_directory.index(x) +1) + ": " + x )