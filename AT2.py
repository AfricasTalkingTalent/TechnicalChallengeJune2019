# Task 2
# importing africastalking and importng flask
from flask import Flask, request
import africastaking

app = Flask(_name_)
username = "sandbox"
apikey = ""

africastalking.initialize(username, apikey)
sms = africastalking.SMS


@app.route('/')
def index():
	return "*"

# receiving 
@app.route('/ussd', methods = ['GET', 'POST'])
def ussd():
    session_id   = request.values.get("sessionId", None)
    serviceCode  = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text         = request.values.get("text", "default")

    # start from empty message and ask for a user name
	if text == '':
		response = "CON Please enter your username \n"
	elif('@' not in text ) and ('.' not in text):
		# check for appropriate email format
		response = "CON Next, please enter your email address \n"
	else:
		# notify about the message to be sents and send sms
		response = "END You will get an SMS to confirm your registration."
		sms.send("Congratulations, you have successfully registered.", [phone_number])
	return response

if __name__ == '__main__':
	app.run()





