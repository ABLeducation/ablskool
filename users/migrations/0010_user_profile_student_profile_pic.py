# Generated by Django 3.2.20 on 2023-09-18 17:34

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20230918_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile_student',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=users.models.save_profile_image, verbose_name='Profile Image'),
        ),
    ]
