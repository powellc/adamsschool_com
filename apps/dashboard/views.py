from django.conf import settings
from django.db.models.loading import get_model
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, TemplateView
from braces import views

from profiles.models import UserProfile
from lunches.models import LunchMenu
from zinnia.models import Entry
from .forms import EntryForm, ProfileForm


def lookup_model(model_name):
    model = None
    for app in settings.INSTALLED_APPS:
        model = get_model(app, model_name)
        if model:
            break
    return model


class PermissionsView(views.LoginRequiredMixin,
                      views.PermissionRequiredMixin):
    permission_required = "dashboard.dashboard_access"


class DashboardView(PermissionsView, TemplateView):
    template_name = 'dashboard/dashboard.html'


class DashboardModuleCreateView(PermissionsView, CreateView):
    template_name = 'dashboard/module_form.html'

    def get_queryset(self):
        app_model = lookup_model(self.kwargs['app_name'])
        return app_model.objects.all()


class DashboardModuleUpdateView(PermissionsView, CreateView):
    template_name = 'dashboard/module_form.html'

    def get_queryset(self):
        app_model = lookup_model(self.kwargs['app_name'])
        return app_model.objects.all()



class DashboardModuleView(ListView):
    template_name = 'dashboard/list_objects.html'

    def get_queryset(self, *args, **kwargs):
        app_model = lookup_model(self.kwargs['app_name'])
        return app_model.objects.all()



class UpdateBlogPosts(UpdateView):
    model = Entry
    form_class = EntryForm
    success_url = '/dashboard/posts/'
    template_name = 'dashboard/post_form.html'


class CreateBlogPosts(CreateView):
    model = Entry
    form_class = EntryForm
    success_url = '/dashboard/posts/'
    template_name = 'dashboard/post_form.html'


class ListMenus(ListView):
    model = LunchMenu
    template_name = 'dashboard/list_menus.html'


class UpdateMenus(UpdateView):
    model = LunchMenu
    success_url = '/dashboard/menus/'
    template_name = 'dashboard/menu_form.html'


class CreateMenus(CreateView):
    model = LunchMenu
    success_url = '/dashboard/menus/'
    template_name = 'dashboard/menu_form.html'


class UpdateProfile(UpdateView):
    model = UserProfile
    form_class = ProfileForm
    success_url = '/dashboard/'
    template_name = 'dashboard/profile_form.html'
