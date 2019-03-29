import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
public class FindFile {
	public String[] foundFile(String[] files) {
		//Creates a new String array which returns all files with the letter 'a' in them
		String[] afound = new String[files.length];
		
		/*
		 * Iterate through all the documents passing them to the Find_a function which return
		 * the name of the file if the file contains the letter 'a' else returns null
		 */
		for(int i = 0; i < files.length; i++) {
			String s = Find_a(files[i]);
			if(s != null)
				afound[i] = s;
		}
		
		//return file names which contain letter a in them
		return afound;
	}
	public String Find_a(String file) {
		try{
			/*
			 * Creates an instance of the BufferedReader which Reads text from a character-input stream, 
			 * buffering characters so as to provide for the efficient reading of characters, arrays, and lines.
			*/
	        BufferedReader buf = new BufferedReader(new FileReader(file));
	        
	        //fetches a line from the document
	        String lineJustFetched;
	        
	        //splits the line fetched
	        String[] wordsArray;
	        while(true){
	        	//Iteratively fetches a line from the document till there's no line to be fetched
	            lineJustFetched = buf.readLine();
	            
	            // Breaks out of the for loop if theres no line to be fetched
	            if(lineJustFetched == null) 
	                break; 
	            else{
	            	//Splits the line fetched into an array of Strings
	                wordsArray = lineJustFetched.split(" ");
	                
	                //Loops through the String to find the letter 'a' and returns the filename once the letter 'a' is found
	                for(String s : wordsArray) {
	                	char[] chars = s.toCharArray();
	                	for(char ch: chars) {
	                		if(ch == 'a') {
	                			return  file;
	                		}
	                	}
	                }
	                
	            }
	        }
	        buf.close();
		}catch(FileNotFoundException e) {
			e.printStackTrace();
        }catch(Exception e){
            e.printStackTrace();
        }
		//returns null if letter 'a' is not found
		return null;
	}
}