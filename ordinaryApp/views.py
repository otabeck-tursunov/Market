from django.db.models import Q, Avg
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.generics import *
from rest_framework.response import Response
from rest_framework.permissions import *

from mainApp.models import Category, Product, News
from mainApp.serializers import CategorySerializer, ProductSerializer, NewsSerializer
from orderApp.models import Cart, CartItem, Order, OrderItem
from orderApp.serializers import CartItemSerializer, CartItemPostSerializer, OrderSerializer
from userApp.models import Profile
from userApp.permissions import IsOrdinaryUser
from userApp.serializers import ProfileSerializer, ProfileOrdinarySerializer
from userApp.serializers import *


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

    @swagger_auto_schema(
        request_body=CartItemPostSerializer,
    )
    def post(self, request):
        serializer = CartItemPostSerializer(data=request.data)
        if serializer.is_valid():
            cart = Cart.objects.filter(user=request.user)
            if not cart.exists():
                Cart.objects.create(user=request.user)
                cart = Cart.objects.filter(user=request.user)
            serializer.save(cart=cart.first())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartItemRetrieveAPIView(RetrieveAPIView):
    permission_classes = (IsOrdinaryUser,)
    serializer_class = CartItemSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            cartItems = CartItem.objects.filter(cart__user__id=user.id)
            return cartItems
        return CartItem.objects.filter(id=0)


class CartItemUpdateAPIView(UpdateAPIView):
    permission_classes = (IsOrdinaryUser,)
    serializer_class = CartItemPostSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            cartItems = CartItem.objects.filter(cart__user__id=user.id)
            return cartItems
        return CartItem.objects.filter(id=0)

    @swagger_auto_schema(
        request_body=CartItemSerializer
    )
    def perform_update(self, serializer):
        cartItem = CartItem.objects.get(pk=self.kwargs['pk'])
        cartItem.amount = serializer.validated_data['amount']
        cartItem.save()
        return cartItem


class CartItemDeleteAPIView(DestroyAPIView):
    permission_classes = (IsOrdinaryUser,)
    serializer_class = CartItemSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            user = self.request.user
            cartItems = CartItem.objects.filter(cart__user__id=user.id)
            return cartItems
        return CartItem.objects.filter(id=0)


# Orders
class OrdersAPIView(APIView):
    permission_classes = (IsOrdinaryUser,)

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='status',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                enum=['pending', 'canceled', 'confirmed', 'paid', 'done']
            )
        ]
    )
    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        status = request.query_params.get('status', None)
        if status is not None:
            orders = orders.filter(status=status)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)


class OrderCreateAPIView(APIView):
    permission_classes = (IsOrdinaryUser,)

    def post(self, request):
        cart = Cart.objects.filter(user=request.user)
        if not cart.exists():
            Cart.objects.create(user=request.user)
        cartItems = CartItem.objects.filter(cart__user__id=request.user.id)
        if cartItems.exists():
            order = Order.objects.create(
                user=request.user,
                status='pending',
                total_price=0
            )
            for cartItem in cartItems:
                orderItem = OrderItem.objects.create(
                    order=order,
                    product=cartItem.product,
                    amount=cartItem.amount,
                )
                order.total_price += orderItem.amount * orderItem.product.price
                order.save()
            CartItem.objects.filter(cart__user__id=request.user.id).delete()
            serializer = OrderSerializer(order)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response({
            "success": False,
            "message": "Cart is empty"
        })


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


class ProductsPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 100


class ProductsAPIView(APIView):
    permission_classes = (AllowAny,)
    pagination_class = ProductsPagination

    @swagger_auto_schema(
        manual_parameters=[
            openapi.Parameter(
                name='id',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description='Filter by ID',
            ),
            openapi.Parameter(
                name='search',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_STRING,
                description='Search by name, brand, country, color, category',
            ),
            openapi.Parameter(
                name='discount',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_BOOLEAN,
                description='Filter by discount',
            ),
            openapi.Parameter(
                name='page',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description='Page number',
            ),
            openapi.Parameter(
                name='page_size',
                in_=openapi.IN_QUERY,
                type=openapi.TYPE_INTEGER,
                description='Number of items per page',
            ),
        ]
    )
    def get(self, request):
        products = Product.objects.order_by('id')
        if request.query_params.get('id'):
            products = products.filter(id=request.query_params.get('id'))
        if request.query_params.get('search'):
            search = request.query_params.get('search')
            products = products.filter(
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

        paginator = self.pagination_class()
        paginated_products = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(paginated_products, many=True)
        return paginator.get_paginated_response(serializer.data)


class ProductDetailsAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny, ]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class NewsListAPIView(ListAPIView):
    permission_classes = [AllowAny, ]
    queryset = News.objects.order_by('-id')
    serializer_class = NewsSerializer


class NewsDetailsAPIView(RetrieveAPIView):
    permission_classes = (AllowAny,)
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class ProductLikeAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        liked_products = ProductLike.objects.filter(profile=request.user)
        serializer = ProductLikeSerializer(liked_products, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        request_body=ProductLikePostSerializer
    )
    def post(self, request):
        serializer = ProductLikePostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(profile=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDislikeAPIView(APIView):
    permission_classes = (IsOrdinaryUser,)

    def delete(self, request, id):
        liked_product = get_object_or_404(ProductLike, profile=request.user, id=id)
        liked_product.delete()
        return Response({"success": True}, status=status.HTTP_204_NO_CONTENT)


class ProductRatePostAPIView(APIView):
    permission_classes = (IsOrdinaryUser,)

    @swagger_auto_schema(
        request_body=ProductRatePostSerializer
    )
    def post(self, request):
        serializer = ProductRatePostSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save(profile=request.user)
                product = Product.objects.get(id=serializer.data['product'])
                product.rating = Avg(ProductRate.objects.filter(product=product).values_list('rate', flat=True))
                product.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"success": False, "message": "Alredy exists!"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
