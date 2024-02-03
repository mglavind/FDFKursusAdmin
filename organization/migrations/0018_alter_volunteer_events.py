# Generated by Django 5.0.1 on 2024-01-31 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0017_auto_20240110_0005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteer',
            name='events',
            field=models.ManyToManyField(blank=True, through='organization.EventMembership', to='organization.event'),
        ),
    ]