# Generated by Django 4.1.13 on 2024-12-22 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_likenotification_comment_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_reported',
            field=models.BooleanField(default=False),
        ),
    ]