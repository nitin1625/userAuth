from django.shortcuts import render,redirect 
from rest_framework.views import APIView 
from .emails import send_otp_via_email
from rest_framework.response import Response 
from .serializers import * 
from .models import * 

class RegisterView(APIView):
    def post(self,request):
        try:
            data=request.data 
            serializer=UserSerializer(data=data)
            if serializer.is_valid():
                user=serializer.save()
                email=user.email
                try :
                    send_otp_via_email(email)
                except Exception as e :
                    return Response({
                        'status':500,
                        'message':'Fail to send Otp via mail'
                    })
                
                return Response({
                    'status': 200,
                    'message': 'Registration successful, check your email for OTP.',
                    'data': serializer.data,
                })

                
            return Response({
                'status': 400,
                'message': 'Invalid data provided.',
                'data': serializer.errors
            })
        


        except Exception as e:
            return Response({
                'status': 500,
                'message': 'Internal server error.',
                'data': str(e)
            })
                

class VerifyOTP(APIView):
    def post(self, request):
        data = request.data
        serializer = VerifyAccountSerializer(data=data)

        if serializer.is_valid():
            email = serializer.validated_data['email']
            otp = serializer.validated_data['otp']
            user = customUser.objects.filter(email=email).first()

            if not user:
                return Response({
                    'status': 400,
                    'message': 'User Not Found',
                    'data': 'Invalid Email'
                }, status=400)

            if user.otp != otp:
                return Response({
                    'status': 400,
                    'message': 'OTP Not valid',
                    'data': 'Invalid OTP'
                }, status=400)

            user.is_verified = True
            user.save()
            print('user saved successfully')

            return Response({
                'status': 200,
                'message': 'Account successfully verified',
            }, status=200)

        return Response({
            'status': 400,
            'message': 'Invalid OTP data.',
            'data': serializer.errors,
        }, status=400)




