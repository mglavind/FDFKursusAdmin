# Generated by Django 4.2 on 2023-10-06 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Butikken', '0010_mealbooking_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mealbooking',
            name='friday_dinner',
            field=models.CharField(choices=[('Fællesforplejning', 'Fællesforplejning')], default='none', max_length=200),
        ),
        migrations.AlterField(
            model_name='mealbooking',
            name='wednesday_dinner',
            field=models.CharField(choices=[('Vælg fra liste', 'Vælg fra liste'), ('Laver mad bestilt ved KØK', 'Laver mad bestilt ved KØK'), ('DYI - Chili Con Carne med ris / Råkost', 'DYI - Chili Con Carne med ris / Råkost'), ('DYI - Ciabatta med kylling og bacon', 'DYI - Ciabatta med kylling og bacon'), ('DYI - Indisk Kartoffelcurry / Råkost', 'DYI - Indisk Kartoffelcurry / Råkost'), ('DYI - Jambalaya / Spidskålssalat', 'DYI - Jambalaya / Spidskålssalat'), ('DYI - Pasta kødsovs / Spidskålssalat', 'DYI - Pasta kødsovs / Spidskålssalat'), ('DYI - Svensk pølseret / Spidskålssalat', 'DYI - Svensk pølseret / Spidskålssalat'), ('Står selv for forplejning', 'Står selv for forplejning')], default='none', max_length=200),
        ),
    ]
