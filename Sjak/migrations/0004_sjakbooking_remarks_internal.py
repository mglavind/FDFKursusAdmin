# Generated by Django 4.2 on 2023-08-23 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sjak', '0003_remove_sjakbooking_use_date_sjakbooking_end_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sjakbooking',
            name='remarks_internal',
            field=models.TextField(blank=True),
        ),
    ]
