"""Plugins for CMS"""

from django.conf import settings
from django.utils.translation import ugettext as _

from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase

from cmsplugin_zinnia_category.models import CategoryEntriesPlugin

class CMSEntriesByCategoryPlugin(CMSPluginBase):
    """Plugin for including a category's worth of entries"""
    module = 'Zinnia'
    model = CategoryEntriesPlugin
    name = _('Entries by category')
    render_template = 'cmsplugin_zinnia/entry_list.html'
    fields = ('category', 'template_to_render')
    text_enabled = True

    def render(self, context, instance, placeholder):
        """Update the context with plugin's data"""
        context.update({'entries': instance.category.entries.all(),
                        'category': instance.category,
                        'object': instance,
                        'placeholder': placeholder})
        return context

    def icon_src(self, instance):
        """Icon source of the plugin"""
        return settings.STATIC_URL + u'cmsplugin_zinnia/img/plugin.png'

plugin_pool.register_plugin(CMSEntriesByCategoryPlugin)
