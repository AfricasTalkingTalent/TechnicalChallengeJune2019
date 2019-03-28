# Simple app demonstrating use of USSD and SMS using the Africa's Talking gateway

from flask import Flask, request, Response
import africastalking

# Initialize SDK
username = "sandbox"    # for sandbox testing enviromnent
api_key = "f29a3c192d68ab1ab466793e7907ab4d88bb58a4363c66578cb768b94a1b1599"      # current sandbox API key. You need to use your own
africastalking.initialize(username, api_key)

sms = africastalking.SMS #initialise sms service

users = {}      #dictionary to store users: {username: email}

# initialise app
app = Flask(__name__) 
  

@app.route('/', methods = ['POST'])     # set the function to receive only POST requests
def main():    
    if request.method == 'POST':    
        # receive data from POST request
        session_id = request.form.get('sessionId')
        service_code = request.form.get('serviceCode')
        phone_number = request.form.get('phoneNumber')
        text = request.form.get('text')

    response = ""       # variable for storing respose temporarily

    if text == "":      # the session has just been initialised
        response = "CON Enter a username and password separated by a colon (:)"
        
    if text != "":      # the user has responded
        if ":" in text:         #check if the text has the specified format
            parts = text.split(':')
            username = parts[0].strip()
            email = parts[1].strip()

            if not username == "" and not email == "" and "@" in email: #additional validation for the username and password
                usernames = users.keys()
                if username not in usernames:   # check if username is unique
                    response = "END A confirmation will be sent via text."
                    
                    # register user
                    users[username] = email
                    
                    # send confirmation message
                    number = []     #the send function requires a list
                    number.append(phone_number)
                    confirmationText = "You have been successfully registered!"
                    shortCode = "1635"
                    sms.send(confirmationText, number, shortCode, enqueue = False)
                elif username in usernames:
                    response = "END The username has already been taken."

            else:
                response = "END Invalid username or email"
        else:
            response = "END Incorrect format! Try again"

    return Response(response)
            

if __name__ == '__main__': 
   app.run() 