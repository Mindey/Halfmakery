from django import forms
from django.utils.translation import ugettext as _
from halfmakery.models import Approach

class ApproachForm(forms.ModelForm):
    class Meta:
        model=Approach
