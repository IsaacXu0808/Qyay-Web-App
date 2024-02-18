"""
URL configuration for QYay_Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app_login import views

urlpatterns = [
    path("index/", views.index),
    path("login/", views.login),
    path("register/", views.register),
    path("createEvent/", views.createEvent),
    path("hello_world/", views.hello_world),
    path("getEventList/", views.getEventList),
    path("getEvent/", views.getEvent),
    path("getEvent2/", views.getEvent2),
    path("activeEvent/", views.activeEvent),
    path("terminateEvent/", views.terminateEvent),
    path("submitQue/", views.submitQue),
    path("getQueList/", views.getQueList),
    path("voteQue/", views.voteQue),
    path("ansQue/", views.ansQue),
]