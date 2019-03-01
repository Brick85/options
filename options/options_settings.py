from django.conf import settings

CREATE_ITEMS = getattr(settings, 'OPTIONS_CREATE_ITEMS', False)
