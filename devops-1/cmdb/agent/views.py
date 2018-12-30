from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView

from django.http import  JsonResponse
from django.views.decorators.csrf import csrf_exempt

from api.models import Client, Resource
from agent.forms import ClientModifyForm

import json

class ClientListView_v1(View):
    def get(self, request, *args, **kwargs):
        context = {'object_list': Client.objects.all()}
        return render(request, 'agent/list.html', context)


class ClientListView(ListView):
    model = Client
    template_name = 'agent/list.html'


class ClientModifyView(View):

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        form = ClientModifyForm(request.POST)
        if form.is_valid():
            client = Client.objects.get(pk=request.POST.get('id'))
            client.addr = request.POST.get('addr')
            client.application = request.POST.get('application')
            client.user = request.POST.get('user')
            client.remark = request.POST.get('remark')
            client.save()
            return JsonResponse({'code': '200', 'text': 'SUCCESS', 'result': None, 'errors': {}})
        else:
            return JsonResponse({
                'code': '400', 'text': 'error', 'result': None, 'errors': json.loads(form.errors.as_json())
            })


class ResourceListView(View):
    def get(self, request, *args, **kwargs):
        uuid = request.GET.get('uuid', '')
        resources = Resource.objects.filter(uuid=uuid).order_by('-time')[:180]
        result = [resource.as_dict() for resource in resources]
        return JsonResponse({'code': 200, 'text': 'success', 'result': result, 'errors': {}})