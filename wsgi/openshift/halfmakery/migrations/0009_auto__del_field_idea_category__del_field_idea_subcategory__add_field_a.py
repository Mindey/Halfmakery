# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Idea.category'
        db.delete_column('halfmakery_idea', 'category_id')

        # Deleting field 'Idea.subcategory'
        db.delete_column('halfmakery_idea', 'subcategory_id')

        # Adding field 'Approach.category'
        db.add_column('halfmakery_approach', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['halfmakery.Category']),
                      keep_default=False)

        # Adding field 'Approach.subcategory'
        db.add_column('halfmakery_approach', 'subcategory',
                      self.gf('smart_selects.db_fields.ChainedForeignKey')(default=1, to=orm['halfmakery.Subcategory']),
                      keep_default=False)


        # Changing field 'Approach.idea'
        db.alter_column('halfmakery_approach', 'idea_id', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['halfmakery.Idea']))
        # Adding field 'Subcategory.idea'
        db.add_column('halfmakery_subcategory', 'idea',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['halfmakery.Idea']),
                      keep_default=False)


        # Changing field 'Subcategory.name'
        db.alter_column('halfmakery_subcategory', 'name', self.gf('django.db.models.fields.CharField')(max_length=20))
        # Adding field 'Category.subcategory'
        db.add_column('halfmakery_category', 'subcategory',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['halfmakery.Subcategory']),
                      keep_default=False)


        # Changing field 'Category.name'
        db.alter_column('halfmakery_category', 'name', self.gf('django.db.models.fields.CharField')(max_length=20))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Idea.category'
        raise RuntimeError("Cannot reverse this migration. 'Idea.category' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Idea.category'
        db.add_column('halfmakery_idea', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Category']),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'Idea.subcategory'
        raise RuntimeError("Cannot reverse this migration. 'Idea.subcategory' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Idea.subcategory'
        db.add_column('halfmakery_idea', 'subcategory',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Subcategory']),
                      keep_default=False)

        # Deleting field 'Approach.category'
        db.delete_column('halfmakery_approach', 'category_id')

        # Deleting field 'Approach.subcategory'
        db.delete_column('halfmakery_approach', 'subcategory_id')


        # Changing field 'Approach.idea'
        db.alter_column('halfmakery_approach', 'idea_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['halfmakery.Idea']))
        # Deleting field 'Subcategory.idea'
        db.delete_column('halfmakery_subcategory', 'idea_id')


        # Changing field 'Subcategory.name'
        db.alter_column('halfmakery_subcategory', 'name', self.gf('django.db.models.fields.CharField')(max_length=255))
        # Deleting field 'Category.subcategory'
        db.delete_column('halfmakery_category', 'subcategory_id')


        # Changing field 'Category.name'
        db.alter_column('halfmakery_category', 'name', self.gf('django.db.models.fields.CharField')(max_length=55))

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
            'Meta': {'object_name': 'Approach'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Category']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'goal': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': "orm['halfmakery.Idea']"}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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
            'currency': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Currency']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Attempt']"}),
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
        'halfmakery.suggestion': {
            'Meta': {'object_name': 'Suggestion'},
            'approach': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['halfmakery.Approach']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'text': ('django.db.models.fields.TextField', [], {})
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