# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviebase', '0009_auto_20150615_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rater',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=255),
        ),
    ]
