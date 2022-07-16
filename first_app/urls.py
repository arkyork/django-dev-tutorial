from django.urls import path
from . import views

app_name='first_app'

urlpatterns=[
    path('hello',views.index,name='index'),
    path('mypage/<str:user_name>',views.mypage,name='mypage'),
    path('sum/<int:a>/<int:b>',views.Sum,name='Sum')
]
