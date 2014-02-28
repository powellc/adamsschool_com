from datetime import datetime
from BeautifulSoup import BeautifulSoup
from cms.plugin_base import CMSPluginBase
from cms.models import CMSPlugin
from cms.plugin_pool import plugin_pool
from newsletters.models import Edition

class LatestNewsletterContentPlugin(CMSPluginBase):
    model = CMSPlugin
    name = u'Latest Newsletter'
    render_template = 'newsletters/newsletter.html'

    def render(self, context, instance, placeholder):
        newsletters = Edition.objects.filter(
                publish=True, publish_on__lte=datetime.now())
        if newsletters.count():
            context['content'] = BeautifulSoup(
                    Edition.published_objects.latest().html_content).prettify()
        return context
plugin_pool.register_plugin(LatestNewsletterContentPlugin)

