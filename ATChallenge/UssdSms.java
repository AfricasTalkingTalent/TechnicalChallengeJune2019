/****
Name: Kenneth
I compiled and ran the program on Codio, and Eclipse, and Sublime.

Language: java
 
Task 2:
The online tutorials on the at website were helpful, but unfortunately
some of them did not have Java implementation. 
Somehow, I could not get the SandBox and the simulator to run my code, since I did
not have enough time to interact with africastalking interfaces. 

However, below is Java code which would simulate the underlying customer process 
in Task #2. 

It essesntially uses a Scanner to ask for imput and gives the customer necessary 
feedback on their information.

Assumption:

--The user knows the USSD number beforehand.
--User knows their credentials well enough

With more time, I would:
--Check for some exceptional cases
--Implement the Africastalking underlying code on sms, messages, and USDs
--Use the simulator
****/


import java.util.*;


public class UssdSms {
    
    public static void main (String [] args) {
        
        Scanner input = new Scanner(System.in);
        
        System.out.println("Please enter the USSD code: ");
        String ussd = input.next();
                
        //check if USSD is a 4-digit Number
        if(isAllDigits(ussd) == false || ussd == null || ussd.length() != 4){
            System.out.println("Kindly enter the 4 digits of the USSD code");
            ussd = input.next();
        }    
        else{
            ;
        }
         
        //Ask for email
        System.out.println("Please enter your email address: ");
        
        String email = input.next();
        
      //Ask for username
        System.out.println("Please enter your username: ");
                    
        String username = input.next();        
        
        //Confirm the credentials   
        if(email == null || username == null){
            System.out.println("Please start enter your credentials correctly: ");
            username = input.next();
        }else{
            ;
        }
      
        
        
        System.out.println("Kindly confirm that this is your email adress and username ");
        System.out.println("EMAIL: " + email);
        System.out.println("USERNAME: " + username);
        
        System.out.println("If credentials above are correct, press 1. If not, press any digit number");
        
        int pressedNo = input.nextInt();
        
      
        if(pressedNo != 1)  {
            System.out.println("Please try again. Thank you");  
        }
        else{
            System.out.println("Thank you. You are successfulyy registered");
        }
      
        
    }
    
    //Boolean method to check whether the USSD is all Iteger values
    public static boolean isAllDigits(String character) { 
        
        try {
            Integer.parseInt(character);
            return true;
        }catch(NumberFormatException nfe) {
            return false;
        }
               
        
    }
    
}