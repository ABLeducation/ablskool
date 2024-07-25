# Generated by Django 3.2.20 on 2023-08-10 17:28

import autoslug.fields
import curriculum.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0006_studentresult'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mechanzo_kit_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kit_id', models.CharField(max_length=50)),
                ('kit_name', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from=models.CharField(max_length=50))),
            ],
        ),
        migrations.CreateModel(
            name='Mechanzo_model_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_id', models.CharField(max_length=50)),
                ('model_name', models.CharField(max_length=50)),
                ('slug', autoslug.fields.AutoSlugField(blank=True, editable=False, null=True, populate_from=models.CharField(max_length=50))),
                ('file', models.FileField(blank=True, upload_to=curriculum.models.save_mechanzo_file, verbose_name='Mechanzo')),
                ('kit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mechanzo_models', to='curriculum.mechanzo_kit_name')),
            ],
        ),
    ]