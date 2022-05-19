from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from index.models import *


def rankingView(request):
    username = request.user.username
    song_info = Dynamic.objects.select_related('song').order_by('-dynamic_plays').all()
    page = request.GET.get('page')
    paginator = Paginator(song_info, 10)
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts = paginator.page(1)
    except EmptyPage:
        contacts = paginator.page(paginator.num_pages)

    return render(request, 'ranking.html', locals())


