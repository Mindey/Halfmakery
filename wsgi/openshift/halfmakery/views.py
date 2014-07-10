# Create your views here.

from halfmakery import forms
from django.shortcuts import render, redirect
from halfmakery.models import Approach

def approach_add(request, template_name='halfmakery/approach_tpl.html'):
    """ This view will be used to add
        approaches, depending on the POST and GET variables we get."""
    form = forms.ApproachForm(request.POST or None)
    validity = False
    if form.is_valid():
        validity = True
        form.save()
        return redirect('/')
    return render(request, template_name, {'form': form,
                                           'valid': validity,
                                           'form_action': '/approach/' })
    
def approach_edit(request, approach_id, template_name='halfmakery/approach_tpl.html'):
    """ This view will be used to edit
        approaches, depending on the POST and GET variables we get."""
    approach = Approach.objects.get(id=approach_id)
    form = forms.ApproachForm(request.POST or None, instance=approach)
    if form.is_valid():
        form.save()

    return render(request, template_name, {'form': form,
                                           'req': request,
                                           'form_action': '/approach/'+str(approach_id)})

def approach_delete(request, approach_id, action, template_name='halfmakery/approach_tpl.html'):
    """ This view will be used to delete
        approaches, depending on the POST and GET variables we get."""
    approach = Approach.objects.get(id=approach_id)
    approach.delete()
    return redirect('/')

