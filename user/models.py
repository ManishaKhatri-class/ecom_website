from django.db import models
<<<<<<< HEAD
from django.core.validators import RegexValidator, EmailValidator
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User

mobile_validator = RegexValidator(
    regex=r'^[6-9]\d{9}$',
    message="Enter a valid 10-digit Indian mobile number!"
)

class CustomUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True, validators=[EmailValidator()])
    mobile_number = models.CharField(max_length=15, unique=True, validators=[mobile_validator])
    password = models.CharField(max_length=128,null=True,blank=True)  # store hashed password
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['usernam','email','mobile_number']  
    def set_password(self, raw_password):
        """Hash and set the password"""
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
       
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.username
    
=======
<<<<<<< HEAD
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


=======

# Create your models here.
>>>>>>> 93a7b86ed4178619cc4bc13f8f0f6141663a87af
>>>>>>> cb1b3181f1be4f3ce5ea799625050162a878655a
