from django.db import models

# Create your models here.
# note: manipulate database

class UserInfo(models.Model):
    uid = models.CharField(max_length=16, primary_key=True, default=0)
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

class Msg(models.Model):
    context = models.CharField(max_length=3, unique=True)
    content = models.CharField(max_length=60)

class Event(models.Model):
    uid = models.CharField(max_length=20)
    uname = models.CharField(max_length=14)
    ename = models.CharField(max_length=30)
    ediscription = models.CharField(max_length=200)
    edate = models.DateField(max_length=20)
    etime = models.TimeField(max_length=20)
    ivcode = models.CharField(max_length=6, unique=True)