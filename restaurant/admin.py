from django.contrib import admin
from .models import Restaurant
from import_export.admin import ImportExportModelAdmin

@admin.register(Restaurant)
class RestaurantAdmin(ImportExportModelAdmin):
    list_display = ['name', 'description','address','rating']


