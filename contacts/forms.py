from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form for creating and updating contacts.
    Styled to match the ZENVIO aesthetic.
    """
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'email', 'company', 'notes']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control form-control-custom',
                'placeholder': 'John Doe'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control form-control-custom',
                'placeholder': '+1 (555) 123-4567'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control form-control-custom',
                'placeholder': 'john@example.com'
            }),
            'company': forms.TextInput(attrs={
                'class': 'form-control form-control-custom',
                'placeholder': 'Acme Inc.'
            }),
            'notes': forms.Textarea(attrs={
                'class': 'form-control form-control-custom',
                'rows': 3,
                'placeholder': 'Add any additional notes...'
            }),
        }
        labels = {
            'name': 'Full Name',
            'phone': 'Phone Number',
            'email': 'Email Address',
            'company': 'Company',
            'notes': 'Notes',
        }


class ContactSearchForm(forms.Form):
    """
    Form for searching contacts.
    """
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-custom',
            'placeholder': 'Search contacts by name, phone, or email...'
        })
    )
