# Generated by Django 2.2.5 on 2019-11-06 13:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paiement', '0002_auto_20191001_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paiement',
            name='valid_until',
            field=models.DateField(default=datetime.date(2019, 12, 1), verbose_name='valid until'),
        ),
    ]
