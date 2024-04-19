from django.contrib.auth.models import AbstractUser
from django.db import models


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

    def __str__(self):
        return self.username
