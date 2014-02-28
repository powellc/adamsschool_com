from django.conf.urls.defaults import patterns, url
from django.views.generic.dates import YearArchiveView, MonthArchiveView, DayArchiveView

from newsletters.views import NewsletterView
from newsletters.models import Edition

urlpatterns = patterns('',
    url(r'^(?P<id>\d+)/',
        YearArchiveView.as_view(model=Edition,
                                                   queryset=Edition.published_objects.all(),
                                                   template_name='newsletters/newsletter-list.html',
                                                   date_field='publish_on')),
                       url(r'^',
                           NewsletterView.as_view(), name="newsletter-latest")
)
