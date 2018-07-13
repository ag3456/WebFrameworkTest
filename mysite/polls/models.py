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
      



# Create your models here.