"""Models of Zinnia CMS Plugins"""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from cms.models import CMSPlugin
from zinnia.models import Category

from cmsplugin_zinnia.settings import PLUGINS_TEMPLATES

TEMPLATES = [('cmsplugin_zinnia/entry_list.html', _('Entry list (default)')),
             ('cmsplugin_zinnia/entry_detail.html', _('Entry detailed')),
             ('cmsplugin_zinnia/entry_slider.html', _('Entry slider'))] + \
             PLUGINS_TEMPLATES

class CategoryEntriesPlugin(CMSPlugin):
    """CMS Plugin for displaying category of entries"""

    category = models.ForeignKey(
        Category, verbose_name=_('category'))
    template_to_render = models.CharField(
        _('template'), blank=True,
        max_length=250, choices=TEMPLATES,
        help_text=_('template used to display the plugin'))

    @property
    def render_template(self):
        """Override render_template to use
        the template_to_render attribute"""
        return self.template_to_render

    def copy_relations(self, old_instance):
        """Duplicate ManyToMany relations on plugin copy"""
        self.category = old_instance.category

    def __unicode__(self):
        return _('%s') % self.category


