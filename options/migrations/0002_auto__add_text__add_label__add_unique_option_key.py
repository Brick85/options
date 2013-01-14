# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Text'
        db.create_table('options_text', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('value', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('options', ['Text'])

        # Adding model 'Label'
        db.create_table('options_label', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('key', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=256)),
        ))
        db.send_create_signal('options', ['Label'])

        # Removing index on 'Option', fields ['key']
        db.delete_index('options_option', ['key'])

        # Adding unique constraint on 'Option', fields ['key']
        db.create_unique('options_option', ['key'])


    def backwards(self, orm):
        # Removing unique constraint on 'Option', fields ['key']
        db.delete_unique('options_option', ['key'])

        # Adding index on 'Option', fields ['key']
        db.create_index('options_option', ['key'])

        # Deleting model 'Text'
        db.delete_table('options_text')

        # Deleting model 'Label'
        db.delete_table('options_label')


    models = {
        'options.label': {
            'Meta': {'ordering': "['key']", 'object_name': 'Label'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'options.option': {
            'Meta': {'ordering': "['key']", 'object_name': 'Option'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        },
        'options.text': {
            'Meta': {'ordering': "['key']", 'object_name': 'Text'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'key': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'value': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['options']