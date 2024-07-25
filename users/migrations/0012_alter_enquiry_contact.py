# Generated by Django 3.2.20 on 2023-09-22 14:57

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20230922_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='contact',
            field=models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Enter a valid mobile number.', regex=re.compile('^\\d{3}-\\d{3}-\\d{4}$|^\\d{10}$'))]),
        ),
    ]
