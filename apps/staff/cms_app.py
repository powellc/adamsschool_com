"""Applications hooks for cmsplugin_zinnia"""
from django.utils.translation import ugettext_lazy as _

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool


class ClassroomApphook(CMSApp):
    """Classroom's Apphook"""
    name = _('Classroom Manager')
    urls = ['staff.urls']

apphook_pool.register(ClassroomApphook)
