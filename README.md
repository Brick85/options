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
from options.functions import get_option, get_label, get_text
print get_option('your_option_key')  # 'value'
print get_label('your_label_key')  # 'value'
print get_text('your_text_key')  # ['title', 'text']
```

In templates:

```python
{% load options %}
{% get_option 'your_option_key' %}
{% get_label 'your_label_key' %}
```

Or if you want return to context variable:

```python
{% get_option 'your_option_key' 'my_option_key' %}
{{ my_option_key }}
{% get_label 'your_label_key' 'my_label_key' %}
{{ my_label_key }}
```

With texts it's a little more complicated. You need two texts, but you probably do not wont hit database or cache twice. So we return first variable directly and second as context variable.

```python
{% get_text 'your_text_key' 'my_title' %}
{{ my_title }}

OR (if you need title first)

{% get_text_title 'your_text_key' 'my_text' %}
{{ my_text }}
```

Ofcourse we can return both variables as context variables:

```python
{% get_text 'your_text_key' 'my_title' 'my_text' %}

OR

{% get_text_title 'your_text_key' 'my_text' 'my_title' %}

AND
{{ my_title }}: {{ my_text }}
```

### Edit links for superuser on front end

Title and text:

```html
<h1>{% get_editable_text_title 'your_text_key' as_var='my_text' %}</h1>
<div>{{ my_text }}</div>
```

Labels:

```html
<span>{% get_editable_label 'your_text_key' %}</span>
```
