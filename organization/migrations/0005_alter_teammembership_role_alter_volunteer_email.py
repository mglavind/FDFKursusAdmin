# Generated by Django 4.2 on 2023-08-23 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0004_volunteer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammembership',
            name='role',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
