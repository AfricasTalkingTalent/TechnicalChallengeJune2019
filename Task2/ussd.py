import africastalking
from flask import Flask, request

# initialize
app = Flask(__name__)
username = "sandbox"
 
apikey = "2eb97013ea7b1ee3da4b2f902bed7392f4f6728dedd1831f2ad40fc6e1f1a156" 

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
     
    if text == '':
        response = "Please enter your name \n"
        response += "Please do not enter @ in your username \n"

    elif ('@' not in text) :
        response = "Please enter your email address \n"

    else:
        response = "END You will receive an sms confirmation shortly"
        sms.send("You have successfully registered.", [phoneNumber])
    return response

if __name__ == '__main__':
    app.run()
