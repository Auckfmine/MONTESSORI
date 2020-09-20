from django.db import models



class date(models.Model):
    date = models.DateField(auto_now_add= False)

    father = models.CharField(null=True,blank=True,max_length=255)

    child = models.CharField(null=True,blank=True,max_length=255)

    data1 = models.CharField(null=True,blank=True,max_length=255)
# Create your models here.
