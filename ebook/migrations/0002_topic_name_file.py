# Generated by Django 3.2.20 on 2024-01-22 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic_name',
            name='file',
            field=models.URLField(default='', max_length=300, verbose_name='Ebook Lesson'),
        ),
    ]
