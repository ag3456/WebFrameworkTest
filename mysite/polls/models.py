from django.db import models
from django.utils import timezone
from datetime import datetime

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    access = models.CharField(max_length = 200, default = " ")
    endday = models.IntegerField(default = 0) 
    endhour = models.IntegerField(default = 0)
    endmin = models.IntegerField(default = 0)
    endmonth = models.IntegerField(default = 0)
    endsec = models.IntegerField(default = 0)
    endyear = models.IntegerField(default = 0)
    madid = models.IntegerField(default = 0)
    instcode = models.IntegerField(default = 0)
    instname = models.CharField(max_length = 200, default = " ")
    
    madrigalUrl = models.CharField(max_length=200, default = " ")
    name = models.CharField(max_length=400, default = " ")
    pi = models.CharField(max_length = 200, default = " ")
    piEmail = models.CharField(max_length=200, default = " ")
    realUrl = models.CharField(max_length =200, default = " ")
    siteid = models.IntegerField(default = 0)
    sitename = models.CharField(max_length=200, default = " ")
    startdate = models.IntegerField(default = 0)
    starthour = models.IntegerField(default = 0)
    startmin = models.IntegerField(default = 0)
    startmonth = models.IntegerField(default = 0)
    startsec = models.IntegerField(default = 0)
    startyear = models.IntegerField(default = 0)
    url= models.CharField(max_length=200, default= " ")
    version= models.CharField(max_length=200, default = " ")

    def __str__ (self):
        return self.access
    def __init__(self, expList):
        self.expList = expList
# Create your models here.
