# Generated by Django 4.2 on 2023-08-11 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teknik', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teknikitem',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='teknikitem',
            name='type',
        ),
    ]
