from twilio.rest import Client

# SID da sua conta, encontre em twilio.com/console
account_sid = "input_your_sid"
# Seu Auth Token, encontre em twilio.com/console
auth_token  = "input_your_token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+5551984373078",
    from_="+17122275825",
    body="Olha que massa! Enviando SMS com o Python. Um Abs, Sandro Lucas. -- Enviado do meu Iphone :)")

print(message.sid)