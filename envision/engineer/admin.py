from django.contrib import admin
from .models import Engineer, Project, Rating


class EngineerAdmin(admin.ModelAdmin):
    list_display = ['name', 'version']


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title']


class RatingAdmin(admin.ModelAdmin):
    list_display = ['QL1_1_loa', 'QL1_2_loa', 'QL1_3_loa', 'QL2_1_loa', 'QL2_2_loa', 'QL2_3_loa',
                    'QL2_4_loa', 'QL2_5_loa', 'QL2_6_loa', 'QL3_1_loa', 'QL3_2_loa', 'QL3_3_loa']


admin.site.register(Engineer, EngineerAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Rating, RatingAdmin)