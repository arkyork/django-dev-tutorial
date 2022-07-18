from django.urls import path
from . import views
app_name='templateapp'
urlpatterns=[
    path('',views.index,name='index'),
    path('intro/',views.hero,name='pc')
]