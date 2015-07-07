# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('engineers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='engineer',
            name='user',
        ),
        migrations.AddField(
            model_name='engineer',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
