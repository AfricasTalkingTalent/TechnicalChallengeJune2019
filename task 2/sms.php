<?php
require 'vendor/autoload.php';
use AfricasTalking\SDK\AfricasTalking;

//This is to get information posted on the DB 
/* function get_information(){
    $host="dannextech.com";
    $user="dannexte";
    $pass="*******";
    $db="dannexte_asiko";
    
    // Create connection
    $conn = new mysqli($host, $user, $pass, $db);
    // Check connection
    if ($conn->connect_error) {
        die("Connection failed: " . $conn->connect_error);
    }
    
    $sql = "SELECT DISTINCT * FROM info";
    $result = $conn->query($sql);

            if ($result->num_rows > 0) {
                return $result;
            } else {
                return "nothing";
            }
            $conn->close();
}*/

// Set your app credentials
$username   = "atchallenge";
$apiKey     = "577a7efee0c3d05b825e0d0fe112d09fb92d0df79431e8a6e844b4db31988803";

// Initialize the SDK
$AT         = new AfricasTalking($username, $apiKey);

// Get the SMS service
$sms        = $AT->sms();

// Set the numbers you want to send to in international format
$recipient = "";// gets number from database created

// Set your message
$message    = "Account created successfully with username:" $username "and email:" $email;

// Set your shortCode or senderId
$from       = "User_reg";

try {
    // Thats it, hit send and we'll take care of the rest
    $result = $sms->send([
        'to'      => $recipient,
        'message' => $message,
        'from'    => $from
    ]);

    print_r($result);
} catch (Exception $e) {
    echo "Error: ".$e->getMessage();
}