from rest_framework import serializers
from .models import *


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'



class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self, instance):
        product = super(ProductSerializer, self).to_representation(instance)
        images = ProductImage.objects.filter(product__id=product['id'])
        properties = ProductProperty.objects.filter(product__id=product['id'])
        image_serializer = ProductImageSerializer(images, many=True)
        property_serializer = ProductPropertySerializer(properties, many=True)
        product.update(
            {
                'images': image_serializer.data,
                'properties': property_serializer.data
            }
        )
        return product


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductPropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductProperty
        fields = '__all__'
