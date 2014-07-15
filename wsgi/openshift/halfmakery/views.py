# Create your views here.

from halfmakery import forms
from django.shortcuts import render, redirect
from halfmakery.models import Approach, Milestone, Task, Attempt, Address, Comment
from django.contrib.auth.models import User

# Limit of most people's short term memory
MAX_MILESTONES_COUNT = 8

def approach_add(request, template_name='halfmakery/approach_tpl.html'):
    """ This view will be used to add
        approaches, depending on the POST and GET variables we get."""
    form = forms.ApproachForm(request.POST or None)
    validity = False
    if form.is_valid():
        validity = True
        approach = form.save(commit=False)
        approach.user = request.user
        approach.save()
        return redirect('/approach/'+str(approach.id))
    return render(request, template_name, {'form': form,
                                           'valid': validity,
                                           'form_action': '/approach/' })

def approach_view(request, approach_id, template_name='halfmakery/approach_tpl.html'):
    """ This view will be used to edit
        approaches, depending on the POST and GET variables we get."""
    approach = Approach.objects.get(id=approach_id)
    # approach.user = request.user
    form = forms.ApproachForm(request.POST or None, instance=approach)
    if form.is_valid():
        form.save()

    milestone_form = forms.MilestoneForm(initial={'approach': approach_id})
    milestones = Milestone.objects.all().filter(approach_id=approach_id).order_by('-priority')

    def comment_proc(request, approach, approach_id):
        edit_comment_id = request.GET.get('comment', False)
        if edit_comment_id: edit_comment_id = int(edit_comment_id);
        comments = Comment.objects.all().filter(approach_id=approach_id, milestone_id=None, task_id=None, attempt_id=None)
        comment_editing_form = forms.CommentForm(request.POST or None, initial={'approach': approach})
        if comment_editing_form.is_valid():
            comment_editing_form.save()
        for comment in comments:
            if comment.id == edit_comment_id:
                comment_editing_form = forms.CommentForm(instance=comment)
        return comments, edit_comment_id, comment_editing_form

    comments, edit_comment_id, comment_editing_form = comment_proc(request, approach, approach_id)

    # / Comments
    return render(request, template_name, {'form': form,
                                           'milestones': milestones,
                                           'milestone_form': milestone_form,
                                           'milestones_limit_reached': milestones.count() >= MAX_MILESTONES_COUNT,
                                           'req': request,
                                           'form_action': '/approach/'+str(approach_id),
                                           'comments': comments,
                                           'edit_comment_id': edit_comment_id,
                                           'comment_editing_form': comment_editing_form})

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
                milestone = form.save(commit=False)
                milestone.user = request.user
                milestone.save()
        else:
            """MAX_MILESTONES_COUNT reached."""
            pass

    # Create Comment
    if action == 'comment':
        form = forms.CommentForm(request.POST or None)
        if form.is_valid():
            form.save()

    return redirect('/approach/%s' % approach_id)


def milestone_action(request, approach_id, milestone, milestone_id, action, template_name='halfmakery/approach_tpl.html'):
    """ Delete a Milestone. """

    if action == 'delete':
        milestone = Milestone.objects.get(id=milestone_id)
        milestone.delete()
        return redirect('/approach/'+str(approach_id))

    if action == 'task':
        form = forms.TaskForm(request.POST or None)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
        return redirect('/approach/%s/milestone/%s' % (approach_id, milestone_id))

    # Create Comment
    if action == 'comment':
        form = forms.CommentForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/approach/%s/milestone/%s' % (approach_id, milestone_id))

    return redirect('/approach/%s' % approach_id)

def milestone_view(request, approach_id, milestone, milestone_id, template_name='halfmakery/milestone_tpl.html'):
    milestone = Milestone.objects.get(id=milestone_id)
    form = forms.MilestoneForm(request.POST or None, instance=milestone)
    if form.is_valid():
        form.save()

    task_form = forms.TaskForm(initial={'milestone': milestone_id})
    tasks = Task.objects.all().filter(milestone_id=milestone_id).order_by('-priority')

    def comment_proc(request, approach_id, milestone, milestone_id):
        edit_comment_id = request.GET.get('comment', False)
        if edit_comment_id: edit_comment_id = int(edit_comment_id);
        comments = Comment.objects.all().filter(approach_id=approach_id, milestone_id=milestone_id, task_id=None, attempt_id=None)
        approach = Approach.objects.get(id=approach_id)
        comment_editing_form = forms.CommentForm(request.POST or None, initial={'approach': approach, 'milestone': milestone})
        if comment_editing_form.is_valid():
            comment_editing_form.save()
        for comment in comments:
            if comment.id == edit_comment_id:
                comment_editing_form = forms.CommentForm(instance=comment)
        return comments, edit_comment_id, comment_editing_form

    comments, edit_comment_id, comment_editing_form = comment_proc(request, approach_id, milestone, milestone_id)
    
    return render(request, template_name, {'form': form,
                                           'tasks': tasks,
                                           'task_form': task_form,
                                           'return_link': '/approach/%s' % (approach_id,),
                                           'form_action': '/approach/%s/milestone/%s' % (approach_id, milestone_id),
                                           'comments': comments,
                                           'edit_comment_id': edit_comment_id,
                                           'comment_editing_form': comment_editing_form})


def task_action(request, approach_id, milestone, milestone_id, task, task_id, action, template_name='halfmakery/milestone_tpl.html'):

    if action == 'delete':
        task = Task.objects.get(id=task_id)
        task.delete()

    if action == 'attempt':
        form = forms.AttemptForm(request.POST or None)
        if form.is_valid():
            attempt = form.save(commit=False)
            attempt.user = request.user
            attempt.save()
        return redirect('/approach/%s/milestone/%s/task/%s' % (approach_id, milestone_id, task_id))

    if action == 'comment':
        form = forms.CommentForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('/approach/%s/milestone/%s/task/%s' % (approach_id, milestone_id, task_id))
        else:
            return redirect('/test')
    
    return redirect('/approach/%s/milestone/%s' % (approach_id, milestone_id))

def test(request, template_name='halfmakery/test_tpl.html'):
    return render(request, template_name, {'req': request})

def task_view(request, approach_id, milestone, milestone_id, task, task_id, template_name='halfmakery/task_tpl.html'):
    
    task = Task.objects.get(id=task_id)
    form = forms.TaskForm(request.POST or None, instance=task)

    if form.is_valid():
        form.save()

    attempt_form = forms.AttemptForm(initial={'task': task_id})
    attempts = Attempt.objects.all().filter(task_id=task_id)

    def comment_proc(request, approach_id, milestone, milestone_id, task, task_id):
        edit_comment_id = request.GET.get('comment', False)
        if edit_comment_id: edit_comment_id = int(edit_comment_id);
        comments = Comment.objects.all().filter(approach_id=approach_id, milestone_id=milestone_id, task_id=task_id, attempt_id=None)
        approach = Approach.objects.get(id=approach_id)
        comment_editing_form = forms.CommentForm(request.POST or None, initial={'approach': approach, 'milestone': milestone_id, 'task': task})
        if comment_editing_form.is_valid():
            comment_editing_form.save()
        for comment in comments:
            if comment.id == edit_comment_id:
                comment_editing_form = forms.CommentForm(instance=comment)
        return comments, edit_comment_id, comment_editing_form

    comments, edit_comment_id, comment_editing_form = comment_proc(request, approach_id, milestone, milestone_id, task, task_id)
 
    return render(request, template_name, {'form': form,
                                           'attempt_form': attempt_form,
                                           'attempts': attempts,
                                           'form_action': '/approach/%s/milestone/%s/task/%s' % (approach_id, milestone_id, task_id),
                                           'return_link': '/approach/%s/milestone/%s' % (approach_id, milestone_id),
                                           'comments': comments,
                                           'edit_comment_id': edit_comment_id,
                                           'comment_editing_form': comment_editing_form})
    

def attempt_action(request, approach_id, milestone, milestone_id, task, task_id, attempt, attempt_id, action, template_name='halfmakery/task_tpl.html'):

    if action == 'comment':
        form = forms.CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect('/approach/%s/milestone/%s/task/%s/attempt/%s' % (approach_id, milestone_id, task_id, attempt_id))
        else:
            return redirect('/test')
    
    return redirect('/approach/%s/milestone/%s/task/%s' % (approach_id, milestone_id, task_id))


def attempt_view(request, approach_id, milestone, milestone_id, task, task_id, attempt, attempt_id, template_name='halfmakery/attempt_tpl.html'):
    attempt = Attempt.objects.get(id=attempt_id)
    form = forms.AttemptFormFull(request.POST or None, instance=attempt)
    
    if request.POST.get('delete', False) == 'TRUE':
        attempt.delete()
        return redirect('/approach/%s/milestone/%s/task/%s' % (approach_id, milestone_id, task_id))

    elif form.is_valid():
        form.save()

    def comment_proc(request, approach_id, milestone, milestone_id, task, task_id, attempt, attempt_id):
        edit_comment_id = request.GET.get('comment', False)
        if edit_comment_id: edit_comment_id = int(edit_comment_id);
        comments = Comment.objects.all().filter(approach_id=approach_id, milestone_id=milestone_id, task_id=task_id, attempt_id=attempt_id)
        approach = Approach.objects.get(id=approach_id)
        comment_editing_form = forms.CommentForm(request.POST or None, initial={'approach': approach, 'milestone': milestone_id, 'task': task_id, 'attempt': attempt})
        if comment_editing_form.is_valid():
            comment_editing_form.save()
        for comment in comments:
            if comment.id == edit_comment_id:
                comment_editing_form = forms.CommentForm(instance=comment)
        return comments, edit_comment_id, comment_editing_form

    comments, edit_comment_id, comment_editing_form = comment_proc(request, approach_id, milestone, milestone_id, task, task_id, attempt, attempt_id)

    return render(request, template_name, {'form': form,
                                           'form_action': '/approach/%s/milestone/%s/task/%s/attempt/%s' % (approach_id, milestone_id, task_id, attempt_id),
                                           'return_link': '/approach/%s/milestone/%s/task/%s' % (approach_id, milestone_id, task_id),
                                           'comments': comments,
                                           'edit_comment_id': edit_comment_id,
                                           'comment_editing_form': comment_editing_form})

def user(request, user_id, template_name='halfmakery/user_tpl.html'):
    addresses = Address.objects.all().filter(user_id=user_id)
    form = forms.AddressForm(request.POST or None, initial={'user': user_id})
    if form.is_valid():
        form.save()

    return render(request, template_name, {'addresses': addresses,
                                           'form': form,
                                           'form_action': '/user/%s' % user_id})
