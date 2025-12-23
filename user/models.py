from django.db import models

from django.core.validators import RegexValidator
from django.contrib.auth.models import User

mobile_validator = RegexValidator(
    regex=r'^[6-9]\d{9}$',
    message="Enter a valid 10-digit Indian mobile number!"
)

class CustomUser(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    mobile_number = models.CharField(max_length=15, unique=True, validators=[mobile_validator])
    def __str__(self):
        return self.user.username

