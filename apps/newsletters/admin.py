from django.contrib import admin
from newsletters.models import Edition, Section, SectionCategory
from cms.admin.placeholderadmin import PlaceholderAdmin

class CategorySectionAdmin(admin.ModelAdmin):
    list_display = ('title', )
admin.site.register(SectionCategory, CategorySectionAdmin)

class SectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'edition', 'order', )
    list_filter = ('edition',)
    list_editable = ('order', )

class SectionInline(admin.StackedInline):
    model = Section

class EditionAdmin(PlaceholderAdmin):
    inlines = [SectionInline]
    list_display = ('publish_on', 'published')
    list_editable = ('published', )
    date_hierarchy = 'publish_on'

admin.site.register(Edition, EditionAdmin)
