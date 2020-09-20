from django.db import models
from student.models import Student


class Absence(models.Model):
    enfant = models.ForeignKey(Student,null = True,blank = True,on_delete=models.CASCADE)
    absence = models.BooleanField(default=False,blank=True,null=True)
    date = models.DateField()
# Create your models here.
