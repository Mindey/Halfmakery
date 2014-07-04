# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'TaskLink'
        db.delete_table('halfmakery_tasklink')

        # Deleting model 'Page'
        db.delete_table('halfmakery_page')

        # Adding model 'TaskPage'
        db.create_table('halfmakery_taskpage', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Task'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('contents', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('halfmakery', ['TaskPage'])

        # Adding model 'PageLink'
        db.create_table('halfmakery_pagelink', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Task'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=4096)),
        ))
        db.send_create_signal('halfmakery', ['PageLink'])


        # Changing field 'PageComment.page'
        db.alter_column('halfmakery_pagecomment', 'page_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.TaskPage']))

    def backwards(self, orm):
        # Adding model 'TaskLink'
        db.create_table('halfmakery_tasklink', (
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Task'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=4096)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('halfmakery', ['TaskLink'])

        # Adding model 'Page'
        db.create_table('halfmakery_page', (
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('contents', self.gf('django.db.models.fields.TextField')()),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Task'])),
        ))
        db.send_create_signal('halfmakery', ['Page'])

        # Deleting model 'TaskPage'
        db.delete_table('halfmakery_taskpage')

        # Deleting model 'PageLink'
        db.delete_table('halfmakery_pagelink')


        # Changing field 'PageComment.page'
        db.alter_column('halfmakery_pagecomment', 'page_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Page']))

    models = {
        'halfmakery.approach': {
            'Meta': {'object_name': 'Approach'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'goal': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Idea']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'halfmakery.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55'})
        },
        'halfmakery.currency': {
            'Meta': {'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55'})
        },
        'halfmakery.idea': {
            'Meta': {'object_name': 'Idea'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Subcategory']"})
        },
        'halfmakery.idealink': {
            'Meta': {'object_name': 'IdeaLink'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Idea']"}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '4096'})
        },
        'halfmakery.milestone': {
            'Meta': {'object_name': 'Milestone'},
            'achieved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'approach': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Approach']"}),
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'halfmakery.milestonevote': {
            'Meta': {'object_name': 'MilestoneVote'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Milestone']"}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'halfmakery.pagecomment': {
            'Meta': {'object_name': 'PageComment'},
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Currency']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.TaskPage']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'txid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'halfmakery.pagelink': {
            'Meta': {'object_name': 'PageLink'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Task']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '4096'})
        },
        'halfmakery.subcategory': {
            'Meta': {'object_name': 'Subcategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'halfmakery.task': {
            'Meta': {'object_name': 'Task'},
            'complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Milestone']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'halfmakery.taskpage': {
            'Meta': {'object_name': 'TaskPage'},
            'contents': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Task']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'halfmakery.taskvote': {
            'Meta': {'object_name': 'TaskVote'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Milestone']"}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['halfmakery']