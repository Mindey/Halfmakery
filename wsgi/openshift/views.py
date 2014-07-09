import os
from django.shortcuts import render_to_response
from registration.views import RegistrationView, ActivationView
from django.template import RequestContext

def home(request):
    from halfmakery.models import Approach
    approaches = Approach.objects.all()
    return render_to_response('home/home.html',{'approaches': approaches},context_instance=RequestContext(request))

def about(request):
    return render_to_response('home/about.html')
