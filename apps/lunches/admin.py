from django.contrib import admin
#from cms.admin.placeholderadmin import PlaceholderAdmin
from models import LunchMenu


class LunchMenuAdmin(admin.ModelAdmin):
    model = LunchMenu

admin.site.register(LunchMenu, LunchMenuAdmin)
