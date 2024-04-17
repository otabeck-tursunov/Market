from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.views import APIView

from mainApp.models import *
from mainApp.serializers import *
from userApp.serializers import *
from userApp.models import Profile
from userApp.permissions import *


class ProfilesAPIView(APIView):
    permission_classes = (IsSuperUser,)

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileDetailsAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsSuperUser,)
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer


class CategoriesAPIView(APIView):
    permission_classes = (IsManagerUser, IsSuperUser,)

    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=CategorySerializer,
    )
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductsAPIView(APIView):
    permission_classes = (IsManagerUser, IsSuperUser,)

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ProductSerializer,
    )
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
