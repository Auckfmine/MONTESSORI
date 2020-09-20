from django.db import models

class Post (models.Model):
    sections = (('petit-section', 'Petit-Section'), ('moyenne-section', 'Moyenne-Section'), ('grand-section', 'Grand-Section'))
    Title = models.CharField(max_length=120, blank=True, null=True)
    image = models.ImageField(upload_to='images/',blank=True,null=True )
    description = models.CharField(max_length=120, blank=True, null=True)
    date = models.DateField(auto_now_add= True)
    section = models.CharField(max_length=25, choices=sections)
    def __str__(self):
        return self.Title