from twilio.rest import Client

account_sid = 'ACa848d702d6ede05f0f1c019d554d1546'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from='+18336202597',
  body='bamboclat',
  to='+13107809782'
)

print(message.sid)