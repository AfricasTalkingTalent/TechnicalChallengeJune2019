
# imports 
import africastalking
from flask import Flask, request

# initialize app, params 
app = Flask(__name__)
username = "sandbox"
# conceal in production. 
apikey = "550baa3e7545e2cf21711daba7d7a9eea77cb7509d9e494ce919675480cf7235" 

africastalking.initialize(username, apikey)
sms = africastalking.SMS


#  route 
@app.route('/')
def index():
    return ""


@app.route('/ussd', methods = ['GET', 'POST'])
def ussd():
    text         = request.values.get("text", "default")
    sessionId   = request.values.get("sessionId", None)
    serviceCode  = request.values.get("serviceCode", None)
    phoneNumber = request.values.get("phoneNumber", None)
     
     # First request, we then prompt user for username.
     # Explicitly ask the user to exclude the @ symbol.
    if text == '':
        response = "CON Please enter your username \n"
        response += "Please do not enter @ in your username \n"

    # Second request, we then prompt user for email address.
    # To distinguish between user and email prompts, a brute solution is to 
    # code user response with an @.  
    # More robust email (or username) validation such as regex matching may handy 
    # e.g. for user experience and username flexibility, in production. 
    elif ('@' not in text) :
        response = "CON Please enter your email address \n"

    # Last response: user is successfully registered
    # Send confirmation message 
    else:
        response = "END You will receive an sms confirmation shortly"
        sms.send("You have successfully registered.", [phoneNumber])
    return response

if __name__ == '__main__':
    app.run()