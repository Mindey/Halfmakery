from django import forms
from django.utils.translation import ugettext as _

class ApproachForm(forms.Form):
    name = forms.CharField(_('Name'), required=True)
