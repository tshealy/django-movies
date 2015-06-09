# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moviebase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='rater',
            name='job',
            field=models.CharField(choices=[('other', 'other'), ('academic/educator', 'academic/educator'), ('artist', 'artist'), ('clerical/admin', 'clerical/admin'), ('college/grad student', 'college/grad student'), ('customer service', 'customer service'), ('doctor/health care', 'doctor/health care'), ('executive/managerial', 'executive/managerial'), ('farmer', 'farmer'), ('homemaker', 'homemaker'), ('K-12 student', 'K-12 student'), ('lawyer', 'lawyer'), ('programmer', 'programmer'), ('retired', 'retired'), ('sales/marketing', 'sales/marketing'), ('scientist', 'scientist'), ('self-employed', 'self-employed'), ('technician/engineer', 'technician/engineer'), ('tradesman/craftsman', 'tradesman/craftsman'), ('unemployed', 'unemployed'), ('writer', 'writer')], default='other', max_length=20),
        ),
        migrations.AddField(
            model_name='rater',
            name='postal_code',
            field=models.CharField(default='00000', max_length=10),
        ),
        migrations.AddField(
            model_name='rater',
            name='rater_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='rater',
            name='age',
            field=models.IntegerField(choices=[(1, 'Under 18'), (18, '18-24'), (25, '25-34'), (35, '35-44'), (45, '45-49'), (50, '50-55'), (56, '56+')]),
        ),
    ]
