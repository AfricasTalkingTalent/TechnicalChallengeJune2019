#!/usr/bin/env python

import os
import africastalking


def send_sms(text, phone_number):
    #Get variables or set them if the don't exist
    africastalking.initialize(os.getenv('USERNAME', 'sandbox'), os.getenv('API_KEY', '9268b9407ee6a9136b1fb6f3b7d453a68f672cd20154c639fb2d248fe5cec698'))
    sms = africastalking.SMS
    text = "Hi"
    text += "\nYou have been successfully registered with the email "

    #Callback function for asynchronous sending
    def sms_finish(error, data):
        if error is not None:
            raise error
        
        print('\n Message successfully sent!')
        print('\n Message:' + str(data['SMSMessageData']['Message']))

    #Using asynchronous technique...
    sms.send('Hello Async', [phone_number], callback=sms_finish)
    print('Sending message....\n')