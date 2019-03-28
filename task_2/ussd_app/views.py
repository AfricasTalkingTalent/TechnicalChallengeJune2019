from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import africastalking
# Create your views here.

@csrf_exempt
def ussd_callback(request):
	#variables to store user input data
	global user_name
	global email

	#get session data from data in POST
	phone_number = request.POST.get("phoneNumber", None)
	text = request.POST.get("text", "default")
	
	
	#check if it's the start of a SESSION.
	if text == "":

		response = """CON Hello! You are about to register for our service.
		You will be required to provide a username and email. reply with 1 to continue.

		1. Proceed with registration"""

	
	#user proceeded with registration
	elif text == '1':
		#ask for user name
		response = "CON Please provide your username: "

	#if user has provided username
	#ask for user email
	elif text.count('*') == 1 and not text.endswith('*'):
		response = "CON Please provide your email: "


	#check if it's the last prompt(indicator is having two astericks in text) 
	elif text.count('*') == 2 and not text.endswith('*'):

		#last prompt means we have a username and email - in the format '1*username*email'
		# first we store user details after
		#splitting user input along a '*' to separate username from password
		# expected format after split: ['1', 'username', 'password']	
		user_details = text.split('*')
		user_name = user_details[1]
		email = user_details[2]

		#then notify the user that registration is done. End session.
		response = f"END Registration done!\nYou will recieve an sms confirmation shortly.\n\nplease check your inbox"
		send_sms(phone_number)

	else:
		#Incase of invalid input, terminate session
		response = """END Sorry, we recieved an invalid input.
		please ensure you don't use * character with your username/email. 
		dial *384*27278# to try again"""

	return HttpResponse(response)


def send_sms(phone_number):
	#initialize SDK
	username = 'sandbox'
	api_key = 'e72fb40265d5c5f32a80263329e158af69ac5e1366fda77b20926163a6b9d856'
	africastalking.initialize(username, api_key)

	sms = africastalking.SMS
	success_message = f"Success! you completed your registration.Details:\nusername: {user_name}\nemail: {email}"

	#send success message to user!
	result = sms.send(success_message, [phone_number])

