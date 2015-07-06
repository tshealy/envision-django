from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg, Count
from django.core.exceptions import ValidationError
from django.utils import timezone
from django.core.urlresolvers import reverse
import datetime


class Engineer(models.Model):
    user = models.OneToOneField(User)

    version = (
        (1, "A"),
        (2, "B"),
    )

    version = models.CharField(choices=version)

    score = models.OneToOneField(Rating)

class Rating(models.Model):

    applicable = (
        (0, "Not Applicable"),
        (1, "Applicable")
    )

    loa_1_1 = (
        (2, "Improved"),
        (5, "Enhanced"),
        (10, "Superior"),
        (20, "Conserving"),
        (25, "Restorative"),
    )

    QL1_1_app = models.IntegerField(choices=applicable)
    QL1_1_loa = models.IntegerField(choices=loa_1_1)
    QL1_1_exp = models.CharField(max_length=500, null=True, blank=True)

    loa_1_2 = (
            (1, "Improved"),
            (2, "Enhanced"),
            (5, "Superior"),
            (13, "Conserving"),
            (16, "Restorative"),
        )
    QL1_2_app = models.IntegerField(choices=applicable)
    QL1_2_loa = models.IntegerField(choices=loa_1_2)
    QL1_2_exp = models.CharField(max_length=500, null=True, blank=True)

    loa_1_3 = (
            (1, "Improved"),
            (2, "Enhanced"),
            (5, "Superior"),
            (12, "Conserving"),
            (15, "Restorative"),
        )

    QL1_3_app = models.IntegerField(choices=applicable)
    QL1_3_loa = models.IntegerField(choices=loa_1_3)
    QL1_3_exp = models.CharField(max_length=500, null=True, blank=True)

    loa_2_1 = (
            (2, "Improved"),
            (16, "Conserving"),
        )

    QL2_1_app = models.IntegerField(choices=applicable)
    QL2_1_loa = models.IntegerField(choices=loa_2_1)
    QL2_1_exp = models.CharField(max_length=500, null=True, blank=True)

    loa_2_2 = (
            (1, "Improved"),
            (8, "Conserving"),
            (11, "Restorative"),
        )

    QL2_2_app = models.IntegerField(choices=applicable)
    QL2_2_loa = models.IntegerField(choices=loa_2_2)
    QL2_2_exp = models.CharField(max_length=500, null=True, blank=True)

    loa_2_3 = (
                (1, "Improved"),
                (2, "Enhanced"),
                (4, "Superior"),
                (8, "Conserving"),
                (11, "Restorative"),
    )
    QL2_3_app = models.IntegerField(choices=applicable)
    QL2_3_loa = models.IntegerField(choices=loa_2_3)
    QL2_3_exp = models.CharField(max_length=500, null=True, blank=True)

    loa_2_4 = (
                (1, "Improved"),
                (4, "Enhanced"),
                (7, "Superior"),
                (14, "Conserving"),
    )

    QL2_4_app = models.IntegerField(choices=applicable)
    QL2_4_loa = models.IntegerField(choices=loa_2_4)
    QL2_4_exp = models.CharField(max_length=500, null=True, blank=True)

    loa_2_5 = (
                (1, "Improved"),
                (3, "Enhanced"),
                (6, "Superior"),
                (12, "Conserving"),
                (15, "Restorative"),
    )

    QL2_5_app = models.IntegerField(choices=applicable)
    QL2_5_loa = models.IntegerField(choices=loa_2_5)
    QL2_5_exp = models.CharField(max_length=500, null=True, blank=True)

    loa_2_6 = (
                (3, "Enhanced"),
                (6, "Superior"),
                (12, "Conserving"),
                (15, "Restorative"),
    )
    QL2_6_app = models.IntegerField(choices=applicable)
    QL2_6_loa = models.IntegerField(choices=loa_2_6)
    QL2_6_exp = models.CharField(max_length=500, null=True, blank=True)


    loa_3_1 = (
                (1, "Improved"),
                (7, "Superior"),
                (13, "Conserving"),
                (16, "Restorative"),
    )

    QL3_1_app = models.IntegerField(choices=applicable)
    QL3_1_loa = models.IntegerField(choices=loa_3_1)
    QL3_1_exp = models.CharField(max_length=500, null=True, blank=True)

    loa_3_2 = (
                (1, "Improved"),
                (3, "Enhanced"),
                (6, "Superior"),
                (11, "Conserving"),
                (14, "Restorative"),
    )

    QL3_2_app = models.IntegerField(choices=applicable)
    QL3_2_loa = models.IntegerField(choices=loa_3_2)
    QL3_2_exp = models.CharField(max_length=500, null=True, blank=True)

    loa_3_3 = (
                (1, "Improved"),
                (3, "Enhanced"),
                (6, "Superior"),
                (11, "Conserving"),
                (13, "Restorative"),
    )

    QL3_3_app = models.IntegerField(choices=applicable)
    QL3_3_loa = models.IntegerField(choices=loa_3_3)
    QL3_3_exp = models.CharField(max_length=500, null=True, blank=True)

