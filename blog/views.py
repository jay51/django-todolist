from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import (
  CreateView,
  DeleteView,
  ListView,
  UpdateView,
  DetailView
)

# def index(request):
#   return HttpResponse("<h1>Blog</h1>")
from .models import Blog

# ListView
class BlogListView(ListView):
    # class look for templates in <appname>/<modelname>_list.html.
    # To change template location
    # template_name = "blog/blog_list.html"
    # required attr
    queryset = Blog.objects.all()

