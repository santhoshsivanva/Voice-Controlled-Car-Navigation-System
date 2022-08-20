"""AIcar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.http.response import HttpResponse
from . import fingerprint
from django.urls import path,include
from django.shortcuts import render
import multiprocessing
from django.conf.urls import handler404, handler500
import os

# p = multiprocessing.Process(target=os.system("python AIcar/fingerprint.py"))
# p.start()

def home(request):    
    return render(request,"index/home.html",{})

urlpatterns = [
    path('',home),
    path('admin/', admin.site.urls),
    path('ai/',include("aimain.urls")),
]


handler404 = 'aimain.views.error_404'
handler500 = 'aimain.views.error_500'