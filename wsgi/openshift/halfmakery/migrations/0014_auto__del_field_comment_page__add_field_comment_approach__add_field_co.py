# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Comment.page'
        db.delete_column('halfmakery_comment', 'page_id')

        # Adding field 'Comment.approach'
        db.add_column('halfmakery_comment', 'approach',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['halfmakery.Approach']),
                      keep_default=False)

        # Adding field 'Comment.milestone'
        db.add_column('halfmakery_comment', 'milestone',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Milestone'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Comment.task'
        db.add_column('halfmakery_comment', 'task',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Task'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Comment.attempt'
        db.add_column('halfmakery_comment', 'attempt',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Attempt'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Comment.page'
        raise RuntimeError("Cannot reverse this migration. 'Comment.page' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Comment.page'
        db.add_column('halfmakery_comment', 'page',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Attempt']),
                      keep_default=False)

        # Deleting field 'Comment.approach'
        db.delete_column('halfmakery_comment', 'approach_id')

        # Deleting field 'Comment.milestone'
        db.delete_column('halfmakery_comment', 'milestone_id')

        # Deleting field 'Comment.task'
        db.delete_column('halfmakery_comment', 'task_id')

        # Deleting field 'Comment.attempt'
        db.delete_column('halfmakery_comment', 'attempt_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'halfmakery.address': {
            'Meta': {'object_name': 'Address'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Currency']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'halfmakery.approach': {
            'Meta': {'unique_together': "(('category', 'subcategory', 'idea', 'name'),)", 'object_name': 'Approach'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Category']"}),
            'goal': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['halfmakery.Idea']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sketch': ('django.db.models.fields.TextField', [], {}),
            'subcategory': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['halfmakery.Subcategory']"})
        },
        'halfmakery.attempt': {
            'Meta': {'object_name': 'Attempt'},
            'contents': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Task']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'halfmakery.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Subcategory']"})
        },
        'halfmakery.comment': {
            'Meta': {'object_name': 'Comment'},
            'approach': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Approach']"}),
            'attempt': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Attempt']", 'null': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Currency']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Milestone']", 'null': 'True', 'blank': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Task']", 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'txid': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'halfmakery.currency': {
            'Meta': {'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55'})
        },
        'halfmakery.idea': {
            'Meta': {'object_name': 'Idea'},
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'halfmakery.link': {
            'Meta': {'object_name': 'Link'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Attempt']"}),
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
        'halfmakery.reference': {
            'Meta': {'object_name': 'Reference'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Idea']"}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '4096'})
        },
        'halfmakery.subcategory': {
            'Meta': {'object_name': 'Subcategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Idea']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
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
        'halfmakery.taskvote': {
            'Meta': {'object_name': 'TaskVote'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Milestone']"}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['halfmakery']