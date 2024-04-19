from django.urls import path

from .views import *

urlpatterns = [
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
]
