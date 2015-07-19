# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0003_auto_20150719_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rating',
            name='QL1_1_exp',
            field=models.TextField(max_length=1000, blank=True, null=True),
        ),
    ]
