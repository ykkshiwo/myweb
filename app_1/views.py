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
    if request.method == 'POST':  # ���ύ��ʱ
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        p = People(name=str(name), email=str(email), comment=str(comment), date=timezone.now())
        p.save()
        return render(request, 'liuyan.html')

    else:  # ����������ʱ
        return render(request, 'liuyan.html')


def upload(request):
    return render(request, 'upload.html')


def upload_file(request):
    if request.method == "POST":    # ���󷽷�ΪPOSTʱ�����д���
        myFile = request.FILES.get("myfile", None)    # ��ȡ�ϴ����ļ������û���ļ�����Ĭ��ΪNone
        if not myFile:
            return HttpResponse("no files for upload!")
        destination = open(os.path.join("E:/00mypython", myFile.name), 'wb+')    # ���ض����ļ����ж����Ƶ�д����
        for chunk in myFile.chunks():      # �ֿ�д���ļ�
            destination.write(chunk)
        destination.close()
        return HttpResponse("upload over!")
