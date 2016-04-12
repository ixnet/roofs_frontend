from django.contrib import admin
from .models import Roof


@admin.register(Roof)
class RoofAdmin(admin.ModelAdmin):
    # Display:
    list_display = ['__str__', 'metro', 'address', 'created']
    search_fields = ['title', 'metro', 'street', 'description']
    list_filter = ['created', 'complexity', 'slope']

    # Create:
    radio_fields = {'complexity': admin.HORIZONTAL, 'slope': admin.HORIZONTAL}
    fieldsets = (
        ('Общая информация', {'fields': ['title', 'complexity', 'slope']}),
        ('Адрес', {'fields': ['metro', 'street', 'number', 'porch', 'floor']}),
        ('Описание', {'fields': ['description', 'route']}))

# TODO: View on site -> ModelAdmin.view_on_site
