from django.shortcuts import render, redirect
from index.models import *
from user.models import *
from .form import MyUserCreationForm
from django.db.models import Q
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os

# 用户注册与登录
def loginView(request):
    username = request.user.username
    user = MyUserCreationForm()
    # 表单提交
    if request.method == 'POST':
        # 判断表单提交是用户登录还是用户注册
        # 用户登录
        if request.POST.get('loginUser', ''):
            gg = False
            loginUser = request.POST.get('loginUser', '')
            password = request.POST.get('password', '')
            if MyUser.objects.filter(Q(mobile=loginUser) | Q(username=loginUser)):
                user = MyUser.objects.filter(Q(mobile=loginUser) | Q(username=loginUser)).first()
                if check_password(password, user.password):
                    login(request, user)
                    return redirect('/user/home/1.html')
                else:
                    tips = '密码错误'
            else:
                tips = '用户不存在'
        # 用户注册
        else:
            user = MyUserCreationForm(request.POST)
            if user.is_valid():
                user.save()
                tips = '注册成功'
            else:
                if user.errors.get('username',''):
                    tips = user.errors.get('username')
                elif user.errors.get('mobile',''):
                    tips = user.errors.get('mobile')
                elif user.errors.get('password1'):
                    tips = user.errors.get('password1')
                elif user.errors.get('password2'):
                    tips = user.errors.get('password2')
                else:
                    tips = user.errors
    return render(request, 'login.html', locals())

# 用户中心
# 设置用户登录限制
@login_required(login_url='/user/login')
def homeView(request, page):
    username = request.user.username
    if request.method == 'GET':
        # 热搜歌曲
        search_song = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:4]
        # 分页功能
        if "delete_tips" in request.session:
            tips = request.session['delete_tips']
            del request.session['delete_tips']
        song_info = Audio.objects.filter(upload_user=username)
        page = request.GET.get('page')
        paginator = Paginator(song_info, 6)
        try:
            contacts = paginator.page(page)
        except PageNotAnInteger:
            contacts = paginator.page(1)
        except EmptyPage:
            contacts = paginator.page(paginator.num_pages)
        return render(request, 'home.html', locals())
    id_info = request.POST.get('id_info')
    file_info = Audio.objects.get(id = int(id_info))
    try:
        os.remove('media/' + str(file_info.song_file))
        os.remove('media/' + str(file_info.song_image))
        os.remove('media/' + str(file_info.song_lrc))
        info = Audio.objects.filter(id=int(id_info)).delete()
        delete_tips = "删除成功"
        print("success")
    except:
        delete_tips = '删除失败'
        print("wrong")
    request.session['delete_tips'] = delete_tips
    return redirect('1.html')

# 退出登录
def logoutView(request):
    username = request.user.username
    logout(request)
    return redirect('/')