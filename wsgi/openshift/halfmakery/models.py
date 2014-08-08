from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxLengthValidator
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.
# User....

class Category(models.Model):
    name = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return unicode(self.name)

class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey('Category')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return unicode(self.name)

class Currency(models.Model):
    name = models.CharField(max_length=55)
    code = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
         return self.code

class Idea(models.Model):
    category = models.ForeignKey('Category')
    subcategory = ChainedForeignKey(Subcategory, chained_field='category', chained_model_field='category', auto_choose=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    reference = models.URLField(max_length=4096)
    currency = models.ForeignKey(Currency)
    txid = models.CharField(max_length=255)
    user = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return unicode(self.name)

class Approach(models.Model):
    category = models.ForeignKey(Category)
    subcategory = ChainedForeignKey(Subcategory, chained_field='category', chained_model_field='category', auto_choose=True)
    idea = ChainedForeignKey(Idea, chained_field='subcategory', chained_model_field='subcategory', auto_choose=True)
    name = models.CharField(max_length=255)
    goal = models.CharField(max_length=255)
    sketch = models.TextField(validators=[MaxLengthValidator(4096)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    class Meta:
        unique_together = ('category', 'subcategory', 'idea', 'name')
    def __unicode__(self):
        return '%s %s %s' % (self.category, self.subcategory, self.idea)

class Milestone(models.Model):
    approach = models.ForeignKey(Approach)
    priority = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    details = models.TextField(validators=[MaxLengthValidator(4096)], blank=True)
    achieved = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
         return self.name

class Task(models.Model):
    milestone = models.ForeignKey(Milestone)
    priority = models.IntegerField(default=0)
    name = models.CharField(max_length=255)
    description = models.TextField(validators=[MaxLengthValidator(4096)], blank=True)
    complete = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
         return self.name

class Attempt(models.Model): # Note: Attempt is the page itself, where we document what we did...
    task = models.ForeignKey(Task)
    title = models.CharField(max_length=255, blank=True)
    contents = models.TextField(validators=[MaxLengthValidator(65536)], blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
         return self.title

class Link(models.Model):
    task = models.ForeignKey(Attempt)
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    url = models.CharField(max_length=4096)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    def __unicode__(self):
         return self.title

class Comment(models.Model):
    approach = models.ForeignKey(Approach)
    milestone = models.ForeignKey(Milestone, blank=True, null=True)
    task = models.ForeignKey(Task, blank=True, null=True)
    attempt = models.ForeignKey(Attempt, blank=True, null=True)
    currency = models.ForeignKey(Currency, default=1)
    txid = models.CharField(max_length=255)
    text = models.TextField(validators=[MaxLengthValidator(4096)])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)
    recipients = models.ManyToManyField(User, related_name='user', blank=False)
    satoshis = models.BigIntegerField(blank=False)

    def __unicode__(self):
         return self.text

class MilestoneVote(models.Model):
    milestone = models.ForeignKey(Milestone)
    value = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    def __integer__(self):
         return self.value

class TaskVote(models.Model):
    milestone = models.ForeignKey(Milestone)
    value = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User)

    def __integer__(self):
         return self.value

class Address(models.Model):
    user = models.ForeignKey(User)
    currency = models.ForeignKey(Currency)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
