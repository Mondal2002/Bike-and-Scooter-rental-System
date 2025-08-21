from django import forms
from .models import Category  # Assuming this is your Vehicle model

from django import forms

class BookingForm(forms.Form):
    # User fields
    name = forms.CharField(max_length=300, label='Full Name')
    phone = forms.CharField(max_length=15, label='Phone Number')
    email = forms.EmailField(label='Email Address')

    # Booking fields
    vehicle_name = forms.CharField(max_length=200, label='Vehicle Name')
    pickup_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Pickup Date')
    return_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label='Return Date')

