from django.core.urlresolvers import reverse
from django.db import models
from django.db.models import Q
from datetime import datetime, timedelta
from zinnia.models import Entry
from filer.fields.image import FilerImageField
from tinymce import models as tinymce_models
from lunches.models import LunchMenu

_ = lambda x: x

class PublishedObjectManager(models.Manager):
    def get_query_set(self):
        now = datetime.now()
        return super(PublishedObjectManager, self
            ).get_query_set().filter(published=True).filter(
            Q(publish_on__isnull=True)|Q(publish_on__lte=now))


class MainPlaceManager(models.Manager):
    def get_query_set(self):
        return super(MainPlaceManager, self).get_query_set().filter(place='M')


class SidebarPlaceManager(models.Manager):
    def get_query_set(self):
        return super(SidebarPlaceManager, self).get_query_set().filter(place='S')


class Edition(models.Model):
    header = FilerImageField(blank=True, null=True)
    header_caption = models.CharField(_('Header caption'), blank=True, null=True, max_length=255)
    header_description = models.TextField(_('Header description'), blank=True, null=True)
    published = models.BooleanField(_('Published'), default=False)
    publish_on = models.DateTimeField(_('Publish on'), default=datetime.now())
    # This model also pulls in the current week's lunch menu
    # and any classifieds that are live in the classifieds app

    objects = models.Manager()
    published_objects = PublishedObjectManager()

    def __unicode__(self):
        return u'Newsletter %s: %s' % (self.pk, self.publish_on)

    def get_absolute_url(self):
        return reverse('newsletter-detail', args=(self.id,))

    class Meta:
        verbose_name = 'Edition'
        verbose_name_plural = 'Editions'
        ordering = ['-publish_on']
        get_latest_by = 'publish_on'

    def blog_posts(self):
        '''
        Returns a set of blog posts published within the last five days.
        '''
        five_days = self.publish_on - timedelta(days=7)
        return Entry.published.filter(creation_date__gte=five_days)

    @property
    def lunch_menu(self):
        ''' Returns the lunch menu for the newsletters date.
            If no such lunch menu exists, it returns none. '''
        today = self.publish_on.date() + timedelta(weeks=1)
        if today.weekday() < 5:  # If its Friday or earlier
            monday = today - timedelta(days=today.weekday())
        else:
            monday = today + timedelta(days=-today.weekday(), weeks=1)
        try:
            menu = LunchMenu.objects.get(start_date=monday)
        except:
            menu = None
        return menu


class SectionCategory(models.Model):
    title = models.CharField(_('Title'), max_length=100)

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = 'Section category'
        verbose_name_plural = 'Section category'


class Section(models.Model):
    ORDER_CHOICES = (
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
        (6, 'Six'),
        (7, 'Seven'),
        (8, 'Eight'),
        (9, 'Nine'),
        (10, 'Ten'),)
    POSITION_CHOICES=(('left', 'Left'),
                      ('right', 'Right'),
                      ('full', 'Full'))
    edition = models.ForeignKey(Edition)
    title = models.CharField(_('Title'), max_length=255,
                             help_text="Acts like a new page when printed.")
    category = models.ForeignKey(SectionCategory, blank=True, null=True)
    image = FilerImageField(blank=True, null=True)
    image_position = models.CharField(_('Image position'), 
                                        max_length=5,
				                        default="full", 
                                        choices=POSITION_CHOICES, 
                                        blank=True, null=True)
    page_content=tinymce_models.HTMLField(_('Content'), blank=True, null=True)
    order = models.IntegerField(_('Order'), default=1, choices=ORDER_CHOICES)

    class Meta:
        verbose_name = 'Section'
        verbose_name_plural = 'Sections'
        ordering = ['order']

    def __unicode__(self):
        return u'%s in the %s newsletter' % (self.title, self.edition.publish_on)
