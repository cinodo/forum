from django.conf.urls import url
from . import views as myapp_views

urlpatterns = [
    url(r'^$', myapp_views.index, name='index'),
    url(r'^topico/(?P<slug>[\w_-]+)/$', myapp_views.topico, name='topico'),
    url(r'^mensagem/(?P<pk>\d+)/$', myapp_views.mensagem, name='mensagem'),
]