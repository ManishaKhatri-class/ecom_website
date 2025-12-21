from django.db import models
from django.core.validators import RegexValidator,EmailValidator
from django.core.exceptions import ValidationError



#mobile validator
mobile_validator=RegexValidator(
	regex=r'^[6-9]\d{9}$',
	message="Enter a valid 10 digit indian mobile number!")



class Register(models.Model):
	name=models.CharField(max_length=100)
	Email=models.EmailField(unique=True,validators=[EmailValidator(message="Enter a valid email!")])
	mobile_number=models.CharField(max_length=15,unique=True,validators=[mobile_validator],error_messages={'unique':
		'This mobile number already exists!'})
	is_verified=models.BooleanField(default=False)
	is_active=models.BooleanField(default=True)
	password=models.CharField(max_length=100)
	created_at=models.DateTimeField(auto_now_add=True)
	#save 
	def save(self,*args,**kwargs):
		#hashing password
		if not self.password.startwith('pbdkdf2_'):
			self.password=make_password(self.password)
			super().save(*args,**kwargs)


		def __str__(self):
			return self.email


