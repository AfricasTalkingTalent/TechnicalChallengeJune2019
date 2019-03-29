
<?php
function get_information(){
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
}
	  
// Reads the variables sent via POST from our gateway
	$sessionId   = $_POST["sessionId"];
	$serviceCode = $_POST["serviceCode"];
	$phoneNumber = $_POST["phoneNumber"];
	$text        = $_POST["text"];
	if ( $text == "" ) {
	     // This is the first request. Note how we start the response with CON
	     $response  = "CON Welcome to USSD registration! Please enter your username:\n";
	}
	else if ( $text == "" ) {
	  // Business logic for first level response
	  $response = "CON Username successfully registered. Please enter email address: \n"; 
	  
	 }
	 else if($text == "1*1") {
	  // This is a second level response where the user selected 1 in the first instance
	  //$accountNumber  = "ACC1001";
	  // This is a terminal request. Note how we start the response with END
	  $result = "Thank you for registering. Confirmation message coming soon."
	  
	 }
	//
	// Print the response onto the page so that our gateway can read it
	header('Content-type: text/plain');
	echo $response;
	// DONE!!!
?>