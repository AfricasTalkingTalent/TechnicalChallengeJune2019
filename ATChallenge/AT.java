/*******
Name: Kenneth
lLanguage: java

Task #1: Version 1 using java
I used java's OOP to implement this. It takes a root folder, find all the files in it,
reads through the files/docs and returns the files which have the character 'a'/'A'

I compiled and ran the program on Codio, Ellipse, Sublime

The sample main method returns the files containing 'a' from this project, ie the root path
is for this folder

What I could have done better:
  --Use of Map, Filter, Reduce, and Predicate properties of Java 8
  --Use of a Functional programming language instead of OOP. 
  --I hope to get better at Functional Programming and will be learning this earnestly

******/

import java.nio.*;
import java.io.*;
import java.util.*;
import java.util.stream.Stream;
    
public class AT {
  
  
    //finds all the files given a flder/file path
    public  static List<File> allFilesIn(File folder) throws NullPointerException {
        
        List<File> files = new ArrayList<File>();
        for(File f : folder.listFiles()) {
            if(f.isDirectory()){
                files.addAll(allFilesIn(f));
            } 
            else if(f.isFile()) {
                files.add(f);
            }
            else{
              System.out.println("Error here, exception thrown");
              throw new NullPointerException();             
            }
              
        }
        return files;  //returns list of files
          
    }
  
    //calls the helper boolean method below it    
    public static List<File> onlyFilesWithLetterA(List<File> files) throws IOException {
        
        List<File> result = new ArrayList<File>();
        for(File fi : files) {                     
            if(containsA(fi)){
                result.add(fi);
            }            
        }
        return result; //result is list of files
        
    }
    
    //boolean method to check for foles with 'a'
    public static boolean containsA(File file) throws IOException{
        
        List<String> words = new ArrayList<String>();
        BufferedReader reader = new BufferedReader(new FileReader(file));
        String line;
        String line2 = "";
        
        while( (line = reader.readLine()) != null) {
            line2 += line;
        }
        for(int i=0; i < line2.length(); i++){
                char ch = line2.charAt(i);
                if( (ch == 'a') || (ch == 'A') ){
                    return true;                    
                }
                else{
                    continue;
                }                    
            }                
        return false;
                
    }
    
  //sample main method, which tests on this projetc's files 
    public static void main(String [] args) throws IOException  {
                         
        List<File> allFiles = allFilesIn(new File("."));
        List<File> aFiles = onlyFilesWithLetterA(allFiles);        
        
        for (File s : aFiles) {
          System.out.println(s); //prints files with the letter 'a' in them
        }
                        
    }            
            
}