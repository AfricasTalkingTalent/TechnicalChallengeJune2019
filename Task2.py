import africastalking
from flask import Flask, request
import re

#initialize SDK, app and create credentials
app = Flask(__name__)

username = "sandbox"
apikey = "72f179590b354ee62b81bc0127ef268d2dfd2a2a17a6713a91f5070b6fc8c9e3" 

africastalking.initialize(username, apikey)

sms = africastalking.SMS


#route 
@app.route('/')

response = ""

#Send the SMS
def sendconfirmation(message, recipients, sender):
    
    try:
        response = sms.send(message, recipients, sender)
        print(response)
    except Exception as e:
        print(f"The message can't be sent because {e}")


@app.route('/', methods=['POST', 'GET'])
def ussd_callback():

    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    text = request.values.get("text", "default")
    phone_number = request.values.get("phoneNumber", None)

#use regex to validate spacing of the username
    usernamePattern1 = re.compile("\w+\s\w+")
    usernamePattern2 = re.compile("\w+")

#ask user to input their name
    if text == '':
        response  = "CON Please enter your user name\n"
        
#then ask user to input their email address
    elif usernamePattern1.match(text) or usernamePattern2.match(text):
        response = "CON Please enter your email address\n"
    else:
        response  = "END You will receive an sms confirmation shortly\n"
        sendconfirmation([phone_number],"Registration Successful!",service_code)

  return response
