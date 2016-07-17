from options.models import OptionCache, Option, Label, Text
from options import options_settings
from django.utils.safestring import mark_safe

from django.utils.html import format_html
from django.core.urlresolvers import reverse


def get_option(key, fail_silently=True, editable=False):
    return _get_qoption_value(Option, key, fail_silently, editable=editable)


def get_label(key, fail_silently=True, editable=False):
    return _get_qoption_value(Label, key, fail_silently, editable=editable)


def get_text(key, fail_silently=True, editable=False):
    return _get_qoption_value(Text, key, fail_silently, return_tuple=True, editable=editable)


def _format_returned_value(opt, return_tuple, editable):
    if return_tuple:
        if editable:
            value = [_get_text_with_link(opt, opt.title), _get_text_with_link(opt, opt.text)]
        else:
            value = [mark_safe(opt.title), mark_safe(opt.text)]
    else:
        if editable:
            value = _get_text_with_link(opt, opt.value)
        else:
            value = mark_safe(opt.value)
    return value


def _get_text_with_link(obj, value):
    url = reverse('admin:options_{}_change'.format(type(obj).__name__.lower()), args=[obj.pk])
    return format_html("{value} <a href='{url}' style='font-size: 14px'>Edit</a>", value=mark_safe(value), url=url)


def _get_qoption_value(model, key, fail_silently, return_tuple=False, editable=False):
    if return_tuple:
        default = ('', '')
    else:
        default = ''
    cache_key = model.cache_mask.format(key)
    value = OptionCache.get(cache_key)
    if not value:
        try:
            opt = model.objects.get(key=key)
            value = _format_returned_value(opt, return_tuple, editable)
        except model.DoesNotExist:
            if options_settings.CREATE_ITEMS:
                opt = model()
                opt.key = key
                opt.save()
                value = default
            if fail_silently:
                value = default
            if editable:
                value = _get_text_with_link(opt, value)
            else:
                raise model.DoesNotExist('No record with key "{0}"'.format(key))
        except model.MultipleObjectsReturned:
            if fail_silently:
                opt = model.objects.filter(key=key)[0]
                value = _format_returned_value(opt, return_tuple, editable)
            else:
                raise model.DoesNotExist('Returned more than one record with key "{0}"'.format(key))

        OptionCache.set(cache_key, value)
    return value
