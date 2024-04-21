from django.contrib import admin
from .models import *

admin.site.register([News, Category, Product, ProductImage, ProductProperty])