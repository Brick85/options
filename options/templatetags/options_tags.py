from django import template
from options import get_option as get_option_source, get_label as get_label_source, get_text as get_text_source

register = template.Library()


@register.simple_tag(takes_context=True)
def get_option(context, key, as_var=None):
    return _get_qoption_value(get_option_source, context, key, as_var)


@register.simple_tag(takes_context=True)
def get_label(context, key, as_var=None):
    return _get_qoption_value(get_label_source, context, key, as_var)


@register.simple_tag(takes_context=True)
def get_text(context, key, as_var=None):
    return _get_qoption_value(get_text_source, context, key, as_var)


def _get_qoption_value(function, context, key, as_var):
    try:
        ret = function(key)
    except:
        ret = ""

    if as_var:
        context[as_var] = ret
        return ''
    else:
        return ret
