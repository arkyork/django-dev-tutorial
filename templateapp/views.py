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