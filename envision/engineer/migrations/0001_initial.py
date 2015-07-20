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
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('version', models.IntegerField()),
                ('total_time', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('QL1_1_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL1_1_loa', models.IntegerField(choices=[(0, 'No Added Value'), (2, 'Improved'), (5, 'Enhanced'), (10, 'Superior'), (20, 'Conserving'), (25, 'Restorative')], default=0)),
                ('QL1_1_exp', models.TextField(max_length=1000, blank=True, null=True)),
                ('QL1_2_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL1_2_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (2, 'Enhanced'), (5, 'Superior'), (13, 'Conserving'), (16, 'Restorative')], default=0)),
                ('QL1_2_exp', models.TextField(max_length=1000, blank=True, null=True)),
                ('QL2_3_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL2_3_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (2, 'Enhanced'), (4, 'Superior'), (8, 'Conserving'), (11, 'Restorative')], default=0)),
                ('QL2_3_exp', models.TextField(max_length=1000, blank=True, null=True)),
                ('QL2_5_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL2_5_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (3, 'Enhanced'), (6, 'Superior'), (12, 'Conserving'), (15, 'Restorative')], default=0)),
                ('QL2_5_exp', models.TextField(max_length=1000, blank=True, null=True)),
                ('QL2_6_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL2_6_loa', models.IntegerField(choices=[(0, 'No Added Value'), (3, 'Enhanced'), (6, 'Superior'), (12, 'Conserving'), (15, 'Restorative')], default=0)),
                ('QL2_6_exp', models.TextField(max_length=1000, blank=True, null=True)),
                ('QL3_3_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL3_3_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (3, 'Enhanced'), (6, 'Superior'), (11, 'Conserving'), (13, 'Restorative')], default=0)),
                ('QL3_3_exp', models.TextField(max_length=1000, blank=True, null=True)),
                ('LD1_2_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('LD1_2_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (4, 'Enhanced'), (7, 'Superior'), (14, 'Conserving')], default=0)),
                ('LD1_2_exp', models.TextField(max_length=1000, blank=True, null=True)),
                ('LD1_4_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('LD1_4_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (5, 'Enhanced'), (9, 'Superior'), (14, 'Conserving')], default=0)),
                ('LD1_4_exp', models.TextField(max_length=1000, blank=True, null=True)),
                ('LD2_2_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('LD2_2_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (3, 'Enhanced'), (7, 'Superior'), (13, 'Conserving'), (16, 'Restorative')], default=0)),
                ('LD2_2_exp', models.TextField(max_length=1000, blank=True, null=True)),
                ('NW1_2_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('NW1_2_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (4, 'Enhanced'), (9, 'Superior'), (14, 'Conserving'), (18, 'Restorative')], default=0)),
                ('NW1_2_exp', models.TextField(max_length=1000, blank=True, null=True)),
                ('NW2_2_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('NW2_2_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (2, 'Enhanced'), (5, 'Superior'), (9, 'Conserving')], default=0)),
                ('NW2_2_exp', models.TextField(max_length=1000, blank=True, null=True)),
                ('NW2_3_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('NW2_3_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (4, 'Enhanced'), (9, 'Superior'), (14, 'Conserving'), (18, 'Restorative')], default=0)),
                ('NW2_3_exp', models.TextField(max_length=1000, blank=True, null=True)),
                ('engineer', models.ForeignKey(to='engineer.Engineer')),
            ],
        ),
    ]
