import twilio
from twilio.rest import Client

account_sid = 'AC585e6d09c33bf5093baeaa93dc64c19b'
auth_token = 'dd540f124f16b705b122ebfb7ccfec8c'
client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+66 87 670 4116", 
    from_="+13147863882",
    body="Naj praaphatsarang (6005008245)")

print(message.sid)