from django.core.validators import MinValueValidator
from django.db import models

from coreApp.models import CoreModel
from mainApp.models import Product
from userApp.models import Profile


class Cart(CoreModel):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s cart"


class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.cart.user.username}'s cart: {self.product.name}"


class Order(CoreModel):
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("canceled", "Canceled"),
        ("confirmed", "Confirmed"),
        ("paid", "Paid"),
        ("done", "Done")
    )
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)
    total_price = models.FloatField(validators=[MinValueValidator(0), ])

    def __str__(self):
        return f"{self.user.username}: {self.id} - {self.status}"

    def calculate_total_price(self):
        pass


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.order.user.username}: {self.product.name} {self.amount}"
