from django.db import models
from django.utils import timezone
from datetime import datetime

class ExpL(models.Model):
    pub_date = models.DateTimeField('date published')
    madrigalUrl = models.CharField(max_length=200, default = " ")
    name = models.CharField(max_length=400, default = " ")
    realUrl = models.CharField(max_length =200, default = " ")
    url= models.CharField(max_length=200, default= " ")
    madid = models.IntegerField(default = -1)
    
    
    def __str__(self):
        return self.name


class ExpF(models.Model):
    expl = models.ForeignKey(ExpL, on_delete = models.CASCADE) #each instance of this information is related to one experiment file
    expId = models.IntegerField(default = -1)
    expName = models.CharField(max_length = 200)
    kinddatdesc = models.CharField(max_length = 200)

class FilesDwnld(models.Model):
    upload = models.FileField(upload_to = 'media/', max_length=200)


# Create your models here.
