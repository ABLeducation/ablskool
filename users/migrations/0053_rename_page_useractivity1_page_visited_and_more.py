# Generated by Django 5.0.6 on 2024-07-05 12:26

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0052_useractivity1'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useractivity1',
            old_name='page',
            new_name='page_visited',
        ),
        migrations.RemoveField(
            model_name='useractivity1',
            name='duration',
        ),
        migrations.AddField(
            model_name='useractivity1',
            name='login_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useractivity1',
            name='logout_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='useractivity1',
            name='time_spent',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='useractivity1',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
