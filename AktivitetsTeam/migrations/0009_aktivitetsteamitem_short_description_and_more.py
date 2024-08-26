# Generated by Django 5.0.1 on 2024-08-24 11:13

import embed_video.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AktivitetsTeam', '0008_alter_aktivitetsteambooking_assigned_aktivitetsteam'),
    ]

    operations = [
        migrations.AddField(
            model_name='aktivitetsteamitem',
            name='short_description',
            field=models.TextField(default='Short Description', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='aktivitetsteamitem',
            name='youtube_link',
            field=embed_video.fields.EmbedVideoField(blank=True),
        ),
    ]