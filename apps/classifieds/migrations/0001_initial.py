# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ClassroomNeed'
        db.create_table('classifieds_classroomneed', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 25, 0, 0), null=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('teacher', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('classroom', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('need', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('classifieds', ['ClassroomNeed'])

        # Adding model 'Classified'
        db.create_table('classifieds_classified', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2013, 2, 25, 0, 0), null=True, blank=True)),
            ('contact_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('copy', self.gf('django.db.models.fields.TextField')()),
            ('contact_email', self.gf('django.db.models.fields.EmailField')(max_length=75, null=True, blank=True)),
            ('contact_phone', self.gf('django.db.models.fields.CharField')(max_length=12, null=True, blank=True)),
        ))
        db.send_create_signal('classifieds', ['Classified'])


    def backwards(self, orm):
        # Deleting model 'ClassroomNeed'
        db.delete_table('classifieds_classroomneed')

        # Deleting model 'Classified'
        db.delete_table('classifieds_classified')


    models = {
        'classifieds.classified': {
            'Meta': {'ordering': "['-created']", 'object_name': 'Classified'},
            'contact_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'null': 'True', 'blank': 'True'}),
            'contact_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'contact_phone': ('django.db.models.fields.CharField', [], {'max_length': '12', 'null': 'True', 'blank': 'True'}),
            'copy': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 25, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'classifieds.classroomneed': {
            'Meta': {'ordering': "['-created']", 'object_name': 'ClassroomNeed'},
            'classroom': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 2, 25, 0, 0)', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'need': ('django.db.models.fields.TextField', [], {}),
            'teacher': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['classifieds']