# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'SelectedMenuPlugin'
        db.create_table('cmsplugin_selectedmenuplugin', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cms.CMSPlugin'], unique=True, primary_key=True)),
            ('menu', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lunches.LunchMenu'], null=True, blank=True)),
        ))
        db.send_create_signal('lunches', ['SelectedMenuPlugin'])

        # Deleting field 'CurrentMenuPlugin.current_menu'
        db.delete_column('cmsplugin_currentmenuplugin', 'current_menu_id')


    def backwards(self, orm):
        # Deleting model 'SelectedMenuPlugin'
        db.delete_table('cmsplugin_selectedmenuplugin')

        # Adding field 'CurrentMenuPlugin.current_menu'
        db.add_column('cmsplugin_currentmenuplugin', 'current_menu',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['lunches.LunchMenu'], null=True, blank=True),
                      keep_default=False)


    models = {
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2013, 3, 8, 0, 0)'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'max_length': '15', 'db_index': 'True'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.CMSPlugin']", 'null': 'True', 'blank': 'True'}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '50', 'db_index': 'True'})
        },
        'lunches.currentmenuplugin': {
            'Meta': {'object_name': 'CurrentMenuPlugin', 'db_table': "'cmsplugin_currentmenuplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'})
        },
        'lunches.lunchmenu': {
            'Meta': {'ordering': "['-start_date']", 'object_name': 'LunchMenu'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'friday': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'monday': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'thursday': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'tuesday': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'wednesday': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        'lunches.selectedmenuplugin': {
            'Meta': {'object_name': 'SelectedMenuPlugin', 'db_table': "'cmsplugin_selectedmenuplugin'", '_ormbases': ['cms.CMSPlugin']},
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['cms.CMSPlugin']", 'unique': 'True', 'primary_key': 'True'}),
            'menu': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['lunches.LunchMenu']", 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['lunches']