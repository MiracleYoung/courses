

import time

from django.shortcuts import render, redirect
from django.http import HttpResponse


from user.models import User

# /user/index
def index(request):
    html = '''
    <form>
        <input type='text' placeholder='用户名' > <br>
        <input type='password' placeholder='密码' > <br>
        <input type='submit' value='登录'> 
    </form>
    
    '''
    return HttpResponse(html)

def index_v2(request):
    # user 下面创建了一个templates 目录，
    # 下面创建了一个user 目录，
    # 下面创建了一个login.html文件
    print(request.GET)
    print(request.POST)

    print(request.GET.get('name'))

    context = {
        'name': 'miracle',
    }
    return render(request, 'user/login.html', context)


def login(request):
    print(request.GET, request.POST)
    name = request.GET.get('name', '')
    password = request.GET.get('password', '')
    user = User.login(name, password)
    if user:
        return redirect('user:users')
    else:
        context = {}
        context['name'] = name
        context['errors'] = ['用户名或密码错误']
        return render(request, 'user/login.html', context)


def users(request):
    context = {
        # 获取数据库
        'data': User.objects.all()
    }
    return render(request, 'user/users.html', context)