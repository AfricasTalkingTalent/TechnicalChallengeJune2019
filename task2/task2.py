import africastalking

# Initialize SDK
username =  "sandbox"  #  alternatively use environment variables
api_key =  "d74e4822dc6e1d8628d11b129e2f8d42d01d5a4b82ba4475f0ea229bf169db67"
africastalking.initialize(username, api_key)

# Initialize service e.g. SMS
sms = africastalking.SMS

# ussd service
# communicate to user
response = sms.send("Successful account registration", ["+254726782953"])