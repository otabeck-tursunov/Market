from django.urls import path

from .views import *

urlpatterns = [
    path('news/', NewsAPIView.as_view()),
    path('news/<int:pk>/', NewsDetailsAPIView.as_view()),

    path('profiles/', ProfilesAPIView.as_view()),
    path('profiles/<int:pk>/', ProfileDetailsAPIView.as_view()),

    path('categories/', CategoriesAPIView.as_view()),
    path('categories/<int:pk>/', CategoryDetailsAPIView.as_view()),

    path('products/', ProductsAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailsAPIView.as_view()),

    path('product-images/', ProductImagesAPIView.as_view()),
    path('product-images/<int:pk>/', ProductImageDetailsAPIView.as_view()),

    path('product-properties/', ProductPropertiesAPIView.as_view()),
    path('product-properties/<int:pk>/', ProductPropertyDetailsAPIView.as_view()),

    path('carts/', CartsAPIView.as_view()),
    path('carts/<int:pk>/', CartDetailsAPIView.as_view()),

    path('cart-items/', CartItemsAPIView.as_view()),
    path('cart-items/<int:pk>/', CartItemDetailsAPIView.as_view()),

    path('orders/', OrdersAPIView.as_view()),
    path('orders/<int:pk>/', OrderDetailsAPIView.as_view()),

    path('order-items/', OrderItemsAPIView.as_view()),
    path('order-items/<int:pk>/', OrderItemDetailsAPIView.as_view()),

]
