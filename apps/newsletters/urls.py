from django.conf.urls.defaults import patterns, url
from django.views.generic.dates import YearArchiveView, MonthArchiveView, DayArchiveView
from django.views.generic import DetailView

from apps.newsletters.feeds import LatestNewsletterFeed
from apps.newsletters.views import NewsletterView
from apps.newsletters.models import Edition

urlpatterns = patterns('',
    url(r'^feed/$', LatestNewsletterFeed(), name='newsletter-feed'),

    url(r'^subscribe/$', 'newsletters.views.subscribe', name='newsletter-subscribe'),
    url(r'^subscribe/thank-you/$', 'newsletters.views.confirmation', name='newsletter-confirmation'),

    url(r'(?P<pk>\d+)/$',
        DetailView.as_view(model=Edition,
             queryset=Edition.objects.all(),
             template_name='newsletters/newsletter.html',
                               slug_field='id'),
        name='newsletter-detail'),
    url(r'^',
        NewsletterView.as_view(), name="newsletter-latest")
)
