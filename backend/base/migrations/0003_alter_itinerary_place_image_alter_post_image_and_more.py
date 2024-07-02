# Generated by Django 4.1.13 on 2024-07-02 10:46

from django.db import migrations, models
import djongo.storage


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_itinerary_place_image_alter_post_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itinerary',
            name='place_image',
            field=models.ImageField(blank=True, null=True, storage=djongo.storage.GridFSStorage(base_url='http://localhost:5173//uploads/', collection='uploads'), upload_to='place_images'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post_images'),
        ),
        migrations.AlterField(
            model_name='saveitinerary',
            name='main_image',
            field=models.ImageField(blank=True, null=True, storage=djongo.storage.GridFSStorage(base_url='http://localhost:5173//uploads/', collection='uploads'), upload_to='main_images'),
        ),
    ]