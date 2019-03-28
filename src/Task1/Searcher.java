package Task1;

// Regex methods statements
// Input and Output Streams

import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.io.FileReader;
import java.io.BufferedReader;
import java.io.IOException;

public class Searcher {

    private Matcher matcher;    // matcher global variable to obtain a Matcher instance from a Pattern
    private final String[] arr; // Final String array to hold the files

    public Searcher(String letter, String[] args) { // Searcher Constructor for variable initialization

        Pattern pattern = Pattern.compile(letter); // If you need to match a text against a regular expression pattern more than one time, you need to create a Pattern instance using the Pattern.compile() method
        matcher = pattern.matcher(""); // Once you have obtained a Pattern instance, you can use that to obtain a Matcher instance. The Matcher instance is used to find matches of the pattern in texts.
        arr = args;

    }

    private Matcher getMatcher() { // Accessor method

        return matcher; // returns a mathcher instance
    }

    private String[] getArr() { // Accessor method

        return arr; // returns an Array of files
    }

    public void Algo() {

        // loop statement to extract each file from the array of files
        for (String file : getArr()) {
            BufferedReader br; // reads text from a character-input stream
            String line; // variable to hold

            try {  // try catch block for buffered input stream exception
                br = new BufferedReader(new FileReader(file)); //br reads each file in the array
            } catch (IOException e) {
                System.err.println("Cannot read '" + file + "': " + e.getMessage());
                continue;
            }

            try {
                while ((line = br.readLine()) != null) {
                    getMatcher().reset(line);

                    if (getMatcher().find()) {
                        System.out.println(file + ": " + line);
                    }
                }

                br.close(); // closes the buffer reader input stream
            }catch (IOException e){
                System.err.println(e.getMessage());
            }


        }

    }

}
