from django.views import View
from django.http.response import HttpResponse, JsonResponse

from django.views.decorators.csrf import csrf_exempt

import json


class APIView(View):
    CODE_SUCCESS = 200
    TEXT_SUCCESS = 'SUCCESS',
    CODE_ERROR_CLIENT = 400
    TEXT_ERROR_CLIENT = 'CLIENT_ERROR'
    CODE_ERROR_SERVER = 500
    TEXT_ERROR_SERVER = 'SERVER_ERROR'

    # TODO: ...

    @csrf_exempt
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_json(self):
        try:
            return json.loads(self.request.body.decode())
        except BaseException as e:
            return {}

    def response(self, result=None, code=200, text='SUCCESS'):
        # return HttpResponse(json.dumps({
        #     'code': code, 'text': text, 'result': result
        # }))
        return JsonResponse({
            'code': code, 'text': text, 'result': result
        })