# Generated by Django 5.0.1 on 2024-01-17 11:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Sjak', '0015_sjakitem_test'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sjakitem',
            old_name='test',
            new_name='item_type',
        ),
        migrations.RemoveField(
            model_name='sjakitem',
            name='type',
        ),
    ]
