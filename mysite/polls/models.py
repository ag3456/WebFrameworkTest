from django.db import models
from django.utils import timezone
from datetime import datetime

class Question(models.Model):
    pub_date = models.DateTimeField('date published')
    madrigalUrl = models.CharField(max_length=200, default = " ")
    name = models.CharField(max_length=400, default = " ")
    realUrl = models.CharField(max_length =200, default = " ")
    url= models.CharField(max_length=200, default= " ")
    madid = models.IntegerField(default = -1)
    
    def __str__(self):
        return self.name

class ExpListFileNames(models.Model):
    expId = models.IntegerField(default = -1)
    expName = models.CharField(max_length = 200)
    kinddatdesc = models.CharField(max_length = 200)
    question = models.ForeignKey(Question, on_delete = models.CASCADE) #each instance of this information is related to one experiment file
      



# Create your models here.