# Generated by Django 4.2 on 2023-08-28 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depot', '0005_depotitem_quantity_lager_depotitem_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depotitem',
            name='description',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
