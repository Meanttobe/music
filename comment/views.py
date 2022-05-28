from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.http import Http404
from index.models import *
import time



def commentView(request, song_id):
    username = request.user.username
    search_song = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:20]
    # 点评提交处理
    if request.method == 'POST':
        comment_text = request.POST.get('comment','')
        comment_user = request.user.username if request.user.username else '匿名用户'
        if comment_text:
            comment = Comment()
            comment.comment_text = comment_text
            comment.comment_user = comment_user
            comment.comment_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            comment.song_id = song_id
            comment.save()
        return redirect('/comment/%s.html' %(str(song_id)))

    song_info = Audio.objects.filter(id=song_id).first()
    comment_all = Comment.objects.filter(song_id=song_id).order_by('comment_date')
    song_name = song_info.song_name
    page = request.GET.get('page')
    paginator = Paginator(comment_all, 6)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)
    return render(request, 'comment.html', locals())