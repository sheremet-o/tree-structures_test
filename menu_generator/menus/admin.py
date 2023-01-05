from django.contrib import admin

from .models import Menu, MenuItem


class MenuAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'created_at',
        'position'
    )


class MenuItemAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'menu',
    )


admin.site.register(Menu, MenuAdmin)
admin.site.register(MenuItem, MenuItemAdmin)
