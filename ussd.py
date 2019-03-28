#!/usr/bin/env python

from flask import Flask, request, session, g
ussd = Flask(__name__)

import os
ussd.secret_key = os.getenv('SECRET_KEY', 'AfricasTalkingRocks')

import africastalking
import re
import sms
import strings

#Initialize some variables to store values which we can send
#back to our SMS script
response = ""

@ussd.route('/', methods=['POST'])
def ussd_callback():
    global response

    """ 
    : This block of code was meant to create session parameters
    : so that I could use loops to cerate a better user experience
    : and validate data, but sessions aren't persisting over requests
    : for some reason.

        if not 'attempts' in session:
            session['attempts'] = 0

        if not 'name_pending' in session:
            session['name_pending'] = True
    """
    
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")

    """
    :Blocks with session variables

    if (session['attempts'] < 3):
        if(text == ''):
            response = strings.name_request
        elif(session['name_pending'] and not re.match(r'[A-Za-z]',text)):
            response = strings.incorrect_name_request + str(session['attempts'])
            print(text)
            session['attempts'] += 1
        elif(session['name_pending'] and re.match(r'[A-Za-z]',text)):
            name = text
            response = strings.email_request
            session['attempts'] = 0
            session['name_pending'] = False
        elif(not re.match(r'(\w+[.|\w])*@(\w+[.])*\w+',text)):
            response = strings.incorrect_email_request
            session['attempts'] += 1
        else:
            email = text
            response = strings.session_end
            print(phone_number, name, email)
    else:
        response = strings.incorrect_session_end 

    """

    #Request all information in 1 request and keep our fingers crossed
    #that data is valid
    if text == '':
        response = strings.name_request_both
    else:
        response = strings.session_end
    
    sms.send_sms(text, phone_number)

    return response

if __name__ == '__main__':
    ussd.run(host="0.0.0.0", port=os.environ.get('PORT'))