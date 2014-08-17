import os
from django.shortcuts import render_to_response
from registration.views import RegistrationView, ActivationView
from django.template import RequestContext

def home(request):
    from halfmakery.models import Approach, Comment
    approaches = Approach.objects.all()
    approach_list = []
    for item in approaches:
        coin_count = float(sum([i.satoshis for i in Comment.objects.all().filter(approach=item,currency=1)]))/(10**8)
        approach_list.append((item, coin_count))
    return render_to_response('home/home.html',{'approaches': approach_list},context_instance=RequestContext(request))

def about(request):
    return render_to_response('home/about.html',{},context_instance=RequestContext(request))

def news(request):
    return render_to_response('home/news.html',{},context_instance=RequestContext(request))
