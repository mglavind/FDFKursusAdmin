# Generated by Django 4.2 on 2024-01-06 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0007_alter_key_current_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='eventmembership',
            old_name='member',
            new_name='volunteer',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='events',
            field=models.ManyToManyField(through='organization.EventMembership', to='organization.event'),
        ),
    ]
