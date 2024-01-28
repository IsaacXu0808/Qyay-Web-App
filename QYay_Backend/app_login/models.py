from django.db import models

# Create your models here.
# note: manipulate database

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

class Msg(models.Model):
    context = models.CharField(max_length=3)
    content = models.CharField(max_length=60)
