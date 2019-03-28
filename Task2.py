# This code uses flask web framework and Africa's Talking USSD api and SMS api to accept user name and email address via USSD,
#and sends an sms confirmation of successful registration
#ngrok has been used to the local host
from flask import Flask,request
from flask_ngrok import run_with_ngrok
import re
import africastalking

# Initialize SDK
username = "sandbox"
api_key = "xxxxxxxxxxxxxxxxxxxxxxxxx"  #sandbox API Key
africastalking.initialize(username, api_key)

app = Flask(__name__)
run_with_ngrok(app)  # Start ngrok when app is run


response = ""
sms = africastalking.SMS

@app.route('/', methods=['POST','GET'])
def assignment_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    #Check if text is empty after USSD code has been dialed. If empty,prompt user to input their name
    if text == ' ':
      response  = "Please Enter your name\n"

    #Check if string is empty. If not empty, check the text input for email address pattern
    elif text and text.strip():

      #use regular expresion to check if the text entered matches the pattern for an email address

      emailValidity = re.search(r"\S+@\S+", text)
      # if the text matches the pattern of an email address, send sms for successful registration
      if(emailValidity):
          #send user SMS for successful registration
          # Use the sms service synchronously
          response1 = sms.send("Hello Message!", ["+254714369514"])
          print(response1)
      #if text does not match email address pattern, prompt for user email address
      #User either input a name or an invalid email address
      else:
          response = "Please Enter your email address\n"



    return response
if __name__ == '__main__':
    app.run()
