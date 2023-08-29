# Generated by Django 4.2 on 2023-08-29 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Location', '0005_alter_locationitem_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationbooking',
            name='primary_camp',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='locationbooking',
            name='remarks',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='locationbooking',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=10),
        ),
    ]
