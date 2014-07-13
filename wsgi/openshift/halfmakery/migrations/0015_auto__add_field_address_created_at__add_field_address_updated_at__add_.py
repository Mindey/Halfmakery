# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Address.created_at'
        db.add_column('halfmakery_address', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Address.updated_at'
        db.add_column('halfmakery_address', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Reference.created_at'
        db.add_column('halfmakery_reference', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Reference.updated_at'
        db.add_column('halfmakery_reference', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'TaskVote.created_at'
        db.add_column('halfmakery_taskvote', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'TaskVote.updated_at'
        db.add_column('halfmakery_taskvote', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Idea.created_at'
        db.add_column('halfmakery_idea', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Idea.updated_at'
        db.add_column('halfmakery_idea', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Approach.created_at'
        db.add_column('halfmakery_approach', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Approach.updated_at'
        db.add_column('halfmakery_approach', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Task.created_at'
        db.add_column('halfmakery_task', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Task.updated_at'
        db.add_column('halfmakery_task', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Currency.created_at'
        db.add_column('halfmakery_currency', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Currency.updated_at'
        db.add_column('halfmakery_currency', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'MilestoneVote.created_at'
        db.add_column('halfmakery_milestonevote', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'MilestoneVote.updated_at'
        db.add_column('halfmakery_milestonevote', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Attempt.created_at'
        db.add_column('halfmakery_attempt', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Attempt.updated_at'
        db.add_column('halfmakery_attempt', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Comment.created_at'
        db.add_column('halfmakery_comment', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Comment.updated_at'
        db.add_column('halfmakery_comment', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Subcategory.created_at'
        db.add_column('halfmakery_subcategory', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Subcategory.updated_at'
        db.add_column('halfmakery_subcategory', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Category.created_at'
        db.add_column('halfmakery_category', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Category.updated_at'
        db.add_column('halfmakery_category', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Milestone.created_at'
        db.add_column('halfmakery_milestone', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Milestone.updated_at'
        db.add_column('halfmakery_milestone', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Link.created_at'
        db.add_column('halfmakery_link', 'created_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Link.updated_at'
        db.add_column('halfmakery_link', 'updated_at',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2014, 7, 13, 0, 0), blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Address.created_at'
        db.delete_column('halfmakery_address', 'created_at')

        # Deleting field 'Address.updated_at'
        db.delete_column('halfmakery_address', 'updated_at')

        # Deleting field 'Reference.created_at'
        db.delete_column('halfmakery_reference', 'created_at')

        # Deleting field 'Reference.updated_at'
        db.delete_column('halfmakery_reference', 'updated_at')

        # Deleting field 'TaskVote.created_at'
        db.delete_column('halfmakery_taskvote', 'created_at')

        # Deleting field 'TaskVote.updated_at'
        db.delete_column('halfmakery_taskvote', 'updated_at')

        # Deleting field 'Idea.created_at'
        db.delete_column('halfmakery_idea', 'created_at')

        # Deleting field 'Idea.updated_at'
        db.delete_column('halfmakery_idea', 'updated_at')

        # Deleting field 'Approach.created_at'
        db.delete_column('halfmakery_approach', 'created_at')

        # Deleting field 'Approach.updated_at'
        db.delete_column('halfmakery_approach', 'updated_at')

        # Deleting field 'Task.created_at'
        db.delete_column('halfmakery_task', 'created_at')

        # Deleting field 'Task.updated_at'
        db.delete_column('halfmakery_task', 'updated_at')

        # Deleting field 'Currency.created_at'
        db.delete_column('halfmakery_currency', 'created_at')

        # Deleting field 'Currency.updated_at'
        db.delete_column('halfmakery_currency', 'updated_at')

        # Deleting field 'MilestoneVote.created_at'
        db.delete_column('halfmakery_milestonevote', 'created_at')

        # Deleting field 'MilestoneVote.updated_at'
        db.delete_column('halfmakery_milestonevote', 'updated_at')

        # Deleting field 'Attempt.created_at'
        db.delete_column('halfmakery_attempt', 'created_at')

        # Deleting field 'Attempt.updated_at'
        db.delete_column('halfmakery_attempt', 'updated_at')

        # Deleting field 'Comment.created_at'
        db.delete_column('halfmakery_comment', 'created_at')

        # Deleting field 'Comment.updated_at'
        db.delete_column('halfmakery_comment', 'updated_at')

        # Deleting field 'Subcategory.created_at'
        db.delete_column('halfmakery_subcategory', 'created_at')

        # Deleting field 'Subcategory.updated_at'
        db.delete_column('halfmakery_subcategory', 'updated_at')

        # Deleting field 'Category.created_at'
        db.delete_column('halfmakery_category', 'created_at')

        # Deleting field 'Category.updated_at'
        db.delete_column('halfmakery_category', 'updated_at')

        # Deleting field 'Milestone.created_at'
        db.delete_column('halfmakery_milestone', 'created_at')

        # Deleting field 'Milestone.updated_at'
        db.delete_column('halfmakery_milestone', 'updated_at')

        # Deleting field 'Link.created_at'
        db.delete_column('halfmakery_link', 'created_at')

        # Deleting field 'Link.updated_at'
        db.delete_column('halfmakery_link', 'updated_at')


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
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'halfmakery.attempt': {
            'Meta': {'object_name': 'Attempt'},
            'contents': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'task': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Task']"}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
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
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
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
            'url': ('django.db.models.fields.CharField', [], {'max_length': '4096'})
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
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'halfmakery.milestonevote': {
            'Meta': {'object_name': 'MilestoneVote'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Milestone']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
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
            'url': ('django.db.models.fields.CharField', [], {'max_length': '4096'})
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
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'})
        },
        'halfmakery.taskvote': {
            'Meta': {'object_name': 'TaskVote'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'milestone': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Milestone']"}),
            'updated_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'value': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['halfmakery']