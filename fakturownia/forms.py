from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import FV


class EditFV(ModelForm):
    class Meta:
        model = FV
        fields = ['id', 'client', 'address', 'complete_date', 'payment_method', 'iban', 'products', 'nip', 'products']
        widgets = {
            'client': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'complete_date': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_method': forms.TextInput(attrs={'class': 'form-control'}),
            'iban': forms.TextInput(attrs={'class': 'form-control'}),
            'nip': forms.TextInput(attrs={'class': 'form-control'}),
        }


class SignUpForm(UserCreationForm):
    seller_data = forms.CharField(max_length=50)
    address = forms.CharField(max_length=80)
    nip = forms.CharField(max_length=11)
    phonenumber = forms.CharField(max_length=9)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'seller_data', 'address', 'nip', 'phonenumber')

        widgets = {
            'seller_data': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'nip': forms.TextInput(attrs={'class': 'form-control'}),
            'phonenumber': forms.TextInput(attrs={'class': 'form-control'})
        }
