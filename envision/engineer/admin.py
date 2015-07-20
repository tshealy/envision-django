from django.contrib import admin
from .models import Engineer, Rating


class EngineerAdmin(admin.ModelAdmin):
    list_display = ['name', 'version']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['engineer', 'QL1_1_inc', 'QL1_1_loa', 'QL1_1_exp',
              'QL1_2_inc', 'QL1_2_loa', 'QL1_2_exp',
              'QL2_3_inc', 'QL2_3_loa', 'QL2_3_exp',
              'QL2_5_inc', 'QL2_5_loa', 'QL2_5_exp',
              'QL2_6_inc', 'QL2_6_loa', 'QL2_6_exp',
              'QL3_3_inc', 'QL3_3_loa', 'QL3_3_exp',
              'LD1_2_inc', 'LD1_2_loa', 'LD1_2_exp',
              'LD1_4_inc', 'LD1_4_loa', 'LD1_4_exp',
              'LD2_2_inc', 'LD2_2_loa', 'LD2_2_exp',
              'NW1_2_inc', 'NW1_2_loa', 'NW1_2_exp',
              'NW2_2_inc', 'NW2_2_loa', 'NW2_2_exp',
              'NW2_3_inc', 'NW2_3_loa', 'NW2_3_exp',]


admin.site.register(Engineer, EngineerAdmin)
admin.site.register(Rating, RatingAdmin)