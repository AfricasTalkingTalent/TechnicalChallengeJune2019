<?php
//composer dependencies
require 'vendor/autoload.php';
use AfricasTalking\SDK\AfricasTalking;

// Reads the variables sent via POST
$sessionId   = $_POST["sessionId"];
$serviceCode = $_POST["serviceCode"];
$phoneNumber = $_POST["phoneNumber"];
$text        = $_POST["text"];



//This is the first menu 
if ( $text == "" ) {
    $response  = "CON Welcome Client, Please Register \n";
    $response .= "1. Enter your Username \n";    
}



// Menu after inputing username
else if ($text == $text) {
    $response  = "CON Email Address \n";
    $response .= "1. Enter your email address\n";
}


//Message after user finishes registration
else if ($text == preg_replace('/^[a-zA-Z0-9]+$/', $str)){
    $response = "Successfully Registered\n";
}

// Print the response onto the page so that our gateway can read it
header('Content-type: text/plain');
echo $response;


////SMS Section

$username   = "sandbox";
$apiKey     = "0c874ea406208f3ae1f2c1336f09db60772a139dd57b5ea30c72662e0e5c71b4";

// Initialize the SDK
$AT         = new AfricasTalking($username, $apiKey);

// Get the SMS service
$sms        = $AT->sms();

// Recepients mobile number
$recipients = $phoneNumber;

// message
$message    = "You have registered successfully"; 

// Set your shortCode or senderId
$from       = "5ukuma";

try {
    $result = $sms->send([
        'to'      => $recipients,
        'message' => $message,
        'from'    => $from
    ]);

    print_r($result);
} catch (Exception $e) {
    echo "Error: ".$e->getMessage();
}


?>

