# Generated by Django 5.0.1 on 2024-02-11 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Butikken', '0017_butikkenbooking_start_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='butikkenbooking',
            name='for_meal',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='butikkenbooking',
            name='remarks_internal',
            field=models.TextField(blank=True),
        ),
    ]
