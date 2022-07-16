import http
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse('<h1>かかかっかか</h1>')

def mypage(request,user_name):
    return HttpResponse(f'<h1>{user_name}様のページです</h1>')

def Sum(request,a,b):
    return HttpResponse(f'<h3>計算結果は{a+b}です</h3>')