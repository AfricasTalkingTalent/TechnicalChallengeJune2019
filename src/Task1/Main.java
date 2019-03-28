
/******************************************************************************
 *  Compilation:  javac Searcher.java Main.java
 *  Execution:    java Main a File [...]
 *
 *  Reads in string a, a number of files and
 *  searches for the pattern in the input files
 *
 ******************************************************************************/

package Task1;

import static java.lang.System.exit;

public class Main {

    public static void main(String[] args){


        if (args.length < 2 || !args[0].equals("a")) { // if statement checks if args array length is less than 2 or if the value in the first index of the array is not letter a
            System.out.printf ("%s %s %s%n", "Usage:", "a", "FileName [...]"); // prints usage if false
            exit(1); //method terminates the currently running Java Virtual Machine with status code 1.
        }
        Searcher searcher = new Searcher(args[0], args); // Creates a new Searcher object and passes in the first argument and the length of the array
        searcher.Algo(); // searcher instance calls Algo method

    }
}
