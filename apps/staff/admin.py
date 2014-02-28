from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdmin

from staff.models import StaffType, Staff, Position, School

#admin.site.register(Room)
admin.site.register(Staff, PlaceholderAdmin)
admin.site.register(StaffType)
admin.site.register(Position)
admin.site.register(School)
