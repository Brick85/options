from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import get_language
from django.core.cache import cache


class OptionCache(object):
    langs_cache_key = 'qoptlangs'

    @staticmethod
    def _getkey(key, lang=None):
        if lang is None:
            lang = get_language()
        return "qopt_%s_%s" % (key, lang)

    @staticmethod
    def get(key):
        return cache.get(OptionCache._getkey(key), None)

    @staticmethod
    def set(key, value):
        lang = get_language()
        langs = cache.get(OptionCache.langs_cache_key, set())
        langs.add(lang)
        cache.set(OptionCache.langs_cache_key, langs)

        cache.set(OptionCache._getkey(key), value)

    @staticmethod
    def delete(key):
        cache.delete(OptionCache._getkey(key))

    @staticmethod
    def delete_all_langs(key):
        for lang in cache.get(OptionCache.langs_cache_key, set()):
            cache.delete(OptionCache._getkey(key, lang))


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

    def __str__(self):
        return self.key

    def save(self, *args, **kwargs):
        super(Option, self).save(*args, **kwargs)
        try:
            OptionCache.delete_all_langs(Option.cache_mask.format(self.key))
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

    def __str__(self):
        return self.key

    def save(self, *args, **kwargs):
        super(Label, self).save(*args, **kwargs)
        try:
            OptionCache.delete_all_langs(Label.cache_mask.format(self.key))
        except KeyError:
            pass


class Text(models.Model):
    key = models.CharField(_('Key'), max_length=50, unique=True)
    title = models.CharField(_('Title'), max_length=256, blank=True)
    text = models.TextField(_('Text'))

    cache_mask = 'qo_t_{0}'

    class Meta:
        verbose_name = _('text')
        verbose_name_plural = _('texts')
        ordering = ['key']

    def __str__(self):
        return self.key

    def save(self, *args, **kwargs):
        super(Text, self).save(*args, **kwargs)
        try:
            OptionCache.delete_all_langs(Text.cache_mask.format(self.key))
        except KeyError:
            pass
