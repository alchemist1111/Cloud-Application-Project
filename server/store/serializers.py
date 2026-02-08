from rest_framework import serializers
from .models import Product, Order, Payment

# Product serializer
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


# Order serializer
class OrderSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    product = ProductSerializer(read_only=True)  # Nested product details
    
    
    class Meta:
        model = Order
        fields = '__all__'


# Payment serializer
class PaymentSerializer(serializers.ModelSerializer):
    order = OrderSerializer(read_only=True)  # Nested order details
    
    class Meta:
        model = Payment
        fields = '__all__'                