from django.db import models
from django.utils.translation import ugettext_lazy as _
from cms.models import CMSPlugin
from datetime import datetime, timedelta


class CurrentMenuManager(models.Manager):
    def this_week(self):
        """ Considers the current date and returns a context-appropriate
        menu objects.

        For example, if it's a week day, return the menu published for
        the current week. If it's a weekend day, return next week's menu.
        """
        today = datetime.today()
        if today.weekday() < 5: # If its Friday or earlier
            monday = today - timedelta(days=today.weekday())
        else:
            monday = today + timedelta(days=-today.weekday(), weeks=1)
        try:
            menu = self.get_query_set().get(start_date=monday)
        except:
            menu = None
        return menu


class LunchMenu(models.Model):
    start_date = models.DateField()
    monday = models.CharField(_('Monday'), max_length=255, blank=True, null=True)
    tuesday = models.CharField(_('Tuesday'), max_length=255, blank=True, null=True)
    wednesday = models.CharField(_('Wednesday'), max_length=255, blank=True, null=True)
    thursday = models.CharField(_('Thursday'), max_length=255, blank=True, null=True)
    friday = models.CharField(_('Friday'), max_length=255, blank=True, null=True)
    active = models.BooleanField(_('Active menu'), default=True)

    objects = CurrentMenuManager()

    def __unicode__(self):
        return "Lunch menu for the week of " + self.start_date.strftime('%A, %B %d')

    def save(self, *args, **kwargs):
        if self.active:
            LunchMenu.objects.all().update(active=False)
            self.active = True
        super(LunchMenu, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-start_date']
        get_latest_by = 'start_date'

class CurrentMenuPlugin(CMSPlugin):
    pass

class SelectedMenuPlugin(CMSPlugin):
    menu = models.ForeignKey(LunchMenu, blank=True, null=True)
