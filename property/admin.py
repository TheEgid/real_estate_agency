from django.contrib import admin
from .models import Flat


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'town_district', 'address',)
    readonly_fields = ['created_at',]
