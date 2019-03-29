import java.util.*;
import java.io.*;

public class ussd {

 private static String email;
 private static String username;
 private static String phoneno;
 private static boolean requestsuccessful;
 
 
 public static void main(String[] args) {

  //Read USSD code
  Scanner scanner = new Scanner(System.in);
  
  // Request USSD type
  System.out.println("Enter the USSD code");
  String ussd = scanner.nextLine();

  // Request email
  System.out.println("Please enter email");
  String em = scanner.nextLine();
  
  // Request username
  System.out.println("Please enter username");
  String user = scanner.nextLine();
  
  // Request phone number
  System.out.println("Please enter phone number");
  String number = scanner.nextLine();


  //Implement using the needed request, and register user. 
  //All valid request types would ideally be in this if else block but I used *144# only
  if (ussd.equals("*144#")) {
  
   userregisteration(em, user, number);
   System.out.println("Registration Successful!");
   
  } 
  
  else { 
  
  System.out.println("Registration Unsuccessful! System can only support *144# request"); 
  
  }
  
  //In case of an error outside the system, use false to update the session's status.
  //We will assume that the request is successful 
  updatemobileserviceprovider(true);
 }

 public static void userregisteration(String emailaddress, String name, String phonenumber) {
 
  email = emailaddress;
  username = name;
  phoneno = phonenumber;
  
 }
 
 public static void updatemobileserviceprovider(boolean success) {
  requestsuccessful = success;

 }
}