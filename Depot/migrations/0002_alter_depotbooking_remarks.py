# Generated by Django 4.2 on 2023-08-27 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depotbooking',
            name='remarks',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
