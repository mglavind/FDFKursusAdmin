# Generated by Django 4.2 on 2023-08-28 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Location', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationitem',
            name='type',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='Location.locationtype'),
        ),
    ]