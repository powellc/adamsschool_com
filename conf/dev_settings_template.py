DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)
MANAGERS = ADMINS

if DEBUG:
    INTERNAL_IPS = ('127.0.0.1',)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'development.db',                      # Or path to database file if using sqlite3.
        'TEST_NAME': 'test_sqlite.db'
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
        #'LOCATION': '127.0.0.1:11211', # for memcache
    }
}

EMAIL_PORT = 8025 # default port for fakemail.py