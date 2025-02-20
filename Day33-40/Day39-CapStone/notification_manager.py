from twilio.rest import Client

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = "AC93de7bcd904c80a1b17474e2c7bfa1d0"
        self.auth_token = "d1d68290f0698d32c43f679be3de39e1"
        self.client = Client(self.account_sid, self.auth_token)

    def send_sms_notification(self,text):
        message = self.client.messages.create(
            messaging_service_sid='MG18e357cd6901aa14be928a520b533856',
            body=text,
            to='+6583992760'
        )
        print(message.sid)