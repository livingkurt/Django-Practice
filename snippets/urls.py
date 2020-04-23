from django.conf.urls import url

from . import views

app_name = 'snippets'
urlpatterns = [
    url(r'^$', views.SnippetListView.as_view(), name='index'),

    url(r'^detail/(?P<pk>[0-9]+)/$', 
        views.SnippetDetailView.as_view(), name='detail'),

    url(r'^add/$', views.add, name='add'),
]
