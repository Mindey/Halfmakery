from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
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

    url(r'^chaining/', include('smart_selects.urls')),
    # url(r'^openshift/', include('openshift.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
