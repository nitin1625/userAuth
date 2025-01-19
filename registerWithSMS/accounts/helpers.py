import requests
import random 
from django.conf import settings 

def send_otp_to_phone(phone_number):
    try:
        otp=random.randint(1000,9999)
        URL=f'https://2factor.in/API/V1/{settings.SMS_SECRET_KEY}/SMS/{phone_number}/AUTOGEN/{otp}'
        response=requests.get(url=URL)
        return response
    except Exception as e :
        return e 