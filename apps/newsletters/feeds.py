from django.contrib.syndication.views import Feed
from datetime import time, datetime

from apps.newsletters.models import Edition

class LatestNewsletterFeed(Feed):
    title = "Adams School Weekly Newsletter"
    link = "/newsletters/feeds/weekly/"
    description = "Latest newsletter feed"

    def items(self):
        return Edition.published_objects.all()

    def item_title(self, item):
        return item.__unicode__()

    def item_link(self, item):
        return '/newsletter/' + str(item.id)

    def item_description(self, item):
        return "No description"

    def item_pubdate(self, item):
        return datetime.combine(item.publish_on, time())

