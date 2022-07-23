
from django import forms
from .models import Candidate

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CandidateForm(forms.ModelForm):
    class Meta:
        model = Candidate
        fields='__all__'




class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="" ,widget=forms.TextInput(attrs={'class': 'form-control mt-1 mb-1', 'placeholder': 'Enter your Email'}))
    
    first_name = forms.CharField(label="", max_length=30,  widget=forms.TextInput(attrs={'class': 'form-control mb-1', 'placeholder': 'Enter your First Name'}))
    last_name = forms.CharField(label="", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control ', 'placeholder': 'Enter your Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')