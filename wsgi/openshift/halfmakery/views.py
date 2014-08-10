# Create your views here.

from halfmakery import forms
from django.shortcuts import render, redirect
from halfmakery.models import Approach, Milestone, Task, Attempt, Address, Comment, Category, Subcategory, Idea
from django.contrib.auth.models import User

# Interaction with Blockchains.

def get_recipients_and_total(txid, currency='BTC'):
    import requests, json
    r = requests.get('https://blockchain.info/tx-index/%s?format=json' % txid)
    c = json.loads(r.content)
    addrs = [d['addr'] for d in c['out'] if 'addr' in d]
    addresses = Address.objects.all().filter(address__in=addrs)
    recipients = []
    satoshis = 0
    for address in addresses:
        recipients.append(address.user.id)
        satoshis += int(c['out'][addrs.index(address.address)]['value'])
    return (recipients, satoshis)

# Limit of most people's short term memory
MAX_MILESTONES_COUNT = False

def approach_add(request, template_name='halfmakery/add_approach_tpl.html'):
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
    milestones = Milestone.objects.all().filter(approach_id=approach_id).order_by('priority')

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
        if request.GET.get('target',False) == 'content':
            comment_editing_form = forms.CommentForm(None, initial={'approach': approach})
        comment_editing_form.fields['txid'].widget.attrs['placeholder'] = 'Optional.'
        return comments, edit_comment_id, comment_editing_form

    comments, edit_comment_id, comment_editing_form = comment_proc(request, approach, approach_id)

    milestone_list = []
    for item in milestones:
        task_count = Task.objects.all().filter(milestone=item).count()
        milestone_list.append((item, task_count))

    # / Comments
    return render(request, template_name, {'form': form,
                                           'approach': approach,
                                           'milestones': milestone_list,
                                           'milestone_form': milestone_form,
                                           'milestones_limit_reached': (milestones.count() >= MAX_MILESTONES_COUNT) and (MAX_MILESTONES_COUNT > 0),
                                           'req': request,
                                           'form_action': '/approach/'+str(approach_id),
                                           'comments': comments,
                                           'edit_comment_id': edit_comment_id,
                                           'comment_editing_form': comment_editing_form,
                                           'level_id': approach_id,
                                           'info': request.GET.get('info',False)})

def approach_action(request, approach_id, action):
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
        if (Milestone.objects.all().filter(approach_id=approach_id).count() < MAX_MILESTONES_COUNT) or (MAX_MILESTONES_COUNT == False):
            if form.is_valid():
                milestone = form.save(commit=False)
                milestone.user = request.user
                priorities = [m.priority for m in Milestone.objects.all().filter(approach_id=approach_id)]
                if priorities:
                    milestone.priority = max(priorities) + 1
                else:
                    milestone.priority = 0
                milestone.save()
        else:
            """MAX_MILESTONES_COUNT reached."""
            pass

    # Create Comment
    if action == 'comment':
        form = forms.CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            try:
                recipients, total = get_recipients_and_total(comment.txid)
                __this_txid_is_used__ = Comment.objects.all().filter(txid=comment.txid)
                if not __this_txid_is_used__:
                    comment.satoshis = total
                    comment.save()
                    comment.recipients = recipients
                else:
                    return redirect('/approach/%s?info=used_txid' % approach_id)
            except:
                return redirect('/approach/%s?info=invalid_txid' % approach_id)

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
            comment = form.save(commit=False)
            comment.user = request.user
            try:
                recipients, total = get_recipients_and_total(comment.txid)
                __this_txid_is_used__ = Comment.objects.all().filter(txid=comment.txid)
                if not __this_txid_is_used__:
                    comment.satoshis = total
                    comment.save()
                    comment.recipients = recipients
                    return redirect('/approach/%s/milestone/%s' % (approach_id, milestone_id))
                else:
                    return redirect('/approach/%s/milestone/%s?info=used_txid' % (approach_id, milestone_id))
            except:
                return redirect('/approach/%s/milestone/%s?info=invalid_txid' % (approach_id, milestone_id))

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
        if request.GET.get('target',False) == 'content':
            comment_editing_form = forms.CommentForm(None, initial={'approach': approach})
        comment_editing_form.fields['txid'].widget.attrs['placeholder'] = 'Optional.'
        return comments, edit_comment_id, comment_editing_form

    comments, edit_comment_id, comment_editing_form = comment_proc(request, approach_id, milestone, milestone_id)
    
    task_list = []
    for item in tasks:
        attempt_count = Attempt.objects.all().filter(task=item).count()
        task_list.append((item, attempt_count))

    return render(request, template_name, {'form': form,
                                           'tasks': task_list,
                                           'task_form': task_form,
                                           'return_link': '/approach/%s' % (approach_id,),
                                           'form_action': '/approach/%s/milestone/%s' % (approach_id, milestone_id),
                                           'comments': comments,
                                           'edit_comment_id': edit_comment_id,
                                           'comment_editing_form': comment_editing_form,
                                           'milestone': milestone,
                                           'level_id': milestone_id,
                                           'info': request.GET.get('info',False)})


def task_action(request, approach_id, milestone, milestone_id, task, task_id, action):

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

    # Create Comment
    if action == 'comment':
        form = forms.CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            try:
                recipients, total = get_recipients_and_total(comment.txid)
                __this_txid_is_used__ = Comment.objects.all().filter(txid=comment.txid)
                if not __this_txid_is_used__:
                    comment.satoshis = total
                    comment.save()
                    comment.recipients = recipients
                    return redirect('/approach/%s/milestone/%s/task/%s' % (approach_id, milestone_id, task_id))
                else:
                    return redirect('/approach/%s/milestone/%s/task/%s?info=used_txid' % (approach_id, milestone_id, task_id))
            except:
                return redirect('/approach/%s/milestone/%s/task/%s?info=invalid_txid' % (approach_id, milestone_id, task_id))
    
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
        if request.GET.get('target',False) == 'content':
            comment_editing_form = forms.CommentForm(None, initial={'approach': approach})
        comment_editing_form.fields['txid'].widget.attrs['placeholder'] = 'Optional.'
        return comments, edit_comment_id, comment_editing_form

    comments, edit_comment_id, comment_editing_form = comment_proc(request, approach_id, milestone, milestone_id, task, task_id)
 
    return render(request, template_name, {'form': form,
                                           'attempt_form': attempt_form,
                                           'attempts': attempts,
                                           'form_action': '/approach/%s/milestone/%s/task/%s' % (approach_id, milestone_id, task_id),
                                           'return_link': '/approach/%s/milestone/%s' % (approach_id, milestone_id),
                                           'comments': comments,
                                           'edit_comment_id': edit_comment_id,
                                           'comment_editing_form': comment_editing_form,
                                           'task': task,
                                           'level_id': task_id,
                                           'info': request.GET.get('info',False)})
    

def attempt_action(request, approach_id, milestone, milestone_id, task, task_id, attempt, attempt_id, action):

    # Create Comment
    if action == 'comment':
        form = forms.CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            try:
                recipients, total = get_recipients_and_total(comment.txid)
                __this_txid_is_used__ = Comment.objects.all().filter(txid=comment.txid)
                if not __this_txid_is_used__:
                    comment.satoshis = total
                    comment.save()
                    comment.recipients = recipients
                    return redirect('/approach/%s/milestone/%s/task/%s/attempt/%s' % (approach_id, milestone_id, task_id, attempt_id))
                else:
                    return redirect('/approach/%s/milestone/%s/task/%s/attempt/%s?info=used_txid' % (approach_id, milestone_id, task_id, attempt_id))
            except:
                return redirect('/approach/%s/milestone/%s/task/%s/attempt/%s?info=invalid_txid' % (approach_id, milestone_id, task_id, attempt_id))
    
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
        if request.GET.get('target',False) == 'content':
            comment_editing_form = forms.CommentForm(None, initial={'approach': approach})
        comment_editing_form.fields['txid'].widget.attrs['placeholder'] = 'Optional.'
        return comments, edit_comment_id, comment_editing_form

    comments, edit_comment_id, comment_editing_form = comment_proc(request, approach_id, milestone, milestone_id, task, task_id, attempt, attempt_id)

    return render(request, template_name, {'form': form,
                                           'form_action': '/approach/%s/milestone/%s/task/%s/attempt/%s' % (approach_id, milestone_id, task_id, attempt_id),
                                           'return_link': '/approach/%s/milestone/%s/task/%s' % (approach_id, milestone_id, task_id),
                                           'comments': comments,
                                           'edit_comment_id': edit_comment_id,
                                           'attempt': attempt,
                                           'comment_editing_form': comment_editing_form,
                                           'info': request.GET.get('info',False)})

def user(request, user_id, template_name='halfmakery/user_tpl.html'):
    addresses = Address.objects.all().filter(user_id=user_id)
    form = forms.AddressForm(request.POST or None, initial={'user': user_id})
    if form.is_valid():
        address = form.save(commit=False)
        address.user = request.user
        address.save()

    return render(request, template_name, {'addresses': addresses,
                                           'form': form,
                                           'user_id': int(user_id),
                                           'form_action': '/user/%s' % user_id})

def address_action(request, address_id, action):
    """ This view will be used to delete, and execute actions on Users/Addresses. """

    # Delete Approach
    if action == 'delete':
        address = Address.objects.get(id=address_id)
        address.delete()
        return redirect('/user/%s' % request.user.id)

    return redirect('/user/%s' % request.user.id)


def update_priorities(approach_id, priority_map, object='Milestone'):
    """ Updates priorities for objects. """
    if object == 'Milestone':
        for ix, milestone in enumerate(Milestone.objects.all().filter(approach_id=approach_id)):
            milestone.priority = priority_map[milestone.id]
            milestone.save()
        return 'OK'
    else:
        return False

def update_priority_order(request):
    from django.http import Http404
    if request.is_ajax():
        if request.method == 'POST':
            try:
                level = request.POST['level']
                order = request.POST['order']
            except KeyError:
                raise Http404
    order = order.split('&')
    order = [int(o.replace('todo[]=', '')) for o in order]
    priority_map = dict(zip(order,range(len(order))))
    update_priorities(level, priority_map)
    from django.http import HttpResponse
    return HttpResponse('')


def categories_view(request, template_name='halfmakery/categories_tpl.html'):
    categories = Category.objects.all()
    form = forms.CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, template_name, {'categories': categories,
                                           'form_action': '/categories/',
                                           'form': form})

def category_action(request, category_id, action):
    """ This view will be used to delete, and execute actions on categories. """

    # Delete Category
    if action == 'delete':
        category = Category.objects.get(id=category_id)
        category.delete()
        return redirect('/categories/')

    return redirect('/categories/')

def subcategories_view(request, template_name='halfmakery/subcategories_tpl.html'):
    subcategories = Subcategory.objects.all()
    form = forms.SubcategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
    return render(request, template_name, {'subcategories': subcategories,
                                           'form_action': '/subcategories/',
                                           'form': form})

def subcategory_action(request, subcategory_id, action):
    """ This view will be used to delete, and execute actions on subcategories. """

    # Delete Subcategory
    if action == 'delete':
        subcategory = Subcategory.objects.get(id=subcategory_id)
        subcategory.delete()
        return redirect('/subcategories/')

    return redirect('/subcategories/')

def ideas_view(request, template_name='halfmakery/ideas_tpl.html'):
    ideas = Idea.objects.all().filter(user=request.user).order_by('-id')
    form = forms.IdeaForm(request.POST or None)
    if form.is_valid():
        idea = form.save(commit=False)
        idea.user = request.user

        try:
            recipients, total = get_recipients_and_total(idea.txid)
            # I think, we should let people use the txid which was previously 
            # used for commenting, if it was directed to a staff member.
            __this_txid_was_used_for_idea__ = Idea.objects.all().filter(txid=idea.txid)
            if not __this_txid_was_used_for_idea__:
                for user in User.objects.all().filter(is_staff=True):
                    if user.id in recipients:
                        idea.save()
        except:
            pass

    return render(request, template_name, {'ideas': ideas,
                                           'form_action': '/ideas/',
                                           'form': form })

def idea_action(request, idea_id, action):

    # Delete Idea
    if action == 'delete':
        idea = Idea.objects.get(id=idea_id)
        idea.delete()
        return redirect('/ideas/')

    return redirect('/ideas/')

def staff_view(request, template_name='halfmakery/staff_tpl.html'):
    addresses = Address.objects.all()
    return render(request, template_name, {'addresses': addresses})
