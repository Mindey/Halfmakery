from django import forms
from django.utils.translation import ugettext as _
from halfmakery.models import Approach, Milestone, Task, Attempt, Address, Comment, Category, Subcategory, Idea

class ApproachForm(forms.ModelForm):
    class Meta:
        model = Approach
        exclude = ['user']
    def __init__(self, *args, **kwargs):
        super(ApproachForm, self).__init__(*args, **kwargs)
        from django.utils.safestring import mark_safe
        self.fields['category'].label = mark_safe('<span id="swap"><span id="old_idea">Categories</span><span id="new_idea"><a href="/categories/" target="_blank">Categories</a></span></span>')
        self.fields['subcategory'].label = mark_safe('<span id="swap"><span id="old_idea">Subcategories</span><span id="new_idea"><a href="/subcategories/" target="_blank">Subcategories</a></span></span>')
        self.fields['idea'].label = mark_safe('<span id="swap"><span id="old_idea">Idea</span><span id="new_idea"><a href="/idea/" target="_blank">Add New</a></span></span>')

class MilestoneForm(forms.ModelForm):
    class Meta:
        model = Milestone
        exclude = ['user']
        widgets = {'approach': forms.HiddenInput(),
                   'priority': forms.HiddenInput(),
                   'achieved': forms.HiddenInput(),
                   'details': forms.Textarea(attrs={'rows':3}) }

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['user']
        widgets = {'milestone': forms.HiddenInput(),
                   'priority': forms.HiddenInput(),
                   'complete': forms.HiddenInput(),
                   'description': forms.Textarea(attrs={'rows':3}) }

class AttemptForm(forms.ModelForm):
    class Meta:
        exclude = ['user']
        model = Attempt
        widgets = {'task': forms.HiddenInput(),
                   'contents': forms.HiddenInput()}

class AttemptFormFull(forms.ModelForm):
    class Meta:
        model = Attempt
        exclude = ['user']
        widgets = {'task': forms.HiddenInput(),
                   'contents': forms.Textarea(attrs={'rows':30, 'cols': 50}) }

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ['user']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'recipients', 'satoshis']
        widgets = {'approach': forms.HiddenInput(),
                   'milestone': forms.HiddenInput(),
                   'task': forms.HiddenInput(),
                   'attempt': forms.HiddenInput(),
                   'text': forms.Textarea(attrs={'rows':3}) }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
