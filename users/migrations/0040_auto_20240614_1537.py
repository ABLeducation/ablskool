# Generated by Django 3.2.20 on 2024-06-14 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0039_auto_20240613_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='macroplanner',
            name='school',
            field=models.CharField(choices=[('Sparsh Global SChool,Greater Noida', 'Sparsh Global SChool,Greater Noida'), ('JP International School, Greater Noida', 'JP International School, Greater Noida'), ('SPS,Sonipat', 'SPS,Sonipat'), ('Vivekanand School,Delhi', 'Vivekanand School,Delhi'), ('Blooming Dale School,Budaun', 'Blooming Dale School,Budaun'), ('Satya Prakash Public School,Jabalpur', 'Satya Prakash Public School,Jabalpur')], default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='microplanner',
            name='school',
            field=models.CharField(choices=[('Sparsh Global SChool,Greater Noida', 'Sparsh Global SChool,Greater Noida'), ('JP International School, Greater Noida', 'JP International School, Greater Noida'), ('SPS,Sonipat', 'SPS,Sonipat'), ('Vivekanand School,Delhi', 'Vivekanand School,Delhi'), ('Blooming Dale School,Budaun', 'Blooming Dale School,Budaun'), ('Satya Prakash Public School,Jabalpur', 'Satya Prakash Public School,Jabalpur')], default=None, max_length=100),
        ),
    ]
