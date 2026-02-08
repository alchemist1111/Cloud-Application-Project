from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, OrderViewSet, PaymentViewSet

# Create a router and register our viewsets with it
router = DefaultRouter()

# Register viewsets with the router
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'payments', PaymentViewSet)

# url patterns for the store app
urlpatterns = [
    path('', include(router.urls)),  # Include all router-generated URLs
]