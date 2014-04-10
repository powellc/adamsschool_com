from django.contrib import admin

from .models import UserDashboardModule, UserDashboard

admin.site.register(UserDashboard)
admin.site.register(UserDashboardModule)
