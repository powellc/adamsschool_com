from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from cms.sitemaps import CMSSitemap

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^accounts/', include('allauth.urls')),
    url(r'^admintools/', include('admin_tools.urls')),
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sitemap.xml$',
        'django.contrib.sitemaps.views.sitemap',
        {'sitemaps': {'cmspages': CMSSitemap}}),
    (r'^photos/', include('photologue.urls')),
    (r'^tinymce/', include('tinymce.urls')),
    (r'^sentry/', include('sentry.web.urls')),
    (r'^forms/', include('forms_builder.forms.urls')),
    (r'^newsletter/', include('newsletters.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
    (r'^news/', include('zinnia.urls')),
    (r'^dashboard/', include('dashboard.urls')),
    (r'^robots.txt$', include('robots.urls')),
    url(r'^', include('cms.urls')),
) + staticfiles_urlpatterns()

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
        url(r'', include('django.contrib.staticfiles.urls')),
    )

from django.db.models import signals
from django.contrib.auth.management import create_superuser
from django.contrib.auth import models as auth_app

# Prevent interactive question about wanting a superuser created.  (This
# # code has to go in this otherwise empty "models" module so that it gets
# # processed by the "syncdb" command during database creation.)
#
if not settings.CREATE_ADMIN:
    signals.post_syncdb.disconnect(
         create_superuser,
         sender=auth_app,
         dispatch_uid = "django.contrib.auth.management.create_superuser")
