from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, TemplateView

from profiles.models import UserProfile
from lunches.models import LunchMenu
from zinnia.models import Entry
from .forms import EntryForm, ProfileForm


class DashboardView(TemplateView):
    template_name = 'dashboard/dashboard.html'


class ListBlogPosts(ListView):
    model = Entry
    template_name = 'dashboard/list_posts.html'


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
