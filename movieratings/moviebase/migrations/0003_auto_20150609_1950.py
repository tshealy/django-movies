# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviebase', '0002_auto_20150609_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rater',
            name='rater_id',
        ),
        migrations.AddField(
            model_name='movies',
            name='genre',
            field=models.CharField(max_length=20, null=True, choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Animation', 'Animation'), ("Children's", "Children's"), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Documentary', 'Documentary'), ('Drama', 'Drama'), ('Fantasy', 'Fantasy'), ('Film-Noir', 'Film-Noir'), ('Horror', 'Horror'), ('Musical', 'Musical'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Sci-Fi', 'Sci-Fi'), ('Thriller', 'Thriller'), ('War', 'War'), ('Western', 'Western')]),
        ),
        migrations.AddField(
            model_name='movies',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ratings',
            name='movie',
            field=models.ForeignKey(to='moviebase.Movies', null=True),
        ),
        migrations.AddField(
            model_name='ratings',
            name='rating',
            field=models.IntegerField(null=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.AddField(
            model_name='ratings',
            name='timestamp',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='ratings',
            name='user',
            field=models.ForeignKey(to='moviebase.Rater', null=True),
        ),
        migrations.AlterField(
            model_name='rater',
            name='job',
            field=models.IntegerField(default=0, choices=[(0, 'other'), (1, 'academic/educator'), (2, 'artist'), (3, 'clerical/admin'), (4, 'college/grad student'), (5, 'customer service'), (6, 'doctor/health care'), (7, 'executive/managerial'), (8, 'farmer'), (9, 'homemaker'), (10, 'K-12 student'), (11, 'lawyer'), (12, 'programmer'), (13, 'retired'), (14, 'sales/marketing'), (15, 'scientist'), (16, 'self-employed'), (17, 'technician/engineer'), (18, 'tradesman/craftsman'), (19, 'unemployed'), (20, 'writer')]),
        ),
        migrations.AlterField(
            model_name='rater',
            name='postal_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
