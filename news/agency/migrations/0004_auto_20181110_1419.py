# Generated by Django 2.1.2 on 2018-11-10 08:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0003_auto_20181110_1412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='withhold',
            name='from_date',
            field=models.DateTimeField(default=datetime.date(2018, 11, 10)),
        ),
        migrations.AlterField(
            model_name='withhold',
            name='to_date',
            field=models.DateTimeField(default=datetime.date(2018, 11, 10)),
        ),
    ]
