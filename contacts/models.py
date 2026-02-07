from django.db import models
from django.conf import settings
from django.core.validators import RegexValidator


class Contact(models.Model):
    """
    Contact model for storing contact information.
    Each contact belongs to a specific user.
    """
    # Phone number validator
    phone_validator = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in format: '+999999999'. 9-15 digits allowed."
    )
    
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='contacts',
        verbose_name='Owner'
    )
    
    # Contact Information
    name = models.CharField(max_length=100, verbose_name='Full Name', db_index=True)
    phone = models.CharField(
        max_length=20,
        verbose_name='Phone Number',
        validators=[phone_validator]
    )
    email = models.EmailField(blank=True, verbose_name='Email Address', db_index=True)
    company = models.CharField(max_length=100, blank=True, verbose_name='Company', db_index=True)
    notes = models.TextField(blank=True, verbose_name='Notes')
    
    # Favorites
    is_favorite = models.BooleanField(default=False, verbose_name='Favorite', db_index=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')
    
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ['-is_favorite', '-created_at']  # Favorites first
        indexes = [
            models.Index(fields=['user', '-is_favorite', '-created_at']),
            models.Index(fields=['user', 'name']),
        ]
    
    def __str__(self):
        return f'{self.name} ({self.phone})'
    
    def get_initials(self):
        """Return initials for avatar display."""
        parts = self.name.split()
        if len(parts) >= 2:
            return f"{parts[0][0]}{parts[1][0]}".upper()
        return self.name[0].upper() if self.name else '?'

