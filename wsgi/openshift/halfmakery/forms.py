from django import forms
from django.utils.translation import ugettext as _
from halfmakery.models import Approach, Milestone

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
