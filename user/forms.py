

from django import forms
from .models import CustomUser
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    mobile_number = forms.CharField(max_length=10)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
         #username check


    def clean_username(self):
        username=self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Username already Exists')
        return username
     #email check

    def clean_email(self):
        email=self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Email already Exists')
        return email

     #password check
   
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

        return cleaned_data

        #mobile number check
    def clean_mobile_number(self):
        mobile_number=self.cleaned_data['mobile_number']
        if CustomUser.objects.filter(mobile_number=mobile_number).exists():
            raise forms.ValidationError('Mobile Number already Exists')
        return mobile_number

class LoginForm(forms.Form):
    username_or_email = forms.CharField(label="Username or Email")
    password = forms.CharField(widget=forms.PasswordInput)
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['mobile_number','profile_pic']
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','email']

