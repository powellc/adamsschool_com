from django.template.defaultfilters import slugify
from django.forms import ModelForm
from zinnia.models import Entry


class EntryForm(ModelForm):
    class Meta:
        model = Entry
        fields = ('title', 'image', 'content', 'tags')

    def save(self, force_insert=False, force_update=False, commit=True):
        m = super(EntryForm, self).save(commit=False)
        m.slug = slugify(m.title)
        if commit:
            m.save()
        return m
