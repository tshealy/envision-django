# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0002_auto_20150719_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='QL1_1_exp',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
    ]
