
'''
Name: Kenneth
Task #2: Python version
Language: Python

Used Map, Reduce functions.
While java is my main language of instruction, I hope to get better at Python.
The logic here is same as in my Java program, but with diferent implementation.


Compiled in PyCharm, sublime

'''



import os

'''
Create a MapReduce Object with Map and Reduce functions 
'''


class MapReduce(Object):
    def __init__(self, map_tasks, reduce_tasks, file_paths):
        self.file_path = file_paths
        self.map_tasks = map_tasks
        self.reduce_tasks = reduce_tasks


    def input_split():
        file_size = os.stat(self.file_path).st_size
        chunk_size = round(file_size/map_tasks) + 1 #Offset to cater for


    '''
    parses a python-parsable file at file_path for the lowercase character "a"
    returns True
    '''
    def parse_file(self, file_path):
        try:
            f = open(file_path, "r")
            buffer = f.read()
            f.close()
            return (file_path, 1) if "a" in buffer else (file_path, 0)
        except:
            throw(ValueError("File is not parsable"))

    '''
    returns a list of (key, value) pairs 
    key: document path 
    value: 0/1 indicative of whether it has character "a" lowercase in it
    '''
    def do_map(self, file_paths):
        return map(parsse_file, file_paths)

        
    '''
    Returns a list of file_paths that contain the lowercase "a" in it 
    '''
    def do_reduce(self, to_reduce):
        valid = reduce(lambda: x[1] == 1, to_reduce)
        return map(lambda x: x[0], valid)



