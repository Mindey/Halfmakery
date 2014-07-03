import os
from django.shortcuts import render_to_response
from registration.views import RegistrationView, ActivationView
from django.template import RequestContext

def home(request):
    return render_to_response('home/home.html',context_instance=RequestContext(request))

def about(request):
    return render_to_response('home/about.html')
