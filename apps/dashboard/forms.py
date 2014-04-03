from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django import forms

from zinnia.models import Entry
from profiles.models import UserProfile


class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'image', 'content', 'tags')

    def save(self, force_insert=False, force_update=False, commit=True):
        m = super(EntryForm, self).save(commit=False)
        m.slug = slugify(m.title)
        if commit:
            m.save()
        return m


class ProfileForm(forms.ModelForm):
    name = forms.CharField(max_length=255, required=True)

    class Meta:
        model = UserProfile
        exclude = ('url', 'phone_numer', 'birthday', 'user',)

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        try:
            self.fields['name'].initial = self.instance.full_name
        except User.DoesNotExist:
            pass

    def save(self, *args, **kwargs):
        """
        Update the name on the related User object as well.
        """
        u = self.instance.user
        first, last = self.cleaned_data['name'].split(' ')
        u.first_name = first
        u.last_name = last
        u.save()
        profile = super(ProfileForm, self).save(*args, **kwargs)
        return profile
