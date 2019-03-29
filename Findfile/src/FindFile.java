import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
public class FindFile {
	public String[] foundFile(String[] files) {
		String[] afound = new String[files.length];
		for(int i = 0; i < files.length; i++) {
			String s = Find_a(files[i]);
			if(s != null)
				afound[i] = s;
		}
		return afound;
	}
	public String Find_a(String file) {
		try{
	        BufferedReader buf = new BufferedReader(new FileReader(file));
	        String lineJustFetched = null;
	        String[] wordsArray;
	        while(true){
	            lineJustFetched = buf.readLine();
	            if(lineJustFetched == null) 
	                break; 
	            else{
	                wordsArray = lineJustFetched.split(" ");
	                for(int i = 0; i < wordsArray.length; i++) {
	                	char[] chars = wordsArray[i].toCharArray();
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
		return null;
	}
}