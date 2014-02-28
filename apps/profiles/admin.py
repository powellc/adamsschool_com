from django.contrib import admin
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

from profiles.models import UserProfile

admin.site.register(UserProfile)
