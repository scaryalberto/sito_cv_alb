import sys

path='/var/www/sito_cv_alb'

if path not in sys.path:
    sys.path.append(path)



        

          
import os
import sys

sys.path.append('/var/www/sito_cv_alb')
os.environ.setdefault("PYTHON_EGG_CACHE", "/var/www/sito_cv_alb/sito_cv/egg_cache")

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sito_cv.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

