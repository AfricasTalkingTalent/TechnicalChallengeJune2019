public class Main {
	/*
	 * public static void main(String[] args)
	 * args -> takes in a string of arguments from the commandline when running the program.
	 * Be sure to provide a string of filenames as arguments separated by spaces.
	*/
	public static void main(String[] args) {
		
		//Creates an instance of the File finding class
		FindFile findFile = new FindFile();
		
		//Calls the foundFile method inside the findFile method which returns an array of all found files
		String[] found = findFile.foundFile(args);
		
		//Prints all documents where 'a' was found
		for(String s : found)
			if(s!= null)
				System.out.println(s);
	}
}