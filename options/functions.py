from options import options_settings
from options.models import OptionCache, Option, Label, Text

from django.utils.html import mark_safe


def get_option(key, fail_silently=True):
    return _get_qoption_value(Option, key, fail_silently)


def get_label(key, fail_silently=True):
    return _get_qoption_value(Label, key, fail_silently)


def get_text(key, fail_silently=True):
    return _get_qoption_value(Text, key, fail_silently, return_tuple=True)


def _get_qoption_value(model, key, fail_silently, return_tuple=False):
    if return_tuple:
        default = ('', '')
    else:
        default = ''
    cache_key = model.cache_mask.format(key)
    value = OptionCache.get(cache_key)
    if not value:
        try:
            opt = model.objects.get(key=key)
            if return_tuple:
                value = [mark_safe(opt.title), mark_safe(opt.text)]
            else:
                value = mark_safe(opt.value)
        except model.DoesNotExist:
            if options_settings.CREATE_ITEMS:
                opt = model()
                opt.key = key
                opt.save()
                value = default
            if fail_silently:
                value = default
            else:
                raise model.DoesNotExist('No record with key "{0}"'.format(key))
        except model.MultipleObjectsReturned:
            if fail_silently:
                opt = model.objects.filter(key=key)[0]
                if return_tuple:
                    value = [mark_safe(opt.title), mark_safe(opt.text)]
                else:
                    value = mark_safe(opt.value)
            else:
                raise model.DoesNotExist('Returned more than one record with key "{0}"'.format(key))

        OptionCache.set(cache_key, value)
    return value