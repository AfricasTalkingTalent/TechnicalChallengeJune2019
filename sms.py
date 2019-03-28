#import AfricasTalking SDK
import africastalking

#My app credentials
username = "myself"#username for my create app
apikey = "535046bc037164d15318ba442c09e8c0abe0d8f78175a6c256d32f5198247bb7"

#Initialize the SDK
africastalking.initialize(username,apikey)

#Get the SMS service
sms = africastalking.SMS

#Define options that will use to send the SMS
recipients = ['+254701247794']
message = 'You have Successfully Registered'
#sender = 'SwahiliCode'

#Send the SMS
try:
    response = sms.send(message, recipients)
    print(response)
except Exception as e:
    print(f"We have a problem {e}")