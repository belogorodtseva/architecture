from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^projects/', views.projects, name='projects'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^services/', views.services, name='services'),
]
