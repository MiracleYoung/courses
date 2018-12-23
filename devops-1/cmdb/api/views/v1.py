import time

from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.views import View

from django.views.decorators.csrf import csrf_exempt

from .base import APIView
from api.models import Client, Resource


# Create your views here.

def test(request, name, id):
    if request.method == 'GET':
        return HttpResponse('test func')


def test_redirect(request):
    return redirect('api:test_func')


class TestView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('test class get')

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    @csrf_exempt
    def post(self, request, *args, **kwargs):
        return HttpResponse('test_class post')


class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        _uuid = kwargs.get('uuid')
        _json_body = self.get_json()
        _created, _client = Client.register(_uuid, **_json_body)
        print(_created, _client)

        return self.response({'created': _created, 'client': _client.as_dict()})


class HeartbeatView(APIView):
    def post(self, request, *args, **kwargs):
        _uuid = kwargs.get('uuid')
        Client.heartbeat(_uuid)
        return self.response(time.time())


class ResourceView(APIView):
    def post(self, request, *args, **kwargs):
        _uuid = kwargs.get('uuid')
        _json_body = self.get_json()
        _resource = Resource.create(_uuid, **_json_body)
        return self.response(_resource.as_dict())

# GET:url?k1=v1&k2=v2
# POST: url: dict
