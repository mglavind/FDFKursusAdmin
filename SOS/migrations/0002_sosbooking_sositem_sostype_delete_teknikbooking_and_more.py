# Generated by Django 4.2 on 2023-08-27 15:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_alter_teammembership_role_alter_volunteer_email'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('SOS', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SOSBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(default=datetime.datetime.now)),
                ('end', models.DateTimeField(default=datetime.datetime.now)),
                ('quantity', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Rejected', 'Rejected')], default='Pending', max_length=10)),
                ('remarks', models.TextField(blank=True)),
                ('remarks_internal', models.TextField(blank=True)),
                ('assistance_needed', models.BooleanField(blank=True, default=False)),
                ('delivery_needed', models.BooleanField(blank=True, default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SOSItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SOSType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='TeknikBooking',
        ),
        migrations.RemoveField(
            model_name='teknikitem',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='teknikitem',
            name='type',
        ),
        migrations.DeleteModel(
            name='TeknikType',
        ),
        migrations.DeleteModel(
            name='TeknikItem',
        ),
        migrations.AddField(
            model_name='sosbooking',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SOS.sositem'),
        ),
        migrations.AddField(
            model_name='sosbooking',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.team'),
        ),
        migrations.AddField(
            model_name='sosbooking',
            name='team_contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]