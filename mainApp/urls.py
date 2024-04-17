from django.urls import path

from .views import *

urlpatterns = [
    path('categories/', CategoriesAPIView.as_view()),
    path('products/', ProductsAPIView.as_view()),

]