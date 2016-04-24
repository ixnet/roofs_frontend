from django.contrib import admin
from .models import Roof


@admin.register(Roof)
class RoofAdmin(admin.ModelAdmin):
    # Display:
    list_display = ['__str__', 'slug', 'metro', 'address', 'created']
    search_fields = ['title', 'metro', 'street', 'description']
    list_filter = ['created', 'complexity', 'slope']

    # Create:
    radio_fields = {'complexity': admin.HORIZONTAL, 'slope': admin.HORIZONTAL}
    fieldsets = (
        ('Общая информация', {'fields': ['title', 'complexity', 'slope', 'image']}),
        ('Адрес', {'fields': ['metro', 'street', 'number', 'building', 'porch', 'floor']}),
        ('Описание', {'fields': ['description', 'route']}))
