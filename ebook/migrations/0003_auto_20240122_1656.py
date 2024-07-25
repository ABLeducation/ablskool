# Generated by Django 3.2.20 on 2024-01-22 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook', '0002_topic_name_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic_name',
            name='pdf',
        ),
        migrations.AlterField(
            model_name='topic_name',
            name='file',
            field=models.URLField(default='', max_length=300, verbose_name='content'),
        ),
    ]
