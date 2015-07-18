# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('version', models.IntegerField()),
                ('total_time', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('QL1_1_inc', models.IntegerField(default=0, choices=[(0, 'Include'), (1, 'Exclude')])),
                ('QL1_1_loa', models.IntegerField(default=0, choices=[(0, 'No Added Value'), (2, 'Improved'), (5, 'Enhanced'), (10, 'Superior'), (20, 'Conserving'), (25, 'Restorative')])),
                ('QL1_1_exp', models.CharField(max_length=500, null=True, blank=True)),
                ('QL1_2_inc', models.IntegerField(default=0, choices=[(0, 'Include'), (1, 'Exclude')])),
                ('QL1_2_loa', models.IntegerField(default=0, choices=[(0, 'No Added Value'), (1, 'Improved'), (2, 'Enhanced'), (5, 'Superior'), (13, 'Conserving'), (16, 'Restorative')])),
                ('QL1_2_exp', models.CharField(max_length=500, null=True, blank=True)),
                ('QL1_3_inc', models.IntegerField(default=0, choices=[(0, 'Include'), (1, 'Exclude')])),
                ('QL1_3_loa', models.IntegerField(default=0, choices=[(0, 'No Added Value'), (1, 'Improved'), (2, 'Enhanced'), (5, 'Superior'), (12, 'Conserving'), (15, 'Restorative')])),
                ('QL1_3_exp', models.CharField(max_length=500, null=True, blank=True)),
                ('QL2_1_inc', models.IntegerField(default=0, choices=[(0, 'Include'), (1, 'Exclude')])),
                ('QL2_1_loa', models.IntegerField(default=0, choices=[(0, 'No Added Value'), (2, 'Improved'), (16, 'Conserving')])),
                ('QL2_1_exp', models.CharField(max_length=500, null=True, blank=True)),
                ('QL2_2_inc', models.IntegerField(default=0, choices=[(0, 'Include'), (1, 'Exclude')])),
                ('QL2_2_loa', models.IntegerField(default=0, choices=[(0, 'No Added Value'), (1, 'Improved'), (8, 'Conserving'), (11, 'Restorative')])),
                ('QL2_2_exp', models.CharField(max_length=500, null=True, blank=True)),
                ('QL2_3_inc', models.IntegerField(default=0, choices=[(0, 'Include'), (1, 'Exclude')])),
                ('QL2_3_loa', models.IntegerField(default=0, choices=[(0, 'No Added Value'), (1, 'Improved'), (2, 'Enhanced'), (4, 'Superior'), (8, 'Conserving'), (11, 'Restorative')])),
                ('QL2_3_exp', models.CharField(max_length=500, null=True, blank=True)),
                ('QL2_4_inc', models.IntegerField(default=0, choices=[(0, 'Include'), (1, 'Exclude')])),
                ('QL2_4_loa', models.IntegerField(default=0, choices=[(0, 'No Added Value'), (1, 'Improved'), (4, 'Enhanced'), (7, 'Superior'), (14, 'Conserving')])),
                ('QL2_4_exp', models.CharField(max_length=500, null=True, blank=True)),
                ('QL2_5_inc', models.IntegerField(default=0, choices=[(0, 'Include'), (1, 'Exclude')])),
                ('QL2_5_loa', models.IntegerField(default=0, choices=[(0, 'No Added Value'), (1, 'Improved'), (3, 'Enhanced'), (6, 'Superior'), (12, 'Conserving'), (15, 'Restorative')])),
                ('QL2_5_exp', models.CharField(max_length=500, null=True, blank=True)),
                ('QL2_6_inc', models.IntegerField(default=0, choices=[(0, 'Include'), (1, 'Exclude')])),
                ('QL2_6_loa', models.IntegerField(default=0, choices=[(0, 'No Added Value'), (3, 'Enhanced'), (6, 'Superior'), (12, 'Conserving'), (15, 'Restorative')])),
                ('QL2_6_exp', models.CharField(max_length=500, null=True, blank=True)),
                ('QL3_1_inc', models.IntegerField(default=0, choices=[(0, 'Include'), (1, 'Exclude')])),
                ('QL3_1_loa', models.IntegerField(default=0, choices=[(0, 'No Added Value'), (1, 'Improved'), (7, 'Superior'), (13, 'Conserving'), (16, 'Restorative')])),
                ('QL3_1_exp', models.CharField(max_length=500, null=True, blank=True)),
                ('QL3_2_inc', models.IntegerField(default=0, choices=[(0, 'Include'), (1, 'Exclude')])),
                ('QL3_2_loa', models.IntegerField(default=0, choices=[(0, 'No Added Value'), (1, 'Improved'), (3, 'Enhanced'), (6, 'Superior'), (11, 'Conserving'), (14, 'Restorative')])),
                ('QL3_2_exp', models.CharField(max_length=500, null=True, blank=True)),
                ('QL3_3_inc', models.IntegerField(default=0, choices=[(0, 'Include'), (1, 'Exclude')])),
                ('QL3_3_loa', models.IntegerField(default=0, choices=[(0, 'No Added Value'), (1, 'Improved'), (3, 'Enhanced'), (6, 'Superior'), (11, 'Conserving'), (13, 'Restorative')])),
                ('QL3_3_exp', models.CharField(max_length=500, null=True, blank=True)),
                ('engineer', models.ForeignKey(to='engineer.Engineer')),
            ],
        ),
    ]
