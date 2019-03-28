from django.shortcuts import render,redirect
from django.http  import HttpResponse,Http404
from django.views.decorators.csrf import csrf_exempt
import africastalking
# Create your views here.
session_level = {}

@csrf_exempt#decorator passed in to prevent django error with post request
def home(request):
    if request.method == 'POST':
        session_id = request.POST.get('sessionId')
        service_code = request.POST.get('serviceCode')
        username = request.POST.get('username')
        phone_number = request.POST.get('phoneNumber')
        text = request.POST.get('text')
        response = ""
        if session_id not in session_level:
            session_level[session_id] = '1'

        level =  session_level[session_id]
        if level == '1':
            if text == "":#what to be displayed in first session
                response = "CON Welcome to ussd app, would wish to register with us?. \n"

                response += "1.Yes \n 2.No"

            elif text == "2":#if user picks option 2 sesion is ended
                response = "END Thank you"
            elif text == "1":#for option 1 user contiues with registration
                session_level[session_id] = '1-1'
                response = "CON To continue enter your email and name separated by a comma"
        elif level == '1-1':
            # cred = jamea,james@gmail.com
            if text.count(',') == 1:# process username and email
                username, email = text.split(',')
                # response = 'END successfully registered'
                #sending SMS
                username = "sandbox"
                api_key='3dc02351cdd816169989a9f6b92c84fc5c8da322b02a519837a75b7f33d404f0'
                africastalking.initialize(username, api_key)
               # Initialize a service e.g. SMS
                sms = africastalking.SMS
                response = sms.send("END Thank you for registering with us!",["+254707371208"])
                print(response)
                return HttpResponse(response)
            else:
                response = 'END Invalid input'

        return HttpResponse(response)
    else:
        return HttpResponse(f'{request.method} is not allowed')
