from django.contrib import admin
from options import Option


class OptionAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')

admin.site.register(Option, OptionAdmin)
