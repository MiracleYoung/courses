from django.conf.urls import url
from agent import views

urlpatterns = [
    url(r'^agent/list/$', views.ClientListView.as_view(), name='agent_list'),
    url(r'^agent/modify/$', views.ClientModifyView.as_view(), name='agent_modify'),
    url(r'^agent/resource/$', views.ResourceListView.as_view(), name='agent_resource'),
]
