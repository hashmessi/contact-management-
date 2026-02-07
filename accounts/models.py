from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Custom User model for ZENVIO Contact Management System.
    Extends Django's AbstractUser to allow future customization.
    """
    email = models.EmailField(unique=True, verbose_name='Email Address')
    
    # Optional additional fields for user profile
    phone = models.CharField(max_length=20, blank=True, verbose_name='Phone Number')
    company = models.CharField(max_length=100, blank=True, verbose_name='Company')
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    def __str__(self):
        return self.email if self.email else self.username
    
    def get_full_name(self):
        """Return the first_name plus the last_name, with a space in between."""
        full_name = f'{self.first_name} {self.last_name}'.strip()
        return full_name if full_name else self.username
