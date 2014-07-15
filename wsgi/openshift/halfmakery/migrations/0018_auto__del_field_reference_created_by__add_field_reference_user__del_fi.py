# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Reference.created_by'
        db.delete_column('halfmakery_reference', 'created_by_id')

        # Adding field 'Reference.user'
        db.add_column('halfmakery_reference', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'TaskVote.created_by'
        db.delete_column('halfmakery_taskvote', 'created_by_id')

        # Adding field 'TaskVote.user'
        db.add_column('halfmakery_taskvote', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Approach.created_by'
        db.delete_column('halfmakery_approach', 'created_by_id')

        # Adding field 'Approach.user'
        db.add_column('halfmakery_approach', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Task.created_by'
        db.delete_column('halfmakery_task', 'created_by_id')

        # Adding field 'Task.user'
        db.add_column('halfmakery_task', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'MilestoneVote.created_by'
        db.delete_column('halfmakery_milestonevote', 'created_by_id')

        # Adding field 'MilestoneVote.user'
        db.add_column('halfmakery_milestonevote', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Attempt.created_by'
        db.delete_column('halfmakery_attempt', 'created_by_id')

        # Adding field 'Attempt.user'
        db.add_column('halfmakery_attempt', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Comment.created_by'
        db.delete_column('halfmakery_comment', 'created_by_id')

        # Adding field 'Comment.user'
        db.add_column('halfmakery_comment', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Milestone.created_by'
        db.delete_column('halfmakery_milestone', 'created_by_id')

        # Adding field 'Milestone.user'
        db.add_column('halfmakery_milestone', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Link.created_by'
        db.delete_column('halfmakery_link', 'created_by_id')

        # Adding field 'Link.user'
        db.add_column('halfmakery_link', 'user',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['auth.User']),
                      keep_default=False)


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Reference.created_by'
        raise RuntimeError("Cannot reverse this migration. 'Reference.created_by' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Reference.created_by'
        db.add_column('halfmakery_reference', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Reference.user'
        db.delete_column('halfmakery_reference', 'user_id')


        # User chose to not deal with backwards NULL issues for 'TaskVote.created_by'
        raise RuntimeError("Cannot reverse this migration. 'TaskVote.created_by' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'TaskVote.created_by'
        db.add_column('halfmakery_taskvote', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'TaskVote.user'
        db.delete_column('halfmakery_taskvote', 'user_id')


        # User chose to not deal with backwards NULL issues for 'Approach.created_by'
        raise RuntimeError("Cannot reverse this migration. 'Approach.created_by' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Approach.created_by'
        db.add_column('halfmakery_approach', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Approach.user'
        db.delete_column('halfmakery_approach', 'user_id')


        # User chose to not deal with backwards NULL issues for 'Task.created_by'
        raise RuntimeError("Cannot reverse this migration. 'Task.created_by' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Task.created_by'
        db.add_column('halfmakery_task', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Task.user'
        db.delete_column('halfmakery_task', 'user_id')


        # User chose to not deal with backwards NULL issues for 'MilestoneVote.created_by'
        raise RuntimeError("Cannot reverse this migration. 'MilestoneVote.created_by' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'MilestoneVote.created_by'
        db.add_column('halfmakery_milestonevote', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'MilestoneVote.user'
        db.delete_column('halfmakery_milestonevote', 'user_id')


        # User chose to not deal with backwards NULL issues for 'Attempt.created_by'
        raise RuntimeError("Cannot reverse this migration. 'Attempt.created_by' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Attempt.created_by'
        db.add_column('halfmakery_attempt', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Attempt.user'
        db.delete_column('halfmakery_attempt', 'user_id')


        # User chose to not deal with backwards NULL issues for 'Comment.created_by'
        raise RuntimeError("Cannot reverse this migration. 'Comment.created_by' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Comment.created_by'
        db.add_column('halfmakery_comment', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Comment.user'
        db.delete_column('halfmakery_comment', 'user_id')


        # User chose to not deal with backwards NULL issues for 'Milestone.created_by'
        raise RuntimeError("Cannot reverse this migration. 'Milestone.created_by' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Milestone.created_by'
        db.add_column('halfmakery_milestone', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Milestone.user'
        db.delete_column('halfmakery_milestone', 'user_id')


        # User chose to not deal with backwards NULL issues for 'Link.created_by'
        raise RuntimeError("Cannot reverse this migration. 'Link.created_by' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Link.created_by'
        db.add_column('halfmakery_link', 'created_by',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User']),
                      keep_default=False)

        # Deleting field 'Link.user'
        db.delete_column('halfmakery_link', 'user_id')


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
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Currency']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'halfmakery.approach': {
            'Meta': {'unique_together': "(('category', 'subcategory', 'idea', 'name'),)", 'object_name': 'Approach'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Category']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'goal': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['halfmakery.Idea']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sketch': ('django.db.models.fields.TextField', [], {}),
            'subcategory': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['halfmakery.Subcategory']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'halfmakery.attempt': {
            'Meta': {'object_name': 'Attempt'},
            'contents': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Task']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'halfmakery.category': {
            'Meta': {'object_name': 'Category'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'subcategory': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Subcategory']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'halfmakery.comment': {
            'Meta': {'object_name': 'Comment'},
            'approach': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Approach']"}),
            'attempt': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Attempt']", 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Currency']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Milestone']", 'null': 'True', 'blank': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Task']", 'null': 'True', 'blank': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'txid': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'halfmakery.currency': {
            'Meta': {'object_name': 'Currency'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '55'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'halfmakery.idea': {
            'Meta': {'object_name': 'Idea'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'halfmakery.link': {
            'Meta': {'object_name': 'Link'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Attempt']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'halfmakery.milestone': {
            'Meta': {'object_name': 'Milestone'},
            'achieved': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'approach': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Approach']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'halfmakery.milestonevote': {
            'Meta': {'object_name': 'MilestoneVote'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Milestone']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'halfmakery.reference': {
            'Meta': {'object_name': 'Reference'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Idea']"}),
            'summary': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'halfmakery.subcategory': {
            'Meta': {'object_name': 'Subcategory'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Idea']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'halfmakery.task': {
            'Meta': {'object_name': 'Task'},
            'complete': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Milestone']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'priority': ('django.db.models.fields.IntegerField', [], {'default': '0'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'halfmakery.taskvote': {
            'Meta': {'object_name': 'TaskVote'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Milestone']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['halfmakery']