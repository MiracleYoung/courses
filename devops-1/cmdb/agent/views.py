from django.shortcuts import render
from django.views import View
from django.views.generic.list import ListView

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.core.paginator import Paginator

import math

from api.models import Client, Resource
from agent.forms import ClientModifyForm

import json


class ClientListView_v1(View):
    def get(self, request, *args, **kwargs):
        context = {'object_list': Client.objects.all()}
        return render(request, 'agent/list.html', context)


class ClientListView(ListView):
    model = Client
    template_name = 'agent/list_2.html'
    # 每一页显示多少条
    paginate_by = 10

    # def get_context_data(self, *, object_list=None, **kwargs):
    #     page_size = 5
    #     _queryset = super().get_queryset()
    #     # 显示第几页
    #     _page = int(self.request.GET.get('page', 1))
    #     _paginator_object = Paginator(_queryset, page_size)
    #     _page_object = _paginator_object.page(_page)
    #     _context = super().get_context_data(**kwargs)
    #     _context['object_list'] = _queryset[(_page - 1) * page_size:page_size * _page]
    #     _context['total_page'] = math.ceil(_queryset.count() / page_size)
    #     _context['page'] = _page
    #     _context['page_object'] = _page_object
    #
    #     return _context


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


class ClientDeleteView(View):
    # TODO
    # 正常删除
    # 需要做reverse => list.html
    pass


class ClientListAjaxView(View):
    def get(self, request, *args, **kwargs):
        clients = Client.objects.all()
        data = [client.as_dict() for client in clients]
        return JsonResponse({'data': data})


class ResourceListView(View):
    def get(self, request, *args, **kwargs):
        uuid = request.GET.get('uuid', '')
        resources = Resource.objects.filter(uuid=uuid).order_by('-time')[:180]
        result = [resource.as_dict() for resource in resources]
        return JsonResponse({'code': 200, 'text': 'success', 'result': result, 'errors': {}})
