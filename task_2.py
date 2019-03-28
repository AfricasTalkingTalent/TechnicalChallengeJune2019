import africastalking
import os

from flask import Flask, request
app = Flask(__name__)

#authenticating the user in order to use the africastalking API
username = "sandbox"
apikey = "ed76374db40082501ca67f2f1efcde719663a366c4a5fa2ba8c50e969f7c43b6"

africastalking.initialize(username, apikey)     #initializing the SDK


sms = africastalking.SMS       #getting SMS service


response = ""
 #starting Flask apps service
@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
  global response
  session_id = request.values.get("sessionId", None)
  service_code = request.values.get("serviceCode", None)
  phone_number = request.values.get("phoneNumber", None)
  text = request.values.get("text", "default")

  if text == '':
        response  = "CON Input your username and email address below separated by a (#): \n" #prompt for username and password

  else:
      username=text.split('#')[0]
      email_address=text.split('#')[1]
      sms.send('You have registered successfully!\nE-mail: ' + email_address + "\nUsername: " + username + "\n", #sending message to phone number
               [str(phone_number)])
      response = "END Thank you. You will receive a confirmation message soon. \n"

  return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

#using WSGI production server running on 0.0.0.0:5000/
#using ngrok