from django.contrib import admin
from .models import Option, Label, Text
from django.conf import settings


if 'modeltranslation' in settings.INSTALLED_APPS:
    from modeltranslation.admin import TranslationAdmin
    QOptionModelAdminTranslated = TranslationAdmin
else:
    QOptionModelAdminTranslated = admin.ModelAdmin

if 'ckeditor_uploader' in settings.INSTALLED_APPS:
    from django.db import models
    from ckeditor_uploader.widgets import CKEditorUploadingWidget
    qoptions_formfield_overrides = {
        models.TextField: {'widget': CKEditorUploadingWidget},
    }
elif 'ckeditor' in settings.INSTALLED_APPS:
    from django.db import models
    from ckeditor.widgets import CKEditorWidget
    qoptions_formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }
else:
    qoptions_formfield_overrides = {}


class KeyLockMixin(object):
    if not settings.DEBUG:
        readonly_fields = ['key']

        def get_actions(self, request):
            actions = super(KeyLockMixin, self).get_actions(request)
            if 'delete_selected' in actions:
                del actions['delete_selected']
            return actions

        def has_delete_permission(self, request, obj=None):
            return False

        def has_add_permission(self, request):
            return False


class QOptionOptionAdmin(KeyLockMixin, admin.ModelAdmin):
    list_display = ('key', 'value')
    fieldsets = (
        (None, {
            'fields': ('key', 'value',)
        }),
    )

class QOptionLabelAdmin(KeyLockMixin, QOptionModelAdminTranslated):
    list_display = ('key', 'value')
    fieldsets = (
        (None, {
            'fields': ('key', 'value',)
        }),
    )



class QOptionTextAdmin(KeyLockMixin, QOptionModelAdminTranslated):
    list_display = ('key', 'title')
    fieldsets = (
        (None, {
            'fields': ('key', 'title', 'text')
        }),
    )
    formfield_overrides = qoptions_formfield_overrides


admin.site.register(Option, QOptionOptionAdmin)
admin.site.register(Label,  QOptionLabelAdmin)
admin.site.register(Text,   QOptionTextAdmin)
