from datetime import datetime
from django.contrib.sitemaps import Sitemap
from articles.models import Article

class NewsSitemap(Sitemap):
    changefreq="always"
    priority=0.5
    
    def items(self):
        return Article.objects.filter(publish__gte=datetime.now())
    
    def lastmod(self, obj):
        return obj.publish
    
