from flask import Flask, request

#Create an Instance of Flask class
app = Flask(__name__)

#Routing, Add GET and POST Methods
@app.route('/', methods = ['GET','POST'])

def ussd():
    session_id = request.values.get("sessionId",None)
    servicecode =  request.values.get("serviceCode",None)
    phone_number = request.values.get("phoneNumber",None)
    text = request.values.get("text",None)

    if text == "":
        response = "CON Enter your Username\n"
        response += "1. Proceed\n"
    elif text == "1":
        response = "CON Enter your EmailAddress\n"
        response += "1. SignUp\n"
    elif text == "1*1":
        response = "END You have registered Successfully"
    else:
        response = "END Invalid choice"

    return response

if __name__ == "__main__":
    app.run(debug=True)