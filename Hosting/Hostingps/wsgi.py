import os
from django.core.wsgi import get_wsgi_application

# Ensure the settings module is set correctly
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Hostingps.settings')

application = get_wsgi_application()
