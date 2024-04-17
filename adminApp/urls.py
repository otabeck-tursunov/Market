from django.urls import path

from .views import *

urlpatterns = [
    path('profiles/', ProfilesAPIView.as_view()),
    path('profiles/<int:pk>/', ProfileDetailsAPIView.as_view()),
    path('categories/', CategoriesAPIView.as_view()),
    path('products/', ProductsAPIView.as_view()),
]
