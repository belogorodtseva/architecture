from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^projects/(?P<category>[\w]+)/(?P<pk>[0-9]+)/', views.project, name='project'),
    url(r'^projects/', views.projects, name='projects'),
    url(r'^contact/', views.contact, name='contact'),

    url(r'^ru/$', views.ruindex, name='ruindex'),
    url(r'^ru/projects/(?P<category>[\w]+)/(?P<pk>[0-9]+)/', views.ruproject, name='ruproject'),
    url(r'^ru/projects/', views.ruprojects, name='ruprojects'),
    url(r'^ru/contact/', views.rucontact, name='rucontact'),

    url(r'^en/$', views.enindex, name='enindex'),
    url(r'^en/projects/(?P<category>[\w]+)/(?P<pk>[0-9]+)/', views.enproject, name='enproject'),
    url(r'^en/projects/', views.enprojects, name='enprojects'),
    url(r'^en/contact/', views.encontact, name='encontact'),
]
