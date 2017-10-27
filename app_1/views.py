import os
from django.shortcuts import render
from django.http import HttpResponse
from .models import People
from django.utils import timezone
from .forms import AddForm
# Create your views here.


def dayin(request):
    name = request.POST['name']
    email = request.POST['email']
    comment = request.POST['comment']
    p = People(name=str(name), email=str(email), suggestion=str(comment), date=timezone.now())
    p.save()
    return HttpResponse('ok')


def index(request):
    return render(request, 'index.html')


def liuyan(request):
    return render(request, 'liuyan.html')


def dayingaijin(request):
    if request.method == 'POST':  # 当提交表单时
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        p = People(name=str(name), email=str(email), comment=str(comment), date=timezone.now())
        p.save()
        return render(request, 'liuyan.html')

    else:  # 当正常访问时
        return render(request, 'liuyan.html')


def upload(request):
    return render(request, 'upload.html')


def upload_file(request):
    if request.method == "POST":    # 请求方法为POST时，进行处理
        myFile = request.FILES.get("myfile", None)    # 获取上传的文件，如果没有文件，则默认为None
        if not myFile:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join("E:/00mypython", myFile.name), 'wb+')    # 打开特定的文件进行二进制的写操作
        for chunk in myFile.chunks():      # 分块写入文件
            destination.write(chunk)
        destination.close()
        return HttpResponse("upload over!")
