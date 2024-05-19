from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

from coreApp.models import CoreModel
from mainApp.models import Product


class Profile(AbstractUser):
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('ordinary', 'Ordinary'),
    )

    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
    )
    phone_number = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='profiles')
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='ordinary')

    # confirmation_code = models.CharField(max_length=6, blank=True, null=True)
    # confirmed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.username


class ProductLike(CoreModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='liked_profiles')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='liked_products')

    class Meta:
        unique_together = (('product', 'profile'),)


class ProductRate(CoreModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='rated_profiles')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='rated_products')
    rate = models.IntegerField(blank=True, null=True, validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = (('product', 'profile'),)
