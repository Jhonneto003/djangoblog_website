# Generated by Django 5.0.2 on 2024-03-20 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_commentspost'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentspost',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default='Enter'),
            preserve_default=False,
        ),
    ]
