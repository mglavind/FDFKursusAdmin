# Generated by Django 4.2 on 2024-01-07 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0013_alter_event_deadline_aktivitetsteam_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='deadline_aktivitetsteam',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='deadline_foto',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='deadline_lokaler',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='deadline_mad',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='deadline_sjak',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='deadline_sos',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='event',
            name='deadline_teknik',
            field=models.DateField(),
        ),
    ]