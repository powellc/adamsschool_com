from django.conf.urls.defaults import patterns, url

from .feeds import LatestNewsletterFeed
from .views import (NewsletterView, EditionYearArchiveView, EditionListView,
                    EditionMonthArchiveView, EditionDetailView)

urlpatterns = patterns(
    '',
    url(r'^feed/$', LatestNewsletterFeed(), name='newsletter-feed'),

    url(r'^subscribe/$',
        'newsletters.views.subscribe',
        name='newsletter-subscribe'),

    url(r'^subscribe/thank-you/$',
        'newsletters.views.confirmation',
        name='newsletter-confirmation'),

    url(r'(?P<pk>\d+)/$',
        EditionDetailView.as_view(),
        name='newsletter-detail'),

    url(r'archives/',
        EditionListView.as_view(),
        name="newsletter-list"),

    url(r'^$',
        NewsletterView.as_view(),
        name="newsletter-latest")
)
