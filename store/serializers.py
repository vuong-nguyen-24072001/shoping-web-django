from django.db import models
from django.db.models import fields
from rest_framework import serializers
from .models import Product, OrderItem

class GetAllProductSerializer(serializers.ModelSerializer):
    category = serializers.CharField()
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = Product
        fields = ['id', 'category','name', 'image_url', 'price', 'description']

    def get_image_url(self, obj):
        return obj.image.url

class GetAllCartItemSerializer(serializers.ModelSerializer):
    product = serializers.CharField()
    order = serializers.CharField()

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'order', 'quantity', 'date_added']