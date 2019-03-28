'''
Task : Create ussd + sms app
User journey: person dials the USSD Code and gets 
prompted for a username and email address. 
After which they get an SMS response telling them they've
registered successfully
'''

# importing needed libraries
import africastalking
from flask import Flask
from flask import request
from email_validator import validate_email
from email_validator import EmailNotValidError

# initialize app

app = Flask(__name__)

# Initialize sdk

AT_username = ""
AT_api = ''
africastalking.initialize(AT_username, AT_api)

# Initialize a service
sms = africastalking.SMS

# set message
message = "Account registered successfully."

# inititalize variables to used
# stores the responses
response = ""


@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    global message

    session_id = request.values.get("sessionId", None)  # session_id from api
    service_code = request.values.get("serviceCode", None)  # service code api
    phone_number = request.values.get("phoneNumber", None)  # number using the service api
    text = request.values.get("text", "default")

    if text == '':
        # if no blank text requesr username details
        response = "CON Enter username and email separated by | (pipe) "
    # check impute if separated by |
    elif '|' in text:
        # input is made up of two parts username and email we split the two
        segments = text.split('|')
        username = segments[0].strip()
        email = segments[1].strip()


        # validate username and email
        # check is username not null
        if username:
            try:
                valid_email = validate_email(email)  # validate and get info
                email = valid_email["email"]
                response = "END Thank you Confirmation text has been sent"

                # sending of message
                sms.send(message, phone_number)

            except EmailNotValidError as e:
                response = "END " + str(e)
        else:
            response = "END enter valid username"

    return response


if __name__ == '__main__':
    app.run(debug=True)
