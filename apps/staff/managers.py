from django.db import models

class TeacherManager(models.Manager):
    def get_query_set(self):
        return super(TeacherManager, self).get_query_set().filter(type__title='Teacher').filter(active=True)

class StaffManager(models.Manager):
    def get_query_set(self):
        return super(StaffManager, self).get_query_set().filter(type__title='Staff').filter(active=True)

class ConsultantManager(models.Manager):
    def get_query_set(self):
        return super(ConsultantManager, self).get_query_set().filter(type__title='Consultant').filter(active=True)

class ActiveManager(models.Manager):
    def get_query_set(self):
        return super(ActiveManager, self).get_query_set().filter(active=True).order_by('name')
