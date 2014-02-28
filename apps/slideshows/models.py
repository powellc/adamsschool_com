from django.db import models
from datetime import datetime
#from cms.models import CMSPlugin
from filer.fields.image import FilerImageField


class Slideshow(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, help_text="""This value is used in templates to identify
        this slideshow. You probably don't want to change this.""")
    interval = models.IntegerField(default=5,
            help_text="The number of seconds to spend on each slide.")
    transition = models.CharField(max_length=255, choices=(
            ('fade', 'Fade'),
            ('default', 'Instant'),
        ), default='fade', help_text="How should the slides transition?")
    active = models.BooleanField(default=False,
        help_text="Check this box to make this slideshow active. Other slideshows will be deactivated.")

    def __unicode__(self):
        return self.title

    def live_slides(self):
        return Slide.live.filter(slideshow=self)

    def save(self, *args, **kwargs):
        if self.active:
            Slideshow.objects.all().update(active=False)
            self.active = True
        super(Slideshow, self).save(*args, **kwargs)

    @property
    def interval_in_ms(self):
        return self.interval * 1000


class Slide(models.Model):
    ORDER = ((1, 'First'),
             (2, 'Second'),
             (3, 'Third'),
             (4, 'Fourth'),
             (5, 'Fifth'))
    slideshow = models.ForeignKey(Slideshow)
    title = models.CharField(blank=True, max_length=40,
            help_text="The main title to be display in the slide")
    description = models.CharField(blank=True, max_length=255,
            help_text="Short description to show below the slide title")
    photo = FilerImageField()
    button_text = models.CharField("Navigation Text", max_length=40, default='',
            help_text="Text to be used in the slideshow navigation")
    link_text = models.CharField(max_length=100, default='',
            help_text="Text to be used inside the slide for the slide link. Note that this text will appear ON TOP OF your graphic.", blank=True)
    target_url = models.CharField(max_length=1000,
            help_text="The URL to which this slide links.")
    order = models.IntegerField(default=5, choices=ORDER,
            help_text="The order of this slide in the slideshow. Lower numbers are listed earlier.")
    publish = models.BooleanField(default=True)
    publish_on = models.DateTimeField(default=datetime.now())

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ('order', '-publish_on')
