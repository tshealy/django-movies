# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import moviebase.models


class Migration(migrations.Migration):

    dependencies = [
        ('moviebase', '0010_auto_20150615_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre',
            field=models.CharField(choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Animation', 'Animation'), ("Children's", "Children's"), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Documentary', 'Documentary'), ('Drama', 'Drama'), ('Fantasy', 'Fantasy'), ('Film-Noir', 'Film-Noir'), ('Horror', 'Horror'), ('Musical', 'Musical'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Sci-Fi', 'Sci-Fi'), ('Thriller', 'Thriller'), ('War', 'War'), ('Western', 'Western')], null=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True, validators=[moviebase.models.validate_ratings]),
        ),
    ]
