# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engineer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engineer',
            name='version',
            field=models.IntegerField(null=True),
        ),
    ]
