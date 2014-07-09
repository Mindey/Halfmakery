# Create your views here.

from halfmakery import forms
from django.shortcuts import render, redirect
from halfmakery.models import Approach

def approach_add(request, template_name='halfmakery/approach_tpl.html'):
    """ This view will be used to add, edit, delete, and modify
        approaches, depending on the POST and GET variables we get."""
    form = forms.ApproachForm(request.POST or None)
    validity = False
    if form.is_valid():
        validity = True
        form.save()
        return redirect('/')
    return render(request, template_name, {'form': form,
                                           'req': request,
                                           'valid': validity})
    
def approach_edit(request, approach_id, template_name='halfmakery/approach_tpl.html'):
    """ This view will be used to add, edit, delete, and modify
        approaches, depending on the POST and GET variables we get."""
    
    approach = Approach.objects.all().filter(id=int(approach_id))[0] 
    form = forms.ApproachForm(instance=approach)

    return render(request, template_name, {'form': form})
