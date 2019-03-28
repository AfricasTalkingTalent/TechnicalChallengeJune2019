<?php
// Import Africastalking SDK
require 'vendor/autoload.php';
use AfricasTalking\SDK\AfricasTalking;

// Set your app credentials
$username   = "sandbox";
$apiKey     = "YOUR_API_KEY";
$AT         = new AfricasTalking($username, $apiKey); // Initialize the SDK
$sms        = $AT->sms(); // Get the SMS service

function sendsms(){ // Thats it, hit send and we'll take care of the rest
    try {
        $result = $sms->send([
            'to'      => $phoneNumber,
            'message' => $message,
            'from'    => $from
        ]);
    
        print_r($result);
    } catch (Exception $e) {
        echo "Error: ".$e->getMessage();
    }
}

// ---------------------------------------------
// USSD START
// ---------------------------------------------

// Reads the variables sent via POST from our USSD gateway
$sessionId   = $_POST["sessionId"];
$serviceCode = $_POST["serviceCode"]; // Code dialed
$phoneNumber = $_POST["phoneNumber"]; // Recipient
$text        = $_POST["text"]; // USSD payload
$email = ""; // Email from USSD input
$username = "";// Username from USSD input
$message    = "Username: ".$username."\nEmail: ".$email; // Message
$from       = "LewisMunyi"; // Sender ID

if ($text == "") {
    // This is the first request.
    $response  = "CON Hi there. Enter your user name \n";

} else if (!filter_var($text, FILTER_VALIDATE_EMAIL)) {
    // User has entered a username
    $username = $text;
    $response = "CON Enter Username \n";

} else if (filter_var($text, FILTER_VALIDATE_EMAIL)) {
    // User has entered an email address
    $email = $text;
    sendsms();
    $response = "END An SMS has been sent to the number ".$phoneNumber."".$email."".$username;
}

// Echo the response back to the API
header('Content-type: text/plain');
echo $response;
// ---------------------------------------------
//USSD END
// ---------------------------------------------
?>