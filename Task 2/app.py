# Erick Ogaro
# Date: 29th March, 2019.

import africastalking

username = "sandbox"
apikey = "112f3eb08f553c2bd555283a72aed140c323109498f5bfbc5c2e2e1c39337f5d"
africastalking.initialize(username, apikey)

# initialize service
sms = africastalking.SMS
ussd = africastalking.USSD

# use service synchronously
response = sms.send("Hello Erick!", ["+254792835893"])
print(response)
