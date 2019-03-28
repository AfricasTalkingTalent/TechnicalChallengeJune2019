#!/usr/bin/env python

import os
import africastalking


def send_sms(name, phone_number, email):
    africastalking.initialize(os.getenv('USERNAME', 'sandbox'), os.getenv('API_KEY', 'f29a3c192d68ab1ab466793e7907ab4d88bb58a4363c66578cb768b94a1b1599'))
    sms = africastalking.SMS
    text = "Hi"
    text += name.split(' ')[0]
    text += "\nYou have been successfully registered with the email "
    text += "some_email.com"

    def sms_finish(error, data):
        if error is not None:
            raise error
        
        print('\n Message successfully sent!')
        print('\n Message:' + str(data['SMSMessageData']['Message']))

    #Using asynchronous technique...
    sms.send('Hello Async', [phone_number], callback=sms_finish)
    print('Sending message....\n')