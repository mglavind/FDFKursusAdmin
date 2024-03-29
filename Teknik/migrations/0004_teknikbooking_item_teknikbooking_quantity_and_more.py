# Generated by Django 4.2 on 2023-08-12 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0003_remove_volunteer_phone_alter_volunteer_username'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Teknik', '0003_remove_teknikitem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='teknikbooking',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Teknik.teknikitem'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teknikbooking',
            name='quantity',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teknikbooking',
            name='status',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teknikbooking',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='organization.team'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='teknikbooking',
            name='team_contact',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
