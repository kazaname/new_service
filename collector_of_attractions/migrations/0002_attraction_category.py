# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-17 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collector_of_attractions', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attraction',
            name='category',
            field=models.CharField(choices=[('Muzeum', 'Muzeum'), ('Kościół', 'Kościół'), ('Zamek', 'Zamek'), ('Pomnik', 'Pomnik'), ('Galeria Sztuki', 'Galeria Sztuki'), ('Obraz', 'Obraz')], default='Muzeum', max_length=50),
            preserve_default=False,
        ),
    ]
