import random

from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView

from eskiz.client import SMSClient

from Market import settings
from .serializers import *
from .permissions import *
from .models import *

#
# class RegisterAPIView(APIView):
#     permission_classes = (AllowAny,)
#
#     @swagger_auto_schema(
#         request_body=ProfileRegisterSerializer,
#     )
#     def post(self, request):
#         serializer = ProfileRegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             profile = Profile.objects.create_user(
#                 username=serializer.validated_data['phone_number'],
#                 phone_number=serializer.validated_data['phone_number'],
#                 password=serializer.validated_data['password'],
#                 confirmation_code=str(random.randint(111111, 999999)),
#             )
#             client = SMSClient(
#                 api_url="https://notify.eskiz.uz/api/",
#                 email=settings.ESKIZ_GMAIL,
#                 password=settings.ESKIZ_TOKEN,
#             )
#
#             st = client._send_sms(
#                 phone_number=profile.phone_number,
#                 message=f"{profile.confirmation_code} - tasdiqlash kodi",
#             )
#             print(st)
#             return Response(
#                 {
#                     "success": True,
#                     "message": "The verification code has been successfully sent to the phone number!",
#                 }
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ConfirmAPIView(APIView):
#     permission_classes = (IsOrdinaryUnconfirmedUser,)
#
#     @swagger_auto_schema(
#         request_body=ProfileConfirmSerializer,
#     )
#     def post(self, request):
#         serializer = ProfileConfirmSerializer(data=request.data)
#         if serializer.is_valid():
#             profile = request.user
#             if profile.confirmation_code == serializer.validated_data['confirmation_code']:
#                 profile.confirmed = True
#                 profile.save()
#                 return Response({"success": True, "message": "Registration was successful"})
#             return Response({"success": False, "message": "The verification code is invalid"})
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
