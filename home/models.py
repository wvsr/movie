from distutils import text_file
from django.db import models

# Create your models here.

class Movies(models.Model):
   name = models.CharField(max_length=300, default='')
   url = models.URLField(max_length=200, default='')

   def __str__(self):
       return self.name