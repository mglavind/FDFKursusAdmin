# Generated by Django 4.2 on 2023-10-13 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Butikken', '0011_alter_mealbooking_friday_dinner_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='butikkenbooking',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Udleveret', 'Udleveret')], default='Pending', max_length=10),
        ),
    ]