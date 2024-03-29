# Generated by Django 4.2 on 2023-08-15 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0003_remove_volunteer_phone_alter_volunteer_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepotBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DepotLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='DepotItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('description', models.TextField(max_length=500)),
                ('name', models.CharField(max_length=100)),
                ('box', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Depot.depotbox')),
            ],
        ),
        migrations.AddField(
            model_name='depotbox',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Depot.depotlocation'),
        ),
        migrations.CreateModel(
            name='DepotBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.TextField(max_length=500)),
                ('end', models.DateTimeField()),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('start', models.DateTimeField()),
                ('status', models.CharField(max_length=100)),
                ('quantity', models.BigIntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Depot.depotitem')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.team')),
                ('team_contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
