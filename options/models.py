from django.db import models
from django.utils.translation import ugettext_lazy as _


class OptionCache(object):
    _cache = {}

    @staticmethod
    def get(key):
        try:
            return OptionCache._cache[key]
        except:
            return None

    @staticmethod
    def set(key, value):
        OptionCache._cache[key] = value

    @staticmethod
    def delete(key):
        del OptionCache._cache[key]


class Option(models.Model):
    """
    Options model
    """
    key = models.CharField(_('Key'), max_length=50, unique=True)
    value = models.CharField(_('Value'), max_length=256)

    cache_mask = 'qo_o_{0}'

    class Meta:
        verbose_name = _('option')
        verbose_name_plural = _('options')
        ordering = ['key']

    def __unicode__(self):
        return self.key

    def save(self, *args, **kwargs):
        super(Option, self).save(*args, **kwargs)
        try:
            OptionCache.delete(Option.cache_mask.format(self.key))
        except KeyError:
            pass


class Label(models.Model):
    key = models.CharField(_('Key'), max_length=50, unique=True)
    value = models.CharField(_('Value'), max_length=256)

    cache_mask = 'qo_l_{0}'

    class Meta:
        verbose_name = _('label')
        verbose_name_plural = _('labels')
        ordering = ['key']

    def __unicode__(self):
        return self.key

    def save(self, *args, **kwargs):
        super(Label, self).save(*args, **kwargs)
        try:
            OptionCache.delete(Label.cache_mask.format(self.key))
        except KeyError:
            pass


class Text(models.Model):
    key = models.CharField(_('Key'), max_length=50, unique=True)
    value = models.TextField(_('Value'))

    cache_mask = 'qo_t_{0}'

    class Meta:
        verbose_name = _('text')
        verbose_name_plural = _('texts')
        ordering = ['key']

    def __unicode__(self):
        return self.key

    def save(self, *args, **kwargs):
        super(Text, self).save(*args, **kwargs)
        try:
            OptionCache.delete(Text.cache_mask.format(self.key))
        except KeyError:
            pass
