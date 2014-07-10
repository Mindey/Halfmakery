# Create your views here.

from halfmakery import forms
from django.shortcuts import render, redirect
from halfmakery.models import Approach, Milestone

# Limit of most people's short term memory
MAX_MILESTONES_COUNT = 8

def approach_add(request, template_name='halfmakery/approach_tpl.html'):
    """ This view will be used to add
        approaches, depending on the POST and GET variables we get."""
    form = forms.ApproachForm(request.POST or None)
    validity = False
    if form.is_valid():
        validity = True
        approach = form.save()
        return redirect('/approach/'+str(approach.id))
    return render(request, template_name, {'form': form,
                                           'valid': validity,
                                           'form_action': '/approach/' })

def approach_view(request, approach_id, template_name='halfmakery/approach_tpl.html'):
    """ This view will be used to edit
        approaches, depending on the POST and GET variables we get."""
    approach = Approach.objects.get(id=approach_id)
    form = forms.ApproachForm(request.POST or None, instance=approach)
    if form.is_valid():
        form.save()

    milestone_form = forms.MilestoneForm(initial={'approach': approach_id})
    milestones = Milestone.objects.all().filter(approach_id=approach_id).order_by('-priority')

    return render(request, template_name, {'form': form,
                                           'milestones': milestones,
                                           'milestone_form': milestone_form,
                                           'milestones_limit_reached': milestones.count() >= MAX_MILESTONES_COUNT,
                                           'req': request,
                                           'form_action': '/approach/'+str(approach_id)})

def approach_action(request, approach_id, action, template_name='halfmakery/approach_tpl.html'):
    """ This view will be used to delete, and execute actions of its depenents
        approaches, depending on the POST and GET variables we get."""

    # Delete Approach
    if action == 'delete':
        approach = Approach.objects.get(id=approach_id)
        approach.delete()
        return redirect('/')

    # Create Milestone
    elif action == 'milestone':
        form = forms.MilestoneForm(request.POST or None)
        if Milestone.objects.all().filter(approach_id=approach_id).count() < MAX_MILESTONES_COUNT:
            if form.is_valid():
                form.save()
        else:
            """MAX_MILESTONES_COUNT reached."""
            pass

    return redirect('/approach/'+str(approach_id))

def milestone_action(request, approach_id, milestone, milestone_id, action, template_name='halfmakery/approach_tpl.html'):
    """ Delete a Milestone. """

    if action == 'delete':
        milestone = Milestone.objects.get(id=milestone_id)
        milestone.delete()
        return redirect('/approach/'+str(approach_id))

    return redirect('/approach/'+str(approach_id))

def milestone_view(request, approach_id, milestone, milestone_id, template_name='halfmakery/milestone_tpl.html'):
    milestone = Milestone.objects.get(id=milestone_id)
    form = forms.MilestoneForm(request.POST or None, instance=milestone)
    if form.is_valid():
        form.save()
    
    return render(request, template_name, {'form': form,
                                           'return_link': '/approach/%s' % (approach_id,),
                                           'form_action': '/approach/%s/milestone/%s' % (approach_id, milestone_id)})


