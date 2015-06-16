# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviebase', '0008_rater_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('genre', models.CharField(max_length=255, choices=[('Action', 'Action'), ('Adventure', 'Adventure'), ('Animation', 'Animation'), ("Children's", "Children's"), ('Comedy', 'Comedy'), ('Crime', 'Crime'), ('Documentary', 'Documentary'), ('Drama', 'Drama'), ('Fantasy', 'Fantasy'), ('Film-Noir', 'Film-Noir'), ('Horror', 'Horror'), ('Musical', 'Musical'), ('Mystery', 'Mystery'), ('Romance', 'Romance'), ('Sci-Fi', 'Sci-Fi'), ('Thriller', 'Thriller'), ('War', 'War'), ('Western', 'Western')], null=True)),
            ],
        ),
        migrations.AddField(
            model_name='rating',
            name='posted_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='text_rating',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='rater',
            name='gender',
            field=models.CharField(max_length=255, choices=[('M', 'Male'), ('F', 'Female')]),
        ),
        migrations.AddField(
            model_name='movie',
            name='genre',
            field=models.ManyToManyField(to='moviebase.Genre'),
        ),
    ]
