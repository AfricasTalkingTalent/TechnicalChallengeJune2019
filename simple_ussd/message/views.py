from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import africastalking

# Create your views here.
session_stage = {}

@csrf_exempt
def index(request):
    if request.method == 'POST':
        print(request.POST)
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        username = request.POST.get('username')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        response = ""
        if session_id not in session_stage:
            session_stage[session_id] = '1'
        
        stage =  session_stage[session_id]
        if stage == '1':
            if text == "":
                response = "CON Do you want to register with us? \n"
                # response .= "1. if you want to register or 2. if not \n"
                response += "1.Yes \n 2.No"

            elif text == "2":
                response = "END Thank you"
            elif text == "1":
                session_stage[session_id] = '1-1'
                response = "CON Please enter your email and name separated by a comma"
        elif stage == '1-1':
            # text -> reivhax,xavier@gmail.com
            if text.count(',') == 1:
                username, email = text.split(',')
                # process username and email
                # response = 'END successfully registered'

                username = "cliff nyendwe"    # use 'sandbox' for development in the test environment
                # api_key = "167f369c5f2ee27454542e587ae2eee8ebeee655dda0e6af106670f828f057c6" # use your sandbox app API key for development in the test environment
                api_key='ab63434a89142f362716b331a37bcb8c4d04c5fe6f9f183f427b00b35af50489'
                africastalking.initialize(username, api_key)


                # Initialize a service e.g. SMS
                sms = africastalking.SMS


                # Use the service synchronously
                response = sms.send("END Thank you for registering with us!",["+254720132613"])
                print(response)
                return HttpResponse(response)
            else:
                response = 'END Invalid input'

        return HttpResponse(response)
    else:
        return HttpResponse(f'{request.method} is not allowed')



