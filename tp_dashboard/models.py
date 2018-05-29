from django.conf import settings

if settings.APP_NAME == 'tp_dashboard':
    from .tests import models
