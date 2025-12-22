from django.db import models
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
    
