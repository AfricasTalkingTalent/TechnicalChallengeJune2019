import africastalking
from flask import Flask, request
import re

#Create your credentials
username = "sandbox"
apikey = "e02f74dbffdcdfc13d356890e7dfff3769f5e8c0b2dd92b2d98b81989dabb5d3"

#Initialize the SDK
africastalking.initialize(username, apikey)

#Get the SMS service
sms = africastalking.SMS

app = Flask(_name_)

response = ""


def sendconfirmation(recipients, message, sender):
    #Send the SMS
    try:
        #Once this is done, that's it! We'll handle the rest
        response = sms.send(message, recipients, sender)
        print(response)
    except Exception as e:
        print(f"message wasn't sent because {e}")



@app.route('/', methods=['POST', 'GET'])
def ussd_callback():

    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")
    #used regex to check that user name was either a single word or two words separated by a space
    usernamePattern1 = re.compile("\w+\s\w+")
    usernamePattern2 = re.compile("\w+")

    # asks user to enter their name
    if text == '':
        response  = "CON Enter your user name\n"
    # after entering their name ask the user to enter their email address
    elif usernamePattern1.match(text) or usernamePattern2.match(text):
        response = "CON Enter your email address\n"
    else:
        response  = "END You will receive an sms confirmation shortly\n"
        sendconfirmation([phone_number],"You have successfully registered",service_code)

  return response
