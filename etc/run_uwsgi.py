activate_this = "/var/virtualenvs/adams/bin/activate_this.py"
execfile(activate_this, dict(__file__=activate_this))

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

