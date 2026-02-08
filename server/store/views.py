from rest_framework import viewsets
from rest_framework import permissions
from .models import Product, Order, Payment
from .serializers import ProductSerializer, OrderSerializer, PaymentSerializer


# Product viewset
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]  # Allow anyone to view products
    

# Order viewset
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can manage orders
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Set the user to the currently authenticated user


# Payment viewset
class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can manage payments
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Set the user to the currently authenticated user            
