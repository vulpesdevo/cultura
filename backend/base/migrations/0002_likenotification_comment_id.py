# Generated by Django 4.1.13 on 2024-12-21 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='likenotification',
            name='comment_id',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]