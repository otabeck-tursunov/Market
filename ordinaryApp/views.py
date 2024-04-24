from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.permissions import *

from userApp.models import Profile
from userApp.permissions import IsOrdinaryUser
from userApp.serializers import ProfileSerializer, ProfileOrdinarySerializer


class ProfileCreateAPIView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        request_body=ProfileOrdinarySerializer,
    )
    def post(self, request):
        serializer = ProfileOrdinarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetailsAPIView(APIView):
    permission_classes = (IsOrdinaryUser,)

    def get(self, request):
        profile = request.user
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)


class ProfileUpdateAPIView(APIView):
    permission_classes = (IsOrdinaryUser,)

    @swagger_auto_schema(
        request_body=ProfileOrdinarySerializer,
    )
    def put(self, request):
        serializer = ProfileSerializer(request.user, data=request.data)
        if serializer.is_valid():
            serializer.save(
                role="ordinary"
            )
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDeleteAPIView(APIView):
    permission_classes = (IsOrdinaryUser,)

    def delete(self, request):
        profile = request.user
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
