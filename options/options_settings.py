from django.conf import settings

CREATE_ITEMS = getattr(settings, 'OPTIONS_CREATE_ITEMS', False)
DISPLAY_EDIT_LINK = getattr(settings, 'OPTIONS_DISPLAY_EDIT_LINK', False)
