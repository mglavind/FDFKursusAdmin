# Generated by Django 4.2 on 2023-08-13 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Teknik', '0006_tekniktype'),
    ]

    operations = [
        migrations.AddField(
            model_name='teknikbooking',
            name='remarks',
            field=models.TextField(blank=True),
        ),
    ]