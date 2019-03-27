import random
import time
from django.contrib.auth.handlers.modwsgi import check_password
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse
from bj.models import Users


def regist(request):
    if request.method == "GET":
        return render(request, 'user/register.html')
    elif request.method == "POST":
        #注册
        name = request.POST.get("username")
        password = request.POST.get("password")
        #对密码加密
        password = make_password(password)
        Users.objects.create(u_name=name, u_password=password)
        return HttpResponseRedirect("user/login.html/")


def login(request):
    if request.method == 'GET':
        return render(request, 'user/login.html')

    if request.method == 'POST':
        # 如果登录成功，绑定参数到cookie中，set_cookie
        name = request.POST.get('name')
        password = request.POST.get('password')
        # 查询用户是否在数据库中
        if Users.objects.filter(u_name=name).exists():
            user = Users.objects.get(u_name=name)
            if check_password(password, user.u_password):
                # ticket = 'agdoajbfjad'
                ticket = ''
                for i in range(15):
                    s = 'abcdefghijklmnopqrstuvwxyz'
                    # 获取随机的字符串
                    ticket += random.choice(s)
                now_time = int(time.time())
                ticket = 'TK' + ticket + str(now_time)
                # 绑定令牌到cookie里面
                # response = HttpResponse()
                response = HttpResponseRedirect('/stu/index/')
                # max_age 存活时间(秒)
                response.set_cookie('ticket', ticket, max_age=10000)
                # 存在服务端
                user.u_ticket = ticket
                user.save()  # 保存
                return response
            else:
                # return HttpResponse('用户密码错误')
                return render(request, 'user/login.html', {'password': '用户密码错误'})
        else:
            # return HttpResponse('用户不存在')
            return render(request, 'user/login.html', {'name': '用户不存在'})

def logout(request):
    if request.method == 'GET':
        # response = HttpResponse()
        response = HttpResponseRedirect('/user/login/')
        response.delete_cookie('ticket')
        return response