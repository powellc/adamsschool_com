from datetime import datetime
from BeautifulSoup import BeautifulSoup
from cms.plugin_base import CMSPluginBase
from cms.models import CMSPlugin
from cms.plugin_pool import plugin_pool
from classifieds.models import Classified, ClassroomNeed

class LatestAdsPlugin(CMSPluginBase):
    model = CMSPlugin
    name = u'Latest Classified Ads'
    render_template = 'classifieds/classified_list.html'

    def render(self, context, instance, placeholder):
        ads = Classified.objects.filter(
            expired=False, publish_on__lte=datetime.now())
        context['ads'] = ads
        return context
plugin_pool.register_plugin(LatestAdsPlugin)
