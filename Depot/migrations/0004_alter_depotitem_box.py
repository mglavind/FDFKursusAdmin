# Generated by Django 4.2 on 2023-08-28 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Depot', '0003_alter_depotbooking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='depotitem',
            name='box',
            field=models.TextField(max_length=500),
        ),
    ]
