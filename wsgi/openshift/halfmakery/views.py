# Create your views here.

from halfmakery import forms
from django.shortcuts import render, redirect

def approach(request, template_name='halfmakery/approach_tpl.html'):
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
    

def approach_list(request, template_name='halfmakery/approach_list_tpl.html'):
    return render(request, template_name, {})   
