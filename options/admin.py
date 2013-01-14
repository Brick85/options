from django.contrib import admin
from .models import Option, Label, Text
from django.conf import settings


if 'modeltranslation' in settings.INSTALLED_APPS:
    from modeltranslation.admin import TranslationAdmin
    QOptionModelAdminTranslated = TranslationAdmin
else:
    QOptionModelAdminTranslated = admin.ModelAdmin

if 'tinymce' in settings.INSTALLED_APPS:
    from django.db import models
    from tinymce.widgets import AdminTinyMCE
    qoptions_formfield_overrides = {
        models.TextField: {'widget': AdminTinyMCE},
    }
else:
    qoptions_formfield_overrides = {}


class QOptionOptionAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')


class QOptionLabelAdmin(QOptionModelAdminTranslated):
    list_display = ('key', 'value')


class QOptionTextAdmin(QOptionModelAdminTranslated):
    list_display = ('key', 'value')
    formfield_overrides = qoptions_formfield_overrides


admin.site.register(Option, QOptionOptionAdmin)
admin.site.register(Label,  QOptionLabelAdmin)
admin.site.register(Text,   QOptionTextAdmin)
