# Generated by Django 5.0.2 on 2024-03-21 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0008_commentspost_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentspost',
            name='time',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]