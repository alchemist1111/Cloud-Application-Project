from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import UserManager

# user model
class User(AbstractUser):
    USER_ROLES = (
        ('customer', 'Customer'),
        ('admin', 'Admin'),
    )
    username = None 
    email = models.EmailField(unique=True, db_index=True)
    phone_number = models.CharField(max_length=20, unique=True)
    role = models.CharField(max_length=20, choices=USER_ROLES, default='customer')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    # Fields for use
    USERNAME_FIELD = 'email' # Use email for authentication, not username
    REQUIRED_FIELDS = []
    
    objects = UserManager() # Use custom user manager for creating users and superusers
    
    class Meta:
        """Class for defining user table constraints and indexes"""
        db_table = 'user'
        constraints = [
            models.UniqueConstraint(fields=['email'], name='unique_user_email')
        ]
        
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['email']),
            models.Index(fields=['phone_number']),
            models.Index(fields=['role']),
            models.Index(fields=['email', 'role']),
            models.Index(fields=['created_at'])
        ]
    
    
    def __str__(self):
        return f'Name:{self.first_name} {self.last_name}, Email:{self.email}'
    

# User profile model
class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        """Class for defining user profile table indexes"""
        db_table = 'user_profile'
        indexes = [
            models.Index(fields=['id']),
            models.Index(fields=['user']),
            models.Index(fields=['city']),
            models.Index(fields=['state']),
            models.Index(fields=['country']),
            models.Index(fields=['postal_code']),
            models.Index(fields=['created_at'])
        ]
    
    def __str__(self):
        return f"Profile of {self.user.first_name} {self.user.last_name}"             
