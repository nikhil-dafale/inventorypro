from django.conf.urls import url
from .views import *

urlpatterns=[

    url(r'^$',index,name='index'),
    url(r'^metals$',display_metals,name='display_metals'),
    url(r'^plastics$',display_plastics,name='display_plastics'),
    url(r'^composites$',display_composites,name='display_composites'),

    url(r'^add_metals$',add_metals,name='add_metals'),
    url(r'^add_plastics$',add_plastics,name='add_plastics'),
    url(r'^add_composites$',add_composites,name='add_composites'),

    url(r'^metals/edit_item/(?P<pk>\d+)$', edit_metals,name='edit_metals'),
    url(r'^plastics/edit_item/(?P<pk>\d+)$', edit_plastics,name='edit_plastics'),
    url(r'^composites/edit_item/(?P<pk>\d+)$', edit_composites,name='edit_composites'),

    url(r'^metals/delete/(?P<pk>\d+)$', delete_metals,name='delete_metals'),
    url(r'^plastics/delete/(?P<pk>\d+)$', delete_plastics,name='delete_plastics'),
    url(r'^composites/delete/(?P<pk>\d+)$', delete_composites,name='delete_composites'),


]