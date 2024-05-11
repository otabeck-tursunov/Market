from django.urls import path

from .views import *

urlpatterns = [
    path('profile/register/',  ProfileCreateAPIView.as_view()),
    path('profile/details/',  ProfileDetailsAPIView.as_view()),
    path('profile/update/',  ProfileUpdateAPIView.as_view()),
    path('profile/delete/',  ProfileDeleteAPIView.as_view()),

    path('profile/cart/products/', CartItemsAPIView.as_view()),
    path('profile/cart/products/<int:pk>/', CartItemRetrieveAPIView.as_view()),
    path('profile/cart/products/<int:pk>/update/', CartItemUpdateAPIView.as_view()),
    path('profile/cart/products/<int:pk>/delete/', CartItemDeleteAPIView.as_view()),

    path('profile/orders/', OrdersAPIView.as_view()),
    path('profile/order-create/', OrderCreateAPIView.as_view()),

    path('categories/', CategoriesAPIView.as_view()),
    path('categories/<int:pk>/', CategoryDetailsAPIView.as_view()),
    path('products/', ProductsAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailsAPIView.as_view()),

    path('news/', NewsListAPIView.as_view()),
    path('news/<int:pk>/', NewsDetailsAPIView.as_view()),

]