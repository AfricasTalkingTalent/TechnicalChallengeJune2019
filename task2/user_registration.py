
# A very simple Flask Hello World app for you to get started with...

from flask import Flask,request

app = Flask(__name__)
response=""
preferred_username=""
preferred_email=""
@app.route('/',methods=['POST', 'GET'])
def ussd_callback():
  response=""
  session_id = request.values.get("sessionId", None)
  service_code = request.values.get("serviceCode", None)
  phone_number = request.values.get("phoneNumber", None)
  text = request.values.get("text", "default")
  print('==='+str(text))
  if text == '':
      response = "CON Welcome to the JuneTalk Platform. Select an action you would like to perform \n"
      response += "1. Sign Up  \n"
      response += "2. Quit"
  elif text == '1':
      response = "CON Kindly submit your preferred username\n"
  elif text != '' and text != '1' and text != '2':
       preferred_username=text
       response = "CON Kindly submit your preferred email address\n"
  elif text != '' and text != '1' and  text != '2' and '@' in text or text == '3':
       preferred_email=text
       response = "END Thank you for registering. You will receive a confirmation SMS shortly\n"
  elif text  != '' and text != '1' and text != '2' and '@' not in text:
        response = "CON Wrong email format. Kindly include an @ symbol in the email \n"
        response += "3. Try again  \n"
        response += "4. Quit"

  elif text == '2' or '4':
      response = "END Thank you for your time. "
  else:
       response = "CON Invalid Response. Kindly try again with the options below \n"
       response += "1. Sign Up  \n"
       response += "2. Quit"

  print('======+++++++++++++++=',response)
  return response