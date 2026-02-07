"""
ZENVIO URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from contacts.models import Contact
from django.utils import timezone
from datetime import timedelta


class HomeView(TemplateView):
    """Home page view with real user stats."""
    template_name = 'home.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        if self.request.user.is_authenticated:
            user_contacts = Contact.objects.filter(user=self.request.user)
            
            # Total contacts count
            context['total_contacts'] = user_contacts.count()
            
            # Recent contacts (last 7 days)
            week_ago = timezone.now() - timedelta(days=7)
            context['recent_contacts'] = user_contacts.filter(created_at__gte=week_ago).count()
            
            # Unique companies as "groups"
            context['groups_count'] = user_contacts.exclude(company='').values('company').distinct().count()
        else:
            context['total_contacts'] = 0
            context['recent_contacts'] = 0
            context['groups_count'] = 0
            
        return context


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
]
