# Generated by Django 3.2.20 on 2023-10-10 14:13

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_feedbackprincipal_notificationprincipal'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile_principal',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to=users.models.save_profile_image, verbose_name='Profile Image'),
        ),
    ]
