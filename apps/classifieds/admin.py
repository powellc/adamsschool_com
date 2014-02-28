from django.contrib import admin
from classifieds.models import Classified, ClassroomNeed

class ClassifiedAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'contact_name', 'created')
    date_hierarchy = 'created'
    list_filter = ('contact_name',)

admin.site.register(Classified, ClassifiedAdmin)

class ClassroomNeedAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'teacher', 'classroom', 'created')
    date_hierarchy = 'created'
    list_filter = ('teacher', 'classroom',)

admin.site.register(ClassroomNeed, ClassroomNeedAdmin)
