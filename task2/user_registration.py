'''
CODE BY KIMARU THAGANA-----This is the callback file hosted in the url below
Required packages
pip3 install flask
callback url : http://ussdchallenge.pythonanywhere.com/
'''

from flask import Flask,request
from datetime import datetime
from task2.task2 import *

app = Flask(__name__)

preferred_username=""
preferred_email=""

thisYear=datetime.today().year # current year to be used to distinguish username
# also used in mitigation of user errors
# endswith() used to work around the nature of the text returned from the AT simulator
@app.route('/',methods=['POST', 'GET'])
def ussd_callback():
  response=""
  global preferred_username
  global preferred_email
  text = request.values.get("text", "default")
  if text == '' or text.lower().startswith(str('1*')) and text.lower().endswith(str('*3')):
      # blank text hence first time or text starts with 1 and ends with 3 meaning the user started well
      # made a blunder then chose option 3 to try again
      response = "CON Welcome to the JuneTalk Platform. Select an action you would like to perform \n"
      response += "1. Sign Up  \n"
      response += "2. Quit"
  elif text == '1' or text.lower().startswith('1*') and text.lower().endswith('*1'):
      # user opted to sign up or is coming back to sign up after making one or more blunders hence text ends in *1-> Sign up
      response = "CON Kindly submit your preferred username\nEnsure it ends with"+str(thisYear)
  elif text != '' and text != '1' and text != '2' and text.lower().endswith(str(thisYear)):
      # integrity check of username is that it must end in the string of the current year
       preferred_username=text
       response = "CON Kindly submit your preferred email address\n"
  elif text != '' and text != '1' and  text != '2' and '@' in text:
      # email should have an @ symbol
       preferred_email=text
       response = "END Thank you for registering. You will receive a confirmation SMS shortly\n"
       successmessage(preferred_username, preferred_email)# call function to send message
  elif text  != '' and text != '1' and text != '2' and '@' not in text and not (text.lower().endswith(str(thisYear))) and not (text.lower().endswith(str('*2'))):
      # wrong user format---no year included in the username; wrong email format, no @
        response = "CON Wrong email or username format. \n"
        response += "3. Try again  \n"

  elif text == '2' or text.lower().startswith(str('1*')) and text.lower().endswith(str('*2')):
      # if user wishes to quit at first or after a while
      response = "END Thank you for your time. "
  else:
       response = "CON Invalid Response. Kindly try again with the options below \n"
       response += "1. Sign Up  \n"
       response += "2. Quit"
  return response
