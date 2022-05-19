from django.shortcuts import render,redirect
from django.http import StreamingHttpResponse
from index.models import *


# 歌曲播放页面
def playView(request, song_id):
    play_list = request.session.get('play_list', [])
    s_id = request.GET.get('s_id')
    if s_id:
        for i in play_list:
            if s_id and int(s_id) == i['song_id']:
                play_list.remove(i)
        request.session['play_list'] = play_list
        return redirect(str(song_id) + '.html')
    username = request.user.username
    # 热搜歌曲
    search_song = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:6]
    # 歌曲信息
    song_info = Audio.objects.get(id=int(song_id))
    cate = Audio.objects.get(id=int(song_id)).category.all()
    all_cate = str(cate[0])
    for i in cate:
        if i == cate[0]:
            continue
        all_cate = str(all_cate) + '、' + str(i)
    # 播放列表
    song_exist = False
    if play_list:
        for i in play_list:
            if int(song_id) == i['song_id']:
                song_exist = True
    if song_exist == False:
        play_list.append({'song_id': int(song_id), 'song_singer': song_info.singer, 'song_name': song_info.song_name,
                          'song_cate': all_cate})
    request.session['play_list'] = play_list
    # 歌词
    f = open('media/' + str(song_info.song_lrc), 'r', encoding='utf-8')
    song_lyrics = f.read()
    f.close()

    dynamic_info = Dynamic.objects.filter(song_id=int(song_id)).first()
    # 判断歌曲动态信息是否存在，存在就在原来基础上加1
    if dynamic_info:
        dynamic_info.dynamic_plays += 1
        dynamic_info.save()
    # 动态信息不存在则创建新的动态信息
    else:
        dynamic_info = Dynamic(dynamic_plays=1, dynamic_search=0, song_id=song_id)
        dynamic_info.save()
    return render(request, 'play.html', locals())
