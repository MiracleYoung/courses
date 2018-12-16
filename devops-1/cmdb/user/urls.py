from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index_v2, name='user'),
    url(r'^login/$', views.login, name='login'),
    url(r'^users/$', views.users, name='users'),
]