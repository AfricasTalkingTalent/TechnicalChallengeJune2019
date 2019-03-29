//Set up app credentials
const credentials = {
  apiKey: "API_KEY_GOES_HERE",
  username: "USERNAME_GOES_HERE"
};

//Initialize the SDK
const AfricasTalking = require('africastalking')(credentials);

//Get the SMS service
const sms = AfricasTalking.SMS;

//send the SMS
const sendMessage = () => {
  const options = {
      // the numbers that you want to send to in international format
      to: ['YOUR_PHONE_NUMBER_GOES_HERE'],
      // the message
      message: "Congratulations on your registration. You can access our services at the convenience of your mobile phone even without an internet connection.",
      from: '16905'
  }

  //That's it, hit send and we'll handle the rest

  sms.send(options)
      .then((response) => {
          console.log(response);
      })
      .catch((error) => {
          console.log(error);
      });
};

//Call the function
sendMessage();