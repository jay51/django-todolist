from django.db import models

# Create your models here.
class Blog(models.Model):
  title = models.CharField(max_length= 120)
  contnet = models.TextField()
  active = models.BooleanField(default=True)