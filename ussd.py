#!/usr/bin/env python

from flask import Flask, request, session
ussd = Flask(__name__)

import os
ussd.secret_key = os.getenv('SECRET_KEY', 'AfricasTalkingRocks')

import africastalking
import sms
import re

#Initialize some variables to store values which we can send
#back to our SMS script
response = ""
name = ""
email = ""
phone_number = ""

@ussd.route('/', methods=['POST'])
def ussd_callback():
    if not 'attempts' in session:
        session['attempts'] = 0

    if not 'name_pending' in session:
        session['name_pending'] = True

    print(session)
    global response
    
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default").split('*')[-1]

    if (session['attempts'] < 3):
        if(text == ''):
            response = name_request()
        elif(session['name_pending'] and not re.match(r'[A-Za-z]',text)):
            response = incorrect_name_request() + str(session['attempts'])
            print(text)
            session['attempts'] += 1
        elif(session['name_pending'] and re.match(r'[A-Za-z]',text)):
            name = text
            response = email_request()
            session['attempts'] = 0
            session['name_pending'] = False
        elif(not re.match(r'(\w+[.|\w])*@(\w+[.])*\w+',text)):
            response = incorrect_email_request()
            session['attempts'] += 1
        else:
            email = text
            response = session_end()
            print(phone_number, name, email)
    else:
        response = incorrect_session_end()  
    return response

#Functions for input prompts
def name_request():
    return "CON Hi there, please enter your name (alphabets only)...\n"

def incorrect_name_request():
    return "CON You seemed to have entered a wrong name. Try Again\n"

def email_request():
    return "CON Please enter your email address now.\n"

def incorrect_email_request():
    return "CON That's an incorrect email address. Try again...\n"

def session_end():
    return "END Thank you for your input. Our message is just arriving.\n"

def incorrect_session_end():
    return "END Too many attempts, try again later\n"

if __name__ == '__main__':
    ussd.run(host="0.0.0.0", port=os.environ.get('PORT'))