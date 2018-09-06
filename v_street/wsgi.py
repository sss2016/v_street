import os
from django.core.wsgi import get_wsgi_application
import sys
sys.path.append("/var/www/v_street/")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "v_street.settings")

application = get_wsgi_application()