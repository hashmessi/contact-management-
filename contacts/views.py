from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, View
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
import csv

from .models import Contact
from .forms import ContactForm


class ContactListView(LoginRequiredMixin, ListView):
    """
    Display list of all contacts for the logged-in user.
    Includes search and filter functionality.
    """
    model = Contact
    template_name = 'contacts/contact_list.html'
    context_object_name = 'contacts'
    paginate_by = 12
    
    def get_queryset(self):
        queryset = Contact.objects.filter(user=self.request.user)
        search_query = self.request.GET.get('search', '')
        filter_type = self.request.GET.get('filter', '')
        
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(phone__icontains=search_query) |
                Q(email__icontains=search_query) |
                Q(company__icontains=search_query)
            )
        
        # Filter by favorites
        if filter_type == 'favorites':
            queryset = queryset.filter(is_favorite=True)
        
        return queryset.order_by('-is_favorite', '-created_at')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['search_query'] = self.request.GET.get('search', '')
        context['filter_type'] = self.request.GET.get('filter', '')
        
        # Optimize: Use aggregation instead of separate queries
        from django.db.models import Count, Q
        stats = Contact.objects.filter(user=self.request.user).aggregate(
            total=Count('id'),
            favorites=Count('id', filter=Q(is_favorite=True))
        )
        context['total_contacts'] = stats['total']
        context['favorites_count'] = stats['favorites']
        return context


class ContactCreateView(LoginRequiredMixin, CreateView):
    """
    Create a new contact.
    Automatically assigns the contact to the logged-in user.
    """
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/contact_form.html'
    success_url = reverse_lazy('contacts:contact_list')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, f'Contact "{form.instance.name}" created successfully!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Contact'
        context['button_text'] = 'Create Contact'
        return context


class ContactDetailView(LoginRequiredMixin, DetailView):
    """
    Display details of a single contact.
    """
    model = Contact
    template_name = 'contacts/contact_detail.html'
    context_object_name = 'contact'
    
    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)


class ContactUpdateView(LoginRequiredMixin, UpdateView):
    """
    Update an existing contact.
    """
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/contact_form.html'
    success_url = reverse_lazy('contacts:contact_list')
    
    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)
    
    def form_valid(self, form):
        messages.success(self.request, f'Contact "{form.instance.name}" updated successfully!')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Contact'
        context['button_text'] = 'Update Contact'
        return context


class ContactDeleteView(LoginRequiredMixin, DeleteView):
    """
    Delete a contact with confirmation.
    """
    model = Contact
    template_name = 'contacts/contact_confirm_delete.html'
    success_url = reverse_lazy('contacts:contact_list')
    context_object_name = 'contact'
    
    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)
    
    def form_valid(self, form):
        messages.success(self.request, f'Contact deleted successfully!')
        return super().form_valid(form)


class ToggleFavoriteView(LoginRequiredMixin, View):
    """
    Toggle favorite status of a contact.
    Supports both AJAX and regular POST requests.
    """
    def post(self, request, pk):
        contact = get_object_or_404(Contact, pk=pk, user=request.user)
        contact.is_favorite = not contact.is_favorite
        contact.save(update_fields=['is_favorite'])  # Optimize: only update one field
        
        # Check if AJAX request
        if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
            return JsonResponse({
                'success': True,
                'is_favorite': contact.is_favorite,
                'message': f'{contact.name} {"added to" if contact.is_favorite else "removed from"} favorites!'
            })
        
        # Regular POST request with success message
        status = 'added to' if contact.is_favorite else 'removed from'
        messages.success(request, f'{contact.name} {status} favorites!')
        
        # Redirect back to referring page or contact list
        return redirect(request.META.get('HTTP_REFERER', 'contacts:contact_list'))


class ExportContactsView(LoginRequiredMixin, View):
    """
    Export all user contacts to CSV file.
    """
    def get(self, request):
        contacts = Contact.objects.filter(user=request.user).order_by('name')
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="zenvio_contacts.csv"'
        
        writer = csv.writer(response)
        # Header row
        writer.writerow(['Name', 'Phone', 'Email', 'Company', 'Notes', 'Favorite', 'Created At'])
        
        # Data rows
        for contact in contacts:
            writer.writerow([
                contact.name,
                contact.phone,
                contact.email,
                contact.company,
                contact.notes,
                'Yes' if contact.is_favorite else 'No',
                contact.created_at.strftime('%Y-%m-%d %H:%M')
            ])
        
        return response


class ImportContactsView(LoginRequiredMixin, View):
    """
    Import contacts from CSV file.
    Supports CSV files with headers: Name, Phone, Email, Company, Notes
    """
    template_name = 'contacts/contact_import.html'
    MAX_FILE_SIZE = 5 * 1024 * 1024  # 5MB limit
    
    def get(self, request):
        return render(request, self.template_name)
    
    def post(self, request):
        csv_file = request.FILES.get('csv_file')
        
        # Validate file presence
        if not csv_file:
            messages.error(request, 'Please select a CSV file to upload.')
            return render(request, self.template_name)
        
        # Validate file extension
        if not csv_file.name.lower().endswith('.csv'):
            messages.error(request, 'Please upload a valid CSV file.')
            return render(request, self.template_name)
        
        # Validate file size
        if csv_file.size > self.MAX_FILE_SIZE:
            messages.error(request, 'File size exceeds 5MB limit.')
            return render(request, self.template_name)
        
        # Parse CSV
        try:
            # Decode with proper encoding handling
            try:
                decoded_file = csv_file.read().decode('utf-8').splitlines()
            except UnicodeDecodeError:
                try:
                    csv_file.seek(0)
                    decoded_file = csv_file.read().decode('latin-1').splitlines()
                except UnicodeDecodeError:
                    messages.error(request, 'File encoding error. Please use UTF-8 encoded CSV.')
                    return render(request, self.template_name)
            
            reader = csv.DictReader(decoded_file)
            
            # Validate headers
            required_headers = {'Name', 'Phone'}
            if reader.fieldnames is None:
                messages.error(request, 'CSV file appears to be empty.')
                return render(request, self.template_name)
            
            available_headers = set(reader.fieldnames)
            if not required_headers.issubset(available_headers):
                missing = required_headers - available_headers
                messages.error(request, f'CSV missing required columns: {", ".join(missing)}')
                return render(request, self.template_name)
            
            imported_count = 0
            skipped_count = 0
            errors = []
            
            for row_num, row in enumerate(reader, start=2):  # Start at 2 (1 for header)
                # Validate required fields
                name = row.get('Name', '').strip()[:100]  # Enforce max length
                phone = row.get('Phone', '').strip()[:20]
                
                if not name or not phone:
                    skipped_count += 1
                    errors.append(f"Row {row_num}: Missing name or phone")
                    continue
                
                # Create contact
                try:
                    Contact.objects.create(
                        user=request.user,
                        name=name,
                        phone=phone,
                        email=row.get('Email', '').strip()[:254],  # Email max length
                        company=row.get('Company', '').strip()[:100],
                        notes=row.get('Notes', '').strip()
                    )
                    imported_count += 1
                except Exception as e:
                    skipped_count += 1
                    errors.append(f"Row {row_num}: {str(e)}")
            
            # Show summary
            if imported_count > 0:
                messages.success(request, f'Successfully imported {imported_count} contact(s)!')
            
            if skipped_count > 0:
                messages.warning(request, f'Skipped {skipped_count} row(s) due to errors.')
                # Show first 5 errors
                for error in errors[:5]:
                    messages.error(request, error)
                if len(errors) > 5:
                    messages.info(request, f'...and {len(errors) - 5} more errors.')
            
            return redirect('contacts:contact_list')
            
        except csv.Error as e:
            messages.error(request, f'CSV parsing error: {str(e)}')
            return render(request, self.template_name)
        except Exception as e:
            messages.error(request, f'Unexpected error: {str(e)}')
            return render(request, self.template_name)

