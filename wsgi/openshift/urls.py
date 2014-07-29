from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^test$', 'halfmakery.views.test', name='test'),
    # Examples:
    url(r'^$', 'openshift.views.home', name='home'),
    url(r'^about/$', 'openshift.views.about', name='about'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    # Approach
    url(r'^approach/$', 'halfmakery.views.approach_add', name='approach_add'),
    url(r'^approach/(?P<approach_id>\d+)$', 'halfmakery.views.approach_view', name='approach_view'),
    url(r'^approach/(?P<approach_id>\d+)/(?P<action>[^/]+)$', 'halfmakery.views.approach_action', name='approach_action'),
    # Milestone
    url(r'^approach/(?P<approach_id>\d+)/(?P<milestone>[^/]+)/(?P<milestone_id>\d+)/(?P<action>[^/]+)$', 'halfmakery.views.milestone_action', name='milestone_action'),
    url(r'^approach/(?P<approach_id>\d+)/(?P<milestone>[^/]+)/(?P<milestone_id>\d+)$', 'halfmakery.views.milestone_view', name='milestone_view'),
    # Task
    url(r'^approach/(?P<approach_id>\d+)/(?P<milestone>[^/]+)/(?P<milestone_id>\d+)/(?P<task>[^/]+)/(?P<task_id>\d+)/(?P<action>[^/]+)$', 'halfmakery.views.task_action', name='task_action'),
    url(r'^approach/(?P<approach_id>\d+)/(?P<milestone>[^/]+)/(?P<milestone_id>\d+)/(?P<task>[^/]+)/(?P<task_id>\d+)$', 'halfmakery.views.task_view', name='task_view'),
    # Attempt
    url(r'^approach/(?P<approach_id>\d+)/(?P<milestone>[^/]+)/(?P<milestone_id>\d+)/(?P<task>[^/]+)/(?P<task_id>\d+)/(?P<attempt>[^/]+)/(?P<attempt_id>\d+)$', 'halfmakery.views.attempt_view', name='attempt_view'),
    url(r'^approach/(?P<approach_id>\d+)/(?P<milestone>[^/]+)/(?P<milestone_id>\d+)/(?P<task>[^/]+)/(?P<task_id>\d+)/(?P<attempt>[^/]+)/(?P<attempt_id>\d+)/(?P<action>[^/]+)$', 'halfmakery.views.attempt_action', name='attempt_action'),
    # Address (BTC/LTC/etc.)
    url(r'^user/(?P<user_id>\d+)$', 'halfmakery.views.user', name='user'),
    # Priority (Ajax):
    url(r'^ajax/list/update/handler/$', 'halfmakery.views.update_priority_order', name='update_priority_order'),
    # Categories, Subcategories, Ideas
    url(r'^categories/$', 'halfmakery.views.categories_view', name='categories_view'),
    url(r'^subcategories/$', 'halfmakery.views.subcategories_view', name='subcategories_view'),
    url(r'^idea/$', 'halfmakery.views.idea_add', name='idea_add'),
    url(r'^category/(?P<category_id>\d+)/(?P<action>[^/]+)$', 'halfmakery.views.category_action', name='category_action'),
    url(r'^subcategory/(?P<subcategory_id>\d+)/(?P<action>[^/]+)$', 'halfmakery.views.subcategory_action', name='subcategory_action'),
    # For django-smart-selects
    url(r'^chaining/', include('smart_selects.urls')),
    
    # url(r'^openshift/', include('openshift.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
