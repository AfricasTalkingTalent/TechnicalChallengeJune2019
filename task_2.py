from flask import Flask
from flask import request, json, make_response
import africastalking


app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def home():
    """Defines route to ussd
    """

    # retreive phone number and text from the request data
    phone_number = request.values.get("phoneNumber")
    text = request.values.get("text", "")
    response = ""

    if text == "":
        response = "CON Welcome to account registration\n"
        response += "1. Proceed"
    elif text == "1":
        response = "CON Please enter your username"
    else:
        # determine the response level by spliting text using *
        parts = text.split('*')
        if len(parts) == 2:
            response = "CON Please enter your email"
        else:
            response = "END Registration successful.\n"
            response += "An SMS has been sent to your phone"
            # send sms to user with the registered details
            send_sms(dict(phone_number=phone_number, user_name=parts[1],
                     email=parts[2]))

    return response


# @app.route("/", methods=['GET'])
# def index():
#     return "I am alive"


def send_sms(user_details):
    """
    Sends sms to given phone number through Africastalking API

    Arguments:
        user_details {dict} -- contains phone number, email and
                               username of the newly registered user
    """
    username = 'sandbox'
    api_key = 'feedb09e1e093cdc591335a9fb2c4d54920e6471c65765d93ccee4c89510e597'
    africastalking.initialize(username, api_key)

    sms = africastalking.SMS
    msg = f"Registration successful\n\
            Username: {user_details.get('user_name')}\n\
            Email: {user_details.get('email')}"

    result = sms.send(msg, [user_details.get('phone_number')])

if __name__ == "__main__":
    app.run(debug=True)
