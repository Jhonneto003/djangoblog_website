# Generated by Django 5.0.2 on 2024-02-22 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0002_blogpost_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='thumbnail',
            field=models.ImageField(default='default.jpg', upload_to='thumbnails'),
        ),
    ]
