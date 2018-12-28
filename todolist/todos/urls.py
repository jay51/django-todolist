# To manage URLs
from django.urls import path

# import the views functions 
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('make/', views.make, name='make'),
]