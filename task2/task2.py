import africastalking

# Initialize SDK
username =  "sandbox"  #  alternatively use environment variables
api_key =  "d74e4822dc6e1d8628d11b129e2f8d42d01d5a4b82ba4475f0ea229bf169db67"
africastalking.initialize(username, api_key)

# Initialize service e.g. SMS
sms = africastalking.SMS

def successmessage(username, email):
    username=username.split('*')[-1]
    email=email.split('*')[-1]
    # communicate to user
    response = sms.send("Successful account registration\n Your are receiving this message because you have signed up for an account at \n"+
    "JUNETALK Below are your details \n username:"+str(username)+"\n Email:"+str(email)+"\n Visit https://www.juntalk2019.com for more information", ["+254726782953"])