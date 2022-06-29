from dataclasses import fields
from django import forms
from .models import MyUser,Book
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = MyUser
        fields = ['username', 'phone', 'email', 'password1', 'password2']

    
    
    
    
class BookForm(forms.ModelForm):
    class Meta:
        model=Book
        fields=['game','time','date','number']
    
    
