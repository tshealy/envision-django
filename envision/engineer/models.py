from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg, Count
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.urlresolvers import reverse
import datetime
from django.utils import timezone


class Engineer(models.Model):

    name = models.CharField(max_length=255)

    version = models.IntegerField()

    total_time = models.IntegerField(default=0)

#
# class Project(models.Model):
#
#     title = models.CharField(max_length=255, default='Cordova, AL')
#
#     engineer = models.ForeignKey(Engineer)


class Rating(models.Model):

    engineer = models.ForeignKey(Engineer)

    include = (
        (0, "Include"),
        (1, "Exclude")
    )

    loa_1_1 = (
        (0, "No Added Value"),
        (2, "Improved"),
        (5, "Enhanced"),
        (10, "Superior"),
        (20, "Conserving"),
        (25, "Restorative"),
    )

    QL1_1_inc = models.IntegerField(choices=include, default=0)
    QL1_1_loa = models.IntegerField(choices=loa_1_1, default=0)
    QL1_1_exp = models.TextField(max_length=1000, null=True, blank=True)

    loa_1_2 = (
            (0, "No Added Value"),
            (1, "Improved"),
            (2, "Enhanced"),
            (5, "Superior"),
            (13, "Conserving"),
            (16, "Restorative"),
        )
    QL1_2_inc = models.IntegerField(choices=include, default=0)
    QL1_2_loa = models.IntegerField(choices=loa_1_2, default=0)
    QL1_2_exp = models.CharField(max_length=500, null=True, blank=True)

    loa_1_3 = (
            (0, "No Added Value"),
            (1, "Improved"),
            (2, "Enhanced"),
            (5, "Superior"),
            (12, "Conserving"),
            (15, "Restorative"),
        )

    QL1_3_inc = models.IntegerField(choices=include, default=0)
    QL1_3_loa = models.IntegerField(choices=loa_1_3, default=0)
    QL1_3_exp = models.CharField(max_length=500, null=True, blank=True)

    loa_2_1 = (
            (0, "No Added Value"),
            (2, "Improved"),
            (16, "Conserving"),
        )

    QL2_1_inc = models.IntegerField(choices=include, default=0)
    QL2_1_loa = models.IntegerField(choices=loa_2_1, default=0)
    QL2_1_exp = models.CharField(max_length=500, null=True, blank=True)

    loa_2_2 = (
            (0, "No Added Value"),
            (1, "Improved"),
            (8, "Conserving"),
            (11, "Restorative"),
        )

    QL2_2_inc = models.IntegerField(choices=include, default=0)
    QL2_2_loa = models.IntegerField(choices=loa_2_2, default=0)
    QL2_2_exp = models.CharField(max_length=500, null=True, blank=True)

    loa_2_3 = (
                (0, "No Added Value"),
                (1, "Improved"),
                (2, "Enhanced"),
                (4, "Superior"),
                (8, "Conserving"),
                (11, "Restorative"),
    )
    QL2_3_inc = models.IntegerField(choices=include, default=0)
    QL2_3_loa = models.IntegerField(choices=loa_2_3, default=0)
    QL2_3_exp = models.CharField(max_length=500, null=True, blank=True)

    loa_2_4 = (
                (0, "No Added Value"),
                (1, "Improved"),
                (4, "Enhanced"),
                (7, "Superior"),
                (14, "Conserving"),
    )

    QL2_4_inc = models.IntegerField(choices=include, default=0)
    QL2_4_loa = models.IntegerField(choices=loa_2_4, default=0)
    QL2_4_exp = models.CharField(max_length=500, null=True, blank=True)

    loa_2_5 = (
                (0, "No Added Value"),
                (1, "Improved"),
                (3, "Enhanced"),
                (6, "Superior"),
                (12, "Conserving"),
                (15, "Restorative"),
    )

    QL2_5_inc = models.IntegerField(choices=include, default=0)
    QL2_5_loa = models.IntegerField(choices=loa_2_5, default=0)
    QL2_5_exp = models.CharField(max_length=500, null=True, blank=True)

    loa_2_6 = (
                (0, "No Added Value"),
                (3, "Enhanced"),
                (6, "Superior"),
                (12, "Conserving"),
                (15, "Restorative"),
    )
    QL2_6_inc = models.IntegerField(choices=include, default=0)
    QL2_6_loa = models.IntegerField(choices=loa_2_6, default=0)
    QL2_6_exp = models.CharField(max_length=500, null=True, blank=True)


    loa_3_1 = (
                (0, "No Added Value"),
                (1, "Improved"),
                (7, "Superior"),
                (13, "Conserving"),
                (16, "Restorative"),
    )

    QL3_1_inc = models.IntegerField(choices=include, default=0)
    QL3_1_loa = models.IntegerField(choices=loa_3_1, default=0)
    QL3_1_exp = models.CharField(max_length=500, null=True, blank=True)

    loa_3_2 = (
                (0, "No Added Value"),
                (1, "Improved"),
                (3, "Enhanced"),
                (6, "Superior"),
                (11, "Conserving"),
                (14, "Restorative"),
    )

    QL3_2_inc = models.IntegerField(choices=include, default=0)
    QL3_2_loa = models.IntegerField(choices=loa_3_2, default=0)
    QL3_2_exp = models.CharField(max_length=500, null=True, blank=True)

    loa_3_3 = (
                (0, "No Added Value"),
                (1, "Improved"),
                (3, "Enhanced"),
                (6, "Superior"),
                (11, "Conserving"),
                (13, "Restorative"),
    )

    QL3_3_inc = models.IntegerField(choices=include, default=0)
    QL3_3_loa = models.IntegerField(choices=loa_3_3, default=0)
    QL3_3_exp = models.CharField(max_length=500, null=True, blank=True)
