# Erick Ogaro
# Date: 29th March, 2019.


# Import the sdk into app
import africastalking

from flask import request, Flask

app = Flask(__name__)

response = ""


@app.route('/', methods=['POST', 'GET'])
def ussd_callback():
    global response
    session_id = request.values.get("sessionId", None)
    service_code = request.values.get("serviceCode", None)
    phone_number = request.values.get("phoneNumber", None)
    text = request.values.get("text", "default")


# My test credentials
username = "sandbox"
apikey = "112f3eb08f553c2bd555283a72aed140c323109498f5bfbc5c2e2e1c39337f5d"

# Initialize the Africa's Talking SDK
africastalking.initialize(username, apikey)

# Call the SMS service
sms = africastalking.SMS

# Define some options that we will use to send the SMS
recipients = ['+254792835893']
message = 'You have successfully registered your username and your e-mail'
sender = '19256'

# Send the SMS
try:
    # Once this is done, that's it! We'll handle the rest
    response = sms.send(message, recipients, sender)
    print(response)
except Exception as e:
    print(f"Error {e}")
