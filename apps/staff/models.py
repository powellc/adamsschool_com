from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.contrib.localflavor.us.models import PhoneNumberField
from tinymce import models as tinymce_models

#from articles.models import Article
from django_extensions.db.models import TitleSlugDescriptionModel, TimeStampedModel
from django_extensions.db.fields import AutoSlugField
from staff.managers import TeacherManager, StaffManager, ConsultantManager, ActiveManager

from cms.models import CMSPlugin
from cms.models.fields import PlaceholderField

class School(TitleSlugDescriptionModel):
    """
    School model class.

    Manages a school.

    """
    principal=models.ForeignKey('Staff', blank=True, null=True, related_name='principal')
    photo=models.ImageField(_('Photo'), blank=True, null=True, upload_to='staff/school/')
    primary=models.BooleanField(_('Primary'), default=False, 
            help_text='Is this the sites primary, or only school?')
    email=models.EmailField(_('Email'), blank=True, null=True)
    url=models.CharField(_('URL'), blank=True, null=True, max_length=255)
    address=models.CharField(_('Address'), max_length=200)
    city=models.CharField(_('City'), max_length=50)
    state=models.CharField(_('State'), max_length=50)
    zipcode=models.CharField(_('ZIP Code'), max_length=5)
    phone=PhoneNumberField(_('Phone'), max_length=12)
    po_box=models.IntegerField(_('P.O. Box'), blank=True, null=True, max_length=4)
    fax=PhoneNumberField(_('Fax'), blank=True, null=True)

    class Meta:
        verbose_name=_('School')
        verbose_name_plural=_('Schools')

    def __unicode__(self):
        return u'%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return ('cl-school-detail', None, {'slug': self.slug})

class Position(TitleSlugDescriptionModel, TimeStampedModel):
    """
    Position model, but not like homework position, but rather staff position.

    """
    abbreviated_title=models.CharField(_('Abbreviated title'), blank=True, null=True, max_length=40)

    class Meta:
        verbose_name=_('Position')
        verbose_name_plural=_('Positions')

    def __unicode__(self):
        return u'%s' % self.title

    @property
    def shortened_title(self):
        if self.abbreviated_title: return self.abbreviated_title
        else: return self.title

    @models.permalink
    def get_absolute_url(self):
        return ('cl-position-detail', None, {'slug': self.slug})

class StaffType(TimeStampedModel, TitleSlugDescriptionModel):
    """
    Staff Type model.

    """

    class Meta:
        verbose_name=_('Staff type')
        verbose_name_plural=_('Staff types')

    def __unicode__(self):
        return u'%s' % self.title

class Website(TimeStampedModel, TitleSlugDescriptionModel):
    """
    Website model for keeping track of staff websites
    """
    url=models.CharField(_('URL Address'), max_length=255)

    class Meta:
        verbose_name=_('Website')
        verbose_name_plural=_('Websites')

    def __unicode__(self):
        return u'%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return ('cl-website-detail', None, {'slug': self.slug})

class Staff(TimeStampedModel):
    """
    Staff model class.

    """
    name=models.CharField(_('Name'), max_length=100)
    title=models.CharField(_('Title'), blank=True, null=True, max_length=20)
    slug=AutoSlugField(_('Slug'), populate_from='name')
    school=models.ForeignKey(School)
    mug=models.ImageField(_('Mug'), blank=True, null=True, upload_to='staff/mugs/')
    photo=models.ImageField(_('Photo'), blank=True, null=True, upload_to='staff/photos/')
    user=models.ForeignKey(User, blank=True, null=True)
    email=models.EmailField(_('Email'), max_length=200, blank=True, null=True)
    active=models.BooleanField(_('Active'),
            help_text='Is this staff member currently active?', default=False)
    type=models.ForeignKey(StaffType)
    bio=tinymce_models.HTMLField(_('Biography'), blank=True, null=True)
    order=models.IntegerField(_('Order'), blank=True, null=True)
    positions=models.ManyToManyField(Position, blank=True, null=True)
    page_title = models.CharField(_('Page title'), max_length=100, blank=True, null=True)
    background = models.CharField(_('Background'), max_length=255, blank=True, null=True, help_text=_('URL to a background for the staff page.'))
    main_content = PlaceholderField(_('Main content'), blank=True, null=True, related_name='main_content')
    sidebar = PlaceholderField(_('Sidebar content'), blank=True, null=True, related_name='sidebar_content')
    template_name = models.CharField(_('template name'), max_length=255, blank=True, help_text=_("Example: 'staff/staff/best-staff-ever.html'. If this isn't provided, the system will use 'staff/staff_detail.html'."))
    homework_calendar = models.CharField(_('Homework Calendar URL'), max_length=255, blank=True, null=True)

    objects = models.Manager()
    active_objects=ActiveManager()
    teacher_objects=TeacherManager()
    staff_objects=StaffManager()
    consultant_objects=ConsultantManager()

    class Meta:
        verbose_name=_('Staff')
        verbose_name_plural=_('Staff')
        ordering=('order',)

    @property
    def first_name(self):
        return self.name.split(' ')[0]

    def last_name(self):
        return " ".join(self.name.split(' ')[1:])

    def __unicode__(self):
        return u'%s' % self.name

    @models.permalink
    def get_absolute_url(self):
        return ('teacher_detail', None, {'slug': self.slug})

class StaffListPlugin(CMSPlugin):
    """CMS Plugin for displaying list of staff"""

    staff_type = models.ForeignKey(StaffType,
        blank=True, null=True)
    template = models.CharField(max_length=255, blank=True, null=True)

    def __unicode__(self):
        if self.staff_type:
            title = _('%s list') % self.staff_type
        else:
            title = _('All staff list')
        return title

    def copy_relations(self, oldinstance):
        self.staff_type = oldinstance.staff_type.all()
