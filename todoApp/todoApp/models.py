from django.db import models
from django.contrib.auth.models import User

# Extednding user mode featuers
# https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html
# 1.Proxy Model: model inheritance without creating a new table in the database.
# 2.Using One-To-One Link With a User Model:
# It is a regular Django model that’s gonna have it’s own database table and
# will hold a One-To-One relationship with the existing User Model through a OneToOneField.


# One To
# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)


# Many
class Todo(models.Model):
    todo = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    todo = models.ForeignKey(User, on_delete=models.CASCADE)
