from django.conf.urls.defaults import url
from django.conf.urls.defaults import patterns

urlpatterns = patterns(
    'gstudio.views.iconwrite',
    
    url(r'^$', 'Interface'),
    url(r'^subject/$', 'Subject',name='Subject'),

    

    #url(r'^verb/$', 'Verb',name='Verb'),
    #url(r'^object/$', 'Object', name='Object'),    
    )
