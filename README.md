# TASK TWO - AT TECHNICAL CHALLENGE 2019

A simple USSD + SMS app that does user registration. Makes use Africa's talking APIs for USSD and Bulk SMS.


## PREREQUISITES
The following should be installed before running the code:
  -python 3.6+
  -Flask mini web framework
     ```
    pip install Flask
    ```
  -flask_ngrok
      ```
    pip install flask-ngrok
    ```
  -africastalking API

## RUNNING
-Open the code in a code editor of your choosing
-Assign your Africastalking API key as a string to the variable api_key

-Once you run the code, ngrok will start
![ngrokStart](ngrokInPycharm.jpg)
 
-Copy the second URL and use it as your callback URL on your Africa’s talking USSD channel
 
-You can track the requests coming in from your app on the traffic stats URL provided by ngrok
 
-Africa’s Talking Sandbox + Simulator have been used for testing













