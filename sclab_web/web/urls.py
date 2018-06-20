from django.conf.urls import url
from . import views
from django.urls import include, path

urlpatterns = [
    path('', views.index, name='index'),
    path('/professor', views.professor, name='professor'),
    path('/members', views.members, name='members'),
    path('/news', views.news, name='news'),
    path('/publication', views.publication, name='publication'),
    path('/project', views.project, name='project'),
]
