# Generated by Django 3.2.20 on 2024-06-18 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0042_auto_20240614_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='macroplanner',
            name='grade',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]