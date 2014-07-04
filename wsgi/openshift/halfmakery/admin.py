from django.contrib import admin
from halfmakery.models import Category, Subcategory, Idea, IdeaLink, Approach, Milestone, Task, TaskLink, Page, Currency, PageComment, MilestoneVote, TaskVote

admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(Idea)
admin.site.register(IdeaLink)
admin.site.register(Approach)
admin.site.register(Milestone)
admin.site.register(Task)
admin.site.register(TaskLink)
admin.site.register(Page)
admin.site.register(Currency)
admin.site.register(PageComment)
admin.site.register(MilestoneVote)
admin.site.register(TaskVote)
