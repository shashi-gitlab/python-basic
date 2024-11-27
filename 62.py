# pip --version
# pip install twilio
# pip list
from twilio.rest import Client 
# print(Client, type(Client))

account_sid = 'AC821fb45b2bd862b75421a8f039840b6a'
auth_token = 'a96a1e03fd4196ebaa40c5a1046ffde1'
client = Client(account_sid, auth_token) 
# print(client,type(client))
message = client.messages.create( 
    from_='+12093538115', 
    body ='Sending Message From Python Code', 
    to ='+919987107564'
) 
print(message.sid) 
# https://www.geeksforgeeks.org/python-send-sms-using-twilio/