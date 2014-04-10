from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.models import TimeStampedModel
from django_extensions.db.fields import AutoSlugField


class UserDashboardModule(TimeStampedModel):
    title = models.CharField(_("Title"), max_length=255)
    slug = AutoSlugField(_('Slug'), populate_from='title')
    app_slug = models.CharField(_('App slug'), max_length=255)


class UserDashboard(TimeStampedModel):
    title = models.CharField(_("Title"), max_length=255)
    slug = AutoSlugField(_('Slug'), populate_from='title')
    modules = models.ManyToManyField(UserDashboardModule)

    class Meta:
        permissions = (("can_use_dashboard", "Can use user dashboard"),)
