from django.shortcuts import get_object_or_404
from rest_framework.serializers import ModelSerializer

from mainApp.models import ProductImage
from mainApp.serializers import ProductSerializer, ProductImageSerializer
from .models import *


class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class ProductForCartItemSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'brand')

    def to_representation(self, instance):
        product = super(ProductForCartItemSerializer, self).to_representation(instance)
        images = ProductImage.objects.filter(product=instance).first()
        serializer = ProductImageSerializer(images)
        product.update(
            {
                'image': serializer.data.get('image'),
            }
        )
        return product


class CartItemSerializer(ModelSerializer):
    product = ProductForCartItemSerializer()

    class Meta:
        model = CartItem
        fields = ('id', 'product', 'amount')


class CartItemPostSerializer(ModelSerializer):
    class Meta:
        model = CartItem
        fields = ('id', 'product', 'amount')


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

    def to_representation(self, instance):
        order = super(OrderSerializer, self).to_representation(instance)
        orderItems = OrderItem.objects.filter(order=instance)
        serializer = OrderItemSerializer(orderItems, many=True)
        order.update({'products': serializer.data})
        return order


class ProductForOrderItemSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'brand')

    def to_representation(self, instance):
        product = super(ProductForOrderItemSerializer, self).to_representation(instance)
        images = ProductImage.objects.filter(product=instance).first()
        serializer = ProductImageSerializer(images)
        product.update(
            {
                'image': serializer.data.get('image'),
            }
        )
        return product


class OrderItemSerializer(ModelSerializer):
    product = ProductForOrderItemSerializer()

    class Meta:
        model = OrderItem
        fields = '__all__'
