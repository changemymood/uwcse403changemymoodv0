from django.conf.urls import patterns, include, url
from testProgram import storeData, storeData_form, displayData, clearData

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', storeData_form),
    (r'^dbadd/$', storeData),
    (r'^dbdisplay/$', displayData),
    (r'^dbclear/$', clearData),
    # Examples:
    # url(r'^$', 'hellodjango.views.home', name='home'),
    # url(r'^hellodjango/', include('hellodjango.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
