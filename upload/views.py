import datetime
from django.shortcuts import render,redirect
from .form import SaveAudio
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/user/login')
def upload(request):
    username = request.user.username
    if request.method == 'GET':
        form = SaveAudio()
        return render(request,'upload.html',locals())
    form = SaveAudio(request.POST, request.FILES)
    print(form)
    if form.is_valid():
        tips = "上传成功"
        form.save()
        return render(request,'upload.html',locals())
    tips = "上传失败"
    return render(request, 'upload.html', locals())





