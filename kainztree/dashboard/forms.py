# forms.py
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()


class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
