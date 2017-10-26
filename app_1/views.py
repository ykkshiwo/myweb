from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def dayin(request):
    return HttpResponse(request.POST['comment'])


def index(request):
    return render(request, 'index.html')


def liuyan(request):
    return render(request, 'liuyan.html')
