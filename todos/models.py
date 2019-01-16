from django.db import models
from django.urls import reverse


# Create your models here.
class Todos(models.Model):
    Todo = models.CharField(max_length=120)
    summery = models.TextField(blank=True, null=True)
    done = models.BooleanField(default=False)

    def get_absolute_url(self):
        return f"/todos/{self.id}"  # will return the url with todo.id
        # use reverse to make it dynamic based on the route name
        # return reverse("index", kwargs={"id": self.id})
