from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.core.serializers import serialize
from app_login.models import Msg
from app_login.models import UserInfo
from app_login.models import Event
from app_login.models import Question
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
        new_event = Event.objects.create(uid = post_uid,
                            uname = post_uname,
                            ename = post_name,
                            ediscription = post_dscr,
                            edate = post_date,
                            etime = post_time,
                            ivcode = inv_code)
        return JsonResponse({"create_success": True, "ivcode": inv_code, "eid": new_event.id})
    except:
        return JsonResponse({"create_success": False})

def getEventList(request):
    data = json.loads(request.body.decode('utf-8'))
    post_uid = data["uid"]
    try:
        res = Event.objects.filter(uid=post_uid).values()
        
        return JsonResponse({"get_event_success": True, "event_list": list(res)})
    except:
        return JsonResponse({"get_event_success": False})

def getEvent(request):
    data = json.loads(request.body.decode('utf-8'))
    post_code = data["ivcode"]
    try:
        res = Event.objects.filter(ivcode = post_code).values().first()
        if res:
            return JsonResponse({"found_event": True, "event": res})
        else:
            return JsonResponse({"found_event": False, "event": res})
    except:
        return JsonResponse({"get_event_success": False})
    
def getEvent2(request):
    data = json.loads(request.body.decode('utf-8'))
    post_eid = data["eid"]
    try:
        res = Event.objects.filter(id = post_eid).values().first()
        if res:
            return JsonResponse({"found_event": True, "event": res})
        else:
            return JsonResponse({"found_event": False, "event": res})
    except:
        return JsonResponse({"get_event_success": False})

def activeEvent(request):
    data = json.loads(request.body.decode('utf-8'))
    post_id = data["event_id"]
    try:
        res = Event.objects.filter(id = post_id).first()
        res.start = True
        res.save()
        return JsonResponse({"active_success": True})
    except:
        return JsonResponse({"active_success": False})
    
def terminateEvent(request):
    data = json.loads(request.body.decode('utf-8'))
    post_id = data["event_id"]
    try:
        res = Event.objects.filter(id = post_id).first()
        res.ended = True
        res.save()
        return JsonResponse({"end_success": True})
    except:
        return JsonResponse({"end_success": False})

def submitQue(request): 
    data = json.loads(request.body.decode('utf-8'))
    post_eid = data["eid"]
    post_ctt = data["content"]
    
    try:
        newQ = Question.objects.create(eid=post_eid, content=post_ctt)
        newQ = Question.objects.filter(id = newQ.id).values().first()
        return JsonResponse({"submit_que": True, "new_que": newQ})
    except:
        return JsonResponse({"submit_que": False})
    
def getQueList(request): 
    data = json.loads(request.body.decode('utf-8'))
    post_eid = data["eid"]
    try:
        res = Question.objects.filter(eid = post_eid).values()
        if res:
            return JsonResponse({"get_que": True, "questions": list(res)})
        else:
            return JsonResponse({"get_que": False, "questions": list(res)})
    except:
        return JsonResponse({"get_que": False})

def voteQue(request): 
    data = json.loads(request.body.decode('utf-8'))
    post_qid = data["qid"]
    try:
        res = Question.objects.filter(id = post_qid).first()
        if res:
            res.vote += 1
            res.save()
            return JsonResponse({"vote_success": True})
        else:
            return JsonResponse({"vote_success": True})
    except:
        return JsonResponse({"vote_success": False})

def ansQue(request): 
    data = json.loads(request.body.decode('utf-8'))
    post_qid = data["qid"]
    try:
        res = Question.objects.filter(id = post_qid).first()
        if res:
            res.answered = True
            res.save()
            return JsonResponse({"ans_success": True})
        else:
            return JsonResponse({"ans_success": True})
    except:
        return JsonResponse({"ans_success": False})
    
def hello_world(request):
    hw_msg =  Msg.objects.filter(context = 'HLW').first().content
    data = {"msg": hw_msg}
    return JsonResponse(data)