# Generated by Django 5.0.4 on 2024-04-19 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='confirmation_code',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='confirmed',
        ),
    ]