"""
WSGI config for v_street project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/dev/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application
sys.path.append("/var/www/v_street/")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'v_street.settings')

application = get_wsgi_application()
