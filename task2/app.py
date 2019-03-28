from flask import Flask, request, Response
import africastalking

# Initialize SDK
username = "sandbox"    # for sandbox testing enviromnent
api_key = "f29a3c192d68ab1ab466793e7907ab4d88bb58a4363c66578cb768b94a1b1599"      # current sandbox API key
africastalking.initialize(username, api_key)

sms = africastalking.SMS #initialise sms service

users = {}      #dictionary to store users: {username: email}

app = Flask(__name__) 
  
@app.route('/', methods = ['POST']) 
def main(): 
    if request.method == 'POST':
        session_id = request.form.get('sessionId')
        service_code = request.form.get('serviceCode')
        phone_number = request.form.get('phoneNumber')
        text = request.form.get('text')

    response = ""

    if text == "":
        response = "CON Enter a username and password separated by a colon (:)"
        
    if text != "":
        parts = text.split(':')
        username = parts[0].strip()
        email = parts[1].strip()
        users[username] = email
        response = "END A confirmation will be sent via text."

        # send confirmation message
        number = []
        number.append(phone_number)
        confirmationText = "You have been successfully registered!"
        shortCode = "1635"
        sms.send(confirmationText, number, shortCode, enqueue = False)

    return Response(response)
            

if __name__ == '__main__': 
   app.run() 