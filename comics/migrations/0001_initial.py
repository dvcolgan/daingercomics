# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Comic'
        db.create_table('comics_comic', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=256)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('image_title', self.gf('django.db.models.fields.TextField')()),
            ('image_alt', self.gf('django.db.models.fields.TextField')()),
            ('post', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('comics', ['Comic'])

    def backwards(self, orm):
        # Deleting model 'Comic'
        db.delete_table('comics_comic')

    models = {
        'comics.comic': {
            'Meta': {'object_name': 'Comic'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_alt': ('django.db.models.fields.TextField', [], {}),
            'image_title': ('django.db.models.fields.TextField', [], {}),
            'post': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '256'})
        }
    }

    complete_apps = ['comics']