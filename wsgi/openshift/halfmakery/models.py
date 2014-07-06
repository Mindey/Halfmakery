from django.db import models
from django.contrib.auth.models import User
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

class Reference(models.Model):
    idea = models.ForeignKey(Idea)
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    url = models.CharField(max_length=4096)

    def __unicode__(self):
         return self.title

class Approach(models.Model):
    idea = models.ForeignKey(Idea)
    name = models.CharField(max_length=255)
    goal = models.CharField(max_length=255)
    description = models.TextField(validators=[MaxLengthValidator(4096)])

    def __unicode__(self):
         return self.name

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
