# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'AlertsPluginModel'
        db.create_table('alerts_alertspluginmodel', (
            ('cmsplugin_ptr', self.gf('django.db.models.fields.related.OneToOneField')(primary_key=True, unique=True, to=orm['cms.CMSPlugin'])),
            ('alert_type', self.gf('django.db.models.fields.CharField')(max_length=32, default='')),
            ('alert_title', self.gf('django.db.models.fields.CharField')(max_length=32, default='')),
            ('alert_msg', self.gf('django.db.models.fields.CharField')(max_length=32, default='')),
        ))
        db.send_create_signal('alerts', ['AlertsPluginModel'])


    def backwards(self, orm):
        # Deleting model 'AlertsPluginModel'
        db.delete_table('alerts_alertspluginmodel')


    models = {
        'alerts.alertspluginmodel': {
            'Meta': {'_ormbases': ['cms.CMSPlugin'], 'object_name': 'AlertsPluginModel'},
            'alert_msg': ('django.db.models.fields.CharField', [], {'max_length': '32', 'default': "''"}),
            'alert_title': ('django.db.models.fields.CharField', [], {'max_length': '32', 'default': "''"}),
            'alert_type': ('django.db.models.fields.CharField', [], {'max_length': '32', 'default': "''"}),
            'cmsplugin_ptr': ('django.db.models.fields.related.OneToOneField', [], {'primary_key': 'True', 'unique': 'True', 'to': "orm['cms.CMSPlugin']"})
        },
        'cms.cmsplugin': {
            'Meta': {'object_name': 'CMSPlugin'},
            'changed_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True', 'auto_now': 'True'}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '15'}),
            'level': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'lft': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'null': 'True', 'to': "orm['cms.CMSPlugin']"}),
            'placeholder': ('django.db.models.fields.related.ForeignKey', [], {'null': 'True', 'to': "orm['cms.Placeholder']"}),
            'plugin_type': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '50'}),
            'position': ('django.db.models.fields.PositiveSmallIntegerField', [], {'blank': 'True', 'null': 'True'}),
            'rght': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'}),
            'tree_id': ('django.db.models.fields.PositiveIntegerField', [], {'db_index': 'True'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'db_index': 'True', 'max_length': '255'})
        }
    }

    complete_apps = ['alerts']