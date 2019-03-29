import os, sys
import slate3k

class Parser:
	""" 
	defines methods for looking up files in a directory and 
	parsing their contents checking if letter a is present.

	Initialization variables:
	self.dir_path : an absolute path to the directory to get files from for parsing. 

	methods defined:

	1. get_files_in_dir(self, dir_path) : searches for files in a directory i.e dir_path. Returns a list of all files found.
	2. text_file_parser(self, file) : parses text(.txt) files. Checks if a text file has letter 'a'
	3. pdf_file_parser(self, file) : parses pdf(.pdf) files. Checks if a pdf file has letter 'a'
	"""
	def __init__(self, dir_path):
		self.dir_path = dir_path
		self.files_containing_letter_a = []

	def get_files_in_dir(self):
		"""
		returns files_list : a list of all files in a given directory
		"""

		files_list = []

		# check if what the user provides is indeed a directory
		try:
			if os.path.isdir(self.dir_path):
				#check and append any file in the directory to the file_list
				for item in os.listdir(self.dir_path):
					#is it a file? 
					if os.path.isfile(os.path.join(self.dir_path, item)):
						#append full file path to the files_list
						files_list.append(os.path.join(self.dir_path, item))
			else:
				#what the user provided is not a directory! 
				raise ValueError('Error: Please provide a valid directory name;\nAn absolute path to a directory is required')

		except Exception as e:
			print(e)		

		return files_list			

	def text_file_parser(self, file):
		"""
		parses .txt files for letter a

		file: a text(.txt) file
		""" 

		print(f'\nOpenning {file} for parsing')		
		try:
			with open(file, 'r') as f:
				#read one line at a time (more efficient than loading whole file)
				for line in f:
					for word in line.split():
						if 'a' in word:
							#add file to files with letter a
							self.files_containing_letter_a.append(file)
							raise Exception('letter "a" found! Break away and parse next file')
		except Exception as e:
			print(e)


	def pdf_file_parser(self, file):
		"""
		parses .pdf files for letter a

		file: a text(.txt) file
		""" 			

		print(f'\nOpenning {file} for parsing')
		try:
			with open(file, 'rb') as f:
				#load pdf file
				pdf_file = slate3k.PDF(f)

				#loop through pdf_file pages searching for letter a
				for page in pdf_file:
					for line in page.split():
						for word in line:
							if 'a' in word:
								#add file to files with letter a
								self.files_containing_letter_a.append(file)
								raise Exception('letter "a" found! Break away and parse next file')	 
		except Exception as e:
			print(e)						



if __name__ == '__main__':

	#get absolute directory from command line argument variables 
	try:
		dir_path = sys.argv[1]
		#create a Parser object
		parser = Parser(dir_path)

		# get files in a directory
		print(f'Attempting to fetch all files in "{parser.dir_path}"')
		all_files = parser.get_files_in_dir()

		#call relevant file parser method for a given file type 
		for file in all_files:
			#text file
			if file.endswith('txt'):
				parser.text_file_parser(file)

			#pdf file 
			elif file.endswith('pdf'):
				parser.pdf_file_parser(file)

			#unsupported file e.g '.exe' 
			else:
				print(f'\nskip parsing {file} usupported file type\n')		

		#check whether any files with letter a were found 
		if len(parser.files_containing_letter_a) > 0:

			print('\n\nFiles found with letter a: ')
			for f in parser.files_containing_letter_a:
				print(f)

		else:		
			print("No files found with letter a") 

	except Exception:
		print('\nplease provide an absolute directory to start parsing files\n')	

	