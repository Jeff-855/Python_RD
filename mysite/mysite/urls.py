"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mysite.views import hello_world,index,hello_world1,post_list1,index1
from blog.views import post_list
from blog.views import test_list
from blog.views import update,delete,crud
from blog.views import getStock,getStockOwnerDetails,getStockOwnerDetails1


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    path('hello1/', hello_world1),
    path('post/', post_list1),
    path('blog/', post_list),
    path('index/', index),
    path('index1/', index1),
    path('', index1),
    path('crud/', crud, name='crud'),
    path('update/<int:pk>/', update, name='Update'),
    path('delete/<int:pk>/', delete, name='Delete'),
    path('getStock/', getStock),
    path('getStockOwnerDetails/', getStockOwnerDetails),
    path('getStockOwnerDetails1/', getStockOwnerDetails1)
]
