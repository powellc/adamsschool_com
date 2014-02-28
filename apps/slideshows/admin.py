from django.contrib import admin

from slideshows.models import Slideshow, Slide

class SlideInline(admin.StackedInline):
    fields = ('title', 'photo', 'description', 'target_url', 'order', 'publish')
    model = Slide
    extra = 0

class SlideshowAdmin(admin.ModelAdmin):
    inlines = (SlideInline,)
    list_display = ('title', 'active',)
    fieldsets = (
        (None, {
            'fields': ('title', 'active', 'interval',),
            'description': 'Note: Only the first five slides will be shown in'
                ' the slideshow.',
        }),
    )
admin.site.register(Slideshow, SlideshowAdmin)
