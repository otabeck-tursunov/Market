from django.contrib import admin
from django.contrib.auth.models import Group
from mainApp.models import Product
from .models import *

admin.site.register(Profile)
admin.site.unregister(Group)
