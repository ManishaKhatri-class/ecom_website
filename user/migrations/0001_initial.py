
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(

            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, validators=[django.core.validators.EmailValidator()])),
                ('mobile_number', models.CharField(max_length=15, unique=True, validators=[django.core.validators.RegexValidator(message='Enter a valid 10-digit Indian mobile number!', regex='^[6-9]\\d{9}$')])),
                ('password', models.CharField(blank=True, max_length=128, null=True)),

