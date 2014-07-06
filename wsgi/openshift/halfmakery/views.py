# Create your views here.

from halfmakery import forms
from django.shortcuts import render

def approach(request, template_name='halfmakery/approach_tpl.html'):
    """ This view will be used to add, edit, delete, and modify
        approaches, depending on the POST and GET variables we get."""
    form = forms.ApproachForm(request.POST or None)
    return render(request, template_name, {'form': form})
    
