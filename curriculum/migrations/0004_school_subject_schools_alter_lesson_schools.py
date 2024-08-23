# Generated by Django 5.0.6 on 2024-08-22 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0003_alter_lesson_schools'),
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': '1. Schools',
            },
        ),
        migrations.AddField(
            model_name='subject',
            name='schools',
            field=models.ManyToManyField(blank=True, related_name='subjects', to='curriculum.school', verbose_name='Schools'),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='schools',
            field=models.ManyToManyField(blank=True, related_name='lessons', to='curriculum.school', verbose_name='Schools'),
        ),
    ]