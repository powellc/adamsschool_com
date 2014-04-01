from django.conf.urls.defaults import url, patterns
from dashboard import views

urlpatterns = patterns(
    '',
    url(r'^$',
        view=views.DashboardView.as_view(),
        name="dashboard"),
    url(r'^posts/add/$',
        view=views.CreateBlogPosts.as_view(),
        name="add-post"),
    url(r'^posts/update/(?P<id>[\d_])/$',
        view=views.UpdateBlogPosts.as_view(),
        name="update-post"),
    url(r'^posts/$',
        view=views.ListBlogPosts.as_view(),
        name="list-posts"),
    url(r'^menus/add/$',
        view=views.CreateMenus.as_view(),
        name="add-menu"),
    url(r'^menus/update/(?P<id>[\d_])/$',
        view=views.UpdateMenus.as_view(),
        name="update-menu"),
    url(r'^menus/$',
        view=views.ListMenus.as_view(),
        name="list-menus"),
)
