from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize
from app_login.models import Msg
from app_login.models import UserInfo
from app_login.models import Event
# from django.views.decorators.csrf import csrf_exempt
import json
import random
import string

def generate_random_string(length):
    characters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string
 
# Create your views here.
# note: define API
def index(request):
    return HttpResponse("Hello world!")

# @csrf_exempt
def login(request):
    data = json.loads(request.body.decode('utf-8'))
    post_uid = data["uid"]
    post_pw  = data["pw"]
    user_info =  UserInfo.objects.filter(uid = post_uid).first()
    if not user_info:
        return JsonResponse({"findUser": False, "match": False, "uName": None})
    elif post_pw != user_info.password:
        return JsonResponse({"findUser": True, "match": False, "uName": None})
    else:
        return JsonResponse({"findUser": True, "match": True, "uName": user_info.name})
    
def register(request):
    data = json.loads(request.body.decode('utf-8'))
    post_uid = data["uid"]
    post_pw  = data["pw"]
    post_uname = data["uname"]
    user_info =  UserInfo.objects.filter(uid = post_uid).first()
    if user_info:
        return JsonResponse({"Reg_success": False})
    else:
        UserInfo.objects.create(uid = post_uid, name = post_uname, password = post_pw)
        return JsonResponse({"Reg_success": True})

def createEvent(request):
    data = json.loads(request.body.decode('utf-8'))
    post_uid = data["uid"]
    post_uname = data["uname"]
    post_name = data["name"]
    post_dscr = data["discription"]
    post_date = data["date"]
    post_time = data["time"]
    inv_code = generate_random_string(6)
    try:
        Event.objects.create(uid = post_uid,
                            uname = post_uname,
                            ename = post_name,
                            ediscription = post_dscr,
                            edate = post_date,
                            etime = post_time,
                            ivcode = inv_code)
        return JsonResponse({"create_success": True, "ivcode": inv_code})
    except:
        return JsonResponse({"create_success": False})

def getEventList(request):
    data = json.loads(request.body.decode('utf-8'))
    post_uid = data["uid"]
    try:
        res = Event.objects.filter(uid=post_uid).values()
        
        return JsonResponse({"get_event_success": True, "event_list": list(res)})
    except:
        print("here")
        return JsonResponse({"get_event_success": False})



def hello_world(request):
    # where  => filter()
    # delete => delete()
    # create => craeate()
    # update => update()
    # all    => all()

    hw_msg =  Msg.objects.filter(context = 'HLW').first().content
    data = {"msg": hw_msg}
    return JsonResponse(data)