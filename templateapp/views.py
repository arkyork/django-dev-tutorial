from django.shortcuts import render
from bs4 import BeautifulSoup as bs
import requests
import time 
def index(request):
    time.sleep(1)
    res=requests.get('https://www.google.com/search?q=goolge&oq=goolge&aqs=chrome..69i57j0i67i131i433l3j0i10i433j0i67l2j0i10i131i433j0i67l2.1448j0j7&sourceid=chrome&ie=UTF-8')
    soup=bs(res.text)
    h3s=soup.select("h3")
    a=''
    for i in h3s:
        a+=f'{i.text}'
    h3s='k'
    names={'names':'tarohitosi'}
    return render(request,'index.html',context={'key':a,'near':names})

def hero(request):
    name='kaka'
    pc=['ryzen9','rtx3060']
    info={
        "age":25252,
        "kakute":'kakaak'
    }
    return render(request,'base.html',context={'name':name,
    'pc':pc,'info':info})

def sample(request):
    return render(request,'sample.html')

def fil(request):
    name='yamada'
    height=18555
    weight=1500
    bmi=weight/(height/100)**2
    page_url='ホームページ: https://docs.djangoproject.com/ja/4.0/'
    parts=['ryzen3','gtx1660super','memory:64GB']
    msg='hello world'
    num=10
    return render(
        request,
        'filter.html',
        context={
            'name':name,
            'height':height,
            'weight':weight,
            'bmi':bmi,
            'page_url':page_url,
            'parts':parts,
            'msg':msg,
            'st':num
        }
    )