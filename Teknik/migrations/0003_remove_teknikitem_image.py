# Generated by Django 4.2 on 2023-08-11 15:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Teknik', '0002_remove_teknikitem_image_remove_teknikitem_owner_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teknikitem',
            name='image',
        ),
    ]
