import os
from flask import Flask, request

app = Flask(__name__)

response = ""

@app.route('/', methods = ['GET','POST'])

def ussd():
    global response
    session_id = request.values.get("sessionId",None)
    servicecode =  request.values.get("serviceCode",None)
    phone_number = request.values.get("phoneNumber",None)
    email =  request.values.get("email",None)
    name = request.values.get("name",None)
    text =  request.values.get("text",None)

    response = "Whats your name: "


    if text == "":
        response = "Fill the details \n"
        response += "1. Name\n"
        response += "2. My Email\n"
    elif text == "1":
        response = "Write your name:\n"
        name += " \n"
    elif text == "2":
        response = "Write your email:\n"
        email += " \n"
    else:
        response = "END Invalid choice"

        return response

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=os.environ.get("PORT"),debug=True)