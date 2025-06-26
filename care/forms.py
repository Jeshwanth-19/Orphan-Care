from django import forms
from django.contrib.auth.models import User
class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = "_all_"
        fields = ['username', 'password', 'email', 'first_name', 'last_name']
        widgets = {
            'password': forms.PasswordInput()
        }
    