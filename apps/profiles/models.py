from datetime import date
from django.db import models
from django.contrib.auth.models import User
from django.contrib.localflavor.us.models import PhoneNumberField
from django.utils.translation import ugettext_lazy as _
from multiblogs.models import Blog
     
class UserProfile(models.Model):
    url = models.URLField(_('URL'), blank=True, null=True)
    phone_numer = PhoneNumberField(_('Phone number'), blank=True, null=True)
    birthday = models.DateField(_('Birthday'), blank=True, null=True)
    grade = models.IntegerField(_('Grade'), blank=True, null=True, max_length=2)
    mug = models.ImageField(_('Mug'), blank=True, null=True, upload_to='profiles/mugs/')
    user = models.ForeignKey(User, unique=True)

    @property
    def age(self):
        if self.birthday:
            today = date.today()
            try: # raised when birth date is February 29 and the current year is not a leap year
                birthday = self.birthday.replace(year=today.year)
            except ValueError:
                birthday = self.birthday.replace(year=today.year, day=self.birthday.day-1)
            if birthday > today:
                return today.year - self.birthday.year - 1
            else:
                return today.year - self.birthday.year
        else:
            return None

    @property
    def full_name(self):
        if self.user.first_name or self.user.last_name:
            return _(self.user.first_name + " " + self.user.last_name)
        else:
            return self.user.username

    @property
    def blogs(self):
        blogs=[]
	for b in Blog.published_objects.all():
           if self.user in b.authors.all():
               blogs.append(b)
        return blogs

    def __unicode__(self):
        return self.full_name + "'s profile"
