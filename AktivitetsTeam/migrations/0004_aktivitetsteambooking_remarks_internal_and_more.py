# Generated by Django 4.2 on 2023-08-21 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AktivitetsTeam', '0003_remove_aktivitetsteambooking_end_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='aktivitetsteambooking',
            name='remarks_internal',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='aktivitetsteambooking',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='aktivitetsteambooking',
            name='remarks',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
