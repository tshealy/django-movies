# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviebase', '0006_auto_20150610_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='timestamp',
        ),
    ]
