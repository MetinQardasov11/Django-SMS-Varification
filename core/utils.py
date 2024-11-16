import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()

account_sid = os.getenv("TWILIO_ACCOUNT_SID")

auth_token = os.getenv("TWILIO_AUTH_TOKEN")

client = Client(account_sid, auth_token)

def send_sms(user_code, phone_number):
    message = client.messages.create(
        body=f'Your verification code is: {user_code}',
        from_='+14796898340',
        to=f'{phone_number}'
    )
    