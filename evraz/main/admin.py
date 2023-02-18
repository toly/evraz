from django.contrib import admin

from .models import DataItem


class DataItemAdmin(admin.ModelAdmin):
    list_display = ('offset', 'moment', 'key', 'value')


admin.site.register(DataItem, DataItemAdmin)
