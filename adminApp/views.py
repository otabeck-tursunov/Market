from django.db.models import Q
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, filters
from rest_framework.generics import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from mainApp.models import *
from mainApp.serializers import *
from orderApp.models import Cart, CartItem, Order, OrderItem
from orderApp.serializers import CartSerializer, CartItemSerializer, OrderSerializer, OrderItemSerializer
from userApp.serializers import *
from userApp.models import Profile
from userApp.permissions import *


class NewsAPIView(ListCreateAPIView):
    permission_classes = (IsManagerOrSuperUser,)
    serializer_class = NewsSerializer
    queryset = News.objects.all()

    filter_backends = (filters.SearchFilter,)
    search_fields = ('id', 'title', 'content')


class NewsDetailsAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsManagerOrSuperUser,)
    serializer_class = NewsSerializer
    queryset = News.objects.all()


class ProfilesAPIView(APIView):
    permission_classes = (IsSuperUser,)

    def get(self, request):
        profiles = Profile.objects.all()
        serializer = ProfileSerializer(profiles, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ProfileSerializer,
    )
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
    permission_classes = (IsManagerOrSuperUser,)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='id',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description='filter by ID',
            ),
            openapi.Parameter(
                name='search',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='search by title',
            ),
        ]
    )
    def get(self, request):
        categories = Category.objects.all()
        if request.query_params.get('id'):
            categories = categories.filter(id=request.query_params.get('id'))
        if request.query_params.get('search'):
            categories = categories.filter(title__icontains=request.query_params.get('search'))
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


class CategoryDetailsAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsManagerOrSuperUser,)
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsAPIView(APIView):
    permission_classes = (IsManagerOrSuperUser,)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='id',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description='filter by ID',
            ),
            openapi.Parameter(
                name='search',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='search by name, brand, country, color, category',
            ),
            openapi.Parameter(
                name='discount',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_BOOLEAN,
                description='filter by discount',
            ),

        ]
    )
    def get(self, request):
        products = Product.objects.all()
        if request.query_params.get('id'):
            products = Product.objects.filter(id=request.query_params.get('id'))
        if request.query_params.get('search'):
            search = request.query_params.get('search')
            products = Product.objects.filter(
                Q(name__icontains=search) |
                Q(brand__icontains=search) |
                Q(country__icontains=search) |
                Q(color__icontains=search) |
                Q(category__title__icontains=search)
            )
        if request.query_params.get('discount') is not None:
            if request.query_params.get('discount') == 'true':
                products = products.filter(discount__gt=0)
            else:
                products = products.filter(discount=0)
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


class ProductDetailsAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsManagerOrSuperUser,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductImagesAPIView(APIView):
    permission_classes = (IsManagerOrSuperUser,)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='product_id',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='filter by Product ID',
            )
        ]
    )
    def get(self, request):
        images = ProductImage.objects.all()
        if request.query_params.get('product_id'):
            images = images.filter(product__id=request.query_params.get('product_id'))
        serializer = ProductImageSerializer(images, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ProductImageSerializer
    )
    def post(self, request):
        serializer = ProductImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductImageDetailsAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsManagerOrSuperUser,)
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer


class ProductPropertiesAPIView(APIView):
    permission_classes = (IsManagerOrSuperUser,)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='product_id',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='filter by Product ID',
            )
        ]
    )
    def get(self, request):
        properties = ProductProperty.objects.all()
        if request.query_params.get('product_id'):
            properties = properties.filter(product__id=request.query_params.get('product_id'))
        serializer = ProductPropertySerializer(properties, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ProductPropertySerializer
    )
    def post(self, request):
        serializer = ProductPropertySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductPropertyDetailsAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsManagerOrSuperUser,)
    queryset = ProductProperty.objects.all()
    serializer_class = ProductPropertySerializer


# Order and Cart section

class CartsAPIView(ListCreateAPIView):
    permission_classes = (IsManagerOrSuperUser,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__id', 'id')


class CartDetailsAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsManagerOrSuperUser,)
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class CartItemsAPIView(ListCreateAPIView):
    permission_classes = (IsManagerOrSuperUser,)
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('cart__id', 'id')


class CartItemDetailsAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsManagerOrSuperUser,)
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer


class OrdersAPIView(ListCreateAPIView):
    permission_classes = (IsManagerOrSuperUser,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('user__id', 'id')


class OrderDetailsAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsManagerOrSuperUser,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class OrderItemsAPIView(ListCreateAPIView):
    permission_classes = (IsManagerOrSuperUser,)
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

    filter_backends = (filters.SearchFilter,)
    search_fields = ('order__id', 'id')


class OrderItemDetailsAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsManagerOrSuperUser,)
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
