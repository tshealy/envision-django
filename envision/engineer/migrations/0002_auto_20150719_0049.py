# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='QL1_1_exp',
            field=models.TextField(null=True, max_length=1000, blank=True),
        ),
    ]
