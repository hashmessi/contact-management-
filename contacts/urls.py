from django.urls import path
from .views import (
    ContactListView,
    ContactCreateView,
    ContactDetailView,
    ContactUpdateView,
    ContactDeleteView,
    ToggleFavoriteView,
    ExportContactsView,
    ImportContactsView
)

app_name = 'contacts'

urlpatterns = [
    path('', ContactListView.as_view(), name='contact_list'),
    path('add/', ContactCreateView.as_view(), name='contact_create'),
    path('export/', ExportContactsView.as_view(), name='contact_export'),
    path('import/', ImportContactsView.as_view(), name='contact_import'),
    path('<int:pk>/', ContactDetailView.as_view(), name='contact_detail'),
    path('<int:pk>/edit/', ContactUpdateView.as_view(), name='contact_update'),
    path('<int:pk>/delete/', ContactDeleteView.as_view(), name='contact_delete'),
    path('<int:pk>/favorite/', ToggleFavoriteView.as_view(), name='toggle_favorite'),
]
