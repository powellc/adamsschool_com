# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Notification.expires'
        db.add_column('notifications_notification', 'expires',
                      self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Notification.expires'
        db.delete_column('notifications_notification', 'expires')


    models = {
        'notifications.notification': {
            'Meta': {'ordering': "['-show_this_message']", 'object_name': 'Notification'},
            'expires': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'show_this_message': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'db_index': 'True'}),
            'shown_since': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['notifications']