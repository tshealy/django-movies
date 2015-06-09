# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviebase', '0003_auto_20150609_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=100, null=True)),
                ('genre', models.CharField(max_length=20, choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Animation', 'Animation'), ("Children's", "Children's"), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Documentary', 'Documentary'), ('Drama', 'Drama'), ('Fantasy', 'Fantasy'), ('Film-Noir', 'Film-Noir'), ('Horror', 'Horror'), ('Musical', 'Musical'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Sci-Fi', 'Sci-Fi'), ('Thriller', 'Thriller'), ('War', 'War'), ('Western', 'Western')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('rating', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], null=True)),
                ('timestamp', models.DateTimeField(null=True)),
                ('movie', models.ForeignKey(to='moviebase.Movie', null=True)),
                ('user', models.ForeignKey(to='moviebase.Rater', null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='movie',
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='user',
        ),
        migrations.DeleteModel(
            name='Movies',
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
    ]
