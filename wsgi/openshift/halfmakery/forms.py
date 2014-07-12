from django import forms
from django.utils.translation import ugettext as _
from halfmakery.models import Approach, Milestone, Task, Attempt, Address

class ApproachForm(forms.ModelForm):
    class Meta:
        model = Approach

class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        widgets = {'approach': forms.HiddenInput(),
                   'priority': forms.HiddenInput(),
                   'achieved': forms.HiddenInput(),
                   'details': forms.Textarea(attrs={'rows':3}) }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        widgets = {'milestone': forms.HiddenInput(),
                   'priority': forms.HiddenInput(),
                   'complete': forms.HiddenInput(),
                   'description': forms.Textarea(attrs={'rows':3}) }

class AttemptForm(forms.ModelForm):
    class Meta:
        model = Attempt
        widgets = {'task': forms.HiddenInput(),
                   'contents': forms.HiddenInput()}

class AttemptFormFull(forms.ModelForm):
    class Meta:
        model = Attempt
        widgets = {'task': forms.HiddenInput(),
                   'contents': forms.Textarea(attrs={'rows':30, 'cols': 50}) }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        widgets = {'user': forms.HiddenInput()}
