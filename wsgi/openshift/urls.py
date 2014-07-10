from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'openshift.views.home', name='home'),
    url(r'^about/$', 'openshift.views.about', name='about'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^approach/$', 'halfmakery.views.approach_add', name='approach_add'),
    url(r'^approach/(?P<approach_id>\d+)$', 'halfmakery.views.approach_edit', name='approach_edit'),
    url(r'^approach/(?P<approach_id>\d+)/(?P<action>[^/]+)$', 'halfmakery.views.approach_delete', name='approach_delete'),
    url(r'^chaining/', include('smart_selects.urls')),
    # url(r'^openshift/', include('openshift.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
