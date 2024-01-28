from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from app_login.models import Msg

# Create your views here.
# note: define API
def index(request):
    return HttpResponse("Hello world!")

def login(request):
    return HttpResponse("Login page")

def hello_world(request):
    # where  => filter()
    # delete => delete()
    # create => craeate()
    # update => update()
    # all    => all()

    hw_msg =  Msg.objects.filter(context = 'HLW').first().content
    data = {"msg": hw_msg}
    return JsonResponse(data)