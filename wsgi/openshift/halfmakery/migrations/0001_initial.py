# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('halfmakery_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=55)),
        ))
        db.send_create_signal('halfmakery', ['Category'])

        # Adding model 'Subcategory'
        db.create_table('halfmakery_subcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('halfmakery', ['Subcategory'])

        # Adding model 'Idea'
        db.create_table('halfmakery_idea', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Category'])),
            ('subcategory', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Subcategory'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('halfmakery', ['Idea'])

        # Adding model 'IdeaLink'
        db.create_table('halfmakery_idealink', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idea', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Idea'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=4096)),
        ))
        db.send_create_signal('halfmakery', ['IdeaLink'])

        # Adding model 'Approach'
        db.create_table('halfmakery_approach', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('idea', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Idea'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('goal', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('halfmakery', ['Approach'])

        # Adding model 'Milestone'
        db.create_table('halfmakery_milestone', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('approach', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Approach'])),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('details', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('halfmakery', ['Milestone'])

        # Adding model 'Task'
        db.create_table('halfmakery_task', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('milestone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Milestone'])),
            ('priority', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('halfmakery', ['Task'])

        # Adding model 'TaskLink'
        db.create_table('halfmakery_tasklink', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Task'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('summary', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=4096)),
        ))
        db.send_create_signal('halfmakery', ['TaskLink'])

        # Adding model 'Page'
        db.create_table('halfmakery_page', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('task', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Task'])),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('contents', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('halfmakery', ['Page'])

        # Adding model 'Currency'
        db.create_table('halfmakery_currency', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=55)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=5)),
        ))
        db.send_create_signal('halfmakery', ['Currency'])

        # Adding model 'PageComment'
        db.create_table('halfmakery_pagecomment', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('page', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Page'])),
            ('currency', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Currency'])),
            ('txid', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('text', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('halfmakery', ['PageComment'])

        # Adding model 'MilestoneVote'
        db.create_table('halfmakery_milestonevote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('milestone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Milestone'])),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('halfmakery', ['MilestoneVote'])

        # Adding model 'TaskVote'
        db.create_table('halfmakery_taskvote', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('milestone', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Milestone'])),
            ('value', self.gf('django.db.models.fields.IntegerField')(default=0)),
        ))
        db.send_create_signal('halfmakery', ['TaskVote'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('halfmakery_category')

        # Deleting model 'Subcategory'
        db.delete_table('halfmakery_subcategory')

        # Deleting model 'Idea'
        db.delete_table('halfmakery_idea')

        # Deleting model 'IdeaLink'
        db.delete_table('halfmakery_idealink')

        # Deleting model 'Approach'
        db.delete_table('halfmakery_approach')

        # Deleting model 'Milestone'
        db.delete_table('halfmakery_milestone')

        # Deleting model 'Task'
        db.delete_table('halfmakery_task')

        # Deleting model 'TaskLink'
        db.delete_table('halfmakery_tasklink')

        # Deleting model 'Page'
        db.delete_table('halfmakery_page')

        # Deleting model 'Currency'
        db.delete_table('halfmakery_currency')

        # Deleting model 'PageComment'
        db.delete_table('halfmakery_pagecomment')

        # Deleting model 'MilestoneVote'
        db.delete_table('halfmakery_milestonevote')

        # Deleting model 'TaskVote'
        db.delete_table('halfmakery_taskvote')


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
        'halfmakery.page': {
            'Meta': {'object_name': 'Page'},
            'contents': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Task']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'halfmakery.pagecomment': {
            'Meta': {'object_name': 'PageComment'},
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Currency']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Page']"}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'txid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'halfmakery.subcategory': {
            'Meta': {'object_name': 'Subcategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'halfmakery.task': {
            'Meta': {'object_name': 'Task'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Milestone']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'halfmakery.tasklink': {
            'Meta': {'object_name': 'TaskLink'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Task']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '4096'})
        },
        'halfmakery.taskvote': {
            'Meta': {'object_name': 'TaskVote'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Milestone']"}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['halfmakery']