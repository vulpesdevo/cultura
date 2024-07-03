# Generated by Django 4.1.13 on 2024-07-03 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('post_id', models.CharField(max_length=255, null=True)),
                ('replied_to', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('_id', djongo.models.fields.ObjectIdField(auto_created=True, primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(default=None, max_length=255)),
                ('content', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images')),
                ('country', models.CharField(max_length=200)),
                ('itinerary', models.CharField(blank=True, max_length=200, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('likes', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SaveItinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_name', models.CharField(max_length=50)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='main_images')),
                ('main_title', models.CharField(max_length=255)),
                ('main_description', models.CharField(max_length=255)),
                ('gen_tips', models.CharField(max_length=255)),
                ('total_budget', models.FloatField()),
                ('itineraries', models.CharField(default=list, max_length=255)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('status', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Itinerary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator_name', models.CharField(max_length=50)),
                ('place_image', models.ImageField(blank=True, null=True, upload_to='place_images')),
                ('title', models.CharField(max_length=255)),
                ('longitude', models.FloatField()),
                ('latitude', models.FloatField()),
                ('place_name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('budget', models.FloatField(blank=True, null=True)),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(default='onqueue', max_length=255)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CulturaUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=120)),
                ('country', models.CharField(blank=True, max_length=120, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('is_active', models.BooleanField(default=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
