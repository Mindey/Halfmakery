from django import forms
from django.utils.translation import ugettext as _
from halfmakery.models import Approach, Milestone, Task, Attempt, Address, Comment

class ApproachForm(forms.ModelForm):
    class Meta:
        model = Approach
        exclude = ['user']

class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        exclude = ['user']
        widgets = {'approach': forms.HiddenInput(),
                   'priority': forms.HiddenInput(),
                   'achieved': forms.HiddenInput(),
                   'details': forms.Textarea(attrs={'rows':3}) }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['user']
        widgets = {'milestone': forms.HiddenInput(),
                   'priority': forms.HiddenInput(),
                   'complete': forms.HiddenInput(),
                   'description': forms.Textarea(attrs={'rows':3}) }

class AttemptForm(forms.ModelForm):
    class Meta:
        exclude = ['user']
        model = Attempt
        widgets = {'task': forms.HiddenInput(),
                   'contents': forms.HiddenInput()}

class AttemptFormFull(forms.ModelForm):
    class Meta:
        model = Attempt
        exclude = ['user']
        widgets = {'task': forms.HiddenInput(),
                   'contents': forms.Textarea(attrs={'rows':30, 'cols': 50}) }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['user']
        widgets = {'user': forms.HiddenInput()}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user']
        widgets = {'approach': forms.HiddenInput(),
                   'milestone': forms.HiddenInput(),
                   'task': forms.HiddenInput(),
                   'attempt': forms.HiddenInput(),
                   'text': forms.Textarea(attrs={'rows':3}) }
