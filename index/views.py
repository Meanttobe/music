from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import *


def indexView(request):
    # 判断是否已经登录
    username = request.user.username
    # 热搜歌曲
    search_song = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:20]
    # 热门歌曲
    play_hot_song = Dynamic.objects.select_related('song').order_by('-dynamic_plays').all()[:20]
    # 新歌推荐
    daily_recommendation = Audio.objects.order_by('-song_release').all()[:6]
    list = []
    for i in search_song:
        mp ={}
        mp['id'] = i.song.id
        mp['song_name'] = i.song.song_name
        mp['singer'] = i.song.singer
        mp['times'] = i.dynamic_search
        mp['song_image'] = i.song.song_image
        list.append(mp)
    page = request.GET.get('page')
    paginator = Paginator(list, 6)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'index.html', locals())


# 自定义404和500的错误页面
def page_not_found(request):
    return render(request, 'error404.html', status=404)
# Create your views here.
