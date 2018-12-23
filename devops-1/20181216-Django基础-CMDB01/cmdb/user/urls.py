from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index_v2, name='user'),
    url(r'^login/$', views.login, name='login'),
    url(r'^users/$', views.users, name='users'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^create/$', views.create, name='create'),
    url(r'^save/$', views.save, name='save'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^change_password/$', views.change_password, name='change_password'),
]