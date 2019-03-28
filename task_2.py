'''
Author: Stephen Mwanzi
SDK: Africa's Talking Python SDK
Modules Used: [africastalking, flask, make_response, request]
This is test Two for the Africa's Talking Internship Challenge
for the June 2019 - Aug 2019 cohort. This pyhton application
simulates a ussd + sms application that allows the user to register 
when they provide a name and email
'''
import os
import africastalking
import flask
from flask import make_response, request


def main():
    #connect to the sandbox app using the generated api key
    africastalking.initialize('sandbox', 'a54b964872e30496e7b9301c6e982c21802e00dfcde9e9b8c6b4fd51b25cf0da')
    sms = africastalking.SMS

    def on_finish(error, data):
        if error is not None:
            raise error

        print('\nAsync Done with -> ' + str(data['SMSMessageData']['Message']))

    # Send SMS asynchronously
    sms.send('Hello Async', ['+254706451438'], callback=on_finish)
    print('Waiting for async result....')
    # Send SMS synchronously
    result = sms.send('Hello Sync Test', ['+254706451438'])
    print('\nSync Done with -> ' + result['SMSMessageData']['Message'])

def ussdSession():
    africastalking.initialize('sandbox', 'a54b964872e30496e7b9301c6e982c21802e00dfcde9e9b8c6b4fd51b25cf0da')
    sms = africastalking.SMS

    #query the string parameters that are sent by the user to initialize the application
    sessionId   = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phoneNumber = request.values.get("phoneNumber", None)
    text        = request.values.get("text", None)

    textArray    = text.split("*") if text else text
    userResponse = textArray[-1] if isinstance(textArray, list) else text


    #imagine this is a kabambe user interacting with the system
    initialize = "CON welcome to our service"
    print("please reply with your name and email separated by a comma to register")
    name = input("enter your name: ")
    type(name)
    email =input("enter your email: ")
    type(email)

    if name != "" and email != "":
        user_details = {name,email}
        success = True
        #send them a success sms synchronously
        result = sms.send('You have successfully registered. May the gods of Egypt keep you happy', ['+254706451438'])

    print("Thank "+ str(name) + " for joining us")
  
    if name == "" or email == "":
        print("registration not successful")
        #Send them a regret sms synchronously
        result = sms.send('Oops, a bad spell was cast upon us. Your registration went regretfully wrong!', ['+254706451438'])
    kill = "END"
 

if __name__ == "__main__":
    main()
    ussdSession()