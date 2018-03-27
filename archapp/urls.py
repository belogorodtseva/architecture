from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^archprojects/', views.archprojects, name='archprojects'),
    url(r'^designprojects/', views.designprojects, name='designprojects'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^services/', views.services, name='services'),

    url(r'^ru/$', views.ruindex, name='ruindex'),
    url(r'^ru/archprojects/', views.ruarchprojects, name='ruarchprojects'),
    url(r'^ru/designprojects/', views.rudesignprojects, name='rudesignprojects'),
    url(r'^ru/contact/', views.rucontact, name='rucontact'),
    url(r'^ru/services/', views.ruservices, name='ruservices'),

    url(r'^en/$', views.enindex, name='enindex'),
    url(r'^en/archprojects/', views.enarchprojects, name='enarchprojects'),
    url(r'^en/designprojects/', views.endesignprojects, name='endesignprojects'),
    url(r'^en/contact/', views.encontact, name='encontact'),
    url(r'^en/services/', views.enservices, name='enservices'),
]
