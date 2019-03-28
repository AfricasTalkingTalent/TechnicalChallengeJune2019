require('dotenv').config()
const options = {
    apiKey: process.env.AFRICAS_TALKING_API_KEY,
    username: 'sandbox'
};
const africasTalking = require('africastalking')(options);

exports.sendMessage = function(phoneNumber){
    sms = africasTalking.SMS
    const messageOptions = {
        to: [`${phoneNumber}`],
        message:'You have been Registered Successfully.'
    }

    sms.send(messageOptions)
        .then(response=>{
            console.log(response)
        })
        .catch(err=>{
            console.error("Error Sending sms"+err.message)
        })

}