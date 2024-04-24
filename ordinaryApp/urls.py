from django.urls import path
from .views import *

urlpatterns = [
    path('profile/register/',  ProfileCreateAPIView.as_view()),
    path('profile/details/',  ProfileDetailsAPIView.as_view()),
    path('profile/update/',  ProfileUpdateAPIView.as_view()),
    path('profile/delete/',  ProfileDeleteAPIView.as_view()),
]