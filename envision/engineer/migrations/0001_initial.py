# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Engineer',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('version', models.CharField(max_length=20, choices=[(1, 'A'), (2, 'B')])),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, default='Cordova, AL')),
                ('engineer', models.ForeignKey(to='engineer.Engineer')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('start_time', models.DateTimeField(null=True, default=django.utils.timezone.now)),
                ('finish_time', models.DateTimeField(null=True, default=django.utils.timezone.now)),
                ('QL1_1_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL1_1_loa', models.IntegerField(choices=[(0, 'No Added Value'), (2, 'Improved'), (5, 'Enhanced'), (10, 'Superior'), (20, 'Conserving'), (25, 'Restorative')], default=0)),
                ('QL1_1_exp', models.CharField(null=True, max_length=500, blank=True)),
                ('QL1_2_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL1_2_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (2, 'Enhanced'), (5, 'Superior'), (13, 'Conserving'), (16, 'Restorative')], default=0)),
                ('QL1_2_exp', models.CharField(null=True, max_length=500, blank=True)),
                ('QL1_3_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL1_3_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (2, 'Enhanced'), (5, 'Superior'), (12, 'Conserving'), (15, 'Restorative')], default=0)),
                ('QL1_3_exp', models.CharField(null=True, max_length=500, blank=True)),
                ('QL2_1_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL2_1_loa', models.IntegerField(choices=[(0, 'No Added Value'), (2, 'Improved'), (16, 'Conserving')], default=0)),
                ('QL2_1_exp', models.CharField(null=True, max_length=500, blank=True)),
                ('QL2_2_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL2_2_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (8, 'Conserving'), (11, 'Restorative')], default=0)),
                ('QL2_2_exp', models.CharField(null=True, max_length=500, blank=True)),
                ('QL2_3_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL2_3_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (2, 'Enhanced'), (4, 'Superior'), (8, 'Conserving'), (11, 'Restorative')], default=0)),
                ('QL2_3_exp', models.CharField(null=True, max_length=500, blank=True)),
                ('QL2_4_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL2_4_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (4, 'Enhanced'), (7, 'Superior'), (14, 'Conserving')], default=0)),
                ('QL2_4_exp', models.CharField(null=True, max_length=500, blank=True)),
                ('QL2_5_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL2_5_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (3, 'Enhanced'), (6, 'Superior'), (12, 'Conserving'), (15, 'Restorative')], default=0)),
                ('QL2_5_exp', models.CharField(null=True, max_length=500, blank=True)),
                ('QL2_6_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL2_6_loa', models.IntegerField(choices=[(0, 'No Added Value'), (3, 'Enhanced'), (6, 'Superior'), (12, 'Conserving'), (15, 'Restorative')], default=0)),
                ('QL2_6_exp', models.CharField(null=True, max_length=500, blank=True)),
                ('QL3_1_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL3_1_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (7, 'Superior'), (13, 'Conserving'), (16, 'Restorative')], default=0)),
                ('QL3_1_exp', models.CharField(null=True, max_length=500, blank=True)),
                ('QL3_2_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL3_2_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (3, 'Enhanced'), (6, 'Superior'), (11, 'Conserving'), (14, 'Restorative')], default=0)),
                ('QL3_2_exp', models.CharField(null=True, max_length=500, blank=True)),
                ('QL3_3_inc', models.IntegerField(choices=[(0, 'Include'), (1, 'Exclude')], default=0)),
                ('QL3_3_loa', models.IntegerField(choices=[(0, 'No Added Value'), (1, 'Improved'), (3, 'Enhanced'), (6, 'Superior'), (11, 'Conserving'), (13, 'Restorative')], default=0)),
                ('QL3_3_exp', models.CharField(null=True, max_length=500, blank=True)),
                ('project', models.ForeignKey(to='engineer.Project')),
            ],
        ),
    ]
