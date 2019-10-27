from django.contrib import admin
from .models import Flat, Claim


@admin.register(Flat)
class FlatAdmin(admin.ModelAdmin):
    search_fields = ('town',
                     'town_district',
                     'address',
                     )

    readonly_fields = [
        'created_at',
    ]

    list_display = ('address',
                    'price',
                    'new_building',
                    'construction_year',
                    'town',
                    )

    list_editable = ('new_building',)

    list_filter = ('active',
                   'new_building',
                   'has_balcony',
                   'rooms_number',
                   )

    raw_id_fields = ('liked_by',)


@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    raw_id_fields = ('flat',
                     'user',)

