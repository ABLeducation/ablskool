# Generated by Django 3.2.20 on 2024-04-30 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0028_auto_20240429_1523'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advocacyvisit',
            name='sign_mentor',
        ),
        migrations.AddField(
            model_name='advocacyvisit',
            name='handling_comm_2',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=0),
        ),
    ]