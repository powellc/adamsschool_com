# Django settings for adamsschool_com project.
import os
import sys
from easy_thumbnails.conf import Settings as easy_thumbnails_defaults

## Directories
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))
PUBLIC_ROOT = os.path.join(PROJECT_PATH, "public")
sys.path.insert(0, os.path.join(PROJECT_PATH, "apps"))

CREATE_ADMIN = False

MEDIA_ROOT = os.path.join(PUBLIC_ROOT, "media")
STATIC_ROOT = os.path.join(PUBLIC_ROOT, 'static')

STATIC_URL = '/static/'
MEDIA_URL = "/media/"
ADMIN_TOOLS_MEDIA_URL = "/static/"
ADMIN_MEDIA_PREFIX = "/static/admin/"
ADMIN_NAME="Adams School Admin"

LOGIN_REDIRECT_URL = "/"

USE_TZ=False

DEBUG = True
TEMPLATE_DEBUG= DEBUG

# Django settings for adamsschool_com project.
ADMINS = (
    ('Colin Powell', 'colin.powell@adamsschool.com'),
)

LANGUAGES = [
    ('en', 'English'),
]
LANGUAGE_CODE = 'en-us'
MANAGERS = ADMINS
USE_I18N = False
USE_L10N = False

MAILCHIMP_API_KEY='b2df48d27ce38006a9eb4decdf5000e0-us6'
MAILCHIMP_WEBHOOK_KEY = 'k89al230oijlasdf89uj023ljlas'
MAILCHIMP_NEWSLETTER_LIST_ID='e18409d2c3'
MAILCHIMP_PARENTS_LIST_ID='629edc7d26'

MULTIBLOGS_WITHOUT_SETS=False

SEND_BROKEN_LINK_EMAILS=True
#IGNORABLE_404_STARTS=('',)

TIME_ZONE = 'America/New_York'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1

import logging

LOG_DATE_FORMAT = '%d %b %Y %H:%M:%S'
LOG_FORMATTER = logging.Formatter('%(asctime)s %(name)-7s: %(levelname)-8s %(message)s',
    datefmt=LOG_DATE_FORMAT)

#FILE_HANDLER = logging.FileHandler(os.path.join(PROJECT_PATH)+'/django.log', 'w')
CONSOLE_HANDLER = logging.StreamHandler() # defaults to stderr
CONSOLE_HANDLER.setFormatter(LOG_FORMATTER)
CONSOLE_HANDLER.setLevel(logging.DEBUG)


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Additional locations of static files
from imp import find_module
STATICFILES_DIRS = (
    os.path.join(os.path.abspath(find_module("debug_toolbar")[1]), 'media'),
    os.path.join(os.path.abspath(find_module("admin_tools")[1]), 'media'),
    os.path.join(os.path.abspath(find_module("zinnia")[1]), 'static'),
    os.path.join(os.path.join(PROJECT_PATH, "static"))
)

DEBUG_TOOLBAR_MEDIA_ROOT = os.path.join(STATIC_ROOT, 'debug_toolbar')

SECRET_KEY = 'v0%26bx!p-uvrra5vkuvk%cz+8h=b&!7u7i%z4vj)hu3@cow%s'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'raven.contrib.django.raven_compat.middleware.Sentry404CatchMiddleware',
    'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'notifications.context_processors.notification_processor',
    'cms.context_processors.media',
    'sekizai.context_processors.sekizai',
    'allauth.account.context_processors.account',
    'allauth.socialaccount.context_processors.socialaccount',
)

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH, "templates")
)


CMS_TEMPLATES = (
    ('homepage.html', 'Homepage'),
    ('interior_page.html', 'Interior Page'),
    ('one_column.html', 'One Column Page'),
    ('two_columns.html', 'Two Column Page'),
    ('contact_us.html', 'Contact Us Page')
)

CMS_CACHE_PREFIX = 'aes-staging'
CMS_MEDIA_ROOT=os.path.join(STATIC_ROOT, "cms/")
CMS_MEDIA_URL = "/static/cms/"
CMS_SEO_FIELDS = True
CMS_USE_TINYMCE = True
CMS_PERMISSION = True
CMS_REDIRECTS = True
CMS_SOFTROOT = True


TINYMCE_DEFAULT_CONFIG = {
    'theme': "advanced",
    'plugins': "table,paste,searchreplace,fullscreen",
    'theme_advanced_buttons1': 'bold,italic,underline,strikethrough,|,justifyleft,justifycenter,justifyright,justifyfull,|,styleselect,formatselect,fontselect,fontsizeselect',
    'theme_advanced_buttons2': 'cut,copy,paste,pastetext,|,search,replace,|,bullist,numlist,|,outdent,indent,blockquote,|,undo,redo,|,link,unlink,anchor,image,cleanup,help,code,|,insertdate,inserttime,preview,|,forecolor,backcolor',
    'theme_advanced_buttons3': 'tablecontrols,|,hr,removeformat,visualaid,|,sub,sup,|,charmap,emotions,iespell,media,advhr,|,fullscreen',
    'theme_advanced_toolbar_location': "top",
    'theme_advanced_toolbar_align': 'left',
    'theme_advanced_resizing': 'true',
    'theme_advanced_statusbar_location': 'bottom',
    'theme_advanced_resize_horizontal': 'true',
    'height': '380',
    'width': '50%'
}


#AUTH_PROFILE_MODULE = 'profiles.UserProfile'

SKIP_SOUTH_TESTS = True
SOUTH_TESTS_MIGRATE = False

AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'bootstrapform',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.admin',
    'django.contrib.markup',
    'django.contrib.humanize',
    'django.contrib.admindocs',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
    'django.contrib.comments',
    'django.contrib.staticfiles',
    'django.contrib.redirects',
    'django_jenkins',

    'cms',
    'cms.plugins.flash',
    'cms.plugins.link',
    'cms.plugins.snippet',
    'cms.plugins.text',
    'cmsplugin_photologue_pro', 
    'cms.plugins.googlemap',

    'notifications',
    'forms_builder.forms',
    'debug_toolbar',
    'typogrify',
    'south',
    'mailchimp',
    'django_extensions',
    'crispy_forms',
    'tagging',

    'filer',
    'cmsplugin_zinnia',
    'cmsplugin_filer_file',
    'cmsplugin_filer_folder',
    'cmsplugin_filer_image',
    'cmsplugin_filer_teaser',
    'cmsplugin_filer_video',
    'cmsplugin_nivoslider',
    'wunderground',

    'robots',
    'mptt',
    'menus',
    'tinymce',
    'typogrify',
    'sekizai',
    'easy_thumbnails',
    'zinnia',
    'slideshows',
    'lunches',
    'newsletters',
    'photologue',
    'classifieds',

    'dashboard',
    'staff',
    'raven.contrib.django.raven_compat',
    #'apps.profiles',

 )

RAVEN_CONFIG = {
    'dsn': 'http://c989e3856cb44863b2f43468215f09f8:70aec9dee9624c679b2827dd2b6bc5f7@sentry.onec.me/3',
}
ADMIN_TOOLS_INDEX_DASHBOARD = 'dashboard.CustomIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'dashboard.CustomAppIndexDashboard'

#ZINNIA_ENTRY_BASE_MODEL = 'cmsplugin_zinnia.placeholder.EntryPlaceholder'

THUMBNAIL_ALIASES = {
        '': {
             'slideshow': {'size': (1300, 800), 'crop': False},
             'newsletter_header': {'size': (573, 238), 'crop': True},
             'preview': {'size': (400, 400), 'crop': True},
            },
}

WUNDERGROUND_KEY = '71cb0db6cbef5334'

THUMBNAIL_PROCESSORS = easy_thumbnails_defaults.THUMBNAIL_PROCESSORS + (
    'filer.thumbnail_processors.scale_and_crop_with_subject_location',
    'cmsplugin_nivoslider.thumbnail_processors.pad_image',
    )

SOUTH_MIGRATION_MODULES = {
    'cms.plugins.googlemap': 'ignore',
    'cms.plugins.flash': 'ignore',
    'cms.plugins.text': 'ignore',
    'cms.plugins.snippet': 'ignore',
    'cmsplugin_photologue_pro': 'ignore',
    'mptt': 'ignore',
    'tinymce': 'ignore',
}

JENKINS_TASKS = (
    'django_jenkins.tasks.run_pylint',
    'django_jenkins.tasks.with_coverage',
    'django_jenkins.tasks.django_tests',
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_csslint',
    'django_jenkins.tasks.run_sloccount',
)

try:
    from local_settings import *
except:
    pass
