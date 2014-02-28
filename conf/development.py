from common import *

DEBUG=True
TESTING=False
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'NAME':'adams',
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'USER':'adams',
        'PASSWORD':'mainr0ot',
    },
}

MEDIA_URL='/media/'
MEDIA_ROOT= os.path.join(PROJECT_ROOT, 'media/')

ADMIN_MEDIA_PREFIX = MEDIA_URL + "/admin/"

TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, 'templates'),)

ACCOUNT_ACTIVATION_DAYS = 7
GOOGLE_API_KEY='ABQIAAAArieRT_xwgFjdUCrGKqcFtRSmxf42tW8xsTS9f3H9MYQHFe_8JhQGxBlq98P01t9wnQS3A4BO52QwDA'

INTERNAL_IPS = ('24.93.128.34','10.1.1.23','127.0.0.1' )
VIRTUALENV="/Users/admin/.virtualenvs/adams/lib/python2.5/site-packages"

#Start up logging to the console

logging.getLogger('').addHandler(CONSOLE_HANDLER)
logging.debug("Django Started")

RECAPTCHA_PUBLIC_KEY = ''
RECAPTCHA_PRIVATE_KEY = ''

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

##### For Email ########
ACCOUNT_ACTIVATION_DAYS=15
EMAIL_HOST="smtp.gmail.com"
EMAIL_HOST_USER="colin.powell@adamsschool.com"
EMAIL_HOST_PASSWORD="hall6-jerkin"
DEFAULT_FROM_EMAIL="info@adamsschool.com"
EMAIL_USE_TLS = True

CACHE_DIR = os.path.join(SITE_ROOT, 'var',  'cache/')
CACHE_BACKEND = 'file:///' + CACHE_DIR
CACHE_TIMEOUT = 60*5

