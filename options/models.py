from django.db import models
from django.utils.translation import ugettext_lazy as _

class Option(models.Model):
    """
    Options model
    """
    key = models.CharField(_('Key'), max_length=50, db_index=True)
    value = models.CharField(_('Value'), max_length=256)

    _cache = {}

    class Meta:
        verbose_name = _('option')
        verbose_name_plural = _('options')
        ordering = ['key']

    def save(self, *args, **kwargs):
    	super(Option, self).save(*args, **kwargs)
    	try:
    		del Option._cache[self.key]
    	except KeyError:
    		pass

    def __unicode__(self):
        return self.key


    @staticmethod
    def getValues(key):
    	if not key in Option._cache.keys():
    		arr = []
	    	for opt in Option.objects.filter(key=key):
	    		arr.append(opt.value)
	    	Option._cache[key] = arr
    	return Option._cache[key]

    @staticmethod
    def getValue(key):
    	if not key in Option._cache.keys():
	    	opt = Option.objects.filter(key=key)[0]
	    	Option._cache[key] = opt.value
    	return Option._cache[key]

    @staticmethod
    def getInt(key):
    	return int(Option.getValue(key))
