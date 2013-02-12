# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Comic.image_alt'
        db.alter_column('comics_comic', 'image_alt', self.gf('django.db.models.fields.CharField')(max_length=511))

        # Changing field 'Comic.title'
        db.alter_column('comics_comic', 'title', self.gf('django.db.models.fields.CharField')(max_length=255))

        # Changing field 'Comic.image_title'
        db.alter_column('comics_comic', 'image_title', self.gf('django.db.models.fields.CharField')(max_length=511))

    def backwards(self, orm):

        # Changing field 'Comic.image_alt'
        db.alter_column('comics_comic', 'image_alt', self.gf('django.db.models.fields.TextField')())

        # Changing field 'Comic.title'
        db.alter_column('comics_comic', 'title', self.gf('django.db.models.fields.CharField')(max_length=256))

        # Changing field 'Comic.image_title'
        db.alter_column('comics_comic', 'image_title', self.gf('django.db.models.fields.TextField')())

    models = {
        'comics.backgroundimage': {
            'Meta': {'object_name': 'BackgroundImage'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        'comics.comic': {
            'Meta': {'object_name': 'Comic'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'image_alt': ('django.db.models.fields.CharField', [], {'max_length': '511', 'blank': 'True'}),
            'image_title': ('django.db.models.fields.CharField', [], {'max_length': '511', 'blank': 'True'}),
            'post': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['comics']