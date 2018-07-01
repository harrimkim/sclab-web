from django.conf.urls import url
from . import views
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('professor', views.professor, name='professor'),
    path('members', views.members, name='members'),
    path('news', views.news, name='news'),
    path('news/<int:id>', views.posts, name="posts"),
    path('publication', views.publication, name='publication'),
    path('project', views.project, name='project'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
