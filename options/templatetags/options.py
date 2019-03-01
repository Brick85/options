from django import template
from django.urls import reverse
from django.utils.html import format_html, mark_safe
from options.models import Label, Text

from ..functions import get_option as get_option_source, get_label as get_label_source, get_text as get_text_source

register = template.Library()


@register.simple_tag(takes_context=True)
def get_option(context, key, as_var=None):
    return _get_qoption_value(get_option_source, context, key, as_var)


@register.simple_tag(takes_context=True)
def get_label(context, key, as_var=None):
    return _get_qoption_value(get_label_source, context, key, as_var)


@register.simple_tag(takes_context=True)
def get_text(context, key, title_var='title', as_var=None):
    title, text = _get_qoption_value(get_text_source, context, key, None)
    context[title_var] = title
    if as_var:
        context[as_var] = text
        return ''
    return text


@register.simple_tag(takes_context=True)
def get_text_title(context, key, text_var='text', as_var=None):
    title, text = _get_qoption_value(get_text_source, context, key, None)
    context[text_var] = text
    if as_var:
        context[as_var] = title
        return ''
    return title


def _get_qoption_value(function, context, key, as_var):
    try:
        ret = function(key)
    except Exception:
        ret = ""

    if as_var:
        context[as_var] = ret
        return ''
    else:
        return ret


@register.simple_tag(takes_context=True)
def get_editable_label(context, key, as_var=None):
    """
    Print label with link to admin site
    """
    value = get_label(context, key, as_var)

    if context.request.user.is_superuser:
        # TODO: fix extra hit to DB
        obj = Label.objects.get(key=key)

        return format_html(
            "{} <a href='{}' target='_blank'>[Edit]</a>",
            mark_safe(value),
            reverse('admin:options_label_change', args=[obj.pk])
        )
    return value


@register.simple_tag(takes_context=True)
def get_editable_text_title(context, key, text_var='text', as_var=None):
    """
    Print title, text with link to admin site
    """
    title = get_text_title(context, key, as_var)

    if context.request.user.is_superuser:
        # TODO: fix extra hit to DB
        obj = Text.objects.get(key=key)

        return format_html(
            "{} <a href='{}' target='_blank'>[Edit]</a>",
            mark_safe(title),
            reverse('admin:options_text_change', args=[obj.pk])
        )
    return title
