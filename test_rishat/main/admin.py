from django.contrib import admin

from .models import Item


class ItemAdmin(admin.ModelAdmin):
    """Настройки админки."""
    list_display = (
        'name',
        'description',
        'price'
    )

    search_fields = ('name',)
    list_filter = ('name',)


admin.site.register(Item, ItemAdmin)
