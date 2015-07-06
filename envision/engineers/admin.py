from django.contrib import admin
from .models import Engineer, Rating


class EngineerAdmin(admin.ModelAdmin):
    list_display = ['user', 'version', 'rating']


admin.site.register(Engineer, EngineerAdmin)