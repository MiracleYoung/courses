import time

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import models
from django.utils import timezone

from user.models import User
from . import forms


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
        request.session['user'] = {'name': user.name, 'id': user.id}
        return redirect('user:users')
    else:
        context = {}
        context['name'] = name
        context['errors'] = ['用户名或密码错误']
        return render(request, 'user/login.html', context)


def users(request):
    if request.session.get('user') is None:
        return redirect('user:user')
    context = {
        # 获取数据库
        'data': User.objects.all()
    }
    return render(request, 'user/users.html', context)


def delete(request):
    if request.session.get('user') is None:
        return redirect('user:user')

    uid = request.GET.get('id', -1)
    User.objects.filter(pk=uid).delete()
    return redirect('user:users')


def logout(request):
    request.session.flush()
    return redirect('user:user')


def create(request):
    if request.session.get('user') is None:
        return redirect('user:user')
    return render(request, 'user/create.html')


def save(request):
    print(request.POST)
    if request.session.get('user') is None:
        return redirect('user:user')
    is_valid, errors = valid_save(request.POST)
    if is_valid:
        # 创建用户
        user = User()
        user.name = request.POST.get('name', '').strip()
        user.email = request.POST.get('email', '').strip()
        user.age = request.POST.get('age', '').strip()
        user.telephone = request.POST.get('telephone', '').strip()
        user.set_password(request.POST.get('password', '').strip())
        user.login_time = timezone.now()
        user.save()

        return redirect('user:users')
    else:
        # 返回用户注册界面，并且回显数据，打印错误信息
        context = {}
        context['name'] = request.POST.get('name', '')
        context['errors'] = errors
        context['password'] = request.POST.get('password', '')
        context['password2'] = request.POST.get('password2', '')
        context['email'] = request.POST.get('email', '')
        context['age'] = request.POST.get('age', '')
        context['telephone'] = request.POST.get('telephone', '')
        return render(request, 'user/create.html', context)


def valid_save(params):
    is_valid = True
    errors = {}

    name = params.get('name', '').strip()
    errors['name'] = []
    if not name:
        errors['name'].append('name 不能为空')
        is_valid = False
    # 用户是否存在
    elif User.objects.filter(name=name).count() > 0:
        errors['name'].append(('name已经存在'))
        is_valid = False

    password = params.get('password', '').strip()
    password2 = params.get('password2', '').strip()
    errors['password'] = []
    if not password:
        errors['password'].append('password不能为空')
        is_valid = False
    elif password != password2:
        errors['password'].append('两个password不一致')
        is_valid = False

    age = params.get('age', '').strip()
    errors['age'] = []
    if not age.isdigit():
        errors['age'].append('age必须为整数')
        is_valid = False
    elif int(age) < 0 or int(age) > 80:
        errors['age'].append('age 必须为 0-80 的整数')
        is_valid = False

    return is_valid, errors


def edit(request):
    if request.session.get('user') is None:
        return redirect('user:user')

    uid = request.GET.get('id', -1)
    try:
        user = User.objects.get(id=uid)
        return render(request, 'user/edit.html', user.as_dict())
    except models.ObjectDoesNotExist as e:
        return redirect('user:users')


def modify(request):
    if request.session.get('user') is None:
        return redirect('user:user')
    is_valid, errors = valid_modify(request.POST)
    if is_valid:
        uid = request.POST.get('id', -1)
        user = User.objects.get(id=uid)
        user.name = request.POST.get('name', '').strip()
        user.email = request.POST.get('email', '').strip()
        user.age = request.POST.get('age', '').strip()
        user.telephone = request.POST.get('telephone', '').strip()

        user.save()

        return redirect('user:users')
    else:
        context = {}
        context['name'] = request.POST.get('name', '')
        context['errors'] = errors
        context['id'] = request.POST.get('id', '')
        context['email'] = request.POST.get('email', '')
        context['age'] = request.POST.get('age', '')
        context['telephone'] = request.POST.get('telephone', '')
        return render(request, 'user/edit.html', context)


def valid_modify(params):
    is_valid = True
    errors = {}

    uid = params.get('id', -1)

    name = params.get('name', '').strip()
    errors['name'] = []
    try:
        User.objects.get(id=uid)
    except models.ObjectDoesNotExist as e:
        errors['name'].append('操作用户不存在')
        is_valid = False
    if name is None:
        errors['name'].append(('name不能为空'))
        is_valid = False
    # 用户是否存在
    elif User.objects.filter(name=name).exclude(id=uid).count() > 0:
        errors['name'].append(('name已经存在'))
        is_valid = False

    age = params.get('age', '').strip()
    errors['age'] = []
    if not age.isdigit():
        errors['age'].append('age必须为整数')
        is_valid = False
    elif int(age) < 0 or int(age) > 80:
        errors['age'].append('age 必须为 0-80 的整数')
        is_valid = False

    return is_valid, errors


def change_password(request):
    if request.session.get('user') is None:
        return redirect('user:user')

    print(request.POST)
    form = None
    if request.method == 'GET':
        form = forms.ChangePasswordForm()
    else:
        form = forms.ChangePasswordForm(request.session.get('user'), request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.session.get('user').get('id'))
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            return redirect('user:logout')

    return render(request, 'user/change_password.html', {'form': form})


'''
# 检查用户存在与否
request.session[key] = value (json.dumps())

# 第一次登录后 记录下来
request.session['user'] = {
    'name': user.name # User.object.get(pk=uid)
}
'''
