from models import OptionCache, Option, Label, Text


def get_option(key, fail_silently=True):
    return _get_qoption_value(Option, key, fail_silently)


def get_label(key, fail_silently=True):
    return _get_qoption_value(Label, key, fail_silently)


def get_text(key, fail_silently=True):
    return _get_qoption_value(Text, key, fail_silently)


def _get_qoption_value(model, key, fail_silently):
    cache_key = model.cache_mask.format(key)
    value = OptionCache.get(cache_key)
    if not value:
        try:
            opt = model.objects.get(key=key)
            if hasattr(opt, 'title'):
                value = [opt.title, opt.text]
            else:
                value = opt.value
        except model.DoesNotExist:
            if fail_silently:
                value = ''
            else:
                raise model.DoesNotExist('No record with key "{0}"'.format(key))
        except model.MultipleObjectsReturned:
            if fail_silently:
                opt = model.objects.filter(key=key)[0]
                if hasattr(opt, 'title'):
                    value = [opt.title, opt.text]
                else:
                    value = opt.value
            else:
                raise model.DoesNotExist('Returned more than one record with key "{0}"'.format(key))

        OptionCache.set(cache_key, value)
    return value
