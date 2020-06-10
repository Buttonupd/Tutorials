from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils import timesince

class Tutorial(models.Model):
    title = models.CharField(max_length= 70, blank=False,default='')
    description = models.CharField(max_length = 200, blank=False,default='')
    published =models.BooleanField(default=False)
    tutorial_image = models.ImageField(upload_to='images/', default='')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author', default=True)
    created_on = models.DateTimeField(null=True, blank=True)
    updated_on = models.TimeField(null=True, blank=True)
    editor = models.ForeignKey(User,on_delete=models.CASCADE, default=True) 









    


