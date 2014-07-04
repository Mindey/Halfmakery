from django.db import models
from django.core.validators import MaxLengthValidator

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=55)

    def __unicode__(self):
         return self.name

class Subcategory(models.Model):
    name = models.CharField(max_length=255)

    def __unicode__(self):
         return self.name

class Idea(models.Model):
    category = models.ForeignKey(Category)
    subcategory = models.ForeignKey(Subcategory)
    name = models.CharField(max_length=255)
    description = models.TextField(validators=[MaxLengthValidator(4096)])

    def __unicode__(self):
         return self.name

class IdeaLink(models.Model):
    idea = models.ForeignKey(Idea)
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    url = models.CharField(max_length=4096)

    def __unicode__(self):
         return self.title

class Approach(models.Model):
    idea = models.ForeignKey(Idea)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=4096)

    def __unicode__(self):
         return self.name

class Milestone(models.Model):
    approach = models.ForeignKey(Approach)
    priority = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    description = models.TextField(validators=[MaxLengthValidator(4096)])

    def __unicode__(self):
         return self.name

class Task(models.Model):
    milestone = models.ForeignKey(Milestone)
    priority = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    description = models.TextField(validators=[MaxLengthValidator(4096)])

    def __unicode__(self):
         return self.name

class TaskLink(models.Model):
    task = models.ForeignKey(Task)
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    url = models.CharField(max_length=4096)

    def __unicode__(self):
         return self.title

class Page(models.Model):
    task = models.ForeignKey(Task)
    title = models.CharField(max_length=255)
    contents = models.TextField(validators=[MaxLengthValidator(65536)])

    def __unicode__(self):
         return self.title

class Currency(models.Model):
    name = models.CharField(max_length=55)
    code = models.CharField(max_length=5)

    def __unicode__(self):
         return self.name

class PageComment(models.Model):
    page = models.ForeignKey(Page)
    currency = models.ForeignKey(Currency)
    txid = models.CharField(max_length=255)
    text = models.TextField(validators=[MaxLengthValidator(4096)])

    def __unicode__(self):
         return self.text

class MilestoneVote(models.Model):
    milestone = models.ForeignKey(Milestone)
    value = models.IntegerField(default=0)

    def __unicode__(self):
         return self.value

class TaskVote(models.Model):
    milestone = models.ForeignKey(Milestone)
    value = models.IntegerField(default=0)

    def __unicode__(self):
         return self.value
