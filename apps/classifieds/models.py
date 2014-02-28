from django.db import models
from datetime import datetime, timedelta
from django.conf import settings

class Ad(models.Model):
    created = models.DateTimeField(null=True,blank=True,default=datetime.now())

    class Meta:
        abstract = True

    @property
    def expires_in(self):
        '''
        Returns the number of days till the ad expires.
        '''
        expiration = getattr(settings, 'CLASSIFIED_EXPIRATION_DAYS', 7)
        return (self.created + timedelta(days=expiration) - datetime.now()).days()


    @property
    def expired(self):
        expiration = getattr(settings, 'CLASSIFIED_EXPIRATION_DAYS', 7)
        if self.created + timedelta(days=expiration) < datetime.now():
            return True
        else:
            return False

class ClassroomNeed(Ad):
    title = models.CharField(max_length=100)
    teacher = models.CharField(max_length=100, blank=True, null=True)
    classroom = models.CharField(max_length=100, blank=True, null=True)
    need = models.TextField()

    class Meta:
        verbose_name = 'Classroom Need'
        verbose_name_plural = 'Classroom Need'
        ordering = ['-created']


    def __unicode__(self):
        if self.teacher:
            return ' '.join([self.teacher, ':', self.need[:100], '...'])
        else:
            return ' '.join([self.classroom, ':', self.need[:100], '...'])

class Classified(Ad):
    contact_name = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(blank=True, null=True, help_text='If the ad has an associated date.')
    copy = models.TextField()
    contact_email = models.EmailField(blank=True, null=True)
    contact_phone = models.CharField(max_length=12, blank=True, null=True)

    class Meta:
        verbose_name = 'Classified'
        verbose_name_plural = 'Classifieds'
        ordering = ['-created']

    def __unicode__(self):
        return u'%s from %s' % (self.title, self.contact_name)
