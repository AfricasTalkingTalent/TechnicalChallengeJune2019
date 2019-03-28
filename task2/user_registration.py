from flask import Flask,request
from datetime import datetime
from mysite.task2 import *

app = Flask(__name__)
preferred_username=""
preferred_email=""
thisYear=datetime.today().year
@app.route('/',methods=['POST', 'GET'])
def ussd_callback():
  response=""
  global preferred_username
  global preferred_email
  text = request.values.get("text", "default")
  if text == '' or text.lower().startswith(str('1*')) and text.lower().endswith(str('*3')):
      response = "CON Welcome to the JuneTalk Platform. Select an action you would like to perform \n"
      response += "1. Sign Up  \n"
      response += "2. Quit"
  elif text == '1' or text.lower().startswith('1*') and text.lower().endswith('*1'):
      response = "CON Kindly submit your preferred username\nEnsure it ends with"+str(thisYear)
  elif text != '' and text != '1' and text != '2' and text.lower().endswith(str(thisYear)):
       preferred_username=text
       response = "CON Kindly submit your preferred email address\n"
  elif text != '' and text != '1' and  text != '2' and '@' in text:
       preferred_email=text
       response = "END Thank you for registering. You will receive a confirmation SMS shortly\n"
       successmessage(preferred_username, preferred_email)
  elif text  != '' and text != '1' and text != '2' and '@' not in text and not (text.lower().endswith(str(thisYear))) and not (text.lower().endswith(str('*2'))):
        response = "CON Wrong email or username format. \n"
        response += "3. Try again  \n"

  elif text == '2' or text.lower().startswith(str('1*')) and text.lower().endswith(str('*2')):
      response = "END Thank you for your time. "
  else:
       response = "CON Invalid Response. Kindly try again with the options below \n"
       response += "1. Sign Up  \n"
       response += "2. Quit"
  return response
