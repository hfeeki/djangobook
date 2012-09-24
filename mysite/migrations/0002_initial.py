# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Publisher'
        db.create_table('mysite_publisher', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('state_province', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('website', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('publisher_description', self.gf('django.db.models.fields.CharField')(default=' This publisher description', max_length=200)),
        ))
        db.send_create_signal('mysite', ['Publisher'])

        # Adding model 'Author'
        db.create_table('mysite_author', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=40)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
        ))
        db.send_create_signal('mysite', ['Author'])

        # Adding model 'Book'
        db.create_table('mysite_book', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('publisher', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mysite.Publisher'])),
            ('publication_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('mysite', ['Book'])

        # Adding M2M table for field authors on 'Book'
        db.create_table('mysite_book_authors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('book', models.ForeignKey(orm['mysite.book'], null=False)),
            ('author', models.ForeignKey(orm['mysite.author'], null=False))
        ))
        db.create_unique('mysite_book_authors', ['book_id', 'author_id'])


    def backwards(self, orm):
        # Deleting model 'Publisher'
        db.delete_table('mysite_publisher')

        # Deleting model 'Author'
        db.delete_table('mysite_author')

        # Deleting model 'Book'
        db.delete_table('mysite_book')

        # Removing M2M table for field authors on 'Book'
        db.delete_table('mysite_book_authors')


    models = {
        'mysite.author': {
            'Meta': {'object_name': 'Author'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '40'})
        },
        'mysite.book': {
            'Meta': {'object_name': 'Book'},
            'authors': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['mysite.Author']", 'symmetrical': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'publication_date': ('django.db.models.fields.DateField', [], {}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mysite.Publisher']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mysite.publisher': {
            'Meta': {'ordering': "['name', 'city']", 'object_name': 'Publisher'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'publisher_description': ('django.db.models.fields.CharField', [], {'default': "' This publisher description'", 'max_length': '200'}),
            'state_province': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'website': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['mysite']