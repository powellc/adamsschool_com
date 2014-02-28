from django.utils.translation import ugettext as _
from cms.plugin_pool import plugin_pool
from cms.plugin_base import CMSPluginBase
from staff.models import StaffListPlugin, Staff

class CMSStaffListPlugin(CMSPluginBase):
    """Plugin for including a list of staff members, filtered by type"""
    module = 'Teachers'
    model = StaffListPlugin
    name = _('Staff list')
    render_template = 'staff/_staff_list.html'
    fieldsets = (
        (None, {'fields': ('staff_type','template',)}),)

    def render(self, context, instance, placeholder):
        staff_list = Staff.objects.filter(type=instance.staff_type)
        if instance.template:
            self.render_template = instance.template
        context.update({'staff_list': staff_list,
                        'object': instance,
                        'placeholder': placeholder})
        return context

plugin_pool.register_plugin(CMSStaffListPlugin)
