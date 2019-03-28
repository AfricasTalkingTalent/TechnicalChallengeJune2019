file_names = ['test1.txt', 'test2.txt', 'test3.txt', 'test4.txt']


class OpenFile:
    ''' context manager to manage any file operations'''

    def __init__(self, filename, mode):
        ''' A python constructor to create a file object'''
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        '''Magical method to open a file an return it'''
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exec_type, exec_val, traceback):
        '''Magical exit method that makes sure the
         file is closed outside the contex manager '''
        return self.file.close()


def contains_a():
    '''
    Loops over all file names, checks the content of each file.
    If a document has an a, its name is pushed to a result list
    '''
    res = []
    for filename in file_names:
        with OpenFile(filename, 'r') as f:
            content = f.read()
        if 'a' in content:
            res.append(filename)
    return res


print(contains_a())
