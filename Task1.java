package techChallenge;

//finds all documents in the specified folder, that contain the character 'a'

import java.io.File;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.HashMap;

public class Task1 {

	static HashMap<String, String> documentContents =  new HashMap<>();
	static HashMap<String, String [] > documentLines =  new HashMap<>();
	static ArrayList<String> documentsWithCharacter = new ArrayList<>();//arraylist will contain names of all documents with the character 'a'
	
//all the files to be read are taken to be in the 'InputFiles' folder in drive F
	static File f = new File("F:\\InputFiles\\");
	
	public static void main(String[] args) {
		//reading all the files in the input folder
		File[] files = f.listFiles();
		filesReader(files);
		//looping through all files
		for(int i=0;i <files.length;i++){
			map(files[i].getName(),documentContents.get(files[i].getName()));
			reduce(files[i].getName(),documentLines.get(files[i].getName()));
		}
		System.out.println(documentsWithCharacter);
		
		
	}
	//method to read file contents and assign them into hashmap
	//loops through all the files present in the target folder
	public static void filesReader(File [] myDocFiles){
		int docCounter = 0;
		while(docCounter<myDocFiles.length){
		FileInputStream fis;
		try {
			fis = new FileInputStream(myDocFiles[docCounter]);
			byte[] data = new byte[(int) myDocFiles[docCounter].length()];
			fis.read(data);
			fis.close();
			String str = new String(data, "UTF-8");
			
			//putting the file contents into a hashmap, and using the file name as the key
			documentContents.put(myDocFiles[docCounter].getName(), str);
			//System.out.println(str);
			docCounter++;
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		}
		
	}
	public static void map(String docKey, String docContents){
		//splitting the contents of each document to it's lines
		String[] docLines = docContents.split("\\r?\\n|\\r");
		//populate hashmap with an array of the lines
		documentLines.put(docKey, docLines);
	}
	public static void reduce(String key,String [] docLines){
		char toBeFound = 'a';
		//checks if the character 'a' exists in the line
		for(int i=0;i<docLines.length;i++){
			//if character if found in the line, the document name is added in the arraylist of the result
			//the loop then breaks. No need for further processing of document if character is found
			if(docLines[i].contains(Character.toString(toBeFound))){
				documentsWithCharacter.add(key);
				break;
			}
			else{
				//print statement for debugging purposes
				System.out.println("not found in doc "+ key);
			}
		}
	}
}
