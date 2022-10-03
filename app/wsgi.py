import os
from django.core.wsgi import get_wsgi_application

settings_module = 'app.settings.production' if 'WEBSITE_HOSTNAME' in os.environ else 'app.settings.development'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)

application = get_wsgi_application()
