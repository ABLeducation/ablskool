# Generated by Django 3.2.20 on 2023-11-04 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_feedbackteacher_notificationteacher'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInnovativeProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('student_name', models.CharField(max_length=100)),
                ('project_date', models.DateField()),
                ('document', models.FileField(upload_to='documents/')),
                ('video_link', models.URLField()),
            ],
        ),
    ]
