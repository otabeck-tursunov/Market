from django.db.models import Q
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, filters
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.permissions import *

from mainApp.models import Category, Product
from mainApp.serializers import CategorySerializer, ProductSerializer
from orderApp.models import Cart, CartItem
from orderApp.serializers import CartItemSerializer, CartItemPostSerializer
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


class CartItemsAPIView(APIView):
    permission_classes = (IsOrdinaryUser,)
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('id', 'title', 'content')

    def get(self, request):
        if len(Cart.objects.filter(user=request.user)) != 1:
            cart = Cart.objects.create(user=request.user)
        else:
            cart = Cart.objects.get(user=request.user)

        cart_items = CartItem.objects.filter(cart=cart)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CartItemPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(cart=Cart.objects.get(user=request.user))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartItemRetrieveAPIView(RetrieveAPIView):
    permission_classes = (IsOrdinaryUser,)
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(cart=Cart.objects.get(user=self.request.user))


class CartItemUpdateAPIView(UpdateAPIView):
    permission_classes = (IsOrdinaryUser,)
    serializer_class = CartItemPostSerializer

    def get_queryset(self):
        return CartItem.objects.filter(cart=Cart.objects.get(user=self.request.user))

    def perform_update(self, serializer):
        cartItem = CartItem.objects.get(pk=self.kwargs['pk'])
        cartItem.amount = serializer.validated_data['amount']
        cartItem.save()
        return cartItem


class CartItemDeleteAPIView(DestroyAPIView):
    permission_classes = (IsOrdinaryUser,)
    serializer_class = CartItemSerializer

    def get_queryset(self):
        return CartItem.objects.filter(cart=Cart.objects.get(user=self.request.user))


# Categories


class CategoriesAPIView(APIView):
    permission_classes = (AllowAny,)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='ordering',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Order by ID, Title',
                enum=['id', 'title'],
                default='id'
            ),
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
        ordering = request.GET.get('ordering', None)
        categories = Category.objects.all()
        if ordering is not None:
            if ordering == 'title':
                categories = categories.order_by('title')
            elif ordering == 'id':
                categories = categories.order_by('id')
        if request.query_params.get('id'):
            categories = categories.filter(id=request.query_params.get('id'))
        if request.query_params.get('search'):
            categories = categories.filter(title__icontains=request.query_params.get('search'))
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class CategoryDetailsAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny, ]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductsAPIView(APIView):
    permission_classes = (AllowAny,)

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


class ProductDetailsAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
