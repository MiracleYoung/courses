from django.conf.urls import url
from django.urls import reverse_lazy

from django.views.generic.base import RedirectView, TemplateView

from .views import v1

urlpatterns = [
    url(r'^v1/test_func/(?P<id>\d+)/(?P<name>\w+)/$', v1.test, name='test_func'),
    url(r'^v1/test_class/$', v1.TestView.as_view(), name='test_class'),
    url(r'^v1/test_func_redirect/$', v1.test_redirect, name='test_func_redirect'),
    url(r'^v1/test_class_redirect/$', RedirectView.as_view(url=reverse_lazy('api:test_func')),
        name='test_class_redirect'),
    url(r'^$', TemplateView.as_view(template_name='user/login.html'), name='user'),
    url(r'^v1/register/(?P<uuid>\w{32,64})/$', v1.RegisterView.as_view(), name='register'),
    url(r'^v1/heartbeat/(?P<uuid>\w{32,64})/$', v1.HeartbeatView.as_view(), name='heartbeat'),
    url(r'^v1/resource/(?P<uuid>\w{32,64})/$', v1.ResourceView.as_view(), name='resource'),
]
