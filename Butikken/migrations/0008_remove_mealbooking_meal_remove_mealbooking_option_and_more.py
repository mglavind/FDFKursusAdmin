# Generated by Django 4.2 on 2023-09-01 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Butikken', '0007_remove_mealbooking_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mealbooking',
            name='meal',
        ),
        migrations.RemoveField(
            model_name='mealbooking',
            name='option',
        ),
        migrations.AddField(
            model_name='mealbooking',
            name='monday_breakfast',
            field=models.CharField(choices=[('Spiser inde ', 'Spiser inde '), ('Morgenmadspakke', 'Morgenmadspakke'), ('Står selv for forplejning', 'Står selv for forplejning')], default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='mealbooking',
            name='monday_dinner',
            field=models.CharField(choices=[('Spiser inde ', 'Spiser inde '), ('Laver mad bestilt ved KØK', 'Laver mad bestilt ved KØK'), ('Dinner trans', 'Dinner trans'), ('DYI - Chili Con Carne med ris / Råkost', 'DYI - Chili Con Carne med ris / Råkost'), ('DYI - Ciabatta med kylling og bacon', 'DYI - Ciabatta med kylling og bacon'), ('DYI - Indisk Kartoffelcurry / Råkost', 'DYI - Indisk Kartoffelcurry / Råkost'), ('DYI - Jambalaya / Spidskålssalat', 'DYI - Jambalaya / Spidskålssalat'), ('DYI - Pasta kødsovs / Spidskålssalat', 'DYI - Pasta kødsovs / Spidskålssalat'), ('DYI - Svensk pølseret / Spidskålssalat', 'DYI - Svensk pølseret / Spidskålssalat'), ('Står selv for forplejning', 'Står selv for forplejning')], default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='mealbooking',
            name='monday_lunch',
            field=models.CharField(choices=[('Spiser inde ', 'Spiser inde '), ('Frokostpakke', 'Frokostpakke'), ('Står selv for forplejning', 'Står selv for forplejning')], default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='mealbooking',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
