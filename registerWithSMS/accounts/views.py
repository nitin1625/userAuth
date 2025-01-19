from django.shortcuts import render
from rest_framework.decorators import api_view 
from rest_framework.response import Response
from .helpers import  send_otp_to_phone
from .models import User

@api_view(['POST'])
def send_otp(request):
    data=request.data 

    if data.get('phone_number') is None :
        return Response({
            'status':400,
            'message':'phone number is required'
        })
    

    if data.get('password') is None :
        return Response({
        'status':400,
        'message':'password is required'
    })


    user=User.objects.create(
        phone_number=data.get('phone_number'),
        otp=send_otp_to_phone(data.get('phone_number'))
        )
    user.set_password(data.get('password') )
    user.save()

    return Response({
        'status':200,
        'message':'Otp sent Successfully'
    })

    





@api_view(['POST'])
def verify_otp(request):
    data=request.data 

    if data.get('phone_number') is None :
        return Response({
            'status':400,
            'message':'phone number is required'
        })
    

    if data.get('password') is None :
        return Response({
        'status':400,
        'message':'password is required'
    })


    try:
        user=User.objects.get(phone_number=data.get('phone_number'))

    except Exception as e :
        return Response({
            'status':400,
            'message':'Otp sent Successfully'
        })
    

    if user.otp==data.get('otp'):
        user.is_phone_verified=True
        user.save()
        return Response({
            'status':200,
            'message':'Verification Successfull'
        })
    

    return Response({
    'status':400,
    'message':'invalid OTP'
    })

    


    




