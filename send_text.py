from twilio.rest import Client

# SID da sua conta, encontre em twilio.com/console
account_sid = "input"
# Seu Auth Token, encontre em twilio.com/console
auth_token  = "input"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5551984373078",
    from_="+17122275825",
    body="Olhe que legal essa funcionalidade!")s
print(message.sid)