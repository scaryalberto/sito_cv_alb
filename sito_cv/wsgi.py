"""
WSGI config for sito_cv project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sito_cv.settings')

application = get_wsgi_application()


import os 
import time 
import traceback 
import signal 
import sys 
 
from django.core.wsgi import get_wsgi_application 
 
sys.path.append('/home/admin/django_projects/sito_cv_alb') 
# adjust the Python version in the line below as needed 
sys.path.append('/home/admin/django_projects/sito_cv_alb/env/lib/python3.7/site-packages') 
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sito_cv.settings')
 
try: 
    application = get_wsgi_application() 
except Exception: 
    # Error loading applications 
    if 'mod_wsgi' in sys.modules: 
        traceback.print_exc() 
        os.kill(os.getpid(), signal.SIGINT) 
        time.sleep(2.5) 
