from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomerUser

class CustomerUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomerUser
        fields = ['username', 'email', 'phone_number', 'city', 'country']

class CustomerUserEditForm(forms.ModelForm):
    class Meta:
        model = CustomerUser
        fields = ['username', 'email', 'phone_number', 'city', 'country']

class CustomerAuthenticationForm(AuthenticationForm):
    class Meta:
        model = CustomerUser
        fields = ['username', 'password']

    
