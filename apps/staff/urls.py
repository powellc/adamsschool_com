from django.conf.urls.defaults import url, patterns
from django.views.generic import DetailView, ListView
from staff.models import Staff

urlpatterns = patterns('',
    url(r'^$', view=ListView.as_view(queryset=Staff.teacher_objects.all(),
        template_name="staff/index.html"),
        name="teacher_list"),
	url(r'^(?P<slug>[-\w]+)/$', view=DetailView.as_view(model=Staff,
                                                        template_name_field='template_name'),
                                                        name="teacher_detail"),
)
