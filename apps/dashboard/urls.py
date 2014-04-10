from django.conf.urls.defaults import url, patterns
from dashboard import views

urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[-\w]+)/$',
        view=views.DashboardView.as_view(),
        name="dashboard"),

    url(r'^(?P<slug>[-\w]+)/(?P<app_name>[-\w]+)/$',
        view=views.DashboardModuleView.as_view(),
        name="dashboard-module"),

    url(r'^(?P<slug>[-\w]+)/(?P<app_name>[-\w]+)/add/$',
        view=views.DashboardModuleCreateView.as_view(),
        name="dashboard-module-create"),

    url(r'^(?P<slug>[-\w]+)/(?P<app_name>[-\w]+)/update/(?P<id>[\d]+)/$',
        view=views.DashboardModuleUpdateView.as_view(),
        name="dashboard-module-update"),

    url(r'^profile/update/(?P<pk>[\d_])/$',
        view=views.UpdateProfile.as_view(),
        name="update-profile"),
)
