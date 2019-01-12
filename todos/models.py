from django.db import models


# Create your models here.
class Todos(models.Model):
    Todo = models.CharField(max_length=120)
    summery = models.TextField(blank=True, null=True)
    done = models.BooleanField(default=False)
