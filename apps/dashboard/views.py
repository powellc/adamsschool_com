from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, TemplateView

from lunches.models import LunchMenu
from zinnia.models import Entry
from .forms import EntryForm


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
