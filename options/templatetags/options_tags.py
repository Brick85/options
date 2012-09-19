from django import template
from options.models import Option

register = template.Library()

@register.simple_tag(takes_context=True)
def getOption(context, key, as_var=None):
    try:
        ret = Option.getValue(key)
    except:
        ret = ""

    if as_var:
        context[as_var] = ret
        return ''
    else:
        return ret
