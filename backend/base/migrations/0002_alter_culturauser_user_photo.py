# Generated by Django 4.1.13 on 2024-07-12 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='culturauser',
            name='user_photo',
            field=models.ImageField(blank=True, default='profile_pictures/default_profile.png', null=True, upload_to='profile_pictures'),
        ),
    ]