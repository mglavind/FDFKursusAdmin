# Generated by Django 4.2 on 2023-08-28 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depot', '0004_alter_depotitem_box'),
    ]

    operations = [
        migrations.AddField(
            model_name='depotitem',
            name='quantity_lager',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='depotitem',
            name='unit',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
