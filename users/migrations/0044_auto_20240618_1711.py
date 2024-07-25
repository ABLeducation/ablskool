# Generated by Django 3.2.20 on 2024-06-18 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0043_macroplanner_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competition',
            name='school',
            field=models.CharField(choices=[('Sparsh Global School,Greater Noida', 'Sparsh Global SChool,Greater Noida'), ('JP International School, Greater Noida', 'JP International School, Greater Noida'), ('SPS,Sonipat', 'SPS,Sonipat'), ('Vivekanand School,Delhi', 'Vivekanand School,Delhi'), ('Blooming Dale School,Budaun', 'Blooming Dale School,Budaun'), ('Satya Prakash Public School,Jabalpur', 'Satya Prakash Public School,Jabalpur')], max_length=100),
        ),
        migrations.AlterField(
            model_name='guestsession',
            name='school',
            field=models.CharField(choices=[('Sparsh Global School,Greater Noida', 'Sparsh Global SChool,Greater Noida'), ('JP International School, Greater Noida', 'JP International School, Greater Noida'), ('SPS,Sonipat', 'SPS,Sonipat'), ('Vivekanand School,Delhi', 'Vivekanand School,Delhi'), ('Blooming Dale School,Budaun', 'Blooming Dale School,Budaun'), ('Satya Prakash Public School,Jabalpur', 'Satya Prakash Public School,Jabalpur')], max_length=100),
        ),
        migrations.AlterField(
            model_name='innovationclub',
            name='school',
            field=models.CharField(choices=[('Sparsh Global School,Greater Noida', 'Sparsh Global SChool,Greater Noida'), ('JP International School, Greater Noida', 'JP International School, Greater Noida'), ('SPS,Sonipat', 'SPS,Sonipat'), ('Vivekanand School,Delhi', 'Vivekanand School,Delhi'), ('Blooming Dale School,Budaun', 'Blooming Dale School,Budaun'), ('Satya Prakash Public School,Jabalpur', 'Satya Prakash Public School,Jabalpur')], max_length=100),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='school',
            field=models.CharField(choices=[('Sparsh Global School,Greater Noida', 'Sparsh Global School,Greater Noida'), ('JP International School, Greater Noida', 'JP International School, Greater Noida'), ('SPS,Sonipat', 'SPS,Sonipat'), ('Vivekanand School,Delhi', 'Vivekanand School,Delhi'), ('Blooming Dale School,Budaun', 'Blooming Dale School,Budaun'), ('Satya Prakash Public School,Jabalpur', 'Satya Prakash Public School,Jabalpur')], max_length=100),
        ),
        migrations.AlterField(
            model_name='kreativityshow',
            name='school',
            field=models.CharField(choices=[('Sparsh Global School,Greater Noida', 'Sparsh Global SChool,Greater Noida'), ('JP International School, Greater Noida', 'JP International School, Greater Noida'), ('SPS,Sonipat', 'SPS,Sonipat'), ('Vivekanand School,Delhi', 'Vivekanand School,Delhi'), ('Blooming Dale School,Budaun', 'Blooming Dale School,Budaun'), ('Satya Prakash Public School,Jabalpur', 'Satya Prakash Public School,Jabalpur')], max_length=100),
        ),
        migrations.AlterField(
            model_name='schoolcontract',
            name='school',
            field=models.CharField(choices=[('Sparsh Global School,Greater Noida', 'Sparsh Global SChool,Greater Noida'), ('JP International School, Greater Noida', 'JP International School, Greater Noida'), ('SPS,Sonipat', 'SPS,Sonipat'), ('Vivekanand School,Delhi', 'Vivekanand School,Delhi'), ('Blooming Dale School,Budaun', 'Blooming Dale School,Budaun'), ('Satya Prakash Public School,Jabalpur', 'Satya Prakash Public School,Jabalpur')], max_length=100),
        ),
        migrations.AlterField(
            model_name='schoolgallery',
            name='school',
            field=models.CharField(choices=[('Sparsh Global School,Greater Noida', 'Sparsh Global SChool,Greater Noida'), ('JP International School, Greater Noida', 'JP International School, Greater Noida'), ('SPS,Sonipat', 'SPS,Sonipat'), ('Vivekanand School,Delhi', 'Vivekanand School,Delhi'), ('Blooming Dale School,Budaun', 'Blooming Dale School,Budaun'), ('Satya Prakash Public School,Jabalpur', 'Satya Prakash Public School,Jabalpur')], max_length=100),
        ),
    ]