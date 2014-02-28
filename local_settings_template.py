import logging
import os

PROJECT_ROOT = os.path.dirname(os.path.realpath(os.path.dirname(__file__)))
DEBUG=True
#Start up logging to the console

FILE_HANDLER = logging.FileHandler(os.path.join(PROJECT_ROOT)+'django.log', 'w')
logging.getLogger('').addHandler(FILE_HANDLER)
logging.info("Django Started")

CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
CACHE_MIDDLEWARE_SECONDS = 10

# Override this in local_settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'HOST': '127.0.0.1',
        'NAME': 'dev.db',  # Or path to database file if using sqlite3.
        'USER': '',
        'PASSWORD': '',
    }
}

##### For Email ########
#ACCOUNT_ACTIVATION_DAYS=15
#EMAIL_HOST=""
#EMAIL_HOST_USER=""
#EMAIL_HOST_PASSWORD=""
#DEFAULT_FROM_EMAIL=""
#EMAIL_USE_TLS = True
