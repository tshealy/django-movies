# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviebase', '0005_auto_20150609_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='genre',
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(null=True, max_length=255),
        ),
    ]
