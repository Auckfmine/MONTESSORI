from django.db import models
from django.contrib.auth.models import User
from student.models import Student

# Create your models here.

class Photo(models.Model):
    Photo = models.ImageField(upload_to='images/',blank=True,null=True )
    parent = models.ForeignKey(User, default=1, on_delete=models.CASCADE)
    student = models.ForeignKey(Student,on_delete=models.CASCADE ,default=1)
    def __str__(self):
        return self.student.student_first_name +" " +self.student.student_last_name +"("+ self.student.father_name +")"