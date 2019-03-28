<?php

namespace ATChallenge\Http\Controllers;

use ATChallenge\User;
use Illuminate\Http\Request;

class USSDController extends Controller
{
    public function index(Request $request){
		// Extract post data

        $session_id = $request->sessionId;
        $service_code = $request->serviceCode;
        $phone = $request->phoneNumber;
        $text = $request->text;

        $text = trim($text); // Remove any spaces at the beginning or end of the string

        $continue_session = "CON ";
        $end_session = "END ";

        $response = "";
        if($text == ""){
            //Session start
            $response = $continue_session."Enter a username:\n";
        }else if(substr_count($text, "*") == 0){
            // User has entered username
            // Check if the username exists

            if(User::where('username', $text)->exists()){
                $response = $end_session."The username exists!\n";
                //$response .= "Try another:\n";
            }else{
                $response = $continue_session."Enter your email:\n";
            }
        }else if(substr_count($text, "*") == 1){
			// User has entered their email address
            $data = explode("*", $text);  // Split the string into username and email
            $username = trim($data[0]);
            $email = trim($data[1]);

            if(User::where('email', $email)->exists()){ // Ensure no email duplicate occurs
                $response = $end_session."The email exists!\n";
                //$response .= "Try another\n";
            }else{
                $user_data = [
                    "username"=> $username,
                    "email"=> $email,
                    "phone"=> $phone
                ];
                User::create($user_data);  // Save user in the database
                $response = $end_session."You have registered successfully!";  // End session
            }
        }else{
            $response = $end_session."Incorrect input!";
        }

        return $response;
    }

}
