from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from models import CurrentMenuPlugin, SelectedMenuPlugin
from django.utils.translation import ugettext as _
from lunches.models import LunchMenu

class CMSCurrentMenuPlugin(CMSPluginBase):
    """Plugin for including the current lunch menu"""
    module = 'Lunches'
    model = CurrentMenuPlugin
    name = _("Current lunch menu")
    render_template = "lunches/current_menu.html"

    def render(self, context, instance, placeholder):
        menu = LunchMenu.objects.this_week()
        context.update({'current_menu':menu,
                        'object':instance,
                        'placeholder':placeholder})
        return context

plugin_pool.register_plugin(CMSCurrentMenuPlugin)

class CMSSelectedMenuPlugin(CMSPluginBase):
    """Plugin for including a selectedlunch menu"""
    module = 'Lunches'
    model = SelectedMenuPlugin
    name = _("Selected lunch menu")
    render_template = "lunches/current_menu.html"
    fieldsets = (
        (None, {'fields': ('menu',)}),)

    def render(self, context, instance, placeholder):
        context.update({'current_menu':instance.menu,
                        'object':instance,
                        'placeholder':placeholder})
        return context

plugin_pool.register_plugin(CMSSelectedMenuPlugin)
