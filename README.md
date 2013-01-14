# Django-Options

Options, Labels and standalone Texts for django admin. Administrator emails, phones, contact data, etc.

qOptions package allows you to create records in database, wich you can use in your templates and views.

**Works with [django-modeltranslation](https://github.com/deschler/django-modeltranslation) and [django-tinymce](https://github.com/aljosa/django-tinymce)**

### To use modeltranslation:

Add 'modeltranslation' to INSTALLED\_APPS and 'options.translation' to MODELTRANSLATION\_TRANSLATION_FILES

### To use django-tinymce:

Add 'tinymce' to INSTALLED_APPS

## Usage

In python code you can use:

```python
from options import get_option, get_label, get_text
print get_option('your_option_key')
print get_label('your_label_key')
print get_text('your_text_key')
```

In templates:

```python
{% load options_tags %}
{% get_option 'your_option_key' %}
{% get_label 'your_label_key' %}
{% get_text 'your_text_key' %}
```
