from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.

class Idea(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField() #validators=[MaxLengthValidator(4096)])
    def __unicode__(self):
        return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=20)
    idea = models.ForeignKey(Idea)
    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)
    subcategory = models.ForeignKey('Subcategory')
    def __unicode__(self):
        return self.name

class Approach(models.Model):
    category = models.ForeignKey(Category)
    subcategory = ChainedForeignKey(Subcategory, chained_field='category', chained_model_field='category', auto_choose=True)
    idea = ChainedForeignKey(Idea, chained_field='subcategory', chained_model_field='subcategory', auto_choose=True)
    name = models.CharField(max_length=255)
    goal = models.CharField(max_length=255)
    sketch = models.TextField(validators=[MaxLengthValidator(4096)])
    class Meta:
        unique_together = ('category', 'subcategory', 'idea', 'name')
    def __unicode__(self):
        return '%s %s %s' % (self.category, self.subcategory, self.idea)

class Reference(models.Model):
    idea = models.ForeignKey(Idea)
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    url = models.CharField(max_length=4096)

    def __unicode__(self):
         return self.title

class Suggestion(models.Model):
    approach = models.ForeignKey(Approach)
    text = models.TextField(validators=[MaxLengthValidator(4096)])

    def __unicode__(self):
         return self.text

class Milestone(models.Model):
    approach = models.ForeignKey(Approach)
    priority = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    details = models.TextField(validators=[MaxLengthValidator(4096)], blank=True)
    achieved = models.BooleanField()

    def __unicode__(self):
         return self.name

class Task(models.Model):
    milestone = models.ForeignKey(Milestone)
    priority = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    description = models.TextField(validators=[MaxLengthValidator(4096)], blank=True)
    complete = models.BooleanField()

    def __unicode__(self):
         return self.name

class Attempt(models.Model):
    task = models.ForeignKey(Task)
    title = models.CharField(max_length=255, blank=True)
    contents = models.TextField(validators=[MaxLengthValidator(65536)], blank=True)

    def __unicode__(self):
         return self.title

class Link(models.Model):
    task = models.ForeignKey(Attempt)
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    url = models.CharField(max_length=4096)

    def __unicode__(self):
         return self.title

class Currency(models.Model):
    name = models.CharField(max_length=55)
    code = models.CharField(max_length=5)

    def __unicode__(self):
         return self.name

class Comment(models.Model):
    page = models.ForeignKey(Attempt)
    currency = models.ForeignKey(Currency)
    txid = models.CharField(max_length=255)
    text = models.TextField(validators=[MaxLengthValidator(4096)])

    def __unicode__(self):
         return self.text

class MilestoneVote(models.Model):
    milestone = models.ForeignKey(Milestone)
    value = models.IntegerField(default=0)

    def __integer__(self):
         return self.value

class TaskVote(models.Model):
    milestone = models.ForeignKey(Milestone)
    value = models.IntegerField(default=0)

    def __integer__(self):
         return self.value

class Address(models.Model):
    user = models.ForeignKey(User)
    currency = models.ForeignKey(Currency)
    address = models.CharField(max_length=255)
