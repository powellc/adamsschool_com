# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Notification'
        db.create_table('notifications_notification', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('show_this_message', self.gf('django.db.models.fields.BooleanField')(default=False, db_index=True)),
            ('shown_since', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
        ))
        db.send_create_signal('notifications', ['Notification'])


    def backwards(self, orm):
        # Deleting model 'Notification'
        db.delete_table('notifications_notification')


    models = {
        'notifications.notification': {
            'Meta': {'ordering': "['-show_this_message']", 'object_name': 'Notification'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show_this_message': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'shown_since': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['notifications']