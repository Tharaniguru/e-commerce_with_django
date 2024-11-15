from pyexpat import model
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms
from .models import UserPreferences
 
class CustomUserForm(UserCreationForm):
  username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter User Name'}))
  email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Email Address'}))
  password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}))
  password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Confirm Password'}))
  class Meta:
   model=User
   fields=['username','email','password1','password2']


class UserPreferencesForm(forms.ModelForm):
    class Meta:
        model = UserPreferences
        fields = ['product_1', 'product_2', 'product_3']
        widgets = {
            'product_1': forms.Select(attrs={'class': 'form-control'}),
            'product_2': forms.Select(attrs={'class': 'form-control'}),
            'product_3': forms.Select(attrs={'class': 'form-control'}),
        }