from django import forms
from .models import Register


class RegisterationForm(forms.ModelForm):
	confirm_password=forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model=Register
		fields=['name','Email','mobile_number','password']
		widget={'password':forms.PasswordInput()}
		#clean to compare password and confirm password
		def clean(self):
			cleaned_data=super().clean()
			password=cleaned_data.get('password')
			confirm_password=cleaned_data.get('confirm_password')

			if password and confirm_password:
				if password !=confirm_password:
					raise forms.ValidationError("Passwords do not match")
			return cleaned_data

class LoginForm(forms.Form):
	email=forms.EmailField()
	password=forms.CharField()
	remember_me=forms.BooleanField(required=False)
