# Generated by Django 4.2 on 2023-08-16 19:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Sjak', '0002_alter_sjakbooking_quantity_alter_sjakbooking_remarks_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sjakbooking',
            name='use_date',
        ),
        migrations.AddField(
            model_name='sjakbooking',
            name='end',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='End'),
        ),
        migrations.AddField(
            model_name='sjakbooking',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start'),
        ),
    ]
