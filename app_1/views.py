import os
from django.shortcuts import render
from django.http import HttpResponse
from .models import People
from django.utils import timezone
from .forms import AddForm
from .code_picture import Hua
from django.http import StreamingHttpResponse
from myweb import settings
import re
# Create your views here.


this_file_name = ''


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
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        comment = request.POST['comment']
        p = People(name=str(name), email=str(email), comment=str(comment), date=timezone.now())
        p.save()
        return render(request, 'liuyan.html')

    else:
        return render(request, 'liuyan.html')


def upload(request):
    return render(request, 'upload.html')


def hua(request):
    path = "E:/00mypython/" + this_file_name
    a = Hua(path, 90, 50, 'e:/00mypython')
    a.hua()
    return HttpResponse('OK')


def file_download(request):
    # do something...
    with open('file_name.txt') as f:
        c = f.read()
    return HttpResponse(c)


def readFile(file_name, chunk_size=512):
    with open(file_name) as f:
        while True:
            c = f.read(chunk_size)
            if c:
                 yield c
            else:
                break


def upload_file(request):
    if request.method == "POST":
        myFile = request.FILES.get("myfile", None)
        if not myFile:
            return HttpResponse("no files for upload!")
        global this_file_name
        this_file_name = myFile.name
        p = os.path.join(settings.BASE_DIR, 'app_1/p_for_code', this_file_name)
        destination = open(p, 'wb+')
        for chunk in myFile.chunks():
            destination.write(chunk)
        destination.close()
        a = Hua(p, 90, 50)
        t = a.hua()
        context = {'hua': t}
        return render(request, 'hua.html', context)



def downloadfile(request):
    filename = 'test.xlsx'
    filepath = "E:/00mypython/" + filename
    response = StreamingHttpResponse(readFile(filepath))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Encoding'] = 'utf-8'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
    return response




