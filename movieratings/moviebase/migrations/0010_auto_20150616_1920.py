# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import moviebase.models


class Migration(migrations.Migration):

    dependencies = [
        ('moviebase', '0009_auto_20150615_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(validators=[moviebase.models.validating_rating], null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.AlterUniqueTogether(
            name='rating',
            unique_together=set([('rater', 'movie')]),
        ),
    ]
