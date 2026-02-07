from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """Contact admin configuration."""
    list_display = ['name', 'phone', 'email', 'company', 'is_favorite', 'user', 'created_at']
    list_filter = ['is_favorite', 'created_at', 'user']
    search_fields = ['name', 'phone', 'email', 'company']
    readonly_fields = ['created_at', 'updated_at']
    list_editable = ['is_favorite']  # Allow quick toggle from list view
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'phone', 'email', 'company', 'notes')
        }),
        ('Settings', {
            'fields': ('is_favorite',)
        }),
        ('Owner', {
            'fields': ('user',)
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
